<a id="__pageTop"></a>
# openapi_client.apis.tags.annotation_template_type_api.AnnotationTemplateTypeApi

All URIs are relative to *https://www.example.com/api/open/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_anno_template_type_list**](#get_anno_template_type_list) | **get** /annotation-template-types | Get annotation template type list

# **get_anno_template_type_list**
<a id="get_anno_template_type_list"></a>
> AnnotationTemplateTypeList get_anno_template_type_list()

Get annotation template type list

Get annotation template type list

### Example

```python
import openapi_client
from openapi_client.apis.tags import annotation_template_type_api
from openapi_client.model.annotation_template_type_list import AnnotationTemplateTypeList
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = annotation_template_type_api.AnnotationTemplateTypeApi(api_client)

    # example passing only optional values
    query_params = {
        'offset': 0,
        'limit': 10,
    }
    try:
        # Get annotation template type list
        api_response = api_instance.get_anno_template_type_list(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AnnotationTemplateTypeApi->get_anno_template_type_list: %s\n" % e)
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_anno_template_type_list.ApiResponseFor200) | Successful operation

#### get_anno_template_type_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnotationTemplateTypeList**](../../models/AnnotationTemplateTypeList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

