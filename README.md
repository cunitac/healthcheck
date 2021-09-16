# healthcheck

1. `PyPDF2` と `reportlab` をインストールしてください。
1. 健康記録表に `healthcheck3_202109-202112-2.pdf` と名前をつけてください。
2. `input.csv` を編集してください。最初の行の月が基準月になります。ひと月分です。
   - `日付(yyyy/mm/dd) 朝の体温 夕の体温 [体調不良たち]`
   - 体調不良たちはコンマ（カンマ？）区切りで入力してくだい
     - 0=咳嗽（ガイソウ、咳です）
     - 1=倦怠感
     - 2=関節痛
     - 3=呼吸困難
     - 4=咽頭痛
     - 5=鼻汁・鼻閉（ビヘイ、鼻づまりです）
     - 6=頭痛
     - 7=下痢
     - 8=味覚異常
     - 9=嗅覚異常
3. `python3 healthcheck.py` をしてください。
4. `out.pdf` が出てきます。

ファイル名など気に食わなければ書き換えてください。
その他は非対応です。気が向いたら対応します。