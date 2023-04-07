import connexion
import six

from swagger_server.models.application import Application  # noqa: E501
from swagger_server.models.application_provider import ApplicationProvider  # noqa: E501
from swagger_server import util


def applications_application_id_get(application_id):  # noqa: E501
    """Return application name, uri, uuid

    Obtain list of application providers  # noqa: E501

    :param application_id: Consumer Application ID
    :type application_id: str

    :rtype: List[Application]
    """
    return 'do some magic!'


def applications_application_id_providers_get(application_id):  # noqa: E501
    """Return array of application providers

    Obtain application provider keys  # noqa: E501

    :param application_id: Consumer Application ID
    :type application_id: str

    :rtype: List[Application]
    """
    return 'do some magic!'


def applications_application_id_providers_provider_id_get(application_id, provider_id):  # noqa: E501
    """Return provider key for provider_id

    Obtain application provider keys  # noqa: E501

    :param application_id: Consumer Application ID
    :type application_id: str
    :param provider_id: Internal ID for available services
    :type provider_id: str

    :rtype: List[ApplicationProvider]
    """
    return 'do some magic!'
