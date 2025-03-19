from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# ✅ Load the T5 Model
model_name = "t5-small"  # Optionally, use "facebook/bart-large-cnn" for better results
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# ✅ Load the cleaned text file
input_file_path = "cleaned_sdg_report.txt"
with open(input_file_path, "r", encoding="utf-8") as file:
    text = file.read()

# ✅ Summarization function with improved parameters
def generate_summary(text, max_input_length=512, max_output_length=100):
    inputs = tokenizer("summarize: " + text, return_tensors="pt", max_length=max_input_length, truncation=True)
    summary_ids = model.generate(
        inputs.input_ids, 
        max_length=max_output_length, 
        min_length=50, 
        length_penalty=3.0, 
        num_beams=5, 
        repetition_penalty=2.5, 
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# ✅ Process text in chunks to fit model limits
chunk_size = 500  # Reduce chunk size to avoid redundant summaries
summaries = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i+chunk_size]
    summary = generate_summary(chunk)
    summaries.append(summary)

# ✅ Combine all summaries
final_summary = "\n".join(summaries)

# ✅ Save the improved summary
output_file_path = "sdg_summarized_output.txt"
with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(final_summary)

print("✅ Summarization complete! Summary saved to", output_file_path)
