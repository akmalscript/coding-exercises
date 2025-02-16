
"""
> Solusi
(1) rareTerm
Simpan jumlah dari masing-masing kolom dalam array totalKemunculan,
lalu cari kolom dengan jumlah paling sedikit (nilai min dalam array total).
(2) countRareTerm
simpan jumlah baris dari masing-masing kolom dalam array totalBaris,
lalu akses indeks totalBaris[rareTerm], yang artinya mengakses total baris
dari kolom dengan jumlah paling sedikit.
"""
# Definisi Document Term Matrix
A = [
    [0, 6, 2, 1, -999],
    [8, 9, 6, 2, -999],
    [1, 5, 4, 0, -999]
]

# Fungsi RareTerm untuk mencari kolom dengan jumlah kemunculan paling sedikit
def rareTerm(matrix):
    nbaris = len(matrix)        # Jumlah baris
    mkolom = len(matrix[0])     # Jumlah kolom

    # Inisialisasi total kemunculan tiap kolom & jumlah baris yg mengandung term
    totalKemunculan = [0] * mkolom
    totalBaris = [0] * mkolom

    # Hitung total kemunculan & jumlah baris yang mengandung term
    for i in range(nbaris):
        for j in range(mkolom):
            if (matrix[i][j] != -999):  # Hanya diproses jika bukan -999
                totalKemunculan[j] += matrix[i][j]
                if(matrix[i][j] > 0):  # Jika > 0 artinya mengandung term
                    totalBaris[j] += 1
    
    # Cari kolom dengan jumlah kemunculan paling sedikit
    rareTerm = 0
    minKemunculan = totalKemunculan[0]
    for j in range (1, mkolom):
        if (totalKemunculan[j] < minKemunculan) and (totalKemunculan[j] > 0):  # Pastikan kemunculan > 0
            minKemunculan = totalKemunculan[j]
            rareTerm = j
    
    print('rareTerm:', rareTerm+1)  # 4
    print('countRareTerm:', totalBaris[rareTerm])  # 2

# Panggil fungsi dengan matriks A
rareTerm(A)