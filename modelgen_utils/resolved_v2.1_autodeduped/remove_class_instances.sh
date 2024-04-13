#!/bin/bash

#Note: runs from the base (above /api) directory, hardcoded because it's also peeling a level off the path listed in duplicate_class_location... Running it from somewhere else
#would require passing that path to duplicate_class_location and then fixing ClassRemover to read the partial link
./duplicate_class_location.sh . 1  | xargs -P1 -n2 java ClassRemover
