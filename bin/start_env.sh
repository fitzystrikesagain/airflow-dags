#!/usr/bin/env bash

docker compose --file docker-compose.dev.yml --project-name localstack down --volumes || true
if [[ "$1" = "--build" ]]
then
  docker compose --file docker-compose.dev.yml --project-name localstack up --detach --build
else
  docker compose --file docker-compose.dev.yml --project-name localstack up --detach
fi

until [ "`docker inspect -f {{.State.Running}} airflow-tests`"=="true" ]; do
  printf '.'
  sleep 1;
done;

docker exec -ti airflow-tests airflow db init