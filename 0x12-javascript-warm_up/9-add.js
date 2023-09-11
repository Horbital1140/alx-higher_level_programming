#!/usr/bin/node
function add (a, b) {
  const num = a + b;
  console.log(num);
}
add(Number(process.argv[2]), Number(process.argv[3]));
