from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.support.select import Select
sizes=["10","10.00","10.50","1000","11","11.00","11.5","11.50","1100","115","12","12.00","12.50","125","13","13.50","135","14.00","1400","145","155","16.00","165","175","185","195","205","215","225","23","235","24","245","255","265","275","285","295","305","315","325","335","345","355","365","375","385","395","415","425","435","445","455","475","495","525","6.00","7.00","7.50","8","8.25","8.5","9","9.00","9.5","9.50"]
profile=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100"]
options = webdriver.ChromeOptions()
w = webdriver.Chrome()
w.implicitly_wait(30)
w.get('https://reporting.tyrenet.net:81/price_lookup.php')
w.find_element_by_name('username').send_keys('your username')
w.find_element_by_name('password').send_keys('your password')
w.find_element_by_name('Submit').click()
w.get('https://reporting.tyrenet.net:81/price_lookup.php')
l= w.find_element_by_id("DateDropdown")
d= Select(l)
date=[]
#iterate over dropdown options
for opt in d.options:
#get option text
   date.append(opt.text)
#print(date)
for x in range(0,1):
    d.select_by_visible_text(date[x])
    w.find_element_by_id('NetworkDropdown1').click()
    w.find_element_by_id('LookupType1').click()
    for y in range(0,len(sizes)):
        sizeselect=Select(w.find_element_by_id('SizeDropdown'))
        sizeselect.select_by_visible_text(sizes[y])
        time.sleep(1)
        #profile
        profile=[]
        prof=Select(w.find_element_by_id('ProfileDropdown'))
        for profopt in prof.options:
            profile.append(profopt.text)
        profile.pop(0)
        final_profile=list(filter(None, profile))
        #print(final_profile)
        time.sleep(1)
        for z in range(0,len(final_profile)):
            prof.select_by_visible_text(final_profile[z])
            time.sleep(1)
            #rim
            rim=[]
            rimselect=Select(w.find_element_by_id('RimDropdown'))
            for rimopt in rimselect.options:
                rim.append(rimopt.text)
            rim.pop(0)
           # print(rim)
            time.sleep(1)
            for a in range(0,len(rim)):
                rimselect.select_by_visible_text(rim[a])
                time.sleep(1)
                #brand
                brand=[]
                brandslect=Select(w.find_element_by_id('BrandDropdown'))
                for brandopt in brandslect.options:
                    brand.append(brandopt.text)
                brand.pop(0)
                #print(brand)
                time.sleep(1)
                for b in range(0,len(brand)):
                    brandslect.select_by_visible_text(brand[b])
                    time.sleep(1)
                    #pattern
                    pattern=[]
                    patternselect=Select(w.find_element_by_id('PatternDropdown'))
                    for patternopt in patternselect.options:
                        pattern.append(patternopt.text)
                    pattern.pop(0)
                    #print(pattern)
                    time.sleep(1)
                    for c in range(0,len(pattern)):
                        patternselect.select_by_visible_text(pattern[c])
                        time.sleep(1)
                        try:
                            num_rows = len (w.find_elements_by_xpath('//*[@id="PriceDropdown"]/table/tbody/tr'))
                            num_cols=len(w.find_elements_by_xpath('//*[@id="PriceDropdown"]/table/tbody/tr[2]/td'))
                            for xtr in range(2,num_rows+1):
                                rows=[]
                                for ytr in range(1,num_cols+1):
                                        rval='//*[@id="PriceDropdown"]/table/tbody/tr[' +str(xtr)+ ']/td[' +str(ytr)+ ']'

                                        dname=w.find_element_by_xpath(rval).text
                                        rows.append(dname)
                                        #print(dname)
                            print(date[x]+","+"breakdown"+","+"Tyre"+","+sizes[y]+","+final_profile[z]+","+rim[a]+","+brand[b]+","+pattern[c],', '.join(rows))
                        except:
                            print("error")