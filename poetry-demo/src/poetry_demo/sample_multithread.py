import concurrent.futures
import time

def process_file(file_name):
    """
    ファイルの出力処理を模倣する関数。
    """
    print(f"{file_name} の処理を開始します...")
    time.sleep(2)  # 処理に時間がかかることをシミュレート
    with open(file_name, "w") as f:
        f.write(f"{file_name} の内容です。")
    print(f"{file_name} の処理が完了しました。")
    return f"{file_name} が正常に出力されました。"

def main():
    """
    マルチスレッドでファイル出力を行うメイン関数。
    """
    # 出力するファイル名のリストを作成
    files_to_create = [f"output_file_{i}.txt" for i in range(1, 101)]

    # 同時に実行するスレッド数の上限
    max_workers = 5

    # ThreadPoolExecutor を使用してマルチスレッド処理を実行
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # map()メソッドで各ファイルに処理を割り当て、結果を取得
        # map()は、第二引数のイテラブルな要素を順番に取り出し、第一引数の関数に渡して実行
        results = executor.map(process_file, files_to_create)

    # 全ての処理が完了した後に結果を出力
    for result in results:
        print(result)

if __name__ == "__main__":
    main()