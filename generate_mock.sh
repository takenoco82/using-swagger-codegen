WORKSPACE_FOLDER=`pwd`
# swagger-codegenで生成する際のパッケージ名
PACKAGE_CODEGEN=swagger_codegen
# swagger-codegenでいったん出力するディレクトリ
TMP_DIR=${WORKSPACE_FOLDER}/tmp
# swagger-codegenで使用するテンプレートを格納するでディレクトリ
TEMPLATES_DIR=${WORKSPACE_FOLDER}/templates
# 最終的にswagger-codegenから出力したファイルを格納するディレクトリ
CODEGEN_DIR=${WORKSPACE_FOLDER}/src/${PACKAGE_CODEGEN}/


# swagger-codegenから出力したファイルをディレクトリごと削除
rm -rf $CODEGEN_DIR

docker run --rm \
    -v $TMP_DIR:/tmp/out
    -v $TEMPLATES_DIR:/tmp/templates \
    --net using-swagger-codegen_my_networks \
    swaggerapi/swagger-codegen-cli generate \
        -l python-flask
        -i http://swagger-ui:8080/swagger.yaml
        -o /tmp/out
        -t /tmp/templates
        -DpackageName=$PACKAGE_CODEGEN

# 出力したファイルのうち、必要なファイルをコピー
mkdir -p $CODEGEN_DIR
cp ${TMP_DIR}/$PACKAGE_CODEGEN/__init__.py $CODEGEN_DIR
cp ${TMP_DIR}/$PACKAGE_CODEGEN/util.py $CODEGEN_DIR
cp -R ${TMP_DIR}/$PACKAGE_CODEGEN/models $CODEGEN_DIR

# 一時ディレクトリを削除
rm -rf $TMP_DIR
