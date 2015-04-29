from sikuli.Sikuli import *

import unittest
import HTMLTestRunner

import Helpers
import base_cases
from Config import Config

project_name = Helpers.generate_project_name()

class NewProjectFromListTestCase(unittest.TestCase):

    def testCreateProjectFromList(self):
        app = base_cases.BaseMyHeritageTestCase()
        app.openApp()
        app.loginApp()
        app.createProject()
        app.closeAppFromMenu()
        
        base_cases.BaseMyHeritageTestCase.cleanUserData()
        #base_cases.BaseMyHeritageTestCase.cleanProjectData()

Config.init()

suite = unittest.TestLoader().loadTestsFromTestCase(NewProjectFromListTestCase)
outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()





