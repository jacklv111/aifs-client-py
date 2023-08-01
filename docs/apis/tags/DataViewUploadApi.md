<a id="__pageTop"></a>
# aifs_client.apis.tags.data_view_upload_api.DataViewUploadApi

All URIs are relative to *https://www.example.com/api/open/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_annotation_to_data_view**](#upload_annotation_to_data_view) | **post** /data-views/{dataViewId}/annotations | Upload annotations to data view
[**upload_dataset_zip_to_data_view**](#upload_dataset_zip_to_data_view) | **post** /data-views/{dataViewId}/dataset-zip | Upload dataset zip
[**upload_file_to_data_view**](#upload_file_to_data_view) | **post** /data-views/{dataViewId}/artifact | Upload file to data view
[**upload_model_data_to_data_view**](#upload_model_data_to_data_view) | **post** /data-views/{dataViewId}/model | Upload model data to data view
[**upload_raw_data_to_data_view**](#upload_raw_data_to_data_view) | **post** /data-views/{dataViewId}/raw-data | Upload raw data to data view

# **upload_annotation_to_data_view**
<a id="upload_annotation_to_data_view"></a>
> upload_annotation_to_data_view(data_view_id)

Upload annotations to data view

Upload annotations to data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_upload_api
from aifs_client.model.upload_annotation_format import UploadAnnotationFormat
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_upload_api.DataViewUploadApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    try:
        # Upload annotations to data view
        api_response = api_instance.upload_annotation_to_data_view(
            path_params=path_params,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_annotation_to_data_view: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    body = dict(
        file_meta=open('/path/to/file', 'rb'),
        files=[
            open('/path/to/file', 'rb')
        ],
    )
    try:
        # Upload annotations to data view
        api_response = api_instance.upload_annotation_to_data_view(
            path_params=path_params,
            body=body,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_annotation_to_data_view: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**fileMeta** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | [optional] 
**[files](#files)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# files

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**resourcePath** | str,  | str,  | the folder path of the resource | [optional] 
**annotationTemplateId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**format** | [**UploadAnnotationFormat**]({{complexTypePrefix}}UploadAnnotationFormat.md) | [**UploadAnnotationFormat**]({{complexTypePrefix}}UploadAnnotationFormat.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dataViewId | DataViewIdSchema | | 

# DataViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upload_annotation_to_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#upload_annotation_to_data_view.ApiResponseFor404) | data view not found

#### upload_annotation_to_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### upload_annotation_to_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_dataset_zip_to_data_view**
<a id="upload_dataset_zip_to_data_view"></a>
> upload_dataset_zip_to_data_view(data_view_idx_file_namebody)

Upload dataset zip

Upload dataset zip

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_upload_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_upload_api.DataViewUploadApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    header_params = {
        'X-File-Name': "X-File-Name_example",
    }
    body = open('/path/to/file', 'rb')
    try:
        # Upload dataset zip
        api_response = api_instance.upload_dataset_zip_to_data_view(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_dataset_zip_to_data_view: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationOctetStream] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-File-Name | XFileNameSchema | | 

# XFileNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dataViewId | DataViewIdSchema | | 

# DataViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upload_dataset_zip_to_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#upload_dataset_zip_to_data_view.ApiResponseFor404) | data view not found

#### upload_dataset_zip_to_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### upload_dataset_zip_to_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_file_to_data_view**
<a id="upload_file_to_data_view"></a>
> upload_file_to_data_view(data_view_idx_file_namebody)

Upload file to data view

Upload file to data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_upload_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_upload_api.DataViewUploadApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    header_params = {
        'X-File-Name': "X-File-Name_example",
    }
    body = open('/path/to/file', 'rb')
    try:
        # Upload file to data view
        api_response = api_instance.upload_file_to_data_view(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_file_to_data_view: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationOctetStream] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-File-Name | XFileNameSchema | | 

# XFileNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dataViewId | DataViewIdSchema | | 

# DataViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upload_file_to_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#upload_file_to_data_view.ApiResponseFor404) | data view not found

#### upload_file_to_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### upload_file_to_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_model_data_to_data_view**
<a id="upload_model_data_to_data_view"></a>
> upload_model_data_to_data_view(data_view_id)

Upload model data to data view

Upload model data to data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_upload_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_upload_api.DataViewUploadApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    try:
        # Upload model data to data view
        api_response = api_instance.upload_model_data_to_data_view(
            path_params=path_params,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_model_data_to_data_view: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    body = dict(
        commit_id="commit_id_example",
        progress="progress_example",
        model_jit=open('/path/to/file', 'rb'),
        onnx=open('/path/to/file', 'rb'),
        dynamic_onnx=open('/path/to/file', 'rb'),
        config_py=open('/path/to/file', 'rb'),
        best_pth=open('/path/to/file', 'rb'),
        last_pth=open('/path/to/file', 'rb'),
        output_template=open('/path/to/file', 'rb'),
        logs=[
            open('/path/to/file', 'rb')
        ],
    )
    try:
        # Upload model data to data view
        api_response = api_instance.upload_model_data_to_data_view(
            path_params=path_params,
            body=body,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_model_data_to_data_view: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**commitId** | str,  | str,  |  | [optional] 
**progress** | str,  | str,  |  | [optional] 
**modelJit** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | [optional] 
**onnx** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | [optional] 
**dynamicOnnx** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | [optional] 
**configPy** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | [optional] 
**bestPth** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | [optional] 
**lastPth** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | [optional] 
**outputTemplate** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | [optional] 
**[logs](#logs)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# logs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dataViewId | DataViewIdSchema | | 

# DataViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upload_model_data_to_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#upload_model_data_to_data_view.ApiResponseFor404) | data view not found

#### upload_model_data_to_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### upload_model_data_to_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_raw_data_to_data_view**
<a id="upload_raw_data_to_data_view"></a>
> upload_raw_data_to_data_view(data_view_id)

Upload raw data to data view

Upload raw data to data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_upload_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_upload_api.DataViewUploadApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    try:
        # Upload raw data to data view
        api_response = api_instance.upload_raw_data_to_data_view(
            path_params=path_params,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_raw_data_to_data_view: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    body = dict(
        files=[
            open('/path/to/file', 'rb')
        ],
    )
    try:
        # Upload raw data to data view
        api_response = api_instance.upload_raw_data_to_data_view(
            path_params=path_params,
            body=body,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_raw_data_to_data_view: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[files](#files)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# files

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**resourcePath** | str,  | str,  | the folder path of the resource | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dataViewId | DataViewIdSchema | | 

# DataViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upload_raw_data_to_data_view.ApiResponseFor200) | Successful operation

#### upload_raw_data_to_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

