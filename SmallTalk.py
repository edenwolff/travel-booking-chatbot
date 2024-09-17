from Dictionary import small_talk_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Util import text_preprocessing


def small_talk(user_input, threshold):
    processed_input = text_preprocessing(user_input)

    # Construct array of all small talk questions
    small_talk_questions = list(small_talk_dataset.keys())
    all_inputs = [processed_input] + small_talk_questions

    tfidf_vect = TfidfVectorizer(analyzer="word")
    tfidf_matrix = tfidf_vect.fit_transform(all_inputs)
    cos_similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])
    most_similar_index = cos_similarities.argmax()

    if cos_similarities[0][most_similar_index] >= threshold:
        most_similar_question = small_talk_questions[most_similar_index]
        response = small_talk_dataset[most_similar_question]
    else:
        response = None

    return response



    









    