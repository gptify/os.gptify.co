import asyncio
from playwright.async_api import async_playwright
import os
import json

async def run_audit():
    results = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # 1. No horizontal scroll at 375px, 768px and 1280px
        h_scroll_res = {}
        console_errors = []
        tailwind_reqs = []
        
        for vp in [375, 768, 1280]:
            page = await browser.new_page(viewport={"width": vp, "height": 800})
            url = 'file:///' + os.path.abspath('deploy_os/index.html').replace('\\', '/')
            page.on("console", lambda msg: console_errors.append(f"{vp}px: {msg.type}: {msg.text}") if msg.type in ["error", "warning"] else None)
            page.on("request", lambda req: tailwind_reqs.append(req.url) if 'cdn.tailwindcss.com' in req.url else None)
            
            await page.goto(url)
            await page.wait_for_timeout(300)
            
            has_h_scroll = await page.evaluate("() => document.documentElement.scrollWidth > document.documentElement.clientWidth")
            h_scroll_res[vp] = has_h_scroll
            
            if vp == 1280:
                # 2. Homepage height under 6,000px
                body_h = await page.evaluate("() => document.body.scrollHeight")
                results['homepage_height'] = body_h
                
                # 3. Nav + hero fit in 800px height
                header_h = await page.evaluate("() => document.querySelector('header').getBoundingClientRect().height")
                hero_h = await page.evaluate("() => document.getElementById('top').getBoundingClientRect().height")
                results['nav_hero_height'] = header_h + hero_h
                
            if vp == 375:
                # 7b. Tap targets >= 44px on mobile
                bad_targets = await page.evaluate("""() => {
                    const els = Array.from(document.querySelectorAll('button, a, select, input'));
                    const bad = [];
                    for (const el of els) {
                        const rect = el.getBoundingClientRect();
                        if (rect.width > 0 && rect.height > 0 && (rect.height < 43.5 || rect.width < 43.5)) {
                            bad.push({ tag: el.tagName, id: el.id, class: el.className, text: el.innerText.trim(), w: rect.width, h: rect.height });
                        }
                    }
                    return bad;
                }""")
                results['small_targets_mobile'] = bad_targets
                
            await page.close()
            
        results['h_scroll'] = h_scroll_res
        results['console_errors'] = console_errors
        results['tailwind_requests'] = tailwind_reqs
        
        # 4. Calculator defaults and slider live updates
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        await page.goto('file:///' + os.path.abspath('deploy_os/index.html').replace('\\', '/'))
        val_year = await page.inner_text("#res-year-text")
        val_month = await page.inner_text("#res-month-text")
        val_hours = await page.inner_text("#res-hours-text")
        results['calc_defaults'] = {'year': val_year, 'month': val_month, 'hours': val_hours}
        
        await page.fill("#slider-team", "10")
        await page.dispatch_event("#slider-team", "input")
        val_year_10 = await page.inner_text("#res-year-text")
        results['calc_updated_10'] = val_year_10
        
        # 5. Industry tabs and keyboard Tab / Enter
        tab_switches = {}
        await page.focus('#tab-btn-clinic')
        await page.keyboard.press('Tab')
        focused_tab = await page.evaluate('() => document.activeElement.id')
        await page.keyboard.press('Enter')
        badge_edu = await page.inner_text('#ind-product-badge')
        tab_switches['keyboard_tab_enter'] = (focused_tab == 'tab-btn-edu' and 'EDUPRO' in badge_edu)
        
        await page.click("#tab-btn-auto")
        badge_auto = await page.inner_text("#ind-product-badge")
        tab_switches['auto'] = 'AUTOPRO' in badge_auto
        
        await page.click("#tab-btn-advisory")
        badge_adv = await page.inner_text("#ind-product-badge")
        tab_switches['advisory'] = 'ADVISORYPRO' in badge_adv
        
        await page.click("#tab-btn-clinic")
        badge_clinic = await page.inner_text("#ind-product-badge")
        tab_switches['clinic'] = 'MEDPRO' in badge_clinic
        results['industry_tabs'] = tab_switches
        
        # 7a. Text size >= 13px across pages
        small_text_all = {}
        for p_name in ['index.html', 'about.html', 'architecture.html']:
            p_check = await browser.new_page(viewport={"width": 1280, "height": 800})
            await p_check.goto('file:///' + os.path.abspath('deploy_os/' + p_name).replace('\\', '/'))
            st = await p_check.evaluate("""() => {
                const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
                const small = [];
                while (walker.nextNode()) {
                    const node = walker.currentNode;
                    const text = node.nodeValue.trim();
                    if (!text) continue;
                    const el = node.parentElement;
                    if (!el) continue;
                    const style = window.getComputedStyle(el);
                    if (style.display === 'none' || style.visibility === 'hidden') continue;
                    const fs = parseFloat(style.fontSize);
                    if (fs < 12.9) {
                        small.push({ tag: el.tagName, fs: fs, text: text.slice(0, 30) });
                    }
                }
                return small;
            }""")
            small_text_all[p_name] = len(st)
            await p_check.close()
        results['text_under_13px'] = small_text_all
        
        # 8. Reduced motion
        p_rm = await browser.new_page(viewport={"width": 1280, "height": 800})
        await p_rm.emulate_media(reduced_motion="reduce")
        await p_rm.goto('file:///' + os.path.abspath('deploy_os/index.html').replace('\\', '/'))
        anims = await p_rm.evaluate("""() => {
            const selectors = ['.tool-card-0', '.marquee-track', '.hero-chat-container'];
            const res = {};
            for (const s of selectors) {
                const el = document.querySelector(s);
                if (el) {
                    res[s] = window.getComputedStyle(el).animationName;
                }
            }
            return res;
        }""")
        results['reduced_motion_animations'] = anims
        await p_rm.close()
        
        # 9. Language rendering across EN, UZ, RU
        lang_h1s = {}
        for lang in ['en', 'uz', 'ru']:
            prefix = f"{lang}/" if lang != 'en' else ""
            p_lang = await browser.new_page(viewport={"width": 1280, "height": 800})
            
            # Home
            await p_lang.goto('file:///' + os.path.abspath(f'deploy_os/{prefix}index.html').replace('\\', '/'))
            h_home = await p_lang.inner_text("h1")
            
            # About
            await p_lang.goto('file:///' + os.path.abspath(f'deploy_os/{prefix}about.html').replace('\\', '/'))
            h_about = await p_lang.inner_text("h1")
            
            # Architecture
            await p_lang.goto('file:///' + os.path.abspath(f'deploy_os/{prefix}architecture.html').replace('\\', '/'))
            h_arch = await p_lang.inner_text("h1")
            
            lang_h1s[lang] = {'home': h_home[:35], 'about': h_about[:35], 'architecture': h_arch[:35]}
            await p_lang.close()
        results['languages'] = lang_h1s
        
        await browser.close()
        
    print("=== AUDIT SUMMARY ===")
    print(json.dumps(results, indent=2, ensure_ascii=False))

asyncio.run(run_audit())
