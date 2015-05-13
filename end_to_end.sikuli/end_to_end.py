from sikuli.Sikuli import * # App, Pattern 

import unittest
import HTMLTestRunner

import Helpers
import base_cases
reload(base_cases)
from Config import Config

project_name = Helpers.generate_project_name()

class EndtoEndFlow(unittest.TestCase):
    
    def testEndToEndFlow(self):
        app = base_cases.BaseMyHeritageTestCase()
        app.openApp()
        app.signUp()
        app.closeApp()
        wait(1)
        app.openApp()
        app.loginApp()
        app.fullScreenApp()
        app.createProjectFromDropDown()
        app.addNewMemberDetails()
        while not exists(Pattern("avatar2.png").similar(0.60)):
            wait(1)
            app.closeApp()
            app.openApp()
            print "Root person was not visible"
            
        wait(1)
        app.addPersonalFotoFromInfoView()
        wait(1)
        Region(436,26,484,626).hover(find("1430864970320.png"))
        app.addNewMember()
        app.addNewMemberDetails()
        print "Second person was not visible"
        app.addPersonalFotoFromInfoView()
        wait(1)
        app.createProjectFromDropDown()
        click("1430863291594.png")
        wait(1)
        app.viewAllProjects()
        current = Region(2,2,294,431).find(Pattern("1430863796371.png").similar(0.75))
        click(current.above(10))
        if not exists("1430864044044.png"):
                print "Open Project button is not visible completely"
                doubleClick(current.above(10))
            
        while not exists(Pattern("1430896546442.png").similar(0.65)):
                if exists("1430891160748.png"):
                    print "App was crashed after switching on another project by doubleClick"
                    click(find(Pattern("1430891251319.png").targetOffset(-53,0)))
                    app.closeApp()
                    app.openApp()
                    wait(2)
                    app.viewAllProjects()
                    doubleClick(current.above(10))
                wait(1)
        
        app.addPhotos()
        app.viewAllProjects()
        click(find("1430897280186.png").below(10))
        click(find("1430890421157.png").inside().find("1430864425019.png"))
        wait(1)
        click(find("1430864481297.png").inside().find("1430864506835.png"))
        wait(1)
        app.closeAppByShotkey()
        base_cases.BaseMyHeritageTestCase.cleanUserData()
        
        
        
        

Config.init()

suite = unittest.TestLoader().loadTestsFromTestCase(EndtoEndFlow)
outfile = open(Config.get_reports_path() + "/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()





