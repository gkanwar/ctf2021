#!/bin/bash

source .env
docker exec -it -e PGPASSWORD=${RCTF_DATABASE_PASSWORD} rctf_postgres_1 pg_dump -C -U rctf rctf > rctf.dump
