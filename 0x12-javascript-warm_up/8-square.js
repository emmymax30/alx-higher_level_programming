#!/usr/bin/node

const number = Number(process.argv[2]);
let value = '';
if (!number) {
  console.log('Missing size');
} else if (number) {
  for (let i = 0; i < number; i++) {
    value += 'X';
  }
  for (let i = 0; i < number; i++) {
    console.log(value);
  }
}
