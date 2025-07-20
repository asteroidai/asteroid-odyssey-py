# BrowserSessionRecordingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recording_url** | **str** | The URL of the browser session recording | 

## Example

```python
from openapi_client.models.browser_session_recording_response import BrowserSessionRecordingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserSessionRecordingResponse from a JSON string
browser_session_recording_response_instance = BrowserSessionRecordingResponse.from_json(json)
# print the JSON string representation of the object
print(BrowserSessionRecordingResponse.to_json())

# convert the object into a dict
browser_session_recording_response_dict = browser_session_recording_response_instance.to_dict()
# create an instance of BrowserSessionRecordingResponse from a dict
browser_session_recording_response_from_dict = BrowserSessionRecordingResponse.from_dict(browser_session_recording_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


