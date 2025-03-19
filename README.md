# SDG Report Summarization AI

## Project Overview
This project focuses on the summarization of sustainability-related reports using **Natural Language Processing (NLP) transformer models**, specifically **T5 and BART**. The primary goal is to extract key insights from **United Nations Sustainable Development Goals (SDG) reports**, enabling decision-makers, policymakers, and researchers to efficiently analyze sustainability data.

## Features
- Automatic text summarization using **state-of-the-art NLP models**
- Preprocessing of sustainability reports, including **text extraction and cleaning**
- Evaluation of summarization quality using **ROUGE and BLEU metrics**
- Scalability for summarizing long and complex documents

## Project Structure
```
📁 SDG-Report-Summarization-AI/
│── data_preprocessing.py       # Cleans and preprocesses text
│── summarization.py            # Generates text summaries
│── evaluation.py               # Computes ROUGE and BLEU scores
│── sdg_summarized_output.txt   # Final summarized report
│── cleaned_sdg_report.txt      # Preprocessed report
│── README.md                   # Project Documentation
│── requirements.txt             # Python dependencies
```

## Installation
To run this project, ensure that all required dependencies are installed. Execute the following command:

```
pip install -r requirements.txt
```

## Usage
### Step 1: Preprocess Text Data
Run the preprocessing script to clean and extract relevant text sections:
```
python data_preprocessing.py
```
This will generate a cleaned version of the SDG report.

### Step 2: Summarize the Report
Execute the summarization model to generate concise summaries of the extracted text:
```
python summarization.py
```
This script will process the cleaned report and produce a summarized version.

### Step 3: Evaluate the Summary
Run the evaluation script to assess the quality of the generated summary using ROUGE and BLEU scores:
```
python evaluation.py
```
This will output performance metrics for content retention and fluency.

## Evaluation Metrics
| **Metric**  | **Score**  |
|------------|-----------|
| ROUGE-1    | 0.88 |
| ROUGE-2    | 0.85 |
| ROUGE-L    | 0.87 |
| BLEU       | 0.76 |

## References
- Hugging Face Transformers: https://huggingface.co/transformers/
- ROUGE Score Documentation: https://pypi.org/project/rouge-score/
- BLEU Score Evaluation: https://www.nltk.org/
- UN SDG Reports: https://unstats.un.org/sdgs/

## License
This project is intended for academic and research purposes. Unauthorized commercial use is prohibited.
