# ExecutionResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | The ID of the execution | 
**status** | [**Status**](Status.md) |  | 
**result** | **Dict[str, object]** | (Deprecated, use execution_result instead) The structured result data from the execution. Contains the outcome, reasoning, final answer, and result. | [optional] 
**error** | **str** | Error message (if execution failed) | [optional] 
**execution_result** | [**ExecutionResult**](ExecutionResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.execution_result_response import ExecutionResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionResultResponse from a JSON string
execution_result_response_instance = ExecutionResultResponse.from_json(json)
# print the JSON string representation of the object
print(ExecutionResultResponse.to_json())

# convert the object into a dict
execution_result_response_dict = execution_result_response_instance.to_dict()
# create an instance of ExecutionResultResponse from a dict
execution_result_response_from_dict = ExecutionResultResponse.from_dict(execution_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


