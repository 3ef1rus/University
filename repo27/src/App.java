import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
       
        ArrayList<String> people = new ArrayList<String>();
        FileOutputStream fileOutputStream = new FileOutputStream("D:\\Desktop\\4.1 kyrs\\РКПП\\JavaLab7\\start.txt");
        FileInputStream fileInputStream = new FileInputStream("D:\\Desktop\\4.1 kyrs\\РКПП\\JavaLab7\\start.txt");
        for (int i = 0; i < 8; i++) {
            Integer a = ((int) (Math.random() * 12) - 5);
            String s = a.toString()+' ';
            fileOutputStream.write(s.getBytes());
        }
        int size = fileInputStream.available();
        char x = 0;
        Character mas[]=new Character[size];
        for(int j = 0; j < size; j++) {
            x=(char)fileInputStream.read();
            String convertedChar = Character.toString(x);
            mas[j]=convertedChar.charAt(0);
        }
        String arr[] = new String[size];
        for(int i = 0 ; i < mas.length;i++){
            if(mas[i]==' ')continue;
            if(mas[i]=='-'){
                arr[i]='-'+String.valueOf(mas[i+1]);
                i++;
            continue;
            }
            arr[i]=String.valueOf(mas[i]);
        }
        for(String s : arr) {
            if(s != null && s.length() > 0) {
               people.add(s);
            }
         }
         System.out.print("Список до преобразований : ");
        for (String person : people) {
            System.out.print(person+ ' ');
        }

        int i = 0;
        int res = 0;
        while (i < people.size() - res) {
            if (Integer.parseInt(people.get(i)) < 0) {
                people.add(people.get(i));
                people.remove(people.get(i));
                res++;
            } else
                i++;
        }
        System.out.println(" ");
        System.out.print("Список после преобразований : ");
        for (String person : people) {

            System.out.print(person+ ' ');
        }
        fileInputStream.close();
        fileOutputStream.close();
        System.gc();
    }
}
