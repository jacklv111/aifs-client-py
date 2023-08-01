# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from aifs_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from aifs_client.model.annotation_data import AnnotationData
from aifs_client.model.annotation_list_item import AnnotationListItem
from aifs_client.model.annotation_template_details import AnnotationTemplateDetails
from aifs_client.model.annotation_template_list_item import AnnotationTemplateListItem
from aifs_client.model.annotation_template_type_list import AnnotationTemplateTypeList
from aifs_client.model.annotation_view_data import AnnotationViewData
from aifs_client.model.annotation_view_locations import AnnotationViewLocations
from aifs_client.model.artifact_locations import ArtifactLocations
from aifs_client.model.create_anno_template_success_resp import CreateAnnoTemplateSuccessResp
from aifs_client.model.create_annotation_template_request import CreateAnnotationTemplateRequest
from aifs_client.model.create_data_view_request import CreateDataViewRequest
from aifs_client.model.create_data_view_success_resp import CreateDataViewSuccessResp
from aifs_client.model.data_view_details import DataViewDetails
from aifs_client.model.data_view_list_item import DataViewListItem
from aifs_client.model.data_view_statistics import DataViewStatistics
from aifs_client.model.data_view_type import DataViewType
from aifs_client.model.dataset_zip_location import DatasetZipLocation
from aifs_client.model.divide_raw_data_data_view_request import DivideRawDataDataViewRequest
from aifs_client.model.divide_raw_data_data_view_response import DivideRawDataDataViewResponse
from aifs_client.model.error import Error
from aifs_client.model.filter_annotations_in_data_view_request import FilterAnnotationsInDataViewRequest
from aifs_client.model.filter_annotations_in_data_view_response import FilterAnnotationsInDataViewResponse
from aifs_client.model.fold_uri_type import FoldUriType
from aifs_client.model.image_data import ImageData
from aifs_client.model.key_point_def import KeyPointDef
from aifs_client.model.key_point_skeleton import KeyPointSkeleton
from aifs_client.model.label import Label
from aifs_client.model.label_distribution import LabelDistribution
from aifs_client.model.merge_data_views_request import MergeDataViewsRequest
from aifs_client.model.merge_data_views_success_resp import MergeDataViewsSuccessResp
from aifs_client.model.model_data_view_locations import ModelDataViewLocations
from aifs_client.model.move_data_view_items_request import MoveDataViewItemsRequest
from aifs_client.model.raw_data_hash_list import RawDataHashList
from aifs_client.model.raw_data_list_item import RawDataListItem
from aifs_client.model.raw_data_type import RawDataType
from aifs_client.model.raw_data_view_locations import RawDataViewLocations
from aifs_client.model.s3_storage import S3Storage
from aifs_client.model.time_fmt_in_ms import TimeFmtInMs
from aifs_client.model.update_annotation_template_request import UpdateAnnotationTemplateRequest
from aifs_client.model.update_dataset_zip_request import UpdateDatasetZipRequest
from aifs_client.model.upload_annotation_format import UploadAnnotationFormat
from aifs_client.model.word_list import WordList
from aifs_client.model.zip_format import ZipFormat
