#!/bin/bash
#sends a JSON POST request to a URL
curl -sH "content-Type:application/json" -d "@$2" "$1"