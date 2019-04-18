using System;

namespace wcapp
{
    class Program
    {
        static void Main(string[] args)
        {
            // Asks for your salary
            Console.Write("Ka du tjen i året? ");
            int salary = Convert.ToInt32(Console.ReadLine());

            // Add error handling if not int here.

            // Asks for how long you were on the can
            Console.Write("Kor lenge satt du på dass? ");
            int wctime = Convert.ToInt32(Console.ReadLine());

            // Add error handling if not int here.

            // calculates how much you earned while sitting on the can
            int shitMoney = ((salary / 1850) / 60 * wctime);
            Console.WriteLine();
            Console.WriteLine("Du tjente " + (shitMoney) + " krona mens du va på dass");

        }
    }
}