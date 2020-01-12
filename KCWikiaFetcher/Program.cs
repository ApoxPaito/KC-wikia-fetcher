using System;
using System.IO;
using System.Net;

namespace KCWikiaFetcher
{
    class Program
    {
        static void Main(string[] args)
        {
            bool fwe = false;
            string[] ships;
            if (!Directory.Exists("img")) //Check if directory exists for images
                Directory.CreateDirectory("img");
            try { ships = File.ReadAllLines("ships.txt"); }
            catch
            {
                Console.WriteLine("ships.txt wasn't found. Make sure a Text file named ships.txt containing " +
                    "the ship IDs and names in format of \"ID - Name\" exists.");
                Console.ReadKey();
                return;
            }
            using (FileStream fileStream = new FileStream("log.txt", FileMode.Create, FileAccess.Write))
            {
                using (StreamWriter writer = new StreamWriter(fileStream))
                {
                    using (WebClient webClient = new WebClient())
                    {
                        foreach (string ship in ships)
                        {
                            string shipID = ship.Substring(0, ship.IndexOf("-") - 1);
                            string shipName = ship.Substring(ship.IndexOf("-") + 2);
                            try
                            {
                                string html = $"https://kancolle.fandom.com/wiki/File:{shipName}_Full.png";
                                writer.WriteLine($"INFO - Fetched HTML of {html}.");
                                string str = webClient.DownloadString(html);
                                str = str.Substring(str.IndexOf("<meta property=\"og:image\" content=\"") + 35);
                                str = str.Substring(0, str.IndexOf("\""));
                                writer.WriteLine($"INFO - Downloading {str} ...");
                                webClient.DownloadFile(str, $"img\\{shipID}.png");
                            }
                            catch
                            {
                                string msg = $"ERR - Failed to get {shipID} - {shipName} image, check name or try again.";
                                Console.WriteLine(msg);
                                writer.WriteLine(msg);
                                fwe = true;
                            }
                        }
                    }
                }
            }
            if (fwe)
                Console.WriteLine("Finished with errors, check log.txt for more info.");
            else
                Console.WriteLine("Finished with no errors.");
            Console.ReadKey();
        }
    }
}
