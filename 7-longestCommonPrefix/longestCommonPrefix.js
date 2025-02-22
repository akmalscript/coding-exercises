// Day 7 - February 21, 2025
// 14. Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/

// Solution
function longestCommonPrefix(strs) {
    // Jika array kosong
    if (!strs.length) return "";

    // Mulai dengan asumsi prefix terpanjang adalah kata pertama
    let prefix = strs[0];

    // Bandingkan prefix ini dengan setiap kata dalam array
    for (let i = 1; i < strs.length; i++) {
        // Potong prefix hingga cocok dengan awal dari string saat ini
        while (strs[i].indexOf(prefix) !== 0) {
            prefix = prefix.slice(0, -1); // Hapus satu karakter dari belakang
            if (prefix === "") return "";
        }
    }

    return prefix;
}

// Contoh penggunaan:
const strs1 = ["flower", "flow", "flight"];
const strs2 = ["dog", "racecar", "car"];

console.log(longestCommonPrefix(strs1)); // Output: "fl"
console.log(longestCommonPrefix(strs2)); // Output: ""
