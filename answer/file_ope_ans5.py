"""
問題5:
JSONファイル config.json には以下のような設定データが格納されています。

{
  "debug": true,
  "log_level": "info",
  "data_dir": "/path/to/data"
}

"debug" フラグが true の場合は、全てのログを表示し、false の場合は重要なログのみを表示するプログラムを作成してください。
"""
import json

with open('config.json', 'r') as json_file:
    config_data = json.load(json_file)

debug_mode = config_data.get('debug', False)

if debug_mode:
    log_level = config_data.get('log_level', 'info')
    data_dir = config_data.get('data_dir', '/path/to/data')

    print(f"Debug Mode: ON")
    print(f"Log Level: {log_level}")
    print(f"Data Directory: {data_dir}")
else:
    print("Debug Mode: OFF")
    print("Displaying important logs only.")