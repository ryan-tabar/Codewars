// 7kyu: Complementary DNA

// In DNA strings, symbols "A" and "T" are complements of each other,
// as "C" and "G". Your function receives one side of the DNA (string,
// except for Haskell); you need to return the other complementary side.
// DNA strand is never empty or there is no DNA at all (again, except
// for Haskall).

#include <iostream>
#include <string>

std::string DNAStrand(const std::string& dna) {
  const std::string s = "ATCGTAGC";
  
  std::string result;
  
  for (const char& c : dna) 
    result.push_back(s[s.find(c) + 4]);
  
  return result;
}


int main() {
    std::cout << DNAStrand("ATTGC") << std::endl; // expect "TTACG"
    std::cout << DNAStrand("GTAT") << std::endl; // expect "CATA"

    return 0;
}