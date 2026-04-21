personas = {
    "bot_a": "I love AI and technology",
    "bot_b": "I hate tech and care about nature",
    "bot_c": "I care about money and business",
}

def route_post_to_bots(post):
    post = post.lower()  

    matched = []
    if "AI" in post or "technology" in post:
        matched.append("bot_a")
    if"nature" in post:
        matched.append("bot_b")
    if "money" in post or "business" in post:
        matched.append("bot_c")
    
    return matched
