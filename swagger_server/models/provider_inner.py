# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ProviderInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, provider_id: int=None, uuid: str=None, name: str=None, uri: str=None):  # noqa: E501
        """ProviderInner - a model defined in Swagger

        :param provider_id: The provider_id of this ProviderInner.  # noqa: E501
        :type provider_id: int
        :param uuid: The uuid of this ProviderInner.  # noqa: E501
        :type uuid: str
        :param name: The name of this ProviderInner.  # noqa: E501
        :type name: str
        :param uri: The uri of this ProviderInner.  # noqa: E501
        :type uri: str
        """
        self.swagger_types = {
            'provider_id': int,
            'uuid': str,
            'name': str,
            'uri': str
        }

        self.attribute_map = {
            'provider_id': 'provider_id',
            'uuid': 'uuid',
            'name': 'name',
            'uri': 'uri'
        }
        self._provider_id = provider_id
        self._uuid = uuid
        self._name = name
        self._uri = uri

    @classmethod
    def from_dict(cls, dikt) -> 'ProviderInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The provider_inner of this ProviderInner.  # noqa: E501
        :rtype: ProviderInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provider_id(self) -> int:
        """Gets the provider_id of this ProviderInner.


        :return: The provider_id of this ProviderInner.
        :rtype: int
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id: int):
        """Sets the provider_id of this ProviderInner.


        :param provider_id: The provider_id of this ProviderInner.
        :type provider_id: int
        """

        self._provider_id = provider_id

    @property
    def uuid(self) -> str:
        """Gets the uuid of this ProviderInner.


        :return: The uuid of this ProviderInner.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this ProviderInner.


        :param uuid: The uuid of this ProviderInner.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def name(self) -> str:
        """Gets the name of this ProviderInner.


        :return: The name of this ProviderInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ProviderInner.


        :param name: The name of this ProviderInner.
        :type name: str
        """

        self._name = name

    @property
    def uri(self) -> str:
        """Gets the uri of this ProviderInner.


        :return: The uri of this ProviderInner.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri: str):
        """Sets the uri of this ProviderInner.


        :param uri: The uri of this ProviderInner.
        :type uri: str
        """

        self._uri = uri