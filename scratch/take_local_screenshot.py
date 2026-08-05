import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        # Launch headless browser
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1536, "height": 730})
        
        try:
            # Go to local server
            url = "http://localhost:8000/index.html"
            print(f"Navigating to {url}...")
            await page.goto(url)
            
            # Wait for 3 seconds for transitions/images to load
            await page.wait_for_timeout(3000)
            
            # Scroll to the local stories section
            selector = ".editorial-image-frame-wrapper"
            element = page.locator(selector)
            if await element.count() > 0:
                await element.scroll_into_view_if_needed()
                print("Scrolled to .editorial-image-frame-wrapper successfully.")
                
                # Take screenshot of the element
                output_path = "scratch/editorial_preview.png"
                await element.screenshot(path=output_path)
                print(f"Saved element screenshot to {output_path}")
            else:
                print("Element .editorial-image-frame-wrapper not found!")
                
        except Exception as e:
            print(f"Error during screenshot capture: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
