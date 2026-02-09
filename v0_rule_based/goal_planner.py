GOALS = [
    "greeting",
    "ask_preference",
    "recommend",
    "inform"
]

def predict_goal(user_text):
    """
    Rule-based goal prediction (v0)
    """
    text = user_text.lower()

    if "recommend" in text or "suggest" in text:
        return "recommend"
    if "like" in text or "love" in text:
        return "ask_preference"
    if "hello" in text or "hi" in text:
        return "greeting"

    return "inform"
