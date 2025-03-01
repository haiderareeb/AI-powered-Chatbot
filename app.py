import asyncio
import nest_asyncio
nest_asyncio.apply()    

from transformers import pipeline

qa_pipeline = pipeline('question-answering',model='deepset/roberta-base-squad2')

import json

with open('dataset/cs_data.json','r',encoding="utf-8") as f:
    knowledge_base = json.load(f)

cybersecurity_context = " ".join(knowledge_base.values())

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Chatbot API is running!"


@app.route('/chat',methods=["POST"])
def chat():
    """Handles chatbot queries and returns answers from the knowledge base."""
    data = request.get_json()
    question = data.get("question","").strip()

    if not question:
        return jsonify({"error":"No question provided"}), 400
    
    
    answer = qa_pipeline(question = question, context = cybersecurity_context)["answer"]

    return jsonify({"question":question, "answer":answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
            