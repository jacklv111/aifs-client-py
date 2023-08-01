# aifs_client.model.data_view_details.DataViewDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str, uuid.UUID,  | str,  | the id of the data view | [optional] value must be a uuid
**name** | str,  | str,  | the name of the data view | [optional] 
**viewType** | [**DataViewType**](DataViewType.md) | [**DataViewType**](DataViewType.md) |  | [optional] 
**description** | str,  | str,  | the description of the data view | [optional] 
**rawDataType** | [**RawDataType**](RawDataType.md) | [**RawDataType**](RawDataType.md) |  | [optional] 
**annotationTemplateType** | str,  | str,  | if data view is an annotation view, it has annotation template type | [optional] 
**createAt** | decimal.Decimal, int,  | decimal.Decimal,  | Unix timestamp in ms | [optional] value must be a 64 bit integer
**progress** |  |  |  | [optional] 
**commitId** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] 
**zipFormat** | [**ZipFormat**](ZipFormat.md) | [**ZipFormat**](ZipFormat.md) |  | [optional] 
**trainRawDataViewId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**trainAnnotationViewId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**valRawDataViewId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**valAnnotationViewId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**annotationTemplateId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**rawDataViewId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**annotationViewId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

