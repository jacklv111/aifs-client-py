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


class AnnotationListItem(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    the result of get annotation list
    """


    class MetaOapg:
        
        class properties:
            rawDataId = schemas.UUIDSchema
            dataItemId = schemas.UUIDSchema
            url = schemas.StrSchema
            
            
            class labels(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.UUIDSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, uuid.UUID, ]], typing.List[typing.Union[MetaOapg.items, str, uuid.UUID, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'labels':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "rawDataId": rawDataId,
                "dataItemId": dataItemId,
                "url": url,
                "labels": labels,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rawDataId"]) -> MetaOapg.properties.rawDataId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataItemId"]) -> MetaOapg.properties.dataItemId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labels"]) -> MetaOapg.properties.labels: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["rawDataId", "dataItemId", "url", "labels", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rawDataId"]) -> typing.Union[MetaOapg.properties.rawDataId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataItemId"]) -> typing.Union[MetaOapg.properties.dataItemId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labels"]) -> typing.Union[MetaOapg.properties.labels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["rawDataId", "dataItemId", "url", "labels", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        rawDataId: typing.Union[MetaOapg.properties.rawDataId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        dataItemId: typing.Union[MetaOapg.properties.dataItemId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        labels: typing.Union[MetaOapg.properties.labels, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AnnotationListItem':
        return super().__new__(
            cls,
            *_args,
            rawDataId=rawDataId,
            dataItemId=dataItemId,
            url=url,
            labels=labels,
            _configuration=_configuration,
            **kwargs,
        )
