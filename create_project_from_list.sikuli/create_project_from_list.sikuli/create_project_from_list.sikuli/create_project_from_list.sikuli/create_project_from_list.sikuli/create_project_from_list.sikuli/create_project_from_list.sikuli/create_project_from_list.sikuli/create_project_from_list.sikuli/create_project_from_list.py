from sikuli.Sikuli import *

import unittest
import HTMLTestRunner

import Helpers
import base_cases
from Config import Config

project_name = Helpers.generate_project_name()

class NewProjectTestCase(unittest.TestCase):

    def testCreateProject(self):
        app = base_cases.BaseMyHeritageTestCase()
        app.openApp()
        app.loginApp()

        while not exists("no_projects_found.png"):
                wait(3)

        print "User is logged in successfully"
        try:
            create = Region(find("create_NP.png"))
        except FindFailed:
            popup("Unable to find target Region")
            
        #create.highlight(1)
        click(find(Pattern("plusCreateNP.png").similar(0.62)))
        

        click(find("1428487586983.png"))

        click(find(Pattern("project_name.png").similar(0.59)))

        type(project_name)

        click(find("next.png"))

        wait(2)

        click(find(Pattern("done.png").similar(0.62)))

        while not exists(Pattern("person_icon.png").similar(0.54)):
            wait(1)

        click(find(Pattern("first_name.png").similar(0.62)).right(30))

        person_name = Helpers.generate_random_string()
        type(person_name)
        click(find(Pattern("last_name.png").similar(0.61)).right(30))
        person_last_name = Helpers.generate_random_string()
        type(person_last_name)

        click(find("1430142653165.png"))
        calendar = Region(find("1430142731847.png"))
        click(find(Pattern("month_drop_down.png").similar(0.61)))
        click(Pattern("value_month.png").similar(0.59))
        click(Pattern("date.png").similar(0.78))
        doubleClick(Pattern("year.png").similar(0.61))
        
        type("1984")        
        
        click(find(Pattern("birth_place.png").similar(0.61)).right(30))
        birth_place = Helpers.generate_random_string()
        type(birth_place)

        click(find(Pattern("1428488759155.png").similar(0.50)))

        while not exists(Pattern("avatar2.png").similar(0.60)):
            wait(1)
            
        print "Root person was added"

        #exit from app after testing
        click(find(Pattern("FTBmac_menu.png").similar(0.66)))
        click(find(Pattern("SSQ.png").similar(0.60)))
        
        base_cases.BaseMyHeritageTestCase.cleanUserData()
        #base_cases.BaseMyHeritageTestCase.cleanProjectData()

Config.init()

suite = unittest.TestLoader().loadTestsFromTestCase(NewProjectTestCase)
outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()





