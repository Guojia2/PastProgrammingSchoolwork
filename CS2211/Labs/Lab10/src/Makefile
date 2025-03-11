# Targets for compiling the object files and linking them together

program: database.o person.o linked_list.o interact.o
	clang -o program database.o person.o linked_list.o interact.o

# Compile database.o
database.o: database.c person.h linked_list.h interact.h
	clang -c database.c

# Compile person.o
person.o: person.c person.h
	clang -c person.c

# Compile linked_list.o
linked_list.o: linked_list.c linked_list.h
	clang -c linked_list.c

# Compile interact.o
interact.o: interact.c interact.h
	clang -c interact.c

# Clean the object files and executable
clean:
	rm -f *.o program
