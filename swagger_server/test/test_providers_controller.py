# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.provider import Provider  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProvidersController(BaseTestCase):
    """ProvidersController integration test stubs"""

    def test_v10_providers_get(self):
        """Test case for v10_providers_get

        Provider ID list
        """
        response = self.client.open(
            '/v10/v10/providers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v10_providers_provider_id_get(self):
        """Test case for v10_providers_provider_id_get

        Service API KEY
        """
        response = self.client.open(
            '/v10/v10/providers/{provider_id}'.format(provider_id='provider_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
