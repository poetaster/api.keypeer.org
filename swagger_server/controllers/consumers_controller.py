import connexion
import six

from swagger_server.models.consumer import Consumer  # noqa: E501
from swagger_server.models.consumer_application import ConsumerApplication  # noqa: E501
from swagger_server.models.consumer_application_inner import ConsumerApplicationInner  # noqa: E501
from swagger_server.models.consumer_provider import ConsumerProvider  # noqa: E501
from swagger_server import util


def consumers_consumer_id_applications_application_id_delete(consumer_id, application_id):  # noqa: E501
    """remove consumer application

    Returns true if consumer application is updated  # noqa: E501

    :param consumer_id: Consumer ID
    :type consumer_id: str
    :param application_id: Consumer Application ID
    :type application_id: str

    :rtype: None
    """
    return 'do some magic!'


def consumers_consumer_id_applications_application_id_get(consumer_id, application_id):  # noqa: E501
    """Retrieve Service Api keys for users application, application_id

    Returns service api key  # noqa: E501

    :param consumer_id: Consumer ID
    :type consumer_id: str
    :param application_id: Consumer Application ID
    :type application_id: str

    :rtype: List[ConsumerApplication]
    """
    return 'do some magic!'


def consumers_consumer_id_applications_post(body, consumer_id):  # noqa: E501
    """Add consumer application

    Returns true if consumer application is added  # noqa: E501

    :param body: Request to add consumer application
    :type body: list | bytes
    :param consumer_id: Consumer ID
    :type consumer_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = [ConsumerApplicationInner.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def consumers_consumer_id_get(consumer_id):  # noqa: E501
    """Request user data

    Returns a dict containing varoius user data  # noqa: E501

    :param consumer_id: End User ID
    :type consumer_id: str

    :rtype: List[Consumer]
    """
    return 'do some magic!'


def consumers_consumer_id_providers_provider_id_delete(consumer_id, provider_id):  # noqa: E501
    """remove consumer provider

    Returns true if consumer provider is updated  # noqa: E501

    :param consumer_id: Consumer ID
    :type consumer_id: str
    :param provider_id: Consumer Provider ID
    :type provider_id: str

    :rtype: None
    """
    return 'do some magic!'


def consumers_consumer_id_providers_provider_id_get(consumer_id, provider_id):  # noqa: E501
    """Retrieve Service Api keys for users provider, provider_id

    Returns service api key  # noqa: E501

    :param consumer_id: Consumer ID
    :type consumer_id: str
    :param provider_id: Consumer Provider ID
    :type provider_id: str

    :rtype: List[ConsumerProvider]
    """
    return 'do some magic!'
