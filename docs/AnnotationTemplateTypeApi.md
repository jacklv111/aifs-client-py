# aifs_client.AnnotationTemplateTypeApi

All URIs are relative to *https://www.example.com/api/open/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_anno_template_type_list**](AnnotationTemplateTypeApi.md#get_anno_template_type_list) | **GET** /annotation-template-types | Get annotation template type list


# **get_anno_template_type_list**
> AnnotationTemplateTypeList get_anno_template_type_list()

Get annotation template type list

Get annotation template type list

### Example


```python
import time
import aifs_client
from aifs_client.api import annotation_template_type_api
from aifs_client.model.annotation_template_type_list import AnnotationTemplateTypeList
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_template_type_api.AnnotationTemplateTypeApi(api_client)
    offset = 0 # int | The number of items to skip before starting to collect the result set (optional) if omitted the server will use the default value of 0
    limit = 10 # int | The numbers of items to return (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get annotation template type list
        api_response = api_instance.get_anno_template_type_list(offset=offset, limit=limit)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling AnnotationTemplateTypeApi->get_anno_template_type_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip before starting to collect the result set | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of items to return | [optional] if omitted the server will use the default value of 10

### Return type

[**AnnotationTemplateTypeList**](AnnotationTemplateTypeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

