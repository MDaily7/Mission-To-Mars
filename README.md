# Mission-To-Mars
## Overview
The goal of this project was to use splinter, beautifulsoup, and Mongo to learn about and gain experience with web scraping and the use of a non-relational database.
The initial work was done in jupyter notebook to assemble the scraping script piece by piece. To begin with, a news title and paragraph were scraped using splinter to navigate
to the website and beautifulsoup to parse the HTML so that the elements of interest could be extracted. The same tools were used again to scrape a featured image; in this case
splinter was used not just to open the webpage, but also to click a button on the page to get to the desired image, and beautifulsoup was used to parse the HTML and obtain the 
relative url of the image. Pandas read_html function was used to scrape a table from a third website into a dataframe. The columns of the dataframe were specified, and the index 
was set before the dataframe was converted back to HTML with df.to_html(). Finally, in the challenge portion of this project, a for loop was used in conjunction with splinter
and beautifulsoup to click various links on a webpage, scrape the images from the links page as well as the title of the image, and collect those elements as dictionaries into a 
list. Each of the scrapes were refactored into discrete functions and a scrape_all() function was defined to utilize each of the discrete scrape functions, and store their resulting
data into a dictionary. The scraping file was then called in the app.py file that uses flask to display the scrape results in a webpage; the scrape_all() function specifically 
was set to be called when the button (set up in the index.html file) was clicked. Additionally, when the button is clicked, the scraped results are added to the mongo database
which is connected to within the app.py file as well. 
## Resources
* Anaconda 4.11.0
* Python 3.7.11
* Various Webpages used:
	* News title and paragraph: https://redplanetscience.com/   
	* Featured Image: https://spaceimages-mars.com
	* Mars Facts Table: https://galaxyfacts-mars.com
	* Hemisphere Images and titles: https://marshemispheres.com/
* [Jupyter Notebook]() with all scrapes
* [Scraping Script]() with refactored scrapes
* [Flask app script]()
* [index.html]()


    
