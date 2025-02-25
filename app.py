import streamlit as st
import spacy
import pandas as pd
import plotly.express as px

# Load NER Model
nlp = spacy.load("en_core_web_sm")

# Function to process text
def process_text(input_text):
    doc = nlp(input_text)
    summary = " ".join([str(sent) for sent in list(doc.sents)[:5]])  # Dummy summary
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return summary, entities

# Highlight Entities
def highlight_entities(summary, entities):
    for entity, label in entities:
        summary = summary.replace(entity, f"[{entity} ({label})]")
    return summary

# Streamlit UI
st.title("NER and Summarization App")
st.write("Upload text or paste it below to extract named entities and summarize.")

# Input Section
input_text = st.text_area("Enter Text Here")
if st.button("Process"):
    if input_text.strip():
        # Process text
        summary, entities = process_text(input_text)
        highlighted_summary = highlight_entities(summary, entities)
        
        # Display Results
        st.subheader("Summarized Text with Highlighted Entities")
        st.markdown(highlighted_summary)
        
        st.subheader("Extracted Entities")
        entity_df = pd.DataFrame(entities, columns=["Entity", "Type"])
        st.dataframe(entity_df)

        st.subheader("Entity Type Distribution")
        entity_counts = entity_df['Type'].value_counts().reset_index()
        entity_counts.columns = ["Entity Type", "Count"]
        fig = px.bar(entity_counts, x="Entity Type", y="Count", title="Entity Distribution")
        st.plotly_chart(fig)
    else:
        st.error("Please enter some text.")
