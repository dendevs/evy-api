#!/bin/bash
# Arrète le docker splash précédemment lancé.

docker stop splash && docker rm splash;

exit $?
