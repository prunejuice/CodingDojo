using Microsoft.AspNetCore.Mvc;
using dachi.Models;
using Microsoft.AspNetCore.Http;
using System;

namespace dachi.Controllers

{

    public class HomeController : Controller
    {
     [Route("")]
     public IActionResult Index() {

         if(HttpContext.Session.GetInt32("happiness")==null){
             HttpContext.Session.SetInt32("happiness", 20);
             HttpContext.Session.SetInt32("fullness", 20);
             HttpContext.Session.SetInt32("energy", 50);
             HttpContext.Session.SetInt32("meals", 3);
         }
        ViewBag.Happiness = HttpContext.Session.GetInt32("happiness");
        ViewBag.Fullness = HttpContext.Session.GetInt32("fullness");
        ViewBag.Energy = HttpContext.Session.GetInt32("energy");
        ViewBag.Meals = HttpContext.Session.GetInt32("meals");
         return View();
     }

    [Route("/Submit")]
     [HttpPost]

     public IActionResult Submit(string action) {

         Random rnd = new Random();
        var fullness = HttpContext.Session.GetInt32("fullness");
        var hap = HttpContext.Session.GetInt32("happiness");
        var meals = HttpContext.Session.GetInt32("meals");
        var energy = HttpContext.Session.GetInt32("energy");
         switch(action) {
             case "Play":
                
                 int happadd = rnd.Next(5,10);
                 hap += happadd;
                 energy -= 5;
                 
                 break;
             case "Feed":
               
                if (meals == 0 ){
                    Console.WriteLine("You do not have any meals");
                }

                meals -= 1;
               
                int fulladd = rnd.Next(5,10);
                fullness += fulladd;
             

                 break;
             case "Work":

                 energy -= 5;

                 int mealadd = rnd.Next(1,3);

                 meals += mealadd;
      

                 break;
             case "Sleep":

                energy += 15;
         
                fullness -= 5;
                hap -= 5;
           
                break;
             default:
                break;
            }

            HttpContext.Session.SetInt32("fullness", (int)fullness);
            HttpContext.Session.SetInt32("energy", (int)energy);
            HttpContext.Session.SetInt32("meals", (int)meals);
            HttpContext.Session.SetInt32("happiness", (int)hap);
            return RedirectToAction("Index");
        }
     
    }
}