import java.util.NoSuchElementException; // imports the exception, as instructed in the assignment instructions
public class UOLIterator<T> implements CopyableIterator<T>{
 
	
	LinearNode<T> curr; // curr is the node that the iterator is currently on
	
	public UOLIterator(LinearNode<T> start) {
		curr = start; // the starting node can be set to any node on a list. The iterator will start from that point.
	}
	public boolean hasNext() { // checks if there is another item that can be returned
		if (curr == null) {
			return false;
		}
		return true;
	}
	
	public T next() throws NoSuchElementException{ // returns curr's data  and move the iterator one spot further on the list
		if (hasNext()) {
			T returnData = curr.getData(); 
			curr = curr.getNext();
			return returnData; // returns next item in list
		}
		else {
			throw new NoSuchElementException("iterator empty");// throws exception if next() not possible
		}
	}
	
	public UOLIterator<T> copy(){ // creates a new iterator that starts from whatever position "this" iterator is at
		UOLIterator<T> copyIt =  new UOLIterator<T>(this.curr);
		return copyIt; 
	}
}
