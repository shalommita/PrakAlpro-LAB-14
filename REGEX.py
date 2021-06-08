# Shalommita P
# 71200640
# Inf - UKDW

import re

def lahir():
    inp=input("Masukkan tanggal lahir anda (tt-bb-hhhh) : ")
    cmp=re.compile("\d{1,2}-\d{1,2}-\d{1,4}")
    txt=cmp.match(inp)
    if txt:
        print("Benar")
        print("Format tanggal lahir Anda sudah benar yaitu ",inp)
    else:
        print("Terjadi kesalahan. Mohon cek ulang.")

lahir()