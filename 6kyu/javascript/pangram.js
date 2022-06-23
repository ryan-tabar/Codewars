// 6kyu: Detect Pangram
// A pangram is a sentence contains every single letter of the alhabet at least once.
// For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
// because it uses the letters A-Z at least once (case if irrelevant).

// Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
// Ignore numbers and punctuation.

function isPangram(string){
    return [...new Set(string.toLocaleLowerCase().match(/[a-z]/g))].length === 26;
  }