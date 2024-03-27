#!/bin/bash
#display the bytes 
curl -s "$1" | wc -c
