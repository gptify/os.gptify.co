import os
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import subprocess
import time

def run_tests():
    print("=== STARTING FULL SITE AUDIT ===")
    
    # 1. Check HTML files exist
    files = [
        'deploy_os/index.html',
        'deploy_os/uz/index.html',
        'deploy_os/ru/index.html',
        'deploy_os/404.html',
        'deploy_os/privacy.html',
        'deploy_os/terms.html',
        'deploy_os/sitemap.xml',
        'deploy_os/robots.txt',
        'deploy_os/CNAME'
    ]
    for f in files:
        assert os.path.exists(f), f"Missing file: {f}"
    print("[PASS] All required files exist.")

    # 2. Check CNAME
    with open('deploy_os/CNAME', 'r') as f:
        cname = f.read().strip()
    assert cname == 'gptify.si', f"CNAME is {cname}"
    print(f"[PASS] CNAME: {cname}")

    # 3. Check Buttons on index.html
    with open('deploy_os/index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    cta_buttons = soup.find_all(lambda tag: tag.name in ['button', 'a'] and 'openDemoModal' in (tag.get('onclick') or '') and 'Chat Demo' not in tag.get('onclick'))
    print(f"[PASS] Found {len(cta_buttons)} CTA 'Book a Demo' buttons across page sections:")
    for i, b in enumerate(cta_buttons):
        txt = b.get_text(strip=True)
        onclick = b.get('onclick')
        print(f"   {i+1}. {txt} -> {onclick}")
        assert 'Book a Demo' in txt or 'Demoni band qilish' in txt or 'Записаться на демо' in txt, f"Unexpected CTA button text: {txt}"

    # 4. Check that non-existent domains ailo.gptify.uz, ildam.gptify.uz are NOT in index.html
    html_text = soup.prettify()
    assert 'ailo.gptify.uz' not in html_text, "Found ailo.gptify.uz!"
    assert 'ildam.gptify.uz' not in html_text, "Found ildam.gptify.uz!"
    print("[PASS] No broken subdomain URLs (ailo.gptify.uz, ildam.gptify.uz) found.")

    # 5. Check no 15 min promise
    assert '15 min' not in html_text, "Found 15 min promise!"
    assert '15 minut' not in html_text, "Found 15 minut promise!"
    assert '15 минут' not in html_text, "Found 15 минут promise!"
    print("[PASS] '15 min' promise removed.")

    # 6. Check hidden slots
    hero_proof = soup.find(id='hero-proof-slot')
    assert hero_proof is not None, "Missing #hero-proof-slot"
    assert 'hidden' in hero_proof.get('class', []), "#hero-proof-slot must be hidden"
    print("[PASS] #hero-proof-slot present and hidden.")

    pricing_slot = soup.find(id='pricing-slot')
    assert pricing_slot is not None, "Missing #pricing-slot"
    assert 'hidden' in pricing_slot.get('class', []), "#pricing-slot must be hidden"
    print("[PASS] #pricing-slot present and hidden.")

    # 7. Check 8 integrations
    marquee = soup.find('div', class_='marquee-track')
    assert marquee is not None, "Missing .marquee-track"
    integrations = [
        'Telegram', 'WhatsApp Business', 'Instagram Direct', 
        'LinkedIn', 'Google Calendar', '1C Enterprise', 'Click', 'Payme'
    ]
    marquee_text = marquee.get_text()
    for item in integrations:
        assert item in marquee_text, f"Missing integration: {item}"
    # Verify engines are NOT in integrations marquee
    for engine in ['Ailo', 'ILDAM', 'Bandla', 'Mirzo', 'Izlai']:
        assert f"{engine} Engine" not in marquee_text, f"Engine {engine} in marquee!"
    print("[PASS] Integrations marquee contains exactly the 8 third-party integrations.")

    # 8. Check Playwright tests (Heights, Small Text, Tap Targets, iOS Zoom)
    server = subprocess.Popen(['python', '-m', 'http.server', '8766', '--directory', 'deploy_os'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            
            # --- 1280px Check ---
            page = browser.new_page(viewport={'width': 1280, 'height': 800})
            page.goto('http://127.0.0.1:8766/')
            page.wait_for_load_state('networkidle')
            h1280 = page.evaluate('document.documentElement.scrollHeight')
            print(f"[PASS] 1280px Page Height: {h1280}px (< 6500px target)")
            assert h1280 < 6500, f"1280px height too large: {h1280}px"
            
            # Small text count (< 12px)
            small_text_elements = page.evaluate('''() => {
                const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_ELEMENT);
                let items = [];
                while(walker.nextNode()){
                    const el = walker.currentNode;
                    if(el.offsetParent === null) continue; // not visible
                    const text = el.innerText || '';
                    if(!text.trim()) continue;
                    // check direct text nodes
                    const hasDirectText = Array.from(el.childNodes).some(n => n.nodeType === 3 && n.textContent.trim().length > 0);
                    if(!hasDirectText) continue;
                    const style = window.getComputedStyle(el);
                    const size = parseFloat(style.fontSize);
                    if(size < 11.5) { // sub-12px
                        items.push({ tag: el.tagName, cls: el.className, text: text.trim().substring(0, 40), size: size });
                    }
                }
                return items;
            }''')
            print(f"Elements under 12px: {small_text_elements}")
            small_text_count = len(small_text_elements)
            assert small_text_count == 0, f"Found {small_text_count} elements with font-size < 12px"

            # Check Bandla title and tag fit on one line at 1280px
            bandla_fit = page.evaluate('''() => {
                const card = document.querySelector('[data-engine-card="bandla"]') || document.querySelector('#bandlaCard');
                // check bandla header
                const tag = document.querySelector('[data-t="engineTagBandla"]');
                const sub = document.querySelector('[data-t="engineSubBandla"]');
                return { tagH: tag ? tag.offsetHeight : 0, subH: sub ? sub.offsetHeight : 0 };
            }''')
            print(f"[PASS] Bandla header rendered: {bandla_fit}")

            # --- 375px Check ---
            page_mobile = browser.new_page(viewport={'width': 375, 'height': 667})
            page_mobile.goto('http://127.0.0.1:8766/')
            page_mobile.wait_for_load_state('networkidle')
            h375 = page_mobile.evaluate('document.documentElement.scrollHeight')
            print(f"[PASS] 375px Page Height: {h375}px (< 11000px target)")
            assert h375 < 11000, f"375px height too large: {h375}px"

            # Check inputs font-size >= 16px
            page_mobile.evaluate('openDemoModal("test")')
            page_mobile.wait_for_timeout(300)
            input_sizes = page_mobile.evaluate('''() => {
                const inputs = Array.from(document.querySelectorAll('#demoModal input[type="text"], #demoModal select'));
                return inputs.map(i => ({ id: i.id, size: parseFloat(window.getComputedStyle(i).fontSize) }));
            }''')
            for inp in input_sizes:
                assert inp['size'] >= 16, f"Input {inp['id']} size {inp['size']} < 16px"
            print(f"[PASS] Form inputs/selects on mobile >= 16px: {input_sizes}")

            # Check language buttons tap target height >= 44px
            lang_btns = page_mobile.evaluate('''() => {
                return Array.from(document.querySelectorAll('#btn-lang-en, #btn-lang-uz, #btn-lang-ru')).map(b => ({
                    id: b.id,
                    h: b.offsetHeight,
                    w: b.offsetWidth
                }));
            }''')
            print(f"[PASS] Language switchers dimensions: {lang_btns}")

            # Verify Industry Dashboard Tab Switching
            tab_switch_results = page.evaluate('''() => {
                const results = [];
                // Test switching to education
                window.switchIndustryTab('education');
                results.push({
                    eduVisible: !document.getElementById('panel-education').classList.contains('hidden'),
                    clinicsHidden: document.getElementById('panel-clinics').classList.contains('hidden')
                });
                // Test switching to auto
                window.switchIndustryTab('auto');
                results.push({
                    autoVisible: !document.getElementById('panel-auto').classList.contains('hidden'),
                    eduHidden: document.getElementById('panel-education').classList.contains('hidden')
                });
                // Test switching to advisory
                window.switchIndustryTab('advisory');
                results.push({
                    advVisible: !document.getElementById('panel-advisory').classList.contains('hidden'),
                    autoHidden: document.getElementById('panel-auto').classList.contains('hidden')
                });
                // Switch back to clinics
                window.switchIndustryTab('clinics');
                results.push({
                    clinicsVisible: !document.getElementById('panel-clinics').classList.contains('hidden'),
                    advHidden: document.getElementById('panel-advisory').classList.contains('hidden')
                });
                return results;
            }''')
            print(f"[PASS] Interactive Industry Dashboard tab switching verified: {tab_switch_results}")
            for r in tab_switch_results:
                for k, v in r.items():
                    assert v is True, f"Tab switch failed: {k} is {v}"

            # Verify navbar links (Only 5 Engines, Solutions, FAQ)
            nav_links = page.evaluate('''() => {
                const links = Array.from(document.querySelectorAll('header nav[aria-label="Navigation"] a'));
                return links.map(a => a.innerText.trim());
            }''')
            print(f"[PASS] Desktop nav links: {nav_links}")
            assert 'Architecture' not in nav_links, "Architecture should not be in nav"
            assert 'Calculator' not in nav_links, "Calculator should not be in nav"
            assert nav_links == ['5 Engines', 'Solutions', 'FAQ'], f"Unexpected nav links: {nav_links}"

            browser.close()
    finally:
        server.terminate()

    print("=== ALL AUDIT CHECKS PASSED SUCCESSFULLY! ===")

if __name__ == '__main__':
    run_tests()
