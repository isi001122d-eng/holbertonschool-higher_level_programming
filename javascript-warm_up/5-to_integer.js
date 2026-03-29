#!/usr/bin/node

// İlk arqumenti götürürük və tam ədədə çevirməyə çalışırıq
const num = parseInt(process.argv[2]);

// Əgər çevirmə nəticəsi NaN-dırsa (rəqəm deyilsə)
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
