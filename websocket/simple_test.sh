#!/bin/bash

for ((i=0; i<200000; ++i)); do
	echo "$i run"
	python simple_client.py
	if (($? != 0 )); then
		exit
	fi
done
