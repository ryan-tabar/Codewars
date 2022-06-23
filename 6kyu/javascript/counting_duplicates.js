// 6kyu: Counting Duplicates
// Write a function that will return the count of distinct case-insensitive alphabetic characters
// and numeric digits that occur more than once in the input string. The input string can be
// assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

const duplicateCount = (text) => {
  const arr = text.toLowerCase().split("");

  let currentArray = [...arr];
  let count = 0;
  while (currentArray.length > 1) {
    const lengthBefore = currentArray.length;
    // remove letters that are equal to first letter
    currentArray = currentArray.filter((l) => currentArray[0] !== l);
    // if new length is less than 1, count as duplicate
    count += currentArray.length < lengthBefore - 1 ? 1 : 0;
  }
  return count;
};
