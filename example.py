import os
from asteroid_odyssey import AsteroidClient

# Set up client
api_key = os.getenv('ASTEROID_API_KEY')
if api_key is None:
    raise ValueError('ASTEROID_API_KEY is not set')
client = AsteroidClient(api_key)

# Execute agent and wait for result
execution_id = client.execute_agent('agent_id', {'input': 'data'})

# Upload files to an execution
with open('hello.txt', 'r') as f:
    file_content = f.read().encode()
response = client.upload_execution_files(execution_id, [file_content])
print(f"Uploaded files: {response.file_ids}")
result = client.wait_for_execution_result(execution_id)
recording_url = client.get_browser_session_recording(execution_id)
print(f"Recording available at: {recording_url}")
print(result)