# Asteroid Odyssey

The official Python SDK for interacting with the Asteroid Agents API.

## Installation

```bash
pip install asteroid-odyssey
```

## Usage

Please head to our documentation at https://docs.asteroid.ai/sdk/python

## License

The Asteroid Odyssey SDK is available under the MIT License.

### Tests

Execute `pytest` to run the tests.

## Getting Started

The SDK provides a high-level `AsteroidClient` class that makes it easy to interact with the Asteroid Agents API:

```python
from asteroid_odyssey import AsteroidClient

# Create a client with your API key
client = AsteroidClient('your-api-key')

# Execute an agent
execution_id = client.execute_agent('my-agent-id', {'input': 'some dynamic value'})

# Wait for the execution to complete and get the result
result = client.wait_for_execution_result(execution_id)
print(result)

# Or check status manually
status = client.get_execution_status(execution_id)
print(f"Status: {status.status}")

# Upload files to an execution
hello_content = "Hello World!".encode()
response = client.upload_execution_files(execution_id, [hello_content])
print(f"Uploaded files: {response.file_ids}")

# Get browser session recording (for completed executions)
recording_url = client.get_browser_session_recording(execution_id)
print(f"Recording available at: {recording_url}")
```

### Context Manager Usage

The client can also be used as a context manager:

```python
from asteroid_odyssey import AsteroidClient

with AsteroidClient('your-api-key') as client:
    execution_id = client.execute_agent('my-agent-id', {'input': 'test'})
    result = client.wait_for_execution_result(execution_id)
    print(result)
```

### Convenience Functions

The SDK also provides convenience functions:

```python
from asteroid_odyssey import create_client, execute_agent, wait_for_execution_result

client = create_client('your-api-key')
execution_id = execute_agent(client, 'my-agent-id', {'input': 'test'})
result = wait_for_execution_result(client, execution_id)
```

## API Reference

### AsteroidClient

The main client class provides the following methods:

- `execute_agent(agent_id, agent_profile_id, execution_data)` - Execute an agent and return execution ID
- `get_execution_status(execution_id)` - Get current execution status
- `get_execution_result(execution_id)` - Get final execution result
- `wait_for_execution_result(execution_id, interval=1.0, timeout=3600.0)` - Wait for completion
- `upload_execution_files(execution_id, files, default_filename="file.txt")` - Upload files
- `get_browser_session_recording(execution_id)` - Get browser recording URL

### Low-Level API Access

If you need direct access to the generated OpenAPI client, you can still use it:

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://odyssey.asteroid.ai/api/v1
configuration = openapi_client.Configuration(
    host = "https://odyssey.asteroid.ai/api/v1"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.APIApi(api_client)

    try:
        # Get the OpenAPI schema
        api_instance.get_open_api()
    except ApiException as e:
        print("Exception when calling APIApi->get_open_api: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://odyssey.asteroid.ai/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APIApi* | [**get_open_api**](docs/APIApi.md#get_open_api) | **GET** /openapi.yaml | Get the OpenAPI schema
*APIApi* | [**health_check**](docs/APIApi.md#health_check) | **GET** /health | Check the health of the API
*ExecutionApi* | [**upload_execution_files**](docs/ExecutionApi.md#upload_execution_files) | **POST** /execution/{id}/files | Upload files to an execution
*SDKApi* | [**execute_agent**](docs/SDKApi.md#execute_structured_agent) | **POST** /agent/{id} | Execute an agent
*SDKApi* | [**get_browser_session_recording**](docs/SDKApi.md#get_browser_session_recording) | **GET** /execution/{id}/browser_session/recording | Get browser session recording
*SDKApi* | [**get_execution_result**](docs/SDKApi.md#get_execution_result) | **GET** /execution/{id}/result | Get execution result
*SDKApi* | [**get_execution_status**](docs/SDKApi.md#get_execution_status) | **GET** /execution/{id}/status | Get execution status


## Documentation For Models

 - [BrowserSessionRecordingResponse](docs/BrowserSessionRecordingResponse.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ExecutionResponse](docs/ExecutionResponse.md)
 - [ExecutionResult](docs/ExecutionResult.md)
 - [ExecutionResultResponse](docs/ExecutionResultResponse.md)
 - [ExecutionStatusResponse](docs/ExecutionStatusResponse.md)
 - [HealthCheck200Response](docs/HealthCheck200Response.md)
 - [HealthCheck500Response](docs/HealthCheck500Response.md)
 - [Status](docs/Status.md)
 - [UploadExecutionFiles200Response](docs/UploadExecutionFiles200Response.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-Asteroid-Agents-Api-Key
- **Location**: HTTP header

## Regenerating the SDK

To update the SDK, regenerate the code by running

```bash
 npx @openapitools/openapi-generator-cli generate \
  -i https://odyssey.asteroid.ai/api/v1/openapi.yaml \
  -g python \
  -o . 

 ```

After generation, ensure `pyproject.toml` is configured correctly and that files are modified correctly. Check for new files and if they are needed.





