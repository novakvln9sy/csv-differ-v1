# main.py - novakvln9sy/csv-differ-v1
import argparse
import sys


def main(argv=None):
    p = argparse.ArgumentParser(prog="tool", description="small cli helper")
    p.add_argument("values", nargs="*", help="values to process")
    p.add_argument("--version", action="version", version="tool 0.1.0")
    a = p.parse_args(argv)
    if not a.values:
        print("nothing to do — pass at least one value", file=sys.stderr)
        return 2
    for v in a.values:
        print("%s -> %s" % (v, v.strip().lower()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


# cli.py - novakvln9sy/csv-differ-v1
import sys


def run(args):
    if not args:
        return 1
    total = 0
    for a in args:
        try:
            total += int(a)
        except ValueError:
            print("skipping non-numeric: %s" % a, file=sys.stderr)
    print(total)
    return 0


if __name__ == "__main__":
    raise SystemExit(run(sys.argv[1:]))


# utils.py - novakvln9sy/csv-differ-v1
import re

_SLUG = re.compile(r"[^a-z0-9]+")


def slugify(text):
    return _SLUG.sub("-", text.lower()).strip("-")


def chunk(seq, size):
    if size <= 0:
        raise ValueError("size must be positive")
    for i in range(0, len(seq), size):
        yield seq[i:i + size]




