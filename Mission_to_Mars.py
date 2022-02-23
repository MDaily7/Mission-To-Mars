# Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
# set up executable path 
executable_path = {'executable_path':ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
# create url variable
url = 'https://redplanetscience.com/'
# visit the mars  news site
browser.visit(url)
# optional delay for loading page
browser.is_element_present_by_css('div.list_text', wait_time=1)
# set up html parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
# scrape for the article title
slide_elem.find('div', class_='content_title')
# get just the text for the scraped element
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title
# use parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p
# visit images url
url_2 = 'https://spaceimages-mars.com/'
browser.visit(url_2)
# Find and click the 'Full Image' button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()
# parse the html with soup
html2 = browser.html
img_soup = soup(html2, 'html.parser')
# get the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel
# use base url to create absolute URL for the image
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url
# scrape a table of mars facts into a df
mars_facts_df = pd.read_html('https://galaxyfacts-mars.com')[0]
mars_facts_df.columns=['Description', 'Mars', 'Earth']
mars_facts_df.set_index('Description', inplace=True)
mars_facts_df
# conver the dataframe back to html
mars_facts_df.to_html()
# exit the automated browser
browser.quit()




