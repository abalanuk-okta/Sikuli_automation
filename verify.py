
def verifyApp(ftbApp):
# check application
    if not ftbApp.window():
        print("FAIL: No FTB window")
    else:
        print("PASS: FTB app is appeared")