# coding: utf-8

"""
    Aifs api

    aifs api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.data_views.post import CreateDataView
from openapi_client.paths.data_views_data_view_id_data_items.delete import DeleteDataItemInDataView
from openapi_client.paths.data_views_data_view_id.delete import DeleteDataView
from openapi_client.paths.data_views_data_view_id_raw_data_divide.post import DivideDataView
from openapi_client.paths.data_views_data_view_id_annotation_filter.post import FilterAnnotationsInDataView
from openapi_client.paths.data_views_data_view_id_annotation_data.get import GetAllAnnotationDataInDataView
from openapi_client.paths.data_views_data_view_id_annotation_locations.get import GetAllAnnotationLocationsInDataView
from openapi_client.paths.data_views_data_view_id_raw_data_locations.get import GetAllRawDataLocationsInDataView
from openapi_client.paths.data_views_data_view_id_annotations.get import GetAnnotationsInDataView
from openapi_client.paths.data_views_data_view_id_artifact_locations.get import GetArtifactLocationsInDataView
from openapi_client.paths.data_views_data_view_id_details.get import GetDataViewDetails
from openapi_client.paths.data_views.get import GetDataViewList
from openapi_client.paths.data_views_data_view_id_statistics.get import GetDataViewStatistics
from openapi_client.paths.data_views_data_view_id_dataset_zip_location.get import GetDatasetZipLocationInDataView
from openapi_client.paths.data_views_data_view_id_model_data_locations.get import GetModelDataLocationsInDataView
from openapi_client.paths.data_views_data_view_id_raw_data_hash_list.get import GetRawDataHashListInDataView
from openapi_client.paths.data_views_data_view_id_raw_data.get import GetRawDataInDataView
from openapi_client.paths.data_views_data_view_id_hard_delete.delete import HardDeleteDataView
from openapi_client.paths.data_views_merge.post import MergeDataViews
from openapi_client.paths.data_views_data_view_id_merge.post import MergeDataViewsToCrurrent
from openapi_client.paths.data_views_move.post import MoveDataViewItems
from openapi_client.paths.data_views_data_view_id_dataset_zip.put import UpdateDatasetZipView


class DataViewApi(
    CreateDataView,
    DeleteDataItemInDataView,
    DeleteDataView,
    DivideDataView,
    FilterAnnotationsInDataView,
    GetAllAnnotationDataInDataView,
    GetAllAnnotationLocationsInDataView,
    GetAllRawDataLocationsInDataView,
    GetAnnotationsInDataView,
    GetArtifactLocationsInDataView,
    GetDataViewDetails,
    GetDataViewList,
    GetDataViewStatistics,
    GetDatasetZipLocationInDataView,
    GetModelDataLocationsInDataView,
    GetRawDataHashListInDataView,
    GetRawDataInDataView,
    HardDeleteDataView,
    MergeDataViews,
    MergeDataViewsToCrurrent,
    MoveDataViewItems,
    UpdateDatasetZipView,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass