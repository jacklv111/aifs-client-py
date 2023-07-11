# openapi_client.model.label.Label

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**color** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**name** | str,  | str,  | the name of the label | 
**id** | str, uuid.UUID,  | str,  | the id of the label | [optional] value must be a uuid
**superCategoryName** | str,  | str,  | the super category name | [optional] 
**keyPointDef** | [**KeyPointDef**](KeyPointDef.md) | [**KeyPointDef**](KeyPointDef.md) |  | [optional] 
**keyPointSkeleton** | [**KeyPointSkeleton**](KeyPointSkeleton.md) | [**KeyPointSkeleton**](KeyPointSkeleton.md) |  | [optional] 
**coverImageUrl** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

