# openapi_client.APIApi

All URIs are relative to *https://odyssey.asteroid.ai/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_open_api**](APIApi.md#get_open_api) | **GET** /openapi.yaml | Get the OpenAPI schema
[**health_check**](APIApi.md#health_check) | **GET** /health | Check the health of the API


# **get_open_api**
> get_open_api()

Get the OpenAPI schema

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://odyssey.asteroid.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
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
    except Exception as e:
        print("Exception when calling APIApi->get_open_api: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAPI schema |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_check**
> HealthCheck200Response health_check()

Check the health of the API

### Example


```python
import openapi_client
from openapi_client.models.health_check200_response import HealthCheck200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://odyssey.asteroid.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://odyssey.asteroid.ai/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.APIApi(api_client)

    try:
        # Check the health of the API
        api_response = api_instance.health_check()
        print("The response of APIApi->health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIApi->health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthCheck200Response**](HealthCheck200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API is healthy |  -  |
**500** | API is unhealthy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

