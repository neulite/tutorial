import h5py
import pandas as pd

# 設定
input_file = 'output/spikes.h5'
output_file = 'spikes.csv'

def export_spikes_to_csv(h5_path, csv_path):
    try:
        with h5py.File(h5_path, 'r') as f:
            # HDF5内のデータパスを指定 
            group = f['spikes']['V1']
            
            # データの読み込み [cite: 25]
            node_ids = group['node_ids'][:]
            timestamps = group['timestamps'][:]
            
            # 単位情報の取得（デコードエラーを回避する安全な方法） [cite: 30, 72, 73]
            unit_attr = group['timestamps'].attrs.get('units', 'ms')
            # 属性がバイト列(bytes)の場合のみデコードし、文字列(str)ならそのまま使う
            unit = unit_attr.decode('utf-8') if hasattr(unit_attr, 'decode') else unit_attr

        # データフレームの作成（時間, ニューロン番号の順）
        df = pd.DataFrame({
            f'timestamp_{unit}': timestamps,
            'node_id': node_ids
        })

        # CSVへ書き出し
        df.to_csv(csv_path, index=False)
        
        print(f"完了: '{csv_path}' に保存しました（全 {len(df)} 行）。")
        print("-" * 30)
        print(df.head())

    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    export_spikes_to_csv(input_file, output_file)
