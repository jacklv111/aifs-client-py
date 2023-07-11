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


class LabelDistribution(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            labelId = schemas.StrSchema
            count = schemas.Int32Schema
            ratio = schemas.Schema
            __annotations__ = {
                "labelId": labelId,
                "count": count,
                "ratio": ratio,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labelId"]) -> MetaOapg.properties.labelId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ratio"]) -> MetaOapg.properties.ratio: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["labelId", "count", "ratio", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labelId"]) -> typing.Union[MetaOapg.properties.labelId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ratio"]) -> typing.Union[MetaOapg.properties.ratio, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["labelId", "count", "ratio", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        labelId: typing.Union[MetaOapg.properties.labelId, str, schemas.Unset] = schemas.unset,
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ratio: typing.Union[MetaOapg.properties.ratio, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LabelDistribution':
        return super().__new__(
            cls,
            *_args,
            labelId=labelId,
            count=count,
            ratio=ratio,
            _configuration=_configuration,
            **kwargs,
        )
