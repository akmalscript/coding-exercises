"""
Day 2 - 15 Februari 2025

ModusTerm(matrixA) -> modTerm & sumModTerm
- menemukan kolom(term) dengan kemunculan terbanyak pada (Document Term) Matrix A
- abaikan elemen yg bernilai -999
modTerm: indeks kolom terbanyak [dimulai dari 1]
sumModTerm: total kemunculan di kolom terbanyak

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

"""
> Solusi
Simpan jumlah dari masing-masing kolom dalam array total,
lalu cari kolom dengan jumlah terbanyak (nilai max dalam array total)."""
# Definisi Document Term Matrix
A = [
    [0, 6, 2, 1, -999],
    [8, 9, 6, 2, -999],
    [1, 5, 4, 0, -999]
]

# Fungsi ModusTerm untuk mencari term dengan kemunculan terbanyak
def ModusTerm(matrix):
    nbaris = len(matrix)          # Jumlah dokumen (baris)
    mkolom = len(matrix[0])       # Jumlah term (kolom)
    total = []                    # Total kemunculan untuk setiap kolom(term)
    
    # Inisialisasi total kemunculan untuk setiap kolom(term)
    total = [0] * mkolom  # contoh: [0, 0, 0, 0, 0]
    
    # Hitung total kemunculan untuk setiap kolom(term)
    for i in range(nbaris):
        for j in range(mkolom):
            if matrix[i][j] != -999:  # Hanya tambahkan jika bukan -999
                total[j] += matrix[i][j]
    
    # Cari term dengan kemunculan terbanyak (nilai max dalam array total)
    modTerm = 0
    sumModTerm = total[0]
    for j in range(1, mkolom):
        if total[j] > sumModTerm:
            sumModTerm = total[j]
            modTerm = j
    
    # Output hasil
    print('modTerm =', modTerm+1)  # 2
    print('sumModTerm =', sumModTerm)  # 20

# Panggil fungsi dengan matriks A
ModusTerm(A)
