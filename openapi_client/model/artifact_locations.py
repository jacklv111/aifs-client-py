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


class ArtifactLocations(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            dataViewId = schemas.UUIDSchema
        
            @staticmethod
            def viewType() -> typing.Type['DataViewType']:
                return DataViewType
        
            @staticmethod
            def dataItems() -> typing.Type['S3Storage']:
                return S3Storage
            __annotations__ = {
                "dataViewId": dataViewId,
                "viewType": viewType,
                "dataItems": dataItems,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataViewId"]) -> MetaOapg.properties.dataViewId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["viewType"]) -> 'DataViewType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataItems"]) -> 'S3Storage': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dataViewId", "viewType", "dataItems", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataViewId"]) -> typing.Union[MetaOapg.properties.dataViewId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["viewType"]) -> typing.Union['DataViewType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataItems"]) -> typing.Union['S3Storage', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dataViewId", "viewType", "dataItems", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        dataViewId: typing.Union[MetaOapg.properties.dataViewId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        viewType: typing.Union['DataViewType', schemas.Unset] = schemas.unset,
        dataItems: typing.Union['S3Storage', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ArtifactLocations':
        return super().__new__(
            cls,
            *_args,
            dataViewId=dataViewId,
            viewType=viewType,
            dataItems=dataItems,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.data_view_type import DataViewType
from openapi_client.model.s3_storage import S3Storage
