#!/bin/bash
# takes url and get requestd to the url
curl -s $1 | wc -c
