from transformers import pipeline, set_seed


generator = pipeline("text-generation", model="gpt2")

have_question = True
print("Ask your question:")
while have_question:
    question = input()
    print(f"You: {question}")
    text = generator(question, max_length=30)
    print(f"Bot: {text}")
    
