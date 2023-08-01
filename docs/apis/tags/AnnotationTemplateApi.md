<a id="__pageTop"></a>
# aifs_client.apis.tags.annotation_template_api.AnnotationTemplateApi

All URIs are relative to *https://www.example.com/api/open/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_annotation_template**](#copy_annotation_template) | **post** /annotation-templates/{annotationTemplateId}/copy | Copy an annotation template
[**create_annotation_template**](#create_annotation_template) | **post** /annotation-templates | Create an annotation template
[**delete_annotation_template**](#delete_annotation_template) | **delete** /annotation-templates/{annotationTemplateId} | Delete an annotation template
[**get_anno_template_details**](#get_anno_template_details) | **get** /annotation-templates/{annotationTemplateId}/details | Get annotation template details
[**get_anno_template_list**](#get_anno_template_list) | **get** /annotation-templates | Get annotation template list
[**update_annotation_template**](#update_annotation_template) | **put** /annotation-templates | Update an annotation template

# **copy_annotation_template**
<a id="copy_annotation_template"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} copy_annotation_template(annotation_template_id)

Copy an annotation template

Copy an annotation template

### Example

```python
import aifs_client
from aifs_client.apis.tags import annotation_template_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = annotation_template_api.AnnotationTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'annotationTemplateId': "annotationTemplateId_example",
    }
    try:
        # Copy an annotation template
        api_response = api_instance.copy_annotation_template(
            path_params=path_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling AnnotationTemplateApi->copy_annotation_template: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
annotationTemplateId | AnnotationTemplateIdSchema | | 

# AnnotationTemplateIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#copy_annotation_template.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#copy_annotation_template.ApiResponseFor404) | Annotation template not found

#### copy_annotation_template.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**annotationTemplateId** | str, uuid.UUID,  | str,  | annotation template id of the copied annotation template | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### copy_annotation_template.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_annotation_template**
<a id="create_annotation_template"></a>
> CreateAnnoTemplateSuccessResp create_annotation_template(create_annotation_template_request)

Create an annotation template

Create an annotation template

### Example

```python
import aifs_client
from aifs_client.apis.tags import annotation_template_api
from aifs_client.model.create_annotation_template_request import CreateAnnotationTemplateRequest
from aifs_client.model.create_anno_template_success_resp import CreateAnnoTemplateSuccessResp
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = annotation_template_api.AnnotationTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateAnnotationTemplateRequest(
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
                    "key_point_def_example"
                ]),
                key_point_skeleton=KeyPointSkeleton([
                    [
                        1
                    ]
                ]),
                cover_image_url="cover_image_url_example",
            )
        ],
        word_list=WordList([
            "word_list_example"
        ]),
    )
    try:
        # Create an annotation template
        api_response = api_instance.create_annotation_template(
            body=body,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling AnnotationTemplateApi->create_annotation_template: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateAnnotationTemplateRequest**](../../models/CreateAnnotationTemplateRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_annotation_template.ApiResponseFor201) | Successful operation
400 | [ApiResponseFor400](#create_annotation_template.ApiResponseFor400) | Invalid input parameters

#### create_annotation_template.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateAnnoTemplateSuccessResp**](../../models/CreateAnnoTemplateSuccessResp.md) |  | 


#### create_annotation_template.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_annotation_template**
<a id="delete_annotation_template"></a>
> delete_annotation_template(annotation_template_id)

Delete an annotation template

Delete an annotation template

### Example

```python
import aifs_client
from aifs_client.apis.tags import annotation_template_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = annotation_template_api.AnnotationTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'annotationTemplateId': "annotationTemplateId_example",
    }
    try:
        # Delete an annotation template
        api_response = api_instance.delete_annotation_template(
            path_params=path_params,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling AnnotationTemplateApi->delete_annotation_template: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
annotationTemplateId | AnnotationTemplateIdSchema | | 

# AnnotationTemplateIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_annotation_template.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#delete_annotation_template.ApiResponseFor404) | Annotation template not found

#### delete_annotation_template.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_annotation_template.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_anno_template_details**
<a id="get_anno_template_details"></a>
> AnnotationTemplateDetails get_anno_template_details(annotation_template_id)

Get annotation template details

Get annotation template details

### Example

```python
import aifs_client
from aifs_client.apis.tags import annotation_template_api
from aifs_client.model.annotation_template_details import AnnotationTemplateDetails
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = annotation_template_api.AnnotationTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'annotationTemplateId': "annotationTemplateId_example",
    }
    try:
        # Get annotation template details
        api_response = api_instance.get_anno_template_details(
            path_params=path_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling AnnotationTemplateApi->get_anno_template_details: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
annotationTemplateId | AnnotationTemplateIdSchema | | 

# AnnotationTemplateIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_anno_template_details.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_anno_template_details.ApiResponseFor404) | annotation template not found

#### get_anno_template_details.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnotationTemplateDetails**](../../models/AnnotationTemplateDetails.md) |  | 


#### get_anno_template_details.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_anno_template_list**
<a id="get_anno_template_list"></a>
> [AnnotationTemplateListItem] get_anno_template_list()

Get annotation template list

Get annotation template list

### Example

```python
import aifs_client
from aifs_client.apis.tags import annotation_template_api
from aifs_client.model.annotation_template_list_item import AnnotationTemplateListItem
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = annotation_template_api.AnnotationTemplateApi(api_client)

    # example passing only optional values
    query_params = {
        'offset': 0,
        'limit': 10,
        'annotationTemplateIdList': "aaa,bbb,ccc",
    }
    try:
        # Get annotation template list
        api_response = api_instance.get_anno_template_list(
            query_params=query_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling AnnotationTemplateApi->get_anno_template_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
offset | OffsetSchema | | optional
limit | LimitSchema | | optional
annotationTemplateIdList | AnnotationTemplateIdListSchema | | optional


# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0value must be a 32 bit integer

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

# AnnotationTemplateIdListSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_anno_template_list.ApiResponseFor200) | Successful operation

#### get_anno_template_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AnnotationTemplateListItem**]({{complexTypePrefix}}AnnotationTemplateListItem.md) | [**AnnotationTemplateListItem**]({{complexTypePrefix}}AnnotationTemplateListItem.md) | [**AnnotationTemplateListItem**]({{complexTypePrefix}}AnnotationTemplateListItem.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_annotation_template**
<a id="update_annotation_template"></a>
> update_annotation_template(update_annotation_template_request)

Update an annotation template

Update an annotation template

### Example

```python
import aifs_client
from aifs_client.apis.tags import annotation_template_api
from aifs_client.model.update_annotation_template_request import UpdateAnnotationTemplateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = annotation_template_api.AnnotationTemplateApi(api_client)

    # example passing only required values which don't have defaults set
    body = UpdateAnnotationTemplateRequest(
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
                    "key_point_def_example"
                ]),
                key_point_skeleton=KeyPointSkeleton([
                    [
                        1
                    ]
                ]),
                cover_image_url="cover_image_url_example",
            )
        ],
        word_list=WordList([
            "word_list_example"
        ]),
    )
    try:
        # Update an annotation template
        api_response = api_instance.update_annotation_template(
            body=body,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling AnnotationTemplateApi->update_annotation_template: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateAnnotationTemplateRequest**](../../models/UpdateAnnotationTemplateRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_annotation_template.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#update_annotation_template.ApiResponseFor404) | Annotation template not found

#### update_annotation_template.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_annotation_template.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

