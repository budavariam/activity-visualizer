#!/bin/bash

# assume that the virtual env has been activated and pwd is the project root directory

rm ./activity_selector-*.tar.gz
mv ./components/activity_selector/dist/activity_selector-* .
NEW_FILE=$(find . -name 'activity_selector*' -maxdepth 1 | head -1 | xargs basename)
sed -i.bak "s/activity_selector-\S*/$NEW_FILE/" ./requirements.txt
rm  ./*.bak
pip install "./$NEW_FILE"