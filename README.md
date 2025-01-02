# Rerun サンプル集

[Rerun](https://www.rerun.io/) のロギング・可視化機能を試すためのサンプルコード集です。

## サンプル一覧

### 単調増加グラフ

0から99までの単純な直線グラフを描画するサンプルです。

### toio 3Dモデル

toioのIMUから取得した姿勢角データを使って3Dモデルを回転させるサンプルです。

## 動作環境

- Python 3.12
- uv
- rerun-sdk
- toio-py (toio 3Dモデルのサンプルのみ)

## セットアップ

uvを使用して環境を構築します。

``` bash
# プロジェクトの初期化
uv init

# 依存パッケージのインストール
uv add rerun-sdk
uv add toio-py  # toio 3Dモデルのサンプルを実行する場合のみ

# 仮想環境の有効化
. .venv/bin/activate  # Linux/Mac
# または
.\.venv\Scripts\activate  # Windows
```

## サンプルの実行方法

### 単調増加グラフ

``` bash
python examples/simple_graph/plot_graph.py
```

### toio 3Dモデル

``` bash
python examples/toio_3d/posture.py
```

## ディレクトリ構成

``` plaintext
rerun-examples/
├── README.md                    # このファイル
├── examples/
│   ├── simple_graph/           # 単調増加グラフのサンプル
│   │   ├── README.md
│   │   └── plot_graph.py
│   └── toio_3d/               # toio 3Dモデルのサンプル
│       ├── README.md
│       ├── posture.py
│       └── toiocorecube_v003.gltf
└── .gitignore
```

## 参考

- [オープンソースのロギング・可視化ツールRerunを使ってみよう](https://zenn.dev/turing_motors/articles/fa687a8d30b373)
- [Rerun公式ドキュメント](https://www.rerun.io/docs)
