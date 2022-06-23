// 4kyu: Catching Car Mileage Numbers
// Let's make it so Bob never misses another interesting number.
// We've hacked into his car's computer, and we have a box hooked up
// that reads mileage numbers. We've got a box glued to his dash
// that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively)

// It's up to you, intrepid warrior, to glue the parts together. Write the function
// that parses the mileage number input, and returns a 2 if the number is "interesting" (see below),
// a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.

// "Interesting" Numbers:
// - Any digit followed by all zeros: 100, 90000
// - Every digit is the same number: 1111
// - The digits are sequential, incementing: 1234
// (0 should come after 9, and not before 1, as in 7890)
// - The digits are sequential, decrementing: 4321
// (0 should come after 1, and not before 9, as in 3210)
// - The digits are a palindrome: 1221 or 73837
// - The digits match one of the values in the awesomePhrases array

function isInteresting(number, awesomePhrases, checkNextTwoMiles = true) {
    if (number > 99) {
      for (const phrase of awesomePhrases) {
        if (number == phrase) return 2;
      }
      const string = number.toString();
      if (
        /^(\d)(\1+|0+)$/.test(string) ||
        "1234567890 9876543210".indexOf(string) != -1 ||
        string === string.split("").reverse().join("")
      )
        return 2;
      else if (checkNextTwoMiles) {
        if (
          isInteresting(number + 1, awesomePhrases, false) ||
          isInteresting(number + 2, awesomePhrases, false)
        )
          return 1;
      }
    } else if (number == 98 || number == 99) return 1;
    return 0;
  }