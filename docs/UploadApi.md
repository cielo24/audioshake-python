# swagger_client.UploadApi

All URIs are relative to *https://groovy.audioshake.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_audio_link_post**](UploadApi.md#upload_audio_link_post) | **POST** /upload/audio-link | Create a new asset from a file link.
[**upload_link_post**](UploadApi.md#upload_link_post) | **POST** /upload/link | Create a new asset from a file link.
[**upload_post**](UploadApi.md#upload_post) | **POST** /upload/ | Create a new asset.

# **upload_audio_link_post**
> InlineResponse2XX1 upload_audio_link_post(body)

Create a new asset from a file link.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UploadApi(swagger_client.ApiClient(configuration))
body = swagger_client.UploadAudiolinkBody() # UploadAudiolinkBody | 

try:
    # Create a new asset from a file link.
    api_response = api_instance.upload_audio_link_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadApi->upload_audio_link_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UploadAudiolinkBody**](UploadAudiolinkBody.md)|  | 

### Return type

[**InlineResponse2XX1**](InlineResponse2XX1.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_link_post**
> InlineResponse2XX1 upload_link_post(body)

Create a new asset from a file link.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UploadApi(swagger_client.ApiClient(configuration))
body = swagger_client.UploadLinkBody() # UploadLinkBody | 

try:
    # Create a new asset from a file link.
    api_response = api_instance.upload_link_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadApi->upload_link_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UploadLinkBody**](UploadLinkBody.md)|  | 

### Return type

[**InlineResponse2XX1**](InlineResponse2XX1.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_post**
> InlineResponse2XX1 upload_post(file)

Create a new asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UploadApi(swagger_client.ApiClient(configuration))
file = '/path/to/file' # file | 

try:
    # Create a new asset.
    api_response = api_instance.upload_post(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadApi->upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | [**file**](.md)|  | 

### Return type

[**InlineResponse2XX1**](InlineResponse2XX1.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

