# aifs_client.model.annotation_template_details.AnnotationTemplateDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str, uuid.UUID,  | str,  | the id of the annotation template | [optional] value must be a uuid
**name** | str,  | str,  | name of the annotation template | [optional] 
**createAt** | decimal.Decimal, int,  | decimal.Decimal,  | Unix timestamp in ms | [optional] value must be a 64 bit integer
**updateAt** | decimal.Decimal, int,  | decimal.Decimal,  | Unix timestamp in ms | [optional] value must be a 64 bit integer
**type** | str,  | str,  | the type of the annotation template | [optional] 
**[labels](#labels)** | list, tuple,  | tuple,  |  | [optional] 
**wordList** | [**WordList**](WordList.md) | [**WordList**](WordList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Label**](Label.md) | [**Label**](Label.md) | [**Label**](Label.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

