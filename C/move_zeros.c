/*
 *Given an integer array nums, move all 0's to the end of it while maintaining the relative    
 * order of the non-zero elements.
 *
 *Note that you must do this in-place without making a copy of the array.
 *
 *Constraints:
 *
 *1 <= nums.length <= 104
 *-231 <= nums[i] <= 231 - 1
 */

void move_zeroes(int* nums, int nums_size)
{
    int index_to_insert_non_zero, i;
    
    index_to_insert_non_zero = 0;
    for(i = 0; i< nums_size; i++)
    {
        /*
        If non_zero element is found, place it in start of the list, but after all previous
        moved non-zero elements
        */
        if (nums[i] != 0)
            nums[index_to_insert_non_zero++] = nums[i];
    }
    
    /*
    Set every element after last non-zero element to 0 
    */
    for(i = index_to_insert_non_zero; i < nums_size; i++)
        nums[i] = 0;
}

