/* The 3n + 1 problem (Colatz conjecture)

Consider the following algorithm to generate a sequence of numbers. Start with an
integer n. If n is even, divide by 2. If n is odd, multiply by 3 and add 1. Repeat this
process with the new value of n, terminating when n = 1. 

For example, the following sequence of numbers will be generated for n = 22:
22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

It is conjectured (but not yet proven) that this algorithm will terminate at n = 1 for
every integer n. Still, the conjecture holds for all integers up to at least 1, 000, 000.
For an input n, the cycle-length of n is the number of numbers generated up to and
including the 1.

In the example above, the cycle length of 22 is 16. Given any two numbers i and j,
you are to determine the maximum cycle length over all numbers between i and j,
including both endpoints.

Input
The input will consist of a series of pairs of integers i and j, one pair of integers per
line. All integers will be less than 1,000,000 and greater than 0.

Output
For each pair of input integers i and j, output i, j in the same order in which they
appeared in the input and then the maximum cycle length for integers between and
including i and j. These three numbers should be separated by one space, with all three
numbers on one line and with one line of output for each line of input.

*/

#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int cycle_length(int n);
int max(vector<int> v);

int main()
{
	int a, b;

	/* Read two integers*/ 
	while (cin >> a >> b)
	{
		/* Fill vector with all possible cycle lengths */
        vector<int> numbers;	
		for(int i = a; i < b; i++)
			numbers.push_back(cycle_length(i));

		/* Output the length of the longest cycle */
		cout << a << " " << b << " " << max(numbers) << endl;	
	}
}

int cycle_length(int n)
{
	int counter;

	/* The minimal length of a cycle is one; when n is 1 */
	counter = 1;
	while(n	!= 1)
	{
		/* n is even; divide by 2 */
		if (n % 2 == 0)
			n = n / 2;

		/* n is odd; multiply by 3, and add 1 */
		else
			n = n * 3 + 1;	

		/* Moved to next number, increase cycle length */
		counter++;
	}
	return counter;
}

int max(vector<int> v)
{
	/* Default value; should always be smaller */
	int val = INT_MIN;	

	/* Iterate over complete vector */
	for(int i = 0; i < v.size(); i++)
	{
		/* If current value is larger than current max, update max to the current value */
		if (v[i] > val)
			val = v[i];
	}
	return val;
}	
