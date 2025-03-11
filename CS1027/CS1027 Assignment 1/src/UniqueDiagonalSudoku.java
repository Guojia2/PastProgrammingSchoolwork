
public class UniqueDiagonalSudoku extends Sudoku{
	
	public UniqueDiagonalSudoku (int[][] numbers){
		super(numbers); 
		
		// HOW DO I CALL A SUPER METHOD I FORGOT 
			
	}

	public boolean isValidSolution () {
		// start by checking if the regular sudoku rules have been met
		 if (!super.isValidSolution()) {
	            return false;
	        }

		// creating boolean arrays to check whether a digit has already been seen in the diagonals.
		 // each diagonal is given its own independent pool of numbers that must only be seen once
		 // also making a boolean variable to store whether or not a diagonal is true
		boolean diagonal1Validity = true;
		boolean diagonal2Validity = true;
		boolean[] diagonal1 = new boolean[this.getSize() + 1];
		boolean [] diagonal2 = new boolean[this.getSize() + 1];
		int i;
		int diagonal1Digit;
		int diagonal2Digit;
		
		for  (i = 0; i < this.getSize(); i++) {
			diagonal1Digit = this.getGrid()[i][i];// this iterates through the top-left to bottom-right diagonal. e.g [1][1] then [2][2]
			diagonal2Digit = this.getGrid()[this.getSize() -1 -i][i]; // this iterates through the bottom-left to top-right diagonal
	
			if (diagonal1[diagonal1Digit]) {
				diagonal1Validity = false;
			}
			else {
				diagonal1[diagonal1Digit] = true;
			}
			
			if (diagonal2[diagonal2Digit]){ 
				diagonal2Validity = false;
				// for each digit, checks either of them have been seen. If they have, set the diagonal to invalid
		}
			else {
				diagonal2[diagonal2Digit] = true;
			}
	// set the diagonals to be true, now that we have checked them

		}
		// if at least one of the diagonals is valid and the regular sudoku rules have been followed, return true. 
    if ((diagonal1Validity || diagonal2Validity) && (super.isValidSolution())) {
    	return true;	
    }

return false;
	}	
	
}