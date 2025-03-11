
public class Polynomial {

	private OrderedLinkedList <Monomial> polyOLL; 

	public Polynomial() {
		polyOLL = new OrderedLinkedList <Monomial>();
	}

	public void add(int coefficient, int degree) {
		// calls the constructor for Monomial and constructs a new Monomial,
		// then inserts the new monomial into the ordered linked list
		Monomial newMonomial = new Monomial(coefficient, degree);
		this.polyOLL.insert(newMonomial);
	}



	public  Polynomial derivative() { 
			// initializing new Polynomial object which will be the derivative
		Polynomial derivativePolynomial = new Polynomial();

		
		int index = 0;
		for (index = 0; index < polyOLL.getSize(); index++) {
			
			// the if statement ensures that constants will not be included in the derivative
			if (polyOLL.get(index).getDegree() > 0) {
				
				// takes the derivative of each Monomial individually and adds it to derivativePolynomial
				Monomial curr = new Monomial(polyOLL.get(index).getDegree() * polyOLL.get(index).getCoefficient(), polyOLL.get(index).getDegree() - 1);
		
				derivativePolynomial.add(curr.getCoefficient(), curr.getDegree());
		
			}
		}

		return derivativePolynomial;
	}
	
	public double eval(double z) {
		double total = 0;
		double evaluatedMonomial;

		// iterates through the OLL instance variable of the Polynomial 
		int index = 0;
		for (index = 0; index < polyOLL.getSize(); index++) {
			// performs the multiplication operation and adds the result  to the total
			evaluatedMonomial = polyOLL.get(index).getCoefficient() * Math.pow(z, polyOLL.get(index).getDegree());
			
			total = total + evaluatedMonomial;
		}
		return total;
	}

	// defining helper method absolute() to get absolute values of double and ints
	// I thought Math.abs required importing when i wrote this, but now it's too late to change my code to use Math.abs
	
	private int absolute(int input) {
		// defines a helper method to get absolute values of integers
		if (input < 0) {
			input = input * -1;
		}
		return input;
	}
	private double absolute(double input) {
		if (input < 0) {
			input = input * -1;
		}
		return input;
	}

	public String toString() {
		
		int index = 0;
	
		String representation = "";

		// returns empty string if there are no terms
		if (polyOLL.getSize() == 0) {
			return representation;
		}

		for (index = 0; index < polyOLL.getSize(); index++) {
			//iterates through the OLL and checks the coefficients of the monomials because negative and positive terms must be handled differently
			//the first term in the polynomial also must be given a special case

			if (polyOLL.get(index).getCoefficient() >= 0 && index == 0) {
				// creates a special case for the first term in the polynomial so we don't print + at the front of the Polynomial
				representation = polyOLL.get(index).getCoefficient() + "*" + "x" + "^" + polyOLL.get(index).getDegree();
			}
			else if ((polyOLL.get(index).getCoefficient() >= 0 && index > 0)){
				representation = representation + " + " + polyOLL.get(index).getCoefficient() + "*" + "x" + "^" + polyOLL.get(index).getDegree();

			}
			else if ((polyOLL.get(index).getCoefficient() < 0) && index > 0) {
				representation = representation + " - " + absolute(polyOLL.get(index).getCoefficient()) + "*" + "x" + "^" + polyOLL.get(index).getDegree();
			}
		}
		return representation;
	}

	// 	creating a helper function to perform Newton's method in the solve() method
	private double newtonFormula(double xi) {
		// xi is the previous
		double xj;
		xj = xi - (eval(xi) / this.derivative().eval(xi));
		return xj;
	}


	public double solve  (double x0, double e, int T) throws SolutionNotFound{
		//	 the solve() method is defined exactly as the assignment files specify.
		int iterations = 0;
		double previous = x0;
		double current = 0;

		
		if (derivative().eval(previous)!= 0) {
			current = newtonFormula(previous);
		}
		else{
			throw new  SolutionNotFound("divide by zero error");
		}
		while ((iterations <= T) && absolute(previous - current) > e) {
			previous = current;
			if (derivative().eval(previous) != 0) {
				current = newtonFormula(previous);
			}
			else {
				throw new SolutionNotFound("divide by zero error");	
			}
			iterations++;
		}
		if (iterations >= T) {
			throw new SolutionNotFound("maximum iteration exceeded");
		}
		else {
			return current;
		}
	}
}

