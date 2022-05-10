import java.util.*;

class Fibonacci{
    public static int[] fibs(int n){
        int[] fibs = new int[n + 1];
        fibs[1] = 1;
        for(int i=2; i<=n; i++){
            fibs[i] = (fibs[i-1] + fibs[i-2]) % 1000000007;
        }
        return fibs;
    }

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int[] memo = fibs(100000000);

        while(in.hasNextLine()){
            try{
                int i = in.nextInt();
                System.out.println(memo[i]);
            }catch(java.util.InputMismatchException e){
                return;
            }
        }

    }
}