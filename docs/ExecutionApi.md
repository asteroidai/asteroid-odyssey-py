# openapi_client.ExecutionApi

All URIs are relative to *https://odyssey.asteroid.ai/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_execution_files**](ExecutionApi.md#upload_execution_files) | **POST** /execution/{id}/files | Upload files to an execution


# **upload_execution_files**
> UploadExecutionFiles200Response upload_execution_files(id, files=files)

Upload files to an execution

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.upload_execution_files200_response import UploadExecutionFiles200Response
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
    api_instance = openapi_client.ExecutionApi(api_client)
    id = 'id_example' # str | The ID of the execution
    files = None # List[bytearray] | Files to upload to the execution (optional)

    try:
        # Upload files to an execution
        api_response = api_instance.upload_execution_files(id, files=files)
        print("The response of ExecutionApi->upload_execution_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionApi->upload_execution_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the execution | 
 **files** | **List[bytearray]**| Files to upload to the execution | [optional] 

### Return type

[**UploadExecutionFiles200Response**](UploadExecutionFiles200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Files uploaded successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Execution not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

