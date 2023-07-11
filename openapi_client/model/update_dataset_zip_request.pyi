# coding: utf-8

"""
    Aifs api

    aifs api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class UpdateDatasetZipRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            progress = schemas.Schema
            status = schemas.StrSchema
            trainRawDataViewId = schemas.UUIDSchema
            trainAnnotationViewId = schemas.UUIDSchema
            valRawDataViewId = schemas.UUIDSchema
            valAnnotationViewId = schemas.UUIDSchema
            annotationTemplateId = schemas.UUIDSchema
            rawDataViewId = schemas.UUIDSchema
            annotationViewId = schemas.UUIDSchema
            __annotations__ = {
                "progress": progress,
                "status": status,
                "trainRawDataViewId": trainRawDataViewId,
                "trainAnnotationViewId": trainAnnotationViewId,
                "valRawDataViewId": valRawDataViewId,
                "valAnnotationViewId": valAnnotationViewId,
                "annotationTemplateId": annotationTemplateId,
                "rawDataViewId": rawDataViewId,
                "annotationViewId": annotationViewId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["progress"]) -> MetaOapg.properties.progress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainRawDataViewId"]) -> MetaOapg.properties.trainRawDataViewId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainAnnotationViewId"]) -> MetaOapg.properties.trainAnnotationViewId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["valRawDataViewId"]) -> MetaOapg.properties.valRawDataViewId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["valAnnotationViewId"]) -> MetaOapg.properties.valAnnotationViewId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annotationTemplateId"]) -> MetaOapg.properties.annotationTemplateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rawDataViewId"]) -> MetaOapg.properties.rawDataViewId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annotationViewId"]) -> MetaOapg.properties.annotationViewId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["progress", "status", "trainRawDataViewId", "trainAnnotationViewId", "valRawDataViewId", "valAnnotationViewId", "annotationTemplateId", "rawDataViewId", "annotationViewId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["progress"]) -> typing.Union[MetaOapg.properties.progress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainRawDataViewId"]) -> typing.Union[MetaOapg.properties.trainRawDataViewId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainAnnotationViewId"]) -> typing.Union[MetaOapg.properties.trainAnnotationViewId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["valRawDataViewId"]) -> typing.Union[MetaOapg.properties.valRawDataViewId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["valAnnotationViewId"]) -> typing.Union[MetaOapg.properties.valAnnotationViewId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annotationTemplateId"]) -> typing.Union[MetaOapg.properties.annotationTemplateId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rawDataViewId"]) -> typing.Union[MetaOapg.properties.rawDataViewId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annotationViewId"]) -> typing.Union[MetaOapg.properties.annotationViewId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["progress", "status", "trainRawDataViewId", "trainAnnotationViewId", "valRawDataViewId", "valAnnotationViewId", "annotationTemplateId", "rawDataViewId", "annotationViewId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        progress: typing.Union[MetaOapg.properties.progress, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        trainRawDataViewId: typing.Union[MetaOapg.properties.trainRawDataViewId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        trainAnnotationViewId: typing.Union[MetaOapg.properties.trainAnnotationViewId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        valRawDataViewId: typing.Union[MetaOapg.properties.valRawDataViewId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        valAnnotationViewId: typing.Union[MetaOapg.properties.valAnnotationViewId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        annotationTemplateId: typing.Union[MetaOapg.properties.annotationTemplateId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        rawDataViewId: typing.Union[MetaOapg.properties.rawDataViewId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        annotationViewId: typing.Union[MetaOapg.properties.annotationViewId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateDatasetZipRequest':
        return super().__new__(
            cls,
            *_args,
            progress=progress,
            status=status,
            trainRawDataViewId=trainRawDataViewId,
            trainAnnotationViewId=trainAnnotationViewId,
            valRawDataViewId=valRawDataViewId,
            valAnnotationViewId=valAnnotationViewId,
            annotationTemplateId=annotationTemplateId,
            rawDataViewId=rawDataViewId,
            annotationViewId=annotationViewId,
            _configuration=_configuration,
            **kwargs,
        )