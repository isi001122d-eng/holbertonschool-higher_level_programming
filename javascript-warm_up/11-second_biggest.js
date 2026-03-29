#!/usr/bin/node

// Arqumentlərin sayını yoxlayırıq
if (process.argv.length <= 3) {
  console.log(0);
} else {
  // İlk iki elementi (node və fayl adı) kəsib atırıq, qalanları rəqəmə çeviririk
  const args = process.argv.slice(2).map(Number);
  
  // Massivi böyükdən kiçiyə sıralayırıq
  // Set istifadə edirik ki, təkrar rəqəmlər siyahıdan çıxsın
  const uniqueSorted = [...new Set(args)].sort((a, b) => b - a);
  
  // İkinci elementi çap edirik (əgər varsa)
  if (uniqueSorted.length < 2) {
    console.log(0);
  } else {
    console.log(uniqueSorted[1]);
  }
}
