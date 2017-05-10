#!/bin/bash
# Lance le docker qui exécuté splash.

docker run --name splash -p 8050:8050 scrapinghub/splash

exit $?
