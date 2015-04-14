from sikuli.Sikuli import App, Pattern 
from Config import Config
import Helpers
import os
import baseCases 
reload(baseCases)

import sikuli1
reload(sikuli1)

import unittest
import HTMLTestRunner


project_name = Helpers.generate_random_string()


class PositiveLoginTest(unittest.TestCase):

        def testLogin(self):
            Config.init()
        
            baseCases.BaseCases.cleanUserData()
    
            baseCases.BaseCases.testOpenApp()
                           
            click("1428511211225.png")
            wait("1428511375900.png")
            click(find("1428512393650.png").right(30))
            type("shahar@testmh.com")
            click(find("1428512672638.png").right(30))
            type("236541")
            click("1428512772486.png")
   
suite = unittest.TestSuite()

Config.init()

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(PositiveLoginTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(sikuli1.CreatingProjectTest))

outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()


