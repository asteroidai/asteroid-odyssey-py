from asteroid_odyssey.client import Odyssey
import os

# Ensure latest version of the public SDK
# Ensure ASTEROID_API_URL=https://api.asteroid.ai/api/v1 in env
base_url = "https://odyssey.asteroid.ai/api/v1"
api_key = ""

client = Odyssey(api_key=api_key, agents_base_url=base_url)

# Define the base job data
base_job_data = {
    "task": """
Get online car insurance quotes for a 2020 Toyota Camry in San Francisco, CA. The full details are: 
Vehicle: Toyota Camry, 2020, VIN optional (if asked) 
Driver: 30 years old, no prior accidents, single, good credit score 
Location: San Francisco, CA, ZIP code 94103 
Coverage: Standard liability coverage with $500 deductible. 
Name: Peter Phillips. 
Date of birth: 1990-01-01, Male, active driver license, no certificate needed, got license when 18 years old, credit score 680, did Bachelor, did not serve in the military. 
I'm employed, car is in storage, never had. 
email: peter.phillips@gmail.com
phone: 415-588-1284
    """
}

# List of insurance sites to check
insurance_urls = [
    "https://autoinsurance5.progressivedirect.com/ApplicationStart.aspx?Page=Create&OfferingID=CA&state=CA&zip=94103&SessionStart=True&Zippaste=1&Qtstatecode=0&progcom_sp=0&progcom_ns=&Product=AU&HQXSupportedBrowser=Y&mvt=off&quoteStartID=87cae6f7-4c16-448e-982f-141d5762ab84&quotesessionid=41abb030-283a-4ef3-86b0-8dcb3180aa99", # Pre-filled the zip code
    "https://www.geico.com/auto-insurance/"
]

# Start all jobs and collect run IDs
run_ids = []
for url in insurance_urls:
    job_data = base_job_data.copy()
    job_data["start_url"] = url
    run_id = client.start(job_data, agent_name="insurance_quote_agent")
    run_ids.append((url, run_id))

# Check results for all jobs
for url, run_id in run_ids:
    try:
        print(f"\nChecking results for {url.split('/')[-1]}")
        result = client.get_final_result(run_id, max_retries=600, retry_delay=1)
        print(f"Result found: {result}")
    except Exception as e:
        print(f"Error getting result for {url}: {str(e)}")
