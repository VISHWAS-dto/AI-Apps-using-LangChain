from langchain.messages import SystemMessage , HumanMessage , AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile" , temperature = 0)

messages = [
    SystemMessage(content = "You are a helpful assistant that answers questions about the solar system."),
    HumanMessage(content = "What is the largest planet in our solar system?"),
    AIMessage(content = "The largest planet in our solar system is Jupiter.")
    
]

result = model.invoke(messages)
messages.append(AIMessage(content = result.content))

print(messages)
