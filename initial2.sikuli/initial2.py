from sikuli.Sikuli import App, Pattern 
from Config import Config
import Helpers
import os
import baseCases 
reload(baseCases)

import unittest
import HTMLTestRunner


project_name = Helpers.generate_random_string()


class PositiveLoginTest(unittest.TestCase):
    
        baseCases.BaseCases.testOpenApp()
                           
        click("1428511211225.png")
        wait("1428511375900.png")
        click(find("1428512393650.png").right(30))
        type("shahar@testmh.com")
        click(find("1428512672638.png").right(30))
        type("236541")
        click("1428512772486.png")

        baseCases.BaseCases.cleanUserData()
        #if exists("1428512944589.png"):
            #popup("Login was sucessfull")

        baseCases.BaseCases.testCloseApp()
        

Config.init()
        
suite = unittest.TestLoader().loadTestsFromTestCase(PositiveLoginTest)
outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()


