/*
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
modTerm = 2
sumModTerm = 20
> Penjelasan:
Term/kolom dengan kemunculan terbanyak adalah term/kolom ke-2
dengan total kemunculan 20 (6+9+5).

*/

/*
> Solusi
Simpan jumlah kemunculan dari masing-masing kolom dalam array Total,
lalu cari kolom dengan jumlah terbanyak (nilai max dalam array total) */

const A = [
    [0, 6, 2, 1, -999],
    [8, 9, 6, 2, -999],
    [1, 5, 4, 0, -999]
];

function ModusTerm(A) {
    const nbaris = A.length;        // Jumlah dokuman (baris)
    const mkolom = A[0].length;     // Jumlah term (kolom)
    let total = [];                 // Total kemunculan untuk setiap kolom(term)

    // Inisialisasi total kemunculan untuk setiap kolom(term)
    for(let j = 0; j < mkolom; j++) {
        total[j] = 0;  // contoh: [0, 0, 0, 0, 0]
    }

    // Hitung total kemunculan untuk setiap kolom(term)
    for(let i = 0; i < nbaris; i++) {
        for(let j = 0; j < mkolom; j++) {
            if(A[i][j] !== -999) {  // Hanya tambahkan jika bukan -999
                total[j] += A[i][j];
            }
        }
    }

    // Cari term dengan kemunculan terbanyak (nilai max dalam array total)
    let modTerm = 0;
    let sumModTerm = total[0];
    for(let j = 1; j < mkolom; j++) {
        if(total[j] > sumModTerm) {
            sumModTerm = total[j];
            modTerm = j
        }
    }

    // Output hasil
    console.log('modTerm =', modTerm+1);  // 2
    console.log('sumModTerm =', sumModTerm);  // 20
}

ModusTerm(A);