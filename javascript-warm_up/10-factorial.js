#!/usr/bin/node

// Rekursiv funksiya təyin edirik
function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

// Arqumenti tam ədədə çeviririk
const input = parseInt(process.argv[2]);

// Nəticəni çap edirik
console.log(factorial(input));
