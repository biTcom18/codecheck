!#/bin/sh

set -e

IMAGE_ID=$(docker inspect ${HEROKU_REGISTRY_IMAGE} --format={{.Id}})
PAYLOAD='{"updates": [{"type": "web", "docker-image": "'"$IMAGE_ID"'"}]}'

curl -n -X PATCH https://api.heroku.com/apps/$HEROKU_APP_NAME/formation\
  -d "${PAYLOAD}" \
  -H "Content-type: application/json" \
  -H "Accept: application/vnd.heroku.json; version=3.docker-releases" \
  -H "Authorisation: Bearer ${HEROKU_AUTH_TOKEN}"
