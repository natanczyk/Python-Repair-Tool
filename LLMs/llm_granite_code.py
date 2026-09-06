from __future__ import annotations

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


class GraniteCodeLLM:
    def __init__(
        self,
        model_name: str = "ibm-granite/granite-34b-code-instruct-8k",
        max_new_tokens: int = 200,
        temperature: float = 0.2,
        top_p: float = 0.9,
        use_4bit: bool = True,
        max_input_tokens: int = 7900,
    ) -> None:
        self.model_name = model_name
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.top_p = top_p
        # Granite-code uses GPT-BigCode's learned absolute position embeddings
        # (a fixed-size table, ~8192 for this "-8k" checkpoint), unlike the
        # RoPE-based models elsewhere in this project. Exceeding that length
        # indexes the table out of range and crashes with a CUDA device-side
        # assert instead of degrading gracefully. Repair prompts can get huge
        # when a submission's failing-tests text embeds large literals (e.g.
        # QuixBugs' wrap.py test data), so truncate defensively with headroom
        # left for max_new_tokens.
        self.max_input_tokens = max_input_tokens

        quant_config = None
        if use_4bit:
            quant_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_use_double_quant=False,
                bnb_4bit_compute_dtype=torch.float16,
            )

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name, clean_up_tokenization_spaces=False
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            dtype=torch.float16,
            quantization_config=quant_config,
        )

    def generate_chat(self, messages: list[dict]) -> str:
        formatted_prompt = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )

        enc = self.tokenizer(
            formatted_prompt,
            return_tensors="pt",
            truncation=True,
            max_length=self.max_input_tokens,
        )
        inputs = {k: v.to(self.model.device) for k, v in enc.items()}

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=self.max_new_tokens,
            do_sample=False,
            pad_token_id=self.tokenizer.eos_token_id,
        )

        generated_ids = outputs[0][inputs["input_ids"].shape[1]:]
        return self.tokenizer.decode(generated_ids, skip_special_tokens=True).strip()

    def generate(self, prompt: str) -> str:
        return self.generate_chat([{"role": "user", "content": prompt}])
