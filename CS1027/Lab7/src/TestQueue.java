
public class TestQueue {

	public static void main(String[] args) {
		
		//LinkedQueue<String> Q = new LinkedQueue<String>();
		DLQueue<String> Q = new DLQueue<String>();
		
		if (Q.isEmpty()) {
			System.out.println("Test 1 passed - isEmpty()");
		} else {
			System.out.println("Test 1 failed - isEmpty()");
		}
		
		Q.enqueue("one");
		Q.enqueue("two");
		Q.enqueue("three");
		Q.enqueue("four");
		Q.enqueue("five");
		Q.enqueue("six");
		Q.enqueue("seven");
		Q.enqueue("eight");
		Q.enqueue("nine");

		if (Q.size() == 9) {
			System.out.println("Test 2 passed - size()");
		} else {
			System.out.println("Test 2 failed - size()");
		}
		
		
		String firstElem = Q.first();
		if (firstElem.equals("one")) {
			System.out.println("Test 3 passed - first()");
		} else {
			System.out.println("Test 3 failed - first()");
		}

		// Dequeue several elements.
		for (int i = 0; i < 5; i++) {
			Q.dequeue();
		}
		
		firstElem = Q.first();
		if (firstElem.equals("six")) {
			System.out.println("Test 4 passed - first()");
		} else {
			System.out.println("Test 4 failed - first()");
		}
		
		
		// Check that the queue is connected properly in both directions.
		
		DoubleNode<String> currF = Q.getFront(), currB = Q.getRear();
		String sf = "", sb = "";
		while (currF != null) {
			sf += currF.getElement() + " ";
			currF = currF.getNext();
		}
		while (currB != null) {
			sb += currB.getElement() + " ";
			currB = currB.getPrev();
		}
		System.out.println("\t\t"+sf);
		System.out.println("\t\t"+sb);
		
		if (sf.equals("six seven eight nine ") && sb.equals("nine eight seven six ")) {
			System.out.println("Test 5 passed - prev connections");
		} else {
			System.out.println("Test 5 failed - prev connections");
		}

		
		String toStr = Q.toString();
		System.out.println("\t\t"+Q);

		if (toStr.equals("Queue: six, seven, eight, nine.")) {
			System.out.println("Test 6 passed - toString()");
		} else {
			System.out.println("Test 6 failed - toString()");
		}
		

		// Dequeue the remaining elements.
		for (int i = 0; i < 4; i++) {
			Q.dequeue();
		}
		
		toStr = Q.toString();
		System.out.println("\t\t"+Q);
		
		if (toStr.equals("The queue is empty.")) {
			System.out.println("Test 7 passed - toString()");
		} else {
			System.out.println("Test 7 failed - toString()");
		}
		
		
		
	}

}
