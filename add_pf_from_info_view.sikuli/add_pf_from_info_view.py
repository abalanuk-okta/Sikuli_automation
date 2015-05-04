from sikuli.Sikuli import *

import unittest
import HTMLTestRunner

import Helpers
import base_cases
reload(base_cases)
#does it need here import config???
from Config import Config

project_name = Helpers.generate_project_name()

class AddPersonalFotoFromInfoTestCase(unittest.TestCase):

    def testAddPersonalFoto(self):
        app = base_cases.BaseMyHeritageTestCase()
        app.openApp()
        app.loginApp()
        app.fullScreenApp()
        app.addPersonalFotoFromInfoView()
        while not exists("added_personal_foto.png"):
            wait(1)
            
        print "Personal foto was added"
        
        app.closeAppByShotkey()
        base_cases.BaseMyHeritageTestCase.cleanUserData()


Config.init()

suite = unittest.TestLoader().loadTestsFromTestCase(AddPersonalFotoFromInfoTestCase)
outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()





