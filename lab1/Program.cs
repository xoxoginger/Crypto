using System;
using System.Numerics;
using System.IO;
using System.Linq;

namespace factor
{
    class Program
    {
        static void Main(string[] args)
        {
            string num = "4873822355066485648401071991924136818675872398286535454064775888224354057647759827888672904881758021952112721372792540754490030245608396182923905355014076090502386397665983839009222976102719595547524782591827859918063701352306472019393440971955164354386032725843607346843355546699218596423146704382946211873403241967325626024974089074590478580274181015361612573624846467079841362239862486328418954301422487721661475185724434860156652642467350107207026973065315203";
            BigInteger GCD = 1, r, res = 1;
            BigInteger.TryParse(num, out r);
            BigInteger[] nums = new BigInteger[40];
            string[] lines = File.ReadAllLines("GCD.txt").Take(40).ToArray();
            for (int i = 0; i < 40; i++)
            {
                BigInteger.TryParse(lines[i], out nums[i]);
                GCD = BigInteger.GreatestCommonDivisor(r, nums[i]);
                if (GCD > 1)
                {
                    res = BigInteger.Divide(r, GCD);
                    break;
                }
            }

            using (StreamWriter outputFile = new StreamWriter("res.txt"))
            {
                outputFile.WriteLine(GCD);
                outputFile.WriteLine(res);
            }
        }
    }
}
