/*
 * Write a function that reverses a string. The input string is given as an array of characters s.
 *     
 * Constraints:
 * 
 * 1 <= s.length <= 105
 * s[i] is a printable ascii character.
 *  
 * 
 * Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
 */

void swap(char *elem1, char *elem2);

void reverse_string(char* s, int s_size){
    
    int low, high;
    
    low = 0;
    high = s_size - 1;
    
    while(low < high)
        /*
        Swap places of every element from both outer edges towards the center of the array
        */
        swap(&s[low++], &s[high--]);
    
}

void swap(char *elem1, char *elem2)
{
    char tmp;
    tmp = *elem1;
    *elem1 = *elem2;
    *elem2 = tmp;
}
