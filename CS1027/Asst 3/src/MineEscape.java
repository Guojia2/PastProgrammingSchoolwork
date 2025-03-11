import java.io.FileNotFoundException;
import java.io.IOException;

public class MineEscape {

	private Map map;
	private int numGold;
	private int[] numKeys; //   index 0 is red keys, then 1 ise green keys, and 2 is blue keys

	public MineEscape (String filename) {


		try { // change to catch just Exception e
			this.map = new Map(filename);
		} 
		catch (Exception e) {
			e.printStackTrace();
		}
		this.numGold = 0;
		this.numKeys = new int[3];
	}


	private MapCell findNextCell(MapCell cell) {
		int index;
		MapCell nextCell = null;

		// creates sequential for loops that check for each type of cell in order of priority 
		//(i.e first checks if any neighbours are exit cells, then checks for collectible cells, and so on)

		for (index = 0; index <= 3; index++) { // checks neighbours for exit cells
			if(cell.getNeighbour(index) != null) { // checks that the cell is valid before trying to access information about it. The other blocks follow a similar format.

				if (cell.getNeighbour(index).isExit()) { 
					nextCell = cell.getNeighbour(index);
					return nextCell;
				}
			}
		}
		for (index = 0; index <= 3; index++) { // checks all neighbours for key/gold cells

			if(cell.getNeighbour(index) != null) { 
				if(cell.getNeighbour(index).isKeyCell()||cell.getNeighbour(index).isGoldCell()) {
					nextCell = cell.getNeighbour(index);
					return nextCell;	
				}
			}
		}
		for (index = 0; index <= 3; index++) { // checks for normal floor cells that have not already been traversed
			if(cell.getNeighbour(index) != null) {
				if (cell.getNeighbour(index).isFloor() && !cell.getNeighbour(index).isMarked())  {
					nextCell = cell.getNeighbour(index);
					return nextCell;
				}
			}
		}
		for (index = 0; index <= 3; index++) { // checks for lock cells for which we already have a key.
			if(cell.getNeighbour(index) != null) {
				if (cell.getNeighbour(index).isLockCell()) {

					if(cell.getNeighbour(index).isRed() && numKeys[0] > 0) {
						nextCell = cell.getNeighbour(index);
						return nextCell;
					}

					else if(cell.getNeighbour(index).isGreen() && numKeys[1] > 0) {
						nextCell = cell.getNeighbour(index);
						return nextCell;
					}
					else if(cell.getNeighbour(index).isBlue() && numKeys[2] > 0) {
						nextCell = cell.getNeighbour(index);
						return nextCell;
					}
				}
			}
		}	
		return nextCell;
	}	

	public String findEscapePath() {

		ArrayStack<MapCell> S = new ArrayStack<MapCell>();
		S.push(map.getStart());
		// the pathfinding algorithm is implemented according to assignment instructions

		map.getStart().markInStack();

		MapCell curr;

		boolean running = true;
		String path = "Path: " + map.getStart() ;

		while (!S.isEmpty() && running == true) {
			curr = S.peek();
			//checks if any neighbours are lava cells. If so, number of gold pieces is set to 0
			int i = 0;
			for(i = 0; i < 4; i++) {
				if(curr.getNeighbour(i) != null && curr.getNeighbour(i).isLava()) { 
					numGold = 0;
				}
			}
			// stops the pathfinding algorithm if an exit has been found
			if (curr.isExit()) {
				running = false;
				break;
			}
			// checks for key cells and updates the list of keys accordingly
			if (curr.isKeyCell()) {
				if(curr.isRed()) {
					numKeys[0] += 1;
				}
				else if (curr.isGreen()) {
					numKeys[1] += 1;

				}
				else if (curr.isBlue()) {
					numKeys[2] += 1;
				}
				curr.changeToFloor(); // changes the tile to a normal floor cell once key has been claimed
			}

			if (curr.isGoldCell()) {
				numGold += 1;	
				curr.changeToFloor();
			}

			MapCell next = findNextCell(curr);
			if (next == null) {
				curr = S.pop();
				curr.markOutStack();
			}
			else {
				path = path + " " + next.toString();
				S.push(next);
				next.markInStack();
				if (next.isLockCell()) {
					if (next.isRed()){
						next.changeToFloor();
						numKeys[0]--;

					}
					else if (next.isGreen()){
						next.changeToFloor();
						numKeys[1]--;

					}
					else if (next.isBlue()){
						next.changeToFloor();
						numKeys[2]--;
					}
				}
			}
		}
		// once we are done finding an escape path, we return a string desribing the escape path
		if (!running) {
			path = path + " " + numGold + "G";
			return path ;
		}
		else {
			return "No solution found";
		}
	}



	public static void main(String[] args) {
		if (args.length != 1) {
			System.out.print("Map file not given in the arguments.");
		} 
		else {
			MineEscape search = new MineEscape(args[0]); 
			String result = search.findEscapePath(); 
			System.out.println(result);
		}
	}
}

















