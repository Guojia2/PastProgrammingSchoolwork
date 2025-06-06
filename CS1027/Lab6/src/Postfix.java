import java.util.Scanner;

public class Postfix {

	private ArrayStack<String> expStack;
	private PostfixEvaluator evaluator;
	
	public Postfix () {
		// ADD CODE HERE.
		this.expStack = new ArrayStack<String>();
		this.evaluator = new PostfixEvaluator();
		
	}

	public void run () {
		String expression, action = "e";
		int result;

		try {
			Scanner in = new Scanner(System.in);
      
			do {
				if (action.equals("e")) {
					System.out.print("Enter a valid postfix expression:  ");
					expression = in.nextLine();
	
					result = evaluator.evaluate(expression.trim());
					System.out.println("The result is " + result);
	
					// ADD CODE HERE.
					this.expStack.push(expression);
				
				} else if (action.equals("r")) {
					if (this.expStack.size() >= 3) {
						showRecent(3);
					}
					else if (this.expStack.size() < 3) {
						showRecent(this.expStack.size());
					}
					// ADD CODE HERE.



				}

				System.out.println("\nWhat do you want to do?");
				System.out.println("\tType 'e' if you want to evaluate another postfix expression.");
				System.out.println("\tType 'r' if you want to see the recent expressions.");
				System.out.println("\tType any other key to quit.");
				action = in.nextLine();
				System.out.println();
			} while (action.equalsIgnoreCase("e") || action.equalsIgnoreCase("r"));
    	} catch (Exception IOException) {
    		System.out.println("Input exception reported");
    	}

	}
	
	private void showRecent (int numToShow) {

		ArrayStack<String> tmp = new ArrayStack<String>();

		System.out.println("Recent Expressions:");
		for (int i = 0; i < numToShow; i++) {
			tmp.push(this.expStack.peek());
			System.out.println(this.expStack.pop());
			
		}
			
		for (int i = 0; i < numToShow; i++) {
			this.expStack.push(tmp.pop());
		}
		this.expStack.peek();
		
		
		
		
		
		
		
	
	}
	
	
	public static void main (String[] args) {
		Postfix pf = new Postfix();
		pf.run();
	}
}
