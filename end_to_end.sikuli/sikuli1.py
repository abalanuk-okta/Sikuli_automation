from sikuli.Sikuli import * # App, Pattern 

import unittest
import HTMLTestRunner

import Helpers
from myheritage import *
from Config import Config

project_name = Helpers.generate_project_name()

class EndtoEndFlow(unittest.TestCase):
    
    def testFlow(self):
        app = MyHeritage()
        app.openApp()

        #signup
        wait(3)
        click(Pattern("button_Sign_Up.png").similar(0.80))
      
        wait("1429693900329.png")
        click(find("first_name.png").right(30))
        type("Test")
            
        click(find("last_name.png").right(30))
        type("User")
            
        click(find("1429692552272.png").right(30))
        type("abalanuk@lohika.com")
            
        click(find("1429692637305.png").right(30))
        type("Abcd1234")

        click(find("1429692681989.png").right(30))
        type("Abcd1234")
            
        click("1428512772486.png")
            
        wait("birth_year.png")
        click(find("birth_year.png").right(30))
        type("1984")

        click(find("adress.png").right(30))
        type("301 Brannan Street")

        click(find("state.png").right(30))
        type("California")

        click(find("country.png").right(30))
        click("1429694326436.png")

        click(find("zip_code.png").right(30))
        type("CA 94107")

        click(find("1429694428633.png").right(30))
        type("1-888-722-7871")

        click("1428512772486.png")
            
        if (exists("1429694591863.png") or exists("1429696065256.png")):
            click("1429694625259.png")
        elif exists("1429694868493.png"):
            app.closeApp()

        #login into app
        app.openApp()

        wait(Pattern("1429719459653.png").similar(0.80))
                        
        click("Log_in_button.png")
        wait("1428511375900.png")
        click(find("1428512393650.png").right(30))
        type("shahar@testmh.com")
            
        click(find("1428512672638.png").right(30))
        type("236541")
        click("1428512772486-1.png")   
        #m = Region("1429858690529.png").find(Pattern("1429858532302.png").similar(0.80))
        #while not exists(m):
        
        wait("1429859193288.png",11)
        
        #create new project
        
        #click(find(Pattern("refresh_icon.png").similar(0.85)).nearby(25).right().find("1428489180533.png"))

        #click("Screen Shot 2015-04-07 at 1.16.21 PM.png")
        click(Pattern("1429859596817.png").similar(0.79))

        wait(1)

        click(find(Pattern("1428487586983.png").similar(0.68)))

        click(find(Pattern("1429860143826.png").similar(0.80)))

        #type(project_name)
        type("Test Project")

        click(find("1428487891580.png"))

        wait(2)

        click(find("1428488028343.png"))

        while not exists(Pattern("1429861116679.png").similar(0.65)):
            wait(3)
        click(find(Pattern("1429861252301.png").similar(0.64)).right(30))

        #person_name = Helpers.generate_random_string()
        type("Andrew")

        click(find(Pattern("1428488759155.png").similar(0.50)))
        wait(3)

        hover(find(Pattern("1428489545679.png").similar(0.60)))

        wait(1)

        click(find(Pattern("1428489494577.png").similar(0.80)))

        hover(find("1428489619025.png"))

        click(find(Pattern("1428489619025.png").similar(0.80)))

        wait(3)

        #mother_maiden_name = Helpers.generate_random_string()

        type("Balanuk")

        click(find(Pattern("1428488759155.png").similar(0.50)))

        # quitting app after testing

        wait(3)
        click(find(Pattern("Screen Shot 2015-04-08 at 12.57.33 PM.png").similar(0.90)))
        click(find(Pattern("SSQ.png").similar(0.60)))

Config.init()

suite = unittest.TestLoader().loadTestsFromTestCase(EndtoEndFlow)
outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()





