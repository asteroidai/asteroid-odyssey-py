# ExecutionStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | The ID of the execution | 
**status** | [**Status**](Status.md) |  | 
**reason** | **str** | Reason for the current status (if applicable) | [optional] 
**updated_at** | **datetime** | Time when the status was last updated | [optional] 

## Example

```python
from openapi_client.models.execution_status_response import ExecutionStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionStatusResponse from a JSON string
execution_status_response_instance = ExecutionStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ExecutionStatusResponse.to_json())

# convert the object into a dict
execution_status_response_dict = execution_status_response_instance.to_dict()
# create an instance of ExecutionStatusResponse from a dict
execution_status_response_from_dict = ExecutionStatusResponse.from_dict(execution_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


