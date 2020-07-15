from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import csv

def behaviour(webdriver, hashtag_list):
    
    prev_user_list = pd.read_csv('users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
    prev_user_list = list(prev_user_list['0'])

    new_followed = []
    tag = -1
    followed = 0
    likes = 0
    comments = 0

    for hashtag in hashtag_list:
        tag += 1
        webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
        sleep(5)
        first_thumbnail = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
        
        first_thumbnail.click()
        sleep(randint(1,2))    
        try:        
            for x in range(1,200):
                username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').text
                
                # If we already follow, do not unfollow
                if username not in prev_user_list:               
                    if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                        
                        # Follow new user
                        webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                        new_followed.append(username)                       
                        followed += 1
                        sleep(randint(3,6))
                        
                        # Liking the picture
                        webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                        likes += 1
                        sleep(randint(2,7))
                        
                        # Comments and tracker
                        comm_prob = randint(1,10)
                        print('{}_{}: {}'.format(hashtag, x,comm_prob))
                        if comm_prob > 0:
                            comments += 1
                            webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form').click()
                            comment_box = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                            
                            # Case of random comment
                            if comm_prob == 1:
                                comment_box.send_keys('Really cool!')
                                sleep(randint(3,7))
                            elif comm_prob == 2:
                                comment_box.send_keys('lovely <3')
                                sleep(randint(3,7))
                            elif comm_prob == 3:
                                comment_box.send_keys('Nice!')
                                sleep(randint(3,7))
                            elif comm_prob == 4:
                                comment_box.send_keys('So cute!! <3')
                                sleep(randint(3,7))
                            elif comm_prob == 5:
                                comment_box.send_keys('Love it!!!')
                                sleep(randint(3,7))
                            elif comm_prob == 6:
                                comment_box.send_keys('Wowww! :)')
                                sleep(randint(3,7))
                            elif comm_prob == 7:
                                comment_box.send_keys('Liked!')
                                sleep(randint(3,7))
                            elif comm_prob == 8:
                                comment_box.send_keys('Ahha! (y)')
                                sleep(randint(3,7))
                            elif comm_prob == 9:
                                comment_box.send_keys('So cool! :)')
                                sleep(randint(3,7))
                            elif comm_prob == 10:
                                comment_box.send_keys('Beautiful pic~~')
                                sleep(randint(3,7))
                                
                            # Post comment by send Enter key
                            comment_box.send_keys(Keys.ENTER)
                            sleep(randint(4,9))

                    # Go to next picture after like, follow, comment
                    webdriver.find_element_by_link_text('Next').click()
                    sleep(randint(10,18))
                
                # If user already been followed, go to next picture in the same hashtag
                else:
                    sleep(randint(2,5))
                    webdriver.find_element_by_link_text('Next').click()
                    sleep(randint(5,12))
                    
        # Some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
        except:
            continue
    
    # Write list of user followed to csv
    for n in range(0,len(new_followed)):
        prev_user_list.append(new_followed[n])
        
    updated_user_df = pd.DataFrame(prev_user_list)
    updated_user_df.to_csv('users_followed_list.csv')
    print('Liked {} photos.'.format(likes))
    print('Commented {} photos.'.format(comments))
    print('Followed {} new people.'.format(followed))