
public class DLQueue<T> implements QueueADT<T> {

	private int count;
	private DoubleNode<T> front, rear;

	public DLQueue () {
		count = 0;
		front = rear = null;
	}

	public void enqueue(T element) {
		// Complete this method.
		if (isEmpty()) {
			front = new DoubleNode(element);
			rear = front;
		}
		else {
			DoubleNode<T> newNode = new DoubleNode (element);
			newNode.setPrev(rear);
			rear.setNext(newNode);
			rear = newNode;
			//rear.setNext(null);
		}
		count++;
	}

	public T dequeue() throws EmptyCollectionException {

		if(this.isEmpty()) {
			throw new EmptyCollectionException(this.toString());
		}

		else if (count == 1){
			front = null;
			count--;
			T returnElement = rear.getElement();
			rear = null;
			return returnElement;
		}
		else {
			T returnElement = front.getElement();
			
			front = front.getNext();
			front.setPrev(null);
			count--;
			return returnElement;
		}
	}

	public T first() throws EmptyCollectionException {
		return front.getElement();
	}

	public boolean isEmpty() {
		return (count == 0);
	}

	public int size() {
		return count;
	}

	public String toString() {

		
		if (this.isEmpty()) {
			return "The queue is empty.";
		}
		else {
			DoubleNode<T> curr = this.getFront();
			String s = "Queue: ";
			
			while (curr.getNext() != null) {
				s += curr.getElement() + ", ";
				curr = curr.getNext();
			}
			s += rear.getElement() + ".";
			System.out.println("222");

			return s;
		}
	}

	public DoubleNode<T> getFront () {
		return front;
	}

	public DoubleNode<T> getRear () {
		return rear;
	}

}
