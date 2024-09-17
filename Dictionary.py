small_talk_dataset = {
    'hi': 'Hello! How can I help you today?',
    'hello': 'Hi there! What can I do for you?',
    'hey': 'Hey! What can I assist you with?',
    'how are you': "I'm just a bot, but thanks for asking!",
    'whats up': 'Not much. How can I assist you?',
    'how are you today': "I'm doing well, thanks! How can I help?",
    'hows it going': 'It\'s going well. What can I do for you?',
    'whats happening':'Not much, I\'m only a bot!',
    'hows the weather': 'I\'m sorry, I don\'t have real-time weather information. You can check a weather website or app for that.',
    'thanks':'No problem at all! I\'m always here for you!',
    'thank you':'Always a pleasure',
    'nice work':'It is my pleasure!', 
    'great work':'Anytime!',
    'cool':'Great Stuff!',
    'thanks for your help':'Pleasure!'
}

travel_dataset = [
    {
        'question': "What are the popular travel destinations in Europe?",
        'answer': "Some popular travel destinations in Europe include Paris, Rome, Barcelona, and Amsterdam."
    },

    {
        'question': "How can I find cheap flights?",
        'answer': "To find cheap flights, you can use online travel agencies, compare prices on multiple websites, and consider flexible travel dates."
    },

    {
        'question': "Where can I travel?",
        'answer': "You can travel to various destinations based on your preferences. Some popular options include beach resorts, historical cities, and natural wonders. Consider your interests and check travel websites for recommendations."
    },

    {
        'question': "What are the must-visit landmarks in New York?",
        'answer': "Must-visit landmarks in New York include the Statue of Liberty, Central Park, Times Square, and the Empire State Building."
    },
    {
        'question': "What documents do I need for flights?",
        'answer': "For flights, you typically need a valid passport, and depending on the destination, a visa. Check the requirements for your specific destination."
    },
    {
        'question': "How can I book a hotel online?",
        'answer': "You can book a hotel online through various platforms like Booking.com, Expedia, or the hotel's official website. Compare prices and read reviews before making a reservation."
    },
    {
        'question': "What is the baggage allowance for international flights?",
        'answer': "Baggage allowances for international flights vary by airline. Check with your airline for specific information on luggage weight and size limits."
    },
    {
        'question': "What are some travel safety tips?",
        'answer': "Some travel safety tips include keeping your valuables secure, being aware of your surroundings, and researching the safety of your destination. Register with your embassy if necessary."
    },]

transaction_dataset = {
    "book_flight": ["flight","book a flight", "reserve a seat", "I want to fly", "get me a plane ticket", "book me a flight", "book a flight from to"],
    "book_train": ["train","book a train", "reserve a seat on a train", "I want to travel by train", "get me a train ticket", "book me a train", "book a train from to", "could you book a train"],
    "rent_car":["rent a car", "rent me a car on holiday", "i need to rent a car", "hire me a car for my holiday", "rent a car for me", "i want to pick up a car", "i want to rent a car", "book me a car", "car rental"]
    }

identity_management_dataset = [
    ("whats my name", "identity"),
    ("tell me my name", "identity"),
    ("can you remember my name", "identity"),
    ("do you know who i am", "identity"),
    ("what am i called", "identity"),
    ("who am i", "identity")
]

discoverability_responses = {
    "help me": "You can ask me about travel booking, including flights, trains and car rentals. If you want to exit, just type 'exit'.",
    "what can i do": "You can inquire about flights, hotels, and general travel information. Type 'exit' to end the chat.",
    "what can you do" : "I'm a travel booking bot here to assist you with your travel-related queries! I can book flights, trains, car rentals & hotels.",
}

date_time_dataset = {
    "current_date": ["what is the current date", "tell me todays date", "whats todays date?"],
    "current_time": ["what is the current time", "tell me the time now", "what time is it"],
    "today_day": ["whats the day today", "tell me todays day", "whats todays day", "what day is it"],
}

booking_action_dataset = {
    "booking_information": ["show booking","show me my booking", "show me booking information", "show me my previous booking", "show my recent booking", "whats my last booking", "can i view my booking"],
    "cancel_booking": ["cancel my booking", "cancel reservation", "change my plans", "i want to cancel", "cancel it", "cancel my flight", "cancel my train", "cancel my flight"],
}