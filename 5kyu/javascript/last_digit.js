// 5Kyu: Last digit of a large number
// Define a function that takes in two non-negative integers
// a and b and returns the last decimal digit of a^b.
// Note that a and b may be very large!

const lastDigit = (str1, str2) => {
  const patterns = [
    [0],
    [1],
    [2, 4, 8, 6],
    [3, 9, 7, 1],
    [4, 6],
    [5],
    [6],
    [7, 8, 3, 1],
    [8, 4, 2, 6],
    [9, 1],
  ];

  // anything to the power of 0 is 1 including 0
  if (str2.split("").every((d) => d === "0")) {
    return 1;
  } else {
    const pattern = patterns[Number(str1.slice(-1))];
    const length = pattern.length;
    return pattern[(BigInt(str2) - BigInt(1)) % BigInt(length)];
  }
};
