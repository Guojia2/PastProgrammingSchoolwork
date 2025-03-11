
public class BillSplitter {

	public static UniqueOrderedList<Integer> split (UniqueOrderedList<Integer> in, int target){
		return yourSplit(in.iterator(),target);

	}
	private static UniqueOrderedList<Integer> yourSplit (CopyableIterator<Integer> it, int target){
		UniqueOrderedList<Integer> soln;
		if (!it.hasNext()) {  // if the list is empty AND the target is 0, then the empty list is a valid solution and we return  it.
			if (target == 0) {
				UniqueOrderedList<Integer> emptyList = new UniqueOrderedList<Integer>();
				return emptyList ;
			}
			else { // if the list is empty and the target is not zero, then there is no solution and we return null
				return null;
			}	
		}
		else { //if list is not empty, then there are more items remaining
			Integer curr = it.next();  
			if (curr <= target) { // solution is still possible so long as there are more items and target is positive
				soln = yourSplit(it.copy(), target - curr); //since the solution is still possible, we call the recursive method again with a separate iterator. we assign curr to our tab.
				if (soln != null) { // if soln at the end of all the recursive calls is NOT null, then we know it is a valid final solution and we return it with curr added
					soln.add(curr);
					return soln;
				}
			}
			soln = yourSplit(it.copy(), target);  // if there are items remaining and condition curr <= target is not met, then we do not assign curr to our tab. 
			return soln;
		}
	}
}


