#!/usr/bin/node

// Arqumentlərin sayını yoxlayırıq
if (process.argv.length <= 3) {
  console.log(0);
} else {
  
  const args = process.argv.slice(2).map(Number);
  
  // Massivi böyükdən kiçiyə sıralayırıq
  
  const uniqueSorted = [...new Set(args)].sort((a, b) => b - a);
  
  // İkinci elementi çap edirik (əgər varsa)
  if (uniqueSorted.length < 2) {
    console.log(0);
  } else {
    console.log(uniqueSorted[1]);
  }
}
