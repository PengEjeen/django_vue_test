from transformers import AutoTokenizer, pipeline

# Model and tokenizer names
base_model_name = "NousResearch/Llama-2-7b-chat-hf"
refined_model_name = "llama-2-7b-mlabonne-enhanced"

# Tokenizer
llama_tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
llama_tokenizer.pad_token = llama_tokenizer.eos_token
llama_tokenizer.padding_side = "right"

# Refined model path
refined_model_path = refined_model_name

# Generate Text
query = "뭐하냐"
text_gen = pipeline(task="text-generation", model=refined_model_path, tokenizer=llama_tokenizer, max_length=200)
output = text_gen(f"<s>[INST] {query} [/INST]")
print(output[0]['generated_text'])
