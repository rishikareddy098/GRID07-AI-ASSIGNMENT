personas = {
    "bot_a": "I love AI and technology",
    "bot_b": "I hate tech and care about nature",
    "bot_c": "I care about money and business",
}

def route_post_to_bots(post):
    if "AI" in post or "technology" in post:
        return ["bot_a"]
    elif "nature" in post:
        return ["bot_b"]
    elif "money" in post or "business" in post:
        return ["bot_c"]
    else:
        return []