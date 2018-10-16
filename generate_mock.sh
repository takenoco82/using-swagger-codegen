# modelsのパッケージ名
PACKAGE_MODELS=swagger_codegen

rm -rf $PWD/app

docker run --rm \
    -v $PWD/out:/tmp/out -v $PWD/templates:/tmp/templates \
    --net using-swagger-codegen_my_networks \
    swaggerapi/swagger-codegen-cli \
    generate -l python-flask -i http://swagger-ui:8080/swagger.yaml -o /tmp/out -t /tmp/templates -DpackageName=$PACKAGE_MODELS

mkdir -p $PWD/app/$PACKAGE_MODELS
cp $PWD/out/$PACKAGE_MODELS/__init__.py $PWD/app/$PACKAGE_MODELS/
cp $PWD/out/$PACKAGE_MODELS/util.py $PWD/app/$PACKAGE_MODELS/
cp -R $PWD/out/$PACKAGE_MODELS/models $PWD/app/$PACKAGE_MODELS/

rm -rf $PWD/out
