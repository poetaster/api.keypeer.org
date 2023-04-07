import connexion
import six

from swagger_server.models.provider import Provider  # noqa: E501
from swagger_server import util


def v10_providers_get():  # noqa: E501
    """Provider ID list

    Returns a list of providers # noqa: E501


    :rtype: List[Provider]
    """
    return 'do some magic!'


def v10_providers_provider_id_get(provider_id):  # noqa: E501
    """Service API KEY

    Returns the provider service api key for {provider_id}   # noqa: E501

    :param provider_id: Internal ID for available services
    :type provider_id: str

    :rtype: List[Provider]
    """
    return 'do some magic!'
