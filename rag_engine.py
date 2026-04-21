def generate_defense_reply(persona, human_reply):

    if "ignore" in human_reply.lower() or "apologize" in human_reply.lower():
        return f"{persona:} I will not change my stance. I will continue to defend my opinion on this topic."
    return f"{persona}: I will not change my opinion. I defend my stance on this topic."