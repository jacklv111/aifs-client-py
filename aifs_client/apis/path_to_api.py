import typing_extensions

from aifs_client.paths import PathValues
from aifs_client.apis.paths.annotation_template_types import AnnotationTemplateTypes
from aifs_client.apis.paths.annotation_templates import AnnotationTemplates
from aifs_client.apis.paths.annotation_templates_annotation_template_id import AnnotationTemplatesAnnotationTemplateId
from aifs_client.apis.paths.annotation_templates_annotation_template_id_copy import AnnotationTemplatesAnnotationTemplateIdCopy
from aifs_client.apis.paths.annotation_templates_annotation_template_id_details import AnnotationTemplatesAnnotationTemplateIdDetails
from aifs_client.apis.paths.data_views import DataViews
from aifs_client.apis.paths.data_views_merge import DataViewsMerge
from aifs_client.apis.paths.data_views_move import DataViewsMove
from aifs_client.apis.paths.data_views_data_view_id import DataViewsDataViewId
from aifs_client.apis.paths.data_views_data_view_id_merge import DataViewsDataViewIdMerge
from aifs_client.apis.paths.data_views_data_view_id_hard_delete import DataViewsDataViewIdHardDelete
from aifs_client.apis.paths.data_views_data_view_id_details import DataViewsDataViewIdDetails
from aifs_client.apis.paths.data_views_data_view_id_statistics import DataViewsDataViewIdStatistics
from aifs_client.apis.paths.data_views_data_view_id_raw_data import DataViewsDataViewIdRawData
from aifs_client.apis.paths.data_views_data_view_id_raw_data_hash_list import DataViewsDataViewIdRawDataHashList
from aifs_client.apis.paths.data_views_data_view_id_annotations import DataViewsDataViewIdAnnotations
from aifs_client.apis.paths.data_views_data_view_id_model import DataViewsDataViewIdModel
from aifs_client.apis.paths.data_views_data_view_id_artifact import DataViewsDataViewIdArtifact
from aifs_client.apis.paths.data_views_data_view_id_dataset_zip import DataViewsDataViewIdDatasetZip
from aifs_client.apis.paths.data_views_data_view_id_raw_data_divide import DataViewsDataViewIdRawDataDivide
from aifs_client.apis.paths.data_views_data_view_id_annotation_filter import DataViewsDataViewIdAnnotationFilter
from aifs_client.apis.paths.data_views_data_view_id_data_items import DataViewsDataViewIdDataItems
from aifs_client.apis.paths.data_views_data_view_id_raw_data_locations import DataViewsDataViewIdRawDataLocations
from aifs_client.apis.paths.data_views_data_view_id_model_data_locations import DataViewsDataViewIdModelDataLocations
from aifs_client.apis.paths.data_views_data_view_id_annotation_locations import DataViewsDataViewIdAnnotationLocations
from aifs_client.apis.paths.data_views_data_view_id_dataset_zip_location import DataViewsDataViewIdDatasetZipLocation
from aifs_client.apis.paths.data_views_data_view_id_artifact_locations import DataViewsDataViewIdArtifactLocations
from aifs_client.apis.paths.data_views_data_view_id_annotation_data import DataViewsDataViewIdAnnotationData

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ANNOTATIONTEMPLATETYPES: AnnotationTemplateTypes,
        PathValues.ANNOTATIONTEMPLATES: AnnotationTemplates,
        PathValues.ANNOTATIONTEMPLATES_ANNOTATION_TEMPLATE_ID: AnnotationTemplatesAnnotationTemplateId,
        PathValues.ANNOTATIONTEMPLATES_ANNOTATION_TEMPLATE_ID_COPY: AnnotationTemplatesAnnotationTemplateIdCopy,
        PathValues.ANNOTATIONTEMPLATES_ANNOTATION_TEMPLATE_ID_DETAILS: AnnotationTemplatesAnnotationTemplateIdDetails,
        PathValues.DATAVIEWS: DataViews,
        PathValues.DATAVIEWS_MERGE: DataViewsMerge,
        PathValues.DATAVIEWS_MOVE: DataViewsMove,
        PathValues.DATAVIEWS_DATA_VIEW_ID: DataViewsDataViewId,
        PathValues.DATAVIEWS_DATA_VIEW_ID_MERGE: DataViewsDataViewIdMerge,
        PathValues.DATAVIEWS_DATA_VIEW_ID_HARDDELETE: DataViewsDataViewIdHardDelete,
        PathValues.DATAVIEWS_DATA_VIEW_ID_DETAILS: DataViewsDataViewIdDetails,
        PathValues.DATAVIEWS_DATA_VIEW_ID_STATISTICS: DataViewsDataViewIdStatistics,
        PathValues.DATAVIEWS_DATA_VIEW_ID_RAWDATA: DataViewsDataViewIdRawData,
        PathValues.DATAVIEWS_DATA_VIEW_ID_RAWDATAHASHLIST: DataViewsDataViewIdRawDataHashList,
        PathValues.DATAVIEWS_DATA_VIEW_ID_ANNOTATIONS: DataViewsDataViewIdAnnotations,
        PathValues.DATAVIEWS_DATA_VIEW_ID_MODEL: DataViewsDataViewIdModel,
        PathValues.DATAVIEWS_DATA_VIEW_ID_ARTIFACT: DataViewsDataViewIdArtifact,
        PathValues.DATAVIEWS_DATA_VIEW_ID_DATASETZIP: DataViewsDataViewIdDatasetZip,
        PathValues.DATAVIEWS_DATA_VIEW_ID_RAWDATADIVIDE: DataViewsDataViewIdRawDataDivide,
        PathValues.DATAVIEWS_DATA_VIEW_ID_ANNOTATIONFILTER: DataViewsDataViewIdAnnotationFilter,
        PathValues.DATAVIEWS_DATA_VIEW_ID_DATAITEMS: DataViewsDataViewIdDataItems,
        PathValues.DATAVIEWS_DATA_VIEW_ID_RAWDATALOCATIONS: DataViewsDataViewIdRawDataLocations,
        PathValues.DATAVIEWS_DATA_VIEW_ID_MODELDATALOCATIONS: DataViewsDataViewIdModelDataLocations,
        PathValues.DATAVIEWS_DATA_VIEW_ID_ANNOTATIONLOCATIONS: DataViewsDataViewIdAnnotationLocations,
        PathValues.DATAVIEWS_DATA_VIEW_ID_DATASETZIPLOCATION: DataViewsDataViewIdDatasetZipLocation,
        PathValues.DATAVIEWS_DATA_VIEW_ID_ARTIFACTLOCATIONS: DataViewsDataViewIdArtifactLocations,
        PathValues.DATAVIEWS_DATA_VIEW_ID_ANNOTATIONDATA: DataViewsDataViewIdAnnotationData,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ANNOTATIONTEMPLATETYPES: AnnotationTemplateTypes,
        PathValues.ANNOTATIONTEMPLATES: AnnotationTemplates,
        PathValues.ANNOTATIONTEMPLATES_ANNOTATION_TEMPLATE_ID: AnnotationTemplatesAnnotationTemplateId,
        PathValues.ANNOTATIONTEMPLATES_ANNOTATION_TEMPLATE_ID_COPY: AnnotationTemplatesAnnotationTemplateIdCopy,
        PathValues.ANNOTATIONTEMPLATES_ANNOTATION_TEMPLATE_ID_DETAILS: AnnotationTemplatesAnnotationTemplateIdDetails,
        PathValues.DATAVIEWS: DataViews,
        PathValues.DATAVIEWS_MERGE: DataViewsMerge,
        PathValues.DATAVIEWS_MOVE: DataViewsMove,
        PathValues.DATAVIEWS_DATA_VIEW_ID: DataViewsDataViewId,
        PathValues.DATAVIEWS_DATA_VIEW_ID_MERGE: DataViewsDataViewIdMerge,
        PathValues.DATAVIEWS_DATA_VIEW_ID_HARDDELETE: DataViewsDataViewIdHardDelete,
        PathValues.DATAVIEWS_DATA_VIEW_ID_DETAILS: DataViewsDataViewIdDetails,
        PathValues.DATAVIEWS_DATA_VIEW_ID_STATISTICS: DataViewsDataViewIdStatistics,
        PathValues.DATAVIEWS_DATA_VIEW_ID_RAWDATA: DataViewsDataViewIdRawData,
        PathValues.DATAVIEWS_DATA_VIEW_ID_RAWDATAHASHLIST: DataViewsDataViewIdRawDataHashList,
        PathValues.DATAVIEWS_DATA_VIEW_ID_ANNOTATIONS: DataViewsDataViewIdAnnotations,
        PathValues.DATAVIEWS_DATA_VIEW_ID_MODEL: DataViewsDataViewIdModel,
        PathValues.DATAVIEWS_DATA_VIEW_ID_ARTIFACT: DataViewsDataViewIdArtifact,
        PathValues.DATAVIEWS_DATA_VIEW_ID_DATASETZIP: DataViewsDataViewIdDatasetZip,
        PathValues.DATAVIEWS_DATA_VIEW_ID_RAWDATADIVIDE: DataViewsDataViewIdRawDataDivide,
        PathValues.DATAVIEWS_DATA_VIEW_ID_ANNOTATIONFILTER: DataViewsDataViewIdAnnotationFilter,
        PathValues.DATAVIEWS_DATA_VIEW_ID_DATAITEMS: DataViewsDataViewIdDataItems,
        PathValues.DATAVIEWS_DATA_VIEW_ID_RAWDATALOCATIONS: DataViewsDataViewIdRawDataLocations,
        PathValues.DATAVIEWS_DATA_VIEW_ID_MODELDATALOCATIONS: DataViewsDataViewIdModelDataLocations,
        PathValues.DATAVIEWS_DATA_VIEW_ID_ANNOTATIONLOCATIONS: DataViewsDataViewIdAnnotationLocations,
        PathValues.DATAVIEWS_DATA_VIEW_ID_DATASETZIPLOCATION: DataViewsDataViewIdDatasetZipLocation,
        PathValues.DATAVIEWS_DATA_VIEW_ID_ARTIFACTLOCATIONS: DataViewsDataViewIdArtifactLocations,
        PathValues.DATAVIEWS_DATA_VIEW_ID_ANNOTATIONDATA: DataViewsDataViewIdAnnotationData,
    }
)
