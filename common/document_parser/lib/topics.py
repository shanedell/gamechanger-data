from dataScience.models.topic_models.tfidf import bigrams, tfidf_model
from dataScience.src.text_handling.process import topic_processing


def extract_topics(doc_dict):
    """
    This function takes in a document dictionary, checks if it is
    longer than 1 page, and if it is extracts up to 5 topics from
    the text of the document.
    Args:
        doc_dict (dict): A dictionary containing document data.
            Note that `page_count` and `text` must be present in
            the dictionary.
    Returns:
        doc_dict (dict): The output dict differs from the input
            only in that it now includes `topics_rs` as a key.
    """

    doc_dict['topics_rs'] = {}

    if(doc_dict['page_count'] > 1):
        topics = tfidf_model.get_topics(
            topic_processing(doc_dict['text'], bigrams), topn=5)
        for score, topic in topics:
            topic = topic.replace('_', ' ')
            doc_dict['topics_rs'][topic] = score

    return doc_dict
