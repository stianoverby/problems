/* Merge Linked Lists

Write a function that takes in the head of two Singly Linked
Lists that are in sorted order, respectively.
The function should merge the lists in place and return the 
head of the merged list; the merged list should be in sorted
order.

Each LinkedList node has an integer value as well as a next
node pointing to the next node in the list or to None/null
if it's the tail of the list.

You can assume that the input linked lists will always have at
least one node; in other words, the head will never be NULL.

Source: algoexpert
*/


#include <vector>

using namespace std;

class LinkedList {
public:
  int value;
  LinkedList *next;

  LinkedList(int value) {
    this->value = value;
    next = nullptr;
  }
};

LinkedList *mergeLinkedLists(LinkedList *headOne, LinkedList *headTwo) {

  LinkedList *head, *previous;
  LinkedList *p1, *p2, *smallest;

  /* The input linked lists are never null; set the head to be the
     smallest value. This will be our return value */
  head = (headOne->value < headTwo->value) ? headOne : headTwo;

  /* No previous yet */
  previous = NULL;

  /* Initialize a ptr that will iterate over each linked list */
  p1 = headOne;
  p2 = headTwo;

  /* Compare the values as long as both ptrs still are pointing to a linked list */
  while(p1 && p2)
  {
    /* Set smallest to be the lesser value of p1 and p2; move the corresponding ptr */
    if (p1 -> value < p2 -> value)
    {
      smallest = p1;
      p1 = p1 -> next;
    }
    else
    {
      smallest = p2;
      p2 = p2 -> next;
    } 

    /* Set the previous's next to be the smallest, and update previous to be the smallest */
    if(previous) previous -> next = smallest;
    previous = smallest;
  }

  /* While condition failed, but one of the lists may still contain elements.
     Set the previous ptrs next to be the list still containing one ore more
     elements if that is the case */
  if(p1)
    previous->next = p1;
  
  if(p2)
    previous->next = p2;
    
  
  return head;
}
