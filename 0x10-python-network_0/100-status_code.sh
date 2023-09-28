#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
curl -so /dev/null -w "%{http_code}" "$1"
