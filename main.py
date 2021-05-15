##############################
#    WEB SCRAPPING
#   @By MathiasMendoza
##############################

#################
# IMPORT MODULES
#################
import time
from selenium import webdriver
import os
import io
import requests
import PillowImage
from PIL import Image


# BING AND SEARCH
bing = 'https://bing.com/images/search?q='
query = input('Search for: ')
url = bing + query

# Chrome Driver
driver = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
driver.get(url)


# Check if dir if not create it
dir = 'C:\\Users\\Useer\\Desktop\\Images\\' + query
if not os.path.isdir(dir):
    os.mkdir(dir)

# Scroll To The End of The Page
i = 0
while i <= 4:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(10)
    i+=1


# SAVE IMAGES
images = driver.find_elements_by_tag_name('img')
nro = 1
for img in images:
    try:
        src = img.get_attribute('src')
        image_content = requests.get(src).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = dir + '\\Image' + str(nro) + '.jpg'
        with open(file_path, 'wb') as f:
            image.save(f, 'JPEG', quality= 85)
        print("Success - saved {} on {}".format(src, file_path))
        nro+=1

    except Exception as e:
        print("Error - could not save image from url {} - {}".format(url, e))

