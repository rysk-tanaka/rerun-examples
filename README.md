# Rerun サンプル集

[Rerun](https://www.rerun.io/) のロギング・可視化機能を試すためのサンプルコード集です。

## サンプル一覧

### 単調増加グラフ

0から99までの単純な直線グラフを描画するサンプルです。

### IOTセンサーシミュレーション

温度センサーと位置情報を持つIOTデバイスをシミュレートし、リアルタイムでデータを可視化するサンプルです。

- 温度データの時系列表示
- センサーの3D位置表示

### 3軸加速度センサーシミュレーション

3軸（X, Y, Z）の加速度データをシミュレートし、時系列グラフとして可視化するサンプルです。

- 3軸の加速度データをリアルタイムでグラフ表示
- 各軸を異なる色で表示
- グラフのカスタマイズ設定

## 動作環境

- Python 3.12
- uv
- rerun-sdk
- pandas

## セットアップ

uvを使用して環境を構築します。

``` bash
# プロジェクトの初期化
uv init

# 依存パッケージのインストール
uv add rerun-sdk

# 仮想環境の有効化
. .venv/bin/activate  # Linux/Mac
# または
.\.venv\Scripts\activate  # Windows
```

## ディレクトリ構成

``` plaintext
rerun-examples/
├── README.md                    # このファイル
├── examples/
│   ├── simple_graph/           # 単調増加グラフのサンプル
│   │   ├── README.md
│   │   └── plot_graph.py
│   └── iot_sensor/            # IoTセンサーのサンプル
│       ├── README.md
│       └── sensor_sim.py
└── .gitignore
```

## 参考

- [オープンソースのロギング・可視化ツールRerunを使ってみよう](https://zenn.dev/turing_motors/articles/fa687a8d30b373)
- [Rerun公式ドキュメント](https://www.rerun.io/docs)
