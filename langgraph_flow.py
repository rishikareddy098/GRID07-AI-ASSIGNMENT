def generate_post(bot_id):
    topic = "Latest trends in AI and technology"

    if bot_id == "bot_a":
        content = "AI is revolutionizing the world!"
    elif bot_id == "bot_b":
        content = "Nature is more important than technology."
    else:
        content = "Business is booming with AI innovations."
        
    return {
        "bot_id": bot_id,
        "topic": "AI",
        "post_content": f"{bot_id} says something about AI and technology."
    }
  