## Tokenization
## Corpus -> Documents or Sentence -> Paragraphs
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import os

# Verify and create NLTK data directory if it doesn't exist
nltk_data_dir = '/Users/vmahankali/nltk_data'
if not os.path.exists(nltk_data_dir):
    os.makedirs(nltk_data_dir)

# Set the NLTK data directory
nltk.data.path.append(nltk_data_dir)

# Download the Punkt tokenizer models
nltk.download('punkt', download_dir=nltk_data_dir)
nltk.download('punkt_tab', download_dir=nltk_data_dir)

# Debugging: Check NLTK data path
print("NLTK data path:", nltk.data.path)

# Debugging: Check if Punkt tokenizer models are present
punkt_path = os.path.join(nltk_data_dir, 'tokenizers', 'punkt')
print("Punkt tokenizer path:", punkt_path)
print("Punkt tokenizer files:", os.listdir(punkt_path) if os.path.exists(punkt_path) else "Not found")

corpus="""Hello Welcome, to Vijay NLP Tutorials. 
Please do watch the entire session, to become expert in NLP."""

documents=word_tokenize(corpus, language="english")
print(documents)
type (documents)