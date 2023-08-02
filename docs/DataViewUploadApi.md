# aifs_client.DataViewUploadApi

All URIs are relative to *https://www.example.com/api/open/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_annotation_to_data_view**](DataViewUploadApi.md#upload_annotation_to_data_view) | **POST** /data-views/{dataViewId}/annotations | Upload annotations to data view
[**upload_dataset_zip_to_data_view**](DataViewUploadApi.md#upload_dataset_zip_to_data_view) | **POST** /data-views/{dataViewId}/dataset-zip | Upload dataset zip
[**upload_file_to_data_view**](DataViewUploadApi.md#upload_file_to_data_view) | **POST** /data-views/{dataViewId}/artifact | Upload file to data view
[**upload_model_data_to_data_view**](DataViewUploadApi.md#upload_model_data_to_data_view) | **POST** /data-views/{dataViewId}/model | Upload model data to data view
[**upload_raw_data_to_data_view**](DataViewUploadApi.md#upload_raw_data_to_data_view) | **POST** /data-views/{dataViewId}/raw-data | Upload raw data to data view


# **upload_annotation_to_data_view**
> upload_annotation_to_data_view(data_view_id)

Upload annotations to data view

Upload annotations to data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_upload_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_upload_api.DataViewUploadApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view
    file_meta = open('/path/to/file', 'rb') # file_type |  (optional)
    files = [
        open('/path/to/file', 'rb'),
    ] # [file_type] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload annotations to data view
        api_instance.upload_annotation_to_data_view(data_view_id)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_annotation_to_data_view: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload annotations to data view
        api_instance.upload_annotation_to_data_view(data_view_id, file_meta=file_meta, files=files)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_annotation_to_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |
 **file_meta** | **file_type**|  | [optional]
 **files** | **[file_type]**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_dataset_zip_to_data_view**
> upload_dataset_zip_to_data_view(data_view_id, x_file_name, body)

Upload dataset zip

Upload dataset zip

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_upload_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_upload_api.DataViewUploadApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view
    x_file_name = "X-File-Name_example" # str | 
    body = open('/path/to/file', 'rb') # file_type | 

    # example passing only required values which don't have defaults set
    try:
        # Upload dataset zip
        api_instance.upload_dataset_zip_to_data_view(data_view_id, x_file_name, body)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_dataset_zip_to_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |
 **x_file_name** | **str**|  |
 **body** | **file_type**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_to_data_view**
> upload_file_to_data_view(data_view_id, x_file_name, body)

Upload file to data view

Upload file to data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_upload_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_upload_api.DataViewUploadApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view
    x_file_name = "X-File-Name_example" # str | 
    body = open('/path/to/file', 'rb') # file_type | 

    # example passing only required values which don't have defaults set
    try:
        # Upload file to data view
        api_instance.upload_file_to_data_view(data_view_id, x_file_name, body)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_file_to_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |
 **x_file_name** | **str**|  |
 **body** | **file_type**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_model_data_to_data_view**
> upload_model_data_to_data_view(data_view_id)

Upload model data to data view

Upload model data to data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_upload_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_upload_api.DataViewUploadApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view
    commit_id = "commit_id_example" # str |  (optional)
    progress = "progress_example" # str |  (optional)
    model_jit = open('/path/to/file', 'rb') # file_type |  (optional)
    onnx = open('/path/to/file', 'rb') # file_type |  (optional)
    dynamic_onnx = open('/path/to/file', 'rb') # file_type |  (optional)
    config_py = open('/path/to/file', 'rb') # file_type |  (optional)
    best_pth = open('/path/to/file', 'rb') # file_type |  (optional)
    last_pth = open('/path/to/file', 'rb') # file_type |  (optional)
    output_template = open('/path/to/file', 'rb') # file_type |  (optional)
    logs = [
        open('/path/to/file', 'rb'),
    ] # [file_type] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload model data to data view
        api_instance.upload_model_data_to_data_view(data_view_id)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_model_data_to_data_view: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload model data to data view
        api_instance.upload_model_data_to_data_view(data_view_id, commit_id=commit_id, progress=progress, model_jit=model_jit, onnx=onnx, dynamic_onnx=dynamic_onnx, config_py=config_py, best_pth=best_pth, last_pth=last_pth, output_template=output_template, logs=logs)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_model_data_to_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |
 **commit_id** | **str**|  | [optional]
 **progress** | **str**|  | [optional]
 **model_jit** | **file_type**|  | [optional]
 **onnx** | **file_type**|  | [optional]
 **dynamic_onnx** | **file_type**|  | [optional]
 **config_py** | **file_type**|  | [optional]
 **best_pth** | **file_type**|  | [optional]
 **last_pth** | **file_type**|  | [optional]
 **output_template** | **file_type**|  | [optional]
 **logs** | **[file_type]**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | data view not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_raw_data_to_data_view**
> upload_raw_data_to_data_view(data_view_id)

Upload raw data to data view

Upload raw data to data view

### Example


```python
import time
import aifs_client
from aifs_client.api import data_view_upload_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.example.com/api/open/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = aifs_client.Configuration(
    host = "https://www.example.com/api/open/v1"
)


# Enter a context with an instance of the API client
with aifs_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_view_upload_api.DataViewUploadApi(api_client)
    data_view_id = "dataViewId_example" # str | The id of a data view
    files = [
        open('/path/to/file', 'rb'),
    ] # [file_type] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload raw data to data view
        api_instance.upload_raw_data_to_data_view(data_view_id)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_raw_data_to_data_view: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload raw data to data view
        api_instance.upload_raw_data_to_data_view(data_view_id, files=files)
    except aifs_client.ApiException as e:
        print("Exception when calling DataViewUploadApi->upload_raw_data_to_data_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_view_id** | **str**| The id of a data view |
 **files** | **[file_type]**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

