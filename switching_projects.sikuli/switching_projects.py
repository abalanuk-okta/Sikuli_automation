from sikuli.Sikuli import *

from Config import Config
import Helpers
import base_cases

import unittest
import HTMLTestRunner


project_name = Helpers.generate_random_string()

class SwitchingProjectTestCase(unittest.TestCase):
    
        def testSwitchingProject(self):
            app = base_cases.BaseMyHeritageTestCase()
            app.openApp()
            app.loginApp()

            while not exists("project_ui_elements.png"):
                wait(2)
            add_first_person = Region("add_first_person_dialog.png")
            if exists(add_first_person):
                click(add_first_person.inside().find(Pattern("cancel_button.png").similar(0.67)))
            wait(1)
            
            app.switchingProject()
            
            wait(2)
            if exists("project_ui_elements.png"):
                print "Switching between projects was successful"
            else: 
                print "Something went wrong...Switching project was failed"
            
            app.closeApp()
            base_cases.BaseMyHeritageTestCase.cleanUserData()

Config.init()
suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(SwitchingProjectTestCase))
#suite.addTest(unittest.TestLoader().loadTestsFromTestCase(sikuli1.CreatingProjectTest))

outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()


