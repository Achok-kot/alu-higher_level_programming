#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(arg => parseInt(arg)).sort((a, b) => b - a);
  console.log(numbers[1]);
}
