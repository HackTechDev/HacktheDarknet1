#!/bin/sh

rm darknet.db

echo
echo "***********************************"
echo "************** table **************"
echo "***********************************"
python ./tableDatabase.py

echo
echo "***********************************"
echo "************** populate ***********"
echo "***********************************"
python ./populateDatabase.py

echo 
echo "***********************************"
echo "************** query **************"
echo "***********************************"
#python ./queryDatabase.py
