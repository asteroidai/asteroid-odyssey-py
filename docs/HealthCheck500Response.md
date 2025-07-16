# HealthCheck500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | The error message | [optional] 

## Example

```python
from openapi_client.models.health_check500_response import HealthCheck500Response

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheck500Response from a JSON string
health_check500_response_instance = HealthCheck500Response.from_json(json)
# print the JSON string representation of the object
print(HealthCheck500Response.to_json())

# convert the object into a dict
health_check500_response_dict = health_check500_response_instance.to_dict()
# create an instance of HealthCheck500Response from a dict
health_check500_response_from_dict = HealthCheck500Response.from_dict(health_check500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


