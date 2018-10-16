rm -rf $PWD/app

docker run --rm \
    -v $PWD/app:/tmp/out -v $PWD/templates:/tmp/templates \
    --net using-swagger-codegen_my_networks \
    swaggerapi/swagger-codegen-cli \
    generate -l python-flask -i http://swagger-ui:8080/swagger.yaml -o /tmp/out -t /tmp/templates
