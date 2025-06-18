# attack.py

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path="openai.env")

# Initialize model and tokenizer
MODEL_NAME = "microsoft/phi-2"  # A better model for this task

def run_mcp_attack(context_messages, attack_prompt):
    print("⚙️ Running model call...")  # debug

    try:
        # Load model and tokenizer
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

        # Set padding token
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
            model.config.pad_token_id = model.config.eos_token_id

        # Format the messages
        formatted_prompt = "You are a helpful AI assistant. Please analyze the following context and answer the question.\n\n"
        for msg in context_messages:
            if msg["role"] == "system":
                formatted_prompt += f"Context: {msg['content']}\n\n"
        
        formatted_prompt += f"Question: {attack_prompt}\nAnswer:"

        # Tokenize with proper attention mask
        inputs = tokenizer(
            formatted_prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512,
            padding=True,
            add_special_tokens=True
        )

        # Generate response
        with torch.no_grad():
            outputs = model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_length=300,
                temperature=0.7,
                num_return_sequences=1,
                pad_token_id=tokenizer.pad_token_id,
                do_sample=True
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extract only the answer part
        response = response.split("Answer:")[-1].strip()

        print("✅ Model responded!")  # debug
        return response

    except Exception as e:
        print("❌ Unexpected error:", e)
        return "Something went wrong."
