# ExecutionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | The ID of the execution | 

## Example

```python
from openapi_client.models.execution_response import ExecutionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionResponse from a JSON string
execution_response_instance = ExecutionResponse.from_json(json)
# print the JSON string representation of the object
print(ExecutionResponse.to_json())

# convert the object into a dict
execution_response_dict = execution_response_instance.to_dict()
# create an instance of ExecutionResponse from a dict
execution_response_from_dict = ExecutionResponse.from_dict(execution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


