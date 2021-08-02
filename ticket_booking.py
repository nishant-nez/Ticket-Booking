from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

PATH = 'C:\Program Files (x86)\chromedriver.exe'
# Replace this path with your chrome driver file location
driver = webdriver.Chrome(PATH)


def nepal_airlines():

    int_dom = input('International flight or Domestic?: ')

    if int_dom.lower() == 'international':
        print('Sorry, Internet booking engine (IBE) for International sectors is suspended until further notice.')
    else:
        driver.get('http://domestic.nepalairlines.com.np/nacOnline/faces/home.jspx')
        sleep(5)
        way = input('One way or Round Trip?: ')
        if way.lower() == 'round trip':
            radio_1 = driver.find_element_by_xpath('//*[@id="r1:0:sor1:_1"]').click()

        from_place = input('From? : ')
        from_drdw = Select(driver.find_element_by_xpath('//*[@id="r1:0:soc1::content"]'))
        from_drdw.select_by_visible_text(from_place.upper())

        to_place = input('Destination? : ')
        to_drdw = Select(driver.find_element_by_xpath('//*[@id="r1:0:soc2::content"]'))
        to_drdw.select_by_visible_text(to_place.upper())

        departure_dt = input('Departure Date? MM/DD/YYYY : ')
        driver.find_element_by_xpath('//*[@id="r1:0:id1::content"]').send_keys(departure_dt)

        if way == 'round trip':
            return_dt = input('Returning Date? MM/DD/YYYY : ')
            driver.find_element_by_xpath('//*[@id="r1:0:id2::content"]').send_keys(return_dt)

        adults = input('No of adults? : ')
        adults_no = Select(driver.find_element_by_xpath('//*[@id="r1:0:soc3::content"]'))
        adults_no.select_by_visible_text(adults)

        child = input('No of chlid? : ')
        child_no = Select(driver.find_element_by_xpath('//*[@id="r1:0:soc4::content"]'))
        child_no.select_by_visible_text(child)

        nationality = input("Your Nationality? Nepalese/Indian : ")
        nat_opt = Select(driver.find_element_by_xpath('//*[@id="r1:0:soc6::content"]'))
        nat_opt.select_by_visible_text(nationality)

        book_btn = driver.find_element_by_xpath('//*[@id="r1:0:cb1"]').click()


def buddha_air():
    driver.get('https://www.buddhaair.com/')
    sleep(2)


def yeti_airlines():
    driver.get('https://www.yetiairlines.com/')
    sleep(2)


air_choice = input('Enter your choice of airline: ')
if air_choice.lower() == 'nepal airlines':
    nepal_airlines()
elif air_choice.lower() == 'buddha air':
    buddha_air()
elif air_choice.lower() == 'yeti airlines':
    yeti_airlines()
else:
    print('Airlines not available yet!')
