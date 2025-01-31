from asteroid_odyssey.client import Odyssey
import os

# Ensure latest version of the public SDK
# Ensure ASTEROID_API_URL=https://api.asteroid.ai/api/v1 in env
base_url = "https://odyssey.asteroid.ai/api/v1"
api_key = ""

client = Odyssey(api_key=api_key, agents_base_url=base_url)

job_data = {
    "task": """
Get online car insurance quotes for a 2020 Toyota Camry in San Francisco, CA. The full details are: 
Vehicle: Toyota Camry, 2020, VIN optional (if asked) 
Driver: 30 years old, no prior accidents, single, good credit score 
Location: San Francisco, CA, ZIP code 94103 
Coverage: Standard liability coverage with $500 deductible. 
Name: Peter Phillips. 
Date of birth: 1990-01-01, Male, active driver license, no certificate needed, got license when 18 years old, credit score 680, did Bachelor, did not serve in the military. 
I'm employed, car is in storage, never had. 
    """,
    "start_url": "https://www.directauto.com/our-products/auto-insurance"
}

run_id = client.start(job_data, agent_name="insurance_quote_agent")

result = client.get_final_result(run_id, max_retries=600, retry_delay=1)
print(result)

