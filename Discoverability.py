from Dictionary import discoverability_responses
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Util import text_preprocessing

# Find most similar discoverability response to user input
def discoverability_response(user_input, threshold):
    processed_input = text_preprocessing(user_input)

    # Construct array of all small talk questions
    discoverability_questions = list(discoverability_responses.keys())
    all_inputs = [processed_input] + discoverability_questions

    tfidf_vect = TfidfVectorizer(analyzer="word")
    tfidf_matrix = tfidf_vect.fit_transform(all_inputs)
    cos_similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])
    most_similar_index = cos_similarities.argmax()

    if cos_similarities[0][most_similar_index] >= threshold:
        most_similar_question = discoverability_questions[most_similar_index]
        response = discoverability_responses[most_similar_question]
    else:
        response = None

    return response