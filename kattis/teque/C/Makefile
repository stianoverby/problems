CC=gcc
FLAGS=-std=gnu11 -Wall -Wextra
CFILES=teque.c
EXE=teque
.PHONY: clean

all: $(EXE)

teque: teque.o
	${CC} ${FLAGS} teque.o -o teque
%.o:%.c
	$(CC) -c $(FLAGS) $< -o $@
clean:
	rm -f *.o $(EXE)
