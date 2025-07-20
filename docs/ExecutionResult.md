# ExecutionResult

The result of an execution. Contains the outcome, reasoning, and result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome** | **str** | The outcome of the execution (success or failure) | [optional] 
**reasoning** | **str** | The reasoning behind the execution outcome | [optional] 
**result** | **Dict[str, object]** | The structured result data from the execution. This will follow the format defined in the result_schema of the agent. | [optional] 

## Example

```python
from openapi_client.models.execution_result import ExecutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionResult from a JSON string
execution_result_instance = ExecutionResult.from_json(json)
# print the JSON string representation of the object
print(ExecutionResult.to_json())

# convert the object into a dict
execution_result_dict = execution_result_instance.to_dict()
# create an instance of ExecutionResult from a dict
execution_result_from_dict = ExecutionResult.from_dict(execution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


