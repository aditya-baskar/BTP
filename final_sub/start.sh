#!/bin/bash

for i in {1..4}
do
	python newAgent.py $i &
	sleep 0.23
done
