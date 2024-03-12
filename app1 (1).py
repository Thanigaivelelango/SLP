import streamlit as st
import spacy
nlp_pos = spacy.load("en_core_web_sm")
nlp_ner = spacy.load("en_core_web_sm")
def pos_tagging(text):
    doc = nlp_pos(text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return pos_tags
def named_entity_recognition(text):
    doc = nlp_ner(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
st.set_page_config(
    page_title="POS and NER Tool",
    page_icon=":mag:",
    layout="centered",
)
st.title("NLP Toolbox")
st.write(
    "A simple tool for Parts Of Speech Tagging and Named Entity Recognition using spaCy."
)
task = st.sidebar.radio("Select Task:", ("POS Tagging", "NER"))
st.header("Input Text")
input_text = st.text_area("Enter your text:")
if st.button("Perform Task"):
    st.spinner("Performing Task...")
    if task == "POS Tagging":
        pos_tags = pos_tagging(input_text)
        st.header("POS Tagging Results")
        st.table(pos_tags)
    else:
        entities = named_entity_recognition(input_text)
        st.header("Named Entity Recognition Results")
        st.table(entities)
