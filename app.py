from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Define your intents dictionary
intents = {
    "intents": [
        {
            "student": ["Hi", "How are you", "Is anyone there?", "Hello", "Good day"],
            "cre": ["Hello, thanks for visiting", "Good to see you again", "Hi there, how can I help?"]
        },
        {
            "student": ["Bye", "See you later", "Goodbye"],
            "cre": ["See you later, thanks for visiting", "Have a nice day", "Bye! Come back again soon."]
        },
        {
            "student": ["Thanks", "Thank you", "That's helpful"],
            "cre": ["Happy to help!", "Any time!", "My pleasure"]
        },
        {
            "student": ["How to join in workshop?",  "How to apply the workshop?", "When and where is the workshop taking place?", "What are the registration requirements?", "How can I register for the workshop?", "How can I get more information or contact the organizers?"],
            "cre": ["We will guide you through a link to apply or call: 7358119288", "You can apply by following the link or contacting 7358119288"]
        },
        {
            "student": ["Are there any additional fees or charges?", "Is there a payment deadline?", "Is there a minimum payment amount?", "Is there a registration fee?"],
            "cre": ["The workshop is free to join."]
        },
        {
            "student": ["What time does the event start and end?", "Will there be reminders or notifications before the event?", "What is the time and date for the event?", "Is the timing flexible?", "When is the event scheduled?", "What are your hours today?"],
            "cre": ["The event will be from 11am to 1pm."]
        },
        {
            "student": ["Will there be reminders before the event?", "When will I get notifications before the event?"],
            "cre": ["Yes, you will receive reminders before the event."]
        },
        {
            "student": ["Will I get a certificate after completing the workshop?", "If I have complaints or doubts?"],
            "cre": ["Yes, you will receive a certificate, but it may take some time."]
        },
        {
            "student": ["Contact number for complaints?", "I have doubts, how can I reach you?"],
            "cre": ["Kayal-7358119288", "Inba-7358114288"]
        }
    ]
}

# Function to handle user input and provide appropriate response
def get_response(user_input):
    user_input = user_input.lower()
    for intent in intents['intents']:
        for pattern in intent['student']:
            if pattern.lower() in user_input:
                return random.choice(intent['cre'])
    return "Sorry, I'm not sure how to respond to that."

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
