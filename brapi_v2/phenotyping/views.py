# generated by fastapi-codegen:
#   filename:  PlantBreedingAPI-BrAPI-Phenotyping-2.0-resolved.yaml
#   timestamp: 2021-03-24T21:08:46+00:00

from __future__ import annotations

from datetime import datetime
from typing import List, Optional, Union

from fastapi import FastAPI, Query
from pydantic import constr

# To keep each module independent we are going to use the router 
# as a replacement for the app
from fastapi import APIRouter
router = APIRouter(
    tags = ["phenotyping"]
)
app = router
# from brapi_v2.core.models import (
from .. core.models import (
    Field202AcceptedSearchResponse,
    # Field202AcceptedSearchResponseResult,
    WSMIMEDataTypes,
)
from . models import (
    AdditionalInfo,
    EventsResponse,
    # Field202AcceptedSearchResponse,
    ImageListResponse,
    ImageNewRequest,
    ImageSearchRequest,
    ImageSingleResponse,
    Metadata,
    MethodListResponse,
    MethodNewRequest,
    MethodSingleResponse,
    ObservationLevelListResponse,
    ObservationListResponse,
    ObservationNewRequest,
    ObservationSearchRequest,
    ObservationSingleResponse,
    ObservationsPutRequest,
    ObservationTableResponse,
    ObservationUnitListResponse,
    ObservationUnitNewRequest,
    ObservationUnitSearchRequest,
    ObservationUnitSingleResponse,
    ObservationunitsPutRequest,
    ObservationUnitTableResponse,
    ObservationVariableListResponse,
    ObservationVariableNewRequest,
    ObservationVariableSearchRequest,
    ObservationVariableSingleResponse,
    OntologyListResponse,
    ScaleListResponse,
    ScaleNewRequest,
    ScaleSingleResponse,
    TraitListResponse,
    TraitNewRequest,
    TraitSingleResponse,
    # WSMIMEDataTypes,
)


@app.get('/events', response_model=EventsResponse)
def get_events(
    study_db_id: Optional[str] = Query(None, alias='studyDbId'),
    observation_unit_db_id: Optional[str] = Query(None, alias='observationUnitDbId'),
    event_db_id: Optional[str] = Query(None, alias='eventDbId'),
    event_type: Optional[str] = Query(None, alias='eventType'),
    date_range_start: Optional[datetime] = Query(None, alias='dateRangeStart'),
    date_range_end: Optional[datetime] = Query(None, alias='dateRangeEnd'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> EventsResponse:
    """
    Get the Events
    """
    
    # here we construct a dummy event just to show the functionaliy
    from .models import Event, EventsResponseResult, AdditionalInfo
    additional_info_test = {}
    additional_info_test["info_tag_1"] = AdditionalInfo(location="Earth!",importance="Very Important!")

    events = [Event(eventDbId="123456789", eventType="Example event", additionalInfo=additional_info_test)]
    meta = Metadata()
    result = EventsResponseResult(data=events)
    return EventsResponse(metadata=meta, result = result)


@app.get('/images', response_model=ImageListResponse)
def get_images(
    image_db_id: Optional[str] = Query(None, alias='imageDbId'),
    image_name: Optional[str] = Query(None, alias='imageName'),
    observation_unit_db_id: Optional[str] = Query(None, alias='observationUnitDbId'),
    observation_db_id: Optional[str] = Query(None, alias='observationDbId'),
    descriptive_ontology_term: Optional[str] = Query(
        None, alias='descriptiveOntologyTerm'
    ),
    external_reference_i_d: Optional[str] = Query(None, alias='externalReferenceID'),
    external_reference_source: Optional[str] = Query(
        None, alias='externalReferenceSource'
    ),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ImageListResponse:
    """
    Get the image meta data summaries
    """
    pass


@app.post('/images', response_model=ImageListResponse)
def post_images(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[ImageNewRequest] = None,
) -> ImageListResponse:
    """
    Create new image meta data objects
    """
    pass


@app.get('/images/{image_db_id}', response_model=ImageSingleResponse)
def get_images_image_db_id(
    image_db_id: str = Query(..., alias='imageDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ImageSingleResponse:
    """
    Get the an image meta data summary
    """
    pass


@app.put('/images/{image_db_id}', response_model=ImageSingleResponse)
def put_images_image_db_id(
    image_db_id: str = Query(..., alias='imageDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ImageNewRequest = None,
) -> ImageSingleResponse:
    """
    Update an image meta data
    """
    pass


@app.put('/images/{image_db_id}/imagecontent', response_model=ImageSingleResponse)
def put_images_image_db_id_imagecontent(
    image_db_id: str = Query(..., alias='imageDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ImageSingleResponse:
    """
    Update an image with the image file content
    """
    pass


@app.get('/methods', response_model=MethodListResponse)
def get_methods(
    method_db_id: Optional[str] = Query(None, alias='methodDbId'),
    observation_variable_db_id: Optional[str] = Query(
        None, alias='observationVariableDbId'
    ),
    external_reference_i_d: Optional[str] = Query(None, alias='externalReferenceID'),
    external_reference_source: Optional[str] = Query(
        None, alias='externalReferenceSource'
    ),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> MethodListResponse:
    """
    Get the Methods
    """
    pass


@app.post('/methods', response_model=MethodListResponse)
def post_methods(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[MethodNewRequest] = None,
) -> MethodListResponse:
    """
    Add new Methods
    """
    pass


@app.get('/methods/{method_db_id}', response_model=MethodSingleResponse)
def get_methods_method_db_id(
    method_db_id: str = Query(..., alias='methodDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> MethodSingleResponse:
    """
    Get the details for a specific Method
    """
    pass


@app.put('/methods/{method_db_id}', response_model=MethodSingleResponse)
def put_methods_method_db_id(
    method_db_id: str = Query(..., alias='methodDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: MethodNewRequest = None,
) -> MethodSingleResponse:
    """
    Update an existing Method
    """
    pass


@app.get('/observationlevels', response_model=ObservationLevelListResponse)
def get_observationlevels(
    study_db_id: Optional[str] = Query(None, alias='studyDbId'),
    trial_db_id: Optional[str] = Query(None, alias='trialDbId'),
    program_db_id: Optional[str] = Query(None, alias='programDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ObservationLevelListResponse:
    """
    Get the Observation Levels
    """
    pass


@app.get('/observations', response_model=ObservationListResponse)
def get_observations(
    observation_db_id: Optional[str] = Query(None, alias='observationDbId'),
    observation_unit_db_id: Optional[str] = Query(None, alias='observationUnitDbId'),
    germplasm_db_id: Optional[str] = Query(None, alias='germplasmDbId'),
    observation_variable_db_id: Optional[str] = Query(
        None, alias='observationVariableDbId'
    ),
    study_db_id: Optional[str] = Query(None, alias='studyDbId'),
    location_db_id: Optional[str] = Query(None, alias='locationDbId'),
    trial_db_id: Optional[str] = Query(None, alias='trialDbId'),
    program_db_id: Optional[str] = Query(None, alias='programDbId'),
    season_db_id: Optional[str] = Query(None, alias='seasonDbId'),
    observation_unit_level_name: Optional[str] = Query(
        None, alias='observationUnitLevelName'
    ),
    observation_unit_level_order: Optional[str] = Query(
        None, alias='observationUnitLevelOrder'
    ),
    observation_unit_level_code: Optional[str] = Query(
        None, alias='observationUnitLevelCode'
    ),
    observation_time_stamp_range_start: Optional[datetime] = Query(
        None, alias='observationTimeStampRangeStart'
    ),
    observation_time_stamp_range_end: Optional[datetime] = Query(
        None, alias='observationTimeStampRangeEnd'
    ),
    external_reference_i_d: Optional[str] = Query(None, alias='externalReferenceID'),
    external_reference_source: Optional[str] = Query(
        None, alias='externalReferenceSource'
    ),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ObservationListResponse:
    """
    Get a filtered set of Observations
    """
    pass


@app.put('/observations', response_model=ObservationListResponse)
def put_observations(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ObservationsPutRequest = None,
) -> ObservationListResponse:
    """
    Update multiple Observation entities
    """
    pass


@app.post('/observations', response_model=ObservationListResponse)
def post_observations(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[ObservationNewRequest] = None,
) -> ObservationListResponse:
    """
    Add new Observation entities
    """
    pass


@app.get('/observations/table', response_model=ObservationTableResponse)
def get_observations_table(
    observation_unit_db_id: Optional[str] = Query(None, alias='observationUnitDbId'),
    germplasm_db_id: Optional[str] = Query(None, alias='germplasmDbId'),
    observation_variable_db_id: Optional[str] = Query(
        None, alias='observationVariableDbId'
    ),
    study_db_id: Optional[str] = Query(None, alias='studyDbId'),
    location_db_id: Optional[str] = Query(None, alias='locationDbId'),
    trial_db_id: Optional[str] = Query(None, alias='trialDbId'),
    program_db_id: Optional[str] = Query(None, alias='programDbId'),
    season_db_id: Optional[str] = Query(None, alias='seasonDbId'),
    observation_level: Optional[str] = Query(None, alias='observationLevel'),
    search_results_db_id: Optional[str] = Query(None, alias='searchResultsDbId'),
    observation_time_stamp_range_start: Optional[datetime] = Query(
        None, alias='observationTimeStampRangeStart'
    ),
    observation_time_stamp_range_end: Optional[datetime] = Query(
        None, alias='observationTimeStampRangeEnd'
    ),
    accept: WSMIMEDataTypes = Query(..., alias='Accept'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ObservationTableResponse:
    """
    Get a list of Observations in a table format
    """
    pass


@app.get('/observations/{observation_db_id}', response_model=ObservationSingleResponse)
def get_observations_observation_db_id(
    observation_db_id: str = Query(..., alias='observationDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ObservationSingleResponse:
    """
    Get the details of a specific Observations
    """
    pass


@app.put('/observations/{observation_db_id}', response_model=ObservationSingleResponse)
def put_observations_observation_db_id(
    observation_db_id: str = Query(..., alias='observationDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ObservationNewRequest = None,
) -> ObservationSingleResponse:
    """
    Update an existing Observation
    """
    pass


@app.get('/observationunits', response_model=ObservationUnitListResponse)
def get_observationunits(
    observation_unit_db_id: Optional[str] = Query(None, alias='observationUnitDbId'),
    germplasm_db_id: Optional[str] = Query(None, alias='germplasmDbId'),
    study_db_id: Optional[str] = Query(None, alias='studyDbId'),
    location_db_id: Optional[str] = Query(None, alias='locationDbId'),
    trial_db_id: Optional[str] = Query(None, alias='trialDbId'),
    program_db_id: Optional[str] = Query(None, alias='programDbId'),
    season_db_id: Optional[str] = Query(None, alias='seasonDbId'),
    observation_unit_level_name: Optional[str] = Query(
        None, alias='observationUnitLevelName'
    ),
    observation_unit_level_order: Optional[str] = Query(
        None, alias='observationUnitLevelOrder'
    ),
    observation_unit_level_code: Optional[str] = Query(
        None, alias='observationUnitLevelCode'
    ),
    include_observations: Optional[bool] = Query(None, alias='includeObservations'),
    external_reference_i_d: Optional[str] = Query(None, alias='externalReferenceID'),
    external_reference_source: Optional[str] = Query(
        None, alias='externalReferenceSource'
    ),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ObservationUnitListResponse:
    """
    Get a filtered set of Observation Units
    """
    pass


@app.put('/observationunits', response_model=ObservationUnitListResponse)
def put_observationunits(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ObservationunitsPutRequest = None,
) -> ObservationUnitListResponse:
    """
    Update a set of Observation Units
    """
    pass


@app.post('/observationunits', response_model=ObservationUnitListResponse)
def post_observationunits(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[ObservationUnitNewRequest] = None,
) -> ObservationUnitListResponse:
    """
    Add new Observation Units
    """
    pass


@app.get('/observationunits/table', response_model=ObservationUnitTableResponse)
def get_observationunits_table(
    observation_unit_db_id: Optional[str] = Query(None, alias='observationUnitDbId'),
    germplasm_db_id: Optional[str] = Query(None, alias='germplasmDbId'),
    observation_variable_db_id: Optional[str] = Query(
        None, alias='observationVariableDbId'
    ),
    study_db_id: Optional[str] = Query(None, alias='studyDbId'),
    location_db_id: Optional[str] = Query(None, alias='locationDbId'),
    trial_db_id: Optional[str] = Query(None, alias='trialDbId'),
    program_db_id: Optional[str] = Query(None, alias='programDbId'),
    season_db_id: Optional[str] = Query(None, alias='seasonDbId'),
    observation_level: Optional[str] = Query(None, alias='observationLevel'),
    accept: WSMIMEDataTypes = Query(..., alias='Accept'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ObservationUnitTableResponse:
    """
    Get a list of Observations in a table format
    """
    pass


@app.get(
    '/observationunits/{observation_unit_db_id}',
    response_model=ObservationUnitSingleResponse,
)
def get_observationunits_observation_unit_db_id(
    observation_unit_db_id: str = Query(..., alias='observationUnitDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ObservationUnitSingleResponse:
    """
    Get the details of a specific Observation Unit
    """
    pass


@app.put(
    '/observationunits/{observation_unit_db_id}',
    response_model=ObservationUnitSingleResponse,
)
def put_observationunits_observation_unit_db_id(
    observation_unit_db_id: str = Query(..., alias='observationUnitDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ObservationUnitNewRequest = None,
) -> ObservationUnitSingleResponse:
    """
    Update an existing Observation Units
    """
    pass


@app.get('/ontologies', response_model=OntologyListResponse)
def get_ontologies(
    ontology_db_id: Optional[str] = Query(None, alias='ontologyDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> OntologyListResponse:
    """
    Get the Ontologies
    """
    pass


@app.get('/scales', response_model=ScaleListResponse)
def get_scales(
    scale_db_id: Optional[str] = Query(None, alias='scaleDbId'),
    observation_variable_db_id: Optional[str] = Query(
        None, alias='observationVariableDbId'
    ),
    external_reference_i_d: Optional[str] = Query(None, alias='externalReferenceID'),
    external_reference_source: Optional[str] = Query(
        None, alias='externalReferenceSource'
    ),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ScaleListResponse:
    """
    Get the Scales
    """
    pass


@app.post('/scales', response_model=ScaleListResponse)
def post_scales(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[ScaleNewRequest] = None,
) -> ScaleListResponse:
    """
    Add new Scales
    """
    pass


@app.get('/scales/{scale_db_id}', response_model=ScaleSingleResponse)
def get_scales_scale_db_id(
    scale_db_id: str = Query(..., alias='scaleDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ScaleSingleResponse:
    """
    Get the details of a specific Scale
    """
    pass


@app.put('/scales/{scale_db_id}', response_model=ScaleSingleResponse)
def put_scales_scale_db_id(
    scale_db_id: str = Query(..., alias='scaleDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ScaleNewRequest = None,
) -> ScaleSingleResponse:
    """
    Update an existing Scale
    """
    pass


@app.post(
    '/search/images',
    response_model=Union[ImageListResponse, Field202AcceptedSearchResponse],
)
def post_search_images(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ImageSearchRequest = None,
) -> Union[ImageListResponse, Field202AcceptedSearchResponse]:
    """
    Submit a search request for Images
    """
    pass


@app.get(
    '/search/images/{search_results_db_id}',
    response_model=Union[ImageListResponse, Field202AcceptedSearchResponse],
)
def get_search_images_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[ImageListResponse, Field202AcceptedSearchResponse]:
    """
    Get the results of an Images search request
    """
    pass


@app.post(
    '/search/observations',
    response_model=Union[ObservationListResponse, Field202AcceptedSearchResponse],
)
def post_search_observations(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ObservationSearchRequest = None,
) -> Union[ObservationListResponse, Field202AcceptedSearchResponse]:
    """
    Submit a search request for a set of Observations
    """
    pass


@app.get(
    '/search/observations/{search_results_db_id}',
    response_model=Union[ObservationListResponse, Field202AcceptedSearchResponse],
)
def get_search_observations_search_results_db_id(
    accept: WSMIMEDataTypes = Query(..., alias='Accept'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
) -> Union[ObservationListResponse, Field202AcceptedSearchResponse]:
    """
    Returns a list of Observations based on search criteria.
    """
    pass


@app.post(
    '/search/observationunits',
    response_model=Union[ObservationUnitListResponse, Field202AcceptedSearchResponse],
)
def post_search_observationunits(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ObservationUnitSearchRequest = None,
) -> Union[ObservationUnitListResponse, Field202AcceptedSearchResponse]:
    """
    Submit a search request for Observation Units
    """
    pass


@app.get(
    '/search/observationunits/{search_results_db_id}',
    response_model=Union[ObservationUnitListResponse, Field202AcceptedSearchResponse],
)
def get_search_observationunits_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[ObservationUnitListResponse, Field202AcceptedSearchResponse]:
    """
    Observation Unit Search
    """
    pass


@app.post(
    '/search/variables',
    response_model=Union[
        ObservationVariableListResponse, Field202AcceptedSearchResponse
    ],
)
def post_search_variables(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ObservationVariableSearchRequest = None,
) -> Union[ObservationVariableListResponse, Field202AcceptedSearchResponse]:
    """
    Submit a search request for Observation Variables
    """
    pass


@app.get(
    '/search/variables/{search_results_db_id}',
    response_model=Union[
        ObservationVariableListResponse, Field202AcceptedSearchResponse
    ],
)
def get_search_variables_search_results_db_id(
    search_results_db_id: str = Query(..., alias='searchResultsDbId'),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> Union[ObservationVariableListResponse, Field202AcceptedSearchResponse]:
    """
    Get the results of a Observation Variable search request
    """
    pass


@app.get('/traits', response_model=TraitListResponse)
def get_traits(
    trait_db_id: Optional[str] = Query(None, alias='traitDbId'),
    observation_variable_db_id: Optional[str] = Query(
        None, alias='observationVariableDbId'
    ),
    external_reference_i_d: Optional[str] = Query(None, alias='externalReferenceID'),
    external_reference_source: Optional[str] = Query(
        None, alias='externalReferenceSource'
    ),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> TraitListResponse:
    """
    Get the Traits
    """
    pass


@app.post('/traits', response_model=TraitListResponse)
def post_traits(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[TraitNewRequest] = None,
) -> TraitListResponse:
    """
    Add new Traits
    """
    pass


@app.get('/traits/{trait_db_id}', response_model=TraitSingleResponse)
def get_traits_trait_db_id(
    trait_db_id: str = Query(..., alias='traitDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> TraitSingleResponse:
    """
    Get the details of a specific Trait
    """
    pass


@app.put('/traits/{trait_db_id}', response_model=TraitSingleResponse)
def put_traits_trait_db_id(
    trait_db_id: str = Query(..., alias='traitDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: TraitNewRequest = None,
) -> TraitSingleResponse:
    """
    Update an existing Trait
    """
    pass


@app.get('/variables', response_model=ObservationVariableListResponse)
def get_variables(
    observation_variable_db_id: Optional[str] = Query(
        None, alias='observationVariableDbId'
    ),
    trait_class: Optional[str] = Query(None, alias='traitClass'),
    study_db_id: Optional[str] = Query(None, alias='studyDbId'),
    external_reference_i_d: Optional[str] = Query(None, alias='externalReferenceID'),
    external_reference_source: Optional[str] = Query(
        None, alias='externalReferenceSource'
    ),
    page: Optional[int] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ObservationVariableListResponse:
    """
    Get the Observation Variables
    """
    pass


@app.post('/variables', response_model=ObservationVariableListResponse)
def post_variables(
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: List[ObservationVariableNewRequest] = None,
) -> ObservationVariableListResponse:
    """
    Add new Observation Variables
    """
    pass


@app.get(
    '/variables/{observation_variable_db_id}',
    response_model=ObservationVariableSingleResponse,
)
def get_variables_observation_variable_db_id(
    observation_variable_db_id: str = Query(..., alias='observationVariableDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
) -> ObservationVariableSingleResponse:
    """
    Get the details for a specific Observation Variable
    """
    pass


@app.put(
    '/variables/{observation_variable_db_id}',
    response_model=ObservationVariableSingleResponse,
)
def put_variables_observation_variable_db_id(
    observation_variable_db_id: str = Query(..., alias='observationVariableDbId'),
    authorization: Optional[constr(regex=r'^Bearer .*$')] = Query(
        None, alias='Authorization'
    ),
    body: ObservationVariableNewRequest = None,
) -> ObservationVariableSingleResponse:
    """
    Update an existing Observation Variable
    """
    pass
