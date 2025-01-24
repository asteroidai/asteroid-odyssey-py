import os
from asteroid_odyssey import AsteroidClient

client = AsteroidClient(
    api_key=os.getenv("ASTEROID_API_KEY"),
)

# Use the client
client.run("Find the new OpenAI operator blog post")
