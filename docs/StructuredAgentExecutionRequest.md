# StructuredAgentExecutionRequest

Request to execute an agent with structured parameters including optional agent profile configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_profile_id** | **str** | The ID of the browser profile to use | [optional] 
**dynamic_data** | **Dict[str, object]** | Dynamic data to be merged into the saved agent configuration. | [optional] 

## Example

```python
from openapi_client.models.structured_agent_execution_request import StructuredAgentExecutionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredAgentExecutionRequest from a JSON string
structured_agent_execution_request_instance = StructuredAgentExecutionRequest.from_json(json)
# print the JSON string representation of the object
print(StructuredAgentExecutionRequest.to_json())

# convert the object into a dict
structured_agent_execution_request_dict = structured_agent_execution_request_instance.to_dict()
# create an instance of StructuredAgentExecutionRequest from a dict
structured_agent_execution_request_from_dict = StructuredAgentExecutionRequest.from_dict(structured_agent_execution_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


