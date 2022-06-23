// 6kyu: Build a pile of Cubes
// Your task is to contruct a building which will be a pile of n cubes. The cube
// at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3
// and so on until the top which will have a volume of 1^3.

// You are given the total volume of m of the building. Being given m can you find the number
// n of cubes you will have to build?

// The parameter of the function find (find_nb, find-nb, findNb, ...) will be an integer m
// and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such
// a exists or -1 if there is no such n

function findNb(m) {
  const result = 0.5 * (Math.sqrt(8 * Math.sqrt(m) + 1) - 1);
  return result % 1 ? -1 : result;
}
