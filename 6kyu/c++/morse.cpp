// 6kyu Decode the Morse code

#include <iostream>
#include <unordered_map>
#include <regex>

std::string decodeMorse(std::string morseCode) {
	std::unordered_map<std::string, char> MORSE_CODE;
	MORSE_CODE["...."] = 'H';
	MORSE_CODE["."] = 'E';
	MORSE_CODE["-.--"] = 'Y';
	MORSE_CODE[".---"] = 'J';
	MORSE_CODE["..-"] = 'U';
	MORSE_CODE["-.."] = 'D';

	const std::regex mLetter(R"([^\s]+|\s+)");
	auto begin = std::sregex_iterator(morseCode.begin(), morseCode.end(), mLetter);
	auto end = std::sregex_iterator();

	std::string decoded;
	for (std::sregex_iterator i = begin; i != end; ++i) {
		decoded += i->str() == "   " ? ' ' : MORSE_CODE[i->str()];
	}

	return decoded;
}


int main() {
	std::string decoded = decodeMorse("  .... . -.--   .--- ..- -.. .   ");
	std::cout << decoded << std::endl;
}
