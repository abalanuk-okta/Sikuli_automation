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
