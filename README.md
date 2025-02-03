**Named Entity Recognition and Summarization Project**

##**Project Overview**

This project combines Named Entity Recognition (NER) and extractive summarization techniques to analyze text data. It is designed to identify key entities in text (e.g., names, dates, locations) and provide concise summaries while maintaining critical information. The project also includes evaluation metrics for NER to assess the system's performance.

##**Applications**

This project can be applied to:

Customer Feedback Analysis: Summarize and extract key entities (e.g., dates, organizations) from customer complaints or reviews.

Legal Document Analysis: Extract critical dates, names, and legal references while summarizing contracts or legal documents.

News Summarization: Highlight important entities (e.g., people, events, locations) from news articles and summarize the content for quick insights.

Healthcare: Extract patient or doctor names, dates, and conditions from medical reports.

##**Key Features**

NER Extraction: Identifies and classifies entities in text using pre-trained SpaCy models.

Extractive Summarization: Uses SpaCy’s PyTextRank for concise summaries.

Performance Evaluation: Compares predicted entities against true entities with precision, recall, and F1-score metrics.

Interactive Visualization: Provides bar charts and highlights entities within summarized text.

##**Workflow**

Data Preprocessing:

Clean and preprocess text data.

Tokenize sentences and words.

Named Entity Recognition (NER):

Extract entities from the original and summarized text using SpaCy.

Extractive Summarization:

Summarize the input text using PyTextRank.

##**Evaluation:**

Compute metrics (precision, recall, F1-score) for entity recognition by comparing true entities and predicted entities.

Visualization:

Highlight entities in summarized text.

Generate bar charts showing NER performance by entity type.

##**How to Run the Application**

Requirements

Python 3.13+

Required libraries:

pandas

spacy

pytextrank

plotly

streamlit

##**Setup**

Clone the repository:

git clone <repository-link>
cd <repository-folder>

Install dependencies:

pip install -r requirements.txt

Download SpaCy language model:

python -m spacy download en_core_web_sm

##**Run the Application**

To run the Streamlit app:

streamlit run app.py

The application will open in your browser. You can input text, process it, and view highlighted summaries and visualized metrics.

##**File Structure**

project-folder/
├── app.py                 # Streamlit application code
├── requirements.txt       # List of dependencies
├── data/                  # Folder for datasets
├── utils.py               # Utility functions for text processing and evaluation
├── README.md              # Project documentation

##**Evaluation Metrics**

The system computes the following for each entity type:

Precision: Percentage of correctly predicted entities out of all predicted entities.

Recall: Percentage of correctly predicted entities out of all true entities.

F1-Score: Harmonic mean of precision and recall.

##**Future Enhancements**

Add More Language Support: Extend the model to handle multilingual text.

Integrate with a Database: Store processed summaries and entities for later retrieval.

Support File Uploads: Allow users to upload documents for batch processing.

Deploy as a Web Application: Use AWS or Heroku for online access.

Improved Summarization: Explore abstractive summarization techniques for better summaries.

##**Acknowledgments**

SpaCy for NER and PyTextRank for summarization.

Streamlit for building the application interface.

##**Contact**

For queries, suggestions, or contributions, feel free to reach out:

Email: wahomeshiko@gmail.com

