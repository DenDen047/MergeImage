# MergeImage

画像を横方向に結合するプログラム

## 環境
* Docker version 18.09.2, build 6247962
* docker-compose version 1.23.2, build 1110ad01

## Usage
1. `<image_folder>`に結合したい画像を全て入れておく
2. 以下のコマンドを実行する
```
$ chmod +x run.sh
$ ./run.sh <image_folder>
```
3. `<image_folder>/result.png`が生成される

## Build only

docker-composeを使ってbuildできる。
```
$ cd docker
$ docker-compose up --build --no-start
$ docker rm docker_main_1
```

