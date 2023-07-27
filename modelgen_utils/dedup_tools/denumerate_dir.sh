#!/bin/bash
find $1 | grep 'models.py' | grep -v '.orig' | xargs -n1 java Denumerator
