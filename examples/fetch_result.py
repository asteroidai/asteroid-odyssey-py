from asteroid_odyssey.client import Odyssey

# Ensure latest version of the public SDK
# Ensure ASTEROID_API_URL=https://api.asteroid.ai/api/v1 in env
base_url = "https://odyssey.asteroid.ai/api/v1"
api_key = ""

client = Odyssey(api_key=api_key, agents_base_url=base_url)

# Successful run (requires founders@asteroid.ai key)
result = client.get_final_result("7b1e3475-2afe-4736-9f5c-964ffa930c16", max_retries=600, retry_delay=1)
print(result)
