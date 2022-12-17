import java.io.*;
import java.util.*;
import java.io.File; // Import the File class
import java.io.FileWriter; // Import the FileWriter class

public class Assembler2 {

    static int opcode(String s) {
        if (s.equals("STOP"))
            return 00;
        if (s.equals("ADD"))
            return 01;
        if (s.equals("SUB"))
            return 2;
        if (s.equals("MULT"))
            return 3;
        if (s.equals("MOVER"))
            return 4;
        if (s.equals("MOVEM"))
            return 5;
        if (s.equals("COMP"))
            return 6;
        if (s.equals("BC"))
            return 7;
        if (s.equals("DIV"))
            return 8;
        if (s.equals("READ"))
            return 9;
        if (s.equals("PRINT"))
            return 10;
        if (s.equals("START"))
            return 01;
        if (s.equals("END"))
            return 2;
        if (s.equals("ORIGIN"))
            return 3;
        if (s.equals("EQU"))
            return 4;
        if (s.equals("LTORG"))
            return 5;
        if (s.equals("DC"))
            return 1;
        if (s.equals("DS"))
            return 2;
        return -1;
    }

    static String opclass(String s) {
        if (s.equals("ADD") || s.equals("STOP") || s.equals("SUB") || s.equals("MULT") || s.equals("MOVER")
                || s.equals("MOVEM") || s.equals("COMP") || s.equals("BC") || s.equals("DIV") || s.equals("READ")
                || s.equals("PRINT"))
            return "IS";
        if (s.equals("START") || s.equals("END") || s.equals("ORIGIN") || s.equals("EQU") || s.equals("LTORG"))
            return "AD";
        if (s.equals("DS") || s.equals("DC"))
            return "DL";
        return "$";
    }

    static int registers(String s) {
        if (s.equals("AREG"))
            return 1;
        if (s.equals("BREG"))
            return 2;
        if (s.equals("CREG"))
            return 3;
        if (s.equals("DREG"))
            return 4;
        return -1;
    }

    static int condition_codes(String s) {
        if (s.equals("LT"))
            return 1;
        if (s.equals("LE"))
            return 2;
        if (s.equals("EQ"))
            return 3;
        if (s.equals("GT"))
            return 4;
        if (s.equals("GE"))
            return 5;
        if (s.equals("ANY"))
            return 6;
        return -1;
    }

    public static void main(String args[]) throws IOException {
        FileWriter myObj = new FileWriter("IC.txt");
        FileWriter pool = new FileWriter("pooltable.txt");
        FileWriter symb = new FileWriter("symbtab.txt");
        FileWriter litt = new FileWriter("littab.txt");

        LinkedHashMap<String, Integer> symbtab = new LinkedHashMap<>();
        LinkedHashMap<String, Integer> littab = new LinkedHashMap<>();
        
        ArrayList<String> lit = new ArrayList<String>();
        ArrayList<Integer> litc = new ArrayList<Integer>();
        ArrayList<Integer> pooltab = new ArrayList<Integer>(2);

        pooltab.add(1);
        File input = new File("/Users/sanikainamdar/Desktop/LP1/A1_AssemblerPass1/pass1a.txt");
        FileReader fr = new FileReader(input);
        BufferedReader br = new BufferedReader(fr);
        String line;
        int lc = 0;
        while ((line = br.readLine()) != null) {
            String[] a = line.split("[ ,]");
            String op1 = "", op2 = "", op = "";
            int opco = opcode(a[0]);

            if (opco == -1) {
                symbtab.put(a[0], lc);
                op = a[1];
                if (a.length > 2)
                    op1 = a[2];
                if (a.length > 3)
                    op2 = a[3];
            } else {
                op = a[0];
                if (a.length > 1)
                    op1 = a[1];
                if (a.length > 2)
                    op2 = a[2];
            }
            opco = opcode(op);
            String opclass = opclass(op);

            // Printing opcode
            if (!op.equals("EQU") && !op.equals("LTORG"))
                myObj.write("(" + opclass + "," + opco + ") ");

            if (op.equals("MOVER") || op.equals("MOVEM") || op.equals("ADD") ||
                    op.equals("SUB") || op.equals("MULT") || op.equals("DIV") ||
                    op.equals("COMP")) {
                int r = registers(op1);
                myObj.write(" (" + r + ") ");
                int s;
                if (op2.charAt(0) == '=') {
                    op2 = op2.substring(2, op2.length() - 1);
                    if (littab.containsKey(op2)) {
                        Set<String> keys = littab.keySet();
                        List<String> listKeys = new ArrayList<String>(keys);
                        s = listKeys.indexOf(op2) + 1;
                    } else {
                        littab.put(op2, 0);
                        s = littab.size();

                    }
                    myObj.write(" (L," + s + ") ");
                } else {
                    if (symbtab.containsKey(op2)) {
                        Set<String> keys = symbtab.keySet();
                        List<String> listKeys = new ArrayList<String>(keys);
                        s = listKeys.indexOf(op2) + 1;
                        myObj.write(" (S," + s + ") ");
                    } else {
                        symbtab.put(op2, 0);
                        s = symbtab.size();
                        myObj.write(" (S," + s + ") ");
                    }
                }
            }

            if (op.equals("READ") || op.equals("PRINT")) {
                int s = 0;
                op2 = op1;
                if (symbtab.containsKey(op2)) {
                    Set<String> keys = symbtab.keySet();
                    List<String> listKeys = new ArrayList<String>(keys);
                    s = listKeys.indexOf(op2) + 1;
                    myObj.write(" (S," + s + ") ");
                } else {
                    symbtab.put(op2, 0);
                    s = symbtab.size();
                    myObj.write(" (S," + s + ") ");
                }
            }

            int check = 0;
            if (op.equals("EQU"))
                check = 1;
            if (op.equals("LTORG") || op.equals("END")) {
                if (op.equals("END"))
                    myObj.write("\n");
                pooltab.add(pooltab.get(pooltab.size() - 1) + littab.size());
                Set<String> keys = littab.keySet();
                for (String key : keys) {
                    myObj.write("(DL,01) (C," + key + ")\n");
                    check = 1;
                    lit.add(key);
                    litc.add(lc);
                    lc++;
                }
                littab = new LinkedHashMap<>();

            }
            if (op.equals("ORIGIN")) {
                int s;

                String[] operands = op1.split("[+]");
                // System.out.println(operands[0]+symbtab.containsKey(operands[0]));
                if (symbtab.containsKey(operands[0]))
                    lc = symbtab.get(operands[0]);
                if (operands.length > 1) {

                    lc = lc + Integer.parseInt(operands[1]);

                }
                String[] operands2 = op1.split("[-]");
                if (symbtab.containsKey(operands2[0]))
                    lc = symbtab.get(operands2[0]);

                if (operands2.length > 1) {

                    lc = lc - Integer.parseInt(operands2[1]);

                }
                op2 = operands[0];
                if (symbtab.containsKey(op2)) {
                    Set<String> keys = symbtab.keySet();
                    List<String> listKeys = new ArrayList<String>(keys);
                    s = listKeys.indexOf(op2) + 1;
                    myObj.write(" (S," + s + ") ");
                } else {
                    symbtab.put(op2, 0);
                    s = symbtab.size();
                    myObj.write(" (S," + s + ") ");
                }
                myObj.write(op1.substring(operands[0].length()));

            }
            if (op.equals("START")) {
                lc = Integer.parseInt(op1);
                myObj.write("(C," + lc + ")");
            }
            if (op.equals("EQU")) {
                if (symbtab.containsKey(op1))
                    symbtab.put(a[0], symbtab.get(op1));

            }
            if (op.equals("BC")) {
                int s = condition_codes(op1);
                myObj.write(" (" + s + ") ");
                if (symbtab.containsKey(op2)) {
                    Set<String> keys = symbtab.keySet();
                    List<String> listKeys = new ArrayList<String>(keys);
                    s = listKeys.indexOf(op2) + 1;
                    myObj.write(" (S," + s + ") ");
                } else {
                    symbtab.put(op2, 0);
                    s = symbtab.size();
                    myObj.write(" (S," + s + ") ");
                }
            }
            if (op.equals("DS")) {
                op1 = op1.replace('\'', ' ').trim();
                myObj.write("(C," + Integer.parseInt(op1) + ")");
                lc = lc + Integer.parseInt(op1);
            } else if (op.equals("DC")) {
                op1 = op1.replace('\'', ' ').trim();
                myObj.write("(DL,01) (C," + Integer.parseInt(op1) + ")");
                lc = lc + 1;
            }
            if (opclass.equals("IS"))
                lc = lc + 1;
            if (check == 0)
                myObj.write("\n");
        }
        myObj.close();
        System.out.println();

        Set<String> keys = symbtab.keySet();
        for (String key : keys) {
            symb.write("" + key + ":" + symbtab.get(key) + "\n");
        }

        for (int i = 0; i < lit.size(); i++) {
            litt.write("" + lit.get(i) + ":" + litc.get(i) + "\n");
        }
        System.out.println();
        System.out.println("POOLTAB");
        for (int i = 0; i < pooltab.size() - 1; i++) {
            pool.write("" + pooltab.get(i) + "\n");
        }
        symb.close();
        pool.close();
        litt.close();
    }
}