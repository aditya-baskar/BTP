#!/bin/bash

for i in {1..8}
do
	python newAgent.py $i &
done