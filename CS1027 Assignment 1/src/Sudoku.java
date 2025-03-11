
public class Sudoku {
	private int size;
	private int[][] grid;
	
	
	
	public Sudoku (int[][] numbers) {
		size = numbers.length;
		grid = numbers;
			}

	public int getSize() {
		return size;
		
	}
	
	public int[][] getGrid (){
		return grid;	
	}
	
	
	public int getDigitAt (int row, int col) {
		if ((row < 0) ||row >= (this.getSize())| (col < 0) || col >= (this.getSize())) {
			return -1;
		}
		else {
			
		return this.getGrid()[row][col];
		}
	}
		
	public boolean isValidRow(int row) { 
				
		
		// First of all, check if the row being asked for is actually in the grid.
		if (row >= this.getSize()|| row < 0){
			return false;
		}
		
		// iterates through the row and checks if it has been seen before. 
		// if it has not been seen before, it marks it as seen
		// if it has been seen, then the sudoku is not valid and the function returns false.
		// it also checks each digit in the row to ensure that its value does not exceed the size of the sudoku grid
		// ex. 7 should not be present on a grid of size 5
		
		boolean [] numbersAlreadySeen = new boolean[this.getSize() + 1];
		int col;
		for (col = 0; col < this.getSize(); ++col) {
			if (numbersAlreadySeen[this.getGrid()[row][col]] || this.getGrid()[row][col] > this.getSize() || this.getGrid()[row][col] < 1) {
				return false;
			}
			numbersAlreadySeen[this.getGrid()[row][col]] = true;
		}
		
		/* if nothing is found that could disqualify this row, 
		 * then the method isValidRow(int row) will return true
		 */
		return true;
	}
	
	
	public boolean isValidCol (int col) {
		/*
		 * 
		 * Determine if the column at index col in the sudoku is valid, i.e. that it contains all the digits from 1 through size (inclusive) exactly once each. 
		 * Return true if it's valid, or false otherwise. 
		 * If the col index is out of range, return false.
		 * 
		 */	
		//	Checks for duplicates and checks that none of the digits in the column exceed the value of 'size'
		// I think it also ensures that list index is within range... I think.
		
	
		int row;
		boolean [] numbersAlreadySeen = new boolean [this.getSize() + 1];
		for (row = 0; row < this.getSize(); ++row) {
			if (numbersAlreadySeen[this.getGrid()[row][col]]|| (this.getGrid()[row][col]) > this.getSize()||(this.getGrid()[row][col] < 1) ){
			return false;
			}
			else {
				numbersAlreadySeen[this.getGrid()[row][col]] = true;
			}
		}
		return true;		
		
	}// this brace closes the function isValidCol()

	
	public boolean isValidBox (int row, int col) {
		/*	Determine if the 3x3 box whose top-left corner is at index row, col in the sudoku is valid, 
		 *  i.e. that it contains all the digits from 1 through 9 (inclusive) exactly once each. 
		 *  Return true if it's valid, or false otherwise. 
		 *  If the row or col indices are out of range, return false.  DONE
		 *   NOTE: this method will only be called for a 3x3 box in a 9-sized sudoku so it does not need to work for any other sized boxes
		 */

		// Checks if the row and column are within bounds
		 if (row < 0 || row > this.getSize() - 3 || col < 0 || col > this.getSize() - 3) {
			return false;
		}
		int i;
		int j;
		// creates a list of size 9 to indicate whether the digit has been seen.
		boolean [] numbersAlreadySeen  = new boolean [this.getSize()+1];
		// If we inspect a digit in the grid and see that it has already appeared, or if the digit is not from 1 to 9, return false.
		// If it has not been seen, set that digit's index in numbersAlreadySeen to true.
		for  (i = row; i < row + 3; i++) {
			for (j = col; j < col + 3; j++) {
				 int currentDigit = this.getGrid()[i][j];
				 if (numbersAlreadySeen[currentDigit] || currentDigit < 1 || currentDigit > 9||numbersAlreadySeen[currentDigit]) {
					 return false;
				 }
				 numbersAlreadySeen[currentDigit] = true;
				 }
			}
		
		// If nothing is found to invalidate this box, then the box is valid and we return true.
		return true;
				
	}// this brace closes the function isValidBox (int row, int col)
	
	public boolean isValidSolution () {
		
			int row;
			int col;
		if (this.getSize() != 9){
			
			for (row = 0 ; row < this.getSize(); ++row) {
				if   (!this.isValidRow(row)) {
					return false;
				}
				else {
					for (col = 0; col < this.getSize(); ++col) {
						if (!this.isValidCol(col)) {
							return false;	
						}
					}
				}
			}		
		}
		else if (this.getSize() == 9){
				
			for (int i : new int[]{0, 3, 6}) {
			    for (int j : new int[]{0, 3, 6}) {
			    	if (!this.isValidBox(i, j)) {
			    		return false;
			    	}
			    	
			    }
			}
				for (row = 0 ; row < this.getSize(); ++row) {
					if   (!this.isValidRow(row)) {
						return false;
					}
					else {
				for (col = 0; col < this.getSize(); ++col) {
					if (!this.isValidCol(col)) {
						return false;	
					}
				}

					}
				}
				}		
			
			
		return true;
		}
	
	public boolean equals (Sudoku other) {
		/*
		 *  Determine if the'this'sudoku is identical to the other Sudoku.
		 *  To be identical,the size of each must be equal 
		 *  and the digits in the grid of each must all me equal in the same positions. 
		 *  Return true if they are identical, or false otherwise.
		 */
		int row;
		int col;
		
		if (this.getSize() != other.getSize()) {
			return false;
		}
		// iterates through every row in the grid and every column in each row.
		// if the integer at index [row][col] is not equal, the loop will return false.
		// if every digit in the two grids are equal, the function will return true at the end.
		for (row = 0 ; row < this.getSize(); ++row) {  
			for (col = 0; col < this.getSize(); ++col) {
				if (this.getGrid()[row][col] != other.getGrid()[row][col]) {  
					return false;
				}
			}
		}
		return true;
	
	} // this brace closes the function equals(Sudoku other)
	
	public String toString () {
		/*
		 * Build and return a string containing all the digits in the grid with a single space after each digit 
		 * and a newline character (\n) at the end of each row 
		 * (after the space that follows the final digit in the row) 
		 * so that the printed string looks like a grid structure.
		 */
		
		int row;
		int col;
		String sudokuGridAsString = "";
		
		for (row = 0 ; row < this.getSize(); ++row) { 	
			sudokuGridAsString += "\n";
			for (col = 0; col < this.getSize(); ++col) {
				//System.out.println(sudokuGridAsString += this.getGrid()[row][col]);
				sudokuGridAsString += this.getGrid()[row][col] + " ";		
				
			}
		}
		return sudokuGridAsString;
	}
	
} // this brace closes the class Sudoku. 
