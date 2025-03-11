
public class ArrayStack<T> implements StackADT<T>{
	private T[] array; 
	private int top;



	public ArrayStack() {
		this.array = (T[]) new Object[10];
		top = -1;
	}

	public void push(T element) {
		
		this.expandCapacity(); // starts by expanding capacity if necessary
		
		this.array[top + 1] = element; // adds the element at the index right after top
		top++; // increments top

	}
	
	public T pop()	throws StackException{
		if (isEmpty()) { // starts by checking for empty array
			throw new StackException("Stack is empty");
		}

		else { 
			shrinkCapacity(); // shrinks capacity if needed

			T poppedItem = this.array[top]; // holder variable so the value of top can be accessed and returned later
			this.array[top] = null; //  deletes the item at the top of the stack
			top = top - 1;	// reassigns top

			return poppedItem; // returns the item that was deleted
		}
	}

	public T peek () throws StackException{
		if (isEmpty()) { // starts by checking for empty array
			throw new StackException("Stack is empty");
		}
		else {
			return this.array[top];
		}
	}

	public boolean isEmpty () {
		if (top == -1) {
			return true;
		}
		else {
			return false;
		}
	}
	
	public int size (){
		return top + 1;
	}
	
	public void clear() { // reassigns the variable this.array with an emptty array 
		this.array = (T[]) new Object[10];
		top = -1;
	}
	
	public int getCapacity(){
		return this.array.length;
	}
	
	public int getTop() {
		return top;
	}
	
	public String toString(){
		
		if (isEmpty()) { // starts by checking for the case of an empty stack
			return  "Empty stack.";
		}
		else {
			String returnString = new String("Stack: ");
			int index;
			for (index = top; index > 0; index--) { // iterate through array and adds each element to returnString, except the last one
				returnString += this.array[index] + ", " ;
			}
			returnString += this.array[0] + ".";  // adds the last element of the array
			
			return returnString; // returns returnString	
		}
	}
	
	private void expandCapacity() {
		double fractionUsed = (double) (getTop() + 1) / getCapacity(); // calculates how much of the array is used
		int expandedCapacity = getCapacity() + 10; // calculates the increased capacity

		if (fractionUsed < 0.75) { // if the array is not close to being full, do nothing
			return;
		}
		else  if (fractionUsed >= 0.75){ //create a new larger array and copy all the elements of this.array into it. Then, set this.array to be the newly generated array.
			T[] newArray = (T[]) new Object[expandedCapacity];

			int i;
			for (i = 0; i <= getTop(); i++) {
				newArray[i] = array[i];
			}
			this.array = newArray ;
		}
	}

	private void shrinkCapacity(){ // follows the same idea as expandCapacity()
		//
		double fractionUsed = (double) (getTop() + 1) / getCapacity() ; // calculates how much of the array is used
		int shrunkCapacity= getCapacity()  - 10;

		if (fractionUsed > 0.25 || getCapacity()  < 20) { //
			return;
		}
		else if (fractionUsed <= 0.25 && getCapacity()  >= 20) {

			T[] newArray = (T[]) new Object[shrunkCapacity];
			int i;
			for (i = 0; i <= getTop(); i++) {
				newArray[i] = array[i];
			}
			this.array = newArray;
		}
	}	
















}
