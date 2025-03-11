
public class TreeAlgorithms {

	public static int min (BinaryTreeNode<Integer> node) {
		if (node == null){
			return 239482;
		}
		int value = node.getData();
		int leftMin = min(node.getLeft());
		int rightMin = min(node.getRight());
		
		if (value < leftMin && value < rightMin) {
			return value;
		}
		if (leftMin < value && leftMin < rightMin) {
			return leftMin;
		}
		if (rightMin < value && rightMin < leftMin) {
			return rightMin;
		}
		return 95845;

	}

	public static int countLeafs (BinaryTreeNode<Integer> node) {
		if (node == null) {
			return 0;
		}
		int counter = 0;
		if (node.getLeft() == null && node.getRight() == null) {
			counter++;
		}
		
		if(node.getLeft() != null) {
		counter += countLeafs(node.getLeft());
		}
		if (node.getRight() != null) {
			counter += countLeafs(node.getRight());
			
		}
		return counter;
	}




	public static void main(String[] args) {
		LinkedBinaryTree<Integer> tree = buildTree();
		System.out.println(tree);

		// Testing min
		if (min(tree.getRoot()) == 1 && min(tree.getRoot().getLeft()) == 1 && min(tree.getRoot().getRight()) == 7) {
			System.out.println("Min value test passed");
		} else {
			System.out.println("Min value test failed");
		}


		// Testing count leafs
		if (countLeafs(tree.getRoot()) == 5 && countLeafs(tree.getRoot().getLeft()) == 3 && countLeafs(tree.getRoot().getRight()) == 2) {
			System.out.println("Count leafs test passed");
		} else {
			System.out.println("Count leafs test failed");
		}

	}



	private static LinkedBinaryTree<Integer> buildTree () {

		LinkedBinaryTree<Integer> leftTree;
		LinkedBinaryTree<Integer> rightTree;

		// construct the left subtree of the binary tree

		LinkedBinaryTree<Integer> t1 = new LinkedBinaryTree<Integer>(1);
		LinkedBinaryTree<Integer> t2 = new LinkedBinaryTree<Integer>(3);
		LinkedBinaryTree<Integer> t3 = new LinkedBinaryTree<Integer>(2,t1,t2);
		t1 = new LinkedBinaryTree<Integer>(5);
		leftTree = new LinkedBinaryTree<Integer>(4,t3,t1);

		// construct the right subtree of the binary tree

		t1 = new LinkedBinaryTree<Integer>(9);
		t2 = new LinkedBinaryTree<Integer>(10,t1,null);
		t3 = new LinkedBinaryTree<Integer>(7);
		rightTree = new LinkedBinaryTree<Integer>(8,t3,t2);

		return new LinkedBinaryTree<Integer>(6, leftTree, rightTree);
	}

}
