// 4kyu: Most frequently used words in a text
// Write a function that, given a string of text (possibly with punctuation and line-breaks),
// returns an array of the top-3 most occuring words, in descending order of the number of occurrences.

// Assumptions:
// A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
// Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
// Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
// Matches should be case-insensitive, and the words in the result should be lowercased.
// Ties may be broken arbitrarily.
// If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.

function topThreeWords(text) {
  const words = text.toLowerCase().match(/\b[a-z']+\b/g);

  return [...new Set(words)]
    .map((word) => [word, words.filter((w) => w === word).length])
    .sort((a, b) => b[1] - a[1])
    .slice(0, 3)
    .map((w) => w[0]);
}
