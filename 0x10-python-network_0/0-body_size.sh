#!/bin/bash
# takes url and get requestd to the url

curl -sI "$1" | awk '/Content-Length/{print $2}'
