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


class S3Storage(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class items(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    dataItemId = schemas.UUIDSchema
                    dataName = schemas.StrSchema
                    objectKey = schemas.StrSchema
                    __annotations__ = {
                        "dataItemId": dataItemId,
                        "dataName": dataName,
                        "objectKey": objectKey,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["dataItemId"]) -> MetaOapg.properties.dataItemId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["dataName"]) -> MetaOapg.properties.dataName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["objectKey"]) -> MetaOapg.properties.objectKey: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["dataItemId", "dataName", "objectKey", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["dataItemId"]) -> typing.Union[MetaOapg.properties.dataItemId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["dataName"]) -> typing.Union[MetaOapg.properties.dataName, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["objectKey"]) -> typing.Union[MetaOapg.properties.objectKey, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dataItemId", "dataName", "objectKey", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                dataItemId: typing.Union[MetaOapg.properties.dataItemId, str, uuid.UUID, schemas.Unset] = schemas.unset,
                dataName: typing.Union[MetaOapg.properties.dataName, str, schemas.Unset] = schemas.unset,
                objectKey: typing.Union[MetaOapg.properties.objectKey, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *_args,
                    dataItemId=dataItemId,
                    dataName=dataName,
                    objectKey=objectKey,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'S3Storage':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)