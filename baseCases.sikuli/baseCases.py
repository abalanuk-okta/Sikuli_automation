from sikuli.Sikuli import App, Pattern 
from Config import Config
import os

import unittest
import HTMLTestRunner

class BaseCases():

    @classmethod
    def testOpenApp(cls):
        
        # appPath like "~/Users/username/Library/Developer/Xcode/DerivedData/FTBmac-bdlxzelqkdzjxseeollhyiidfbzj/Build/Products/Debug/FTBmac.app"
        appPath = Config.get_app_path()
        
        ftbApp = App(appPath)

        if not ftbApp.window():
            App.open(appPath)
                  
        ftbApp.focus()

    @classmethod
    def cleanUserData(cls):       
        os.remove(Config.get_user_data_path() + "/LoggedUser.info")

    @classmethod
    def testCloseApp(cls):       
        appPath = Config.get_app_path()

        ftbApp = App(appPath)

        ftbApp.close()

    @classmethod
    def testDoLogin(cls):
        click("1428511211225.png")
        wait("1428511375900.png")
        click(find("1428512393650.png").right(30))
        type("shahar@testmh.com")
        click(find("1428512672638.png").right(30))
        type("236541")
        click("1428512772486.png")

