# using-swagger-codegen

## これは何？
- swagger-codegenを使って、テンプレートからコードを自動生成するサンプルです。
- テンプレートは flaskConnexion からコピーしたものを一部修正しています。
    - 対象は基本的にモデルだけです。
    - 例外としてモデルから使用するものも含まれています。
- Makefileで、swagger-codegenから自動生成し、生成したコードに対するテストまで実行できます。

## 使い方
``` sh
# swagger-codegenを実行後にテストを実行する
make test

# コンテナ名が重複してエラーになったとき
make clean
```
