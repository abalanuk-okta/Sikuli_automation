from sikuli.Sikuli import *
import os

from Config import Config
import Helpers
from myheritage import *


import unittest
import HTMLTestRunner


project_name = Helpers.generate_random_string()

class Signup(unittest.TestCase):

    def testSignUp(self):
        app = MyHeritage()
        app.openApp()
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


Config.init()
suite = unittest.TestSuite()

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Signup))

outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()


