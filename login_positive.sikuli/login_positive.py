from sikuli.Sikuli import App, Pattern

from Config import Config
import Helpers
from myheritage import *

import unittest
import HTMLTestRunner


project_name = Helpers.generate_random_string()
app = MyHeritage()

class PositiveLogin(unittest.TestCase):
    
        def testPositive(self):
            app.openApp()

            wait(Pattern("1429719459653.png").similar(0.80))
                        
            click("Log_in_button.png")
            wait("1428511375900.png")
            click(find("1428512393650.png").right(30))
            type("shahar@testmh.com")
            
            click(find("1428512672638.png").right(30))
            type("236541")
            click("1428512772486.png")   
            wait("1429720378867.png",10)
            
            app.closeApp()
            myheritage.MyHeritage.cleanUserData()

suite = unittest.TestSuite()

Config.init()

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(PositiveLogin))
#suite.addTest(unittest.TestLoader().loadTestsFromTestCase(sikuli1.CreatingProjectTest))

outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()


