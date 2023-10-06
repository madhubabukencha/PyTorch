"""
You have to pass context to ask questions
"""
from transformers import pipeline

# colors
GREEN = '\033[92m'
BLUE = '\033[94m'
END = '\033[0m'

que_ans = pipeline("question-answering",
                   model="distilbert-base-uncased-distilled-squad")
context = "Madhu have a friend called Kiran. He is a good person. Kiran is an artist. Madhu is a Artifical Intelligence Engineer."
while True:
    question = input(f"{BLUE}Question: {END}")
    result = que_ans(question=question, context=context)
    print(f"{GREEN}Answer: {END}{result['answer']}")
