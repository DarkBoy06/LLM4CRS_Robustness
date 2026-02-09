from .goal_planner import predict_goal
from .knowledge_base import retrieve_knowledge
from .response_generator import generate_response

def chatcrs_pipeline(user_text):
    """
    End-to-end v0 ChatCRS pipeline
    """
    goal = predict_goal(user_text)
    knowledge = retrieve_knowledge(goal, user_text)
    response = generate_response(goal, knowledge)

    return {
        "goal": goal,
        "knowledge": knowledge,
        "response": response
    }
