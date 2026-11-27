# csv-differ-v1

Bandingkan dua CSV berdasarkan satu kolom kunci. Python 3.9+, tanpa dependensi
(stdlib `csv` saja).

## Pakai

```
python3 main.py lama.csv baru.csv -k id
```

Output menampilkan jumlah baris yang ditambah (`+`), dihapus (`-`), dan berubah
(`~`), plus daftar kolom yang berubah per baris. Exit code `1` kalau ada
perbedaan, `0` kalau identik - bisa dipakai langsung di script atau CI.

Opsi:

- `-k, --key` - kolom kunci (default: kolom pertama)
- `--limit` - maksimum baris dicetak per kategori (default 50)

## Contoh

```
$ python3 main.py old.csv new.csv -k id
key=id  lama=3  baru=3
+1 ditambah  -0 dihapus  ~1 berubah
  + 104
  ~ 2: qty
```
