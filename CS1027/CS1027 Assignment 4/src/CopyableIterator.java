
import java.util.Iterator; // imports Iterator as instructed in the assignment instructions

public interface CopyableIterator<T> extends Iterator<T> {
	public CopyableIterator<T> copy(); 
}
