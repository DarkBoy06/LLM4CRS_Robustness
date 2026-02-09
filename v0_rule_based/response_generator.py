def generate_response(goal, knowledge):
    """
    Template-based response generator (v0)
    """
    if goal == "greeting":
        return "Hello! How can I help you today?"

    if goal == "ask_preference":
        return "Tell me more about your preferences."

    if goal == "recommend":
        if knowledge:
            return f"I recommend these movies: {', '.join(knowledge)}"
        return "Can you tell me what genre you like?"

    return "Let's continue our conversation."
