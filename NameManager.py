import os
from nltk.tokenize import word_tokenize
from Dictionary import identity_management_dataset
from Util import text_preprocessing

def set_username():
    print("Bot: Hello! What's your name?")
    user_name = input("You: ")
    return user_name


def name_management():
    user_name_file = "user_name.txt"

    if os.path.exists(user_name_file):
        with open(user_name_file, "r") as file:
            user_name = file.read().strip()
    else:
        user_name = set_username()
        with open(user_name_file, "w") as file:
            file.write(user_name)

    return user_name

def get_name(user_input, user_name, threshold):
    processed_input = text_preprocessing(user_input)
    input_tokens = set(word_tokenize(processed_input.lower()))

    identity_question_type = "identity"

    for question, question_type in identity_management_dataset:
        question_tokens = set(word_tokenize(question.lower()))

        # Calculate the Jaccard similarity between input and question tokens
        intersection = len(input_tokens.intersection(question_tokens))
        union = len(input_tokens.union(question_tokens))
        jaccard_similarity = intersection / union

        if jaccard_similarity >= threshold:
            if question_type == identity_question_type:
                return f"Bot: Your name is {user_name}."

    return None

