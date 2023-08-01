# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from aifs_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ANNOTATIONTEMPLATETYPES = "/annotation-template-types"
    ANNOTATIONTEMPLATES = "/annotation-templates"
    ANNOTATIONTEMPLATES_ANNOTATION_TEMPLATE_ID = "/annotation-templates/{annotationTemplateId}"
    ANNOTATIONTEMPLATES_ANNOTATION_TEMPLATE_ID_COPY = "/annotation-templates/{annotationTemplateId}/copy"
    ANNOTATIONTEMPLATES_ANNOTATION_TEMPLATE_ID_DETAILS = "/annotation-templates/{annotationTemplateId}/details"
    DATAVIEWS = "/data-views"
    DATAVIEWS_MERGE = "/data-views/merge"
    DATAVIEWS_MOVE = "/data-views/move"
    DATAVIEWS_DATA_VIEW_ID = "/data-views/{dataViewId}"
    DATAVIEWS_DATA_VIEW_ID_MERGE = "/data-views/{dataViewId}/merge"
    DATAVIEWS_DATA_VIEW_ID_HARDDELETE = "/data-views/{dataViewId}/hard-delete"
    DATAVIEWS_DATA_VIEW_ID_DETAILS = "/data-views/{dataViewId}/details"
    DATAVIEWS_DATA_VIEW_ID_STATISTICS = "/data-views/{dataViewId}/statistics"
    DATAVIEWS_DATA_VIEW_ID_RAWDATA = "/data-views/{dataViewId}/raw-data"
    DATAVIEWS_DATA_VIEW_ID_RAWDATAHASHLIST = "/data-views/{dataViewId}/raw-data-hash-list"
    DATAVIEWS_DATA_VIEW_ID_ANNOTATIONS = "/data-views/{dataViewId}/annotations"
    DATAVIEWS_DATA_VIEW_ID_MODEL = "/data-views/{dataViewId}/model"
    DATAVIEWS_DATA_VIEW_ID_ARTIFACT = "/data-views/{dataViewId}/artifact"
    DATAVIEWS_DATA_VIEW_ID_DATASETZIP = "/data-views/{dataViewId}/dataset-zip"
    DATAVIEWS_DATA_VIEW_ID_RAWDATADIVIDE = "/data-views/{dataViewId}/raw-data-divide"
    DATAVIEWS_DATA_VIEW_ID_ANNOTATIONFILTER = "/data-views/{dataViewId}/annotation-filter"
    DATAVIEWS_DATA_VIEW_ID_DATAITEMS = "/data-views/{dataViewId}/data-items"
    DATAVIEWS_DATA_VIEW_ID_RAWDATALOCATIONS = "/data-views/{dataViewId}/raw-data-locations"
    DATAVIEWS_DATA_VIEW_ID_MODELDATALOCATIONS = "/data-views/{dataViewId}/model-data-locations"
    DATAVIEWS_DATA_VIEW_ID_ANNOTATIONLOCATIONS = "/data-views/{dataViewId}/annotation-locations"
    DATAVIEWS_DATA_VIEW_ID_DATASETZIPLOCATION = "/data-views/{dataViewId}/dataset-zip-location"
    DATAVIEWS_DATA_VIEW_ID_ARTIFACTLOCATIONS = "/data-views/{dataViewId}/artifact-locations"
    DATAVIEWS_DATA_VIEW_ID_ANNOTATIONDATA = "/data-views/{dataViewId}/annotation-data"
