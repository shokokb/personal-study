# personal-study

* 個人勉強用（SWEの面接用）  
  Personal study repository (for SWE interview preparation)
* 対応バージョン Python3（幅広く使われている言語のため）  
  Supported version: Python 3 (widely used language)
* Python3の実行環境はDocker composeで作成する  
  Python 3 execution environment is created with Docker Compose

# 環境の作り方 / How to set up the environment

```
$ cd (env_path)
# コンテナ起動
$ docker-compose up -d --build
# コンテナに接続
$ docker-compose exec python3 bash
# シャットダウン
$ docker-compose down
```


## Recommended Books / おすすめ書籍

- **Code Complete**  
  Author: Steve McConnell  
  ソフトウェア開発のベストプラクティスを網羅した名著。  
  A comprehensive guide to software construction best practices.

- **なっとくアルゴリズム**  
  著者：小川 龍之介  
  アルゴリズムの基礎をわかりやすく解説した日本語の入門書。  
  An easy-to-understand Japanese introduction to fundamental algorithms.

- **アルゴリズム図鑑**  
  著者：石田 保輝  
  イラストでアルゴリズムを解説するビジュアルな書籍。  
  A visual book explaining algorithms with illustrations.

- **独学プログラマ**  
  著者：Cory Althoff  
  初心者が独学でプログラミングを学ぶための実践的なガイド。  
  A practical guide for beginners to learn programming by self-study.

- **Coding Interview**  
  著者：Gayle Laakmann McDowell  
  コーディング面接対策の定番書籍（原題："Cracking the Coding Interview"）。  
  The classic book for coding interview preparation.

- **結城浩のDesign Pattern**  
  著者：結城 浩  
  日本語で丁寧に解説されたデザインパターンの入門書。  
  An introductory book on design patterns with clear Japanese explanations.s