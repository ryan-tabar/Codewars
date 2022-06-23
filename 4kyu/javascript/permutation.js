// 4kyu: Permutations
// In this kata you have to create all permutations
// of non empty input string and remove duplications, 
// if present. This means, you have to suffle all
// letters from the input in all possible orders.

// Examples:
// * With input 'a'
// * Your function should return: ['a']
// * With input 'ab'
// * Your function should return ['ab', 'ba']
// * With input 'aabb'
// * Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

function permutations(string) {
    if (string.length > 1) {
      const results = [];
  
      string.split("").forEach((char, index) => {
        permutations(
          string.substring(0, index) + string.substring(index + 1)
        ).forEach((perm) => results.push(char + perm));
      });
      return [...new Set(results)];
    } else {
      return [string];
    }
  }