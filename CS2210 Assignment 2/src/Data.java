
public class Data {
	
	private int score;
	private String configuration;
	
	public Data(String config, int score) {
		this.configuration = config;
		this.score = score;
	}
	
	public String getConfiguration() {
		return this.configuration;
	}
	
	public int getScore() {
		return this.score;
	}
}
