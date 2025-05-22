# python
# Mock conversation history
conversation_history = []

def mock_chatbot(prompt: str) -> str:
    conversation_history.append({"role": "user", "content": prompt})
    # Mock response based on history
    if "laptop" in prompt.lower():
        response = "I suggest the Dell XPS 13 or Lenovo ThinkPad for programming."
    elif any("gaming" in msg["content"].lower() for msg in conversation_history[:-1]):
        response = "The Dell XPS 13 is decent for light gaming but not ideal for heavy gaming."
    else:
        response = "Sorry, I don't understand the query."
    conversation_history.append({"role": "assistant", "content": response})
    return response

# Test the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = mock_chatbot(user_input)
    print(f"Chatbot: {response}")
