/* source : https://open.kattis.com/problems/teque */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

#define CAPACITY 500001

typedef struct deque
{
    int buffer[CAPACITY];
    int size;
    int front;
    int back;
    
} Deque;
int dq_add_front(Deque *dq, int n);
int dq_add_back(Deque *dq, int n);
int dq_get(Deque *dq, int index);
void init_deque(Deque *dq);

typedef struct teque
{
    Deque *front;
    Deque *back;
} Teque;
void push_front(Teque *tq, int n);
void push_back(Teque *tq, int n);
void push_middle(Teque *tq, int n);
int get(Teque *tq, int index);
void init_teque(Teque *tq, Deque *front, Deque *back);
void balance(Teque *tq);

int main(void)
{
    char buffer[1024] = {0};
    int i;  
    Deque front, back;
    Teque tq;
    init_deque(&front);
    init_deque(&back);
    init_teque(&tq, &front, &back);

    scanf("%d", &i);
    while (scanf("%255s%d", buffer, &i) == 2) {
        if(strcmp(buffer, "push_back") == 0){push_back(&tq, i);}
        else if(strcmp(buffer, "push_front") == 0){push_front(&tq,i);}
        else if(strcmp(buffer, "push_middle") == 0){push_middle(&tq, i);}
        else {printf("%d\n", get(&tq, i));}
    }
    return EXIT_SUCCESS;
}

int dq_add_front(Deque *dq, int n)
{
    if(dq->size == CAPACITY){return EXIT_FAILURE;}
    dq->front = (dq->front - 1 + CAPACITY) % CAPACITY;
    dq->buffer[dq->front] = n;
    dq->size ++;
    return EXIT_SUCCESS;
}

int dq_add_back(Deque *dq, int n)
{
    if(dq->size == CAPACITY){return EXIT_FAILURE;}
    dq->buffer[dq->back] = n;
    dq->back = (dq->back + 1)  % CAPACITY;
    dq->size++;
    return EXIT_SUCCESS;
}

int dq_remove_front(Deque *dq)
{
    if(dq->size == 0){return -1;}
    int item = dq->buffer[dq->front];
    dq->front = (dq->front + 1) % CAPACITY;
    dq->size--;
    return item;
}

int dq_remove_back(Deque *dq)
{
    if(dq->size == 0){return -1;}
    dq->back = (dq->back - 1 + CAPACITY) % CAPACITY;
    int item = dq->buffer[dq->back];
    dq->size--;
    return item;
}

int dq_get(Deque *dq, int index)
{
    if(index < 0 || index >= dq->size){return -1;}
    return dq->buffer[(dq->front + index) % CAPACITY];
}

void push_front(Teque *tq, int n)
{
    switch (dq_add_front(tq->front, n))
    {
        case EXIT_FAILURE: {printf("<Warning>: push front failed\n");}
    }
    balance(tq);
}

void push_back(Teque *tq, int n)
{
    switch (dq_add_back(tq->back, n))
    {
        case EXIT_FAILURE: {printf("<Warning>: push back failed\n");}
    }
    balance(tq);
}

void push_middle(Teque *tq, int n)
{
    switch (dq_add_back(tq->front, n))
    {
        case EXIT_FAILURE: {printf("<Warning>: push middle failed\n");}
    }
    balance(tq);
}

void balance(Teque *tq)
{
    while(tq->front->size > tq->back->size + 1)
    {
        dq_add_front(tq->back, (dq_remove_back(tq->front)));
    }

    while(tq->back->size > tq->front->size)
    {
        dq_add_back(tq->front, (dq_remove_front(tq->back)));
    }
}

int get(Teque *tq, int index)
{
    if(index < tq->front->size){return dq_get(tq->front, index);}
    return dq_get(tq->back, index - tq->front->size);

}

void init_deque(Deque *dq)
{
    dq->size = 0;
    dq->front = 0;
    dq->back = 0;
}

void init_teque(Teque *tq, Deque *front, Deque *back)
{
    tq->front = front;
    tq->back = back;
}
