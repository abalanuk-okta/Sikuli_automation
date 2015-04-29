from sikuli.Sikuli import *
import unittest

from Config import Config
import Helpers

import base_cases
import HTMLTestRunner

project_name = Helpers.generate_random_string()

class SignupTestCase(unittest.TestCase):

    def testSignUp(self):
        app = base_cases.BaseMyHeritageTestCase()
        app.openApp()
        #popup("App is opened. Trying to signup")
        wait(2)
        app.verifyApp()
        app.signUp()
        if (exists("exists_pwd_not_valid.png") or exists("already_auth.png")):
            click("exit.png")
            #popup("User is already registered")
        elif exists("no_project_found.png"):
            app.closeApp()        

        
Config.init()
suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(SignupTestCase))

outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()


