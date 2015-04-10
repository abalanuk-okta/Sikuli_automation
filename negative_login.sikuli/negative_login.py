from sikuli.Sikuli import App, Pattern 
from Config import Config
import Helpers
import os
import baseCases 
reload(baseCases)

import unittest
import HTMLTestRunner


project_name = Helpers.generate_random_string()


class NegativeLoginTest(unittest.TestCase):

        baseCases.BaseCases.testOpenApp()

        if not exists(Pattern("signUp_Login.png").similar(0.80)):
            baseCases.BaseCases.testCloseApp()
            baseCases.BaseCases.cleanUserData()
            wait(1)
            baseCases.BaseCases.testOpenApp()
                           
        click("1428511211225.png")
        wait("1428511375900.png")
        click(find("1428512393650.png").right(30))
        type("testuser@testmh.com")
        click(find("1428512672638.png").right(30))
        type("123456")
        click("1428512772486.png")
        wait("Exit_button_login_flow.png")
        # use image of actual UI
        click("Exit_button_login_flow.png")
        
        popup("Negative Login test is sucessfull")


Config.init()
        
suite = unittest.TestLoader().loadTestsFromTestCase(NegativeLoginTest)
outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()


