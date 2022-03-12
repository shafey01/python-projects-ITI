import random
import webbrowser

websiteList = ["https://www.facebook.com/","https://www.google.com","https://www.youtube.com/","https://twitter.com/?lang=en","https://www.linkedin.com"]

webbrowser.open(str(random.choice(websiteList)), new=2)
# print(str(random.choice(websiteList)))