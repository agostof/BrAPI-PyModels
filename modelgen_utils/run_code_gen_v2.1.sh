#!/bin/bash

VERSION=2.1

OUT_DIR="resolved_v${VERSION}"
OPENAPI_MODELS_DIR="brapi_openapi_models/v${VERSION}/"

for MODULE in Core Genotyping Germplasm Phenotyping
do
   RESULT_DIR="${OUT_DIR}/api/${MODULE,,}"
   MODEL_SOURCE="${OPENAPI_MODELS_DIR}/PlantBreedingAPI-BrAPI-${MODULE}-${VERSION}-resolved.yaml"
   echo "Running coden for: [BrAPI ${MODULE} v${VERSION}]"
   echo "Reading OPENAPI source: ${MODEL_SOURCE}"
   echo "Will store output at: [${RESULT_DIR}]"
   
   mkdir -pv resolved_v${VERSION}/api/${MODULE,,}
   fastapi-codegen -i ${MODEL_SOURCE} -o ${RESULT_DIR}

done


