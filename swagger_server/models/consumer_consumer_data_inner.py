# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ConsumerConsumerDataInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, consumer_id: str=None, application_id: str=None, provider_id: str=None, expiry: str=None):  # noqa: E501
        """ConsumerConsumerDataInner - a model defined in Swagger

        :param consumer_id: The consumer_id of this ConsumerConsumerDataInner.  # noqa: E501
        :type consumer_id: str
        :param application_id: The application_id of this ConsumerConsumerDataInner.  # noqa: E501
        :type application_id: str
        :param provider_id: The provider_id of this ConsumerConsumerDataInner.  # noqa: E501
        :type provider_id: str
        :param expiry: The expiry of this ConsumerConsumerDataInner.  # noqa: E501
        :type expiry: str
        """
        self.swagger_types = {
            'consumer_id': str,
            'application_id': str,
            'provider_id': str,
            'expiry': str
        }

        self.attribute_map = {
            'consumer_id': 'consumer_id',
            'application_id': 'application_id',
            'provider_id': 'provider_id',
            'expiry': 'expiry'
        }
        self._consumer_id = consumer_id
        self._application_id = application_id
        self._provider_id = provider_id
        self._expiry = expiry

    @classmethod
    def from_dict(cls, dikt) -> 'ConsumerConsumerDataInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The consumer_consumerData_inner of this ConsumerConsumerDataInner.  # noqa: E501
        :rtype: ConsumerConsumerDataInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def consumer_id(self) -> str:
        """Gets the consumer_id of this ConsumerConsumerDataInner.


        :return: The consumer_id of this ConsumerConsumerDataInner.
        :rtype: str
        """
        return self._consumer_id

    @consumer_id.setter
    def consumer_id(self, consumer_id: str):
        """Sets the consumer_id of this ConsumerConsumerDataInner.


        :param consumer_id: The consumer_id of this ConsumerConsumerDataInner.
        :type consumer_id: str
        """

        self._consumer_id = consumer_id

    @property
    def application_id(self) -> str:
        """Gets the application_id of this ConsumerConsumerDataInner.


        :return: The application_id of this ConsumerConsumerDataInner.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id: str):
        """Sets the application_id of this ConsumerConsumerDataInner.


        :param application_id: The application_id of this ConsumerConsumerDataInner.
        :type application_id: str
        """

        self._application_id = application_id

    @property
    def provider_id(self) -> str:
        """Gets the provider_id of this ConsumerConsumerDataInner.


        :return: The provider_id of this ConsumerConsumerDataInner.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id: str):
        """Sets the provider_id of this ConsumerConsumerDataInner.


        :param provider_id: The provider_id of this ConsumerConsumerDataInner.
        :type provider_id: str
        """

        self._provider_id = provider_id

    @property
    def expiry(self) -> str:
        """Gets the expiry of this ConsumerConsumerDataInner.

        ISO 8601 Format  # noqa: E501

        :return: The expiry of this ConsumerConsumerDataInner.
        :rtype: str
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry: str):
        """Sets the expiry of this ConsumerConsumerDataInner.

        ISO 8601 Format  # noqa: E501

        :param expiry: The expiry of this ConsumerConsumerDataInner.
        :type expiry: str
        """

        self._expiry = expiry
