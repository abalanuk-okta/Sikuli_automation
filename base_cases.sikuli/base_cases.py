from sikuli.Sikuli import *
from Config import Config
import os
import Helpers
#from shutil.py import rmtree

project_name = Helpers.generate_project_name()

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

    def fullScreenApp(self):
        type("f",KeyModifier.CMD + KeyModifier.CTRL)
        wait(2)

    def closeAppByShotkey(self):
        type("q",KeyModifier.CMD)
           

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
        while exists("login_spiner.png"):
            wait(1)

        
        
    def createProjectFromDropDown(self):
        try:
            create = Region(0,0,290,103).find("sync_navigate.png")
        except FindFailed:
            popup("Unable to find Project list drop down menu")
  
        create.highlight(1)        
        click(create.inside().find(Pattern("sync_icon.png").similar(0.56)).right(30))  
        click(Pattern("create_NP_from_list.png").similar(0.64))
        wait("start_new_tree.png",3)
        click(Pattern("start_new_tree.png").similar(0.65))
        click(Pattern("project_name.png").similar(0.59))

        type(project_name)
        click("next-1.png")
        wait(2)
        click(Pattern("done.png").similar(0.62))
        while not exists(Pattern("person_icon.png").similar(0.54)):
            wait(1)
            
        

    def viewAllProjects(self):
        click(find(Pattern("refresh_icon.png").similar(0.63)).right(20))
        
        click(find(Pattern("view_all_projects.png").similar(0.61)))
        wait(2)


            
    def switchToAnotherProject(self):
        try:
            project_list = (find(Pattern("project_dashboard.png").similar(0.62)))
        except FindFailed:
            popup("Unable to find Project list")
            
        project_list.highlight(2)
        print "Project dashboard appeared"

        if exists(current_project.above(10).find(Pattern("another_project.png").similar(0.80))):
            click(current_project.above(10).find(Pattern("another_project.png").similar(0.80)))
        elif exists(current_project.below(10).find(Pattern("another_project.png").similar(0.80))):
            click(current_project.below(10).find(Pattern("another_project.png").similar(0.80)))
        while not exists("open_project_button.png"):
            wait(1)
            click(find(Pattern("open_project_button.png").similar(0.71)))

    
    def addNewMember(self):

        Region(436,26,484,626).hover(find("1430579340575.png"))
        click(Pattern("add_new_member.png").targetOffset(0,-1))
        #idea to add list of screenshots and click it in cycle
        click("1430593983615.png")


        
    def addNewMemberDetails(self):
        click(find(Pattern("first_name-1.png").similar(0.62)).right(30))
        person_name = Helpers.generate_random_string()
        type(person_name)
        
        click(find(Pattern("last_name-1.png").similar(0.61)).right(30))
        person_last_name = Helpers.generate_random_string()
        type(person_last_name)
        
        calc = find(Pattern("region_calendar_icon.png").similar(0.74).targetOffset(143,9))

        click(calc.inside().find("1430589398792.png"))

        month = Region(791,348,504,433).find(Pattern("Exact.png").targetOffset(-73,1)).below(35)
        
        click(month)
        click(Pattern("value_month.png").similar(0.59))
        wait(2)
        #date = month.right(100)click(date)wait(1)click(find("date_drop_down.png").inside().find("1430584640795.png"))wait(1)
        doubleClick(month.right(10))
        type("1984")        
        click(find(Pattern("birth_place.png").similar(0.61)).right(30))
        birth_place = Helpers.generate_random_string()
        type(birth_place)
        click(find(Pattern("1428488759155.png").similar(0.50)))
        while not exists(Pattern("avatar2.png").similar(0.60)):
            wait(1)
            
        print "Root person was added"
        


    def addPersonalFotoFromInfoView(self):
        while not exists("add_foto_info_view.png"):
            wait(1)
        click(Pattern("add_foto_info_view.png").similar(0.60).targetOffset(-1,31))
        click(Pattern("avatar.png").similar(0.77))
        click("finder_open_button.png")
        click(find("finder_action_chooser.png").inside().find("finder_done.png"))
        
        
    def addPhotos(self):
        wait(2)
        click(find(Pattern("menus_to_photos.png").targetOffset(-138,0)))
        click(find("add_photos_area.png").inside().find("add_photos_content_button.png"))
        wait(1)
        type("G",KeyModifier.CMD + KeyModifier.SHIFT)
        type(Config.get_media_content_path())
        type(Key.ENTER)
        finder = find(Pattern("finder_title_bar.png").targetOffset(-11,1))
        type("2",KeyModifier.CMD)
        
        click(finder)
        click(find("1430781412816.png").inside().find("1430781446132.png"))
        image_files = find(Pattern("images-1.png").similar(0.62).targetOffset(-14,-7))
        click(image_files)
        #keyDown(Key.SHIFT)wait(0.5)type(Key.Down)keyUp(Key.SHIFT)
        
        click(find("1430782780125.png").inside().find("1430782807293.png"))
        
        
       
        
        
    @classmethod
    def cleanUserData(cls):   
        try:
            os.remove(Config.get_media_content_path() + "/LoggedUser.info")
        except OSError:
            pass

    #@classmethod
    #def openFilesWithOneExtension(cls):   
        try:
            for file in os.listdir(Config.get_media_content_path()):
                if file.endswith(".jpg"):
                    os.open(file,'r')
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




        
