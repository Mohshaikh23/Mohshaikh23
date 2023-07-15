import asyncio
from PIL import Image
from pyppeteer import launch
import streamlit as st
import pandas as pd

async def capture_screenshot(url, output_filename):
    output_path = f'E:/END TO END ML PROJECT/Mohshaikh23/blogs_folder/blog_pics/{output_filename}.png'
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.screenshot({'path': output_path, 'type': 'png'})
    await browser.close()
    return output_path

# Capture screenshots and store the paths
async def screenshot_all(urls):
    screenshot_data = []
    for url, output_filename in urls:
        screenshot_path = await capture_screenshot(url, output_filename)
        screenshot_data.append(screenshot_path)
    return screenshot_data

def url_name(urls):
    word_before_html_list = [url.rsplit('/', 1)[-1].split('.html', 1)[0] for url, _ in urls]
    return word_before_html_list

def url_links(urls):
    url_list = [url for url, _ in urls]
    return url_list

def blog_frame(urls):
    loop = asyncio.get_event_loop()
    screenshot_data = loop.run_until_complete(screenshot_all(urls))
    word_before_html_list = url_name(urls)
    url_list = url_links(urls)
    
    data = {
        'screenshot_paths': screenshot_data,
        'blog_name': word_before_html_list,
        'blog_links': url_list
    }
    dataframe = pd.DataFrame(data)
    return dataframe



blog_data = [
    ('https://machinelearninginmind.blogspot.com/2023/07/demystifying-machine-learning-models.html',
     'screenshot1'),
    ('https://aiengineervsdatascientist.blogspot.com/2023/07/simplifying-mobile-phone-search.html',
     'screenshot2'),
    ('https://aiengineervsdatascientist.blogspot.com/2023/06/ai-engineer-vs-data-scientist.html', 
     'screenshot3')
]


# dataframe = blog_frame(urls = blog_data)
# dataframe.to_csv('blogs_folder/blog_data.csv')