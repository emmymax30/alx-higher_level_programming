#!/usr/bin/node

let i;

for (i = 2; process.argv[i] != null; i++) {
  i++;
}
if (i === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
