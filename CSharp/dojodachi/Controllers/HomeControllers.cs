using Microsoft.AspNetCore.Mvc;

namespace Dojodachi.Controllers

{
    public class HomeController : Controller
    {
        [Route("")]
        [HttpGet]
        public IActionResult Index(){
            return View();
        }

        [Route("submit")]
        [HttpPost]

        public IActionResult Submission(string name, string location)
        {
            
            return RedirectToAction("Index");
        }

    }
}