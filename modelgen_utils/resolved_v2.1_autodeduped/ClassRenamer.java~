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

        //List of class names that have to be deduplicated by hand
        //Example: GeometryItem in Genotype is the same as GeometryItem3, but GeometryItem 2 and 4 are a single separate
        //entity containing different elements. Really should be GeometryItem and GeometryItem2. But the only way to teach
        //this algorithm to do that is to save off the whole token stream of the class for each class we're doing this with,
        //Including the original non-numbered version that we're not dealing with here, so would have to have a lot more 'brains'
        //(and probably a full rewrite.) -JDLS
        List<String> ignoreList = Arrays.asList("GeometryItem","SortBy");

        String backupFilePath = filePath+".orig";

        File outFile = new File(filePath);
        File backupFile = new File(backupFilePath);
        Files.move(outFile.toPath(),backupFile.toPath()); //Make sure this move completes before we destroy outFile
        BufferedReader lineStreamer = new BufferedReader(new FileReader(backupFile));

        HashMap<String,String> denumerations = new HashMap<String,String>();// Original -> Denumeration

        String line = lineStreamer.readLine();
        while(line!=null)
        {
            StringTokenizer tokenizer = new StringTokenizer(line,"\t\n\r\f (=");//All newlines, etc ... '(' is used for class blahclassName(blah)
            // = is also here for 'description='blahblah', and ( for ClassName(blahblah)
            String nextToken = null; //Terrible hack - store the 'next token' so we can have single token lookahead if nextToken is not null, use it
            while(tokenizer.hasMoreTokens()){
                if((nextToken!=null?nextToken:tokenizer.nextToken()).equalsIgnoreCase(cls)){ //class BLAH
                    nextToken=null;//clear read token

                    String className=tokenizer.hasMoreTokens()?tokenizer.nextToken():null;
                    if(     className!=null && //We have a class name
                            !denumerate(className).equals(className) && //We don't need to prume the originals
                            !ignoreList.contains(denumerate(className))){ // ClassName isn't one of the ignored names (we need to dedup these by hand)
                    String description = null;
                    nextToken=tokenizer.nextToken();
                    while(tokenizer.hasMoreTokens() && !nextToken.equals(cls)){
                        //Look ahead to see if there's a 'description'. Geometry dedups on name+description
                        if(nextToken.equals("description")){

                        }
                        nextToken=tokenizer.nextToken();
                        }
                    if(description !=null){
                        //denumerations gets a description field
                    }else {
                        denumerations.put(className, denumerate(className));
                    }
                    }
                }
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

        System.out.println("Identified " + denumerations.size() + " classes containing numerics");
        for(String key:denumerations.keySet()){
            System.out.println(key + " => " + denumerations.get(key));
        }

        System.out.println("Replacing all instances with denumerated versions");

        int instances=0;
        lineStreamer.close();
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
        System.out.println("Successfully denumerated all instances of " + denumerations.size() + " classes over " + instances + " instances");
        rewriter.flush();
        rewriter.close();
    }

    //Removes trailing numerics
    private static String denumerate(String in){
        char maybeNumber = in.charAt(in.length()-1);//The last character in this token
        if(maybeNumber >= '0' && maybeNumber <= '9'){ //it was a number
            return denumerate(in.substring(0,in.length()-1)); //'tail' recursion. Get it, because we're looking at the tail of the....
        }
        return in;
    }
}
