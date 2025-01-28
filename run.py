import os
from asteroid_odyssey import Odyssey

odyssey = Odyssey(
    api_key=os.getenv("ASTEROID_API_KEY"),
)

# Use the client
odyssey.start("Find the new OpenAI operator blog post")




