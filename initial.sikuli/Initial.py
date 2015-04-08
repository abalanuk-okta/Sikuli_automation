from sikuli.Sikuli import App, Pattern 
import string, random
import os

import unittest
import HTMLTestRunner

def generate_random_string(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

project_name = generate_random_string()

class WelcomeTest(unittest.TestCase):
    
    def testLogin(self):
        appPath = "/Volumes/Untitled/Users/abalanuk/Library/Developer/Xcode/DerivedData/FTBmac-bdlxzelqkdzjxseeollhyiidfbzj/Build/Products/Debug/FTBmac.app"

        ftbApp = App(appPath)

        if not ftbApp.window():
            App.open(appPath)
                  
        ftbApp.focus()
       
        #if not ftbApp.window():
            #print "No FTB window"
        #else:
            #print "FTB app is appeared"
        
        click("1428511211225.png")
        wait("1428511375900.png")
        click(find("1428512393650.png").right(30))
        type("shahar@testmh.com")
        click(find("1428512672638.png").right(30))
        type("236541")
        click("1428512772486.png")
        if exists("1428512944589.png"):
            popup("Login was sucessfull")

        #os.remove("/Volumes/Untitled/Users/abalanuk/Library/Application Support/com.myheritage.FTBmac/")
        
        
        
suite = unittest.TestLoader().loadTestsFromTestCase(WelcomeTest)
outfile = open("/Users/abalanuk/Desktop/Sikuli/Reports/%s.html" % (project_name), "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title=' Report Title', description='desc..' )
runner.run(suite)
outfile.close()


