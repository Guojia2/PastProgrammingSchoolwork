
public class Snail {

	public static char icon = '@';
	private int position ;
	private QueueADT<Integer> movePattern;




	public Snail (int[] pattern) {
		this.position = 0;
		int i;
		movePattern = new DLQueue<Integer>();
		for (i = 0; i < pattern.length; i++) {
			movePattern.enqueue(pattern[i]);
		}
	}

	public void move () {

		
			int movement = movePattern.dequeue();
			this.position += movement;

			movePattern.enqueue(movement);
			if (position > SnailRace.raceLength) {
				position = SnailRace.raceLength;
			}
		
	}

	public int getPosition () {
		return position;
	}

	public void display () {
		int dashesBefore = position;
		int dashesAfter = 50 - position ;
		int i;
		for (i = 0; i < dashesBefore; i++) {
			System.out.print("-");

		}

		System.out.print(icon);

		for (i = 0; i < dashesAfter; i++) {
			System.out.print("-");
		}
		System.out.println();
	}

}
