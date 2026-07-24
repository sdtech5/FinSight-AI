from graph import run_graph
from langchain_core.messages import HumanMessage

print("Welcome to FinSight AI!")
print("Type 'exit' to quit.\n")

conversation = []

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    conversation.append(HumanMessage(content=question))
    
    conversation = run_graph(conversation)
    
    conversation = conversation[-10:]
    
    print(f"\nFinSight AI: {conversation[-1].content}\n")