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


class DataViewStatistics(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            itemCount = schemas.Int32Schema
            labelCount = schemas.Int32Schema
            
            
            class labelDistribution(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['LabelDistribution']:
                        return LabelDistribution
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['LabelDistribution'], typing.List['LabelDistribution']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'labelDistribution':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'LabelDistribution':
                    return super().__getitem__(i)
            totalDataSize = schemas.Int64Schema
            __annotations__ = {
                "itemCount": itemCount,
                "labelCount": labelCount,
                "labelDistribution": labelDistribution,
                "totalDataSize": totalDataSize,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["itemCount"]) -> MetaOapg.properties.itemCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labelCount"]) -> MetaOapg.properties.labelCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labelDistribution"]) -> MetaOapg.properties.labelDistribution: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalDataSize"]) -> MetaOapg.properties.totalDataSize: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["itemCount", "labelCount", "labelDistribution", "totalDataSize", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["itemCount"]) -> typing.Union[MetaOapg.properties.itemCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labelCount"]) -> typing.Union[MetaOapg.properties.labelCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labelDistribution"]) -> typing.Union[MetaOapg.properties.labelDistribution, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalDataSize"]) -> typing.Union[MetaOapg.properties.totalDataSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["itemCount", "labelCount", "labelDistribution", "totalDataSize", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        itemCount: typing.Union[MetaOapg.properties.itemCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        labelCount: typing.Union[MetaOapg.properties.labelCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        labelDistribution: typing.Union[MetaOapg.properties.labelDistribution, list, tuple, schemas.Unset] = schemas.unset,
        totalDataSize: typing.Union[MetaOapg.properties.totalDataSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DataViewStatistics':
        return super().__new__(
            cls,
            *_args,
            itemCount=itemCount,
            labelCount=labelCount,
            labelDistribution=labelDistribution,
            totalDataSize=totalDataSize,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.label_distribution import LabelDistribution
