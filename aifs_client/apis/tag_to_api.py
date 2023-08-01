import typing_extensions

from aifs_client.apis.tags import TagValues
from aifs_client.apis.tags.annotation_template_type_api import AnnotationTemplateTypeApi
from aifs_client.apis.tags.annotation_template_api import AnnotationTemplateApi
from aifs_client.apis.tags.data_view_api import DataViewApi
from aifs_client.apis.tags.data_view_upload_api import DataViewUploadApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ANNOTATION_TEMPLATE_TYPE: AnnotationTemplateTypeApi,
        TagValues.ANNOTATION_TEMPLATE: AnnotationTemplateApi,
        TagValues.DATA_VIEW: DataViewApi,
        TagValues.DATA_VIEW_UPLOAD: DataViewUploadApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ANNOTATION_TEMPLATE_TYPE: AnnotationTemplateTypeApi,
        TagValues.ANNOTATION_TEMPLATE: AnnotationTemplateApi,
        TagValues.DATA_VIEW: DataViewApi,
        TagValues.DATA_VIEW_UPLOAD: DataViewUploadApi,
    }
)
