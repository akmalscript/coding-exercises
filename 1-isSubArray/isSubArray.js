/*
Day 1 - 14 Februari 2025

isSubArray: mengecek apakah array B merupakan bagian dari array A.

> Testcase (1)
ArrA = [X, Y, A, B, C]
ArrB = [A, B, C]
Output: True
> Testcase (2)
ArrA = [H, I, J, K, L]
ArrB = [A, B, C]
Output: False
> Testcase (3)
ArrA = [C, X, Y, A, B]
ArrB = [A, B, C]
Output: False
> Testcase (4)
ArrA = [X, Y, A, B, C]
ArrB = [C, B, A]
Output: False

*/

// Solusi
const Test1 = ['X', 'Y', 'A', 'B', 'C']
const Test2 = ['H', 'I', 'J', 'K', 'L']
const Test3 = ['C', 'X', 'Y', 'A', 'B']
const Arr1 = ['A', 'B', 'C']
const Arr2 = ['C', 'B', 'A']

function isSubArray(ArrA, ArrB) {
    const n = ArrA.length;  // panjang ArrayA
    const m = ArrB.length;  // panjang ArrayB
    let count = 0;  // penghitung kecocokan

    // i adalah (semua kemungkinan) index awal ArrayB dalam ArrayA
    for(let i = 0; i < n-m+1; i++) {  // i dari 0 hingga n-m (loop sebanyak n - m + 1 kali)
        count = 0;  // Reset count untuk setiap posisi i
        // Loop j untuk mengecek semua elemen ArrayB
        for(let j = 0; j < m; j++) {  // j dari 0 hingga m-1 (loop sebanyak m kali)
            if(ArrA[i+j] === ArrB[j]) {
                count++;
            }
            else {
                break;  // Jika tidak cocok, lanjut ke i berikutnya
            }
        }
        // Jika count sama dengan panjang ArrayB, berarti cocok
        if(count === m) {
            return true;
        }
    }
    // Jika tidak cocok, return False
    return false;
}

console.log('Test Case 1:', isSubArray(Test1, Arr1));  // true
console.log('Test Case 2:', isSubArray(Test2, Arr1));  // false
console.log('Test Case 3:', isSubArray(Test3, Arr1));  // false
console.log('Test Case 4:', isSubArray(Test1, Arr2));  // false