import connexion
import six

from swagger_server.models.application import Application  # noqa: E501
from swagger_server.models.application_inner import ApplicationInner  # noqa: E501
from swagger_server.models.consumer import Consumer  # noqa: E501
from swagger_server.models.consumer_application_inner import ConsumerApplicationInner  # noqa: E501
from swagger_server.models.consumer_provider_inner import ConsumerProviderInner  # noqa: E501
from swagger_server.models.provider import Provider  # noqa: E501
from swagger_server.models.provider_inner import ProviderInner  # noqa: E501
from swagger_server import util


def applications_get():  # noqa: E501
    """Return array of applications

    Obtain list of application providers  # noqa: E501


    :rtype: List[Application]
    """
    return 'do some magic!'


def applications_post(body):  # noqa: E501
    """Add application

    Returns true if consumer application is added  # noqa: E501

    :param body: Request to add an application
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [ApplicationInner.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


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


def consumers_consumer_id_providers_post(body, consumer_id):  # noqa: E501
    """Add consumer provider

    Returns true if consumer provider is added  # noqa: E501

    :param body: Request to add consumer provider
    :type body: list | bytes
    :param consumer_id: consumer_id
    :type consumer_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = [ConsumerProviderInner.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
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


def consumers_get():  # noqa: E501
    """Request user data

    Returns a dict userids  # noqa: E501


    :rtype: List[Consumer]
    """
    return 'do some magic!'


def providers_get():  # noqa: E501
    """Provider ID list

    Returns a list of providers # noqa: E501


    :rtype: List[Provider]
    """
    return 'do some magic!'


def providers_post(body):  # noqa: E501
    """Add provider

    Returns new provider ID (and?) if provider is added  # noqa: E501

    :param body: Request to add consumer application
    :type body: list | bytes

    :rtype: List[Provider]
    """
    if connexion.request.is_json:
        body = [ProviderInner.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def providers_provider_id_get(provider_id):  # noqa: E501
    """Service API KEY

    Returns the provider service api key for {provider_id}   # noqa: E501

    :param provider_id: Internal ID for available services
    :type provider_id: str

    :rtype: List[Provider]
    """
    return 'do some magic!'
