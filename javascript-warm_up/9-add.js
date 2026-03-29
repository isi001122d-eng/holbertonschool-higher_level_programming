#!/usr/bin/node

// Funksiya təyin edirik (prototype: function add(a, b))
function add (a, b) {
  return a + b;
}

// Arqumentləri tam ədədə çeviririk
const firstInt = parseInt(process.argv[2]);
const secondInt = parseInt(process.argv[3]);

// Nəticəni çap edirik
console.log(add(firstInt, secondInt));
