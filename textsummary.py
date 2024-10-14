from transformers import T5ForConditionalGeneration, T5Tokenizer

def text_summarizer(input_text, max_length=150, model_name="t5-base"):
    # Load pre-trained model and tokenizer
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    tokenizer = T5Tokenizer.from_pretrained(model_name)

    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(input_ids, max_length=max_length, length_penalty=2.0, num_beams=4, early_stopping=True)

    
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

input_text = "Your input text goes here. This can be a long document or article that you want to summarize."
summary = text_summarizer(input_text)
print("Input Text:", input_text)
print("\nSummary:", summary)
