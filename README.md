## Output VMD data
Vocaloid Motion Data (.vmd) ファイルのデータをテキストファイルに出力する Python スクリプト。

<br>

### Usage
`readvmd.py` の引数に、vmd ファイルのパスを指定してください。

```bash:
readvmd.py <vmd file path>
```

`vmd_data.txt` が同ディレクトリに出力され、そのファイルに vmd 内のデータが書き込まれます。

<br>

### Note
- vmd ファイルの仕様は、t_tetosuki様の [ブログ](https://blog.goo.ne.jp/torisu_tetosuki/e/bc9f1c4d597341b394bd02b64597499d) から拝借しました

- 各データは namedtuple に格納しています

    [readvmd.py](readvmd.py) において、モーションデータや表情データの各フィールドのデータを取得したい場合は、`vmdread()` メソッドの第2引数に namedtuple ではなくその要素を渡してください。
