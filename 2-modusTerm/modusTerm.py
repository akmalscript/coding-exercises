"""
Day 2 - 15 Februari 2025

ModusTerm(A, modTerm, sumModTerm)
- menemukan kolom(term) dengan kemunculan terbanyak pada (Document Term) Matrix A
- abaikan elemen yg bernilai -999

> Testcase
A = [
    [0, 6, 2, 1, -999],
    [8, 9, 6, 2, -999],
    [1, 5, 4, 0, -999]
]
> Output:
modTerm = 2  (indeks kolom(term) terbanyak [dimulai dari 1])
sumModTerm = 20  (total kemunculan di kolom(term) terbanyak)
> Penjelasan:
Term/kolom dengan kemunculan terbanyak adalah term/kolom ke-2
dengan total kemunculan 20 (6+9+5).

"""