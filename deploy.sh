#!/bin/bash

aws s3 cp ./index.html s3://deadbeef.io/
aws cloudfront create-invalidation --distribution-id EH9CMSD54V6Z9 --paths "/*"
