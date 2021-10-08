# from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .brapi_v2 import core, germplasm, genotyping, phenotyping
from functools import wraps

# Create your views here.
def create_error_response(message):
    from .brapi_v2.core.models import Metadata, IndexPagination, MessageType, Status
    from .brapi_v2.proposals.models import ErrorResponseResult, ErrorResponse

    status = Status(message=message, messageType=MessageType.ERROR)
    pagination = IndexPagination(currentPage = 0, pageSize=1000, totalCount=1, totalPages=1)
    metadata = Metadata(datafiles=[], status=[status], pagination=pagination)
    
    error_info = ErrorResponseResult(data=[])
    response = ErrorResponse(metadata=metadata, result=error_info)

    return response

def brapi_decorator(call):
    @wraps(call)
    def brapi_call(*args, **kwargs):
        try:
            response = call(*args, **kwargs)

        except Exception as e:
            default_msg = 'Error during service execution'
            message = default_msg + ': ' + str(e)
            response = create_error_response(message=message)

        # pydantic objects can be converted to JSON directly
        django_response = HttpResponse(response.json(), content_type='application/json')
        return django_response
    return brapi_call

@require_http_methods(["GET"])
@brapi_decorator
def serverinfo(request):
    from .brapi_v2.core.models import (
        Metadata, ServerInfo, Version, HttpMethod, Service, 
        IndexPagination, WSMIMEDataTypes, ServerInfoResponse)

    pagination = IndexPagination(currentPage = 0, pageSize=1000, totalCount=1, totalPages=1)
    metadata = Metadata(datafiles=[], status=[], pagination=pagination)
    services = []
    services.append(
        # Lists Server information (Core Module)
        Service(service="serverinfo",
                methods=[HttpMethod.GET], 
                dataTypes=[ WSMIMEDataTypes.application_json],
                versions=[Version.v2_0])
    )

    serverinfo = ServerInfo(serverName='BrAPIv2 Test Server.',
                    organizationName='Placeholder Organization',
                    contactEmail='user@email.host.com',
                    serverDescription='BrAPI Django Server Testbed.',
                    calls=services)

    pagination = IndexPagination(currentPage = 0, pageSize=1000)
    metadata = Metadata(datafiles=[], status=[], pagination=pagination)

    response = ServerInfoResponse(metadata=metadata, result=serverinfo)
    return response


