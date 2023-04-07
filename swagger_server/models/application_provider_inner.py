# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ApplicationProviderInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, application_id: str=None, provider_id: str=None, service_api_key: str=None, expiry: str=None):  # noqa: E501
        """ApplicationProviderInner - a model defined in Swagger

        :param application_id: The application_id of this ApplicationProviderInner.  # noqa: E501
        :type application_id: str
        :param provider_id: The provider_id of this ApplicationProviderInner.  # noqa: E501
        :type provider_id: str
        :param service_api_key: The service_api_key of this ApplicationProviderInner.  # noqa: E501
        :type service_api_key: str
        :param expiry: The expiry of this ApplicationProviderInner.  # noqa: E501
        :type expiry: str
        """
        self.swagger_types = {
            'application_id': str,
            'provider_id': str,
            'service_api_key': str,
            'expiry': str
        }

        self.attribute_map = {
            'application_id': 'application_id',
            'provider_id': 'provider_id',
            'service_api_key': 'service_api_key',
            'expiry': 'expiry'
        }
        self._application_id = application_id
        self._provider_id = provider_id
        self._service_api_key = service_api_key
        self._expiry = expiry

    @classmethod
    def from_dict(cls, dikt) -> 'ApplicationProviderInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The application_provider_inner of this ApplicationProviderInner.  # noqa: E501
        :rtype: ApplicationProviderInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application_id(self) -> str:
        """Gets the application_id of this ApplicationProviderInner.


        :return: The application_id of this ApplicationProviderInner.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id: str):
        """Sets the application_id of this ApplicationProviderInner.


        :param application_id: The application_id of this ApplicationProviderInner.
        :type application_id: str
        """

        self._application_id = application_id

    @property
    def provider_id(self) -> str:
        """Gets the provider_id of this ApplicationProviderInner.


        :return: The provider_id of this ApplicationProviderInner.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id: str):
        """Sets the provider_id of this ApplicationProviderInner.


        :param provider_id: The provider_id of this ApplicationProviderInner.
        :type provider_id: str
        """

        self._provider_id = provider_id

    @property
    def service_api_key(self) -> str:
        """Gets the service_api_key of this ApplicationProviderInner.


        :return: The service_api_key of this ApplicationProviderInner.
        :rtype: str
        """
        return self._service_api_key

    @service_api_key.setter
    def service_api_key(self, service_api_key: str):
        """Sets the service_api_key of this ApplicationProviderInner.


        :param service_api_key: The service_api_key of this ApplicationProviderInner.
        :type service_api_key: str
        """

        self._service_api_key = service_api_key

    @property
    def expiry(self) -> str:
        """Gets the expiry of this ApplicationProviderInner.

        ISO 8601 Format  # noqa: E501

        :return: The expiry of this ApplicationProviderInner.
        :rtype: str
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry: str):
        """Sets the expiry of this ApplicationProviderInner.

        ISO 8601 Format  # noqa: E501

        :param expiry: The expiry of this ApplicationProviderInner.
        :type expiry: str
        """

        self._expiry = expiry
