#!/usr/bin/env python3
"""
Menyinkronkan blok ```java pada satu berkas naskah dengan isi berkas
sumber di kode/bab-NN/ yang sesungguhnya (dicocokkan lewat nama kelas
public di dalam fence), agar naskah selalu identik dengan kode yang
sudah diuji kompilasi.

Pemakaian:
    python tools/sync_kode.py bab-01
    python tools/sync_kode.py bab-01 bab-02 bab-03
"""

import re
import sys
from pathlib import Path

AKAR = Path(__file__).resolve().parent.parent
POLA_FENCE = re.compile(r"```java\n(.*?)```", re.DOTALL)
POLA_KELAS = re.compile(r"public (?:final )?class (\w+)")


def sinkron(nomor_bab):
    naskah = AKAR / "naskah" / f"{nomor_bab}.md"
    kode_dir = AKAR / "kode" / nomor_bab
    if not naskah.exists():
        print(f"lewati: {naskah} tidak ada")
        return
    berkas_java = {p.stem: p for p in kode_dir.rglob("*.java")}
    if not berkas_java:
        print(f"lewati: tidak ada .java di {kode_dir}")
        return

    def ganti(m):
        isi = m.group(1)
        if not isi.lstrip().startswith("package "):
            return m.group(0)  # cuplikan tulisan tangan, jangan disentuh
        mk = POLA_KELAS.search(isi)
        if not mk or mk.group(1) not in berkas_java:
            return m.group(0)
        baru = berkas_java[mk.group(1)].read_text(
            encoding="utf-8").rstrip("\n")
        return f"```java\n{baru}\n```"

    teks = naskah.read_text(encoding="utf-8")
    teks_baru, n = POLA_FENCE.subn(ganti, teks)
    naskah.write_text(teks_baru, encoding="utf-8")
    print(f"{nomor_bab}: {n} blok kode diperiksa/disinkronkan")


if __name__ == "__main__":
    daftar = sys.argv[1:] or [f"bab-{i:02d}" for i in range(1, 16)]
    for nomor in daftar:
        sinkron(nomor)
