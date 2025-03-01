import asyncio
import nest_asyncio
nest_asyncio.apply()    

from transformers import pipeline

qa_pipeline = pipeline('question-answering',model='deepset/roberta-base-squad2')

import json

with open(r'dataset\cs_data.json','r',encoding="utf-8") as f:
    knowledge_base = json.load(f)

cybersecurity_context = " ".join(knowledge_base.values())

import streamlit as st

st.title("Cybersecurity Chatbot")

question = st.text_input("Ask a question: ")

if st.button("Get Answer"):
    if question.strip():
        answer = qa_pipeline(question=question, context=cybersecurity_context)["answer"]
        st.write(f"**Answer:** {answer}")

    else:
        st.warning("Please enter a question.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
            