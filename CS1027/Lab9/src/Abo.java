
public class Abo {

	
	public static int rabo (int n) {
		if (n == 0) {
			return n;
		}
		else if (n == 1) {
			return n;
		}
		else if (n > 1) {
			if (n % 2 == 0) {
				n = 1 + rabo(n / 2);
			}
			else if (n % 2 != 0) {
				n = 2 + rabo((n + 1) / 2);
			}
		}
		return n;
		
	}
	
	public static int iabo (int n) {
		System.out.println(n);
		
		return 999999999;
	}
	
	public static void main (String[]args) {
		for (int i = 0; i < 20; i++) {
			System.out.println(rabo(i));
		}
	}
	
	
}
