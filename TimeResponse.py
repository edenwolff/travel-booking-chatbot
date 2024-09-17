from datetime import datetime
from Dictionary import date_time_dataset
from Util import text_preprocessing

def time_response(user_input):
    processed_input = text_preprocessing(user_input)

    for query_type, patterns in date_time_dataset.items():
        for pattern in patterns:
            if pattern in processed_input:
                if query_type == "current_date":
                    return f"Bot: The current date is {datetime.now().strftime('%Y-%m-%d')}."
                elif query_type == "current_time":
                    return f"Bot: The current time is {datetime.now().strftime('%H:%M:%S')}."
                elif query_type == "today_day":
                    # Get the current day of the week
                    return f"Bot: Today is {datetime.now().strftime('%A')}."

    # Check for specific keywords with relevant context
    if 'date' in processed_input and any(word in processed_input for word in ['what', 'tell', 'today']):
        return f"Bot: The current date is {datetime.now().strftime('%Y-%m-%d')}."
    
    if 'time' in processed_input and any(word in processed_input for word in ['what', 'tell']):
        return f"Bot: The current time is {datetime.now().strftime('%H:%M:%S')}."

    return None
