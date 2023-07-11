# openapi_client.model.create_data_view_request.CreateDataViewRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dataViewName** | str,  | str,  | the name of the data view | [optional] 
**description** | str,  | str,  | the description of the data view | [optional] 
**viewType** | [**DataViewType**](DataViewType.md) | [**DataViewType**](DataViewType.md) |  | [optional] 
**rawDataType** | [**RawDataType**](RawDataType.md) | [**RawDataType**](RawDataType.md) |  | [optional] 
**zipFormat** | [**ZipFormat**](ZipFormat.md) | [**ZipFormat**](ZipFormat.md) |  | [optional] 
**relatedDataViewId** | str, uuid.UUID,  | str,  | If it is an annotation type data view, it must have a related raw-data data view | [optional] value must be a uuid
**annotationTemplateId** | str, uuid.UUID,  | str,  | If it is an annotation type data view, it must have a related annotation template id. If it is a dataset-zip data view, it can have an annotation template id to indicate the annotation template of the annotation data. | [optional] value must be a uuid
**rawDataViewId** | str, uuid.UUID,  | str,  | If it is a dataset-zip type data view, it can have a raw data view id to upload raw data to the data view | [optional] value must be a uuid
**annotationViewId** | str, uuid.UUID,  | str,  | If it is a dataset-zip type data view, it can have a annotation view id to upload annotation data to the data view | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

