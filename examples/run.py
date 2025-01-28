from asteroid_odyssey.client import Odyssey
import os

api_key = os.getenv("ASTEROID_API_KEY")
base_url = os.getenv("ASTEROID_AGENTS_API_URL") # http://localhost:9090/api/v1

client = Odyssey(api_key=api_key, agents_base_url=base_url)
run_id = client.start("What is the weather in Tokyo?", "default_web")

# Navigate to the platform and ensure that the job is visible

# Wait for the job to complete
result = client.get_final_result(run_id)
print(result)
