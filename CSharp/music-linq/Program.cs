using System;
using System.Collections.Generic;
using System.Linq;
using JsonData;

namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //Collections to work with
            List<Artist> Artists = JsonToFile<Artist>.ReadJson();
            List<Group> Groups = JsonToFile<Group>.ReadJson();

            //========================================================
            //Solve all of the prompts below using various LINQ queries
            //========================================================

            //There is only one artist in this collection from Mount Vernon, what is their name and age?
            Artist selectArtist = Artists.SingleOrDefault(art => art.Hometown == "Mount Vernon");
            Console.WriteLine(selectArtist.Age);

            //Who is the youngest artist in our collection of artists?
            int youngestage = Artists.Min(art => art.Age);
            List<Artist>  youngestArtist = Artists.Where(a => a.Age == youngestage).ToList();
            System.Console.WriteLine(youngestArtist[0].ArtistName);
            //Display all artists with 'William' somewhere in their real name
            List<Artist> willArtists = Artists.Where( a => a.RealName.Contains("William")).ToList();
            for (var i = 0; i < willArtists.Count; i++)
                {
                    Console.WriteLine(willArtists[i].RealName);
                }
            //Display the 3 oldest artist from Atlanta

            List<Artist> oldestArtists = Artists.OrderByDescending ( a => a.Age ).ToList();
            for (var i = 0; i < 3; i++)
                {
                    Console.WriteLine(oldestArtists[i].ArtistName);
                }
            //(Optional) Display the Group Name of all groups that have members that are not from New York City

            //(Optional) Display the artist names of all members of the group 'Wu-Tang Clan'
        }
    }
}
