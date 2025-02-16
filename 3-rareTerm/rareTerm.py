"""
Day 3 - 16 Februari 2025

rareTerm(matrixA) -> rareTerm & countRareTerm
- menemukan kolom(term) dengan kemunculan paling sedikit pada (Document Term) Matrix A
- abaikan elemen yg bernilai -999
rareTerm: indeks kolom dengan kemunculan paling sedikit [indeks dimulai dari 1]
countRareTerm: jumlah baris(dokumen) yang mengandung kolom(term) tersebut

> Testcase
A = [
    [0, 6, 2, 1, -999],
    [8, 9, 6, 2, -999],
    [1, 5, 4, 0, -999]
]
> Output:
rareTerm = 4
countRareTerm = 2
> Penjelasan:
- Kolom dengan kemunculan paling sedikit adalah kolom ke-4 dengan total kemunculan 3 (1+2)
- Jumlah baris yang mengandung kolom ke-4 adalah 2 baris, yaitu baris ke-1 & baris ke-2

"""