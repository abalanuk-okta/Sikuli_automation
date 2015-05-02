from sikuli.Sikuli import *
from Config import Config
import os
#from shutil.py import rmtree

import unittest

class BaseMyHeritageTestCase(object):

    def __init__(self):
        appPath = Config.get_app_path()
        self._app = App(appPath)
        Settings.ActionLogs = True

        

    def openApp(self):
        if not self._app.window():
            self._app.open()
           
        self._app.focus()


    def closeApp(self):       
        self._app.close()
        

    def closeAppFromMenu(self):
        click(find(Pattern("FTBmac_menu.png").similar(0.66)))
        click(find(Pattern("SSQ.png").similar(0.60)))


    def verifyApp(self):
        if exists(Pattern("menus.png").similar(0.62)):
            print "PASS: FTB window appeared"
        else:
            print "FAIL: No FTB window"

        

    def signUp(self):
        
        click(Pattern("button_Sign_Up.png").similar(0.69))
      
        wait("signup_title.png")
        click(find("first_name.png").right(30))
        type("Test")
            
        click(find("last_name.png").right(30))
        type("User")
            
        click(find("Email.png").right(30))
        type("abalanuk@lohika.com")
            
        click(find("password.png").right(30))
        type("Abcd1234")

        click(find("confirm_pass.png").right(30))
        type("Abcd1234")
            
        click("next.png")
            
        wait("birth_year.png")
        click(find("birth_year.png").right(30))
        type("1984")

        click(find("adress.png").right(30))
        type("301 Brannan Street")

        click(find("state.png").right(30))
        type("California")

        click(find("country.png").right(30))
        click("country_value.png")

        click(find("zip_code.png").right(30))
        type("CA 94107")

        click(find("telephone.png").right(30))
        type("1-888-722-7871")

        click("next.png")

        

    def loginApp(self):
        wait("Login_button.png",2)
                        
        click("Log_in_button.png")
        wait("Title_login_form.png")
        click(find("email-1.png").right(30))
        type("shahar@testmh.com")
            
        click(find("pwd.png").right(30))
        type("236541")
        click("next_button.png")

        
        
    def createProject(self):
        while not exists("tree_menu.png"):
                wait(3)

        print "User is logged in successfully"
        
        try:
            create = Region(find(Pattern("project_list.png").similar(0.57)))
        except FindFailed:
            popup("Unable to find Project list drop down menu")
            
        create.highlight(1)

        if exists(Pattern("title_adding_root_person.png").similar(0.61)):
            click(Pattern("cancel_button.png").similar(0.66))
        wait(2)
            
        click(find(Pattern("refresh_icon.png").similar(0.63)).right(20))
        
        click(find(Pattern("create_NP_from_list.png").similar(0.64)))

        wait("start_new_tree.png",3)

        click(find(Pattern("start_new_tree.png").similar(0.65)))

        click(find(Pattern("project_name.png").similar(0.59)))

        type(project_name)

        click(find("next-1.png"))

        wait(2)

        click(find(Pattern("done.png").similar(0.62)))

        while not exists(Pattern("person_icon.png").similar(0.54)):
            wait(1)

        click(find(Pattern("first_name-1.png").similar(0.62)).right(30))

        person_name = Helpers.generate_random_string()
        type(person_name)
        click(find(Pattern("last_name-1.png").similar(0.61)).right(30))
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
        

   def switchingProject(self)
        click(find(Pattern("refresh_icon.png").similar(0.63)).right(20))
        
        click(find(Pattern("view_all_projects.png").similar(0.61)))
        wait(2)
        current_project = find(Pattern("current_project.png").similar(0.75))
        another_project_above = current_project.above(10).find(Pattern("another_project.png").similar(0.75))
        another_project_below = current_project.below(10).find(Pattern("another_project.png").similar(0.75))
        if exists(another_project_above):
            click(another_project_above)
        elif exists(another_project_below):
            click(another_project_below)

        click(find(Pattern("open_project_button.png").similar(0.71)))

    
    @classmethod
    def cleanUserData(cls):   
        try:
            os.remove(Config.get_user_data_path() + "/LoggedUser.info")
        except OSError:
            pass

    #@classmethod
    #def cleanProjectData(cls):   
        try:
            folder_path = Config.get_project_data_path()
            for file_object in os.listdir(folder_path):
                file_object_path = os.path.join(folder_path, file_object)
                if os.path.isfile(file_object_path):
                    os.unlink(file_object_path)
                elif os.path.isdir(file_object_path): shutil.rmtree(file_object_path)
        except Exception, e:
                print e




        
