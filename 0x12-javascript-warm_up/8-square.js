#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  let u = 0;
  while (u < x) {
    console.log('x'.repeat(x));
    u++;
  }
}
