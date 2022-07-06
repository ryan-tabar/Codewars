#include <iostream>

// 7kyu: Count the divisors of a number


int divisors(int n) {
	int totalDivisors = 0;
	for (int i = 1; i <= n; i++) {
		if (!(n % i)) {
			totalDivisors++;
		}
	}
	return totalDivisors;
}

int main() {

	std::cout << divisors(30) << std::endl;

	return 0;
}