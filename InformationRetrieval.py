from Util import text_preprocessing
from Dictionary import booking_action_dataset, travel_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function that handles actions for existing booking - show info, cancel...
def get_booking_action(user_input, threshold):

    processed_input = text_preprocessing(user_input)

     # Flatten the values in the transaction dataset
    dataset_documents = sum(booking_action_dataset.values(), [])
    all_inputs = [processed_input] + dataset_documents

    # Create TF-IDF vectors for user input and dataset
    tfidf_vect = TfidfVectorizer(analyzer="word")
    tfidf_matrix = tfidf_vect.fit_transform(all_inputs)
    cos_similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])

    for key, values in booking_action_dataset.items():
        if processed_input in [v for v in values]:
            return key
    
    best_match_index = cos_similarities.argmax()
    best_match_value = dataset_documents[best_match_index]

    if cos_similarities[0][best_match_index] >= threshold:

        # Find the corresponding key for the best match value
        best_match_key = next(key for key, values in booking_action_dataset.items() if best_match_value in [v for v in values])
        return best_match_key
    else:
        return None
    
def answer_query(user_input, threshold):

    # Extract questions from the dataset
    questions = [item['question'] for item in travel_dataset]

    # Add the user input to the questions
    questions.append(user_input)

    # Vectorize the questions using TfidfVectorizer
    vectorizer = TfidfVectorizer(analyzer="word")
    question_vectors = vectorizer.fit_transform(questions)

    # Calculate cosine similarity between user input and each question
    similarities = cosine_similarity(question_vectors[-1], question_vectors[:-1])

    # Find the index of the most similar question
    most_similar_index = similarities.argmax()

    # Get the similarity score
    similarity_score = similarities[0, most_similar_index]

    # Check if the similarity score is above the threshold
    if similarity_score >= threshold:
        # Retrieve the corresponding answer
        answer = travel_dataset[most_similar_index]['answer']
    else:
        answer = None

    return answer


def show_booking_info(booking):
    print(f"Bot: Here's your booking info:\nType of travel: {booking['type']}, Date: {booking['date']}, Origin: {booking['origin']}, Destination: {booking['destination']}")
