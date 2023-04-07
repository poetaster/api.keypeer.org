# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.application import Application  # noqa: E501
from swagger_server.models.application_inner import ApplicationInner  # noqa: E501
from swagger_server.models.consumer import Consumer  # noqa: E501
from swagger_server.models.consumer_application_inner import ConsumerApplicationInner  # noqa: E501
from swagger_server.models.consumer_provider_inner import ConsumerProviderInner  # noqa: E501
from swagger_server.models.provider import Provider  # noqa: E501
from swagger_server.models.provider_inner import ProviderInner  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAdminsController(BaseTestCase):
    """AdminsController integration test stubs"""

    def test_applications_get(self):
        """Test case for applications_get

        Return array of applications
        """
        response = self.client.open(
            '/v1.0/applications',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_applications_post(self):
        """Test case for applications_post

        Add application
        """
        body = [ApplicationInner()]
        response = self.client.open(
            '/v1.0/applications',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_consumers_consumer_id_applications_application_id_delete(self):
        """Test case for consumers_consumer_id_applications_application_id_delete

        remove consumer application
        """
        response = self.client.open(
            '/v1.0/consumers/{consumer_id}/applications/{application_id}'.format(consumer_id='consumer_id_example', application_id='application_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_consumers_consumer_id_applications_post(self):
        """Test case for consumers_consumer_id_applications_post

        Add consumer application
        """
        body = [ConsumerApplicationInner()]
        response = self.client.open(
            '/v1.0/consumers/{consumer_id}/applications'.format(consumer_id='consumer_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_consumers_consumer_id_providers_post(self):
        """Test case for consumers_consumer_id_providers_post

        Add consumer provider
        """
        body = [ConsumerProviderInner()]
        response = self.client.open(
            '/v1.0/consumers/{consumer_id}/providers'.format(consumer_id='consumer_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='provider/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_consumers_consumer_id_providers_provider_id_delete(self):
        """Test case for consumers_consumer_id_providers_provider_id_delete

        remove consumer provider
        """
        response = self.client.open(
            '/v1.0/consumers/{consumer_id}/providers/{provider_id}'.format(consumer_id='consumer_id_example', provider_id='provider_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_consumers_get(self):
        """Test case for consumers_get

        Request user data
        """
        response = self.client.open(
            '/v1.0/consumers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_providers_get(self):
        """Test case for providers_get

        Provider ID list
        """
        response = self.client.open(
            '/v1.0/providers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_providers_post(self):
        """Test case for providers_post

        Add provider
        """
        body = [ProviderInner()]
        response = self.client.open(
            '/v1.0/providers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_providers_provider_id_get(self):
        """Test case for providers_provider_id_get

        Service API KEY
        """
        response = self.client.open(
            '/v1.0/providers/{provider_id}'.format(provider_id='provider_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
