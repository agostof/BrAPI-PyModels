#!/bin/bash

# Utility script to find and enumerate which classes are defined more than once across modules. It will produce class def counts and names as follows:
#   4  AdditionalInfo(BaseModel):
#   2  Season(BaseModel):

#  usage example:
# ./find_duplicate_classes.sh ../brapi_v2

CUTLEVEL="3"
BRAPIDIR=$1
if [ -n ""$2 ]
then
    CUTLEVEL=$2
fi
cd $BRAPIDIR

grep -nr "^class"  ./ | tr ":" " "| cut -d " " -f1,4 | grep -v ".orig" | sort -k2 | uniq -f1 -D | awk 'a[$1]++' |cut -d "/" -f$CUTLEVEL- 
