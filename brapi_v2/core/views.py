# generated by fastapi-codegen:
#   filename:  PlantBreedingAPI-BrAPI-Core-2.0-resolved.yaml
#   timestamp: 2021-03-24T20:58:23+00:00

from __future__ import annotations

from datetime import date
from typing import List, Optional, Union

from fastapi import FastAPI, Query
from pydantic import constr

# use this to get access to the URL and path of the request
from starlette.requests import Request

# To keep each module independent we are going to use the router 
# as a replacement for the app
from fastapi import APIRouter, Query
router = APIRouter(
    tags = ["core"]
)
app = router

from .models import (
    CommonCropNamesResponse,
    Field202AcceptedSearchResponse,
    ListNewRequest,
    ListResponse,
    ListSearchRequest,
    ListsListResponse,
    ListsSingleResponse,
    ListTypes,
    LocationListResponse,
    LocationNewRequest,
    LocationSearchRequest,
    LocationSingleResponse,
    PersonListResponse,
    PersonNewRequest,
    PersonSearchRequest,
    PersonSingleResponse,
    ProgramListResponse,
    ProgramNewRequest,
    ProgramSearchRequest,
    ProgramSingleResponse,
    Season,
    SeasonListResponse,
    SeasonSingleResponse,
    ServerInfoResponse,
    StudyListResponse,
    StudyNewRequest,
    StudySearchRequest,
    StudySingleResponse,
    StudyTypesResponse,
    TrialListResponse,
    TrialNewRequest,
    TrialSearchRequest,
    TrialSingleResponse,
    WSMIMEDataTypes,
)

@app.get('/commoncropnames', response_model=CommonCropNamesResponse)
def get_commoncropnames(
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> CommonCropNamesResponse:
    """
    Get the Common Crop Names
    """
    pass


@app.get('/lists', response_model=ListsListResponse)
def get_lists(
    list_type: Optional[ListTypes] = Query(None, alias='listType'),
    list_name: Optional[str] = Query(None, alias='listName'),
    list_db_id: Optional[str] = Query(None, alias='listDbId'),
    list_source: Optional[str] = Query(None, alias='listSource'),
    external_reference_i_d: Optional[str] = Query(None, alias='externalReferenceID'),
    external_reference_source: Optional[str] = Query(
        None, alias='externalReferenceSource'
    ),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ListsListResponse:
    """
    Get filtered set of generic lists
    """
    pass


@app.post('/lists', response_model=ListsListResponse)
def post_lists(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[ListNewRequest] = None,
) -> ListsListResponse:
    """
    Create New List Objects
    """
    pass


@app.get('/lists/{list_db_id}', response_model=ListsSingleResponse)
def get_lists_list_db_id(
    list_db_id: str = Query(..., alias='listDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ListsSingleResponse:
    """
    Get the details of a specific List
    """
    pass


@app.put('/lists/{list_db_id}', response_model=ListsSingleResponse)
def put_lists_list_db_id(
    list_db_id: str = Query(..., alias='listDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ListNewRequest = None,
) -> ListsSingleResponse:
    """
    Update an existing generic list
    """
    pass


@app.post('/lists/{list_db_id}/items', response_model=ListResponse)
def post_lists_list_db_id_items(
    list_db_id: str = Query(..., alias='listDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[str] = None,
) -> ListResponse:
    """
    Add Items to a specific List
    """
    pass


@app.get('/locations', response_model=LocationListResponse)
def get_locations(
    location_type: Optional[str] = Query(None, alias='locationType'),
    location_db_id: Optional[str] = Query(None, alias='locationDbId'),
    external_reference_i_d: Optional[str] = Query(None, alias='externalReferenceID'),
    external_reference_source: Optional[str] = Query(
        None, alias='externalReferenceSource'
    ),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> LocationListResponse:
    """
    Get a filtered list of Locations
    """
    pass


@app.post('/locations', response_model=LocationListResponse)
def post_locations(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[LocationNewRequest] = None,
) -> LocationListResponse:
    """
    Create new Locations
    """
    pass


@app.get('/locations/{location_db_id}', response_model=LocationSingleResponse)
def get_locations_location_db_id(
    location_db_id: str = Query(..., alias='locationDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> LocationSingleResponse:
    """
    Get the details of a specific Location
    """
    pass


@app.put('/locations/{location_db_id}', response_model=LocationSingleResponse)
def put_locations_location_db_id(
    location_db_id: str = Query(..., alias='locationDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: LocationNewRequest = None,
) -> LocationSingleResponse:
    """
    Update the details for an existing Location
    """
    pass


@app.get('/people', response_model=PersonListResponse)
def get_people(
    first_name: Optional[str] = Query(None, alias='firstName'),
    last_name: Optional[str] = Query(None, alias='lastName'),
    person_db_id: Optional[str] = Query(None, alias='personDbId'),
    user_i_d: Optional[str] = Query(None, alias='userID'),
    external_reference_i_d: Optional[str] = Query(None, alias='externalReferenceID'),
    external_reference_source: Optional[str] = Query(
        None, alias='externalReferenceSource'
    ),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> PersonListResponse:
    """
    Get filtered list of People
    """
    pass


@app.post('/people', response_model=PersonListResponse)
def post_people(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[PersonNewRequest] = None,
) -> PersonListResponse:
    """
    Create new People
    """
    pass


@app.get('/people/{person_db_id}', response_model=PersonSingleResponse)
def get_people_person_db_id(
    person_db_id: str = Query(..., alias='personDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> PersonSingleResponse:
    """
    Get the details for a specific Person
    """
    pass


@app.put('/people/{person_db_id}', response_model=PersonSingleResponse)
def put_people_person_db_id(
    person_db_id: str = Query(..., alias='personDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: PersonNewRequest = None,
) -> PersonSingleResponse:
    """
    Update an existing Person
    """
    pass


@app.get('/programs', response_model=ProgramListResponse)
def get_programs(
    common_crop_name: Optional[str] = Query(None, alias='commonCropName'),
    program_db_id: Optional[str] = Query(None, alias='programDbId'),
    program_name: Optional[str] = Query(None, alias='programName'),
    abbreviation: Optional[str] = None,
    external_reference_i_d: Optional[str] = Query(None, alias='externalReferenceID'),
    external_reference_source: Optional[str] = Query(
        None, alias='externalReferenceSource'
    ),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ProgramListResponse:
    """
    Get a filtered list of breeding Programs
    """
    pass


@app.post('/programs', response_model=ProgramListResponse)
def post_programs(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[ProgramNewRequest] = None,
) -> ProgramListResponse:
    """
    Add new breeding Programs to the database
    """
    pass


@app.get('/programs/{program_db_id}', response_model=ProgramSingleResponse)
def get_programs_program_db_id(
    program_db_id: str = Query(..., alias='programDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ProgramSingleResponse:
    """
    Get a breeding Program by Id
    """
    pass


@app.put('/programs/{program_db_id}', response_model=ProgramSingleResponse)
def put_programs_program_db_id(
    program_db_id: str = Query(..., alias='programDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ProgramNewRequest = None,
) -> ProgramSingleResponse:
    """
    Update an existing Program
    """
    pass


@app.post(
    '/search/lists',
    response_model=Union[ListsListResponse, Field202AcceptedSearchResponse],
)
def post_search_lists(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ListSearchRequest = None,
) -> Union[ListsListResponse, Field202AcceptedSearchResponse]:
    """
    Submit a search request for Lists
    """
    pass


@app.get(
    '/search/lists/{search_results_db_id}',
    response_model=Union[ListsListResponse, Field202AcceptedSearchResponse],
)
def get_search_lists_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[ListsListResponse, Field202AcceptedSearchResponse]:
    """
    Get the results of a List search request
    """
    pass


@app.post(
    '/search/locations',
    response_model=Union[LocationListResponse, Field202AcceptedSearchResponse],
)
def post_search_locations(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: LocationSearchRequest = None,
) -> Union[LocationListResponse, Field202AcceptedSearchResponse]:
    """
    Submit a search request for Locations
    """
    pass


@app.get(
    '/search/locations/{search_results_db_id}',
    response_model=Union[LocationListResponse, Field202AcceptedSearchResponse],
)
def get_search_locations_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[LocationListResponse, Field202AcceptedSearchResponse]:
    """
    Get the results of a Locations search request
    """
    pass


@app.post(
    '/search/people',
    response_model=Union[PersonListResponse, Field202AcceptedSearchResponse],
)
def post_search_people(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: PersonSearchRequest = None,
) -> Union[PersonListResponse, Field202AcceptedSearchResponse]:
    """
    Submit a search request for People
    """
    pass


@app.get(
    '/search/people/{search_results_db_id}',
    response_model=Union[PersonListResponse, Field202AcceptedSearchResponse],
)
def get_search_people_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[PersonListResponse, Field202AcceptedSearchResponse]:
    """
    Get the results of a People search request
    """
    pass


@app.post(
    '/search/programs',
    response_model=Union[ProgramListResponse, Field202AcceptedSearchResponse],
)
def post_search_programs(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ProgramSearchRequest = None,
) -> Union[ProgramListResponse, Field202AcceptedSearchResponse]:
    """
    Submit a search request for Programs
    """
    pass


@app.get(
    '/search/programs/{search_results_db_id}',
    response_model=Union[ProgramListResponse, Field202AcceptedSearchResponse],
)
def get_search_programs_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[ProgramListResponse, Field202AcceptedSearchResponse]:
    """
    Get the results of a Programs search request
    """
    pass


@app.post(
    '/search/studies',
    response_model=Union[StudyListResponse, Field202AcceptedSearchResponse],
)
def post_search_studies(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: StudySearchRequest = None,
) -> Union[StudyListResponse, Field202AcceptedSearchResponse]:
    """
    Submit a search request for Studies
    """
    pass


@app.get(
    '/search/studies/{search_results_db_id}',
    response_model=Union[StudyListResponse, Field202AcceptedSearchResponse],
)
def get_search_studies_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[StudyListResponse, Field202AcceptedSearchResponse]:
    """
    Get the results of a Studies search request
    """
    pass


@app.post(
    '/search/trials',
    response_model=Union[TrialListResponse, Field202AcceptedSearchResponse],
)
def post_search_trials(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: TrialSearchRequest = None,
) -> Union[TrialListResponse, Field202AcceptedSearchResponse]:
    """
    Submit a search request for Trials
    """
    pass


@app.get(
    '/search/trials/{search_results_db_id}',
    response_model=Union[TrialListResponse, Field202AcceptedSearchResponse],
)
def get_search_trials_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[TrialListResponse, Field202AcceptedSearchResponse]:
    """
    Get the results of a Trials search request
    """
    pass


@app.get('/seasons', response_model=SeasonListResponse)
def get_seasons(
    season_db_id: Optional[str] = Query(None, alias='seasonDbId'),
    season: Optional[str] = None,
    year: Optional[int] = None,
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> SeasonListResponse:
    """
    Get the Seasons
    """
    pass


@app.post('/seasons', response_model=SeasonListResponse)
def post_seasons(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[Season] = None,
) -> SeasonListResponse:
    """
    POST new Seasons
    """
    pass


@app.get('/seasons/{season_db_id}', response_model=SeasonSingleResponse)
def get_seasons_season_db_id(
    season_db_id: str = Query(..., alias='seasonDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> SeasonSingleResponse:
    """
    Get the a single Season
    """
    pass


@app.put('/seasons/{season_db_id}', response_model=SeasonSingleResponse)
def put_seasons_season_db_id(
    season_db_id: str = Query(..., alias='seasonDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: Season = None,
) -> SeasonSingleResponse:
    """
    Update existing Seasons
    """
    pass

# basic serverInfo endpoint implementation
@app.get('/serverinfo', response_model=ServerInfoResponse, response_model_exclude_none=False)
def get_serverinfo(
    request: Request,
    data_type: Optional[WSMIMEDataTypes] = Query(None, alias='dataType'),
    authorization: Optional[constr(regex='^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ServerInfoResponse:
    """
    Get the list of implemented Calls
    """
    import os
    from .models import Metadata, ServerInfo, Version, HttpMethod, Service
    metadata = Metadata(datafiles=[], status=[], pagination=None)

    # retrieve the request url as it its "seen" by the client
    services_url = request.url
    base_url = os.path.split(str(services_url))[0]

    services = []
    services.append(
        # Lists Server information (Core Module)
        Service(service=f"{base_url}/serverinfo",
                methods=[HttpMethod.GET], 
                dataTypes=[ WSMIMEDataTypes.application_json],
                versions=[Version.v2_0])
    )
    services.append(
        # Lists Events (Phenotyping Module)
        Service(service=f"{base_url}/events",
                dataTypes=[ WSMIMEDataTypes.application_json],
                methods=[HttpMethod.GET],
                versions=[Version.v2_0])
    )

    services.append(
        # Lists attributes (Germplasm Module)
        Service(service=f"{base_url}/attributes",
                dataTypes=[ WSMIMEDataTypes.application_json],
                methods=[HttpMethod.GET],
                versions=[Version.v2_0])
    )

    services.append(
        # Lists samples (Genotyping Module)
        Service(service=f"{base_url}/samples",
                dataTypes=[ WSMIMEDataTypes.application_json],
                methods=[HttpMethod.GET],
                versions=[Version.v2_0])
    )

    serverinfo = ServerInfo(serverName='BrAPIv2 Test Server.',
                    organizationName='Placeholder Organization',
                    contactEmail='user@email.host.com',
                    serverDescription='BrAPI FastAPI Server Testbed.',
                    calls=services)

    import time
    serverinfo.serverName += ' Current server time: ' + str(time.asctime())

    response = ServerInfoResponse(metadata=metadata, result=serverinfo)
    
    return response


@app.get('/studies', response_model=StudyListResponse)
def get_studies(
    common_crop_name: Optional[str] = Query(None, alias='commonCropName'),
    study_type: Optional[str] = Query(None, alias='studyType'),
    program_db_id: Optional[str] = Query(None, alias='programDbId'),
    location_db_id: Optional[str] = Query(None, alias='locationDbId'),
    season_db_id: Optional[str] = Query(None, alias='seasonDbId'),
    trial_db_id: Optional[str] = Query(None, alias='trialDbId'),
    study_db_id: Optional[str] = Query(None, alias='studyDbId'),
    study_name: Optional[str] = Query(None, alias='studyName'),
    study_code: Optional[str] = Query(None, alias='studyCode'),
    study_p_u_i: Optional[str] = Query(None, alias='studyPUI'),
    germplasm_db_id: Optional[str] = Query(None, alias='germplasmDbId'),
    observation_variable_db_id: Optional[str] = Query(
        None, alias='observationVariableDbId'
    ),
    active: Optional[bool] = None,
    sort_by: Optional[str] = Query(None, alias='sortBy'),
    sort_order: Optional[str] = Query(None, alias='sortOrder'),
    external_reference_i_d: Optional[str] = Query(None, alias='externalReferenceID'),
    external_reference_source: Optional[str] = Query(
        None, alias='externalReferenceSource'
    ),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> StudyListResponse:
    """
    Get a filtered list of Studies
    """
    pass


@app.post('/studies', response_model=StudyListResponse)
def post_studies(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[StudyNewRequest] = None,
) -> StudyListResponse:
    """
    Create new Studies.
    """
    pass


@app.get('/studies/{study_db_id}', response_model=StudySingleResponse)
def get_studies_study_db_id(
    study_db_id: str = Query(..., alias='studyDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> StudySingleResponse:
    """
    Get the details for a specific Study
    """
    pass


@app.put('/studies/{study_db_id}', response_model=StudySingleResponse)
def put_studies_study_db_id(
    study_db_id: str = Query(..., alias='studyDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: StudyNewRequest = None,
) -> StudySingleResponse:
    """
    Update an existing Study
    """
    pass


@app.get('/studytypes', response_model=StudyTypesResponse)
def get_studytypes(
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> StudyTypesResponse:
    """
    Get the Study Types
    """
    pass


@app.get('/trials', response_model=TrialListResponse)
def get_trials(
    active: Optional[bool] = None,
    common_crop_name: Optional[str] = Query(None, alias='commonCropName'),
    contact_db_id: Optional[str] = Query(None, alias='contactDbId'),
    program_db_id: Optional[str] = Query(None, alias='programDbId'),
    location_db_id: Optional[str] = Query(None, alias='locationDbId'),
    search_date_range_start: Optional[date] = Query(None, alias='searchDateRangeStart'),
    search_date_range_end: Optional[date] = Query(None, alias='searchDateRangeEnd'),
    study_db_id: Optional[str] = Query(None, alias='studyDbId'),
    trial_db_id: Optional[str] = Query(None, alias='trialDbId'),
    trial_name: Optional[str] = Query(None, alias='trialName'),
    trial_p_u_i: Optional[str] = Query(None, alias='trialPUI'),
    sort_by: Optional[str] = Query(None, alias='sortBy'),
    sort_order: Optional[str] = Query(None, alias='sortOrder'),
    external_reference_i_d: Optional[str] = Query(None, alias='externalReferenceID'),
    external_reference_source: Optional[str] = Query(
        None, alias='externalReferenceSource'
    ),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> TrialListResponse:
    """
    Get a filtered list of Trials
    """
    pass


@app.post('/trials', response_model=TrialListResponse)
def post_trials(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[TrialNewRequest] = None,
) -> TrialListResponse:
    """
    Create new trials
    """
    pass


@app.get('/trials/{trial_db_id}', response_model=TrialSingleResponse)
def get_trials_trial_db_id(
    trial_db_id: str = Query(..., alias='trialDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> TrialSingleResponse:
    """
    Get the details of a specific Trial
    """
    pass


@app.put('/trials/{trial_db_id}', response_model=TrialSingleResponse)
def put_trials_trial_db_id(
    trial_db_id: str = Query(..., alias='trialDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: TrialNewRequest = None,
) -> TrialSingleResponse:
    """
    Update the details of an existing Trial
    """
    pass
