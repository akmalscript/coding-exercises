/*
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

*/

/*
> Solusi
(1) rareTerm
Simpan jumlah dari masing-masing kolom dalam array totalKemunculan,
lalu cari kolom dengan jumlah paling sedikit (nilai min dalam array total).
(2) countRareTerm
simpan jumlah baris dari masing-masing kolom dalam array totalBaris,
lalu akses indeks totalBaris[rareTerm], yang artinya mengakses total baris
dari kolom dengan jumlah paling sedikit.
*/

const A = [
    [0, 6, 2, 1, -999],
    [8, 9, 6, 2, -999],
    [1, 5, 4, 0, -999]
];

function rareTerm(matrix) {
    const nbaris = matrix.length;       // Jumlah baris
    const mkolom = matrix[0].length;    // Jumlah kolom
    let totalKemunculan = [];           // Total kemunculan tiap kolom
    let totalBaris = [];                // Total baris (yg mengandung term) tiap kolom

    // Inisialisasi total kemunculan tiap kolom & jumlah baris yg mengandung term
    for(let j = 0; j < mkolom; j++) {
        totalKemunculan[j] = 0;
        totalBaris[j] = 0;
    }

    // Hitung total kemunculan & jumlah baris yang mengandung term
    for(let i = 0; i < nbaris; i++) {
        for(let j = 0; j < mkolom; j++) {
            if(matrix[i][j] !== -999) {  // Hanya diproses jika bukan -999
                totalKemunculan[j] += matrix[i][j];
                if(matrix[i][j] > 0) {  // Jika > 0 artinya mengandung term
                    totalBaris[j] += 1;
                }
            }
        }
    }

    // Cari kolom dengan jumlah kemunculan paling sedikit
    let rareTerm = 0;
    let minKemunculan = totalKemunculan[0];
    for(let j = 1; j < mkolom; j++) {
        if((totalKemunculan[j] < minKemunculan) && (totalKemunculan[j] > 0)) {  // Pastikan kemunculan > 0
            minKemunculan = totalKemunculan[j];
            rareTerm = j;
        }
    }
    
    console.log('rareTerm:', rareTerm+1);  // 4
    console.log('countRareTerm:', totalBaris[rareTerm]);  // 2
}

rareTerm(A);