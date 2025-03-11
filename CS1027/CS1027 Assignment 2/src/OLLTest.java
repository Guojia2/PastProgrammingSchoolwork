
public class OLLTest {

	public static void main (String[] args) { 

		myCustomTest();
		System.out.println( "OLL Test 01 " + (test01() ? "passed" : "failed" ));
		System.out.println( "OLL Test 02 " + (test02() ? "passed" : "failed" ));
		System.out.println( "OLL Test 03 " + (test03() ? "passed" : "failed" ));
		System.out.println( "OLL Test 04 " + (test04() ? "passed" : "failed" ));
		System.out.println( "OLL Test 05 " + (test05() ? "passed" : "failed" ));

	}


	public static boolean test01() { 
		OrderedLinkedList<Integer> oll = new OrderedLinkedList<>();

		if (oll.getSize() != 0) {
			return false;
		}

		try {
			oll.get(0);
			return false;
		} catch (IndexOutOfBoundsException e) {
			return true;
		}

	}

	public static boolean test02() { 
		OrderedLinkedList<Integer> oll = new OrderedLinkedList<>();
		int x = (int) (Math.random()*100);
		oll.insert(x);

		return (oll.getSize() == 1) && (oll.get(0) == x);
	}

	public static boolean test03() { 
		OrderedLinkedList<Integer> oll = new OrderedLinkedList<>();
		oll.insert(5);

		try {
			oll.get(1);
			return false;
		} catch (IndexOutOfBoundsException e) {
			return true;
		}

	}

	public static boolean test04() { 
		OrderedLinkedList<Integer> oll = new OrderedLinkedList<>();
		// test 4 seems to fail based on whether x > y
		
		
		int x = (int) (Math.random()*100);
		int y = (int) (Math.random()*100);
		int[] all = new int[] {x,y};
		oll.insert(x);
		oll.insert(y);
		
		//		System.out.println("x is " + x);
		//		System.out.println("y is " + y);

		//System.out.println("size  is " + oll.getSize());
		if (oll.getSize()!= 2) {
			return false; 
		} 
		else {

			int first = oll.get(0);
			//System.out.println("oll.get(0) is " + oll.get(0));

			int second = oll.get(1);

			return (first >= second) && (first == all[0] || first == all[1]) && (second == all[0] || second == all[1]);
		}

	}

	public static void  myCustomTest(){ 

		System.out.println("Custom test follows");
		OrderedLinkedList<Integer> oll = new OrderedLinkedList<>();
//		for (int i = 0; i < 6; i++) { 
//			oll.insert(i);	
//
//			//System.out.println("i is " + i);
//			//System.out.println(oll.getSize());
//		}
//		
//		oll.insert(99);
//		oll.insert(98);
//		oll.insert(97);
		oll.insert(8);
		oll.insert(6);
		oll.insert(9);
		oll.insert(3);
		oll.insert(2);
		oll.insert(1);
		//oll.insert(0);
		System.out.println(oll.getSize());
		for (int i = 0; i < oll.getSize(); i++) { 


			System.out.println("oll.get(i) is " + oll.get(i));
		}
	}
	
	public static boolean test05() { 

		OrderedLinkedList<Integer> oll = new OrderedLinkedList<>();

		for (int i = 99; i >=0; i--) { 
			oll.insert(i);	
			
			//System.out.println(i);
			//System.out.println("Size of oll is:");
			//System.out.println(oll.getSize());
			//System.out.println("We got to this point")
			

			
			// at index position 0, 1 , 2, ...99
			// this loop inserts monomials of degree 99, 98, 97, ... 0
		}
		boolean result = true;
		for (int i = 0; i< 100; i++) { 
			// at i = 0, oll.get(i) should return 99 because it is the highest variable
			// at i = 99, oll.get(i) should return 0

			//			System.out.println("i is " + i);
			//			System.out.println("oll.get(i) is " + oll.get(i));
			//			System.out.print("100 - oll.get(i) is meant to be equal to " + i + " but it is ");
			//			System.out.println( 100 - oll.get(i)-1);
			//			
			//System.out.println("size is"  + oll.getSize());

			result = result && (i == 100-oll.get(i)-1);

		}

		return result;


	}

}
