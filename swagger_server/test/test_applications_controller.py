# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.application import Application  # noqa: E501
from swagger_server.models.application_provider import ApplicationProvider  # noqa: E501
from swagger_server.test import BaseTestCase


class TestApplicationsController(BaseTestCase):
    """ApplicationsController integration test stubs"""

    def test_applications_application_id_get(self):
        """Test case for applications_application_id_get

        Return application name, uri, uuid
        """
        response = self.client.open(
            '/v1.0/applications/{application_id}'.format(application_id='application_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_applications_application_id_providers_get(self):
        """Test case for applications_application_id_providers_get

        Return array of application providers
        """
        response = self.client.open(
            '/v1.0/applications/{application_id}/providers'.format(application_id='application_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_applications_application_id_providers_provider_id_get(self):
        """Test case for applications_application_id_providers_provider_id_get

        Return provider key for provider_id
        """
        response = self.client.open(
            '/v1.0/applications/{application_id}/providers/{provider_id}'.format(application_id='application_id_example', provider_id='provider_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
