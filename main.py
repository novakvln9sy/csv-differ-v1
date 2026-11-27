#!/usr/bin/env python3
# csv-differ: bandingkan dua CSV berdasarkan satu kolom kunci. Stdlib only.
import argparse
import csv
import sys


def load(path, key):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if rows and key not in rows[0]:
        sys.exit("kolom kunci %r tidak ada. kolom tersedia: %s" % (key, ", ".join(rows[0])))
    return {r[key]: r for r in rows if r.get(key) is not None}


def first_col(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        head = next(csv.reader(f), [])
    if not head:
        sys.exit("CSV kosong")
    return head[0]


def main():
    p = argparse.ArgumentParser(description="Bandingkan dua CSV per kolom kunci.")
    p.add_argument("old")
    p.add_argument("new")
    p.add_argument("-k", "--key", default=None, help="kolom kunci (default: kolom pertama)")
    p.add_argument("--limit", type=int, default=50, help="maks baris dicetak per kategori")
    a = p.parse_args()
    if not a.key:
        a.key = first_col(a.old)

    old, new = load(a.old, a.key), load(a.new, a.key)
    added = [k for k in new if k not in old]
    removed = [k for k in old if k not in new]
    changed = [(k, [c for c in new[k] if new[k][c] != old[k].get(c)])
               for k in new if k in old
               and any(new[k][c] != old[k].get(c) for c in new[k])]
    print("key=%s  lama=%d  baru=%d" % (a.key, len(old), len(new)))
    print("+%d ditambah  -%d dihapus  ~%d berubah" % (len(added), len(removed), len(changed)))
    for k in added[: a.limit]:
        print("  + " + str(k))
    for k in removed[: a.limit]:
        print("  - " + str(k))
    for k, cols in changed[: a.limit]:
        print("  ~ %s: %s" % (k, ", ".join(cols)))
    return 0 if not (added or removed or changed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
