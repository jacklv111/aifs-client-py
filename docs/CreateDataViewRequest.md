# CreateDataViewRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_view_name** | **str** | the name of the data view | [optional] 
**description** | **str** | the description of the data view | [optional] 
**view_type** | [**DataViewType**](DataViewType.md) |  | [optional] 
**raw_data_type** | [**RawDataType**](RawDataType.md) |  | [optional] 
**zip_format** | [**ZipFormat**](ZipFormat.md) |  | [optional] 
**related_data_view_id** | **str** | If it is an annotation type data view, it must have a related raw-data data view | [optional] 
**annotation_template_id** | **str** | If it is an annotation type data view, it must have a related annotation template id. If it is a dataset-zip data view, it can have an annotation template id to indicate the annotation template of the annotation data. | [optional] 
**raw_data_view_id** | **str** | If it is a dataset-zip type data view, it can have a raw data view id to upload raw data to the data view | [optional] 
**annotation_view_id** | **str** | If it is a dataset-zip type data view, it can have a annotation view id to upload annotation data to the data view | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


