# here I am using selenium webdriver for web scrapping from facebook
from selenium import webdriver
import time
#sometime the website takes time to load due to javascript so will use time.sleep to avoid any errors
from secret import username,password,url
import pymongo
from pymongo import MongoClient



cluster = pymongo.MongoClient(url)
db=cluster["data"]
collection=db["collect"]




class Webscrapper:
    def __init__(self,email):
        d={}
        email_id=email
        d["_id"]=email
        path="C:\chromedriver.exe"
        driver_obj=webdriver.Chrome(path)
        #using mobile site of facebook due to frequently asking about notification on main facebook
        driver_obj.get("https://mobile.facebook.com")
        #finding login and password form
        username_element=driver_obj.find_element_by_id("m_login_email")
        password_element=driver_obj.find_element_by_id("m_login_password")
        #writing email and password
        username_element.send_keys(username)
        password_element.send_keys(password)
        submit_button=driver_obj.find_element_by_id("u_0_4")
        submit_button.click()
        time.sleep(2)
        #after login the website is always asking for whether to save password
        dont_save=driver_obj.find_element_by_class_name('_2pii')
        dont_save.click()
        time.sleep(2)
        #finding search button
        click_search=driver_obj.find_element_by_id('search_jewel')
        click_search.click()
        time.sleep(2)
        search=driver_obj.find_element_by_id('main-search-input')
        #writing email address in search form
        search.send_keys(email_id)
        time.sleep(2)
        search_send=driver_obj.find_element_by_class_name('_7msg')
        search_send.click()
        
        time.sleep(2)
        #clicking on person
        find_person=driver_obj.find_elements_by_class_name('_x0a')
        for i in find_person:
            if i.text=='People':
                i.click()
                break
        time.sleep(5)
        try:
            #the try is for if no person is found to return that search was unsuccessfull
            person=driver_obj.find_element_by_id('BrowseResultsContainer')
            person.click()
            time.sleep(2)
            try:
                #finding name
                person_name=driver_obj.find_elements_by_class_name('_6x2x')
                person_name=person_name[0].text
                d['name']=person_name
                
            except:
                pass
            time.sleep(2)
            try:
                #finding education
                person_about=driver_obj.find_element_by_class_name('_5b6s')
                person_about.click()
                time.sleep(2)
                education=driver_obj.find_element_by_id('education')
                education=education.text
                d['education']=education[11:]
            except:
                pass
            time.sleep(2)
            try:
                #finding work
                work=driver_obj.find_element_by_id('work')
                work= work.text
                d['work']=work[5:]
            except:
                pass
            time.sleep(2)
            try:
                #finding places lived
                places_lived=driver_obj.find_element_by_id('living')
                places_lived=places_lived.text
                d['places']=places_lived[13:]
            except:
                pass
            time.sleep(2)
            try:
                #finding life_events
                more_life=driver_obj.find_element_by_class_name('_49tq')
                more_life.click()
                time.sleep(2)
                life_events=driver_obj.find_element_by_id('year-overviews')
                life_events=life_events.text
                d['life_events']=life_events[12:]
            except:
                pass
            collection.insert_one(d)
        except:
            #if no person could be found
            print('could not find the person')
      
        
a=['anannyauberoi27@gmail.com','bhawanakarna5636@gmail.com','pratyushkumarkarna@gmaiil.com','vishalmahey2016@gmail.com']
#example
for i in a:
    
    obj1=Webscrapper(i)
        
                        
                        