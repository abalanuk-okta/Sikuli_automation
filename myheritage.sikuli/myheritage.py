from sikuli.Sikuli import App, Pattern 
from Config import Config
import os

class MyHeritage(object):

    def __init__(self):
        appPath = Config.get_app_path()
        self._app = App(appPath)
    
    def openApp(self):

        if not self._app.window():
            self._app.open()
                  
        self._app.focus()

    def closeApp(self):       
        self._app.close()

    #def signUp(self):
        #self.openApp()

        

    @classmethod
    def cleanUserData(cls):   
        try:
            os.remove(Config.get_user_data_path() + "/LoggedUser.info")
        except OSError:
            pass




        
