from sikuli.Sikuli import *

import unittest
import HTMLTestRunner

import Helpers
import base_cases
#does it need here import config???
from Config import Config

project_name = Helpers.generate_project_name()

class AddPersonalFotoFromInfoTestCase(unittest.TestCase):

    def testCreateProject(self):
        app = base_cases.BaseMyHeritageTestCase()
        app.openApp()
        #app.loginApp()
        app.addPersonalFotoFromInfoView()

        #while not exists(Pattern("avatar2.png").similar(0.60)):
            #wait(1)
            
        #print "Root person was added"

        #exit from app after testing
        #click(find(Pattern("FTBmac_menu.png").similar(0.66)))
        #click(find(Pattern("SSQ.png").similar(0.60)))
        
        base_cases.BaseMyHeritageTestCase.cleanUserData()
        #base_cases.BaseMyHeritageTestCase.cleanProjectData()

Config.init()

suite = unittest.TestLoader().loadTestsFromTestCase(AddPersonalFotoFromInfoTestCase)
outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()





