import java.io.*;
import java.nio.file.CopyOption;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.HashMap;
import java.util.List;
import java.util.Arrays;
/**
 * Removes a python 'class' given:
 * ClassRemover FullPathURI nameOfClass
 * assming the class starts with
 * class "nameOfClass"
 *     and ends at the start of the next instance of the word 'class'
 *
 */
public class Denumerator {
    public static final String cls="class";

    public static void debugMain(String[] args){
        for(String arg:args){
            System.out.println(denumerate(arg));
        }
    }
    public static void main(String[] args) throws IOException {
        String filePath=args[0];
	String classToRename=args[1];
	String newClassName=args[2];

        String backupFilePath = filePath+".orig";

        File outFile = new File(filePath);
        File backupFile = new File(backupFilePath);
        Files.move(outFile.toPath(),backupFile.toPath()); //Make sure this move completes before we destroy outFile
        BufferedReader lineStreamer;

        HashMap<String,String> denumerations = new HashMap<String,String>();// In this case, rewrites a single class, workse like Denumerator.java
	denumerations.add(classToRename,newClassName);

        String line;
        int instances=0;
       
        lineStreamer = new BufferedReader(new FileReader(backupFile));

        BufferedWriter rewriter = new BufferedWriter(new FileWriter(outFile,false));//Blow out outFile (our argument). Risky but why not? We made a backup

        line = lineStreamer.readLine();
        while(line!=null)
        {
            for(String key:denumerations.keySet()){
                if(line.contains(key)){
                    instances++;
                    line = line.replaceAll(key, denumerations.get(key));
                }
            }
            rewriter.write(line);
            rewriter.write(System.lineSeparator());//When reading lines, we're not getting the line separator
            try {
                line = lineStreamer.readLine(); // Null if null,
            }
            catch (Exception e) {
                System.err.println(e);
                line = null;
                //Done, either we hit EoF or a read error or whatever.
            }
        }
        System.out.println("Successfully renamed all instances over " + instances + " instances");
        rewriter.flush();
        rewriter.close();
    }

}
