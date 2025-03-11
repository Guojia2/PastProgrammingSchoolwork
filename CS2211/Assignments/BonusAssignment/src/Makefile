# Targets for compiling the object files and linking them together


# Compiler and flags
CC = clang
CFLAGS = -g -Wall -O0 # Add -g for debugging information, -Wall for all warnings     
gcal: reminder.o main.o linked_list.o interact.o
	clang -o gcal main.o reminder.o linked_list.o interact.o

# Compile main.o
main.o: main.c reminder.h linked_list.h interact.h
	clang -c main.c

# Compile reminder.o
reminder.o: reminder.c reminder.h
	clang -c reminder.c

# Compile linked_list.o
linked_list.o: linked_list.c linked_list.h
	clang -c linked_list.c

# Compile interact.o
interact.o: interact.c interact.h
	clang -c interact.c

# Clean the object files and executable
clean:
	rm -f *.o gcal