import re

# ✅ Load the processed SDG report
with open("processed_sdg_report.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

# ✅ Function to clean metadata
def clean_text(text):
    # Remove long numbers that might be document references
    text = re.sub(r"\b\d{4,}\b", "", text)  # Removes long numbers (e.g., "202454")
    
    # Remove repetitive bureaucratic terms (e.g., "assembly", "resolution", "session")
    metadata_keywords = r"\b(assembly|resolution|session|agenda|framework|council|preliminary|indicator|goal|forum|highlevel)\b"
    text = re.sub(metadata_keywords, "", text, flags=re.IGNORECASE)
    
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text

# ✅ Apply text cleaning
cleaned_text = clean_text(raw_text)

# ✅ Save cleaned text
with open("cleaned_sdg_report.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)

print("✅ Cleaned SDG report saved as 'cleaned_sdg_report.txt'")
