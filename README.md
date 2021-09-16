# healthcheck

1. 健康記録表に `healthcheck3_202109-202112-2.pdf` と名前をつけてください。
2. `input.csv` を編集してください。最初の行の月が基準月になります。ひと月分です。
   - `日付(yyyy/mm/dd) 朝の体温 夕の体温 [体調不良たち]`
   - 体調不良たちはスペース区切りで入力してくだい
     1. 咳嗽（ガイソウ、咳です）
     2. 倦怠感
     3. 関節痛
     4. 呼吸困難
     5. 咽頭痛
     6. 鼻汁・鼻閉（ビヘイ、鼻づまりです）
     7. 頭痛
     8. 下痢
     9. 味覚異常
     10. 嗅覚異常
3. `python3 healthcheck.py` をしてください。
4. `out.pdf` が出てきます。

ファイル名など気に食わなければ書き換えてください。
その他は非対応です。気が向いたら対応します。