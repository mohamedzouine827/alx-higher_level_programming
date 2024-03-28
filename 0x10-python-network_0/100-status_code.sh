#!/bin/bash
# Sends a GET
curl -s -o /dev/null -w "%{http_code}" "$1"
