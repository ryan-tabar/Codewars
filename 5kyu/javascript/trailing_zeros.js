// 5kyu Number of trailing zeros of N!
// Write a program that will calculate the number of 
// trailing zeros in a factorial of a given number.
// Be careful 1000! has 2568 digits...

// For more info, see: http://mathworld.wolfram.com/Factorial.html

const getBaseLog = (x, y) => Math.log(y)/Math.log(x)

function zeros (n) {
  const kMax = Math.floor(getBaseLog(5, n))
  let sum = 0
  for (let i = 1; i <= kMax; i++) 
    sum += Math.floor(n/(5**i))
  return sum
}