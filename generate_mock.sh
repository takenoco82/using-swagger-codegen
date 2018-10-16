rm -rf $PWD/app

docker run --rm \
    -v $PWD/out:/tmp/out -v $PWD/templates:/tmp/templates \
    --net using-swagger-codegen_my_networks \
    swaggerapi/swagger-codegen-cli \
    generate -l python-flask -i http://swagger-ui:8080/swagger.yaml -o /tmp/out -t /tmp/templates

mkdir -p $PWD/app/swagger_server
cp $PWD/out/swagger_server/__init__.py $PWD/app/swagger_server/
cp $PWD/out/swagger_server/util.py $PWD/app/swagger_server/
cp -R $PWD/out/swagger_server/models $PWD/app/swagger_server/

rm -rf $PWD/out
