
public class Configurations {

	private char[][] board;
	private int k;

	public Configurations (int boardSize, int lengthToWin, int maxLevels) {
		board = new char[boardSize][boardSize];
		for (int i = 0; i < boardSize; i++) {
			for (int j = 0; j < boardSize; j++) {
				board[i][j] = ' ';
			}
		}
		  k = lengthToWin;

		
	}
	
	

	public HashDictionary createDictionary() {
		HashDictionary hashDict = new HashDictionary(8233);
		return hashDict;
	}

	/*
	 * This method first stores the characters of the board in a String; 
	 * then it checks whether the String representing the board is in the hashTable:
	 *  	If the String is in the hashTable, this method returns its associated score, 
	 *  	otherwise it returns the value -1.
	 */
	public int repeatedConfiguration(HashDictionary hashTable) {

		String boardString = "";  //initialize the string to store the board characters

		for (char[] row : board) {  //iterate through the 2d array and concatenate the characters to the string
			for (char c : row) {
				boardString += c;
			} 
		}
		return hashTable.get(boardString); // returns the associated score if boardString is in hashTable, and -1 if it isnt
	}



	/*
	 * This method first represents the content of the board as a String as described above; 
	 * then it inserts this String and score in the hashDictionary
	 */
	public void addConfiguration(HashDictionary hashDictionary, int score) {

		String boardString = "";  //initialize the string to store the board characters
		for (char[] row : board) {  //iterate through the 2d array and concatenate the characters to the string
			for (char c : row) {
				boardString += c;
			} 
		}
		Data record = new Data(boardString, score);  // builds a new Data object to hold boardString and score
		hashDictionary.put(record); //puts the record to the hash dictionary
	}


	/*
	 * Stores a symbol in the board[row][col]
	 */
	public void savePlay(int row, int col, char symbol) {
		board[row][col] = symbol;
	}

	/*
	 *  Returns true if board[row][col] is ’ ’;otherwise it returns false. 
	 */
	public boolean squareIsEmpty (int row, int col) {
		return board[row][col] == ' ';
		

	}



	/*
	 * Returns true if there is a continuous sequence of length at least k formed by tiles of the 
	 * kind symbol on the board, where k is the length of the vertical 
	 * or horizontal of diagonal line needed to win the game.
	 */
	public boolean wins (char symbol) {

		int row;   // remember: board [row][col] 
		int col; 	// row refers to a horiztonal 1d array in the 2d array, and col refers to the index in that 1d array
		 
		
	
		//check for horizontal combo of length k
		for (row = 0; row < board.length; row++) {
			int horizontalCombo = 0; //resets the combo counter to 0 with each new row.
			for (col = 0; col < board[row].length; col++) {
				if (board[row][col] == symbol) {
					
					horizontalCombo++;
				}
			}
			if (horizontalCombo >= k) { //returns true if a combo of length k has been found. Otherwise, keep going.
				return true;
			}
		}
		
		
		//check for vertical combo of length k
		row = 0;
		col = 0;

		for (col = 0; col < board.length; col++) {
//			System.out.println(row);
//			System.out.println(col);
			
			int verticalCombo = 0;
			for (row = 0; row < board.length; row++) {
				if (board[row][col] == symbol) {
					verticalCombo++;
				}
				
			}
			if (verticalCombo >= k) {
				return true;
			}
		}
		

		
		// Check for diagonal combo (downward)
		for (int startRow = 0; startRow < board.length; startRow++) {
		    int diagonalDownCombo = 0;
		     row = startRow;
		     col = 0;
		    while (row < board.length && col < board[row].length) {
		        if (board[row][col] == symbol) {
		            diagonalDownCombo++;
		        } else {
		            diagonalDownCombo = 0;
		        }
		        if (diagonalDownCombo >= k) {
		            return true;
		        }
		        row++;
		        col++;
		    }
		}

		// Check for diagonal combo (upward)
		for (int startCol = 1; startCol < board[0].length; startCol++) {
		    int diagonalUpCombo = 0;
		     row = 0;
		     col = startCol;
		    while (row < board.length && col < board[row].length) {
		        if (board[row][col] == symbol) {
		            diagonalUpCombo++;
		        } else {
		            diagonalUpCombo = 0;
		        }
		        if (diagonalUpCombo >= k) {
		            return true;
		        }
		        row++;
		        col++;
		    }
		}
		return false;
	}


	/*
	 * Returns true if board has no empty positions left and no player has won the game.
	 */
	public boolean isDraw() {

		if (this.wins('O') || this.wins('X')) { // if there is a winner, return false
			return false;
		}
		for (char[] row : board) {  //iterate through the 2d array 
			for (char c : row) {
				
				if (c != 'O' && c !='X'){
					return false; // returns false as soon as an empty spot is found
				}
			} 
		}
		return true;
	}


	/*
	 * Returns one of the following values:
	 * 
	 * 3, if the computer has won, 
	 * 		i.e. there is a vertical or horizontal or diagonal line formedby tiles of type ’O’ on the board
	 * 
	 * 0, if the human player has won
	 * 
	 * 2, if the game is a draw,
	 * 		i.e. there are no empty positions in board and no player has won
	 * 
	 * 1, if the game is still undecided, 
	 * 		i.e. there are still empty positions in board and no player has won yet.
	 */
	public int evalBoard() {
		if (this.wins('O')) {
			return 3;
		}
		
		if (this.wins('X')) {
			return 0;
		}
		if (this.isDraw()) {
			return 2;
		}
			return 1;
	}
}