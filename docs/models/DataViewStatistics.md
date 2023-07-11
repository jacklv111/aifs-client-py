# openapi_client.model.data_view_statistics.DataViewStatistics

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**itemCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**labelCount** | decimal.Decimal, int,  | decimal.Decimal,  | the number of labels in the annotation data view. | [optional] value must be a 32 bit integer
**[labelDistribution](#labelDistribution)** | list, tuple,  | tuple,  | the distribution of labels in the annotation data view. | [optional] 
**totalDataSize** | decimal.Decimal, int,  | decimal.Decimal,  | the total size of the data in the data view in bytes. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# labelDistribution

the distribution of labels in the annotation data view.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the distribution of labels in the annotation data view. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LabelDistribution**](LabelDistribution.md) | [**LabelDistribution**](LabelDistribution.md) | [**LabelDistribution**](LabelDistribution.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

