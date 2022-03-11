from validation import *

def emailcomposer():
    emailSub = emailsubject()
    emailFrom = isValidEmailFrom()
    emailTo = isValidEmailTo()
    name = isValidName()
    print(f".......................................................\n")
    print(f"From: {emailFrom}\nTo: {emailTo}\n\nHi, {name}\nThis is am Email Template\nThanks.")
    print(f"........................{emailSub}...............................\n")


emailcomposer()