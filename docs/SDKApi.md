# openapi_client.SDKApi

All URIs are relative to *https://odyssey.asteroid.ai/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_agent**](SDKApi.md#execute_agent) | **POST** /agent/{id} | Execute an agent
[**get_browser_session_recording**](SDKApi.md#get_browser_session_recording) | **GET** /execution/{id}/browser_session/recording | Get browser session recording
[**get_execution_result**](SDKApi.md#get_execution_result) | **GET** /execution/{id}/result | Get execution result
[**get_execution_status**](SDKApi.md#get_execution_status) | **GET** /execution/{id}/status | Get execution status


# **execute_agent**
> ExecutionResponse execute_agent(id, request_body)

Execute an agent

Executes an agent with the provided parameters

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.execution_response import ExecutionResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://odyssey.asteroid.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://odyssey.asteroid.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SDKApi(api_client)
    id = 'id_example' # str | The ID of the agent
    request_body = None # Dict[str, object] | 

    try:
        # Execute an agent
        api_response = api_instance.execute_agent(id, request_body)
        print("The response of SDKApi->execute_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKApi->execute_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the agent | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**ExecutionResponse**](ExecutionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Agent execution started successfully |  -  |
**400** | Invalid request |  -  |
**404** | Agent not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_browser_session_recording**
> BrowserSessionRecordingResponse get_browser_session_recording(id)

Get browser session recording

Retrieves the browser session recording URL for a completed execution

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.browser_session_recording_response import BrowserSessionRecordingResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://odyssey.asteroid.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://odyssey.asteroid.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SDKApi(api_client)
    id = 'id_example' # str | The ID of the execution

    try:
        # Get browser session recording
        api_response = api_instance.get_browser_session_recording(id)
        print("The response of SDKApi->get_browser_session_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKApi->get_browser_session_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the execution | 

### Return type

[**BrowserSessionRecordingResponse**](BrowserSessionRecordingResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Browser session recording retrieved successfully |  -  |
**404** | Browser session not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution_result**
> ExecutionResultResponse get_execution_result(id)

Get execution result

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.execution_result_response import ExecutionResultResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://odyssey.asteroid.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://odyssey.asteroid.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SDKApi(api_client)
    id = 'id_example' # str | The ID of the execution

    try:
        # Get execution result
        api_response = api_instance.get_execution_result(id)
        print("The response of SDKApi->get_execution_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKApi->get_execution_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the execution | 

### Return type

[**ExecutionResultResponse**](ExecutionResultResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Execution result retrieved successfully |  -  |
**404** | Execution not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution_status**
> ExecutionStatusResponse get_execution_status(id)

Get execution status

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.execution_status_response import ExecutionStatusResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://odyssey.asteroid.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://odyssey.asteroid.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SDKApi(api_client)
    id = 'id_example' # str | The ID of the execution

    try:
        # Get execution status
        api_response = api_instance.get_execution_status(id)
        print("The response of SDKApi->get_execution_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SDKApi->get_execution_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the execution | 

### Return type

[**ExecutionStatusResponse**](ExecutionStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Execution status retrieved successfully |  -  |
**404** | Execution not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

