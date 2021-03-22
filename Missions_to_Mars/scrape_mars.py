# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd


# %%

def scrape():

    from webdriver_manager.chrome import ChromeDriverManager
    executable_path = {"executable_path": ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)


    # %%
    #Visit the "NASA Mars News Site"
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)


    # %%



    # %%
    #Scrape the "NASA Mars News" Site
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    item_slide = soup.select_one("ul.item_list li.slide")
    item_slide.find("div", class_="content_title")
    news_title = item_slide.find("div", class_="content_title").get_text()
    news_p = soup.find('div', class_='article_teaser_body').text


    # %%
    #Print the lastest News Title and Description
    print(news_title)
    print(news_p)


    # %%
    # Visit the "JPL webpage"
    executable_path = {"executable_path": ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)
    url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(url)


    # %%
    #Click Full Image button, and find url
    jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'
    image_button = browser.find_by_css("button.btn.btn-outline-light")
    image_button.click()

    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_path = soup.select_one("div.fancybox-inner img").get('src')
    image_path


    # %%
    #Determine the complete URL for the Image page
    featured_image_url = jpl_url + image_path
    print(featured_image_url)


    # %%
    #Visit the MARS FACTS webpage
    executable_path = {"executable_path": ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)
    url = "https://space-facts.com/mars/"
    browser.visit(url)


    # %%
    tables = pd.read_html(url)
    MarsTable = tables[0]
    MarsTable.columns = ['Description', 'Value']
    MarsTable_html = MarsTable.to_html(table_id="html_tbl_css",justify='left',index=False)
    data = MarsTable.to_dict(orient='records')
    MarsTable

    # %% [markdown]
    # Part IV: Mars Hemisphere

    # %%
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # %%
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemi_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # %%
    items = soup.find_all('div', class_='item')

    image_urls = []

    main_url = 'https://astrogeology.usgs.gov'

    for i in items: 
        title = i.find('h3').text
        img_url_partial = i.find('a', class_='itemLink product-item')['href'] 
        
        browser.visit(main_url + img_url_partial)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        img_url = main_url + soup.find('img', class_='wide-image')['src']
    
        image_urls.append({"title" : title, "img_url" : img_url})
        
    image_urls

    mars_data = { "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image": featured_img_url,
        "mars_facts": MarsTable,
        "hemispheres": image_urls}

    browser.quit()
    return mars_data
