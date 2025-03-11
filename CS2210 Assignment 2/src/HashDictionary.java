import java.util.LinkedList;
public class HashDictionary implements DictionaryADT{

	private LinkedList<Data>[] hashTable;
	private int size;

	public HashDictionary(int capacity) {
		this.size = capacity;
		this.hashTable = new LinkedList[capacity];
		for (int i = 0; i < capacity; i++) {
			hashTable[i] = new LinkedList<Data>();
		}
	}


	private int hash(String key, int tableSize) {
		// lowest collisions: 
		// 687 with base 11
		// 1074 with base 811
		int base = 811; 
		int hashCode = 0;  

		// use polynomial hash code to generate a hashcode
		for (int i = 0; i < key.length(); i++) {
			char c = key.charAt(i); 

			// Convert the char into integer
			int charInt = c;

			// Calculate (base^exponent) modulo tableSize
			int power = 1;
			for (int j = 0; j < i; j++) {
				power = (power * base) % tableSize;
			}

			// Update hashCode
			hashCode += (charInt * power) % tableSize;
			hashCode %= tableSize; // Ensure hashCode is within range
		}

		return hashCode;
	}



	/*Adds record to the dictionary. 
	 * This method must throw a DictionaryException if record.getConfiguration() is already in the dictionary.
	 */
	public int put(Data record) throws DictionaryException{

		int hashCode = hash(record.getConfiguration(), this.size); //calculates hashcode to determine which index in hashTable needs to be accessed

		LinkedList<Data> separateChain = hashTable[hashCode]; // initialize this variable for readability

		if (separateChain.isEmpty()) {
			separateChain.add(record);
			return 0;
		}
		for (int i = 0; i < separateChain.size();i++) {  //checking each element in separateChain to see if any match record
			if (separateChain.get(i).getConfiguration().equals(record.getConfiguration())){ 
				throw new DictionaryException();  // throws exception if it's already in the dictionary
			}
		}
		separateChain.add(record);
		return 1;
	}


	// removes a record from the dictionary based on its configuration
	public void remove(String config) throws DictionaryException{
		int hashCode = hash(config, size); // calculates the hashcode
		LinkedList<Data> separateChain = hashTable[hashCode]; // initialize these variables for readability
		Data record;
		if (separateChain.isEmpty()) { // throws exception if the array index is empty
			throw new DictionaryException();
		}
		for (int i = 0; i < separateChain.size();i++) {  //iterating through the linked list separateChain until we get the desired record
			record = separateChain.get(i);
			if (separateChain.get(i).getConfiguration().equals(config)){ 
				separateChain.remove(i);  //removes the record if found
				return;
			}
		}
		throw new DictionaryException(); // if desired record not found, throw DictionaryException to indicate not found
	}


	
	//  Returns the score (of type int) stored in the record (of type Data) in the dictionary with key config, or -1 if config is not in the dictionary.
	public int get(String config) {
		int hashCode = hash(config, size); 	// calculate the hashcode to find the index of the array hashTable we need to access
		LinkedList<Data> separateChain = hashTable[hashCode]; // initializing separateChain and record for readability.
		Data record;

		if (separateChain.isEmpty()) { //returns a failure if separateChain is empty
			return -1;
		}
		for (int i = 0; i < separateChain.size();i++) {  //iterating through the linked list separateChain until we get the desired record
			record = separateChain.get(i);
			if (separateChain.get(i).getConfiguration().equals(config) ){ 
				//System.out.println("found");
				return record.getScore();  //returns the score of the desired record if found
			}
		}
		return -1; // if desired record not found, return -1 to indicate not found
	}

	
	
	

	public int numRecords() {	

		int totalRecords = 0; // initialize a counter

		for( int i = 0; i < this.size; i++){ //iterates through the entire hashTable
			totalRecords = totalRecords + hashTable[i].size();  //counts the number of elements in the linked list stored in each array index of hashTable and adds it to the total
		}
		return totalRecords; //returns the total
	}
}
