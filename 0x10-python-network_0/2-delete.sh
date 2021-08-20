#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -s "http://localhost:5000/route_3" -X DELETE
