from asteroid_odyssey.client import Odyssey

# export ASTEROID_API_URL=https://api.asteroid.ai/api/v1
# export ASTEROID_API_KEY=astiyeHrSLulaJi0IwrR1cX1tDohfOgnYN5LViKYix4hMlpary8pYBom5k1B3qOZ
# export ASTEROID_AGENTS_API_URL=https://odyssey.asteroid.ai/api/v1


client = Odyssey(
    api_key="",
    # agents_base_url=base_url, 
    # platform_base_url=platform_base_url
)

job_data = {
    "task": "Get insurance quotes for a Honda Accord 2003 Coupe in San Francisco, CA",
    "customer_details": """Name: Peter Phillips.
Date of birth: 1990-01-01, Male, active driver license, no certificate needed, got license when 18 years old, credit score 680, did Bachelor, did not serve in the military. 
Email: peter.phillips@gmail.com
Phone: 415-581-2338
Home address: 3648 20th St, San Francisco, CA, 94102
License at 16
Bachelors Degree

Vehicle: Honda Accord, 2003, VIN is 1HGCM82633A123456, Coupe
Vehicle details: 
- 2003 Honda Accord Coupe
- 2.0L 4-cylinder engine
- 5-speed automatic transmission
- 100,000 miles
Current insurer is 21st Century, insured for 8 months
Have had the car for 1 year
Bodily injury limits currently $40k
Driver: 30 years old, no prior accidents, single, good credit score 
Coverage: Standard liability coverage with $500 deductible.
Employed, car is in storage, never had an accident.
New policy start date as of 2025-02-08""",
    "start_url": "https://customer.directauto.com/AutoInsurance/Client/DGClientInfo?INTCID=DirectAuto%2FFE%2Fhome%7CPromotionQuoteHero%7CQuote%7CAu"
}

run_id = client.start(job_data, agent_name="insurance_quote_agent")

result = client.get_final_result(run_id, max_retries=600, retry_delay=1)

print(result)

