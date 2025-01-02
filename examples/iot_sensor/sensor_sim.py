import time

import rerun as rr
import numpy as np


def main():
    # ログの初期化
    rr.init("iot_visualization", spawn=True)

    try:
        # データストリームのシミュレーション
        while True:
            # センサーデータの生成（例：温度）
            temperature = np.random.normal(25, 2)

            # 時系列データの記録
            rr.log("sensor/temperature", rr.Scalar(temperature))

            # 3D位置の記録
            rr.log("sensor/position", rr.Points3D(positions=[[0, 0, 0]]))

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nシミュレーション終了")


if __name__ == "__main__":
    main()
