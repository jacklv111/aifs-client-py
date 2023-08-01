<a id="__pageTop"></a>
# aifs_client.apis.tags.data_view_api.DataViewApi

All URIs are relative to *https://www.example.com/api/open/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_view**](#create_data_view) | **post** /data-views | Create a data view
[**delete_data_item_in_data_view**](#delete_data_item_in_data_view) | **delete** /data-views/{dataViewId}/data-items | Delete data item in a data view
[**delete_data_view**](#delete_data_view) | **delete** /data-views/{dataViewId} | Delete a data view
[**divide_data_view**](#divide_data_view) | **post** /data-views/{dataViewId}/raw-data-divide | Divide data view
[**filter_annotations_in_data_view**](#filter_annotations_in_data_view) | **post** /data-views/{dataViewId}/annotation-filter | Filter annotations in a data view
[**get_all_annotation_data_in_data_view**](#get_all_annotation_data_in_data_view) | **get** /data-views/{dataViewId}/annotation-data | Get all annotation data in a data view
[**get_all_annotation_locations_in_data_view**](#get_all_annotation_locations_in_data_view) | **get** /data-views/{dataViewId}/annotation-locations | Get all annotation locations in a data view
[**get_all_raw_data_locations_in_data_view**](#get_all_raw_data_locations_in_data_view) | **get** /data-views/{dataViewId}/raw-data-locations | Get all raw data locations in a data view
[**get_annotations_in_data_view**](#get_annotations_in_data_view) | **get** /data-views/{dataViewId}/annotations | Get data view annotations
[**get_artifact_locations_in_data_view**](#get_artifact_locations_in_data_view) | **get** /data-views/{dataViewId}/artifact-locations | Get files&#x27; locations in artifact data view
[**get_data_view_details**](#get_data_view_details) | **get** /data-views/{dataViewId}/details | Get data view details
[**get_data_view_list**](#get_data_view_list) | **get** /data-views | Get data view list
[**get_data_view_statistics**](#get_data_view_statistics) | **get** /data-views/{dataViewId}/statistics | Get data view statistics
[**get_dataset_zip_location_in_data_view**](#get_dataset_zip_location_in_data_view) | **get** /data-views/{dataViewId}/dataset-zip-location | Get dataset zip&#x27;s location in a data view
[**get_model_data_locations_in_data_view**](#get_model_data_locations_in_data_view) | **get** /data-views/{dataViewId}/model-data-locations | Get all model data locations in a data view
[**get_raw_data_hash_list_in_data_view**](#get_raw_data_hash_list_in_data_view) | **get** /data-views/{dataViewId}/raw-data-hash-list | Get data view raw data hash list
[**get_raw_data_in_data_view**](#get_raw_data_in_data_view) | **get** /data-views/{dataViewId}/raw-data | Get data view raw data
[**hard_delete_data_view**](#hard_delete_data_view) | **delete** /data-views/{dataViewId}/hard-delete | Hard delete a data view
[**merge_data_views**](#merge_data_views) | **post** /data-views/merge | Merge data views
[**merge_data_views_to_crurrent**](#merge_data_views_to_crurrent) | **post** /data-views/{dataViewId}/merge | Merge data views
[**move_data_view_items**](#move_data_view_items) | **post** /data-views/move | Move data items between data views
[**update_dataset_zip_view**](#update_dataset_zip_view) | **put** /data-views/{dataViewId}/dataset-zip | Update a dataset-zip view meta

# **create_data_view**
<a id="create_data_view"></a>
> CreateDataViewSuccessResp create_data_view(create_data_view_request)

Create a data view

Create a data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.create_data_view_request import CreateDataViewRequest
from aifs_client.model.create_data_view_success_resp import CreateDataViewSuccessResp
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateDataViewRequest(
        data_view_name="data_view_name_example",
        description="description_example",
        view_type=DataViewType("raw-data"),
        raw_data_type=RawDataType("image"),
        zip_format=ZipFormat("image-classification"),
        related_data_view_id="related_data_view_id_example",
        annotation_template_id="annotation_template_id_example",
        raw_data_view_id="raw_data_view_id_example",
        annotation_view_id="annotation_view_id_example",
    )
    try:
        # Create a data view
        api_response = api_instance.create_data_view(
            body=body,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->create_data_view: %s\n" % e)
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
[**CreateDataViewRequest**](../../models/CreateDataViewRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_data_view.ApiResponseFor201) | Successful operation
400 | [ApiResponseFor400](#create_data_view.ApiResponseFor400) | Invalid input parameters

#### create_data_view.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateDataViewSuccessResp**](../../models/CreateDataViewSuccessResp.md) |  | 


#### create_data_view.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_data_item_in_data_view**
<a id="delete_data_item_in_data_view"></a>
> delete_data_item_in_data_view(data_view_iddata_view_item_id_list)

Delete data item in a data view

Delete data item in a data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    query_params = {
        'dataViewItemIdList': [
        "dataViewItemIdList_example"
    ],
    }
    try:
        # Delete data item in a data view
        api_response = api_instance.delete_data_item_in_data_view(
            path_params=path_params,
            query_params=query_params,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->delete_data_item_in_data_view: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dataViewItemIdList | DataViewItemIdListSchema | | 


# DataViewItemIdListSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, uuid.UUID,  | str,  |  | value must be a uuid

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
200 | [ApiResponseFor200](#delete_data_item_in_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#delete_data_item_in_data_view.ApiResponseFor404) | data item not found

#### delete_data_item_in_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_data_item_in_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_data_view**
<a id="delete_data_view"></a>
> delete_data_view(data_view_id)

Delete a data view

Delete a data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    try:
        # Delete a data view
        api_response = api_instance.delete_data_view(
            path_params=path_params,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->delete_data_view: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#delete_data_view.ApiResponseFor404) | Data view not found

#### delete_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **divide_data_view**
<a id="divide_data_view"></a>
> DivideRawDataDataViewResponse divide_data_view(data_view_iddivide_raw_data_data_view_request)

Divide data view

Divide data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.divide_raw_data_data_view_response import DivideRawDataDataViewResponse
from aifs_client.model.divide_raw_data_data_view_request import DivideRawDataDataViewRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    body = DivideRawDataDataViewRequest([
        dict(
            name="name_example",
            description="description_example",
            ratio=1,
        )
    ])
    try:
        # Divide data view
        api_response = api_instance.divide_data_view(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->divide_data_view: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DivideRawDataDataViewRequest**](../../models/DivideRawDataDataViewRequest.md) |  | 


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
200 | [ApiResponseFor200](#divide_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#divide_data_view.ApiResponseFor404) | data view not found

#### divide_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DivideRawDataDataViewResponse**](../../models/DivideRawDataDataViewResponse.md) |  | 


#### divide_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **filter_annotations_in_data_view**
<a id="filter_annotations_in_data_view"></a>
> FilterAnnotationsInDataViewResponse filter_annotations_in_data_view(data_view_idfilter_annotations_in_data_view_request)

Filter annotations in a data view

Filter annotations in a data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.filter_annotations_in_data_view_request import FilterAnnotationsInDataViewRequest
from aifs_client.model.filter_annotations_in_data_view_response import FilterAnnotationsInDataViewResponse
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    body = FilterAnnotationsInDataViewRequest(
        raw_data_view_id="raw_data_view_id_example",
    )
    try:
        # Filter annotations in a data view
        api_response = api_instance.filter_annotations_in_data_view(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->filter_annotations_in_data_view: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FilterAnnotationsInDataViewRequest**](../../models/FilterAnnotationsInDataViewRequest.md) |  | 


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
200 | [ApiResponseFor200](#filter_annotations_in_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#filter_annotations_in_data_view.ApiResponseFor404) | data view not found

#### filter_annotations_in_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FilterAnnotationsInDataViewResponse**](../../models/FilterAnnotationsInDataViewResponse.md) |  | 


#### filter_annotations_in_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_all_annotation_data_in_data_view**
<a id="get_all_annotation_data_in_data_view"></a>
> AnnotationViewData get_all_annotation_data_in_data_view(data_view_id)

Get all annotation data in a data view

Get all annotation data in a data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.annotation_view_data import AnnotationViewData
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    try:
        # Get all annotation data in a data view
        api_response = api_instance.get_all_annotation_data_in_data_view(
            path_params=path_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_all_annotation_data_in_data_view: %s\n" % e)
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
200 | [ApiResponseFor200](#get_all_annotation_data_in_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_all_annotation_data_in_data_view.ApiResponseFor404) | data view not found

#### get_all_annotation_data_in_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnotationViewData**](../../models/AnnotationViewData.md) |  | 


#### get_all_annotation_data_in_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_all_annotation_locations_in_data_view**
<a id="get_all_annotation_locations_in_data_view"></a>
> AnnotationViewLocations get_all_annotation_locations_in_data_view(data_view_id)

Get all annotation locations in a data view

Get all annotation locations in a data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.annotation_view_locations import AnnotationViewLocations
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    try:
        # Get all annotation locations in a data view
        api_response = api_instance.get_all_annotation_locations_in_data_view(
            path_params=path_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_all_annotation_locations_in_data_view: %s\n" % e)
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
200 | [ApiResponseFor200](#get_all_annotation_locations_in_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_all_annotation_locations_in_data_view.ApiResponseFor404) | data view not found

#### get_all_annotation_locations_in_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnotationViewLocations**](../../models/AnnotationViewLocations.md) |  | 


#### get_all_annotation_locations_in_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_all_raw_data_locations_in_data_view**
<a id="get_all_raw_data_locations_in_data_view"></a>
> RawDataViewLocations get_all_raw_data_locations_in_data_view(data_view_id)

Get all raw data locations in a data view

Get all raw data locations in a data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.raw_data_view_locations import RawDataViewLocations
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    try:
        # Get all raw data locations in a data view
        api_response = api_instance.get_all_raw_data_locations_in_data_view(
            path_params=path_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_all_raw_data_locations_in_data_view: %s\n" % e)
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
200 | [ApiResponseFor200](#get_all_raw_data_locations_in_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_all_raw_data_locations_in_data_view.ApiResponseFor404) | data view not found

#### get_all_raw_data_locations_in_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RawDataViewLocations**](../../models/RawDataViewLocations.md) |  | 


#### get_all_raw_data_locations_in_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_annotations_in_data_view**
<a id="get_annotations_in_data_view"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_annotations_in_data_view(data_view_id)

Get data view annotations

Get data view annotations

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.annotation_list_item import AnnotationListItem
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    query_params = {
    }
    try:
        # Get data view annotations
        api_response = api_instance.get_annotations_in_data_view(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_annotations_in_data_view: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    query_params = {
        'offset': 0,
        'limit': 10,
        'rawDataIdList': [
        "rawDataIdList_example"
    ],
        'labelId': "labelId_example",
    }
    try:
        # Get data view annotations
        api_response = api_instance.get_annotations_in_data_view(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_annotations_in_data_view: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
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
rawDataIdList | RawDataIdListSchema | | optional
labelId | LabelIdSchema | | optional


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

# RawDataIdListSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, uuid.UUID,  | str,  |  | value must be a uuid

# LabelIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

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
200 | [ApiResponseFor200](#get_annotations_in_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_annotations_in_data_view.ApiResponseFor404) | annotation template not found

#### get_annotations_in_data_view.ApiResponseFor200
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
**annotationTemplateId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**annotationTemplateType** | str,  | str,  |  | [optional] 
**[annotationList](#annotationList)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# annotationList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AnnotationListItem**]({{complexTypePrefix}}AnnotationListItem.md) | [**AnnotationListItem**]({{complexTypePrefix}}AnnotationListItem.md) | [**AnnotationListItem**]({{complexTypePrefix}}AnnotationListItem.md) |  | 

#### get_annotations_in_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_artifact_locations_in_data_view**
<a id="get_artifact_locations_in_data_view"></a>
> ArtifactLocations get_artifact_locations_in_data_view(data_view_id)

Get files' locations in artifact data view

Get files' locations in artifact data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.artifact_locations import ArtifactLocations
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    try:
        # Get files' locations in artifact data view
        api_response = api_instance.get_artifact_locations_in_data_view(
            path_params=path_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_artifact_locations_in_data_view: %s\n" % e)
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
200 | [ApiResponseFor200](#get_artifact_locations_in_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_artifact_locations_in_data_view.ApiResponseFor404) | data view not found

#### get_artifact_locations_in_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArtifactLocations**](../../models/ArtifactLocations.md) |  | 


#### get_artifact_locations_in_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_data_view_details**
<a id="get_data_view_details"></a>
> DataViewDetails get_data_view_details(data_view_id)

Get data view details

Get data view details

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.data_view_details import DataViewDetails
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    try:
        # Get data view details
        api_response = api_instance.get_data_view_details(
            path_params=path_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_data_view_details: %s\n" % e)
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
200 | [ApiResponseFor200](#get_data_view_details.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_data_view_details.ApiResponseFor404) | data view not found

#### get_data_view_details.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DataViewDetails**](../../models/DataViewDetails.md) |  | 


#### get_data_view_details.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_data_view_list**
<a id="get_data_view_list"></a>
> [DataViewListItem] get_data_view_list()

Get data view list

Get data view list

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.data_view_list_item import DataViewListItem
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only optional values
    query_params = {
        'offset': 0,
        'limit': 10,
        'dataViewIdList': "aaa,bbb,ccc",
        'dataViewName': "hand",
    }
    try:
        # Get data view list
        api_response = api_instance.get_data_view_list(
            query_params=query_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_data_view_list: %s\n" % e)
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
dataViewIdList | DataViewIdListSchema | | optional
dataViewName | DataViewNameSchema | | optional


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

# DataViewIdListSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DataViewNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_data_view_list.ApiResponseFor200) | Successful operation

#### get_data_view_list.ApiResponseFor200
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
[**DataViewListItem**]({{complexTypePrefix}}DataViewListItem.md) | [**DataViewListItem**]({{complexTypePrefix}}DataViewListItem.md) | [**DataViewListItem**]({{complexTypePrefix}}DataViewListItem.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_data_view_statistics**
<a id="get_data_view_statistics"></a>
> DataViewStatistics get_data_view_statistics(data_view_id)

Get data view statistics

Get data view statistics

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.data_view_statistics import DataViewStatistics
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    try:
        # Get data view statistics
        api_response = api_instance.get_data_view_statistics(
            path_params=path_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_data_view_statistics: %s\n" % e)
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
200 | [ApiResponseFor200](#get_data_view_statistics.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_data_view_statistics.ApiResponseFor404) | data view not found

#### get_data_view_statistics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DataViewStatistics**](../../models/DataViewStatistics.md) |  | 


#### get_data_view_statistics.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_dataset_zip_location_in_data_view**
<a id="get_dataset_zip_location_in_data_view"></a>
> DatasetZipLocation get_dataset_zip_location_in_data_view(data_view_id)

Get dataset zip's location in a data view

Get dataset zip's location in a data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.dataset_zip_location import DatasetZipLocation
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    try:
        # Get dataset zip's location in a data view
        api_response = api_instance.get_dataset_zip_location_in_data_view(
            path_params=path_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_dataset_zip_location_in_data_view: %s\n" % e)
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
200 | [ApiResponseFor200](#get_dataset_zip_location_in_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_dataset_zip_location_in_data_view.ApiResponseFor404) | data view not found

#### get_dataset_zip_location_in_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DatasetZipLocation**](../../models/DatasetZipLocation.md) |  | 


#### get_dataset_zip_location_in_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_model_data_locations_in_data_view**
<a id="get_model_data_locations_in_data_view"></a>
> ModelDataViewLocations get_model_data_locations_in_data_view(data_view_id)

Get all model data locations in a data view

Get all model data locations in a data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.model_data_view_locations import ModelDataViewLocations
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    try:
        # Get all model data locations in a data view
        api_response = api_instance.get_model_data_locations_in_data_view(
            path_params=path_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_model_data_locations_in_data_view: %s\n" % e)
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
200 | [ApiResponseFor200](#get_model_data_locations_in_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_model_data_locations_in_data_view.ApiResponseFor404) | data view not foundF

#### get_model_data_locations_in_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelDataViewLocations**](../../models/ModelDataViewLocations.md) |  | 


#### get_model_data_locations_in_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_raw_data_hash_list_in_data_view**
<a id="get_raw_data_hash_list_in_data_view"></a>
> RawDataHashList get_raw_data_hash_list_in_data_view(data_view_id)

Get data view raw data hash list

Get data view raw data hash list.

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.raw_data_hash_list import RawDataHashList
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    query_params = {
    }
    try:
        # Get data view raw data hash list
        api_response = api_instance.get_raw_data_hash_list_in_data_view(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_raw_data_hash_list_in_data_view: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    query_params = {
        'offset': 0,
        'limit': 10,
    }
    try:
        # Get data view raw data hash list
        api_response = api_instance.get_raw_data_hash_list_in_data_view(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_raw_data_hash_list_in_data_view: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
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
200 | [ApiResponseFor200](#get_raw_data_hash_list_in_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_raw_data_hash_list_in_data_view.ApiResponseFor404) | data view not found

#### get_raw_data_hash_list_in_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RawDataHashList**](../../models/RawDataHashList.md) |  | 


#### get_raw_data_hash_list_in_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_raw_data_in_data_view**
<a id="get_raw_data_in_data_view"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_raw_data_in_data_view(data_view_id)

Get data view raw data

Get data view raw data

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.raw_data_list_item import RawDataListItem
from aifs_client.model.raw_data_type import RawDataType
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    query_params = {
    }
    try:
        # Get data view raw data
        api_response = api_instance.get_raw_data_in_data_view(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_raw_data_in_data_view: %s\n" % e)

    # example passing only optional values
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    query_params = {
        'offset': 0,
        'limit': 10,
        'rawDataIdList': [
        "rawDataIdList_example"
    ],
        'excludedAnnotationViewId': "excludedAnnotationViewId_example",
        'includedAnnotationViewId': "includedAnnotationViewId_example",
    }
    try:
        # Get data view raw data
        api_response = api_instance.get_raw_data_in_data_view(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_raw_data_in_data_view: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
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
rawDataIdList | RawDataIdListSchema | | optional
excludedAnnotationViewId | ExcludedAnnotationViewIdSchema | | optional
includedAnnotationViewId | IncludedAnnotationViewIdSchema | | optional


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

# RawDataIdListSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, uuid.UUID,  | str,  |  | value must be a uuid

# ExcludedAnnotationViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# IncludedAnnotationViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

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
200 | [ApiResponseFor200](#get_raw_data_in_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#get_raw_data_in_data_view.ApiResponseFor404) | data view not found

#### get_raw_data_in_data_view.ApiResponseFor200
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
**rawDataType** | [**RawDataType**]({{complexTypePrefix}}RawDataType.md) | [**RawDataType**]({{complexTypePrefix}}RawDataType.md) |  | [optional] 
**[rawDataList](#rawDataList)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rawDataList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RawDataListItem**]({{complexTypePrefix}}RawDataListItem.md) | [**RawDataListItem**]({{complexTypePrefix}}RawDataListItem.md) | [**RawDataListItem**]({{complexTypePrefix}}RawDataListItem.md) |  | 

#### get_raw_data_in_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **hard_delete_data_view**
<a id="hard_delete_data_view"></a>
> hard_delete_data_view(data_view_id)

Hard delete a data view

Hard delete a data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    try:
        # Hard delete a data view
        api_response = api_instance.hard_delete_data_view(
            path_params=path_params,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->hard_delete_data_view: %s\n" % e)
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
200 | [ApiResponseFor200](#hard_delete_data_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#hard_delete_data_view.ApiResponseFor404) | Data view not found

#### hard_delete_data_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### hard_delete_data_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **merge_data_views**
<a id="merge_data_views"></a>
> MergeDataViewsSuccessResp merge_data_views(merge_data_views_request)

Merge data views

Merge data views, generate a new data view to put the result

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.merge_data_views_request import MergeDataViewsRequest
from aifs_client.model.merge_data_views_success_resp import MergeDataViewsSuccessResp
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    body = MergeDataViewsRequest(
        name="name_example",
        description="description_example",
        data_view_id_list=[
            "data_view_id_list_example"
        ],
    )
    try:
        # Merge data views
        api_response = api_instance.merge_data_views(
            body=body,
        )
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->merge_data_views: %s\n" % e)
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
[**MergeDataViewsRequest**](../../models/MergeDataViewsRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#merge_data_views.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#merge_data_views.ApiResponseFor400) | Invalid input parameters

#### merge_data_views.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MergeDataViewsSuccessResp**](../../models/MergeDataViewsSuccessResp.md) |  | 


#### merge_data_views.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **merge_data_views_to_crurrent**
<a id="merge_data_views_to_crurrent"></a>
> merge_data_views_to_crurrent(data_view_idmerge_data_views_request)

Merge data views

Merge other data views to current data view

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.merge_data_views_request import MergeDataViewsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    body = MergeDataViewsRequest(
        name="name_example",
        description="description_example",
        data_view_id_list=[
            "data_view_id_list_example"
        ],
    )
    try:
        # Merge data views
        api_response = api_instance.merge_data_views_to_crurrent(
            path_params=path_params,
            body=body,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->merge_data_views_to_crurrent: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MergeDataViewsRequest**](../../models/MergeDataViewsRequest.md) |  | 


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
200 | [ApiResponseFor200](#merge_data_views_to_crurrent.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#merge_data_views_to_crurrent.ApiResponseFor400) | Invalid input parameters

#### merge_data_views_to_crurrent.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### merge_data_views_to_crurrent.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **move_data_view_items**
<a id="move_data_view_items"></a>
> move_data_view_items(move_data_view_items_request)

Move data items between data views

Move data items from data view A to data view B

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.move_data_view_items_request import MoveDataViewItemsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    body = MoveDataViewItemsRequest(
        src_data_view_id="src_data_view_id_example",
        dst_data_view_id="dst_data_view_id_example",
    )
    try:
        # Move data items between data views
        api_response = api_instance.move_data_view_items(
            body=body,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->move_data_view_items: %s\n" % e)
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
[**MoveDataViewItemsRequest**](../../models/MoveDataViewItemsRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#move_data_view_items.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#move_data_view_items.ApiResponseFor400) | Invalid input parameters

#### move_data_view_items.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### move_data_view_items.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_dataset_zip_view**
<a id="update_dataset_zip_view"></a>
> update_dataset_zip_view(data_view_idupdate_dataset_zip_request)

Update a dataset-zip view meta

Update a dataset-zip view meta

### Example

```python
import aifs_client
from aifs_client.apis.tags import data_view_api
from aifs_client.model.update_dataset_zip_request import UpdateDatasetZipRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)

# Enter a context with an instance of the API client
with aifs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataViewId': "dataViewId_example",
    }
    body = UpdateDatasetZipRequest(
null,
        status="status_example",
        train_raw_data_view_id="train_raw_data_view_id_example",
        train_annotation_view_id="train_annotation_view_id_example",
        val_raw_data_view_id="val_raw_data_view_id_example",
        val_annotation_view_id="val_annotation_view_id_example",
        annotation_template_id="annotation_template_id_example",
        raw_data_view_id="raw_data_view_id_example",
        annotation_view_id="annotation_view_id_example",
    )
    try:
        # Update a dataset-zip view meta
        api_response = api_instance.update_dataset_zip_view(
            path_params=path_params,
            body=body,
        )
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->update_dataset_zip_view: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateDatasetZipRequest**](../../models/UpdateDatasetZipRequest.md) |  | 


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
200 | [ApiResponseFor200](#update_dataset_zip_view.ApiResponseFor200) | Successful operation
404 | [ApiResponseFor404](#update_dataset_zip_view.ApiResponseFor404) | data view not found

#### update_dataset_zip_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_dataset_zip_view.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

