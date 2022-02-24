# Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt
def scrape_all():
    #Inititate headless driver for deployment
    executable_path = {'executable_path':ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    news_title, news_paragraph = mars_news(browser)
    #run scrape functions and store results in dictionary
    data = {'news_title': news_title, 'news_paragraph': news_paragraph, 'featured_image': featured_image(browser), 'facts': mars_facts(), 'last_modified':dt.datetime.now()}
    #quit the browser and return the dictionary
    browser.quit()
    return data
def mars_news(browser):
    # create url variable
    url = 'https://redplanetscience.com/'
    # visit the mars  news site
    browser.visit(url)
    # optional delay for loading page
    browser.is_element_present_by_css('div.list_text', wait_time=1)
    # set up html parser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    try:

        slide_elem = news_soup.select_one('div.list_text')
         # get just the text for the scraped element
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # use parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    except AttributeError:
        return None, None
    return news_title, news_p
def featured_image(browser):
    # visit images url
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    # Find and click the 'Full Image' button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()
    # parse the html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    try:
        # get the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    except AttributeError:
        return None
    # use base url to create absolute URL for the image
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'           
    return img_url
# scrape a table of mars facts into a df
def mars_facts():
    try:
        mars_facts_df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None
    mars_facts_df.columns=['Description', 'Mars', 'Earth']
    mars_facts_df.set_index('Description', inplace=True)
    # convert the dataframe back to html
    return mars_facts_df.to_html(classes='table table-striped')
if __name__ =='__main__':
    print(scrape_all())




