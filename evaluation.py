import nltk
nltk.download('punkt')
nltk.download('punkt_tab') # Download the missing data

from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import nltk

# ✅ Load summarized output and original text
summary_file = "sdg_summarized_output.txt"
original_file = "cleaned_sdg_report.txt"

with open(original_file, "r", encoding="utf-8") as file:
    original_text = file.read()

with open(summary_file, "r", encoding="utf-8") as file:
    summarized_text = file.read()

# ✅ Compute ROUGE Scores
scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
rouge_scores = scorer.score(original_text, summarized_text)

# ✅ Compute BLEU Score
original_sentences = nltk.sent_tokenize(original_text)[:5]  # Take first few sentences for BLEU reference
summary_sentences = nltk.sent_tokenize(summarized_text)[:5]  # Take first few sentences from summary

# Convert sentences to word tokens
reference = [nltk.word_tokenize(sentence) for sentence in original_sentences]  # Multiple references
candidate = nltk.word_tokenize(" ".join(summary_sentences))  # Summary as candidate

# Compute BLEU score with smoothing
smoothing = SmoothingFunction().method1
bleu_score = sentence_bleu(reference, candidate, smoothing_function=smoothing)

# ✅ Print the Results
print("🔹 ROUGE-1 Score:", rouge_scores["rouge1"].fmeasure)
print("🔹 ROUGE-2 Score:", rouge_scores["rouge2"].fmeasure)
print("🔹 ROUGE-L Score:", rouge_scores["rougeL"].fmeasure)
print("🔹 BLEU Score:", bleu_score)