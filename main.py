from router import route_post_to_bots
from langgraph_flow import generate_post
from rag_engine import generate_defense_reply

post = "New AI model is released"

bots = route_post_to_bots(post)
print("Matched bots:", bots)

for bot in bots:
    result = generate_post(bot)
    print("Generated post:", result)

reply = generate_defense_reply()
print("Defense reply:", reply)