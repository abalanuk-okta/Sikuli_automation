from sikuli.Sikuli import *

import unittest
import HTMLTestRunner

from Config import Config
import Helpers
import base_cases
reload(base_cases)

project_name = Helpers.generate_project_name()

class AddMediaContentTestCase(unittest.TestCase):

    def testAddMediaContent(self):
        app = base_cases.BaseMyHeritageTestCase()
        app.openApp()
        app.loginApp()
        
        app.fullScreenApp()
        app.addPhotos()
        while not exists("1430789093915.png"):
            wait(1)
            
        print "New foto was added"
        app.closeApp()
        base_cases.BaseMyHeritageTestCase.cleanUserData()

        
#Config.init()
suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(AddMediaContentTestCase))
#suite.addTest(unittest.TestLoader().loadTestsFromTestCase(sikuli1.CreatingProjectTest))

outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()