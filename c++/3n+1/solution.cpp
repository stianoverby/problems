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
