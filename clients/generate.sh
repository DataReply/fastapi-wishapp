LANGUAGE=$1

docker run --rm -v "${PWD}/$LANGUAGE:/local" openapitools/openapi-generator-cli generate \
    -i http://host.docker.internal:8000/openapi.json \
    -g $LANGUAGE \
    -o /local/out/$LANGUAGE


# Add '--library asyncio' argument to generate async python client
