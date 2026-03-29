#!/usr/bin/node

// length istifadə etmək qadağan olduğu üçün birbaşa 2-ci indeksi yoxlayırıq
const firstArg = process.argv[2];

if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
