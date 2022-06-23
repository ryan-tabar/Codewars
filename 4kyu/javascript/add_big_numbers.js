// 4kyu: Adding Big Numbers
// A function that returns the sum of two numbers
// The input numbers are string and thefunction must return a string

// The numbers are big
// The input is a string of only digits
// The numbers are positives

function add(...numbers) {
    const longest = numbers.reduce((f, g) => (g.length > f.length ? g : f), "");
    let shortest = numbers.find((num) => num !== longest);
    if (numbers.every(num => numbers[0] === num)) {
      shortest = longest;
    }
    shortest = new Array(longest.length - shortest.length).fill("0").join("") + shortest;
  
    let carry = 0;
    let sum = "";
    for (let i = longest.length - 1; i >= 0; i--) {
      const addedDigits = parseInt(longest[i]) + parseInt(shortest[i]) + carry;
      sum += (addedDigits % 10).toString();
      carry = Math.floor(addedDigits / 10);
    }
    if (carry > 0) {
      sum += carry.toString()
    }
  
    return sum.split("").reverse().join("");
  }