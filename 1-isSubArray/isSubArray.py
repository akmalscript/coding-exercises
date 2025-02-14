"""
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

"""

# Solusi
Test1 = ['X', 'Y', 'A', 'B', 'C']
Test2 = ['H', 'I', 'J', 'K', 'L']
Test3 = ['C', 'X', 'Y', 'A', 'B']
Arr1 = ['A', 'B', 'C']
Arr2 = ['C', 'B', 'A']


def isSubArray(ArrA, ArrB):
    n = len(ArrA)  # panjang ArrayA
    m = len(ArrB)  # panjang ArrayB
    count = 0  # penghitung kecocokan

    # i adalah (semua kemungkinan) index awal ArrayB dalam ArrayA
    for i in range(n-m+1):  # i dari 0 hingga n-m (loop sebanyak n - m + 1 kali)
        count = 0  # Reset count untuk setiap posisi i
        # Loop j untuk mengecek semua elemen ArrayB
        for j in range(m):  # j dari 0 hingga m-1 (loop sebanyak m kali)
            if ArrA[i+j] == ArrB[j]:
                count += 1
            else:
                break  # Jika tidak cocok, lanjut ke i berikutnya
         # Jika count sama dengan panjang ArrayB, berarti cocok
        if count == m:
            return True
    # Jika tidak cocok, return False
    return False

print('Test Case 1:', isSubArray(Test1, Arr1))  # true
print('Test Case 2:', isSubArray(Test2, Arr1))  # false
print('Test Case 3:', isSubArray(Test3, Arr1))  # false
print('Test Case 4:', isSubArray(Test1, Arr2))  # false