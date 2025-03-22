import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Hey! How can I assist you?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great, thanks for asking!", "All good here, how about you?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot. You can call me ChatBot.", "I go by the name ChatBot.", "I'm ChatBot, your virtual assistant."]
    ],
    [
        r"what can you do ?",
        ["I can chat with you, answer simple questions, and help you with basic tasks.", "I'm here to have conversations and assist you with information."]
    ],
    [
        r"quit|bye|exit",
        ["Goodbye! Have a great day!", "Bye! Take care!", "See you later!"]
    ],
    [
        r"my name is (.*)",
        ["Hello %1! How can I help you today?", "Nice to meet you, %1! What can I do for you?"]
    ],
    [
        r"i need (.*)",
        ["Why do you need %1?", "How can I help you with %1?", "What do you need %1 for?"]
    ],
    [
        r"i feel (.*)",
        ["Why do you feel %1?", "What's causing you to feel %1?", "Tell me more about why you feel %1."]
    ],
    [
        r"can you help me (.*)",
        ["Sure, I can help you with %1. What do you need?", "Of course! What do you need help with regarding %1?"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"]
    ],
    [
        r"what is (.*) ?",
        ["%1 is a topic I'm still learning about. Can you be more specific?", "I'm not sure about %1. Could you provide more details?"]
    ],
    [
        r"how old are you ?",
        ["I'm just a program, so I don't have an age!", "I'm ageless, but I was created recently."]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem!", "Glad to help!"]
    ],
    [
        r"default",
        ["I'm not sure I understand. Can you rephrase that?", "I didn't get that. Could you say it again?", "Sorry, I don't follow. Can you clarify?"]
    ]
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm your friendly chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

# Start the chatbot
start_chat()
