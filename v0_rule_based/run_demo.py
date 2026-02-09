from pipeline import chatcrs_pipeline

if __name__ == "__main__":
    user_input = "Can you recommend a good sci-fi movie?"
    output = chatcrs_pipeline(user_input)

    print("Goal:", output["goal"])
    print("Knowledge:", output["knowledge"])
    print("Response:", output["response"])
