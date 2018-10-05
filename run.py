from selenium import webdriver

browser = webdriver.Firefox()

# LOGGING IN
browser.get('https://www.dice.com/dashboard/login')
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("password")

username.send_keys("email address") # enter email address here
password.send_keys("password") # enter password here

browser.find_element_by_xpath("//button[@type='submit']").click()
print('Logged In..')


browser.get('https://www.dice.com/jobs?q=QA+Engineer&l=')

# job listing
listings = browser.find_elements_by_xpath('/html[1]/body[1]/div[8]/div[3]/div[2]/div[2]/div[1]/div[1]/div[*]')
# listings is a list with 30 elements
for i in range(0, len(listings)):
    li = browser.find_elements_by_xpath('/html[1]/body[1]/div[8]/div[3]/div[2]/div[2]/div[1]/div[1]/div['+ str(i) + ']//li')
    if len(li) == 9:
        print('EASY APPLY!')
        company_name_elem = browser.find_element_by_xpath('/html[1]/body[1]/div[8]/div[3]/div[2]/div[2]/div[1]/div[1]/div['+ str(i) + ']/div[1]/ul[1]/li[1]/h3[1]/a[1]/span[1]')
        company_name = company_name_elem.text
        print(company_name)
        browser.find_element_by_xpath('/html[1]/body[1]/div[8]/div[3]/div[2]/div[2]/div[1]/div[1]/div['+ str(i) + ']//a').click()


        # On the job page - time to click apply
        browser.find_element_by_xpath("//div[@class='pull-right hidden-xs']//button[@id='applybtn-2']").click()
        print ('Apply Time!')
        browser.find_element_by_xpath("//span[@class='bfh-selectbox-option'][contains(text(),'choose one')]").click()
        browser.find_element_by_xpath("//a[contains(text(),'QA Engineer(Last Updated: 10/03/2018)')]").click()
        browser.find_element_by_xpath("//button[@id='submit-job-btn']").click()
        print ('Job Successfully Applied!')
