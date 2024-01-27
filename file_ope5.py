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

with open('resources/config.json', 'r', encoding='utf-8') as json_file:
  config_data = json.load(json_file)
  debug_flg = config_data.get('debug')
  
  if debug_flg:
    log_level = config_data.get('log_level')
    data_dir = config_data.get('data_dir')
    
    print(f'debug mode is {debug_flg}')
    print(f'log level is {log_level}')
    print(f'data directory is {data_dir}')
  else:
    print(f'debug mode is {debug_flg}')
    print('display only important log')
