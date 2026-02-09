KNOWLEDGE_BASE = {
    "action": ["John Wick", "Mad Max: Fury Road", "The Dark Knight"],
    "sci-fi": ["Interstellar", "Inception", "Blade Runner 2049"],
    "romance": ["Before Sunrise", "Titanic"],
    "comedy": ["Superbad", "The Hangover"]
}

def retrieve_knowledge(goal, user_text):
    """
    Simple keyword-based knowledge retrieval (v0)
    """
    if goal != "recommend":
        return []

    text = user_text.lower()
    for genre in KNOWLEDGE_BASE:
        if genre in text:
            return KNOWLEDGE_BASE[genre]

    return []
