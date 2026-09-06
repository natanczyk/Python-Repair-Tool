import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig


class CodeLlamaLLM:
    def __init__(
        self,
        model_name: str = "meta-llama/CodeLlama-7b-Instruct-hf",
        max_new_tokens: int = 200,
        temperature: float = 0.2,
        top_p: float = 0.9,
        use_4bit: bool = True,
    ):
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
            )

        print("Loading tokenizer...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        print("Loading model (this may take time)...")
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            torch_dtype=torch.float16,
            quantization_config=quant_config,
        )

    def generate(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=self.max_new_tokens,
            temperature=self.temperature,
            top_p=self.top_p,
            do_sample=True,
        )

        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return result[len(prompt):].strip()