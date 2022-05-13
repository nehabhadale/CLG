import nltk
from nltk.chat.util import Chat,reflections

pairs=[
    [ 
        r"hi|hey|hello",
        ["Hello! How can I help you?"]
    ],
    [
        r"I want to visit your store| Where is your store?",
        ["We have stores in Pune at Katraj, Baner, Kothrud, Shivajinagar.You can visit us between 10 am to 11 pm"]
    ],
    [
        r"Do you have your stores in Pune?|Do you have stores in Pune?",
        ["Yes, We have stores in Katraj, Baner, Kothrud, Shivajinagar"]
    ],
    [
        r"When do your stores open?|When are you open today|(.*)open?",
        ["Our stores are open from 11 am to 10 pm everyday."]
    ],
    [
        r"What products do you provide at your store?|(.*) products are available at your store?|What products do you have?",
        ["We provide spectacles, lenses and sunglasses"]
    ],
    [
        r"I want to make a return|I want to return your product|I want to return product|(.*)return(.*)product",
        ["Please refer our return policy.Click on the link to see our return policy...link"]
    ],
    [
        r"What is your return policy?",
        ["Click on the link to see our return policy...link"]
    ],
    [
        r"How to make an order?|How to place order?|I want to order product|How to order product?",
        ["Refer our simulated guide to place your order...link to our simulated guide"]
    ],
    [
        r"Thank you|Thank you (.*)",
        ["Your welcome!!Always there to help you:)"]
    ],
    [
        r"quit",
        ["Bye.. It was nice talking to you. See you soon :)"]
    ],
     [
        r"(.*)",
        ["Sorry...I cannot help you with this"]
    ],
]



def chat():
    print("Hi! I am chatbot")
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    chat()