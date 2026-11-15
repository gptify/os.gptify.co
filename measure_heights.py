import subprocess
import time
import os
from playwright.sync_api import sync_playwright

# Start a local python http server in deploy_os on port 8765
server = subprocess.Popen(['python', '-m', 'http.server', '8765', '--directory', 'deploy_os'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)

try:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        
        # 1280px
        page = browser.new_page(viewport={'width': 1280, 'height': 800})
        page.goto('http://127.0.0.1:8765/')
        page.wait_for_load_state('networkidle')
        h_1280 = page.evaluate('document.documentElement.scrollHeight')
        
        sections_1280 = page.evaluate('''() => {
            return Array.from(document.querySelectorAll('section, header, footer')).map(s => ({
                id: s.id || s.tagName,
                height: s.offsetHeight
            }));
        }''')
        print(f"Height @ 1280px: {h_1280}px")
        for s in sections_1280:
            print(f"  {s['id']}: {s['height']}px")
            
        # 375px
        page2 = browser.new_page(viewport={'width': 375, 'height': 667})
        page2.goto('http://127.0.0.1:8765/')
        page2.wait_for_load_state('networkidle')
        h_375 = page2.evaluate('document.documentElement.scrollHeight')
        print(f"\nHeight @ 375px: {h_375}px")
        
        browser.close()
finally:
    server.terminate()

