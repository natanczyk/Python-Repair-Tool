from __future__ import annotations

import re

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


class Qwen3CoderLLM:
    def __init__(
        self,
        model_name: str = "Qwen/Qwen3-Coder-30B-A3B-Instruct",
        max_new_tokens: int = 200,
        temperature: float = 0.2,
        top_p: float = 0.9,
        use_4bit: bool = True,
    ) -> None:
        self.model_name = model_name
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.top_p = top_p

        quant_config = None
        if use_4bit:
            quant_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_use_double_quant=False,
                bnb_4bit_compute_dtype=torch.float16,
            )

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            dtype=torch.float16,
            quantization_config=quant_config,
            # Qwen3-Coder is a MoE model; accelerate's device-map estimator
            # sizes modules at the pre-quantization fp16 footprint (~60GB for
            # 30B params) rather than the actual 4-bit footprint (~15-20GB),
            # so a tight max_memory budget makes it (wrongly) try to spill
            # modules to CPU/disk even though the real quantized model fits
            # easily. Give it enough headroom to satisfy its own inflated
            # estimate instead of restricting it, with a small CPU allowance
            # as a safety net rather than a hard 0 that turns any spill
            # attempt into an immediate crash.
            max_memory={0: "44GiB", 1: "44GiB", "cpu": "4GiB"},
        )

    def generate_chat(self, messages: list[dict]) -> str:
        formatted_prompt = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False,  # disable <think> blocks for cleaner output
        )

        enc = self.tokenizer(formatted_prompt, return_tensors="pt")
        inputs = {k: v.to(self.model.device) for k, v in enc.items()}

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=self.max_new_tokens,
            do_sample=False,
            pad_token_id=self.tokenizer.eos_token_id,
        )

        generated_ids = outputs[0][inputs["input_ids"].shape[1]:]
        response = self.tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
        # Strip any residual <think>...</think> blocks if thinking was not fully disabled
        response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()
        return response

    def generate(self, prompt: str) -> str:
        return self.generate_chat([{"role": "user", "content": prompt}])
