import h5py
import pandas as pd
import numpy as np

input_h5 = 'output/v_report.h5'
output_csv = 'v_report.csv'

def extract_safe():
    try:
        with h5py.File(input_h5, 'r') as f:
            # 1. 膜電位データの取得 (20000, 1)
            voltages = f['/report/mcortex/data'][:]
            num_steps = voltages.shape[0]
            
            # 2. 時間データの取得
            time_node = f['/report/mcortex/mapping/time']
            
            # 属性(start/step)を探すが、なければデフォルト値や推論を行う
            try:
                t_start = time_node.attrs['start']
                t_step = time_node.attrs['step']
                times = t_start + (np.arange(num_steps) * t_step)
            except (KeyError, AttributeError):
                # 属性がない場合、time_node自体が配列(0, 0.1, 0.2...)であると仮定して読み込む
                times = time_node[:]
            
            # 3. 万が一、時間の配列が 3 しかなくてデータが 20000 ある場合への最終対策
            if len(times) != num_steps:
                print(f"警告: 時間配列の長さ({len(times)})がデータ({num_steps})と一致しません。")
                print("データの行数に合わせて時間軸を 0.1ms 刻みで再生成します。")
                # シミュレーションで一般的な 0.1ms 刻みで強制生成
                times = np.linspace(0, (num_steps - 1) * 0.1, num_steps)

            # 4. 書き出し
            df = pd.DataFrame({
                'Time (ms)': times,
                'Membrane Potential (mV)': voltages[:, 0]
            })
            
            df.to_csv(output_csv, index=False)
            print(f"--- 完了 ---")
            print(f"CSV保存先: {output_csv}")
            print(f"合計行数: {len(df)}")

    except Exception as e:
        print(f"予期せぬエラー: {e}")

if __name__ == "__main__":
    extract_safe()
