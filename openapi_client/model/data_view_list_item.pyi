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


class DataViewListItem(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
            name = schemas.StrSchema
        
            @staticmethod
            def viewType() -> typing.Type['DataViewType']:
                return DataViewType
        
            @staticmethod
            def rawDataType() -> typing.Type['RawDataType']:
                return RawDataType
            annotationTemplateId = schemas.UUIDSchema
            annotationTemplateType = schemas.StrSchema
            createAt = schemas.Int64Schema
            __annotations__ = {
                "id": id,
                "name": name,
                "viewType": viewType,
                "rawDataType": rawDataType,
                "annotationTemplateId": annotationTemplateId,
                "annotationTemplateType": annotationTemplateType,
                "createAt": createAt,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["viewType"]) -> 'DataViewType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rawDataType"]) -> 'RawDataType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annotationTemplateId"]) -> MetaOapg.properties.annotationTemplateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annotationTemplateType"]) -> MetaOapg.properties.annotationTemplateType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createAt"]) -> MetaOapg.properties.createAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "viewType", "rawDataType", "annotationTemplateId", "annotationTemplateType", "createAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["viewType"]) -> typing.Union['DataViewType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rawDataType"]) -> typing.Union['RawDataType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annotationTemplateId"]) -> typing.Union[MetaOapg.properties.annotationTemplateId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annotationTemplateType"]) -> typing.Union[MetaOapg.properties.annotationTemplateType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createAt"]) -> typing.Union[MetaOapg.properties.createAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "viewType", "rawDataType", "annotationTemplateId", "annotationTemplateType", "createAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        viewType: typing.Union['DataViewType', schemas.Unset] = schemas.unset,
        rawDataType: typing.Union['RawDataType', schemas.Unset] = schemas.unset,
        annotationTemplateId: typing.Union[MetaOapg.properties.annotationTemplateId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        annotationTemplateType: typing.Union[MetaOapg.properties.annotationTemplateType, str, schemas.Unset] = schemas.unset,
        createAt: typing.Union[MetaOapg.properties.createAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DataViewListItem':
        return super().__new__(
            cls,
            *_args,
            id=id,
            name=name,
            viewType=viewType,
            rawDataType=rawDataType,
            annotationTemplateId=annotationTemplateId,
            annotationTemplateType=annotationTemplateType,
            createAt=createAt,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.data_view_type import DataViewType
from openapi_client.model.raw_data_type import RawDataType