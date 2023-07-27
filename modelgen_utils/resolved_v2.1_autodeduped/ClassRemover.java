import java.io.*;
import java.nio.file.CopyOption;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

/**
 * Removes a python 'class' given:
 * ClassRemover FullPathURI nameOfClass
 * assming the class starts with
 * class "nameOfClass"
 *     and ends at the start of the next instance of the word 'class'
 *
 */
public class ClassRemover {
    public static final String cls="class";

    public static void main(String[] args) throws IOException {
	String filePath=args[0];
	String className=args[1];

	String backupFilePath = filePath+".orig";

	File outFile = new File(filePath);
	File backupFile = new File(backupFilePath+0);
	boolean madeBackup=false;
	int backupFileNumber=0;
	while(!madeBackup && backupFileNumber++ < 100){
	    try{
		backupFile=new File(backupFilePath+backupFileNumber);
		Files.copy(outFile.toPath(),backupFile.toPath()); //Make sure this move completes before we destroy outFile
		madeBackup=true;
	    }
	    catch(Exception e){
		//Good Old LCV through exception handler
	    }
	}
	BufferedReader lineStreamer = new BufferedReader(new FileReader(backupFile));

	BufferedWriter rewriter = new BufferedWriter(new FileWriter(outFile,false));//Blow out outFile (our argument). Risky but why not? We made a backup

	String line = lineStreamer.readLine();
	int classCount=0;
	int lineCount=0;
	boolean inClassToDestroy = false; //Mode 0 - output our input
	while(line!=null)
	    {
		if(line.contains(cls) && !line.contains("'")){
		    inClassToDestroy=false;
		    if(line.contains(className) /*and cls*/) {
			inClassToDestroy = true;
			classCount++;
		    }
		}
		
		if(!inClassToDestroy) {
		    rewriter.write(line);
		    rewriter.write(System.lineSeparator());//When reading lines, we're not getting the line separator
		}
		else{
		    if(false){
			System.out.println("-- :" + line);
		    }//fun debugging output
		    lineCount++;
		}
		//else throw out the line
		try {
		    line = lineStreamer.readLine(); // Null if null,
		}
		catch (Exception e) {
		    System.err.println(e);
		    line = null;
		    //Done, either we hit EoF or a read error or whatever.
		}
	    }
	System.out.println("Successfully removed all instances of class "+args[0]+" in file "+args[1] + "  " + classCount + " Class definitions over " + lineCount + " lines");
	rewriter.flush();
	rewriter.close();
    }
}
