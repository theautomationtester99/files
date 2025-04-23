import asyncio
import os
from pyppeteer import launch
import pyppeteer
import base64

from generate_html import generate_html
from generate_html import generate_html1

rev = pyppeteer.__chromium_revision__
print(rev)

base64_string = ""
with open("logo.png", "rb") as image_file:
    base64_string = base64.b64encode(image_file.read()).decode('utf-8')

async def main():
    html_content = generate_html()
    
    #head_template = '<style>@divHeader{width: 2500px;height:auto;align-items:center;border-bottom:2px solid #413a97;} #logo{max-width:100px;} #tcid{margin-left:auto;margin-right:0;}</style><div id="divHeader"><img id="logo"src="data:image/png;base64,'+base64_string+'"alt="Logo"><hr></hr></div>'
    # head_template = '<div style="display: flex; width: 100%; margin:0; padding:0; height: auto; justify-content: space-between; align-items: center; border-bottom: 2px solid #413a97;"><div style="flex: 0;margin-left: 5px;"><img id="logo" src="data:image/png;base64,'+base64_string+'" alt="Logo" style="max-height: 99px;object-fit: contain;"></div><div id="tcid" style="flex: 0;font-size:10px;white-space: nowrap;margin-right: 20px;"><h1>TCID-11221121</h1></div></div>'
    head_template = '<div style="display: flex; width: 100%; height: auto; justify-content: space-between; align-items: center; border-bottom: 2px solid #413a97; margin: 0; padding: 0;"><div style="flex: 0;margin-left: 5px;margin-top: 0;"><img id="logo" src="data:image/png;base64,'+base64_string+'" alt="Logo" style="max-height: 60px;object-fit: contain;"></div><div id="tcid" style="flex: 0;font-size:10px;white-space: nowrap;margin-right: 20px;"><h1 style="margin: 0; padding: 0;">TCID-11221121</h1></div></div>'

    browser = await launch({"headless": True})
    print(await browser.version())
    page = await browser.newPage()
    
    # # Replace this with the path to your local HTML file
    # file_path = os.path.abspath("a copy.html")
    # local_url = f"file://{file_path}"
    
    # await page.goto(local_url)
    
    await page.setContent(html_content)
    
    # Set PDF options for A4 size
    await page.pdf({
        "path": "output.pdf",
        "format": "Letter",
        "printBackground": True,  # Include background graphics
        "landscape": True,
        "margin": {
            "top": 86,
            "bottom": 5,
            "left": 25,
            "right": 25
        },
        "displayHeaderFooter": True,
        "headerTemplate": head_template,
        "footerTemplate": """
            <div style='font-size:10px; width:100%; text-align:center;'>
                Page <span class="pageNumber"></span> of <span class="totalPages"></span>
            </div>
        """
        
    })
    
    await browser.close()

asyncio.run(main())