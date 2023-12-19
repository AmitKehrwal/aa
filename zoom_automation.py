import asyncio
from playwright.async_api import async_playwright
import indian_names

# ... (other imports)

async def start(thread_name, wait_time, meetingcode, passcode):
    print(f"{thread_name} started!")

    async with async_playwright() as p:
        # Use --use-file-for-fake-audio-capture to simulate microphone input
        browser = await p.chromium.launch(
            headless=True,
            args=[
                '--use-fake-device-for-media-stream',
                '--use-fake-ui-for-media-stream',
                '--enable-logging',
                '--v=1',
                '--use-file-for-fake-audio-capture=/dev/snd/controlC0',
            ],
            executable_path="/usr/bin/brave-browser"
        )

        browser_type = p.chromium
        print(f"{thread_name} is using browser: {browser_type.name}")

        context = await browser.new_context()
        page = await context.new_page()

        # Generate a random username using the indian_names module
        user = indian_names.get_full_name()

        await page.goto(f'https://zoom.us/wc/join/{meetingcode}', timeout=200000)

        try:
            await page.click('//button[@id="onetrust-accept-btn-handler"]', timeout=5000)
        except Exception as e:
            pass

        try:
            await page.click('//button[@id="wc_agree1"]', timeout=5000)
        except Exception as e:
            pass

        try:
            await page.wait_for_selector('input[type="text"]', timeout=200000)
            await page.fill('input[type="text"]', user)
            await page.fill('input[type="password"]', passcode)
            join_button = await page.wait_for_selector('button.preview-join-button', timeout=200000)
            await join_button.click()
        except Exception as e:
            pass

        try:
            query = '//button[text()="Join Audio by Computer"]'
            await asyncio.sleep(13)
            mic_button_locator = await page.wait_for_selector(query, timeout=350000)
            await asyncio.sleep(10)
            await mic_button_locator.evaluate_handle('node => node.click()')
            print(f"{thread_name} mic aayenge.")
        except Exception as e:
            print(f"{thread_name} mic nahe aayenge. ", e)

        print(f"{thread_name} sleep for {wait_time} seconds ...")
        while wait_time > 0:
            await asyncio.sleep(1)
            wait_time -= 1
        print(f"{thread_name} ended!")

        await browser.close()

