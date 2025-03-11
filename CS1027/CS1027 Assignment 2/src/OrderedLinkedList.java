
public class OrderedLinkedList <T extends Comparable<T>>{

	private  Node<T> head = new Node<T>(null, null);
	private int size = 0;


	public OrderedLinkedList() {

		this.size = 0;
	}

	public int getSize() {
		return this.size;
	}

	public void insert (T value) { 

		// starts by checking if list is empty. If so, the input value is automatically set as the head
		// and increase size by 1
		if (this.getSize() == 0 ) {
			this.head.setData(value);
			this.size += 1;

		}

		// If list is not empty, perform operations to insert the input value to its proper position
		else if (this.getSize() > 0) {
			int position = 0;
			Node<T> current = this.head;
			Node<T> prev = null;

			// walking down the list while comparing each monomial to the input monomial value
			if (current.getNext() == null) {
				// handles the case where current is the head and there are no other nodes
				if (value.compareTo(current.getData()) < 0 ) { // if value is less than current

					Node<T> newTerm = new Node<T>(value, null);
					current.setNext(newTerm);
					this.size++;

				}
				else {
					// creates a new node to hold the data of the head
					// then sets the head's data as value
					Node<T> newTerm = new Node<T>(current.getData(), null);
					current.setData(value);
					current.setNext(newTerm);
					this.size++;
				}

			}

			else {
				for ( position  = 0; position < this.getSize(); position++){

					if (value.compareTo(current.getData()) < 0 ) {
						prev = current;
						current = current.getNext();
						// if current has a higher degree than input value, then go to next  position	
						if (current == null) {
							current = new Node<T> (value, null);
							prev.setNext(current);
							this.size++;
							break;
						}
					}
					else {
						// once we find a monomial 'current' in the list of a lower degree than input 'value', 
						//insert the input right in front of 'current'.
						if (prev == null) { // handles the case where value is greater than head and head is not the only node
						
							Node<T> newTerm = new Node<T>(current.getData(), current.getNext());

							current.setData(value);
							current.setNext(newTerm);
							this.size++;
							break;
						}
						
						
						else { // if it's not an exceptional case, perform the standard process for inserting a new node
							Node<T> newTerm = new Node<T>(value, current); 
							prev.setNext(newTerm);
							this.size+= 1;
							break;
						}
					}
				}
			}
		}
	}

	public T get(int i) throws  IndexOutOfBoundsException {  

		// starts by checking that the index i being asked for is within bounds
		if (i >= this.getSize()|| i < 0) {
			throw new IndexOutOfBoundsException();
		}
		else if (i == 0) {
			return head.getData();
		}
		else {
			int index = 0;
			Node <T> curr = this.head; // walking down the linked list until we find the node at the position indicated by input i
			while (index < i) { 

				curr = curr.getNext();

				index += 1;		
			} 
			return curr.getData() ;	
		}
	}
}
