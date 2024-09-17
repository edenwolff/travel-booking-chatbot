from Dictionary import transaction_dataset
from TravelDatabase import database, cars
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Util import text_preprocessing

booking_info = None

# Match user to input to most similar transaction
def initiate_transaction(user_input, threshold):
    processed_input = text_preprocessing(user_input)

    # Flatten the values in the transaction dataset
    dataset_documents = sum(transaction_dataset.values(), [])
    all_inputs = [processed_input] + dataset_documents

    # Create TF-IDF vectors for user input and dataset
    tfidf_vect = TfidfVectorizer(analyzer="word")
    tfidf_matrix = tfidf_vect.fit_transform(all_inputs)
    cos_similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])

    for key, values in transaction_dataset.items():
        if processed_input in [v for v in values]:
            return key
    
    best_match_index = cos_similarities.argmax()
    best_match_value = dataset_documents[best_match_index]

    if cos_similarities[0][best_match_index] >= threshold:

        # Find the corresponding key for the best match value
        best_match_key = next(key for key, values in transaction_dataset.items() if best_match_value in [v for v in values])
        return best_match_key
    else:
        return None

# Function checks 
def begin_transaction(transaction_type, username):
        if transaction_type == "book_flight":
            return book_flight_conversation(username)
        
        elif transaction_type == "rent_car":
            return rent_car_conversation(username)
        
        elif transaction_type == "book_train":
            return book_train_conversation(username)

def book_flight_conversation(username):
    global booking_info
    print("Bot: Sure! Let's start the flight booking process. Enter 'cancel' at any point to quit transaction.")

    # Initialize variables to store user inputs
    destination = input("Bot: Where would you like to fly?\nYou: ")
    if destination == "cancel":
        return
    
    origin = input("Bot: Where from?\nYou: ")
    if origin == "cancel":
        return

    available_dates = get_available_travel_dates(origin, destination, "flight")

    if not available_dates:
        print(f"Bot: I'm sorry, but I couldn't find any available flights from {origin} to {destination}.")
        return
    
    # Display available dates to the user
    print("Bot: Here are the available dates for flights:")
    for date in available_dates:
        print(f"- {date}")

    # Prompt the user to select a date for booking
    selected_date = input("Bot: Please enter the date of your preferred flight (DD/MM/YYYY): ")
    if selected_date == "cancel":
        return

    # Check if the selected date is valid
    if selected_date in available_dates:
        confirmation = input(f"Bot: I've found a flight on the {selected_date} from {origin} to {destination}. Would you like to confirm your booking? (yes/no)\nYou: ")

        # Keep asking for confirmation until a valid input is provided
        while confirmation.lower() not in ['yes', 'no']:
            print("Bot: Please enter a valid response (yes/no).")
            confirmation = input("User: ")

        if confirmation.lower() == 'yes':
            # Store booking information
            booking_info = {
                'type': 'flight',
                'origin': origin,
                'destination': destination,
                'date': selected_date,
            }
            print(f"Bot: Great news {username}, your booking has been confirmed. Have a great trip!")
        else:
            print("Bot: Your booking has been canceled")
    else:
        print("Bot: Invalid date selected. Please run the booking process again.")

def book_train_conversation(username):
    global booking_info
    print("Bot: Sure! Let's book you a train journey. Enter 'cancel' at any point to quit transaction.")

    # Initialize variables to store user inputs
    destination = input("Bot: Where would you like to travel?\nYou: ")
    if destination == "cancel":
        return
    
    origin = input("Bot: Where from?\nYou: ")
    if origin == "cancel":
        return

    available_dates = get_available_travel_dates(origin, destination, "train")

    if not available_dates:
        print(f"Bot: I'm sorry, but I couldn't find any available trains from {origin} to {destination}.")
        return
    
    # Display available dates to the user
    print("Bot: Here are the available dates for the train journey you requested:")
    for date in available_dates:
        print(f"- {date}")

    # Prompt the user to select a date for booking
    selected_date = input("Bot: Please enter the date of your preferred train ride (DD/MM/YYYY): ")
    if selected_date == "cancel":
        return

    # Check if the selected date is valid
    if selected_date in available_dates:
        confirmation = input(f"Bot: I've found a train on the {selected_date} from {origin} to {destination}. Would you like to confirm your booking? (yes/no)\nYou: ")

        # Keep asking for confirmation until a valid input is provided
        while confirmation.lower() not in ['yes', 'no']:
            print("Bot: Please enter a valid response (yes/no).")
            confirmation = input("User: ")

        if confirmation.lower() == 'yes':
            # Store booking information
            booking_info = {
                'type': 'train',
                'origin': origin,
                'destination': destination,
                'date': selected_date,
            }
            print(f"Bot: Great news {username}, your booking has been confirmed. Have a great trip!")
        else:
            print("Bot: Your booking has been canceled")
    else:
        print("Bot: Invalid date selected. Please run the booking process again.")
    

def rent_car_conversation(username):
    # Start car rental process
    global booking_info
    print("Bot: Sure! Let's book you a car rental. Enter 'cancel' at any point to quit transaction.")

    location = input("Bot: Where would you like to rent a car?\nYou: ")
    if location == "cancel":
        return

    date = input("Bot: When would you like to pick up the car?\nYou: ")
    if date == "cancel":
        return

    available_cars = get_available_cars(location, date)

    if not available_cars:
        print(f"Bot: I'm sorry, but I couldn't find any available cars in {location} on the {date}.")
        return
    
    # Display available dates to the user
    print("Bot: Here are the available cars in the location and date you requested:")
    for car in available_cars:
        print(f"- {car}")

    # Prompt the user to select a date for booking
    selected_car = input("Bot: Please enter the car you wish to rent.\nYou: ")
    if selected_car.lower() == "cancel":
        return

    # Check if the selected date is valid
    if selected_car.lower() in available_cars:
        confirmation = input(f"Bot: You selected an {selected_car} on {date}. Would you like to confirm?(yes/no)\nYou: ")

        # Keep asking for confirmation until a valid input is provided
        while confirmation.lower() not in ['yes', 'no']:
            print("Bot: Please enter a valid response (yes/no).")
            confirmation = input("User: ")

        if confirmation.lower() == 'yes':
            print(f"Bot: Great news {username}, your car rental has been confirmed. Have a great drive!")
        else:
            print("Bot: Your car rental booking has been canceled")
    else:
        print("Bot: Unavailable car selected. Please run the booking process again.")


# Function to retrieve available dates for flights
def get_available_travel_dates(origin, destination, travel_type):
    available_dates = []

    for details in database.values():
        if (
            details['type'] == travel_type
            and details['origin'].lower() == origin.lower()
            and details['destination'].lower() == destination.lower()
        ):
            available_dates.append(details['date'])

    return available_dates

# Find available cars at the location on the date
def get_available_cars(location, date):
    available_cars = []

    for details in cars.values():
        if (
            details['location'] == location.lower()
            and details['date'] == date.lower()
        ):
            available_cars.append(details['brand'])

    return available_cars

# Function cancels booking
def cancel_booking(booking):
    booking['type'] = None
    booking['origin'] = None
    booking['destination'] = None
    booking['date'] = None
    print("Bot: I've canceled your booking! Is there anything else I can do for you?")
