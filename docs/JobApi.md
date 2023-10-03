# audioshake.JobApi

All URIs are relative to *https://groovy.audioshake.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_id_get**](JobApi.md#job_id_get) | **GET** /job/{id} | Get a job given an Id.
[**job_post**](JobApi.md#job_post) | **POST** /job/ | Create a new job.

# **job_id_get**
> InlineResponse2XX job_id_get(id)

Get a job given an Id.

### Example
```python
from __future__ import print_function
import time
import audioshake
from audioshake.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = audioshake.JobApi(audioshake.ApiClient(configuration))
id = 'id_example' # str |

try:
    # Get a job given an Id.
    api_response = api_instance.job_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->job_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**InlineResponse2XX**](InlineResponse2XX.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_post**
> InlineResponse2XX job_post(body=body)

Create a new job.

### Example
```python
from __future__ import print_function
import time
import audioshake
from audioshake.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = audioshake.JobApi(audioshake.ApiClient(configuration))
body = audioshake.JobBody() # JobBody |  (optional)

try:
    # Create a new job.
    api_response = api_instance.job_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->job_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobBody**](JobBody.md)|  | [optional]

### Return type

[**InlineResponse2XX**](InlineResponse2XX.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

