#!/bin/bash
docker build -t blog_site .
docker container prune -f
docker run --rm -p 4325:4325 blog_site
