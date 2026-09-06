from __future__ import annotations

import torch
from transformers import AutoModelForImageTextToText, AutoProcessor, BitsAndBytesConfig


class Gemma4LLM:
    def __init__(
        self,
        model_name: str = "google/gemma-4-31B-it",
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

        self.processor = AutoProcessor.from_pretrained(model_name, padding_side="left")
        self.model = AutoModelForImageTextToText.from_pretrained(
            model_name,
            device_map="auto",
            dtype=torch.float16,
            quantization_config=quant_config,
        )

    def generate_chat(self, messages: list[dict]) -> str:
        inputs = self.processor.apply_chat_template(
            messages,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
            add_generation_prompt=True,
        ).to(self.model.device)

        input_len = inputs["input_ids"].shape[-1]

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=self.max_new_tokens,
            do_sample=False,
            pad_token_id=self.processor.tokenizer.eos_token_id,
        )

        generated_ids = outputs[0][input_len:]
        return self.processor.decode(generated_ids, skip_special_tokens=True).strip()

    def generate(self, prompt: str) -> str:
        return self.generate_chat([{"role": "user", "content": prompt}])
