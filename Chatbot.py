from SmallTalk import small_talk
from TimeResponse import time_response
from NameManager import name_management, get_name
import Transactions
from Transactions import initiate_transaction, begin_transaction, cancel_booking
from Discoverability import discoverability_response
from InformationRetrieval import get_booking_action, show_booking_info, answer_query

def main():

    user_name = name_management()

    print(f"Bot: Hello {user_name}! I'm your travel booking bot, how can I help you today? Type in exit to quit chat.")
    while True:
            user_input = input("You: ")

            if user_input.lower() == 'exit':
                print("Bot: Goodbye!")
                break

            # Check for discoverability questions
            discoverability_reply = discoverability_response(user_input, 0.7)

            if discoverability_reply:
                print(f"Bot: {discoverability_reply}")

            else:
                    
                # Check if the user wants to change the name
                if "change" in user_input.lower() and "name" in user_input.lower():
                    new_name = input("Bot: Sure! What would you like your new name to be?\nYou: ")

                    # Update the name in the file
                    with open("user_name.txt", "w") as file:
                        file.write(new_name)

                    print(f"Bot: Your name has been updated to {new_name}.")
                    user_name = new_name

                else:
                    query_response = answer_query(user_input, 0.5)
                    if query_response:
                        print(f"Bot: {query_response}")
                    else:

                        # Check for date and time questions
                        date_time_response = time_response(user_input)
                        if date_time_response:
                            print(date_time_response)

                        else:
                            # Check for identity related responses
                            identity_response = get_name(user_input, user_name, 0.6)
                            if identity_response:
                                print(identity_response)

                            else:

                                small_talk_response = small_talk(user_input, 0.6)
                                
                            # Check for small talk
                                if small_talk_response:
                                    print(f"Bot: {small_talk_response}")
                                else:
                                    # User response is initiate a transaction, 
                                    # need to match it to speceific transaction type in dataset
                                    transaction_response = initiate_transaction(user_input, 0.5)
                                    if transaction_response:
                                        begin_transaction(transaction_response, user_name)
                                    else:
                                        # Check for actions on existing booking
                                        booking_action = get_booking_action(user_input, 0.5)
                                        if booking_action:
                                            if Transactions.booking_info:
                                                if Transactions.booking_info["type"] != None:
                                                    if booking_action == 'booking_information':
                                                        show_booking_info(Transactions.booking_info)

                                                if booking_action == 'cancel_booking':
                                                    user_response = input(f"Bot: {user_name}, are you sure you wish to cancel your booking? Please confirm. (yes/no)\nYou: ")

                                                    while user_response.lower() not in ['yes', 'no']:

                                                        print("Bot: Please enter a valid response (yes/no).")
                                                        user_response = input("User: ")
                                                    if user_response.lower() == 'yes':
                                                        cancel_booking(Transactions.booking_info)
                                                    else:
                                                        print("Bot: Glad to see you've kept your booking! Is anything else I can help with?")

                                            else:
                                                # Ask user if they want to start a transactions
                                                user_response = input("Bot: No recent booking has been made! Would you like to start a new transaction? (yes/no)\nYou: ")
                                                while user_response.lower() not in ['yes', 'no']:
                                                    print("Bot: Please enter a valid response (yes/no).")
                                                    user_response = input("User: ")
                                                
                                                if user_response.lower() == 'yes':
                                                    booking_type = input("Bot: Great! Which type of booking would you like to make?\nYou: ")
                                                    booking_response = initiate_transaction(booking_type, 0.7)

                                                    if booking_response:
                                                        begin_transaction(booking_response, user_name)
                                                    else:
                                                        print(f"Bot: Sorry {user_name}, I cannot perform the type of booking you requested.")

                                                else:
                                                    print("Bot: No Problem! Is there anything else I can do for you?")


                                        # Error handling
                                        else:
                                            print("Bot: I'm not sure how to respond to that. Can you please provide more information?")

    
if __name__ == "__main__":
    main()
