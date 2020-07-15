# User lib import
from Src.Get_Hashtags   import get_hashtags
from Src.Auto_Login     import auto_login
from Src.Behaviour      import behaviour 
from Src.Get_Webdriver  import get_webdriver

while True:
    #Get webdriver
    webdriver = get_webdriver()

    # Auto login
    username = ''      # Add your user name here
    password = ''    # Add your password here
    auto_login(webdriver, username, password)

    # Get hashtags list from csv file
    hashtag_list = []
    get_hashtags(hashtag_list)

    #prev_user_list = [] #- if it's the first time you run it, use this line and comment the two below
    while True:
        behaviour(webdriver, hashtag_list)