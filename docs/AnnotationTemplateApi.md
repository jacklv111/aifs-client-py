# aifs_client.AnnotationTemplateApi

All URIs are relative to *https://www.example.com/api/open/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_annotation_template**](AnnotationTemplateApi.md#copy_annotation_template) | **POST** /annotation-templates/{annotationTemplateId}/copy | Copy an annotation template
[**create_annotation_template**](AnnotationTemplateApi.md#create_annotation_template) | **POST** /annotation-templates | Create an annotation template
[**delete_annotation_template**](AnnotationTemplateApi.md#delete_annotation_template) | **DELETE** /annotation-templates/{annotationTemplateId} | Delete an annotation template
[**get_anno_template_details**](AnnotationTemplateApi.md#get_anno_template_details) | **GET** /annotation-templates/{annotationTemplateId}/details | Get annotation template details
[**get_anno_template_list**](AnnotationTemplateApi.md#get_anno_template_list) | **GET** /annotation-templates | Get annotation template list
[**update_annotation_template**](AnnotationTemplateApi.md#update_annotation_template) | **PUT** /annotation-templates | Update an annotation template


# **copy_annotation_template**
> CopyAnnotationTemplate200Response copy_annotation_template(annotation_template_id)

Copy an annotation template

Copy an annotation template

### Example


```python
import time
import aifs_client
from aifs_client.api import annotation_template_api
from aifs_client.model.copy_annotation_template200_response import CopyAnnotationTemplate200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_template_api.AnnotationTemplateApi(api_client)
    annotation_template_id = "annotationTemplateId_example" # str | The id of an annotation template

    # example passing only required values which don't have defaults set
    try:
        # Copy an annotation template
        api_response = api_instance.copy_annotation_template(annotation_template_id)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling AnnotationTemplateApi->copy_annotation_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_template_id** | **str**| The id of an annotation template |

### Return type

[**CopyAnnotationTemplate200Response**](CopyAnnotationTemplate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Annotation template not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_annotation_template**
> CreateAnnoTemplateSuccessResp create_annotation_template(create_annotation_template_request)

Create an annotation template

Create an annotation template

### Example


```python
import time
import aifs_client
from aifs_client.api import annotation_template_api
from aifs_client.model.create_annotation_template_request import CreateAnnotationTemplateRequest
from aifs_client.model.create_anno_template_success_resp import CreateAnnoTemplateSuccessResp
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_template_api.AnnotationTemplateApi(api_client)
    create_annotation_template_request = CreateAnnotationTemplateRequest(
        name="name_example",
        type="type_example",
        description="description_example",
        labels=[
            Label(
                id="id_example",
                name="name_example",
                super_category_name="super_category_name_example",
                color=1,
                key_point_def=KeyPointDef([
                    "key_point_def_example",
                ]),
                key_point_skeleton=KeyPointSkeleton([
                    [
                        1,
                    ],
                ]),
                cover_image_url="cover_image_url_example",
            ),
        ],
        word_list=WordList([
            "word_list_example",
        ]),
    ) # CreateAnnotationTemplateRequest | Create an new annotation template

    # example passing only required values which don't have defaults set
    try:
        # Create an annotation template
        api_response = api_instance.create_annotation_template(create_annotation_template_request)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling AnnotationTemplateApi->create_annotation_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_annotation_template_request** | [**CreateAnnotationTemplateRequest**](CreateAnnotationTemplateRequest.md)| Create an new annotation template |

### Return type

[**CreateAnnoTemplateSuccessResp**](CreateAnnoTemplateSuccessResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Invalid input parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_annotation_template**
> delete_annotation_template(annotation_template_id)

Delete an annotation template

Delete an annotation template

### Example


```python
import time
import aifs_client
from aifs_client.api import annotation_template_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_template_api.AnnotationTemplateApi(api_client)
    annotation_template_id = "annotationTemplateId_example" # str | The id of an annotation template

    # example passing only required values which don't have defaults set
    try:
        # Delete an annotation template
        api_instance.delete_annotation_template(annotation_template_id)
    except aifs_client.ApiException as e:
        print("Exception when calling AnnotationTemplateApi->delete_annotation_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_template_id** | **str**| The id of an annotation template |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Annotation template not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anno_template_details**
> AnnotationTemplateDetails get_anno_template_details(annotation_template_id)

Get annotation template details

Get annotation template details

### Example


```python
import time
import aifs_client
from aifs_client.api import annotation_template_api
from aifs_client.model.annotation_template_details import AnnotationTemplateDetails
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_template_api.AnnotationTemplateApi(api_client)
    annotation_template_id = "annotationTemplateId_example" # str | The id of an annotation template

    # example passing only required values which don't have defaults set
    try:
        # Get annotation template details
        api_response = api_instance.get_anno_template_details(annotation_template_id)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling AnnotationTemplateApi->get_anno_template_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_template_id** | **str**| The id of an annotation template |

### Return type

[**AnnotationTemplateDetails**](AnnotationTemplateDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | annotation template not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anno_template_list**
> [AnnotationTemplateListItem] get_anno_template_list()

Get annotation template list

Get annotation template list

### Example


```python
import time
import aifs_client
from aifs_client.api import annotation_template_api
from aifs_client.model.annotation_template_list_item import AnnotationTemplateListItem
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_template_api.AnnotationTemplateApi(api_client)
    offset = 0 # int | The number of items to skip before starting to collect the result set (optional) if omitted the server will use the default value of 0
    limit = 10 # int | The numbers of items to return (optional) if omitted the server will use the default value of 10
    annotation_template_id_list = "aaa,bbb,ccc" # str | annotation template with id in annotation template id list will be got (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get annotation template list
        api_response = api_instance.get_anno_template_list(offset=offset, limit=limit, annotation_template_id_list=annotation_template_id_list)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling AnnotationTemplateApi->get_anno_template_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip before starting to collect the result set | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of items to return | [optional] if omitted the server will use the default value of 10
 **annotation_template_id_list** | **str**| annotation template with id in annotation template id list will be got | [optional]

### Return type

[**[AnnotationTemplateListItem]**](AnnotationTemplateListItem.md)

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

# **update_annotation_template**
> update_annotation_template(update_annotation_template_request)

Update an annotation template

Update an annotation template

### Example


```python
import time
import aifs_client
from aifs_client.api import annotation_template_api
from aifs_client.model.update_annotation_template_request import UpdateAnnotationTemplateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = annotation_template_api.AnnotationTemplateApi(api_client)
    update_annotation_template_request = UpdateAnnotationTemplateRequest(
        id="id_example",
        name="name_example",
        type="type_example",
        description="description_example",
        labels=[
            Label(
                id="id_example",
                name="name_example",
                super_category_name="super_category_name_example",
                color=1,
                key_point_def=KeyPointDef([
                    "key_point_def_example",
                ]),
                key_point_skeleton=KeyPointSkeleton([
                    [
                        1,
                    ],
                ]),
                cover_image_url="cover_image_url_example",
            ),
        ],
        word_list=WordList([
            "word_list_example",
        ]),
    ) # UpdateAnnotationTemplateRequest | Update an existed annotation template

    # example passing only required values which don't have defaults set
    try:
        # Update an annotation template
        api_instance.update_annotation_template(update_annotation_template_request)
    except aifs_client.ApiException as e:
        print("Exception when calling AnnotationTemplateApi->update_annotation_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_annotation_template_request** | [**UpdateAnnotationTemplateRequest**](UpdateAnnotationTemplateRequest.md)| Update an existed annotation template |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Annotation template not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

