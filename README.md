## Overview


## BrAPI-PyModels: Python-based Breeder's API (BrAPI) data models

Implementation of the [BrAPI v2.0](https://brapi.org/) and 2.1 specification for Python using [pydantic](https://pydantic-docs.helpmanual.io/) data models. Note: *This project is a sibling to [BrAPI-FastAPI](https://github.com/agostof/BrAPI-FastAPI), BrAPI implementation server stubs*.
* Includes models for [Core](models/brapi_v2/core), [Genotyping](models/brapi_v2/genotyping), [Germplasm](models/brapi_v2/germplasm), and [Phenotyping](models/brapi_v2/phenotyping).
* Use models to create a [BrAPI client](client/barebones_brapi_client.py) (a.k.a *BrAPP*) or to create a client library.
* Integrate models with other Python frameworks.


## Using as a BrAPI server template, integration

These models can be used as a template for starting a new project. They could also be *integrated* into an already *existing* project (the pydantic models should work with other Python frameworks).
It might be convenient to add these into your project as a submodule by running:

```sh
git submodule add https://github.com/agostof/BrAPI-PyModels [optional local_name]
```
Then use (by copying or modifying) the appropriate BrAPI module(s) models as needed.

## Using for building BrAPI clients

Simple clients can be built using the Pydantic models. Using these models, clients can parse the responses returned by a BrAPI server with little effort.
***Note:*** *A more capable BrAPI* ***client library*** *is also possible* ***(coming soon)****, for now we provide a very basic client use case.*

For example, to parse the *serverInfo* call response we could import the following **ServerInfoResponse** model:
```python
from brapi_v2.core.models import ServerInfoResponse
```
then use it to construct an object usable by the client:
```python
# [pseudo code]
# ... retrieve response using your favorite library ... 
# then parse response_obj using pydantic model
server_info = ServerInfoResponse.parse_obj(response_obj)
# access the BrAPI response metadata 
server_info.metadata
# For more details and *working* code, please check client's documentation linked below.
```
The code above is merely an introduction and omit several details. The steps necessary to get this process to work are demonstrated by a simple, [barebones, brapi client](client/barebones_brapi_client.py) implementation. This code calls and parses the demo endpoints defined by the BrAPI server, see the [client's documentation](client/README.md) for details.

## Notes

OpenApi-compatible codegen tools were used to generate the foundational data models and servers stubs used on this project. The auto-generated models might still need some cleaning up. ~~Also some models names are *repeated* across modules e.g. **Metadata**, **AdditionalInfo**.~~ These *repeated* models were consolidated and they are uniquely imported from core.models e.g. **core.models.Metadata**,  **core.models.AdditionalInfo**, etc.

These redundant Pydantic models occur because the BrAPI OpenAPI spec files were processed independently.
~~Ideally, they should be consolidated as part of the Core module or in a *commons* package.~~ Check the [modelgen_utils](modelgen_utils) directory for additional details.

## BrAPI v2.1 Status and Notes

The V2.1 model was an attempt to automate a lot of the code-gen cleanup so future BrAPI spec updates could be easily integrated.

Josh L.S. (jdl232 at cornell.edu) tried to merge all the duplicates that were functionally identical via script. The script however missed quite a few instances of duplicate classes. The *auto-deduplication code* differentiated classes by adding a sequential numerical suffix e.g `ClassName1`, `ClassName2`, to the class names. The code may still have several objects where `ClassName#m` and `ClassName#n` are identical, but were separated as different classes by the *autogenerator*. The fix to this is to delete `ClassName#m` and replace its mentions with `ClassName#n`, which is what the [auto-deduplication tools](modelgen_utils/dedup_tools) in the v_2.1_autogen folder attempt to do automatically.

There were also changes in how Pydantic models are specified when this work was underway. The models provided can be used as a start, but changes might be needed for your specific usecase.

