/*
 *  Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
 *    
 *  Constraints:
 *
 *  1 <= s.length <= 5 * 104
 *  s contains printable ASCII characters.
 *  s does not contain any leading or trailing spaces.
 *  There is at least one word in s.
 *  All the words in s are separated by a single space.
 *
 */

void swap(char *elem1, char *elem2);
void reverse_string(char* s, int s_size);
int is_symbol(char* character);
int is_end_of_word(char* character);
    
char * reverse_words(char * s)
{
    
    char *traversing_ptr, *start_of_word;
    bool word_started;
    int size_word;
    
    traversing_ptr = s; 
    word_started = 0;
    size_word = 0;
    
    /*
    We now that the string can never be empty, so we do not have to check if it is. 
    */
    do 
    {
        /*
        If valid symbol in word, start word and start counting the size of it. 
        */
        if (is_symbol(traversing_ptr))
        {
           if (!word_started)
           {
               size_word = 0;
               word_started = 1;
               start_of_word = traversing_ptr;
           }
            
           size_word++;
        }    
        
        /*
        If we have found a space or null-byte, we have found the end of a word, And we reverse it. 
        */
        else if (is_end_of_word(traversing_ptr))
        {
               if (word_started)
               {
                   word_started = 0;
                   reverseString(start_of_word, size_word);
               }
        }
         
         
     } while(*traversing_ptr++);
    
    return s;
}

int is_symbol(char* character)
{
   if (*character != ' ' && *character != '\0') 
       return 1;
   return 0;
}

int is_end_of_word(char* character)
{
    if (*character == ' ' || *character == '\0')
        return 1;
    return 0;
}


void reverse_string(char* s, int s_size)
{
    
    int low, high;
    
    low = 0;
    high = s_size - 1;
    
    while(low < high)
        swap(&s[low++], &s[high--]);
    
}

void swap(char *elem1, char *elem2)
{
    char tmp;
    tmp = *elem1;
    *elem1 = *elem2;
    *elem2 = tmp;
}
