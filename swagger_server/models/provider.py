# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.provider_inner import ProviderInner  # noqa: F401,E501
from swagger_server import util


class Provider(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self):  # noqa: E501
        """Provider - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'Provider':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The provider of this Provider.  # noqa: E501
        :rtype: Provider
        """
        return util.deserialize_model(dikt, cls)