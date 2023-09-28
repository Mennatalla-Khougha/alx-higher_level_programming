#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me
curl -sX PUT -o /dev/null -w "You got me!" 0.0.0.0:5000/catch_me
