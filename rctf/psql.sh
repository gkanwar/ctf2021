#!/bin/bash

source .env
docker exec -it -e PGPASSWORD=${RCTF_DATABASE_PASSWORD} rctf_postgres_1 psql -U rctf rctf
