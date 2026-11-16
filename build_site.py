# -*- coding: utf-8 -*-
"""
build_site.py
Generates the complete static website in deploy_os using translations_all.json.
Output files:
  - deploy_os/style.min.css
  - deploy_os/index.html (EN)
  - deploy_os/uz/index.html (UZ)
  - deploy_os/ru/index.html (RU)
  - deploy_os/about.html (EN)
  - deploy_os/uz/about.html (UZ)
  - deploy_os/ru/about.html (RU)
  - deploy_os/architecture.html (EN)
  - deploy_os/uz/architecture.html (UZ)
  - deploy_os/ru/architecture.html (RU)
  - deploy_os/404.html
  - deploy_os/sitemap.xml
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRANS_JSON = os.path.join(BASE_DIR, 'translations_all.json')

with open(TRANS_JSON, encoding='utf-8') as f:
    T = json.load(f)

SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzM3GZEDsWDc-3SUI4sySAWnJFn6ZolQaYkwo7W4VWG-79J3WVLYeQL7qs5jgAtkK_C_g/exec"

def get_css():
    return """/* GPTify OS Design System Stylesheet */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@600;700&display=swap');

:root {
  --color-page: #FFFFFF;
  --color-tint: #F3F8F7;
  --color-lines: #DCE8E6;
  --color-text: #172B2A;
  --color-secondary: #5F6F6D;
  --color-teal: #087F6A;
  --color-teal-hover: #056453;
  --color-lime: #B7F34A;
  --color-dark: #172B2A;
}

*, *::before, *::after {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
  font-size: 16px;
  overflow-x: hidden;
  max-width: 100vw;
}

body {
  margin: 0;
  padding: 0;
  background: var(--color-page);
  color: var(--color-text);
  font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 16px;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
  max-width: 100vw;
}

h1, h2, h3, h4, h5, h6, .font-heading {
  font-family: 'Poppins', 'Inter', system-ui, sans-serif;
  color: var(--color-text);
  line-height: 1.15;
}

a {
  color: var(--color-teal);
  text-decoration: none;
  transition: color 0.15s ease;
}

a:hover {
  color: var(--color-teal-hover);
}

button {
  font-family: 'Poppins', 'Inter', system-ui, sans-serif;
  font-size: 16px;
  cursor: pointer;
  border: none;
}

button, a.btn, input[type="button"], input[type="submit"], .tab-btn {
  min-height: 44px;
}

input, select, textarea {
  font-size: 16px !important;
  font-family: 'Inter', system-ui, sans-serif;
}

/* Keyframe Animations */
@keyframes inA {
  0%, 3% { opacity: 0; transform: translateY(12px); }
  8%, 93% { opacity: 1; transform: translateY(0); }
  100% { opacity: 0; transform: translateY(0); }
}

@keyframes inB {
  0%, 17% { opacity: 0; transform: translateY(12px); }
  22%, 93% { opacity: 1; transform: translateY(0); }
  100% { opacity: 0; transform: translateY(0); }
}

@keyframes inC {
  0%, 33% { opacity: 0; transform: translateY(12px); }
  38%, 93% { opacity: 1; transform: translateY(0); }
  100% { opacity: 0; transform: translateY(0); }
}

@keyframes inD {
  0%, 47% { opacity: 0; transform: scale(0.92); }
  52%, 93% { opacity: 1; transform: scale(1); }
  100% { opacity: 0; transform: scale(1); }
}

@keyframes inE {
  0%, 57% { opacity: 0; transform: scale(0.92); }
  62%, 93% { opacity: 1; transform: scale(1); }
  100% { opacity: 0; transform: scale(1); }
}

@keyframes inF {
  0%, 67% { opacity: 0; transform: scale(0.92); }
  72%, 93% { opacity: 1; transform: scale(1); }
  100% { opacity: 0; transform: scale(1); }
}

@keyframes marq {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}

@keyframes lit {
  0%, 100% { filter: brightness(1); }
  50% { filter: brightness(1.15); }
}

/* Reduced Motion Override */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation: none !important;
    transition: none !important;
  }
}

/* Sliders */
input[type="range"] {
  -webkit-appearance: none;
  width: 100%;
  height: 44px;
  background: transparent;
  outline: none;
  cursor: pointer;
  margin: 0;
}

input[type="range"]::-webkit-slider-runnable-track {
  width: 100%;
  height: 8px;
  background: var(--color-lines);
  border-radius: 999px;
}

input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: var(--color-teal);
  box-shadow: 0 2px 6px rgba(8, 127, 106, 0.4);
  cursor: pointer;
  margin-top: -9px;
  transition: transform 0.1s ease;
}

input[type="range"]::-webkit-slider-thumb:hover {
  transform: scale(1.12);
}

input[type="range"]::-moz-range-track {
  width: 100%;
  height: 8px;
  background: var(--color-lines);
  border-radius: 999px;
}

input[type="range"]::-moz-range-thumb {
  width: 26px;
  height: 26px;
  border: none;
  border-radius: 50%;
  background: var(--color-teal);
  box-shadow: 0 2px 6px rgba(8, 127, 106, 0.4);
  cursor: pointer;
}

/* Tool Rail Active Glow Stagger */
.tool-card-0 { animation: lit 10s ease-in-out infinite; animation-delay: 0s; }
.tool-card-1 { animation: lit 10s ease-in-out infinite; animation-delay: 2s; }
.tool-card-2 { animation: lit 10s ease-in-out infinite; animation-delay: 4s; }
.tool-card-3 { animation: lit 10s ease-in-out infinite; animation-delay: 6s; }
.tool-card-4 { animation: lit 10s ease-in-out infinite; animation-delay: 8s; }

/* FAQ Details */
details {
  border-bottom: 1px solid var(--color-lines);
  background: #FFFFFF;
}
summary {
  list-style: none;
  padding: 22px 0;
  font-family: 'Poppins', 'Inter', system-ui, sans-serif;
  font-size: 19px;
  font-weight: 600;
  color: var(--color-text);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 44px;
  user-select: none;
}
summary::-webkit-details-marker {
  display: none;
}
summary .faq-icon {
  width: 24px;
  height: 24px;
  flex: none;
  border-radius: 50%;
  background: var(--color-tint);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.2s ease, background 0.2s ease;
}
details[open] summary .faq-icon {
  transform: rotate(45deg);
  background: var(--color-lime);
  color: var(--color-dark);
}
.faq-body {
  padding: 0 0 22px;
  font-size: 17px;
  line-height: 1.6;
  color: var(--color-secondary);
  max-width: 820px;
}

/* Modal Overlay & Card */
.modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 999;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 16px;
  background: rgba(23, 43, 42, 0.65);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  overflow-y: auto;
}
.modal-overlay.active {
  display: flex;
}
.modal-card {
  position: relative;
  background: #FFFFFF;
  border-radius: 20px;
  border: 1px solid var(--color-lines);
  box-shadow: 0 20px 48px rgba(23, 43, 42, 0.2);
  max-width: 540px;
  width: 100%;
  padding: 28px;
  margin: auto;
  max-height: 94vh;
  overflow-y: auto;
}
.modal-close {
  position: absolute;
  top: 16px;
  right: 16px;
  width: 44px;
  height: 44px;
  min-width: 44px;
  min-height: 44px;
  border-radius: 50%;
  background: var(--color-tint);
  border: 1px solid var(--color-lines);
  color: var(--color-text);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.15s ease;
}
.modal-close:hover {
  background: #e2edea;
}
"""

def generate_header(lang, current_page='home'):
    prefix = '/uz/' if lang == 'uz' else ('/ru/' if lang == 'ru' else '/')
    about_url = f"{prefix}about.html" if lang != 'en' else "/about.html"
    home_url = f"{prefix}" if current_page in ['about', 'arch'] else "#top"
    
    if current_page == 'about':
        url_en = "/about.html"
        url_uz = "/uz/about.html"
        url_ru = "/ru/about.html"
    elif current_page == 'arch':
        url_en = "/architecture.html"
        url_uz = "/uz/architecture.html"
        url_ru = "/ru/architecture.html"
    else:
        url_en = "/"
        url_uz = "/uz/"
        url_ru = "/ru/"
        
    tools_href = f"{prefix}#tools" if current_page in ['about', 'arch'] else "#tools"
    ind_href = f"{prefix}#industries" if current_page in ['about', 'arch'] else "#industries"
    sav_href = f"{prefix}#savings" if current_page in ['about', 'arch'] else "#savings"
    faq_href = f"{prefix}#faq" if current_page in ['about', 'arch'] else "#faq"

    en_active = 'background: #F3F8F7; font-weight: 600; color: #172B2A;' if lang == 'en' else 'color: #5F6F6D; font-weight: 500;'
    uz_active = 'background: #F3F8F7; font-weight: 600; color: #172B2A;' if lang == 'uz' else 'color: #5F6F6D; font-weight: 500;'
    ru_active = 'background: #F3F8F7; font-weight: 600; color: #172B2A;' if lang == 'ru' else 'color: #5F6F6D; font-weight: 500;'

    about_active_style = 'color: #087F6A; font-weight: 600;' if current_page == 'about' else 'color: #172B2A; font-weight: 500;'

    return f"""<header style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px 20px; padding: 14px clamp(16px, 2.5vw, 40px); border-bottom: 1px solid #DCE8E6; background: #FFFFFF; position: sticky; top: 0; z-index: 100;">
  <a href="{home_url}" aria-label="GPTify OS home" style="display: flex; align-items: center; gap: 12px; min-height: 44px; text-decoration: none; color: #172B2A; flex-shrink: 0">
    <svg aria-hidden="true" width="38" height="38" viewBox="0 0 100 100" fill="none"><path fill="#087F6A" d="M51.4 9 A41 41 0 1 0 88 65.4 V42 H47 V58 H73.7 A25 25 0 1 1 50.9 25 Z"></path><path fill="#B7F34A" d="M61 9 H88 V36 H78 V19 H61 Z"></path></svg>
    <span style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 24px; letter-spacing: -0.01em">GPTify</span>
    <span style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 13px; color: #FFFFFF; background: #087F6A; border-radius: 6px; padding: 3px 8px">{T[lang]['nav_logo_sub']}</span>
  </a>
  <nav aria-label="Main" style="display: flex; flex-wrap: wrap; align-items: center; gap: 4px 14px">
    <a href="{tools_href}" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; min-width: 44px; padding: 0 8px; font-size: 15px; font-weight: 500; color: #172B2A; text-decoration: none">{T[lang]['nav_tools']}</a>
    <a href="{ind_href}" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; min-width: 44px; padding: 0 8px; font-size: 15px; font-weight: 500; color: #172B2A; text-decoration: none">{T[lang]['nav_industries']}</a>
    <a href="{faq_href}" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; min-width: 44px; padding: 0 8px; font-size: 15px; font-weight: 500; color: #172B2A; text-decoration: none">{T[lang]['nav_faq']}</a>
    <a href="{about_url}" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; min-width: 44px; padding: 0 8px; font-size: 15px; text-decoration: none; {about_active_style}">{T[lang]['nav_about']}</a>
  </nav>
  <div style="display: flex; align-items: center; gap: 12px; margin-left: auto; flex-shrink: 0">
    <div style="display: flex; align-items: center; gap: 4px" role="navigation" aria-label="Language selection">
      <a href="{url_en}" aria-current="{'true' if lang == 'en' else 'false'}" style="display: inline-flex; align-items: center; justify-content: center; min-width: 44px; min-height: 44px; font-size: 14px; border-radius: 10px; text-decoration: none; {en_active}">{T[lang]['nav_lang_en']}</a>
      <a href="{url_uz}" aria-current="{'true' if lang == 'uz' else 'false'}" style="display: inline-flex; align-items: center; justify-content: center; min-width: 44px; min-height: 44px; font-size: 14px; border-radius: 10px; text-decoration: none; {uz_active}">{T[lang]['nav_lang_uz']}</a>
      <a href="{url_ru}" aria-current="{'true' if lang == 'ru' else 'false'}" style="display: inline-flex; align-items: center; justify-content: center; min-width: 44px; min-height: 44px; font-size: 14px; border-radius: 10px; text-decoration: none; {ru_active}">{T[lang]['nav_lang_ru']}</a>
    </div>
    <button onclick="openDemoModal('Header Nav')" style="display: inline-flex; align-items: center; justify-content: center; min-height: 48px; min-width: 44px; padding: 0 18px; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 15px; border-radius: 10px; text-decoration: none; border: none; cursor: pointer; white-space: nowrap">{T[lang]['nav_cta']}</button>
  </div>
</header>"""

def generate_footer(lang):
    prefix = '/uz/' if lang == 'uz' else ('/ru/' if lang == 'ru' else '/')
    about_url = f"{prefix}about.html" if lang != 'en' else "/about.html"
    arch_url = f"{prefix}architecture.html" if lang != 'en' else "/architecture.html"
    return f"""<footer style="border-top: 1px solid #DCE8E6; padding: 36px clamp(20px, 5vw, 80px) 44px; display: flex; flex-wrap: wrap; align-items: flex-start; justify-content: space-between; gap: 24px 48px">
  <div style="display: flex; flex-direction: column; gap: 10px; max-width: 360px">
    <div style="display: flex; align-items: center; gap: 10px">
      <svg aria-hidden="true" width="30" height="30" viewBox="0 0 100 100" fill="none"><path fill="#087F6A" d="M51.4 9 A41 41 0 1 0 88 65.4 V42 H47 V58 H73.7 A25 25 0 1 1 50.9 25 Z"></path><path fill="#B7F34A" d="M61 9 H88 V36 H78 V19 H61 Z"></path></svg>
      <span style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 20px; color: #172B2A">GPTify OS</span>
    </div>
    <div style="font-size: 15px; line-height: 1.5; color: #5F6F6D">{T[lang]['footer_tagline']}</div>
  </div>
  <nav aria-label="Footer" style="display: flex; flex-wrap: wrap; gap: 4px 28px">
    <a href="{about_url}" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; min-width: 44px; font-size: 15px; font-weight: 500; color: #172B2A">{T[lang]['footer_about']}</a>
    <a href="/privacy.html" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; min-width: 44px; font-size: 15px; font-weight: 500; color: #172B2A">{T[lang]['footer_privacy']}</a>
    <a href="/terms.html" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; min-width: 44px; font-size: 15px; font-weight: 500; color: #172B2A">{T[lang]['footer_terms']}</a>
    <a href="{arch_url}" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; min-width: 44px; font-size: 15px; font-weight: 500; color: #172B2A">{T[lang]['footer_security']}</a>
  </nav>
  <div style="flex: 1 1 100%; font-size: 14px; color: #5F6F6D">{T[lang]['footer_rights']}</div>
</footer>"""

def generate_modal(lang):
    close_label = T[lang].get('modal_close', 'Close')
    modal_html = f"""<div id="demoModal" class="modal-overlay" onclick="if(event.target===this)closeDemoModal()" role="dialog" aria-modal="true" aria-labelledby="modalTitle">
  <div class="modal-card">
    <button type="button" class="modal-close" onclick="closeDemoModal()" aria-label="{close_label}">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
    </button>
    
    <div id="modalLeadFormContainer">
      <div style="margin-bottom: 20px">
        <h3 id="modalTitle" style="margin: 0 0 6px 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 24px; font-weight: 700; color: #172B2A">{T[lang]['modal_title']}</h3>
        <p style="margin: 0; font-size: 15px; color: #5F6F6D">{T[lang]['modal_subtitle']}</p>
      </div>
      
      <form id="leadForm" onsubmit="handleLeadSubmit(event)" style="display: flex; flex-direction: column; gap: 14px">
        <input type="hidden" id="modalLeadInterest" name="interest" value="General">
        
        <div>
          <label for="leadName" style="display: block; font-size: 14px; font-weight: 600; color: #172B2A; margin-bottom: 6px">{T[lang]['modal_name_label']}</label>
          <input type="text" id="leadName" name="name" required autocomplete="name" placeholder="{T[lang]['modal_name_ph']}" style="width: 100%; min-height: 46px; border: 1px solid #DCE8E6; border-radius: 10px; padding: 10px 14px; font-size: 16px; color: #172B2A; background: #FFFFFF; outline: none">
        </div>
        
        <div>
          <label for="leadCompany" style="display: block; font-size: 14px; font-weight: 600; color: #172B2A; margin-bottom: 6px">{T[lang]['modal_company_label']}</label>
          <input type="text" id="leadCompany" name="company" required autocomplete="organization" placeholder="{T[lang]['modal_company_ph']}" style="width: 100%; min-height: 46px; border: 1px solid #DCE8E6; border-radius: 10px; padding: 10px 14px; font-size: 16px; color: #172B2A; background: #FFFFFF; outline: none">
        </div>
        
        <div>
          <label for="leadContact" style="display: block; font-size: 14px; font-weight: 600; color: #172B2A; margin-bottom: 6px">{T[lang]['modal_phone_label']}</label>
          <input type="text" id="leadContact" name="contact" required autocomplete="tel" placeholder="{T[lang]['modal_phone_ph']}" style="width: 100%; min-height: 46px; border: 1px solid #DCE8E6; border-radius: 10px; padding: 10px 14px; font-size: 16px; color: #172B2A; background: #FFFFFF; outline: none">
        </div>
        
        <div style="display: flex; flex-direction: column; gap: 14px">
          <div>
            <label for="leadTeamSize" style="display: block; font-size: 14px; font-weight: 600; color: #172B2A; margin-bottom: 6px">{T[lang]['modal_team_label']}</label>
            <select id="leadTeamSize" name="teamSize" style="width: 100%; min-height: 46px; border: 1px solid #DCE8E6; border-radius: 10px; padding: 10px 14px; font-size: 16px; color: #172B2A; background: #FFFFFF; outline: none">
              <option value="1-5">{T[lang]['modal_team_opt_1']}</option>
              <option value="6-15" selected>{T[lang]['modal_team_opt_2']}</option>
              <option value="16-50">{T[lang]['modal_team_opt_3']}</option>
              <option value="50+">{T[lang]['modal_team_opt_4']}</option>
            </select>
          </div>
          
          <div>
            <label style="display: block; font-size: 14px; font-weight: 600; color: #172B2A; margin-bottom: 6px">{T[lang]['modal_channels_label']}</label>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px">
              <label style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 500; color: #172B2A; background: #F3F8F7; padding: 10px 12px; border-radius: 8px; border: 1px solid #DCE8E6; cursor: pointer; min-height: 44px">
                <input type="checkbox" name="channels" value="Telegram" checked style="accent-color: #087F6A; width: 18px; height: 18px"> {T[lang]['modal_ch_tg']}
              </label>
              <label style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 500; color: #172B2A; background: #F3F8F7; padding: 10px 12px; border-radius: 8px; border: 1px solid #DCE8E6; cursor: pointer; min-height: 44px">
                <input type="checkbox" name="channels" value="WhatsApp" checked style="accent-color: #087F6A; width: 18px; height: 18px"> {T[lang]['modal_ch_wa']}
              </label>
              <label style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 500; color: #172B2A; background: #F3F8F7; padding: 10px 12px; border-radius: 8px; border: 1px solid #DCE8E6; cursor: pointer; min-height: 44px">
                <input type="checkbox" name="channels" value="Instagram" checked style="accent-color: #087F6A; width: 18px; height: 18px"> {T[lang]['modal_ch_ig']}
              </label>
              <label style="display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 500; color: #172B2A; background: #F3F8F7; padding: 10px 12px; border-radius: 8px; border: 1px solid #DCE8E6; cursor: pointer; min-height: 44px">
                <input type="checkbox" name="channels" value="Calls" style="accent-color: #087F6A; width: 18px; height: 18px"> {T[lang]['modal_ch_calls']}
              </label>
            </div>
          </div>
        </div>
        
        <button type="submit" id="btnModalSubmit" style="width: 100%; min-height: 48px; border-radius: 10px; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 16px; font-weight: 600; display: inline-flex; align-items: center; justify-content: center; gap: 8px; border: none; cursor: pointer; margin-top: 8px">
          <span>{T[lang]['modal_submit']}</span>
        </button>
      </form>
    </div>
    
    <div id="modalLeadSuccessContainer" style="display: none; text-align: center; padding: 24px 8px">
      <div style="width: 56px; height: 56px; border-radius: 50%; background: #F3F8F7; border: 2px solid #087F6A; color: #087F6A; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 16px">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
      </div>
      <h3 style="margin: 0 0 8px 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 22px; font-weight: 700; color: #172B2A">{T[lang]['modal_success_title']}</h3>
      <p style="margin: 0 0 24px 0; font-size: 15px; color: #5F6F6D; line-height: 1.5">{T[lang]['modal_success_desc']}</p>
      <button type="button" onclick="closeDemoModal()" style="min-height: 44px; padding: 0 24px; border-radius: 10px; background: #172B2A; color: #FFFFFF; font-weight: 600; border: none; cursor: pointer">OK</button>
    </div>
  </div>
</div>
"""
    js = f"""
<script>
function openDemoModal(interest) {{
  var modal = document.getElementById('demoModal');
  var interestField = document.getElementById('modalLeadInterest');
  if (interestField && interest) {{
    interestField.value = interest;
  }}
  if (modal) {{
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }}
}}

function closeDemoModal() {{
  var modal = document.getElementById('demoModal');
  if (modal) {{
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }}
}}

document.addEventListener('keydown', function(e) {{
  if (e.key === 'Escape') {{
    closeDemoModal();
  }}
}});

async function handleLeadSubmit(e) {{
  e.preventDefault();
  var btn = document.getElementById('btnModalSubmit');
  if (btn) btn.disabled = true;
  
  var name = document.getElementById('leadName').value.trim();
  var company = document.getElementById('leadCompany').value.trim();
  var contact = document.getElementById('leadContact').value.trim();
  var teamSize = document.getElementById('leadTeamSize').value;
  var interest = document.getElementById('modalLeadInterest').value || 'General';
  
  var checkedChannels = [];
  var cbs = document.querySelectorAll('input[name="channels"]:checked');
  cbs.forEach(function(cb) {{ checkedChannels.push(cb.value); }});
  
  var payload = {{
    source: 'gptify.si',
    full_name: name,
    company: company,
    phone: contact,
    contact: contact,
    category: 'GPTify OS Demo: ' + interest,
    course_name: 'GPTify OS Demo | Qiziqish: ' + interest + ' | Kompaniya: ' + company + ' | Jamoa: ' + teamSize + ' | Kanallar: ' + checkedChannels.join(', '),
    team_size: teamSize,
    channels: checkedChannels.join(', '),
    interest: interest,
    lang: '{lang}',
    created_at: new Date().toISOString()
  }};
  
  try {{
    await fetch('{SCRIPT_URL}', {{
      method: 'POST',
      mode: 'no-cors',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify(payload)
    }});
  }} catch (err) {{
    console.warn('Lead submit error:', err);
  }}
  
  document.getElementById('modalLeadFormContainer').style.display = 'none';
  document.getElementById('modalLeadSuccessContainer').style.display = 'block';
}}
</script>
"""
    return modal_html + js

HOMEPAGE_JS_CODE = """
<script>
const industriesData = __DATA_JSON__;

function selectIndustryTab(id) {
  const tabs = ['clinic', 'edu', 'auto', 'advisory'];
  tabs.forEach(function(t) {
    const btn = document.getElementById('tab-btn-' + t);
    if (btn) {
      if (t === id) {
        btn.style.background = '#172B2A';
        btn.style.color = '#FFFFFF';
        btn.style.border = '1px solid #172B2A';
        btn.setAttribute('aria-selected', 'true');
      } else {
        btn.style.background = '#FFFFFF';
        btn.style.color = '#172B2A';
        btn.style.border = '1px solid #DCE8E6';
        btn.setAttribute('aria-selected', 'false');
      }
    }
  });

  const d = industriesData[id];
  if (!d) return;

  const badge = document.getElementById('ind-product-badge');
  const pitch = document.getElementById('ind-pitch-heading');
  const cta = document.getElementById('ind-cta-btn');
  const bullets = document.getElementById('ind-bullets-container');
  const steps = document.getElementById('ind-steps-container');

  if (badge) badge.textContent = d.product;
  if (pitch) pitch.textContent = d.pitch;
  if (cta) {
    cta.textContent = d.cta;
    cta.setAttribute('onclick', "openDemoModal('" + d.label.replace(/'/g, "\\\\'") + "')");
  }

  if (bullets) {
    bullets.innerHTML = d.bullets.map(function(b) {
      return '<div style="display: flex; align-items: flex-start; gap: 12px; font-size: 18px; line-height: 1.45; color: #172B2A">' +
        '<svg aria-hidden="true" style="flex: none; margin-top: 3px" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#087F6A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5 9-10"></path></svg>' +
        '<span>' + b + '</span></div>';
    }).join('');
  }

  if (steps) {
    steps.innerHTML = d.steps.map(function(s) {
      return '<div style="display: flex; align-items: center; gap: 14px">' +
        '<div style="flex: none; width: 92px; box-sizing: border-box; text-align: center; border-radius: 10px; padding: 10px 0; font-family: inherit; font-weight: 700; font-size: 15px; color: #FFFFFF; background: ' + s.color + '">' + s.name + '</div>' +
        '<div style="font-size: 16px; line-height: 1.4; color: #172B2A">' + s.text + '</div></div>';
    }).join('');
  }
}

document.addEventListener('DOMContentLoaded', function() {
  const tabList = document.querySelector('[role="tablist"]');
  if (tabList) {
    tabList.addEventListener('keydown', function(e) {
      const tabs = Array.from(tabList.querySelectorAll('[role="tab"]'));
      let index = tabs.indexOf(document.activeElement);
      if (index === -1) return;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        e.preventDefault();
        const next = (index + 1) % tabs.length;
        tabs[next].focus();
        tabs[next].click();
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        e.preventDefault();
        const prev = (index - 1 + tabs.length) % tabs.length;
        tabs[prev].focus();
        tabs[prev].click();
      }
    });
  }

  const sTeam = document.getElementById('slider-team');
  const sHours = document.getElementById('slider-hours');
  const sSalary = document.getElementById('slider-salary');

  if (sTeam) {
    sTeam.addEventListener('input', updateCalculator);
    sTeam.addEventListener('change', updateCalculator);
  }
  if (sHours) {
    sHours.addEventListener('input', updateCalculator);
    sHours.addEventListener('change', updateCalculator);
  }
  if (sSalary) {
    sSalary.addEventListener('input', updateCalculator);
    sSalary.addEventListener('change', updateCalculator);
  }

  updateCalculator();
});

function updateCalculator() {
  const sTeam = document.getElementById('slider-team');
  const sHours = document.getElementById('slider-hours');
  const sSalary = document.getElementById('slider-salary');
  if (!sTeam || !sHours || !sSalary) return;

  const team = Number(sTeam.value);
  const hours = Number(sHours.value);
  const salary = Number(sSalary.value);

  const valTeam = document.getElementById('val-team');
  const valHours = document.getElementById('val-hours');
  const valSalary = document.getElementById('val-salary');

  if (valTeam) valTeam.textContent = team;
  if (valHours) valHours.textContent = hours + ' h';
  if (valSalary) valSalary.textContent = '$' + salary;

  const weekHours = Math.round(team * hours * 0.7 * 10) / 10;
  const yearly = Math.round(weekHours * 50 * (salary / 160));
  const monthly = Math.round(yearly / 12);

  const resYear = document.getElementById('res-year-text');
  const resMonth = document.getElementById('res-month-text');
  const resHours = document.getElementById('res-hours-text');

  if (resYear) resYear.textContent = '~$' + yearly.toLocaleString('en-US');
  if (resMonth) resMonth.textContent = '$' + monthly.toLocaleString('en-US');
  if (resHours) resHours.textContent = weekHours.toFixed(1);
}
</script>
"""

def generate_homepage(lang):
    canonical = "https://gptify.si/" if lang == 'en' else f"https://gptify.si/{lang}/"
    css_href = "style.min.css" if lang == 'en' else "../style.min.css"
    mark_href = "gptify-mark.svg" if lang == 'en' else "../gptify-mark.svg"
    header_html = generate_header(lang, 'home')
    footer_html = generate_footer(lang)
    modal_html = generate_modal(lang)
    
    headline_html = f"{T[lang]['hero_h1_lead']} <span style=\"color: #087F6A\">{T[lang]['hero_h1_highlight']}</span>"

    industries_data_json = json.dumps({
        "clinic": {
            "label": T[lang]["clinic_label"],
            "product": T[lang]["clinic_product"],
            "pitch": T[lang]["clinic_pitch"],
            "cta": T[lang]["clinic_cta"],
            "bullets": [T[lang]["clinic_b1"], T[lang]["clinic_b2"], T[lang]["clinic_b3"]],
            "steps": [
                {"name": "Ailo", "color": "#087F6A", "text": T[lang]["clinic_s1_text"]},
                {"name": "Bandla", "color": "#7C3AED", "text": T[lang]["clinic_s2_text"]},
                {"name": "ILDAM", "color": "#B45309", "text": T[lang]["clinic_s3_text"]},
                {"name": "Mirzo", "color": "#0369A1", "text": T[lang]["clinic_s4_text"]}
            ]
        },
        "edu": {
            "label": T[lang]["edu_label"],
            "product": T[lang]["edu_product"],
            "pitch": T[lang]["edu_pitch"],
            "cta": T[lang]["edu_cta"],
            "bullets": [T[lang]["edu_b1"], T[lang]["edu_b2"], T[lang]["edu_b3"]],
            "steps": [
                {"name": "Ailo", "color": "#087F6A", "text": T[lang]["edu_s1_text"]},
                {"name": "Bandla", "color": "#7C3AED", "text": T[lang]["edu_s2_text"]},
                {"name": "ILDAM", "color": "#B45309", "text": T[lang]["edu_s3_text"]},
                {"name": "Mirzo", "color": "#0369A1", "text": T[lang]["edu_s4_text"]}
            ]
        },
        "auto": {
            "label": T[lang]["auto_label"],
            "product": T[lang]["auto_product"],
            "pitch": T[lang]["auto_pitch"],
            "cta": T[lang]["auto_cta"],
            "bullets": [T[lang]["auto_b1"], T[lang]["auto_b2"], T[lang]["auto_b3"]],
            "steps": [
                {"name": "Ailo", "color": "#087F6A", "text": T[lang]["auto_s1_text"]},
                {"name": "Bandla", "color": "#7C3AED", "text": T[lang]["auto_s2_text"]},
                {"name": "ILDAM", "color": "#B45309", "text": T[lang]["auto_s3_text"]},
                {"name": "Izlai", "color": "#3730A3", "text": T[lang]["auto_s4_text"]}
            ]
        },
        "advisory": {
            "label": T[lang]["advisory_label"],
            "product": T[lang]["advisory_product"],
            "pitch": T[lang]["advisory_pitch"],
            "cta": T[lang]["advisory_cta"],
            "bullets": [T[lang]["advisory_b1"], T[lang]["advisory_b2"], T[lang]["advisory_b3"]],
            "steps": [
                {"name": "Izlai", "color": "#3730A3", "text": T[lang]["advisory_s1_text"]},
                {"name": "ILDAM", "color": "#B45309", "text": T[lang]["advisory_s2_text"]},
                {"name": "Mirzo", "color": "#0369A1", "text": T[lang]["advisory_s3_text"]},
                {"name": "Bandla", "color": "#7C3AED", "text": T[lang]["advisory_s4_text"]}
            ]
        }
    }, ensure_ascii=False)

    page_html = f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
  <script>if(location.protocol==='http:'&&!['localhost','127.0.0.1'].includes(location.hostname)){{location.replace('https://'+location.host+location.pathname+location.search+location.hash);}}</script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{T[lang]['page_title']}</title>
  <meta name="description" content="{T[lang]['meta_description']}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="https://gptify.si/">
  <link rel="alternate" hreflang="uz" href="https://gptify.si/uz/">
  <link rel="alternate" hreflang="ru" href="https://gptify.si/ru/">
  <link rel="alternate" hreflang="x-default" href="https://gptify.si/">
  <link rel="stylesheet" href="{css_href}">
  <link rel="icon" href="{mark_href}" type="image/svg+xml">
  <meta property="og:title" content="{T[lang]['page_title']}">
  <meta property="og:description" content="{T[lang]['meta_description']}">
  <meta property="og:image" content="https://gptify.si/og-image.png">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{T[lang]['page_title']}">
  <meta name="twitter:description" content="{T[lang]['meta_description']}">
  <meta name="twitter:image" content="https://gptify.si/og-image.png">
</head>
<body>
{header_html}

<!-- Hero Section [top] -->
<section id="top" style="display: flex; flex-wrap: wrap; align-items: flex-start; gap: 32px 64px; padding: 44px clamp(20px, 5vw, 80px) 56px">
  <div style="flex: 1 1 420px; min-width: 0; display: flex; flex-direction: column; gap: 22px; padding-top: 8px">
    <h1 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(36px, 4.2vw, 60px); line-height: 1.06; letter-spacing: -0.02em; color: #172B2A">{headline_html}</h1>
    <p style="margin: 0; max-width: 520px; font-size: 19px; line-height: 1.5; color: #5F6F6D">{T[lang]['hero_sub']}</p>
    <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 14px 24px">
      <button onclick="openDemoModal('Hero Demo')" style="display: inline-flex; align-items: center; gap: 14px; min-height: 58px; min-width: 44px; padding: 0 10px 0 26px; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; border-radius: 10px; border: none; cursor: pointer">
        <span>{T[lang]['hero_btn_live']}</span>
        <span style="display: inline-flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 8px; background: #B7F34A">
          <svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#172B2A" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7"></path><path d="M8 7h9v9"></path></svg>
        </span>
      </button>
      <a href="#industries" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; min-width: 44px; font-size: 17px; font-weight: 600; color: #087F6A">{T[lang]['hero_btn_industry']}</a>
    </div>
    <div style="font-size: 15px; font-weight: 500; color: #5F6F6D">{T[lang]['hero_microcopy']}</div>
  </div>

  <!-- Hero Chat Mockup (10s Animation Loop) -->
  <div style="flex: 1.15 1 480px; min-width: 0; background: #F3F8F7; border-radius: 24px; padding: clamp(14px, 1.5vw, 20px); display: flex; flex-direction: column; gap: 12px">
    <div style="background: #FFFFFF; border-radius: 18px; padding: 18px 20px; display: flex; flex-direction: column; gap: 12px">
      <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px">
        <div style="display: flex; align-items: center; gap: 12px">
          <div aria-hidden="true" style="display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 50%; background: #172B2A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 17px">M</div>
          <div style="display: flex; flex-direction: column; gap: 2px">
            <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 16px; color: #172B2A">{T[lang]['chat_title']}</div>
            <div style="font-size: 13px; font-weight: 500; color: #5F6F6D">{T[lang]['chat_sub']}</div>
          </div>
        </div>
        <div style="display: inline-flex; align-items: center; gap: 8px; padding: 7px 12px; border-radius: 999px; background: #087F6A; color: #FFFFFF; font-size: 13px; font-weight: 600">
          <svg aria-hidden="true" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h7l-1 8 9-12h-7z"></path></svg>
          {T[lang]['chat_badge']}
        </div>
      </div>
      
      <div style="display: flex; flex-direction: column; gap: 8px">
        <div style="align-self: flex-start; max-width: 86%; background: #F3F8F7; border-radius: 16px 16px 16px 4px; padding: 10px 14px; font-size: 15px; line-height: 1.4; color: #172B2A; animation: inA 10s ease infinite">{T[lang]['chat_msg_1']}</div>
        <div style="align-self: flex-end; max-width: 86%; background: #172B2A; border-radius: 16px 16px 4px 16px; padding: 10px 14px; font-size: 15px; line-height: 1.4; color: #FFFFFF; animation: inB 10s ease infinite">{T[lang]['chat_msg_2']}</div>
        <div style="align-self: flex-start; max-width: 86%; background: #F3F8F7; border-radius: 16px 16px 16px 4px; padding: 10px 14px; font-size: 15px; line-height: 1.4; color: #172B2A; animation: inC 10s ease infinite">{T[lang]['chat_msg_3']}</div>
      </div>
    </div>
    
    <div style="display: flex; flex-wrap: wrap; gap: 8px">
      <div style="flex: 1 1 140px; background: #087F6A; border-radius: 12px; padding: 10px 14px; color: #FFFFFF; animation: inD 10s ease infinite">
        <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 16px">{T[lang]['chip_ailo_title']}</div>
        <div style="font-size: 14px; font-weight: 500; line-height: 1.3">{T[lang]['chip_ailo_desc']}</div>
      </div>
      <div style="flex: 1 1 140px; background: #7C3AED; border-radius: 12px; padding: 10px 14px; color: #FFFFFF; animation: inE 10s ease infinite">
        <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 16px">{T[lang]['chip_bandla_title']}</div>
        <div style="font-size: 14px; font-weight: 500; line-height: 1.3">{T[lang]['chip_bandla_desc']}</div>
      </div>
      <div style="flex: 1 1 140px; background: #B45309; border-radius: 12px; padding: 10px 14px; color: #FFFFFF; animation: inF 10s ease infinite">
        <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 16px">{T[lang]['chip_ildam_title']}</div>
        <div style="font-size: 14px; font-weight: 500; line-height: 1.3">{T[lang]['chip_ildam_desc']}</div>
      </div>
    </div>
  </div>
</section>

<!-- Integrations Strip Section -->
<section aria-label="Works with" style="padding: 28px 0 36px; border-top: 1px solid #DCE8E6; display: flex; flex-direction: column; gap: 20px; overflow: hidden; max-width: 100vw">
  <div style="text-align: center; padding: 0 clamp(20px, 5vw, 80px); font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #5F6F6D; text-transform: uppercase">{T[lang]['integrations_label']}</div>
  <div style="overflow: hidden; max-width: 100vw; -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent); mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent)">
    <div style="display: flex; flex-wrap: nowrap; width: max-content; animation: marq 40s linear infinite">
      <div style="display: flex; flex-wrap: nowrap; gap: 16px; padding-right: 16px">
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #0369A1"></span>Telegram</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #087F6A"></span>WhatsApp Business</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #BE185D"></span>Instagram Direct</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #3730A3"></span>LinkedIn</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #B45309"></span>Google Calendar</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #0369A1"></span>Outlook</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #3730A3"></span>Zoom</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #087F6A"></span>Google Meet</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #7C3AED"></span>Microsoft Teams</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #B45309"></span>1C</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #0369A1"></span>Click</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #087F6A"></span>Payme</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #7C3AED"></span>Uzum</span>
      </div>
      <div style="display: flex; flex-wrap: nowrap; gap: 16px; padding-right: 16px" aria-hidden="true">
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #0369A1"></span>Telegram</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #087F6A"></span>WhatsApp Business</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #BE185D"></span>Instagram Direct</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #3730A3"></span>LinkedIn</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #B45309"></span>Google Calendar</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #0369A1"></span>Outlook</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #3730A3"></span>Zoom</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #087F6A"></span>Google Meet</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #7C3AED"></span>Microsoft Teams</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #B45309"></span>1C</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #0369A1"></span>Click</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #087F6A"></span>Payme</span>
        <span style="flex: none; display: inline-flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 20px; background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 16px; font-weight: 600; color: #172B2A; white-space: nowrap"><span aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: #7C3AED"></span>Uzum</span>
      </div>
    </div>
  </div>
</section>

<!-- Industries Section [industries] -->
<section id="industries" style="padding: 72px clamp(20px, 5vw, 80px) 88px; display: flex; flex-direction: column; gap: 28px">
  <div style="display: flex; flex-direction: column; gap: 14px; max-width: 820px">
    <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['ind_eyebrow']}</div>
    <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(30px, 3.3vw, 46px); line-height: 1.12; letter-spacing: -0.015em; color: #172B2A">{T[lang]['ind_heading']}</h2>
  </div>
  
  <!-- Tabs Navigation -->
  <div role="tablist" aria-label="Industries" style="display: flex; flex-wrap: wrap; gap: 10px">
    <button role="tab" id="tab-btn-clinic" aria-selected="true" aria-controls="panel-industry" onclick="selectIndustryTab('clinic')" style="min-height: 52px; min-width: 44px; padding: 0 24px; border-radius: 999px; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 17px; background: #172B2A; color: #FFFFFF; border: 1px solid #172B2A; cursor: pointer">{T[lang]['clinic_label']}</button>
    <button role="tab" id="tab-btn-edu" aria-selected="false" aria-controls="panel-industry" onclick="selectIndustryTab('edu')" style="min-height: 52px; min-width: 44px; padding: 0 24px; border-radius: 999px; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 17px; background: #FFFFFF; color: #172B2A; border: 1px solid #DCE8E6; cursor: pointer">{T[lang]['edu_label']}</button>
    <button role="tab" id="tab-btn-auto" aria-selected="false" aria-controls="panel-industry" onclick="selectIndustryTab('auto')" style="min-height: 52px; min-width: 44px; padding: 0 24px; border-radius: 999px; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 17px; background: #FFFFFF; color: #172B2A; border: 1px solid #DCE8E6; cursor: pointer">{T[lang]['auto_label']}</button>
    <button role="tab" id="tab-btn-advisory" aria-selected="false" aria-controls="panel-industry" onclick="selectIndustryTab('advisory')" style="min-height: 52px; min-width: 44px; padding: 0 24px; border-radius: 999px; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 17px; background: #FFFFFF; color: #172B2A; border: 1px solid #DCE8E6; cursor: pointer">{T[lang]['advisory_label']}</button>
  </div>
  
  <!-- Active Tab Panel -->
  <div id="panel-industry" role="tabpanel" style="background: #F3F8F7; border-radius: 28px; padding: clamp(20px, 3vw, 44px); display: flex; flex-wrap: wrap; gap: 32px 56px">
    <div style="flex: 1 1 400px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
      <div id="ind-product-badge" style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 14px; font-weight: 600; letter-spacing: 0.08em; color: #087F6A">{T[lang]['clinic_product']}</div>
      <h3 id="ind-pitch-heading" style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(26px, 2.5vw, 34px); line-height: 1.15; letter-spacing: -0.01em; color: #172B2A">{T[lang]['clinic_pitch']}</h3>
      
      <div id="ind-bullets-container" style="display: flex; flex-direction: column; gap: 12px; margin-top: 4px">
        <div style="display: flex; align-items: flex-start; gap: 12px; font-size: 18px; line-height: 1.45; color: #172B2A">
          <svg aria-hidden="true" style="flex: none; margin-top: 3px" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#087F6A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5 9-10"></path></svg>
          <span>{T[lang]['clinic_b1']}</span>
        </div>
        <div style="display: flex; align-items: flex-start; gap: 12px; font-size: 18px; line-height: 1.45; color: #172B2A">
          <svg aria-hidden="true" style="flex: none; margin-top: 3px" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#087F6A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5 9-10"></path></svg>
          <span>{T[lang]['clinic_b2']}</span>
        </div>
        <div style="display: flex; align-items: flex-start; gap: 12px; font-size: 18px; line-height: 1.45; color: #172B2A">
          <svg aria-hidden="true" style="flex: none; margin-top: 3px" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#087F6A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5 9-10"></path></svg>
          <span>{T[lang]['clinic_b3']}</span>
        </div>
      </div>
      
      <button id="ind-cta-btn" onclick="openDemoModal('Clinics')" style="align-self: flex-start; display: inline-flex; align-items: center; justify-content: center; min-height: 52px; min-width: 44px; margin-top: 8px; padding: 0 24px; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 16px; border-radius: 10px; border: none; cursor: pointer">{T[lang]['clinic_cta']}</button>
    </div>
    
    <div style="flex: 1 1 400px; min-width: 0; background: #FFFFFF; border-radius: 20px; padding: 24px; display: flex; flex-direction: column; gap: 14px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; color: #172B2A">{T[lang]['ind_steps_title']}</div>
      <div id="ind-steps-container" style="display: flex; flex-direction: column; gap: 14px">
        <div style="display: flex; align-items: center; gap: 14px">
          <div style="flex: none; width: 92px; box-sizing: border-box; text-align: center; border-radius: 10px; padding: 10px 0; font-family: inherit; font-weight: 700; font-size: 15px; color: #FFFFFF; background: #087F6A">Ailo</div>
          <div style="font-size: 16px; line-height: 1.4; color: #172B2A">{T[lang]['clinic_s1_text']}</div>
        </div>
        <div style="display: flex; align-items: center; gap: 14px">
          <div style="flex: none; width: 92px; box-sizing: border-box; text-align: center; border-radius: 10px; padding: 10px 0; font-family: inherit; font-weight: 700; font-size: 15px; color: #FFFFFF; background: #7C3AED">Bandla</div>
          <div style="font-size: 16px; line-height: 1.4; color: #172B2A">{T[lang]['clinic_s2_text']}</div>
        </div>
        <div style="display: flex; align-items: center; gap: 14px">
          <div style="flex: none; width: 92px; box-sizing: border-box; text-align: center; border-radius: 10px; padding: 10px 0; font-family: inherit; font-weight: 700; font-size: 15px; color: #FFFFFF; background: #B45309">ILDAM</div>
          <div style="font-size: 16px; line-height: 1.4; color: #172B2A">{T[lang]['clinic_s3_text']}</div>
        </div>
        <div style="display: flex; align-items: center; gap: 14px">
          <div style="flex: none; width: 92px; box-sizing: border-box; text-align: center; border-radius: 10px; padding: 10px 0; font-family: inherit; font-weight: 700; font-size: 15px; color: #FFFFFF; background: #0369A1">Mirzo</div>
          <div style="font-size: 16px; line-height: 1.4; color: #172B2A">{T[lang]['clinic_s4_text']}</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- The Five Tools Section [tools] -->
<section id="tools" style="padding: 88px clamp(20px, 5vw, 80px) 96px; border-top: 1px solid #DCE8E6; display: flex; flex-direction: column; gap: 40px">
  <div style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 20px 48px">
    <h2 style="margin: 0; flex: 1 1 480px; max-width: 760px; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(30px, 3.3vw, 46px); line-height: 1.12; letter-spacing: -0.015em; color: #172B2A">{T[lang]['tools_heading']}</h2>
    <p style="margin: 0; flex: 1 1 320px; max-width: 420px; font-size: 18px; line-height: 1.55; color: #5F6F6D">{T[lang]['tools_sub']}</p>
  </div>
  
  <!-- Connected Color Rail of 5 Tools (Stacks on Mobile) -->
  <div style="display: flex; flex-wrap: wrap; border-radius: 28px; overflow: hidden">
    <article class="tool-card-0" style="flex: 1 1 200px; min-width: 0; min-height: 340px; box-sizing: border-box; background: #3730A3; padding: 30px 24px; display: flex; flex-direction: column; gap: 12px; color: #FFFFFF">
      <div style="font-size: 14px; font-weight: 600; letter-spacing: 0.12em">{T[lang]['izlai_step']}</div>
      <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 40px; line-height: 1.05; letter-spacing: -0.02em">{T[lang]['izlai_name']}</h3>
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; line-height: 1.3">{T[lang]['izlai_job']}</div>
      <p style="margin: 0; font-size: 16px; line-height: 1.55">{T[lang]['izlai_body']}</p>
      <div style="margin-top: auto; min-height: 44px; display: flex; align-items: flex-end; justify-content: space-between; gap: 12px; font-size: 15px; font-weight: 600; line-height: 1.3">
        <span>{T[lang]['izlai_handoff']}</span>
        <svg aria-hidden="true" style="flex: none" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#B7F34A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg>
      </div>
    </article>
    
    <article class="tool-card-1" style="flex: 1 1 200px; min-width: 0; min-height: 340px; box-sizing: border-box; background: #087F6A; padding: 30px 24px; display: flex; flex-direction: column; gap: 12px; color: #FFFFFF">
      <div style="font-size: 14px; font-weight: 600; letter-spacing: 0.12em">{T[lang]['ailo_step']}</div>
      <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 40px; line-height: 1.05; letter-spacing: -0.02em">{T[lang]['ailo_name']}</h3>
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; line-height: 1.3">{T[lang]['ailo_job']}</div>
      <p style="margin: 0; font-size: 16px; line-height: 1.55">{T[lang]['ailo_body']}</p>
      <div style="margin-top: auto; min-height: 44px; display: flex; align-items: flex-end; justify-content: space-between; gap: 12px; font-size: 15px; font-weight: 600; line-height: 1.3">
        <span>{T[lang]['ailo_handoff']}</span>
        <svg aria-hidden="true" style="flex: none" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#B7F34A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg>
      </div>
    </article>
    
    <article class="tool-card-2" style="flex: 1 1 200px; min-width: 0; min-height: 340px; box-sizing: border-box; background: #B45309; padding: 30px 24px; display: flex; flex-direction: column; gap: 12px; color: #FFFFFF">
      <div style="font-size: 14px; font-weight: 600; letter-spacing: 0.12em">{T[lang]['ildam_step']}</div>
      <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 40px; line-height: 1.05; letter-spacing: -0.02em">{T[lang]['ildam_name']}</h3>
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; line-height: 1.3">{T[lang]['ildam_job']}</div>
      <p style="margin: 0; font-size: 16px; line-height: 1.55">{T[lang]['ildam_body']}</p>
      <div style="margin-top: auto; min-height: 44px; display: flex; align-items: flex-end; justify-content: space-between; gap: 12px; font-size: 15px; font-weight: 600; line-height: 1.3">
        <span>{T[lang]['ildam_handoff']}</span>
        <svg aria-hidden="true" style="flex: none" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#B7F34A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg>
      </div>
    </article>
    
    <article class="tool-card-3" style="flex: 1 1 200px; min-width: 0; min-height: 340px; box-sizing: border-box; background: #7C3AED; padding: 30px 24px; display: flex; flex-direction: column; gap: 12px; color: #FFFFFF">
      <div style="font-size: 14px; font-weight: 600; letter-spacing: 0.12em">{T[lang]['bandla_step']}</div>
      <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 40px; line-height: 1.05; letter-spacing: -0.02em">{T[lang]['bandla_name']}</h3>
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; line-height: 1.3">{T[lang]['bandla_job']}</div>
      <p style="margin: 0; font-size: 16px; line-height: 1.55">{T[lang]['bandla_body']}</p>
      <div style="margin-top: auto; min-height: 44px; display: flex; align-items: flex-end; justify-content: space-between; gap: 12px; font-size: 15px; font-weight: 600; line-height: 1.3">
        <span>{T[lang]['bandla_handoff']}</span>
        <svg aria-hidden="true" style="flex: none" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#B7F34A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg>
      </div>
    </article>
    
    <article class="tool-card-4" style="flex: 1 1 200px; min-width: 0; min-height: 340px; box-sizing: border-box; background: #0369A1; padding: 30px 24px; display: flex; flex-direction: column; gap: 12px; color: #FFFFFF">
      <div style="font-size: 14px; font-weight: 600; letter-spacing: 0.12em">{T[lang]['mirzo_step']}</div>
      <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 40px; line-height: 1.05; letter-spacing: -0.02em">{T[lang]['mirzo_name']}</h3>
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; line-height: 1.3">{T[lang]['mirzo_job']}</div>
      <p style="margin: 0; font-size: 16px; line-height: 1.55">{T[lang]['mirzo_body']}</p>
      <div style="margin-top: auto; min-height: 44px; display: flex; align-items: flex-end; justify-content: space-between; gap: 12px; font-size: 15px; font-weight: 600; line-height: 1.3">
        <span>{T[lang]['mirzo_handoff']}</span>
        <svg aria-hidden="true" style="flex: none" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#B7F34A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 0 1 14-5.3L20 9"></path><path d="M20 4v5h-5"></path></svg>
      </div>
    </article>
  </div>
  
  <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px 32px">
    <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 24px; color: #172B2A">{T[lang]['tools_bottom_sub']}</div>
    <button onclick="openDemoModal('The Five Tools')" style="display: inline-flex; align-items: center; justify-content: center; min-height: 56px; min-width: 44px; padding: 0 28px; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 17px; border-radius: 10px; border: none; cursor: pointer">{T[lang]['tools_bottom_cta']}</button>
  </div>
</section>

<!-- Savings Calculator Section [savings] -->
<section id="savings" style="background: #F3F8F7; padding: 88px clamp(20px, 5vw, 80px); display: flex; flex-direction: column; gap: 36px">
  <div style="display: flex; flex-direction: column; gap: 14px; max-width: 820px">
    <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['calc_eyebrow']}</div>
    <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(30px, 3.3vw, 46px); line-height: 1.12; letter-spacing: -0.015em; color: #172B2A">{T[lang]['calc_heading']}</h2>
  </div>
  
  <div style="display: flex; flex-wrap: wrap; gap: 24px">
    <!-- Sliders Input Card -->
    <div style="flex: 1.2 1 420px; min-width: 0; background: #FFFFFF; border-radius: 24px; padding: clamp(20px, 2.6vw, 36px); display: flex; flex-direction: column; gap: 22px">
      <div style="display: flex; flex-direction: column; gap: 6px">
        <div style="display: flex; justify-content: space-between; gap: 12px; font-size: 17px; font-weight: 600; color: #172B2A">
          <label for="slider-team">{T[lang]['slider_team']}</label>
          <span id="val-team" style="color: #087F6A">5</span>
        </div>
        <input id="slider-team" type="range" min="1" max="50" step="1" value="5" aria-label="{T[lang]['slider_team']}" style="width: 100%; height: 44px; margin: 0; accent-color: #087F6A">
      </div>
      
      <div style="display: flex; flex-direction: column; gap: 6px">
        <div style="display: flex; justify-content: space-between; gap: 12px; font-size: 17px; font-weight: 600; color: #172B2A">
          <label for="slider-hours">{T[lang]['slider_hours']}</label>
          <span id="val-hours" style="color: #087F6A">15 h</span>
        </div>
        <input id="slider-hours" type="range" min="5" max="35" step="1" value="15" aria-label="{T[lang]['slider_hours']}" style="width: 100%; height: 44px; margin: 0; accent-color: #087F6A">
      </div>
      
      <div style="display: flex; flex-direction: column; gap: 6px">
        <div style="display: flex; justify-content: space-between; gap: 12px; font-size: 17px; font-weight: 600; color: #172B2A">
          <label for="slider-salary">{T[lang]['slider_salary']}</label>
          <span id="val-salary" style="color: #087F6A">$391</span>
        </div>
        <input id="slider-salary" type="range" min="300" max="1500" step="1" value="391" aria-label="{T[lang]['slider_salary']}" style="width: 100%; height: 44px; margin: 0; accent-color: #087F6A">
      </div>
    </div>
    
    <!-- Results Dark Card -->
    <div style="flex: 1 1 340px; min-width: 0; background: #172B2A; border-radius: 24px; padding: clamp(20px, 2.6vw, 36px); display: flex; flex-direction: column; gap: 10px; color: #FFFFFF">
      <div style="font-size: 16px; font-weight: 600">{T[lang]['calc_result_label']}</div>
      <div id="res-year-text" style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(44px, 5vw, 68px); line-height: 1; letter-spacing: -0.02em; color: #B7F34A">~$6,415</div>
      <div style="font-size: 17px; line-height: 1.45">
        {T[lang]['calc_sub_about']} <span id="res-month-text">$535</span> {T[lang]['calc_sub_month']} · <span id="res-hours-text">52.5</span> {T[lang]['calc_sub_hours']}
      </div>
      <button onclick="openDemoModal('Savings Calculator')" style="align-self: flex-start; display: inline-flex; align-items: center; justify-content: center; min-height: 52px; min-width: 44px; margin-top: 14px; padding: 0 24px; background: #B7F34A; color: #172B2A; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 16px; border-radius: 10px; border: none; cursor: pointer">{T[lang]['calc_btn']}</button>
      <div style="margin-top: auto; padding-top: 14px; font-size: 14px; line-height: 1.45; color: #C9DAD7">{T[lang]['calc_note']}</div>
    </div>
  </div>
</section>

<!-- Optional Extras Section [addons] -->
<section id="addons" style="padding: 88px clamp(20px, 5vw, 80px) 40px; display: flex; flex-direction: column; gap: 32px">
  <div style="display: flex; flex-direction: column; gap: 14px; max-width: 820px">
    <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['addons_eyebrow']}</div>
    <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(30px, 3.3vw, 46px); line-height: 1.12; letter-spacing: -0.015em; color: #172B2A">{T[lang]['addons_heading']}</h2>
  </div>
  
  <div style="display: flex; flex-wrap: wrap; gap: 16px">
    <div style="flex: 1 1 300px; min-width: 0; border: 1px solid #DCE8E6; border-radius: 16px; padding: 20px 22px; display: flex; flex-direction: column; gap: 6px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; color: #172B2A">{T[lang]['addon1_title']}</div>
      <div style="font-size: 16px; line-height: 1.5; color: #5F6F6D">{T[lang]['addon1_desc']}</div>
    </div>
    
    <div style="flex: 1 1 300px; min-width: 0; border: 1px solid #DCE8E6; border-radius: 16px; padding: 20px 22px; display: flex; flex-direction: column; gap: 6px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; color: #172B2A">{T[lang]['addon2_title']}</div>
      <div style="font-size: 16px; line-height: 1.5; color: #5F6F6D">{T[lang]['addon2_desc']}</div>
    </div>
    
    <div style="flex: 1 1 300px; min-width: 0; border: 1px solid #DCE8E6; border-radius: 16px; padding: 20px 22px; display: flex; flex-direction: column; gap: 6px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; color: #172B2A">{T[lang]['addon3_title']}</div>
      <div style="font-size: 16px; line-height: 1.5; color: #5F6F6D">{T[lang]['addon3_desc']}</div>
    </div>
    
    <div style="flex: 1 1 300px; min-width: 0; border: 1px solid #DCE8E6; border-radius: 16px; padding: 20px 22px; display: flex; flex-direction: column; gap: 6px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; color: #172B2A">{T[lang]['addon4_title']}</div>
      <div style="font-size: 16px; line-height: 1.5; color: #5F6F6D">{T[lang]['addon4_desc']}</div>
    </div>
    
    <div style="flex: 1 1 300px; min-width: 0; border: 1px solid #DCE8E6; border-radius: 16px; padding: 20px 22px; display: flex; flex-direction: column; gap: 6px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; color: #172B2A">{T[lang]['addon5_title']}</div>
      <div style="font-size: 16px; line-height: 1.5; color: #5F6F6D">{T[lang]['addon5_desc']}</div>
    </div>
    
    <div style="flex: 1 1 300px; min-width: 0; border: 1px solid #DCE8E6; border-radius: 16px; padding: 20px 22px; display: flex; flex-direction: column; gap: 6px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; color: #172B2A">{T[lang]['addon6_title']}</div>
      <div style="font-size: 16px; line-height: 1.5; color: #5F6F6D">{T[lang]['addon6_desc']}</div>
    </div>
  </div>
</section>

<!-- How We Start Section [process] -->
<section id="process" style="padding: 56px clamp(20px, 5vw, 80px) 88px; display: flex; flex-direction: column; gap: 32px">
  <div style="display: flex; flex-direction: column; gap: 14px; max-width: 820px">
    <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['process_eyebrow']}</div>
    <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(30px, 3.3vw, 46px); line-height: 1.12; letter-spacing: -0.015em; color: #172B2A">{T[lang]['process_heading']}</h2>
  </div>
  
  <div style="display: flex; flex-wrap: wrap; gap: 32px 48px">
    <div style="flex: 1 1 280px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
      <div style="display: flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: #172B2A; color: #B7F34A; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 20px">{T[lang]['step1_num']}</div>
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 22px; color: #172B2A">{T[lang]['step1_title']}</div>
      <div style="font-size: 17px; line-height: 1.5; color: #5F6F6D">{T[lang]['step1_body']}</div>
    </div>
    
    <div style="flex: 1 1 280px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
      <div style="display: flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: #172B2A; color: #B7F34A; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 20px">{T[lang]['step2_num']}</div>
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 22px; color: #172B2A">{T[lang]['step2_title']}</div>
      <div style="font-size: 17px; line-height: 1.5; color: #5F6F6D">{T[lang]['step2_body']}</div>
    </div>
    
    <div style="flex: 1 1 280px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
      <div style="display: flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: #172B2A; color: #B7F34A; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 20px">{T[lang]['step3_num']}</div>
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 22px; color: #172B2A">{T[lang]['step3_title']}</div>
      <div style="font-size: 17px; line-height: 1.5; color: #5F6F6D">{T[lang]['step3_body']}</div>
    </div>
  </div>
</section>

<!-- FAQ Section [faq] -->
<section id="faq" style="background: #F3F8F7; padding: 88px clamp(20px, 5vw, 80px); display: flex; flex-wrap: wrap; gap: 32px 64px">
  <div style="flex: 1 1 300px; min-width: 0; display: flex; flex-direction: column; gap: 14px">
    <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['faq_eyebrow']}</div>
    <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(30px, 3.3vw, 46px); line-height: 1.12; letter-spacing: -0.015em; color: #172B2A">{T[lang]['faq_heading']}</h2>
  </div>
  
  <div style="flex: 2 1 520px; min-width: 0; background: #FFFFFF; border-radius: 24px; padding: 8px clamp(18px, 2.4vw, 32px) 0">
    <details open>
      <summary>{T[lang]['faq1_q']}</summary>
      <div class="faq-body">{T[lang]['faq1_a']}</div>
    </details>
    
    <details>
      <summary>{T[lang]['faq2_q']}</summary>
      <div class="faq-body">{T[lang]['faq2_a']}</div>
    </details>
    
    <details>
      <summary>{T[lang]['faq3_q']}</summary>
      <div class="faq-body">{T[lang]['faq3_a']}</div>
    </details>
    
    <details>
      <summary>{T[lang]['faq4_q']}</summary>
      <div class="faq-body">{T[lang]['faq4_a']}</div>
    </details>
    
    <details>
      <summary>{T[lang]['faq5_q']}</summary>
      <div class="faq-body">{T[lang]['faq5_a']}</div>
    </details>
  </div>
</section>

<!-- Closing CTA Section [demo] -->
<section id="demo" style="padding: 88px clamp(20px, 5vw, 80px)">
  <div style="background: #172B2A; border-radius: 32px; padding: clamp(28px, 5vw, 72px); display: flex; flex-direction: column; align-items: center; gap: 20px; text-align: center; color: #FFFFFF">
    <h2 style="margin: 0; max-width: 820px; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(30px, 3.6vw, 50px); line-height: 1.1; letter-spacing: -0.015em; color: #FFFFFF">{T[lang]['demo_heading']}</h2>
    <p style="margin: 0; max-width: 640px; font-size: 19px; line-height: 1.55; color: #EAF3F1">{T[lang]['demo_body']}</p>
    
    <div style="max-width: 640px; border: 1px solid #3A5552; border-radius: 14px; padding: 14px 20px; font-size: 16px; line-height: 1.5; color: #EAF3F1">
      <strong style="font-weight: 600; color: #B7F34A">{T[lang]['demo_promise_lead']}</strong> {T[lang]['demo_promise_text']}
    </div>
    
    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 14px; margin-top: 8px">
      <button onclick="openDemoModal('Closing CTA Demo')" style="display: inline-flex; align-items: center; justify-content: center; min-height: 58px; min-width: 44px; padding: 0 30px; background: #B7F34A; color: #172B2A; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; border-radius: 10px; border: none; cursor: pointer">{T[lang]['demo_btn_book']}</button>
      <a href="https://t.me/GPTify_uz_bot?start=os_demo" style="display: inline-flex; align-items: center; justify-content: center; min-height: 58px; min-width: 44px; padding: 0 30px; border: 1px solid #EAF3F1; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; border-radius: 10px; text-decoration: none">{T[lang]['demo_btn_tg']}</a>
    </div>
    
    <div style="font-size: 16px; color: #EAF3F1">
      {T[lang]['demo_write_lead']} <a href="mailto:{T[lang]['demo_email']}" style="color: #B7F34A; font-weight: 600; display: inline-flex; align-items: center; min-height: 44px">{T[lang]['demo_email']}</a>
    </div>
  </div>
</section>

{footer_html}
{modal_html}
"""
    js = HOMEPAGE_JS_CODE.replace('__DATA_JSON__', industries_data_json)
    return page_html + js + "</body>\n</html>"

def generate_about_page(lang):
    canonical = "https://gptify.si/about.html" if lang == 'en' else f"https://gptify.si/{lang}/about.html"
    css_href = "style.min.css" if lang == 'en' else "../style.min.css"
    mark_href = "gptify-mark.svg" if lang == 'en' else "../gptify-mark.svg"
    header_html = generate_header(lang, 'about')
    footer_html = generate_footer(lang)
    modal_html = generate_modal(lang)

    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
  <script>if(location.protocol==='http:'&&!['localhost','127.0.0.1'].includes(location.hostname)){{location.replace('https://'+location.host+location.pathname+location.search+location.hash);}}</script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{T[lang]['about_page_title']}</title>
  <meta name="description" content="{T[lang]['about_meta_desc']}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="https://gptify.si/about.html">
  <link rel="alternate" hreflang="uz" href="https://gptify.si/uz/about.html">
  <link rel="alternate" hreflang="ru" href="https://gptify.si/ru/about.html">
  <link rel="alternate" hreflang="x-default" href="https://gptify.si/about.html">
  <link rel="stylesheet" href="{css_href}">
  <link rel="icon" href="{mark_href}" type="image/svg+xml">
  <meta property="og:title" content="{T[lang]['about_page_title']}">
  <meta property="og:description" content="{T[lang]['about_meta_desc']}">
  <meta property="og:image" content="https://gptify.si/og-image.png">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{T[lang]['about_page_title']}">
  <meta name="twitter:description" content="{T[lang]['about_meta_desc']}">
  <meta name="twitter:image" content="https://gptify.si/og-image.png">
</head>
<body>
{header_html}

<main style="padding: 64px clamp(20px, 5vw, 80px) 24px; display: flex; flex-direction: column; overflow-x: hidden">
  <div style="display: flex; flex-direction: column; gap: 20px; max-width: 900px; padding-bottom: 56px">
    <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['about_badge']}</div>
    <h1 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(36px, 4.2vw, 60px); line-height: 1.06; letter-spacing: -0.02em; color: #172B2A">{T[lang]['about_h1_lead']}</h1>
    <p style="margin: 0; font-size: 20px; line-height: 1.6; color: #5F6F6D">{T[lang]['about_intro_p']}</p>
  </div>

  <!-- The Team -->
  <div style="display: flex; flex-wrap: wrap; gap: 12px 56px; padding: 40px 0; border-top: 1px solid #DCE8E6">
    <div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['about_team_badge']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.15; letter-spacing: -0.01em; color: #172B2A">{T[lang]['about_team_h2']}</h2>
    </div>
    <div style="flex: 2 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
      <p style="margin: 0; font-size: 18px; line-height: 1.65; color: #5F6F6D">{T[lang]['about_team_p']}</p>
      
      <div style="display: flex; flex-wrap: wrap; gap: 16px">
        <div style="flex: 1 1 240px; min-width: 0; background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 22px; display: flex; flex-direction: column; gap: 12px">
          <div aria-hidden="true" style="display: flex; align-items: center; justify-content: center; width: 56px; height: 56px; border-radius: 50%; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 20px">SI</div>
          <div style="display: flex; flex-direction: column; gap: 3px">
            <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 20px; color: #172B2A">{T[lang]['team_si_name']}</div>
            <div style="font-size: 16px; line-height: 1.45; color: #172B2A">{T[lang]['team_si_role']}</div>
            <div style="font-size: 15px; color: #5F6F6D">{T[lang]['team_si_loc']}</div>
          </div>
        </div>
        
        <div style="flex: 1 1 240px; min-width: 0; background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 22px; display: flex; flex-direction: column; gap: 12px">
          <div aria-hidden="true" style="display: flex; align-items: center; justify-content: center; width: 56px; height: 56px; border-radius: 50%; background: #3730A3; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 20px">DI</div>
          <div style="display: flex; flex-direction: column; gap: 3px">
            <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 20px; color: #172B2A">{T[lang]['team_di_name']}</div>
            <div style="font-size: 16px; line-height: 1.45; color: #172B2A">{T[lang]['team_di_role']}</div>
            <div style="font-size: 15px; color: #5F6F6D">{T[lang]['team_di_loc']}</div>
          </div>
        </div>
        
        <div style="flex: 1 1 240px; min-width: 0; background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 22px; display: flex; flex-direction: column; gap: 12px">
          <div aria-hidden="true" style="display: flex; align-items: center; justify-content: center; width: 56px; height: 56px; border-radius: 50%; background: #7C3AED; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 20px">GC</div>
          <div style="display: flex; flex-direction: column; gap: 3px">
            <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 20px; color: #172B2A">{T[lang]['team_gc_name']}</div>
            <div style="font-size: 16px; line-height: 1.45; color: #172B2A">{T[lang]['team_gc_role']}</div>
            <div style="font-size: 15px; color: #5F6F6D">{T[lang]['team_gc_loc']}</div>
          </div>
        </div>
        
        <div style="flex: 1 1 240px; min-width: 0; background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 22px; display: flex; flex-direction: column; gap: 12px">
          <div aria-hidden="true" style="display: flex; align-items: center; justify-content: center; width: 56px; height: 56px; border-radius: 50%; background: #B45309; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 20px">CB</div>
          <div style="display: flex; flex-direction: column; gap: 3px">
            <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 20px; color: #172B2A">{T[lang]['team_cb_name']}</div>
            <div style="font-size: 16px; line-height: 1.45; color: #172B2A">{T[lang]['team_cb_role']}</div>
            <div style="font-size: 15px; color: #5F6F6D">{T[lang]['team_cb_loc']}</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- How we work -->
  <div style="display: flex; flex-wrap: wrap; gap: 12px 56px; padding: 40px 0; border-top: 1px solid #DCE8E6">
    <div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['about_method_badge']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.15; letter-spacing: -0.01em; color: #172B2A">{T[lang]['about_method_h2']}</h2>
    </div>
    <div style="flex: 2 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
      <p style="margin: 0; font-size: 18px; line-height: 1.65; color: #5F6F6D">{T[lang]['about_method_p']}</p>
    </div>
  </div>

  <!-- How we handle your data -->
  <div style="display: flex; flex-wrap: wrap; gap: 12px 56px; padding: 40px 0; border-top: 1px solid #DCE8E6">
    <div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['about_data_badge']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.15; letter-spacing: -0.01em; color: #172B2A">{T[lang]['about_data_h2']}</h2>
    </div>
    <div style="flex: 2 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
      <p style="margin: 0; font-size: 18px; line-height: 1.65; color: #5F6F6D">{T[lang]['about_data_p']}</p>
    </div>
  </div>

  <!-- What else we do -->
  <div style="display: flex; flex-wrap: wrap; gap: 12px 56px; padding: 40px 0; border-top: 1px solid #DCE8E6">
    <div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['about_wider_badge']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.15; letter-spacing: -0.01em; color: #172B2A">{T[lang]['about_wider_h2']}</h2>
    </div>
    <div style="flex: 2 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
      <p style="margin: 0; font-size: 18px; line-height: 1.65; color: #5F6F6D">{T[lang]['about_wider_p']}</p>
    </div>
  </div>

  <!-- Talk to us -->
  <div style="display: flex; flex-wrap: wrap; gap: 12px 56px; padding: 40px 0; border-top: 1px solid #DCE8E6">
    <div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['about_contact_badge']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.15; letter-spacing: -0.01em; color: #172B2A">{T[lang]['about_contact_h2']}</h2>
    </div>
    <div style="flex: 2 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
      <p style="margin: 0; font-size: 18px; line-height: 1.65; color: #5F6F6D">{T[lang]['about_contact_p']}</p>
      <div>
        <button onclick="openDemoModal('About Page Contact')" style="align-self: flex-start; display: inline-flex; align-items: center; justify-content: center; min-height: 56px; min-width: 44px; padding: 0 28px; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 17px; border-radius: 10px; border: none; cursor: pointer">{T[lang]['about_contact_btn']}</button>
      </div>
    </div>
  </div>
</main>

{footer_html}
{modal_html}
</body>
</html>"""

def generate_architecture_page(lang):
    canonical = "https://gptify.si/architecture.html" if lang == 'en' else f"https://gptify.si/{lang}/architecture.html"
    css_href = "style.min.css" if lang == 'en' else "../style.min.css"
    mark_href = "gptify-mark.svg" if lang == 'en' else "../gptify-mark.svg"
    header_html = generate_header(lang, 'arch')
    footer_html = generate_footer(lang)
    modal_html = generate_modal(lang)

    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
  <script>if(location.protocol==='http:'&&!['localhost','127.0.0.1'].includes(location.hostname)){{location.replace('https://'+location.host+location.pathname+location.search+location.hash);}}</script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{T[lang]['arch_page_title']}</title>
  <meta name="description" content="{T[lang]['arch_meta_desc']}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="https://gptify.si/architecture.html">
  <link rel="alternate" hreflang="uz" href="https://gptify.si/uz/architecture.html">
  <link rel="alternate" hreflang="ru" href="https://gptify.si/ru/architecture.html">
  <link rel="alternate" hreflang="x-default" href="https://gptify.si/architecture.html">
  <link rel="stylesheet" href="{css_href}">
  <link rel="icon" href="{mark_href}" type="image/svg+xml">
  <meta property="og:title" content="{T[lang]['arch_page_title']}">
  <meta property="og:description" content="{T[lang]['arch_meta_desc']}">
  <meta property="og:image" content="https://gptify.si/og-image.png">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{T[lang]['arch_page_title']}">
  <meta name="twitter:description" content="{T[lang]['arch_meta_desc']}">
  <meta name="twitter:image" content="https://gptify.si/og-image.png">
</head>
<body>
{header_html}

<main style="padding: 64px clamp(20px, 5vw, 80px) 48px; display: flex; flex-direction: column; gap: 64px; overflow-x: hidden">
  
  <!-- Header / Eyebrow -->
  <div style="display: flex; flex-direction: column; gap: 18px; max-width: 960px">
    <div style="display: inline-flex; align-items: center; gap: 8px; width: fit-content; padding: 6px 14px; border-radius: 999px; background: #F3F8F7; border: 1px solid #DCE8E6; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.12em; color: #087F6A; text-transform: uppercase">
      <span style="width: 8px; height: 8px; border-radius: 50%; background: #087F6A"></span>
      {T[lang]['arch_badge']}
    </div>
    <h1 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(34px, 4vw, 54px); line-height: 1.08; letter-spacing: -0.02em; color: #172B2A">{T[lang]['arch_title']}</h1>
    <p style="margin: 0; font-size: 19px; line-height: 1.6; color: #5F6F6D">{T[lang]['arch_sub']}</p>
  </div>

  <!-- 4 Architectural Pillars Grid -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px">
    
    <!-- Pillar 1 -->
    <div style="background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 26px; display: flex; flex-direction: column; justify-content: space-between; gap: 20px">
      <div style="display: flex; flex-direction: column; gap: 12px">
        <div style="width: 44px; height: 44px; border-radius: 12px; background: #F3F8F7; border: 1px solid #DCE8E6; display: flex; align-items: center; justify-content: center; color: #087F6A">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
        </div>
        <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 19px; color: #172B2A">{T[lang]['arch_p1_title']}</h3>
        <p style="margin: 0; font-size: 15px; line-height: 1.55; color: #5F6F6D">{T[lang]['arch_p1_desc']}</p>
      </div>
      <div style="padding-top: 14px; border-top: 1px solid #DCE8E6; display: flex; flex-wrap: wrap; gap: 6px">
        <span style="display: inline-flex; align-items: center; padding: 4px 10px; border-radius: 6px; background: #F3F8F7; border: 1px solid #DCE8E6; font-size: 13px; font-weight: 600; color: #172B2A">{T[lang]['arch_p1_tags'][0]}</span>
        <span style="display: inline-flex; align-items: center; padding: 4px 10px; border-radius: 6px; background: #F3F8F7; border: 1px solid #DCE8E6; font-size: 13px; font-weight: 600; color: #172B2A">{T[lang]['arch_p1_tags'][1]}</span>
        <span style="display: inline-flex; align-items: center; padding: 4px 10px; border-radius: 6px; background: #087F6A; color: #FFFFFF; font-size: 13px; font-weight: 600">{T[lang]['arch_p1_tags'][2]}</span>
      </div>
    </div>

    <!-- Pillar 2 -->
    <div style="background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 26px; display: flex; flex-direction: column; justify-content: space-between; gap: 20px">
      <div style="display: flex; flex-direction: column; gap: 12px">
        <div style="width: 44px; height: 44px; border-radius: 12px; background: #F3F8F7; border: 1px solid #DCE8E6; display: flex; align-items: center; justify-content: center; color: #0369A1">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
        </div>
        <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 19px; color: #172B2A">{T[lang]['arch_p2_title']}</h3>
        <p style="margin: 0; font-size: 15px; line-height: 1.55; color: #5F6F6D">{T[lang]['arch_p2_desc']}</p>
      </div>
      <div style="padding-top: 14px; border-top: 1px solid #DCE8E6; display: flex; flex-wrap: wrap; gap: 6px">
        <span style="display: inline-flex; align-items: center; padding: 4px 10px; border-radius: 6px; background: #F3F8F7; border: 1px solid #DCE8E6; font-size: 13px; font-weight: 600; color: #172B2A">{T[lang]['arch_p2_tags'][0]}</span>
        <span style="display: inline-flex; align-items: center; padding: 4px 10px; border-radius: 6px; background: #F3F8F7; border: 1px solid #DCE8E6; font-size: 13px; font-weight: 600; color: #172B2A">{T[lang]['arch_p2_tags'][1]}</span>
        <span style="display: inline-flex; align-items: center; padding: 4px 10px; border-radius: 6px; background: #0369A1; color: #FFFFFF; font-size: 13px; font-weight: 600">{T[lang]['arch_p2_tags'][2]}</span>
      </div>
    </div>

    <!-- Pillar 3 -->
    <div style="background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 26px; display: flex; flex-direction: column; justify-content: space-between; gap: 20px">
      <div style="display: flex; flex-direction: column; gap: 12px">
        <div style="width: 44px; height: 44px; border-radius: 12px; background: #F3F8F7; border: 1px solid #DCE8E6; display: flex; align-items: center; justify-content: center; color: #3730A3">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
        </div>
        <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 19px; color: #172B2A">{T[lang]['arch_p3_title']}</h3>
        <p style="margin: 0; font-size: 15px; line-height: 1.55; color: #5F6F6D">{T[lang]['arch_p3_desc']}</p>
      </div>
      <div style="padding-top: 14px; border-top: 1px solid #DCE8E6; display: flex; flex-wrap: wrap; gap: 6px">
        <span style="display: inline-flex; align-items: center; padding: 4px 10px; border-radius: 6px; background: #F3F8F7; border: 1px solid #DCE8E6; font-size: 13px; font-weight: 600; color: #172B2A">{T[lang]['arch_p3_tags'][0]}</span>
        <span style="display: inline-flex; align-items: center; padding: 4px 10px; border-radius: 6px; background: #F3F8F7; border: 1px solid #DCE8E6; font-size: 13px; font-weight: 600; color: #172B2A">{T[lang]['arch_p3_tags'][1]}</span>
        <span style="display: inline-flex; align-items: center; padding: 4px 10px; border-radius: 6px; background: #3730A3; color: #FFFFFF; font-size: 13px; font-weight: 600">{T[lang]['arch_p3_tags'][2]}</span>
      </div>
    </div>

    <!-- Pillar 4 -->
    <div style="background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 26px; display: flex; flex-direction: column; justify-content: space-between; gap: 20px">
      <div style="display: flex; flex-direction: column; gap: 12px">
        <div style="width: 44px; height: 44px; border-radius: 12px; background: #F3F8F7; border: 1px solid #DCE8E6; display: flex; align-items: center; justify-content: center; color: #B45309">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
        </div>
        <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 19px; color: #172B2A">{T[lang]['arch_p4_title']}</h3>
        <p style="margin: 0; font-size: 15px; line-height: 1.55; color: #5F6F6D">{T[lang]['arch_p4_desc']}</p>
      </div>
      <div style="padding-top: 14px; border-top: 1px solid #DCE8E6; display: flex; flex-wrap: wrap; gap: 6px">
        <span style="display: inline-flex; align-items: center; padding: 4px 10px; border-radius: 6px; background: #F3F8F7; border: 1px solid #DCE8E6; font-size: 13px; font-weight: 600; color: #172B2A">{T[lang]['arch_p4_tags'][0]}</span>
        <span style="display: inline-flex; align-items: center; padding: 4px 10px; border-radius: 6px; background: #F3F8F7; border: 1px solid #DCE8E6; font-size: 13px; font-weight: 600; color: #172B2A">{T[lang]['arch_p4_tags'][1]}</span>
        <span style="display: inline-flex; align-items: center; padding: 4px 10px; border-radius: 6px; background: #B45309; color: #FFFFFF; font-size: 13px; font-weight: 600">{T[lang]['arch_p4_tags'][2]}</span>
      </div>
    </div>
  </div>

  <!-- Developer API Console Block -->
  <div style="background: #172B2A; border-radius: 28px; padding: clamp(24px, 4vw, 44px); display: flex; flex-direction: column; gap: 24px; color: #FFFFFF">
    
    <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px; border-bottom: 1px solid rgba(220, 232, 230, 0.15); padding-bottom: 18px">
      <div style="display: flex; align-items: center; gap: 12px">
        <span style="display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; border-radius: 6px; background: #087F6A; font-family: monospace; font-size: 13px; font-weight: 700; color: #FFFFFF">POST</span>
        <span style="font-family: monospace; font-size: 15px; color: #EAF3F1">https://api.gptify.co/v1/fleet/dispatch</span>
        <span style="font-size: 13px; color: #C9DAD7; margin-left: 8px">({T[lang]['api_req_badge']})</span>
      </div>
      
      <!-- Code Snippet Switcher Tabs -->
      <div role="tablist" style="display: flex; gap: 4px; background: rgba(255, 255, 255, 0.08); padding: 4px; border-radius: 10px">
        <button id="tab-curl" onclick="switchApiTab('curl')" style="min-height: 36px; padding: 0 14px; border-radius: 8px; font-size: 14px; font-weight: 600; background: #B7F34A; color: #172B2A; border: none; cursor: pointer">cURL</button>
        <button id="tab-py" onclick="switchApiTab('py')" style="min-height: 36px; padding: 0 14px; border-radius: 8px; font-size: 14px; font-weight: 600; background: transparent; color: #FFFFFF; border: none; cursor: pointer">Python</button>
        <button id="tab-node" onclick="switchApiTab('node')" style="min-height: 36px; padding: 0 14px; border-radius: 8px; font-size: 14px; font-weight: 600; background: transparent; color: #FFFFFF; border: none; cursor: pointer">Node.js</button>
      </div>
    </div>

    <!-- Code & Response Grid -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px">
      
      <!-- Code Column -->
      <div style="background: rgba(0, 0, 0, 0.25); border-radius: 16px; padding: 20px; font-family: monospace; font-size: 13px; line-height: 1.6; overflow-x: auto; color: #EAF3F1">
        <div id="code-curl">
curl -X POST https://api.gptify.co/v1/fleet/dispatch \\
  -H "Authorization: Bearer gptify_sec_live_7f8a92bc4e1..." \\
  -H "Content-Type: application/json" \\
  -d '{{
    "tenant_id": "clinic_tashkent_medpro",
    "channel": "telegram",
    "customer": {{
      "phone": "+998901234567",
      "telegram_id": 849201948
    }},
    "input_payload": {{
      "type": "text",
      "content": "Ertaga soat 16:00 ga qabulga yozilmoqchiman"
    }},
    "fleet_routing": ["ailo", "bandla", "ildam"]
  }}'
        </div>
        <div id="code-py" style="display: none">
import httpx

async with httpx.AsyncClient() as client:
    resp = await client.post(
        "https://api.gptify.co/v1/fleet/dispatch",
        headers={{"Authorization": "Bearer gptify_sec_live_7f8a92bc4e1..."}},
        json={{
            "tenant_id": "clinic_tashkent_medpro",
            "channel": "telegram",
            "customer": {{"phone": "+998901234567"}},
            "input_payload": {{"type": "text", "content": "Booking inquiry"}},
            "fleet_routing": ["ailo", "bandla", "ildam"]
        }}
    )
    data = resp.json()
    print("Execution ID:", data["execution_id"])
        </div>
        <div id="code-node" style="display: none">
import {{ GPTifyOSClient }} from '@gptify/sdk';

const client = new GPTifyOSClient({{ apiKey: process.env.GPTIFY_SECRET_KEY }});

const res = await client.fleet.dispatch({{
  tenantId: 'clinic_tashkent_medpro',
  channel: 'telegram',
  customer: {{ phone: '+998901234567' }},
  inputPayload: {{ type: 'text', content: 'Booking inquiry' }},
  fleetRouting: ['ailo', 'bandla', 'ildam']
}});

console.log('Status:', res.status, res.execution_id);
        </div>
      </div>

      <!-- Telemetry Response Column -->
      <div style="background: rgba(0, 0, 0, 0.4); border-radius: 16px; padding: 20px; font-family: monospace; font-size: 13px; line-height: 1.6; color: #B7F34A; overflow-x: auto">
        <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(220, 232, 230, 0.15); padding-bottom: 10px; margin-bottom: 12px; font-size: 13px; color: #C9DAD7">
          <span style="color: #B7F34A; font-weight: 700">● {T[lang]['api_status']}</span>
          <span style="background: rgba(8, 127, 106, 0.4); padding: 2px 8px; border-radius: 4px; color: #FFFFFF">{T[lang]['api_coordination']}</span>
        </div>
        <pre style="margin: 0; color: #EAF3F1; font-family: inherit">{{
  "status": "success",
  "execution_id": "exe_8f912e_live",
  "engines_triaged": {{
    "ailo": {{
      "intent": "appointment_booking",
      "doctor_matched": "Dr. Rustamov",
      "confidence": 0.984
    }},
    "bandla": {{
      "slot_reserved": "2026-11-17T16:00:00+05:00",
      "booking_ref": "BND-4821",
      "calendar_synced": true
    }},
    "ildam": {{
      "deal_id": "dl_98421",
      "stage": "appointment_confirmed",
      "balance_due": 45.00
    }}
  }}
}}</pre>
      </div>
    </div>

    <!-- Security & Encryption Badges -->
    <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px; border-top: 1px solid rgba(220, 232, 230, 0.15); padding-top: 16px; font-size: 14px; color: #C9DAD7">
      <div style="display: flex; align-items: center; gap: 8px">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#B7F34A" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
        <span>{T[lang]['api_encryption']}</span>
      </div>
      <div>
        <span>{T[lang]['api_retention']}</span>
      </div>
    </div>
  </div>

  <!-- Technical Review CTA Card -->
  <div style="background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 28px; padding: clamp(28px, 4vw, 48px); display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 24px">
    <div style="flex: 1 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(24px, 2.8vw, 34px); color: #172B2A">{T[lang]['arch_cta_title']}</h2>
      <p style="margin: 0; font-size: 17px; line-height: 1.55; color: #5F6F6D">{T[lang]['arch_cta_desc']}</p>
    </div>
    <button onclick="openDemoModal('Architecture Technical Review')" style="display: inline-flex; align-items: center; justify-content: center; min-height: 56px; min-width: 44px; padding: 0 32px; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 17px; border-radius: 10px; border: none; cursor: pointer">{T[lang]['arch_cta_btn']}</button>
  </div>
</main>

{footer_html}
{modal_html}

<script>
function switchApiTab(tab) {{
  var tabs = ['curl', 'py', 'node'];
  tabs.forEach(function(t) {{
    var btn = document.getElementById('tab-' + t);
    var code = document.getElementById('code-' + t);
    if (t === tab) {{
      if (btn) {{
        btn.style.background = '#B7F34A';
        btn.style.color = '#172B2A';
      }}
      if (code) code.style.display = 'block';
    }} else {{
      if (btn) {{
        btn.style.background = 'transparent';
        btn.style.color = '#FFFFFF';
      }}
      if (code) code.style.display = 'none';
    }}
  }});
}}
</script>
</body>
</html>"""

def generate_404_page():
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
  <script>if(location.protocol==='http:'&&!['localhost','127.0.0.1'].includes(location.hostname)){{location.replace('https://'+location.host+location.pathname+location.search+location.hash);}}</script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>404 - Page Not Found | GPTify OS</title>
  <link rel="stylesheet" href="/style.min.css">
  <link rel="icon" href="/gptify-mark.svg" type="image/svg+xml">
</head>
<body style="min-height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 24px">
  <div style="max-width: 480px; display: flex; flex-direction: column; align-items: center; gap: 16px">
    <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 72px; font-weight: 700; color: #087F6A; line-height: 1">404</div>
    <h1 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 26px; font-weight: 700; color: #172B2A">{T['en']['err404_title']}</h1>
    <p style="margin: 0; font-size: 16px; color: #5F6F6D; line-height: 1.5">{T['en']['err404_p']}</p>
    <a href="/" style="display: inline-flex; align-items: center; justify-content: center; min-height: 48px; min-width: 44px; padding: 0 24px; background: #087F6A; color: #FFFFFF; font-weight: 600; border-radius: 10px; text-decoration: none; margin-top: 8px">{T['en']['err404_btn']}</a>
  </div>
</body>
</html>"""

def generate_sitemap():
    return """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://gptify.si/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://gptify.si/"/>
    <xhtml:link rel="alternate" hreflang="uz" href="https://gptify.si/uz/"/>
    <xhtml:link rel="alternate" hreflang="ru" href="https://gptify.si/ru/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://gptify.si/"/>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://gptify.si/uz/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://gptify.si/"/>
    <xhtml:link rel="alternate" hreflang="uz" href="https://gptify.si/uz/"/>
    <xhtml:link rel="alternate" hreflang="ru" href="https://gptify.si/ru/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://gptify.si/"/>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://gptify.si/ru/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://gptify.si/"/>
    <xhtml:link rel="alternate" hreflang="uz" href="https://gptify.si/uz/"/>
    <xhtml:link rel="alternate" hreflang="ru" href="https://gptify.si/ru/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://gptify.si/"/>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://gptify.si/about.html</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://gptify.si/about.html"/>
    <xhtml:link rel="alternate" hreflang="uz" href="https://gptify.si/uz/about.html"/>
    <xhtml:link rel="alternate" hreflang="ru" href="https://gptify.si/ru/about.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://gptify.si/about.html"/>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://gptify.si/uz/about.html</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://gptify.si/about.html"/>
    <xhtml:link rel="alternate" hreflang="uz" href="https://gptify.si/uz/about.html"/>
    <xhtml:link rel="alternate" hreflang="ru" href="https://gptify.si/ru/about.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://gptify.si/about.html"/>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://gptify.si/ru/about.html</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://gptify.si/about.html"/>
    <xhtml:link rel="alternate" hreflang="uz" href="https://gptify.si/uz/about.html"/>
    <xhtml:link rel="alternate" hreflang="ru" href="https://gptify.si/ru/about.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://gptify.si/about.html"/>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://gptify.si/architecture.html</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://gptify.si/architecture.html"/>
    <xhtml:link rel="alternate" hreflang="uz" href="https://gptify.si/uz/architecture.html"/>
    <xhtml:link rel="alternate" hreflang="ru" href="https://gptify.si/ru/architecture.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://gptify.si/architecture.html"/>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://gptify.si/uz/architecture.html</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://gptify.si/architecture.html"/>
    <xhtml:link rel="alternate" hreflang="uz" href="https://gptify.si/uz/architecture.html"/>
    <xhtml:link rel="alternate" hreflang="ru" href="https://gptify.si/ru/architecture.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://gptify.si/architecture.html"/>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://gptify.si/ru/architecture.html</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://gptify.si/architecture.html"/>
    <xhtml:link rel="alternate" hreflang="uz" href="https://gptify.si/uz/architecture.html"/>
    <xhtml:link rel="alternate" hreflang="ru" href="https://gptify.si/ru/architecture.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://gptify.si/architecture.html"/>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://gptify.si/privacy.html</loc>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://gptify.si/terms.html</loc>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
</urlset>"""

def main():
    print("Writing deploy_os/style.min.css...")
    with open(os.path.join(BASE_DIR, 'style.min.css'), 'w', encoding='utf-8') as f:
        f.write(get_css())

    for lang in ['en', 'uz', 'ru']:
        print(f"Generating homepage for {lang}...")
        html = generate_homepage(lang)
        if lang == 'en':
            path = os.path.join(BASE_DIR, 'index.html')
        else:
            lang_dir = os.path.join(BASE_DIR, lang)
            os.makedirs(lang_dir, exist_ok=True)
            path = os.path.join(lang_dir, 'index.html')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

    for lang in ['en', 'uz', 'ru']:
        print(f"Generating about page for {lang}...")
        html = generate_about_page(lang)
        if lang == 'en':
            path = os.path.join(BASE_DIR, 'about.html')
        else:
            lang_dir = os.path.join(BASE_DIR, lang)
            os.makedirs(lang_dir, exist_ok=True)
            path = os.path.join(lang_dir, 'about.html')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

    for lang in ['en', 'uz', 'ru']:
        print(f"Generating architecture page for {lang}...")
        html = generate_architecture_page(lang)
        if lang == 'en':
            path = os.path.join(BASE_DIR, 'architecture.html')
        else:
            lang_dir = os.path.join(BASE_DIR, lang)
            os.makedirs(lang_dir, exist_ok=True)
            path = os.path.join(lang_dir, 'architecture.html')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

    print("Generating deploy_os/404.html...")
    with open(os.path.join(BASE_DIR, '404.html'), 'w', encoding='utf-8') as f:
        f.write(generate_404_page())

    print("Generating deploy_os/sitemap.xml...")
    with open(os.path.join(BASE_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(generate_sitemap())

    print("Site generation complete!")

if __name__ == '__main__':
    main()
