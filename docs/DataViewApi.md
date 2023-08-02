# aifs_client.DataViewApi

All URIs are relative to *https://www.example.com/api/open/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_view**](DataViewApi.md#create_data_view) | **POST** /data-views | Create a data view
[**delete_data_item_in_data_view**](DataViewApi.md#delete_data_item_in_data_view) | **DELETE** /data-views/{dataViewId}/data-items | Delete data item in a data view
[**delete_data_view**](DataViewApi.md#delete_data_view) | **DELETE** /data-views/{dataViewId} | Delete a data view
[**divide_data_view**](DataViewApi.md#divide_data_view) | **POST** /data-views/{dataViewId}/raw-data-divide | Divide data view
[**filter_annotations_in_data_view**](DataViewApi.md#filter_annotations_in_data_view) | **POST** /data-views/{dataViewId}/annotation-filter | Filter annotations in a data view
[**get_all_annotation_data_in_data_view**](DataViewApi.md#get_all_annotation_data_in_data_view) | **GET** /data-views/{dataViewId}/annotation-data | Get all annotation data in a data view
[**get_all_annotation_locations_in_data_view**](DataViewApi.md#get_all_annotation_locations_in_data_view) | **GET** /data-views/{dataViewId}/annotation-locations | Get all annotation locations in a data view
[**get_all_raw_data_locations_in_data_view**](DataViewApi.md#get_all_raw_data_locations_in_data_view) | **GET** /data-views/{dataViewId}/raw-data-locations | Get all raw data locations in a data view
[**get_annotations_in_data_view**](DataViewApi.md#get_annotations_in_data_view) | **GET** /data-views/{dataViewId}/annotations | Get data view annotations
[**get_artifact_locations_in_data_view**](DataViewApi.md#get_artifact_locations_in_data_view) | **GET** /data-views/{dataViewId}/artifact-locations | Get files&#39; locations in artifact data view
[**get_data_view_details**](DataViewApi.md#get_data_view_details) | **GET** /data-views/{dataViewId}/details | Get data view details
[**get_data_view_list**](DataViewApi.md#get_data_view_list) | **GET** /data-views | Get data view list
[**get_data_view_statistics**](DataViewApi.md#get_data_view_statistics) | **GET** /data-views/{dataViewId}/statistics | Get data view statistics
[**get_dataset_zip_location_in_data_view**](DataViewApi.md#get_dataset_zip_location_in_data_view) | **GET** /data-views/{dataViewId}/dataset-zip-location | Get dataset zip&#39;s location in a data view
[**get_model_data_locations_in_data_view**](DataViewApi.md#get_model_data_locations_in_data_view) | **GET** /data-views/{dataViewId}/model-data-locations | Get all model data locations in a data view
[**get_raw_data_hash_list_in_data_view**](DataViewApi.md#get_raw_data_hash_list_in_data_view) | **GET** /data-views/{dataViewId}/raw-data-hash-list | Get data view raw data hash list
[**get_raw_data_in_data_view**](DataViewApi.md#get_raw_data_in_data_view) | **GET** /data-views/{dataViewId}/raw-data | Get data view raw data
[**hard_delete_data_view**](DataViewApi.md#hard_delete_data_view) | **DELETE** /data-views/{dataViewId}/hard-delete | Hard delete a data view
[**merge_data_views**](DataViewApi.md#merge_data_views) | **POST** /data-views/merge | Merge data views
[**merge_data_views_to_crurrent**](DataViewApi.md#merge_data_views_to_crurrent) | **POST** /data-views/{dataViewId}/merge | Merge data views
[**move_data_view_items**](DataViewApi.md#move_data_view_items) | **POST** /data-views/move | Move data items between data views
[**update_dataset_zip_view**](DataViewApi.md#update_dataset_zip_view) | **PUT** /data-views/{dataViewId}/dataset-zip | Update a dataset-zip view meta


# **create_data_view**
> CreateDataViewSuccessResp create_data_view(create_data_view_request)

Create a data view

Create a data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.create_data_view_request import CreateDataViewRequest
from aifs_client.model.create_data_view_success_resp import CreateDataViewSuccessResp
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    create_data_view_request = CreateDataViewRequest(
        data_view_name="data_view_name_example",
        description="description_example",
        view_type=DataViewType("raw-data"),
        raw_data_type=RawDataType("image"),
        zip_format=ZipFormat("image-classification"),
        related_data_view_id="related_data_view_id_example",
        annotation_template_id="annotation_template_id_example",
        raw_data_view_id="raw_data_view_id_example",
        annotation_view_id="annotation_view_id_example",
    ) # CreateDataViewRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a data view
        api_response = api_instance.create_data_view(create_data_view_request)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->create_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_data_view_request** | [**CreateDataViewRequest**](CreateDataViewRequest.md)|  |

### Return type

[**CreateDataViewSuccessResp**](CreateDataViewSuccessResp.md)

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

# **delete_data_item_in_data_view**
> delete_data_item_in_data_view(data_view_id, data_view_item_id_list)

Delete data item in a data view

Delete data item in a data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view
    data_view_item_id_list = [
        "dataViewItemIdList_example",
    ] # [str] | ids of raw data which are expected to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Delete data item in a data view
        api_instance.delete_data_item_in_data_view(data_view_id, data_view_item_id_list)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->delete_data_item_in_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |
 **data_view_item_id_list** | **[str]**| ids of raw data which are expected to be deleted |

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
**404** | data item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_view**
> delete_data_view(data_view_id)

Delete a data view

Delete a data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view

    # example passing only required values which don't have defaults set
    try:
        # Delete a data view
        api_instance.delete_data_view(data_view_id)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->delete_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |

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
**404** | Data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **divide_data_view**
> DivideRawDataDataViewResponse divide_data_view(data_view_id, divide_raw_data_data_view_request)

Divide data view

Divide data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.divide_raw_data_data_view_response import DivideRawDataDataViewResponse
from aifs_client.model.divide_raw_data_data_view_request import DivideRawDataDataViewRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view
    divide_raw_data_data_view_request = DivideRawDataDataViewRequest([
        DivideRawDataDataViewRequestInner(
            name="name_example",
            description="description_example",
            ratio=1,
        ),
    ]) # DivideRawDataDataViewRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Divide data view
        api_response = api_instance.divide_data_view(data_view_id, divide_raw_data_data_view_request)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->divide_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |
 **divide_raw_data_data_view_request** | [**DivideRawDataDataViewRequest**](DivideRawDataDataViewRequest.md)|  |

### Return type

[**DivideRawDataDataViewResponse**](DivideRawDataDataViewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_annotations_in_data_view**
> FilterAnnotationsInDataViewResponse filter_annotations_in_data_view(data_view_id, filter_annotations_in_data_view_request)

Filter annotations in a data view

Filter annotations in a data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.filter_annotations_in_data_view_request import FilterAnnotationsInDataViewRequest
from aifs_client.model.filter_annotations_in_data_view_response import FilterAnnotationsInDataViewResponse
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view
    filter_annotations_in_data_view_request = FilterAnnotationsInDataViewRequest(
        raw_data_view_id="raw_data_view_id_example",
    ) # FilterAnnotationsInDataViewRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Filter annotations in a data view
        api_response = api_instance.filter_annotations_in_data_view(data_view_id, filter_annotations_in_data_view_request)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->filter_annotations_in_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |
 **filter_annotations_in_data_view_request** | [**FilterAnnotationsInDataViewRequest**](FilterAnnotationsInDataViewRequest.md)|  |

### Return type

[**FilterAnnotationsInDataViewResponse**](FilterAnnotationsInDataViewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_annotation_data_in_data_view**
> AnnotationViewData get_all_annotation_data_in_data_view(data_view_id)

Get all annotation data in a data view

Get all annotation data in a data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.annotation_view_data import AnnotationViewData
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view

    # example passing only required values which don't have defaults set
    try:
        # Get all annotation data in a data view
        api_response = api_instance.get_all_annotation_data_in_data_view(data_view_id)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_all_annotation_data_in_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |

### Return type

[**AnnotationViewData**](AnnotationViewData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_annotation_locations_in_data_view**
> AnnotationViewLocations get_all_annotation_locations_in_data_view(data_view_id)

Get all annotation locations in a data view

Get all annotation locations in a data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.annotation_view_locations import AnnotationViewLocations
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view

    # example passing only required values which don't have defaults set
    try:
        # Get all annotation locations in a data view
        api_response = api_instance.get_all_annotation_locations_in_data_view(data_view_id)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_all_annotation_locations_in_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |

### Return type

[**AnnotationViewLocations**](AnnotationViewLocations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_raw_data_locations_in_data_view**
> RawDataViewLocations get_all_raw_data_locations_in_data_view(data_view_id)

Get all raw data locations in a data view

Get all raw data locations in a data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.raw_data_view_locations import RawDataViewLocations
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view

    # example passing only required values which don't have defaults set
    try:
        # Get all raw data locations in a data view
        api_response = api_instance.get_all_raw_data_locations_in_data_view(data_view_id)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_all_raw_data_locations_in_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |

### Return type

[**RawDataViewLocations**](RawDataViewLocations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_annotations_in_data_view**
> GetAnnotationsInDataView200Response get_annotations_in_data_view(data_view_id)

Get data view annotations

Get data view annotations

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.get_annotations_in_data_view200_response import GetAnnotationsInDataView200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view
    offset = 0 # int | The number of items to skip before starting to collect the result set (optional) if omitted the server will use the default value of 0
    limit = 10 # int | The numbers of items to return (optional) if omitted the server will use the default value of 10
    raw_data_id_list = [
        "rawDataIdList_example",
    ] # [str] | ids of raw data (optional)
    label_id = "labelId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get data view annotations
        api_response = api_instance.get_annotations_in_data_view(data_view_id)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_annotations_in_data_view: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data view annotations
        api_response = api_instance.get_annotations_in_data_view(data_view_id, offset=offset, limit=limit, raw_data_id_list=raw_data_id_list, label_id=label_id)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_annotations_in_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |
 **offset** | **int**| The number of items to skip before starting to collect the result set | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of items to return | [optional] if omitted the server will use the default value of 10
 **raw_data_id_list** | **[str]**| ids of raw data | [optional]
 **label_id** | **str**|  | [optional]

### Return type

[**GetAnnotationsInDataView200Response**](GetAnnotationsInDataView200Response.md)

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

# **get_artifact_locations_in_data_view**
> ArtifactLocations get_artifact_locations_in_data_view(data_view_id)

Get files' locations in artifact data view

Get files' locations in artifact data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.artifact_locations import ArtifactLocations
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view

    # example passing only required values which don't have defaults set
    try:
        # Get files' locations in artifact data view
        api_response = api_instance.get_artifact_locations_in_data_view(data_view_id)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_artifact_locations_in_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |

### Return type

[**ArtifactLocations**](ArtifactLocations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_view_details**
> DataViewDetails get_data_view_details(data_view_id)

Get data view details

Get data view details

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.data_view_details import DataViewDetails
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view

    # example passing only required values which don't have defaults set
    try:
        # Get data view details
        api_response = api_instance.get_data_view_details(data_view_id)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_data_view_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |

### Return type

[**DataViewDetails**](DataViewDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_view_list**
> [DataViewListItem] get_data_view_list()

Get data view list

Get data view list

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.data_view_list_item import DataViewListItem
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    offset = 0 # int | The number of items to skip before starting to collect the result set (optional) if omitted the server will use the default value of 0
    limit = 10 # int | The numbers of items to return (optional) if omitted the server will use the default value of 10
    data_view_id_list = "aaa,bbb,ccc" # str | data view with id in data view id list will be got (optional)
    data_view_name = "hand" # str | data view name filter, support fuzzy query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data view list
        api_response = api_instance.get_data_view_list(offset=offset, limit=limit, data_view_id_list=data_view_id_list, data_view_name=data_view_name)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_data_view_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip before starting to collect the result set | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of items to return | [optional] if omitted the server will use the default value of 10
 **data_view_id_list** | **str**| data view with id in data view id list will be got | [optional]
 **data_view_name** | **str**| data view name filter, support fuzzy query | [optional]

### Return type

[**[DataViewListItem]**](DataViewListItem.md)

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

# **get_data_view_statistics**
> DataViewStatistics get_data_view_statistics(data_view_id)

Get data view statistics

Get data view statistics

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.data_view_statistics import DataViewStatistics
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view

    # example passing only required values which don't have defaults set
    try:
        # Get data view statistics
        api_response = api_instance.get_data_view_statistics(data_view_id)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_data_view_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |

### Return type

[**DataViewStatistics**](DataViewStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_zip_location_in_data_view**
> DatasetZipLocation get_dataset_zip_location_in_data_view(data_view_id)

Get dataset zip's location in a data view

Get dataset zip's location in a data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.dataset_zip_location import DatasetZipLocation
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view

    # example passing only required values which don't have defaults set
    try:
        # Get dataset zip's location in a data view
        api_response = api_instance.get_dataset_zip_location_in_data_view(data_view_id)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_dataset_zip_location_in_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |

### Return type

[**DatasetZipLocation**](DatasetZipLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_data_locations_in_data_view**
> ModelDataViewLocations get_model_data_locations_in_data_view(data_view_id)

Get all model data locations in a data view

Get all model data locations in a data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.model_data_view_locations import ModelDataViewLocations
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view

    # example passing only required values which don't have defaults set
    try:
        # Get all model data locations in a data view
        api_response = api_instance.get_model_data_locations_in_data_view(data_view_id)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_model_data_locations_in_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |

### Return type

[**ModelDataViewLocations**](ModelDataViewLocations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not foundF |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_data_hash_list_in_data_view**
> RawDataHashList get_raw_data_hash_list_in_data_view(data_view_id)

Get data view raw data hash list

Get data view raw data hash list.

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.raw_data_hash_list import RawDataHashList
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view
    offset = 0 # int | The number of items to skip before starting to collect the result set (optional) if omitted the server will use the default value of 0
    limit = 10 # int | The numbers of items to return (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Get data view raw data hash list
        api_response = api_instance.get_raw_data_hash_list_in_data_view(data_view_id)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_raw_data_hash_list_in_data_view: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data view raw data hash list
        api_response = api_instance.get_raw_data_hash_list_in_data_view(data_view_id, offset=offset, limit=limit)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_raw_data_hash_list_in_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |
 **offset** | **int**| The number of items to skip before starting to collect the result set | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of items to return | [optional] if omitted the server will use the default value of 10

### Return type

[**RawDataHashList**](RawDataHashList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_data_in_data_view**
> GetRawDataInDataView200Response get_raw_data_in_data_view(data_view_id)

Get data view raw data

Get data view raw data

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.get_raw_data_in_data_view200_response import GetRawDataInDataView200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view
    offset = 0 # int | The number of items to skip before starting to collect the result set (optional) if omitted the server will use the default value of 0
    limit = 10 # int | The numbers of items to return (optional) if omitted the server will use the default value of 10
    raw_data_id_list = [
        "rawDataIdList_example",
    ] # [str] | ids of raw data (optional)
    excluded_annotation_view_id = "excludedAnnotationViewId_example" # str | excluded annotation view with id. Return the raw data items which have no annotation in the annotation view. (optional)
    included_annotation_view_id = "includedAnnotationViewId_example" # str | included annotation view with id. Return the raw data items which have annotation in the annotation view. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get data view raw data
        api_response = api_instance.get_raw_data_in_data_view(data_view_id)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_raw_data_in_data_view: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data view raw data
        api_response = api_instance.get_raw_data_in_data_view(data_view_id, offset=offset, limit=limit, raw_data_id_list=raw_data_id_list, excluded_annotation_view_id=excluded_annotation_view_id, included_annotation_view_id=included_annotation_view_id)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->get_raw_data_in_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |
 **offset** | **int**| The number of items to skip before starting to collect the result set | [optional] if omitted the server will use the default value of 0
 **limit** | **int**| The numbers of items to return | [optional] if omitted the server will use the default value of 10
 **raw_data_id_list** | **[str]**| ids of raw data | [optional]
 **excluded_annotation_view_id** | **str**| excluded annotation view with id. Return the raw data items which have no annotation in the annotation view. | [optional]
 **included_annotation_view_id** | **str**| included annotation view with id. Return the raw data items which have annotation in the annotation view. | [optional]

### Return type

[**GetRawDataInDataView200Response**](GetRawDataInDataView200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hard_delete_data_view**
> hard_delete_data_view(data_view_id)

Hard delete a data view

Hard delete a data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view

    # example passing only required values which don't have defaults set
    try:
        # Hard delete a data view
        api_instance.hard_delete_data_view(data_view_id)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->hard_delete_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |

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
**404** | Data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_data_views**
> MergeDataViewsSuccessResp merge_data_views(merge_data_views_request)

Merge data views

Merge data views, generate a new data view to put the result

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.merge_data_views_request import MergeDataViewsRequest
from aifs_client.model.merge_data_views_success_resp import MergeDataViewsSuccessResp
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    merge_data_views_request = MergeDataViewsRequest(
        name="name_example",
        description="description_example",
        data_view_id_list=[
            "data_view_id_list_example",
        ],
    ) # MergeDataViewsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Merge data views
        api_response = api_instance.merge_data_views(merge_data_views_request)
        pprint(api_response)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->merge_data_views: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_data_views_request** | [**MergeDataViewsRequest**](MergeDataViewsRequest.md)|  |

### Return type

[**MergeDataViewsSuccessResp**](MergeDataViewsSuccessResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid input parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_data_views_to_crurrent**
> merge_data_views_to_crurrent(data_view_id, merge_data_views_request)

Merge data views

Merge other data views to current data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.merge_data_views_request import MergeDataViewsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view
    merge_data_views_request = MergeDataViewsRequest(
        name="name_example",
        description="description_example",
        data_view_id_list=[
            "data_view_id_list_example",
        ],
    ) # MergeDataViewsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Merge data views
        api_instance.merge_data_views_to_crurrent(data_view_id, merge_data_views_request)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->merge_data_views_to_crurrent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |
 **merge_data_views_request** | [**MergeDataViewsRequest**](MergeDataViewsRequest.md)|  |

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
**400** | Invalid input parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_data_view_items**
> move_data_view_items(move_data_view_items_request)

Move data items between data views

Move data items from data view A to data view B

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.move_data_view_items_request import MoveDataViewItemsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    move_data_view_items_request = MoveDataViewItemsRequest(
        src_data_view_id="src_data_view_id_example",
        dst_data_view_id="dst_data_view_id_example",
    ) # MoveDataViewItemsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Move data items between data views
        api_instance.move_data_view_items(move_data_view_items_request)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->move_data_view_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_data_view_items_request** | [**MoveDataViewItemsRequest**](MoveDataViewItemsRequest.md)|  |

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
**400** | Invalid input parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset_zip_view**
> update_dataset_zip_view(data_view_id, update_dataset_zip_request)

Update a dataset-zip view meta

Update a dataset-zip view meta

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_api
from aifs_client.model.update_dataset_zip_request import UpdateDatasetZipRequest
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_api.DataViewApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view
    update_dataset_zip_request = UpdateDatasetZipRequest(
null,
        status="status_example",
        train_raw_data_view_id="train_raw_data_view_id_example",
        train_annotation_view_id="train_annotation_view_id_example",
        val_raw_data_view_id="val_raw_data_view_id_example",
        val_annotation_view_id="val_annotation_view_id_example",
        annotation_template_id="annotation_template_id_example",
        raw_data_view_id="raw_data_view_id_example",
        annotation_view_id="annotation_view_id_example",
    ) # UpdateDatasetZipRequest | Update an existed dataset-zip view's meta

    # example passing only required values which don't have defaults set
    try:
        # Update a dataset-zip view meta
        api_instance.update_dataset_zip_view(data_view_id, update_dataset_zip_request)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewApi->update_dataset_zip_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |
 **update_dataset_zip_request** | [**UpdateDatasetZipRequest**](UpdateDatasetZipRequest.md)| Update an existed dataset-zip view&#39;s meta |

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
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

