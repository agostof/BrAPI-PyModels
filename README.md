# BrAPI-FastAPI
#FastAPI-compatible BrAPI

Implementation of the [BrAPI v2.0](https://brapi.org/) specification for Python using the [FastAPI](https://fastapi.tiangolo.com/) framework.
* includes models and server stubs (views.py) for Core, Genotyping, Germplasm, Phenotyping
* use as a template to create your BrAPI server

#### Quick start ####
1. Installation if using pyenv (Python $version could be 3.8.3 and above)
``` sh
pyenv virtualenv 3.9.1 WebAPI
pyenv activate WebAPI
```
2. Install module dependencies
``` sh
python -m pip install -r requirements.txt
```
3. Then start server (do check the script in case you want to modify how the server starts)
``` sh
./start_dev_server.sh
```

4. Now check the API server at: http://127.0.0.1:9000/brapi/v2/serverinfo

A few test(dummy) endpoints have been provided from each BrAPI module: Core, Genotyping, Germplasm, Phenotyping.

