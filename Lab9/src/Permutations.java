import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Permutations {
	
	public static void permutations(String prefix, String suffix) {
		// ADD CODE IN HERE.
		if (suffix.length() == 0) {
			System.out.println(prefix);
		}
		else {
			char c;
			int i;
			String suff;
			String pre = prefix;
			for (i = 0; i < suffix.length(); i++) {
				
				c = suffix.charAt(i);
				suff = removeChar(suffix, i);
				pre = prefix + c;
				permutations(pre, suff);

			}
		}

	}

	
	private static String removeChar(String s, int i) {
	    return s.substring(0, i) + s.substring(i+1, s.length());
	}
	
	public static void main (String[] args) throws Exception {
		BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in), 1);
        System.out.print("Enter a word (or enter nothing to exit): ");
        String text = keyboard.readLine();
        
        while (text.length() > 0) {
        	permutations("", text);
        	
        	System.out.print("Enter a word (or enter nothing to exit): ");
            text = keyboard.readLine();
        }
        
	}

	
}
