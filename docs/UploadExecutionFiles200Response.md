# UploadExecutionFiles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Success message | [optional] 
**file_ids** | **List[str]** | IDs of the uploaded files | [optional] 

## Example

```python
from openapi_client.models.upload_execution_files200_response import UploadExecutionFiles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UploadExecutionFiles200Response from a JSON string
upload_execution_files200_response_instance = UploadExecutionFiles200Response.from_json(json)
# print the JSON string representation of the object
print(UploadExecutionFiles200Response.to_json())

# convert the object into a dict
upload_execution_files200_response_dict = upload_execution_files200_response_instance.to_dict()
# create an instance of UploadExecutionFiles200Response from a dict
upload_execution_files200_response_from_dict = UploadExecutionFiles200Response.from_dict(upload_execution_files200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


