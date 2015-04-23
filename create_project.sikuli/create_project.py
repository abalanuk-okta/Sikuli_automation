from sikuli.Sikuli import *

import unittest
import HTMLTestRunner

import Helpers
import baseCases
from Config import Config
from login_positive import *

project_name = Helpers.generate_project_name()

class NewProject(unittest.TestCase):

    def testCreateProject(self):
        
        a = PositiveLoginTest()
        a.testPositive()

        click(find("Create+.png"))
        #exit()

        click(find("1428487586983.png"))

        click(find("1428487683959.png"))

        type(project_name)

        click(find("1428487891580.png"))

        wait(2)

        click(find("1428488028343.png"))

        while not exists("1428488098834.png"):
            wait(1)

        click(find("1428489281730.png").nearby(25).right().find("1428488180823.png"))

        person_name = Helpers.generate_random_string()
        type(person_name)

        click(find(Pattern("1428488759155.png").similar(0.50)))
        wait(3)

        hover(find(Pattern("1428489545679.png").similar(0.60)))

        wait(1)

        click(find(Pattern("1428489494577.png").similar(0.80)))

        hover(find("1428489619025.png"))

        click(find(Pattern("1428489619025.png").similar(0.80)))

        wait(3)

        mother_maiden_name = Helpers.generate_random_string()

        type(mother_maiden_name)

        click(find(Pattern("1428488759155.png").similar(0.50)))

        # quitting app after testing

        wait(3)
        click(find(Pattern("Screen Shot 2015-04-08 at 12.57.33 PM.png").similar(0.90)))
        click(find(Pattern("SSQ.png").similar(0.60)))

Config.init()

suite = unittest.TestLoader().loadTestsFromTestCase(NewProject)
outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()





