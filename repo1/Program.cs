using System.Text.RegularExpressions;
namespace lab1
{
    public class NewClass
    {
        static void Main()
        {
           /* int[,] arr = new int[3, 3]; // // задание 1
            int length = 3;
            Random x = new Random();
            for (int i = 0; i < length; i++)
            {
                for (int j = 0; j < length; j++)
                {
                    arr[i, j] = x.Next(-10, 10);
                    Console.Write("{0,3}", arr[i, j]);
                }
                Console.WriteLine();
            }
            for (int i = 0; i < length / 2; i++)
            {
                for (int j = 0; j < length; j++)
                {
                    int temp = arr[i, j];
                    arr[i, j] = arr[length - 1 - i, j];
                    arr[length - 1 - i, j] = temp;
                }
            }
            Console.WriteLine();
            for (int i = 0; i < length; i++)
            {
                for (int j = 0; j < length; j++)
                {
                    Console.Write("{0,3}", arr[i, j]);
                }
                Console.WriteLine();
            }*/
           /* string str2 = ""; // задание 2
            int inc = 0;
            string str1 = "Приветтее";
            for (int i = 0; i < str1.Length; i++)
                if (!str2.Contains(str1[i]))
                {
                    str2 += str1[i];
                    {
                        inc++;
                    }

                }
            Console.WriteLine("Различных символов = " + inc);
            Console.ReadKey(true);*/
/*string str1 = "Еслыфвап"; // задание 3
if (!Regex.IsMatch(str1, @"\P{IsCyrillic}"))
{
    Console.WriteLine("Это русский текст");
}
else{
    Console.WriteLine("Это НЕ русский текст");
}*/
        }

    }

}

