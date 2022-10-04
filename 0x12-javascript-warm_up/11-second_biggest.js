#!/usr/bin/node

function max (array) {
  let MaxInt = 0;
  for (const i of array) {
    if (i > MaxInt) {
      MaxInt = i;
    }
  }
  return (MaxInt);
}

const myarray = [];
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    myarray.push(Number(process.argv[i]));
  }
}
const MaxInt = max(myarray);
for (let i = 0; myarray[i] != null; i++) {
  if (myarray[i] === MaxInt) {
    delete myarray[i];
    break;
  }
}
const MaxInt2 = max(myarray);
console.log(MaxInt2);
