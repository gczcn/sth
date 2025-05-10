#include <stdio.h>
double sqrt(double);
double floor(double);
int main(void) {
	unsigned int N;
	scanf("%u", &N);
	printf("1");
	for (unsigned int i = 2; i * i <= N; i++) {
		printf(" %u", i * i);
	}
	return 0;
}
