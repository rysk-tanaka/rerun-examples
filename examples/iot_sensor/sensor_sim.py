import time
import rerun as rr
import numpy as np


def main():
    # ログの初期化
    rr.init("iot_visualization", spawn=True)

    # 3D表示の初期設定
    # 座標軸の表示
    colors = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    vectors = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    origins = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    labels = ["X", "Y", "Z"]
    rr.log(
        "sensor/axis",
        rr.Arrows3D(origins=origins, vectors=vectors, colors=colors, labels=labels),
    )

    try:
        # データストリームのシミュレーション
        while True:
            # センサーデータの生成（例：温度）
            temperature = np.random.normal(25, 2)

            # 時系列データの記録
            rr.log("sensor/temperature", rr.Scalar(temperature))

            # 3D位置の記録
            # サイズを0.3に設定し、赤色で表示
            rr.log(
                "sensor/position",
                rr.Points3D(
                    positions=np.array([[0, 0, 0]]),  # numpy配列として指定
                    radii=0.3,
                    colors=np.array([[1.0, 0.0, 0.0]]),  # 点ごとのRGB値を指定
                ),
            )

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nシミュレーション終了")


if __name__ == "__main__":
    main()
