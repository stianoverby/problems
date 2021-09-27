
/**
 * Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
 * find two numbers such that they add up to a specific target number. Let these two numbers be 
 * numbers[index1] and numbers[index2] where 1 <= first < second <= numbers.length.
 * 
 * Return the indices of the two numbers, index1 and index2, as an integer array [index1, index2] of length 2.
 * 
 * The tests are generated such that there is exactly one solution. You may not use the same element twice.
 *
 * Constraints
 *  2 <= numbers.length <= 3 * 104
 * -1000 <= numbers[i] <= 1000
 * numbers is sorted in non-decreasing order.
 * -1000 <= target <= 1000
 * The tests are generated such that there is exactly one solution.
 *
 * Note: The returned array must be malloced, assume caller calls free().
 */

#define RETURN_SIZE 2

int* two_sum(int* numbers, int numbers_size, int target, int* return_size){
    
    int low, high, sum;
    
    *return_size = 0; 
    
    low = 0;
    high = numbers_size-1;
    
    int *addends = malloc(sizeof(int) * RETURN_SIZE);
    
    while(low < high)
    {
        sum = numbers[low] + numbers[high];
      
        /*
        If the sum of the element at the high and low pointer is equal to the target, return the indexes.
        */
        if (sum == target)
        {
            addends[0] = low + 1;
            addends[1] = high + 1;
            *return_size = RETURN_SIZE;
            return addends;
        }
        
        /*
        If the sum is less than the target, then we have to increase the low pointer to increase the sum.
        */
        else if(sum < target)
            low++;
        
        /*
        If the sum is more than the target, then we have to decrease the low pointer to decrease the sum.
        */
        else if(sum > target)
            high--;
    }
    
    
    return addends;
}
