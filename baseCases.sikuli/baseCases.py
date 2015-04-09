from sikuli.Sikuli import App, Pattern 
from Config import Config
import os

import unittest
import HTMLTestRunner

class BaseCases():

    @classmethod
    def login(cls):
        
        # appPath = "~/Users/user/Library/Developer/Xcode/DerivedData/FTBmac-bdlxzelqkdzjxseeollhyiidfbzj/Build/Products/Debug/FTBmac.app"
        appPath = Config.get_app_path()
        
        ftbApp = App(appPath)

        if not ftbApp.window():
            App.open(appPath)
                  
        ftbApp.focus()

    @classmethod
    def testLogout(cls):       
        os.remove(Config.get_user_data_path() + "/LoggedUser.info")

    #def testRunner(self):
        #suite = unittest.TestLoader().loadTestsFromTestCase(BaseCases)
        #runner.run(suite)