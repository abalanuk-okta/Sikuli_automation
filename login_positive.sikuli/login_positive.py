from sikuli.Sikuli import *

from Config import Config
import Helpers
import base_cases

import unittest
import HTMLTestRunner


project_name = Helpers.generate_random_string()

class PositiveLogin(unittest.TestCase):
    
        def testPositive(self):
            app = base_cases.BaseMyHeritageTestCase()
            app.openApp()
            app.loginApp()    
            while not exists("no_projects_found.png"):
                wait(5)
             
            app.closeApp()
            base_cases.BaseMyHeritageTestCase.cleanUserData()

Config.init()
suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(PositiveLogin))
#suite.addTest(unittest.TestLoader().loadTestsFromTestCase(sikuli1.CreatingProjectTest))

outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()


