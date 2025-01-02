import argparse
import time

import pandas as pd
import rerun as rr
import rerun.blueprint as rrb


def load_sensor_data(file_path):
    """CSVファイルからセンサーデータを読み込む"""
    # ヘッダーなしのCSVを読み込み、カラム名を付ける
    df = pd.read_csv(
        file_path, header=None, names=["timestamp", "acc_x", "acc_y", "acc_z"]
    )
    return df


def visualize_data(data_df):
    """センサーデータを可視化する"""
    # ログの初期化
    rr.init("acceleration_visualization", spawn=True)

    # 時系列グラフの表示設定
    rr.send_blueprint(
        rrb.TimeSeriesView(
            origin="/acceleration",
            contents="**",  # すべてのデータを表示
        )
    )

    try:
        # データの可視化
        for _, row in data_df.iterrows():
            # 時系列データとして記録
            rr.set_time_seconds("time", row["timestamp"])

            # 各軸のデータを記録
            rr.log("acceleration/acc_x", rr.Scalar(row["acc_x"]))
            rr.log("acceleration/acc_y", rr.Scalar(row["acc_y"]))
            rr.log("acceleration/acc_z", rr.Scalar(row["acc_z"]))

            time.sleep(0.01)  # 表示の更新間隔

    except KeyboardInterrupt:
        print("\nVisualization stopped")


def main():
    # コマンドライン引数の解析
    parser = argparse.ArgumentParser(description="Visualize sensor data from CSV file")
    parser.add_argument("csv_file", help="Path to the CSV file containing sensor data")
    args = parser.parse_args()

    # データの読み込み
    try:
        data_df = load_sensor_data(args.csv_file)
        print(f"Loaded {len(data_df)} data points")
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return

    # データの可視化
    visualize_data(data_df)


if __name__ == "__main__":
    main()
