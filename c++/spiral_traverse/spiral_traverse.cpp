/* Spiral Traverse

Write a function that takes an n x m 2d-array,
and returns a array of all the array's elements
in spiral order.

Spiral order starts at the top left corner of the
2d-array, goes to the right, and proceed in a sprial
pattern all the way until every element has been
visited.

*/

using namespace std;

vector<int> spiralTraverse(vector<vector<int>> array)
{

    vector<int> spiral;
    int upper_border, left_border;
    int lower_border, right_border;

    upper_border = 0;
    left_border = 0;
    lower_border = array.size() - 1;
    right_border = array[0].size() - 1;

    while (upper_border <= lower_border && left_border <= right_border)
    {
        /* Retrive the upper border of the matrix */
        for (int i = left_border; i <= right_border; i++)
        {
            spiral.push_back(array[upper_border][i]);
        }

        /* Retrive the right border of the matric*/
        for (int i = upper_border + 1; i <= lower_border; i++)
        {
            spiral.push_back(array[i][right_border]);
        }

        /* Retrive the lower border of the matrix */
        for (int i = right_border - 1; i >= left_border; i--)
        {
            /* Edge case; matrix wider than tall */
            if (upper_border == lower_border)
                break;

            spiral.push_back(array[lower_border][i]);
        }

        /* Retrive the left border of the matrix */
        for (int i = lower_border - 1; i > upper_border; i--)
        {
            /* Edge case; matrix taller than wide*/
            if (left_border == right_border)
                break;

            spiral.push_back(array[i][left_border]);
        }

        /* Move the borders */
        upper_border++;
        right_border--;
        lower_border--;
        left_border++;
    }

    return spiral;
}
