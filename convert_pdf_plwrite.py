import asyncio
import os
from playwright.async_api import async_playwright

import base64

base64_string = ""

with open("logo.png", "rb") as image_file:
    base64_string = base64.b64encode(image_file.read()).decode('utf-8')

print(base64_string)


async def html_file_to_pdf_with_header_footer(html_file_path, output_path, header_html, footer_html):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Open the local HTML file
        html_file_url = f'file://{html_file_path}'
        await page.goto(html_file_url)

        # Set up header and footer
        await page.emulate_media(media="screen")
        await page.pdf(
            path=output_path,
            display_header_footer=True,
            header_template=header_html,
            footer_template=footer_html,
            format="A4"  # Adjust as needed
        )
        await browser.close()

# Example usage
html_file_path = os.path.abspath("a copy.html") # Replace with the path to your HTML file
output_path = 'html-to-pdf-output.pdf'

header_html = """
            <style>
                #divHeader {
                    display: flex;
                    height: auto;
                    justify-content: space-between;
                    align-items:center;            
                    border-bottom: 2px solid #413a97;
                }
                #logo {        
                    max-width:150px;
                }
                #tcid 
                    font-size: 10px;
                    margin-left: auto;
                    margin-right: 0;
                }
            </style>
            <div id="divHeader">
                <img id="logo" src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB1gAAAOSCAYAAADZNQL4AAAABGdBTUEAALGPC/xhBQAACktpQ0NQc1JHQiBJRUM2MTk2Ni0yLjEAAEiJnVNnVFPpFj333vRCS4iAlEtvUhUIIFJCi4BUaaISkgChhBgSQOyIqMCIoiKCFRkUccDREZCxIoqFQbH3AXkIKOPgKDZU3g/eGn2z5r03b/avvfY5Z53vnH0+AEZgsESahaoBZEoV8ogAHzw2Lh4ndwMKVCCBA4BAmC0LifSPAgDg+/Hw7IgAH/gCBODNbUAAAG' alt="Logo">
                <h1 id = "tcid">TCID-11221121</h1>
            </div>"""

footer_html = '''
<div style="font-size:10px; text-align:center; width:100%;">
    <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
</div>
'''

asyncio.run(html_file_to_pdf_with_header_footer(html_file_path, output_path, header_html, footer_html))
