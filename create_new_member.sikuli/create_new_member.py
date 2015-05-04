from sikuli.Sikuli import *

import unittest
import HTMLTestRunner

import Helpers
import base_cases
reload(base_cases)
from Config import Config

project_name = Helpers.generate_project_name()

class NewMemberTestCase(unittest.TestCase):

    def testCreateNewMember(self):
        app = base_cases.BaseMyHeritageTestCase()
        app.openApp()
        app.loginApp()
        app.createProject()
        app.addMemberDetails()
        app.addNewMember()
        app.addMemberDetails()
        wait(2)
        if exists(Pattern("2_members.png").similar(0.55)):
            print "Family member was created successfully"

        app.closeAppFromMenu()        
        base_cases.BaseMyHeritageTestCase.cleanUserData()
        #base_cases.BaseMyHeritageTestCase.cleanProjectData()

Config.init()

suite = unittest.TestLoader().loadTestsFromTestCase(NewMemberTestCase)
outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()





