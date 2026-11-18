# -*- coding: utf-8 -*-
"""
build_site.py
Complete builder for gptify.si clinic redesign.
"""
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRANS_JSON = os.path.join(BASE_DIR, 'translations_all.json')

with open(TRANS_JSON, encoding='utf-8') as f:
    T = json.load(f)

SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzM3GZEDsWDc-3SUI4sySAWnJFn6ZolQaYkwo7W4VWG-79J3WVLYeQL7qs5jgAtkK_C_g/exec"

def get_css():
    return """/* GPTify OS Stylesheet */
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

button, a.btn, input[type="button"], input[type="submit"] {
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

@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.7); opacity: 0.35; }
}

@keyframes lit {
  0%, 100% { filter: brightness(1); }
  50% { filter: brightness(1.12); }
}

@keyframes floaty {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
}

.marquee-track {
  display: flex;
  width: max-content;
  animation: marq 40s linear infinite;
}

.marquee-container:hover .marquee-track {
  animation-play-state: paused;
}

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation: none !important;
    transition: none !important;
  }
}

/* Responsive Header */
.hdr-menu {
  display: none;
}

@media (max-width: 760px) {
  .hdr-nav, .hdr-lang, .hdr-cta {
    display: none !important;
  }
  .hdr-menu {
    display: inline-flex !important;
  }
}

/* Accessible focus outline */
:focus-visible {
  outline: 2px solid var(--color-teal);
  outline-offset: 2px;
}
"""

def generate_header(lang, current_page='home'):
    prefix = '/uz/' if lang == 'uz' else ('/ru/' if lang == 'ru' else '/')
    about_url = f"{prefix}about.html" if lang != 'en' else "/about.html"
    contact_url = f"{prefix}contact.html" if lang != 'en' else "/contact.html"
    arch_url = f"{prefix}architecture.html" if lang != 'en' else "/architecture.html"
    home_url = prefix
    
    if current_page == 'about':
        url_en = "/about.html"
        url_uz = "/uz/about.html"
        url_ru = "/ru/about.html"
    elif current_page == 'contact':
        url_en = "/contact.html"
        url_uz = "/uz/contact.html"
        url_ru = "/ru/contact.html"
    elif current_page == 'arch':
        url_en = "/architecture.html"
        url_uz = "/uz/architecture.html"
        url_ru = "/ru/architecture.html"
    else:
        url_en = "/"
        url_uz = "/uz/"
        url_ru = "/ru/"
        
    how_href = f"{prefix}#how" if current_page != 'home' else "#how"
    savings_href = f"{prefix}#savings" if current_page != 'home' else "#savings"
    privacy_href = f"{prefix}#privacy" if current_page != 'home' else "#privacy"
    faq_href = f"{prefix}#faq" if current_page != 'home' else "#faq"
    demo_href = f"{prefix}#demo" if current_page != 'home' else "#demo"

    en_active = 'background: #F3F8F7; font-weight: 600; color: #172B2A;' if lang == 'en' else 'color: #5F6F6D; font-weight: 500;'
    uz_active = 'background: #F3F8F7; font-weight: 600; color: #172B2A;' if lang == 'uz' else 'color: #5F6F6D; font-weight: 500;'
    ru_active = 'background: #F3F8F7; font-weight: 600; color: #172B2A;' if lang == 'ru' else 'color: #5F6F6D; font-weight: 500;'

    about_active_style = 'color: #087F6A; font-weight: 600;' if current_page == 'about' else 'color: #172B2A; font-weight: 500;'
    contact_active_style = 'color: #087F6A; font-weight: 600;' if current_page == 'contact' else 'color: #172B2A; font-weight: 500;'

    return f"""<header style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px 20px; padding: 14px clamp(16px, 2.5vw, 40px); border-bottom: 1px solid #DCE8E6; background: #FFFFFF; position: sticky; top: 0; z-index: 100;">
  <a href="{home_url}" aria-label="GPTify OS home" style="display: flex; align-items: center; gap: 12px; min-height: 44px; text-decoration: none; color: #172B2A; flex-shrink: 0">
    <svg aria-hidden="true" width="38" height="38" viewBox="0 0 100 100" fill="none"><path fill="#087F6A" d="M51.4 9 A41 41 0 1 0 88 65.4 V42 H47 V58 H73.7 A25 25 0 1 1 50.9 25 Z"></path><path fill="#B7F34A" d="M61 9 H88 V36 H78 V19 H61 Z"></path></svg>
    <span style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 24px; letter-spacing: -0.01em">GPTify</span>
    <span style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 13px; color: #FFFFFF; background: #087F6A; border-radius: 6px; padding: 3px 8px">OS</span>
  </a>
  <nav aria-label="Main" class="hdr-nav" style="display: flex; flex-wrap: wrap; align-items: center; gap: 4px 14px">
    <a href="{how_href}" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; min-width: 44px; padding: 0 8px; font-size: 15px; font-weight: 500; color: #172B2A; text-decoration: none">{T[lang]['nav_how']}</a>
    <a href="{savings_href}" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; min-width: 44px; padding: 0 8px; font-size: 15px; font-weight: 500; color: #172B2A; text-decoration: none">{T[lang]['nav_savings']}</a>
    <a href="{privacy_href}" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; min-width: 44px; padding: 0 8px; font-size: 15px; font-weight: 500; color: #172B2A; text-decoration: none">{T[lang]['nav_privacy']}</a>
    <a href="{faq_href}" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; min-width: 44px; padding: 0 8px; font-size: 15px; font-weight: 500; color: #172B2A; text-decoration: none">{T[lang]['nav_faq']}</a>
    <a href="{about_url}" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; min-width: 44px; padding: 0 8px; font-size: 15px; text-decoration: none; {about_active_style}">{T[lang]['nav_about']}</a>
    <a href="{contact_url}" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; min-width: 44px; padding: 0 8px; font-size: 15px; text-decoration: none; {contact_active_style}">{T[lang]['nav_contact']}</a>
  </nav>
  <div style="display: flex; align-items: center; gap: 12px; margin-left: auto; flex-shrink: 0">
    <div class="hdr-lang" style="display: flex; align-items: center; gap: 4px" role="navigation" aria-label="Language selection">
      <a href="{url_en}" aria-current="{'true' if lang == 'en' else 'false'}" style="display: inline-flex; align-items: center; justify-content: center; min-width: 44px; min-height: 44px; font-size: 14px; border-radius: 10px; text-decoration: none; {en_active}">{T[lang]['nav_lang_en']}</a>
      <a href="{url_uz}" aria-current="{'true' if lang == 'uz' else 'false'}" style="display: inline-flex; align-items: center; justify-content: center; min-width: 44px; min-height: 44px; font-size: 14px; border-radius: 10px; text-decoration: none; {uz_active}">{T[lang]['nav_lang_uz']}</a>
      <a href="{url_ru}" aria-current="{'true' if lang == 'ru' else 'false'}" style="display: inline-flex; align-items: center; justify-content: center; min-width: 44px; min-height: 44px; font-size: 14px; border-radius: 10px; text-decoration: none; {ru_active}">{T[lang]['nav_lang_ru']}</a>
    </div>
    <a class="hdr-cta" href="{demo_href}" onclick="openLeadModal(); return false;" style="display: inline-flex; align-items: center; justify-content: center; min-height: 44px; padding: 0 20px; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 15px; border-radius: 10px; text-decoration: none">{T[lang]['nav_cta']}</a>
    <button type="button" class="hdr-menu" onclick="openMobileMenu()" aria-label="{T[lang]['mobile_menu_open']}" style="align-items: center; justify-content: center; width: 48px; height: 48px; border: 1px solid #DCE8E6; border-radius: 10px; background: transparent; color: #172B2A; cursor: pointer">
      <svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#172B2A" stroke-width="2.2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"></path></svg>
    </button>
  </div>
</header>

<!-- Mobile Menu Overlay -->
<div id="mobile-menu" style="display: none; position: fixed; inset: 0; z-index: 1000; background: rgba(23, 43, 42, 0.6); backdrop-filter: blur(4px);" onclick="if(event.target === this) closeMobileMenu()">
  <div style="position: absolute; top: 0; right: 0; bottom: 0; width: min(320px, 85vw); background: #FFFFFF; padding: 24px; display: flex; flex-direction: column; gap: 20px; box-shadow: -4px 0 24px rgba(0,0,0,0.15); overflow-y: auto;">
    <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #DCE8E6; padding-bottom: 16px;">
      <span style="font-family: 'Poppins', 'Inter', sans-serif; font-weight: 700; font-size: 20px; color: #172B2A;">GPTify <span style="font-size: 12px; background: #087F6A; color: #fff; padding: 2px 6px; border-radius: 4px;">OS</span></span>
      <button type="button" onclick="closeMobileMenu()" aria-label="{T[lang]['mobile_menu_close']}" style="display: inline-flex; align-items: center; justify-content: center; width: 44px; height: 44px; border: 1px solid #DCE8E6; border-radius: 10px; background: transparent; cursor: pointer;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#172B2A" stroke-width="2.2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"></path></svg>
      </button>
    </div>
    <nav style="display: flex; flex-direction: column; gap: 6px;">
      <a href="{how_href}" onclick="closeMobileMenu()" style="display: flex; align-items: center; min-height: 48px; padding: 0 12px; font-size: 16px; font-weight: 500; color: #172B2A; text-decoration: none; border-radius: 8px;">{T[lang]['nav_how']}</a>
      <a href="{savings_href}" onclick="closeMobileMenu()" style="display: flex; align-items: center; min-height: 48px; padding: 0 12px; font-size: 16px; font-weight: 500; color: #172B2A; text-decoration: none; border-radius: 8px;">{T[lang]['nav_savings']}</a>
      <a href="{privacy_href}" onclick="closeMobileMenu()" style="display: flex; align-items: center; min-height: 48px; padding: 0 12px; font-size: 16px; font-weight: 500; color: #172B2A; text-decoration: none; border-radius: 8px;">{T[lang]['nav_privacy']}</a>
      <a href="{faq_href}" onclick="closeMobileMenu()" style="display: flex; align-items: center; min-height: 48px; padding: 0 12px; font-size: 16px; font-weight: 500; color: #172B2A; text-decoration: none; border-radius: 8px;">{T[lang]['nav_faq']}</a>
      <a href="{about_url}" onclick="closeMobileMenu()" style="display: flex; align-items: center; min-height: 48px; padding: 0 12px; font-size: 16px; font-weight: 500; color: #172B2A; text-decoration: none; border-radius: 8px;">{T[lang]['nav_about']}</a>
      <a href="{contact_url}" onclick="closeMobileMenu()" style="display: flex; align-items: center; min-height: 48px; padding: 0 12px; font-size: 16px; font-weight: 500; color: #172B2A; text-decoration: none; border-radius: 8px;">{T[lang]['nav_contact']}</a>
    </nav>
    <div style="border-top: 1px solid #DCE8E6; padding-top: 16px; display: flex; flex-direction: column; gap: 14px;">
      <div style="font-size: 13px; font-weight: 600; color: #5F6F6D; text-transform: uppercase; letter-spacing: 0.05em;">{T[lang]['mobile_menu_lang']}</div>
      <div style="display: flex; align-items: center; gap: 8px;">
        <a href="{url_en}" style="display: inline-flex; align-items: center; justify-content: center; min-width: 44px; min-height: 44px; font-size: 15px; border-radius: 8px; text-decoration: none; {en_active}">{T[lang]['nav_lang_en']}</a>
        <a href="{url_uz}" style="display: inline-flex; align-items: center; justify-content: center; min-width: 44px; min-height: 44px; font-size: 15px; border-radius: 8px; text-decoration: none; {uz_active}">{T[lang]['nav_lang_uz']}</a>
        <a href="{url_ru}" style="display: inline-flex; align-items: center; justify-content: center; min-width: 44px; min-height: 44px; font-size: 15px; border-radius: 8px; text-decoration: none; {ru_active}">{T[lang]['nav_lang_ru']}</a>
      </div>
      <a href="{demo_href}" onclick="closeMobileMenu(); openLeadModal(); return false;" style="display: inline-flex; align-items: center; justify-content: center; min-height: 48px; padding: 0 20px; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', sans-serif; font-weight: 600; font-size: 16px; border-radius: 10px; text-decoration: none; margin-top: 8px;">{T[lang]['nav_cta']}</a>
    </div>
  </div>
</div>
"""

def generate_footer(lang):
    prefix = '/uz/' if lang == 'uz' else ('/ru/' if lang == 'ru' else '/')
    about_url = f"{prefix}about.html" if lang != 'en' else "/about.html"
    contact_url = f"{prefix}contact.html" if lang != 'en' else "/contact.html"
    arch_url = f"{prefix}architecture.html" if lang != 'en' else "/architecture.html"
    privacy_url = f"{prefix}privacy.html" if lang != 'en' else "/privacy.html"
    terms_url = f"{prefix}terms.html" if lang != 'en' else "/terms.html"

    return f"""<footer style="border-top: 1px solid #DCE8E6; padding: 36px clamp(20px, 5vw, 80px) 44px; display: flex; flex-wrap: wrap; align-items: flex-start; justify-content: space-between; gap: 24px 48px; background: #FFFFFF">
  <div style="display: flex; flex-direction: column; gap: 10px; max-width: 380px">
    <div style="display: flex; align-items: center; gap: 10px">
      <svg aria-hidden="true" width="30" height="30" viewBox="0 0 100 100" fill="none"><path fill="#087F6A" d="M51.4 9 A41 41 0 1 0 88 65.4 V42 H47 V58 H73.7 A25 25 0 1 1 50.9 25 Z"></path><path fill="#B7F34A" d="M61 9 H88 V36 H78 V19 H61 Z"></path></svg>
      <span style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 20px; color: #172B2A">GPTify OS</span>
    </div>
    <div style="font-size: 15px; line-height: 1.5; color: #5F6F6D">{T[lang]['footer_tagline']}</div>
  </div>
  <nav aria-label="Footer" style="display: flex; flex-wrap: wrap; gap: 4px 28px">
    <a href="{about_url}" style="display: inline-flex; align-items: center; min-height: 44px; min-width: 44px; font-size: 15px; font-weight: 500; color: #172B2A">{T[lang]['footer_about']}</a>
    <a href="{contact_url}" style="display: inline-flex; align-items: center; min-height: 44px; min-width: 44px; font-size: 15px; font-weight: 500; color: #172B2A">{T[lang]['footer_link_contact']}</a>
    <a href="{privacy_url}" style="display: inline-flex; align-items: center; min-height: 44px; min-width: 44px; font-size: 15px; font-weight: 500; color: #172B2A">{T[lang]['footer_privacy']}</a>
    <a href="{terms_url}" style="display: inline-flex; align-items: center; min-height: 44px; min-width: 44px; font-size: 15px; font-weight: 500; color: #172B2A">{T[lang]['footer_terms']}</a>
    <a href="{arch_url}" style="display: inline-flex; align-items: center; min-height: 44px; min-width: 44px; font-size: 15px; font-weight: 500; color: #172B2A">{T[lang]['footer_security']}</a>
  </nav>
  <div style="flex: 1 1 100%; font-size: 14px; color: #5F6F6D">© 2026 GPTify Technologies MChJ. All rights reserved.</div>
</footer>
"""

def get_modal_script(lang):
    submitting = T[lang]['modal_submitting']
    err_text = T[lang]['modal_error']
    return """
<script>
function openLeadModal(interest) {
  var modal = document.getElementById('leadModal');
  if (modal) {
    if (interest) {
      var field = document.getElementById('modalLeadInterest');
      if (field) field.value = interest;
    }
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
  }
}

function closeLeadModal() {
  var modal = document.getElementById('leadModal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
}

function openMobileMenu() {
  var m = document.getElementById('mobile-menu');
  if (m) {
    m.style.display = 'block';
    document.body.style.overflow = 'hidden';
  }
}

function closeMobileMenu() {
  var m = document.getElementById('mobile-menu');
  if (m) {
    m.style.display = 'none';
    document.body.style.overflow = '';
  }
}

function handleLeadSubmit(e) {
  e.preventDefault();
  var btn = document.getElementById('modalSubmitBtn');
  var form = document.getElementById('leadForm');
  var channels = Array.from(form.querySelectorAll('input[name="channels"]:checked')).map(function(c) { return c.value; });
  
  var payload = {
    source: 'modal',
    interest: document.getElementById('modalLeadInterest').value,
    name: document.getElementById('leadName').value,
    clinic: document.getElementById('leadCompany').value,
    contact: document.getElementById('leadContact').value,
    teamSize: document.getElementById('leadTeamSize').value,
    channels: channels.join(', '),
    timestamp: new Date().toISOString()
  };
  
  if (btn) {
    btn.disabled = true;
    btn.textContent = """ + json.dumps(submitting) + """;
  }
  
  fetch(""" + json.dumps(SCRIPT_URL) + """, {
    method: 'POST',
    mode: 'no-cors',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  }).then(function() {
    document.getElementById('modalBody').style.display = 'none';
    document.getElementById('modalSuccess').style.display = 'block';
  }).catch(function(err) {
    if (btn) {
      btn.disabled = false;
      btn.textContent = """ + json.dumps(err_text) + """;
    }
  });
}
</script>
"""

def generate_modal(lang):
    return f"""<!-- Lead Capture Modal -->
<div id="leadModal" role="dialog" aria-modal="true" aria-labelledby="modalTitle" style="display: none; position: fixed; inset: 0; z-index: 1000; background: rgba(23, 43, 42, 0.6); backdrop-filter: blur(4px); overflow-y: auto; padding: 20px" onclick="if(event.target === this) closeLeadModal()">
  <div style="position: relative; max-width: 520px; margin: 40px auto; background: #FFFFFF; border-radius: 20px; padding: clamp(24px, 4vw, 36px); box-shadow: 0 20px 40px rgba(0,0,0,0.2); border: 1px solid #DCE8E6">
    <button type="button" onclick="closeLeadModal()" aria-label="{T[lang]['modal_close']}" style="position: absolute; top: 18px; right: 18px; width: 44px; height: 44px; border-radius: 10px; background: #F3F8F7; border: 1px solid #DCE8E6; display: flex; align-items: center; justify-content: center; cursor: pointer; color: #172B2A">
      <svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18M6 6l12 12"></path></svg>
    </button>
    
    <div id="modalBody">
      <h3 id="modalTitle" style="margin: 0 0 8px; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 24px; font-weight: 700; color: #172B2A">{T[lang]['modal_title']}</h3>
      <p style="margin: 0 0 20px; font-size: 15px; color: #5F6F6D; line-height: 1.5">{T[lang]['modal_subtitle']}</p>
      
      <form id="leadForm" onsubmit="handleLeadSubmit(event)" style="display: flex; flex-direction: column; gap: 14px">
        <input type="hidden" id="modalLeadInterest" name="interest" value="Clinic Demo">
        
        <div>
          <label for="leadName" style="display: block; font-size: 14px; font-weight: 600; color: #172B2A; margin-bottom: 6px">{T[lang]['modal_name_label']}</label>
          <input type="text" id="leadName" name="name" required autocomplete="name" placeholder="{T[lang]['modal_name_ph']}" style="width: 100%; min-height: 48px; border: 1px solid #DCE8E6; border-radius: 10px; padding: 10px 14px; font-size: 16px; color: #172B2A; background: #FFFFFF; outline: none">
        </div>
        
        <div>
          <label for="leadCompany" style="display: block; font-size: 14px; font-weight: 600; color: #172B2A; margin-bottom: 6px">{T[lang]['modal_company_label']}</label>
          <input type="text" id="leadCompany" name="company" required autocomplete="organization" placeholder="{T[lang]['modal_company_ph']}" style="width: 100%; min-height: 48px; border: 1px solid #DCE8E6; border-radius: 10px; padding: 10px 14px; font-size: 16px; color: #172B2A; background: #FFFFFF; outline: none">
        </div>
        
        <div>
          <label for="leadContact" style="display: block; font-size: 14px; font-weight: 600; color: #172B2A; margin-bottom: 6px">{T[lang]['modal_phone_label']}</label>
          <input type="text" id="leadContact" name="contact" required autocomplete="tel" placeholder="{T[lang]['modal_phone_ph']}" style="width: 100%; min-height: 48px; border: 1px solid #DCE8E6; border-radius: 10px; padding: 10px 14px; font-size: 16px; color: #172B2A; background: #FFFFFF; outline: none">
        </div>
        
        <div>
          <label for="leadTeamSize" style="display: block; font-size: 14px; font-weight: 600; color: #172B2A; margin-bottom: 6px">{T[lang]['modal_team_label']}</label>
          <select id="leadTeamSize" name="teamSize" style="width: 100%; min-height: 48px; border: 1px solid #DCE8E6; border-radius: 10px; padding: 10px 14px; font-size: 16px; color: #172B2A; background: #FFFFFF; outline: none">
            <option value="1-5">{T[lang]['modal_team_opt_1']}</option>
            <option value="6-20" selected>{T[lang]['modal_team_opt_2']}</option>
            <option value="21-50">{T[lang]['modal_team_opt_3']}</option>
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
        
        <p style="margin: 4px 0 0; font-size: 13px; color: #5F6F6D; line-height: 1.4">{T[lang]['modal_privacy_note']}</p>
        
        <button type="submit" id="modalSubmitBtn" style="width: 100%; min-height: 52px; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 16px; font-weight: 600; border-radius: 10px; margin-top: 8px; cursor: pointer">
          {T[lang]['modal_submit']}
        </button>
      </form>
    </div>
    
    <div id="modalSuccess" style="display: none; text-align: center; padding: 20px 10px">
      <div style="width: 64px; height: 64px; border-radius: 50%; background: #EAF8D2; color: #087F6A; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 16px">
        <svg aria-hidden="true" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"></path></svg>
      </div>
      <h3 style="margin: 0 0 8px; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 22px; font-weight: 700; color: #172B2A">{T[lang]['modal_success_title']}</h3>
      <p style="margin: 0; font-size: 15px; color: #5F6F6D; line-height: 1.5">{T[lang]['modal_success_desc']}</p>
      <button type="button" onclick="closeLeadModal()" style="margin-top: 24px; min-height: 44px; padding: 0 24px; background: #087F6A; color: #FFFFFF; border-radius: 8px; font-weight: 600">OK</button>
    </div>
  </div>
</div>
{get_modal_script(lang)}
"""

def generate_homepage(lang):
    prefix = '/uz/' if lang == 'uz' else ('/ru/' if lang == 'ru' else '/')
    canonical = f"https://gptify.si{prefix}"
    
    chat_sub_1 = f'<div style="margin-top: 4px; font-size: 13px; line-height: 1.35; color: #5F6F6D">{T["en"]["chat_msg_1_sub"]}</div>' if lang == 'en' else ''
    chat_sub_2 = f'<div style="margin-top: 4px; font-size: 13px; line-height: 1.35; color: #C9DAD7">{T["en"]["chat_msg_2_sub"]}</div>' if lang == 'en' else ''
    chat_sub_3 = f'<div style="margin-top: 4px; font-size: 13px; line-height: 1.35; color: #5F6F6D">{T["en"]["chat_msg_3_sub"]}</div>' if lang == 'en' else ''

    unit_h = 'h' if lang == 'en' else ('soat' if lang == 'uz' else 'ч')
    sub_calc_template = (
        'About {monthly} a month · {hours} hours back every week' if lang == 'en'
        else ('Oyiga qariyb {monthly} · haftasiga {hours} soat tejaladi' if lang == 'uz'
        else 'Примерно {monthly} в месяц · {hours} часа экономии каждую неделю')
    )

    calc_script = """
<script>
function updateSavings() {
  var teamEl = document.getElementById('c-team');
  var hoursEl = document.getElementById('c-hours');
  var salaryEl = document.getElementById('c-salary');
  if (!teamEl || !hoursEl || !salaryEl) return;
  
  var team = parseInt(teamEl.value, 10) || 3;
  var hours = parseInt(hoursEl.value, 10) || 20;
  var salary = parseInt(salaryEl.value, 10) || 391;
  
  var teamVal = document.getElementById('c-team-val');
  var hoursVal = document.getElementById('c-hours-val');
  var salaryVal = document.getElementById('c-salary-val');
  
  if (teamVal) teamVal.textContent = team;
  if (hoursVal) hoursVal.textContent = hours + ' ' + (hoursVal.getAttribute('data-unit') || 'h');
  if (salaryVal) salaryVal.textContent = '$' + salary.toLocaleString('en-US');
  
  var yearly = Math.round(team * hours * 0.70 * 50 * (salary / 160));
  var monthly = Math.round(yearly / 12);
  var weeklyHours = Math.round(team * hours * 0.70);
  
  var yearEl = document.getElementById('calc-res-year');
  var subEl = document.getElementById('calc-res-sub');
  
  if (yearEl) {
    yearEl.textContent = '~$' + yearly.toLocaleString('en-US');
  }
  if (subEl) {
    var subTemplate = subEl.getAttribute('data-template') || 'About {monthly} a month · {hours} hours back every week';
    subEl.textContent = subTemplate.replace('{monthly}', '$' + monthly.toLocaleString('en-US')).replace('{hours}', weeklyHours);
  }
}
</script>
"""

    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{T[lang]['page_title']}</title>
  <meta name="description" content="{T[lang]['meta_description']}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="https://gptify.si/">
  <link rel="alternate" hreflang="uz" href="https://gptify.si/uz/">
  <link rel="alternate" hreflang="ru" href="https://gptify.si/ru/">
  <link rel="alternate" hreflang="x-default" href="https://gptify.si/">
  <link rel="stylesheet" href="/style.min.css">
  <link rel="icon" href="/gptify-app-icon.svg" type="image/svg+xml">
</head>
<body>
{generate_header(lang, current_page='home')}

<main>
  <!-- Section 2: Hero (#top) -->
  <section id="top" style="padding: clamp(32px, 4.5vw, 64px) clamp(20px, 5vw, 80px) clamp(48px, 6vw, 88px); display: flex; flex-wrap: wrap; gap: 40px 56px; align-items: flex-start; background: #FFFFFF">
    <div style="flex: 1 1 420px; min-width: 0; display: flex; flex-direction: column; gap: 22px; padding-top: 8px">
      <h1 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(34px, 3.5vw, 52px); line-height: 1.08; letter-spacing: -0.02em; color: #172B2A">
        {T[lang]['hero_h1_p1']} <span style="color: #087F6A">{T[lang]['hero_h1_p2']}</span>
      </h1>
      <p style="margin: 0; max-width: 520px; font-size: 19px; line-height: 1.5; color: #5F6F6D">
        {T[lang]['hero_sub']}
      </p>
      <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 14px 24px">
        <a href="#demo" onclick="openLeadModal(); return false;" style="display: inline-flex; align-items: center; gap: 14px; min-height: 58px; padding: 0 10px 0 26px; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; border-radius: 10px; text-decoration: none">
          {T[lang]['hero_btn_demo']}
          <span style="display: inline-flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 8px; background: #B7F34A">
            <svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#172B2A" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7"></path><path d="M8 7h9v9"></path></svg>
          </span>
        </a>
        <a href="#how" style="display: inline-flex; align-items: center; min-height: 44px; font-size: 17px; font-weight: 600; color: #087F6A">{T[lang]['hero_btn_how']}</a>
      </div>
      <div style="font-size: 15px; font-weight: 500; color: #5F6F6D">{T[lang]['hero_microcopy']}</div>
      <div style="display: inline-flex; align-items: center; gap: 10px; align-self: flex-start; padding: 8px 14px; border: 1px solid #DCE8E6; border-radius: 999px; font-size: 15px; font-weight: 500; color: #172B2A">
        <span aria-hidden="true" style="width: 9px; height: 9px; border-radius: 50%; background: #B7F34A; box-shadow: 0 0 0 3px #EAF8D2"></span>
        {T[lang]['hero_pilot_pill']}
      </div>
    </div>

    <!-- Chat Card Mockup -->
    <div style="flex: 1.15 1 480px; min-width: 0; background: #F3F8F7; border-radius: 24px; padding: clamp(14px, 1.5vw, 20px); display: flex; flex-direction: column; gap: 12px">
      <div style="background: #FFFFFF; border-radius: 18px; padding: 18px 20px; display: flex; flex-direction: column; gap: 12px">
        <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px">
          <div style="display: flex; align-items: center; gap: 12px">
            <div aria-hidden="true" style="display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 50%; background: #172B2A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 17px">M</div>
            <div style="display: flex; flex-direction: column; gap: 2px">
              <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 16px; color: #172B2A">{T[lang]['chat_clinic_name']}</div>
              <div style="font-size: 13px; font-weight: 500; color: #5F6F6D">{T[lang]['chat_clinic_sub']}</div>
            </div>
          </div>
          <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 8px">
            <div style="display: inline-flex; align-items: center; padding: 7px 12px; border-radius: 999px; background: #EAF8D2; color: #172B2A; font-size: 13px; font-weight: 600">{T[lang]['chat_lang_tag']}</div>
            <div style="display: inline-flex; align-items: center; gap: 8px; padding: 7px 12px; border-radius: 999px; background: #087F6A; color: #FFFFFF; font-size: 13px; font-weight: 600">
              <svg aria-hidden="true" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h7l-1 8 9-12h-7z"></path></svg>
              {T[lang]['chat_badge_ailo']}
            </div>
          </div>
        </div>
        <div style="display: flex; flex-direction: column; gap: 8px">
          <div style="align-self: flex-start; max-width: 86%; background: #F3F8F7; border-radius: 16px 16px 16px 4px; padding: 10px 14px; font-size: 15px; line-height: 1.4; color: #172B2A; animation: inA 10s ease infinite">
            <div>{T[lang]['chat_msg_1_text']}</div>
            {chat_sub_1}
          </div>
          <div style="align-self: flex-end; max-width: 86%; background: #172B2A; border-radius: 16px 16px 4px 16px; padding: 10px 14px; font-size: 15px; line-height: 1.4; color: #FFFFFF; animation: inB 10s ease infinite">
            <div><!-- TODO: example price 550,000 UZS -->{T[lang]['chat_msg_2_text']}</div>
            {chat_sub_2}
          </div>
          <div style="align-self: flex-start; max-width: 86%; background: #F3F8F7; border-radius: 16px 16px 16px 4px; padding: 10px 14px; font-size: 15px; line-height: 1.4; color: #172B2A; animation: inC 10s ease infinite">
            <div>{T[lang]['chat_msg_3_text']}</div>
            {chat_sub_3}
          </div>
        </div>
      </div>
      <div style="display: flex; flex-wrap: wrap; gap: 8px">
        <div style="flex: 1 1 140px; background: #087F6A; border-radius: 12px; padding: 10px 14px; color: #FFFFFF; animation: inD 10s ease infinite">
          <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 16px">Ailo</div>
          <div style="font-size: 14px; font-weight: 500; line-height: 1.3">{T[lang]['chat_chip_ailo']}</div>
        </div>
        <div style="flex: 1 1 140px; background: #7C3AED; border-radius: 12px; padding: 10px 14px; color: #FFFFFF; animation: inE 10s ease infinite">
          <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 16px">Bandla</div>
          <div style="font-size: 14px; font-weight: 500; line-height: 1.3">{T[lang]['chat_chip_bandla']}</div>
        </div>
        <div style="flex: 1 1 140px; background: #B45309; border-radius: 12px; padding: 10px 14px; color: #FFFFFF; animation: inF 10s ease infinite">
          <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 16px">ILDAM</div>
          <div style="font-size: 14px; font-weight: 500; line-height: 1.3">{T[lang]['chat_chip_ildam']}</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 3: Integrations Marquee -->
  <section aria-label="Works with" style="padding: 28px 0 36px; border-top: 1px solid #DCE8E6; display: flex; flex-direction: column; gap: 20px; background: #FFFFFF">
    <div style="text-align: center; padding: 0 clamp(20px, 5vw, 80px); font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #5F6F6D; text-transform: uppercase">
      {T[lang]['integrations_eyebrow']}
    </div>
    <div class="marquee-container" style="overflow: hidden; -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent); mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent)">
      <div class="marquee-track">
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
      </div>
    </div>
  </section>

  <!-- Section 4: The Problem (#problem) -->
  <section id="problem" style="background: #F3F8F7; padding: 80px clamp(20px, 5vw, 80px); display: flex; flex-direction: column; gap: 36px">
    <div style="display: flex; flex-direction: column; gap: 14px; max-width: 820px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['problem_eyebrow']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(30px, 3.3vw, 46px); line-height: 1.12; letter-spacing: -0.015em; color: #172B2A">{T[lang]['problem_title']}</h2>
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 16px">
      <div style="flex: 1 1 250px; min-width: 0; background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 24px; display: flex; flex-direction: column; gap: 12px">
        <div style="display: flex; align-items: center; justify-content: center; width: 52px; height: 52px; border-radius: 14px; background: #F3F8F7">
          <svg aria-hidden="true" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#087F6A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"></path></svg>
        </div>
        <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 20px; line-height: 1.3; color: #172B2A">{T[lang]['problem_c1_title']}</h3>
        <p style="margin: 0; font-size: 16px; line-height: 1.55; color: #5F6F6D">{T[lang]['problem_c1_desc']}</p>
      </div>
      <div style="flex: 1 1 250px; min-width: 0; background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 24px; display: flex; flex-direction: column; gap: 12px">
        <div style="display: flex; align-items: center; justify-content: center; width: 52px; height: 52px; border-radius: 14px; background: #F3F8F7">
          <svg aria-hidden="true" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#087F6A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"></path></svg>
        </div>
        <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 20px; line-height: 1.3; color: #172B2A">{T[lang]['problem_c2_title']}</h3>
        <p style="margin: 0; font-size: 16px; line-height: 1.55; color: #5F6F6D">{T[lang]['problem_c2_desc']}</p>
      </div>
      <div style="flex: 1 1 250px; min-width: 0; background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 24px; display: flex; flex-direction: column; gap: 12px">
        <div style="display: flex; align-items: center; justify-content: center; width: 52px; height: 52px; border-radius: 14px; background: #F3F8F7">
          <svg aria-hidden="true" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#087F6A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="2.5"></rect><path d="M3 10h18"></path><path d="M8 3v4"></path><path d="M16 3v4"></path><path d="m9.5 14 5 5"></path><path d="m14.5 14-5 5"></path></svg>
        </div>
        <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 20px; line-height: 1.3; color: #172B2A">{T[lang]['problem_c3_title']}</h3>
        <p style="margin: 0; font-size: 16px; line-height: 1.55; color: #5F6F6D">{T[lang]['problem_c3_desc']}</p>
      </div>
      <div style="flex: 1 1 250px; min-width: 0; background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 24px; display: flex; flex-direction: column; gap: 12px">
        <div style="display: flex; align-items: center; justify-content: center; width: 52px; height: 52px; border-radius: 14px; background: #F3F8F7">
          <svg aria-hidden="true" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#087F6A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"></path><path d="M14 3v6h6"></path><path d="M8 13h8"></path><path d="M8 17h5"></path></svg>
        </div>
        <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 20px; line-height: 1.3; color: #172B2A">{T[lang]['problem_c4_title']}</h3>
        <p style="margin: 0; font-size: 16px; line-height: 1.55; color: #5F6F6D">{T[lang]['problem_c4_desc']}</p>
      </div>
    </div>
  </section>

  <!-- Section 5: How It Works (#how) -->
  <section id="how" style="padding: 88px clamp(20px, 5vw, 80px); display: flex; flex-direction: column; gap: 36px; background: #FFFFFF">
    <div style="display: flex; flex-direction: column; gap: 14px; max-width: 820px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['how_eyebrow']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(30px, 3.3vw, 46px); line-height: 1.12; letter-spacing: -0.015em; color: #172B2A">{T[lang]['how_title']}</h2>
      <p style="margin: 0; font-size: 18px; line-height: 1.55; color: #5F6F6D">{T[lang]['how_sub']}</p>
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 16px">
      <article style="flex: 1 1 240px; min-width: 0; min-height: 340px; box-sizing: border-box; background: #087F6A; border-radius: 20px; padding: 30px 26px; display: flex; flex-direction: column; gap: 12px; color: #FFFFFF; animation: lit 8s ease-in-out infinite">
        <div style="font-size: 14px; font-weight: 600; letter-spacing: 0.12em">{T[lang]['how_s1_tag']}</div>
        <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 40px; line-height: 1.05; letter-spacing: -0.02em">{T[lang]['how_s1_name']}</h3>
        <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; line-height: 1.3">{T[lang]['how_s1_role']}</div>
        <p style="margin: 0; font-size: 16px; line-height: 1.55">{T[lang]['how_s1_desc']}</p>
        <div style="margin-top: auto; min-height: 44px; display: flex; align-items: flex-end; justify-content: space-between; gap: 12px; font-size: 15px; font-weight: 600; line-height: 1.3">
          {T[lang]['how_s1_next']}
          <svg aria-hidden="true" style="flex: none" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#B7F34A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg>
        </div>
      </article>
      <article style="flex: 1 1 240px; min-width: 0; min-height: 340px; box-sizing: border-box; background: #7C3AED; border-radius: 20px; padding: 30px 26px; display: flex; flex-direction: column; gap: 12px; color: #FFFFFF; animation: lit 8s ease-in-out 2s infinite">
        <div style="font-size: 14px; font-weight: 600; letter-spacing: 0.12em">{T[lang]['how_s2_tag']}</div>
        <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 40px; line-height: 1.05; letter-spacing: -0.02em">{T[lang]['how_s2_name']}</h3>
        <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; line-height: 1.3">{T[lang]['how_s2_role']}</div>
        <p style="margin: 0; font-size: 16px; line-height: 1.55">{T[lang]['how_s2_desc']}</p>
        <div style="margin-top: auto; min-height: 44px; display: flex; align-items: flex-end; justify-content: space-between; gap: 12px; font-size: 15px; font-weight: 600; line-height: 1.3">
          {T[lang]['how_s2_next']}
          <svg aria-hidden="true" style="flex: none" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#B7F34A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg>
        </div>
      </article>
      <article style="flex: 1 1 240px; min-width: 0; min-height: 340px; box-sizing: border-box; background: #B45309; border-radius: 20px; padding: 30px 26px; display: flex; flex-direction: column; gap: 12px; color: #FFFFFF; animation: lit 8s ease-in-out 4s infinite">
        <div style="font-size: 14px; font-weight: 600; letter-spacing: 0.12em">{T[lang]['how_s3_tag']}</div>
        <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 40px; line-height: 1.05; letter-spacing: -0.02em">{T[lang]['how_s3_name']}</h3>
        <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; line-height: 1.3">{T[lang]['how_s3_role']}</div>
        <p style="margin: 0; font-size: 16px; line-height: 1.55">{T[lang]['how_s3_desc']}</p>
        <div style="margin-top: auto; min-height: 44px; display: flex; align-items: flex-end; justify-content: space-between; gap: 12px; font-size: 15px; font-weight: 600; line-height: 1.3">
          {T[lang]['how_s3_next']}
          <svg aria-hidden="true" style="flex: none" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#B7F34A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg>
        </div>
      </article>
      <article style="flex: 1 1 240px; min-width: 0; min-height: 340px; box-sizing: border-box; background: #0369A1; border-radius: 20px; padding: 30px 26px; display: flex; flex-direction: column; gap: 12px; color: #FFFFFF; animation: lit 8s ease-in-out 6s infinite">
        <div style="font-size: 14px; font-weight: 600; letter-spacing: 0.12em">{T[lang]['how_s4_tag']}</div>
        <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 40px; line-height: 1.05; letter-spacing: -0.02em">{T[lang]['how_s4_name']}</h3>
        <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; line-height: 1.3">{T[lang]['how_s4_role']}</div>
        <p style="margin: 0; font-size: 16px; line-height: 1.55">{T[lang]['how_s4_desc']}</p>
        <div style="margin-top: auto; min-height: 44px; display: flex; align-items: flex-end; justify-content: space-between; gap: 12px; font-size: 15px; font-weight: 600; line-height: 1.3">
          {T[lang]['how_s4_next']}
          <svg aria-hidden="true" style="flex: none" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#B7F34A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 0 1 14-5.3L20 9"></path><path d="M20 4v5h-5"></path></svg>
        </div>
      </article>
    </div>
  </section>

  <!-- Section 6: Pilot (#pilot) -->
  <section id="pilot" style="padding: 0 clamp(20px, 5vw, 80px) 88px; background: #FFFFFF">
    <div style="border: 1px solid #DCE8E6; border-radius: 28px; padding: clamp(24px, 3.4vw, 48px); display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 24px 48px; background: #FFFFFF">
      <div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 12px">
        <div style="align-self: flex-start; display: inline-flex; align-items: center; gap: 10px; padding: 8px 14px; border-radius: 999px; background: #B7F34A; color: #172B2A; font-size: 14px; font-weight: 700">
          <span aria-hidden="true" style="width: 8px; height: 8px; border-radius: 50%; background: #172B2A; animation: pulse 2s ease-in-out infinite"></span>
          {T[lang]['pilot_badge']}
        </div>
        <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.15; color: #172B2A">
          {T[lang]['pilot_title']}
        </h2>
        <p style="margin: 0; font-size: 18px; line-height: 1.55; color: #5F6F6D">
          {T[lang]['pilot_desc']}
        </p>
      </div>
      <a href="#demo" onclick="openLeadModal(); return false;" style="display: inline-flex; align-items: center; min-height: 56px; padding: 0 28px; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 17px; border-radius: 10px; text-decoration: none">
        {T[lang]['pilot_btn']}
      </a>
    </div>
  </section>

  <!-- Section 7: Savings Calculator (#savings) -->
  <section id="savings" style="background: #F3F8F7; padding: 88px clamp(20px, 5vw, 80px); display: flex; flex-direction: column; gap: 36px">
    <div style="display: flex; flex-direction: column; gap: 14px; max-width: 820px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['calc_eyebrow']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(30px, 3.3vw, 46px); line-height: 1.12; letter-spacing: -0.015em; color: #172B2A">{T[lang]['calc_title']}</h2>
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 24px">
      <div style="flex: 1.2 1 420px; min-width: 0; background: #FFFFFF; border-radius: 24px; padding: clamp(20px, 2.6vw, 36px); display: flex; flex-direction: column; gap: 22px">
        <div style="display: flex; flex-direction: column; gap: 6px">
          <div style="display: flex; justify-content: space-between; gap: 12px; font-size: 17px; font-weight: 600; color: #172B2A">
            <label for="c-team">{T[lang]['calc_team_label']}</label>
            <span id="c-team-val" style="color: #087F6A">3</span>
          </div>
          <input id="c-team" type="range" min="1" max="50" step="1" value="3" oninput="updateSavings()" style="width: 100%; height: 44px; margin: 0; accent-color: #087F6A">
        </div>
        <div style="display: flex; flex-direction: column; gap: 6px">
          <div style="display: flex; justify-content: space-between; gap: 12px; font-size: 17px; font-weight: 600; color: #172B2A">
            <label for="c-hours">{T[lang]['calc_hours_label']}</label>
            <span id="c-hours-val" data-unit="{unit_h}" style="color: #087F6A">20 {unit_h}</span>
          </div>
          <input id="c-hours" type="range" min="5" max="35" step="1" value="20" oninput="updateSavings()" style="width: 100%; height: 44px; margin: 0; accent-color: #087F6A">
        </div>
        <div style="display: flex; flex-direction: column; gap: 6px">
          <div style="display: flex; justify-content: space-between; gap: 12px; font-size: 17px; font-weight: 600; color: #172B2A">
            <label for="c-salary">{T[lang]['calc_salary_label']}</label>
            <span id="c-salary-val" style="color: #087F6A">$391</span>
          </div>
          <input id="c-salary" type="range" min="300" max="1500" step="1" value="391" oninput="updateSavings()" style="width: 100%; height: 44px; margin: 0; accent-color: #087F6A">
        </div>
      </div>
      <div style="flex: 1 1 340px; min-width: 0; background: #172B2A; border-radius: 24px; padding: clamp(20px, 2.6vw, 36px); display: flex; flex-direction: column; gap: 10px; color: #FFFFFF">
        <div style="font-size: 16px; font-weight: 600">{T[lang]['calc_card_title']}</div>
        <div id="calc-res-year" style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(44px, 5vw, 68px); line-height: 1; letter-spacing: -0.02em; color: #B7F34A">
          {T[lang]['calc_card_year_default']}
        </div>
        <div id="calc-res-sub" data-template="{sub_calc_template}" style="font-size: 17px; line-height: 1.45">
          {T[lang]['calc_card_sub_default']}
        </div>
        <a href="#demo" onclick="openLeadModal(); return false;" style="align-self: flex-start; display: inline-flex; align-items: center; min-height: 52px; margin-top: 14px; padding: 0 24px; background: #B7F34A; color: #172B2A; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 16px; border-radius: 10px; text-decoration: none">
          {T[lang]['calc_card_btn']}
        </a>
        <div style="margin-top: auto; padding-top: 14px; font-size: 14px; line-height: 1.45; color: #C9DAD7">
          {T[lang]['calc_disclaimer']}
        </div>
      </div>
    </div>
  </section>

  <!-- Section 8: Patient Data & Privacy (#privacy) -->
  <section id="privacy" style="padding: 88px clamp(20px, 5vw, 80px); display: flex; flex-direction: column; gap: 40px; background: #FFFFFF">
    <div style="display: flex; flex-direction: column; gap: 14px; max-width: 820px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['privacy_eyebrow']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(30px, 3.3vw, 46px); line-height: 1.12; letter-spacing: -0.015em; color: #172B2A">{T[lang]['privacy_title']}</h2>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 420px), 1fr)); gap: 32px 64px">
      <div style="flex: 1 1 240px; min-width: 0; display: flex; gap: 16px; align-items: flex-start">
        <div style="flex: none; display: flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: #172B2A">
          <svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#B7F34A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"></path></svg>
        </div>
        <div style="display: flex; flex-direction: column; gap: 6px">
          <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; line-height: 1.3; color: #172B2A">{T[lang]['privacy_p1_title']}</h3>
          <p style="margin: 0; font-size: 16px; line-height: 1.55; color: #5F6F6D">{T[lang]['privacy_p1_desc']}</p>
        </div>
      </div>
      <div style="flex: 1 1 240px; min-width: 0; display: flex; gap: 16px; align-items: flex-start">
        <div style="flex: none; display: flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: #172B2A">
          <svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#B7F34A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"></circle><path d="M4 21a8 8 0 0 1 16 0"></path></svg>
        </div>
        <div style="display: flex; flex-direction: column; gap: 6px">
          <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; line-height: 1.3; color: #172B2A">{T[lang]['privacy_p2_title']}</h3>
          <p style="margin: 0; font-size: 16px; line-height: 1.55; color: #5F6F6D">{T[lang]['privacy_p2_desc']}</p>
        </div>
      </div>
      <div style="flex: 1 1 240px; min-width: 0; display: flex; gap: 16px; align-items: flex-start">
        <div style="flex: none; display: flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: #172B2A">
          <svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#B7F34A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="10" width="16" height="11" rx="2"></rect><path d="M8 10V7a4 4 0 0 1 8 0v3"></path></svg>
        </div>
        <div style="display: flex; flex-direction: column; gap: 6px">
          <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; line-height: 1.3; color: #172B2A">{T[lang]['privacy_p3_title']}</h3>
          <p style="margin: 0; font-size: 16px; line-height: 1.55; color: #5F6F6D">{T[lang]['privacy_p3_desc']}</p>
        </div>
      </div>
      <div style="flex: 1 1 240px; min-width: 0; display: flex; gap: 16px; align-items: flex-start">
        <div style="flex: none; display: flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: #172B2A">
          <svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#B7F34A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="7" rx="2"></rect><rect x="3" y="13" width="18" height="7" rx="2"></rect><path d="M7 7.5h.01"></path><path d="M7 16.5h.01"></path></svg>
        </div>
        <div style="display: flex; flex-direction: column; gap: 6px">
          <h3 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; line-height: 1.3; color: #172B2A">{T[lang]['privacy_p4_title']}</h3>
          <p style="margin: 0; font-size: 16px; line-height: 1.55; color: #5F6F6D">{T[lang]['privacy_p4_desc']}</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 9: How We Start (#process) -->
  <section id="process" style="background: #F3F8F7; padding: 88px clamp(20px, 5vw, 80px); display: flex; flex-direction: column; gap: 32px">
    <div style="display: flex; flex-direction: column; gap: 14px; max-width: 820px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['process_eyebrow']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(30px, 3.3vw, 46px); line-height: 1.12; letter-spacing: -0.015em; color: #172B2A">{T[lang]['process_title']}</h2>
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 32px 48px">
      <div style="flex: 1 1 280px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
        <div style="display: flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: #172B2A; color: #B7F34A; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 20px">1</div>
        <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 22px; color: #172B2A">{T[lang]['process_s1_name']}</div>
        <div style="font-size: 17px; line-height: 1.5; color: #5F6F6D">{T[lang]['process_s1_desc']}</div>
      </div>
      <div style="flex: 1 1 280px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
        <div style="display: flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: #172B2A; color: #B7F34A; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 20px">2</div>
        <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 22px; color: #172B2A">{T[lang]['process_s2_name']}</div>
        <div style="font-size: 17px; line-height: 1.5; color: #5F6F6D">{T[lang]['process_s2_desc']}</div>
      </div>
      <div style="flex: 1 1 280px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
        <div style="display: flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: #172B2A; color: #B7F34A; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 20px">3</div>
        <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 22px; color: #172B2A">{T[lang]['process_s3_name']}</div>
        <div style="font-size: 17px; line-height: 1.5; color: #5F6F6D">{T[lang]['process_s3_desc']}</div>
      </div>
    </div>
    <div style="border-top: 1px solid #DCE8E6; padding-top: 24px; font-size: 16px; line-height: 1.55; color: #5F6F6D">
      {T[lang]['process_cross_industry']} <a href="#demo" onclick="openLeadModal(); return false;" style="font-weight: 600">{T[lang]['process_cross_link']}</a>
    </div>
  </section>

  <!-- Section 10: FAQ (#faq) -->
  <section id="faq" style="padding: 88px clamp(20px, 5vw, 80px); display: flex; flex-wrap: wrap; gap: 32px 64px; background: #FFFFFF">
    <div style="flex: 1 1 300px; min-width: 0; display: flex; flex-direction: column; gap: 14px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['faq_eyebrow']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(30px, 3.3vw, 46px); line-height: 1.12; letter-spacing: -0.015em; color: #172B2A">{T[lang]['faq_title']}</h2>
    </div>
    <div style="flex: 2 1 520px; min-width: 0; background: #F3F8F7; border-radius: 24px; padding: 8px clamp(18px, 2.4vw, 32px) 0">
      <details open style="border-bottom: 1px solid #DCE8E6">
        <summary style="display: flex; align-items: center; min-height: 64px; cursor: pointer; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; color: #172B2A">{T[lang]['faq_q1']}</summary>
        <p style="margin: 0 0 22px; max-width: 820px; font-size: 17px; line-height: 1.6; color: #5F6F6D">{T[lang]['faq_a1']}</p>
      </details>
      <details style="border-bottom: 1px solid #DCE8E6">
        <summary style="display: flex; align-items: center; min-height: 64px; cursor: pointer; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; color: #172B2A">{T[lang]['faq_q2']}</summary>
        <p style="margin: 0 0 22px; max-width: 820px; font-size: 17px; line-height: 1.6; color: #5F6F6D">{T[lang]['faq_a2']}</p>
      </details>
      <details style="border-bottom: 1px solid #DCE8E6">
        <summary style="display: flex; align-items: center; min-height: 64px; cursor: pointer; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; color: #172B2A">{T[lang]['faq_q3']}</summary>
        <p style="margin: 0 0 22px; max-width: 820px; font-size: 17px; line-height: 1.6; color: #5F6F6D">{T[lang]['faq_a3']}</p>
      </details>
      <details style="border-bottom: 1px solid #DCE8E6">
        <summary style="display: flex; align-items: center; min-height: 64px; cursor: pointer; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; color: #172B2A">{T[lang]['faq_q4']}</summary>
        <p style="margin: 0 0 22px; max-width: 820px; font-size: 17px; line-height: 1.6; color: #5F6F6D">{T[lang]['faq_a4']}</p>
      </details>
      <details style="border-bottom: 1px solid #DCE8E6">
        <summary style="display: flex; align-items: center; min-height: 64px; cursor: pointer; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; color: #172B2A">{T[lang]['faq_q5']}</summary>
        <p style="margin: 0 0 22px; max-width: 820px; font-size: 17px; line-height: 1.6; color: #5F6F6D">{T[lang]['faq_a5']}</p>
      </details>
      <details style="border-bottom: 1px solid #DCE8E6">
        <summary style="display: flex; align-items: center; min-height: 64px; cursor: pointer; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 19px; color: #172B2A">{T[lang]['faq_q6']}</summary>
        <p style="margin: 0 0 22px; max-width: 820px; font-size: 17px; line-height: 1.6; color: #5F6F6D">{T[lang]['faq_a6']}</p>
      </details>
    </div>
  </section>

  <!-- Section 11: Closing Demo CTA (#demo) -->
  <section id="demo" style="padding: 0 clamp(20px, 5vw, 80px) 88px; background: #FFFFFF">
    <div style="background: #172B2A; border-radius: 32px; padding: clamp(28px, 5vw, 72px); display: flex; flex-direction: column; align-items: center; gap: 20px; text-align: center; color: #FFFFFF">
      <h2 style="margin: 0; max-width: 820px; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(30px, 3.6vw, 50px); line-height: 1.1; letter-spacing: -0.015em; color: #FFFFFF">
        {T[lang]['demo_title']}
      </h2>
      <p style="margin: 0; max-width: 640px; font-size: 19px; line-height: 1.55; color: #EAF3F1">
        {T[lang]['demo_sub']}
      </p>
      <div style="max-width: 640px; border: 1px solid #3A5552; border-radius: 14px; padding: 14px 20px; font-size: 16px; line-height: 1.5; color: #EAF3F1">
        {T[lang]['demo_promise']}
      </div>
      <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 14px; margin-top: 8px">
        <a href="#book" onclick="openLeadModal(); return false;" style="display: inline-flex; align-items: center; min-height: 58px; padding: 0 30px; background: #B7F34A; color: #172B2A; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; border-radius: 10px; text-decoration: none">
          {T[lang]['demo_btn_book']}
        </a>
        <a href="https://t.me/GPTify_uz_bot?start=os_demo" style="display: inline-flex; align-items: center; min-height: 58px; padding: 0 30px; border: 1px solid #EAF3F1; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; border-radius: 10px; text-decoration: none">
          {T[lang]['demo_btn_tg']}
        </a>
      </div>
      <div style="font-size: 16px; color: #EAF3F1">
        {T[lang]['demo_write_lead']} <a href="mailto:team@gptify.co" style="display: inline-flex; align-items: center; min-height: 44px; color: #B7F34A; font-weight: 600">team@gptify.co</a>
      </div>
    </div>
  </section>
</main>

{generate_footer(lang)}
{generate_modal(lang)}
{calc_script}
</body>
</html>
"""

def generate_about_page(lang):
    prefix = '/uz/' if lang == 'uz' else ('/ru/' if lang == 'ru' else '/')
    canonical = f"https://gptify.si{prefix}about.html"

    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{T[lang]['about_page_title']}</title>
  <meta name="description" content="{T[lang]['about_meta_desc']}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="https://gptify.si/about.html">
  <link rel="alternate" hreflang="uz" href="https://gptify.si/uz/about.html">
  <link rel="alternate" hreflang="ru" href="https://gptify.si/ru/about.html">
  <link rel="alternate" hreflang="x-default" href="https://gptify.si/about.html">
  <link rel="stylesheet" href="/style.min.css">
  <link rel="icon" href="/gptify-app-icon.svg" type="image/svg+xml">
</head>
<body>
{generate_header(lang, current_page='about')}

<main style="padding: 64px clamp(20px, 5vw, 80px) 24px; display: flex; flex-direction: column; background: #FFFFFF">
  <div style="display: flex; flex-direction: column; gap: 20px; max-width: 900px; padding-bottom: 56px">
    <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['about_badge']}</div>
    <h1 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(36px, 4.2vw, 60px); line-height: 1.06; letter-spacing: -0.02em; color: #172B2A">
      {T[lang]['about_h1_p1']} <span style="color: #087F6A">{T[lang]['about_h1_p2']}</span>
    </h1>
    <p style="margin: 0; font-size: 20px; line-height: 1.6; color: #5F6F6D">
      {T[lang]['about_intro_p']}
    </p>
  </div>

  <!-- The Team -->
  <div style="display: flex; flex-wrap: wrap; gap: 12px 56px; padding: 40px 0; border-top: 1px solid #DCE8E6">
    <div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['about_team_eyebrow']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.15; letter-spacing: -0.01em; color: #172B2A">{T[lang]['about_team_title']}</h2>
    </div>
    <div style="flex: 2 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
      <p style="margin: 0; font-size: 18px; line-height: 1.65; color: #5F6F6D">{T[lang]['about_team_intro']}</p>
      <div style="display: flex; flex-wrap: wrap; gap: 16px">
        <div style="flex: 1 1 260px; min-width: 0; background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 22px; display: flex; flex-direction: column; gap: 12px">
          <div aria-hidden="true" style="display: flex; align-items: center; justify-content: center; width: 56px; height: 56px; border-radius: 50%; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 20px">SI</div>
          <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 20px; color: #172B2A">{T[lang]['team_si_name']}</div>
          <div style="font-size: 16px; line-height: 1.45; color: #172B2A">{T[lang]['team_si_role']}</div>
          <div style="font-size: 15px; color: #5F6F6D">{T[lang]['team_si_loc']}</div>
        </div>
        <div style="flex: 1 1 260px; min-width: 0; background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 22px; display: flex; flex-direction: column; gap: 12px">
          <div aria-hidden="true" style="display: flex; align-items: center; justify-content: center; width: 56px; height: 56px; border-radius: 50%; background: #3730A3; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: 20px">DI</div>
          <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 20px; color: #172B2A">{T[lang]['team_di_name']}</div>
          <div style="font-size: 16px; line-height: 1.45; color: #172B2A">{T[lang]['team_di_role']}</div>
          <div style="font-size: 15px; color: #5F6F6D">{T[lang]['team_di_loc']}</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Our Method -->
  <div style="display: flex; flex-wrap: wrap; gap: 12px 56px; padding: 40px 0; border-top: 1px solid #DCE8E6">
    <div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['about_method_eyebrow']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.15; letter-spacing: -0.01em; color: #172B2A">{T[lang]['about_method_title']}</h2>
    </div>
    <div style="flex: 2 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
      <p style="margin: 0; font-size: 18px; line-height: 1.65; color: #5F6F6D">{T[lang]['about_method_p']}</p>
    </div>
  </div>

  <!-- Your Data -->
  <div style="display: flex; flex-wrap: wrap; gap: 12px 56px; padding: 40px 0; border-top: 1px solid #DCE8E6">
    <div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['about_data_eyebrow']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.15; letter-spacing: -0.01em; color: #172B2A">{T[lang]['about_data_title']}</h2>
    </div>
    <div style="flex: 2 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
      <p style="margin: 0; font-size: 18px; line-height: 1.65; color: #5F6F6D">
        {T[lang]['about_data_p']}
      </p>
    </div>
  </div>

  <!-- The Wider GPTify -->
  <div style="display: flex; flex-wrap: wrap; gap: 12px 56px; padding: 40px 0; border-top: 1px solid #DCE8E6">
    <div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['about_wider_eyebrow']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.15; letter-spacing: -0.01em; color: #172B2A">{T[lang]['about_wider_title']}</h2>
    </div>
    <div style="flex: 2 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
      <p style="margin: 0; font-size: 18px; line-height: 1.65; color: #5F6F6D">
        {T[lang]['about_wider_p']}
      </p>
    </div>
  </div>

  <!-- Contact -->
  <div style="display: flex; flex-wrap: wrap; gap: 12px 56px; padding: 40px 0; border-top: 1px solid #DCE8E6">
    <div style="flex: 1 1 260px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['about_talk_eyebrow']}</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(26px, 2.6vw, 36px); line-height: 1.15; letter-spacing: -0.01em; color: #172B2A">{T[lang]['about_talk_title']}</h2>
    </div>
    <div style="flex: 2 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
      <p style="margin: 0; font-size: 18px; line-height: 1.65; color: #5F6F6D">{T[lang]['about_talk_p']}</p>
      <a href="#demo" onclick="openLeadModal(); return false;" style="align-self: flex-start; display: inline-flex; align-items: center; min-height: 56px; padding: 0 28px; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 17px; border-radius: 10px; text-decoration: none">
        {T[lang]['nav_cta']}
      </a>
    </div>
  </div>
</main>

{generate_footer(lang)}
{generate_modal(lang)}
</body>
</html>
"""

def generate_contact_page(lang):
    prefix = '/uz/' if lang == 'uz' else ('/ru/' if lang == 'ru' else '/')
    canonical = f"https://gptify.si{prefix}contact.html"

    success_msg = (
        'Thank you! Your request has been received. We will contact you shortly.' if lang == 'en'
        else ('Rahmat! So‘rovingiz qabul qilindi. Tez orada siz bilan bog‘lanamiz.' if lang == 'uz'
        else 'Спасибо! Ваша заявка принята. Мы свяжемся с вами в ближайшее время.')
    )

    contact_script = """
<script>
function handleContactSubmit(e) {
  e.preventDefault();
  var form = document.getElementById('contactForm');
  var btn = document.getElementById('contactSubmitBtn');
  var name = document.getElementById('c-name').value;
  var contact = document.getElementById('c-contact').value;
  var clinic = document.getElementById('c-clinic').value;
  var size = document.getElementById('c-size').value;
  var msg = document.getElementById('c-msg').value;
  
  if (btn) {
    btn.disabled = true;
    btn.textContent = '...';
  }
  
  var payload = {
    source: 'contact',
    name: name,
    contact: contact,
    clinic: clinic,
    teamSize: size,
    notes: msg,
    timestamp: new Date().toISOString()
  };
  
  fetch(""" + json.dumps(SCRIPT_URL) + """, {
    method: 'POST',
    mode: 'no-cors',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  }).then(function() {
    form.innerHTML = '<div style="padding: 36px 24px; background: #EAF8D2; border-radius: 16px; border: 1px solid #B7F34A; color: #172B2A; text-align: center;">' +
      '<div style="width: 56px; height: 56px; border-radius: 50%; background: #087F6A; color: #FFFFFF; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 16px;">' +
      '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"></path></svg></div>' +
      '<div style="font-family: Poppins, sans-serif; font-weight: 700; font-size: 20px; margin-bottom: 8px;">' + """ + json.dumps(success_msg) + """ + '</div>' +
      '</div>';
  }).catch(function(err) {
    if (btn) {
      btn.disabled = false;
      btn.textContent = 'Error. Try again';
    }
  });
}
</script>
"""

    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{T[lang]['contact_page_title']}</title>
  <meta name="description" content="{T[lang]['contact_meta_desc']}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="https://gptify.si/contact.html">
  <link rel="alternate" hreflang="uz" href="https://gptify.si/uz/contact.html">
  <link rel="alternate" hreflang="ru" href="https://gptify.si/ru/contact.html">
  <link rel="alternate" hreflang="x-default" href="https://gptify.si/contact.html">
  <link rel="stylesheet" href="/style.min.css">
  <link rel="icon" href="/gptify-app-icon.svg" type="image/svg+xml">
</head>
<body>
{generate_header(lang, current_page='contact')}

<main style="padding: 64px clamp(20px, 5vw, 80px) 88px; display: flex; flex-direction: column; gap: 48px; background: #FFFFFF">
  <div style="display: flex; flex-direction: column; gap: 18px; max-width: 820px">
    <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['contact_eyebrow']}</div>
    <h1 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(34px, 3.6vw, 52px); line-height: 1.08; letter-spacing: -0.02em; color: #172B2A">
      {T[lang]['contact_h1_p1']} <span style="color: #087F6A">{T[lang]['contact_h1_p2']}</span>
    </h1>
    <p style="margin: 0; font-size: 19px; line-height: 1.55; color: #5F6F6D">{T[lang]['contact_sub']}</p>
  </div>
  <div style="display: flex; flex-wrap: wrap; gap: 40px 64px; align-items: flex-start">
    <div style="flex: 1 1 360px; min-width: 0; display: flex; flex-direction: column">
      <div style="display: flex; gap: 16px; align-items: flex-start; padding: 20px 0; border-bottom: 1px solid #DCE8E6">
        <div style="flex: none; display: flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: #F3F8F7">
          <svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#087F6A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21 4-18 7 6 2 2 6 3-4 5 4z"></path><path d="m9 13 12-9"></path></svg>
        </div>
        <div style="display: flex; flex-direction: column; gap: 4px; min-width: 0">
          <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; color: #172B2A">{T[lang]['contact_tg_title']}</div>
          <a href="https://t.me/GPTify_uz_bot?start=os_demo" style="display: inline-flex; align-items: center; min-height: 44px; font-size: 17px; font-weight: 600; word-break: break-word">@GPTify_uz_bot</a>
          <div style="font-size: 15px; line-height: 1.45; color: #5F6F6D">{T[lang]['contact_tg_desc']}</div>
        </div>
      </div>
      <div style="display: flex; gap: 16px; align-items: flex-start; padding: 20px 0; border-bottom: 1px solid #DCE8E6">
        <div style="flex: none; display: flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: #F3F8F7">
          <svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#087F6A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"></rect><path d="m3 7 9 6 9-6"></path></svg>
        </div>
        <div style="display: flex; flex-direction: column; gap: 4px; min-width: 0">
          <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; color: #172B2A">{T[lang]['contact_email_title']}</div>
          <a href="mailto:team@gptify.co" style="display: inline-flex; align-items: center; min-height: 44px; font-size: 17px; font-weight: 600; word-break: break-word">team@gptify.co</a>
          <div style="font-size: 15px; line-height: 1.45; color: #5F6F6D">{T[lang]['contact_email_desc']}</div>
        </div>
      </div>
      <div style="display: flex; gap: 16px; align-items: flex-start; padding: 20px 0; border-bottom: 1px solid #DCE8E6">
        <div style="flex: none; display: flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: #F3F8F7">
          <svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#087F6A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"></circle><path d="M9.5 9a2.5 2.5 0 0 1 4.9.8c0 1.7-2.4 2.2-2.4 3.7"></path><path d="M12 17h.01"></path></svg>
        </div>
        <div style="display: flex; flex-direction: column; gap: 4px; min-width: 0">
          <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; color: #172B2A">{T[lang]['contact_support_title']}</div>
          <a href="mailto:support@gptify.co" style="display: inline-flex; align-items: center; min-height: 44px; font-size: 17px; font-weight: 600; word-break: break-word">support@gptify.co</a>
        </div>
      </div>
      <div style="display: flex; gap: 16px; align-items: flex-start; padding: 20px 0; border-bottom: 1px solid #DCE8E6">
        <div style="flex: none; display: flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 12px; background: #F3F8F7">
          <svg aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#087F6A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"></path><circle cx="12" cy="9.5" r="2.5"></circle></svg>
        </div>
        <div style="display: flex; flex-direction: column; gap: 4px; min-width: 0">
          <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 18px; color: #172B2A">{T[lang]['contact_company_title']}</div>
          <div style="font-size: 16px; color: #172B2A">{T[lang]['contact_company_name']}</div>
          <div style="font-size: 15px; color: #5F6F6D">{T[lang]['contact_company_loc']}</div>
        </div>
      </div>
    </div>

    <!-- Standalone Contact Form -->
    <form id="contactForm" onsubmit="handleContactSubmit(event)" style="flex: 1.2 1 440px; min-width: 0; background: #F3F8F7; border-radius: 24px; padding: clamp(20px, 2.6vw, 36px); display: flex; flex-direction: column; gap: 18px">
      <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 22px; color: #172B2A">{T[lang]['contact_form_title']}</div>
      <div style="display: flex; flex-direction: column; gap: 8px">
        <label for="c-name" style="font-size: 15px; font-weight: 600; color: #172B2A">{T[lang]['contact_f_name_label']}</label>
        <input id="c-name" name="name" type="text" required placeholder="{T[lang]['contact_f_name_ph']}" autocomplete="name" style="box-sizing: border-box; width: 100%; min-height: 52px; padding: 12px 14px; border: 1px solid #DCE8E6; border-radius: 10px; background: #FFFFFF; font: inherit; font-size: 16px; color: #172B2A">
      </div>
      <div style="display: flex; flex-direction: column; gap: 8px">
        <label for="c-contact" style="font-size: 15px; font-weight: 600; color: #172B2A">{T[lang]['contact_f_contact_label']}</label>
        <input id="c-contact" name="contact" type="text" required placeholder="{T[lang]['contact_f_contact_ph']}" autocomplete="tel" style="box-sizing: border-box; width: 100%; min-height: 52px; padding: 12px 14px; border: 1px solid #DCE8E6; border-radius: 10px; background: #FFFFFF; font: inherit; font-size: 16px; color: #172B2A">
      </div>
      <div style="display: flex; flex-direction: column; gap: 8px">
        <label for="c-clinic" style="font-size: 15px; font-weight: 600; color: #172B2A">{T[lang]['contact_f_clinic_label']}</label>
        <input id="c-clinic" name="clinic" type="text" required placeholder="{T[lang]['contact_f_clinic_ph']}" autocomplete="organization" style="box-sizing: border-box; width: 100%; min-height: 52px; padding: 12px 14px; border: 1px solid #DCE8E6; border-radius: 10px; background: #FFFFFF; font: inherit; font-size: 16px; color: #172B2A">
      </div>
      <div style="display: flex; flex-direction: column; gap: 8px">
        <label for="c-size" style="font-size: 15px; font-weight: 600; color: #172B2A">{T[lang]['contact_f_size_label']}</label>
        <select id="c-size" name="teamSize" style="box-sizing: border-box; width: 100%; min-height: 52px; padding: 12px 14px; border: 1px solid #DCE8E6; border-radius: 10px; background: #FFFFFF; font: inherit; font-size: 16px; color: #172B2A">
          <option>{T[lang]['contact_f_size_opt1']}</option>
          <option selected>{T[lang]['contact_f_size_opt2']}</option>
          <option>{T[lang]['contact_f_size_opt3']}</option>
          <option>{T[lang]['contact_f_size_opt4']}</option>
        </select>
      </div>
      <div style="display: flex; flex-direction: column; gap: 8px">
        <label for="c-msg" style="font-size: 15px; font-weight: 600; color: #172B2A">{T[lang]['contact_f_msg_label']}</label>
        <textarea id="c-msg" name="notes" rows="3" placeholder="{T[lang]['contact_f_msg_ph']}" style="box-sizing: border-box; width: 100%; padding: 12px 14px; border: 1px solid #DCE8E6; border-radius: 10px; background: #FFFFFF; font: inherit; font-size: 16px; color: #172B2A; resize: vertical"></textarea>
      </div>
      <button type="submit" id="contactSubmitBtn" style="align-self: flex-start; min-height: 56px; padding: 0 28px; border: 0; border-radius: 10px; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 17px; cursor: pointer">
        {T[lang]['contact_f_submit']}
      </button>
      <div style="font-size: 14px; line-height: 1.45; color: #5F6F6D">{T[lang]['contact_f_disclaimer']}</div>
    </form>
  </div>
</main>

{generate_footer(lang)}
{generate_modal(lang)}
{contact_script}
</body>
</html>
"""

def generate_architecture_page(lang):
    prefix = '/uz/' if lang == 'uz' else ('/ru/' if lang == 'ru' else '/')
    canonical = f"https://gptify.si{prefix}architecture.html"
    privacy_url = f"{prefix}privacy.html" if lang != 'en' else "/privacy.html"
    home_url = f"{prefix}#privacy"

    p3_tags = T[lang].get('arch_p3_tags', 'AES-256 · Row-Level Security')
    p4_tags = T[lang].get('arch_p4_tags', '1C ERP Webhooks · Idempotent')
    patient_lead = T[lang].get('arch_patient_lead', 'Patient data is encrypted, never sold, and never used to train AI models.')

    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{T[lang]['arch_page_title']}</title>
  <meta name="description" content="{T[lang]['arch_meta_desc']}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="https://gptify.si/architecture.html">
  <link rel="alternate" hreflang="uz" href="https://gptify.si/uz/architecture.html">
  <link rel="alternate" hreflang="ru" href="https://gptify.si/ru/architecture.html">
  <link rel="alternate" hreflang="x-default" href="https://gptify.si/architecture.html">
  <link rel="stylesheet" href="/style.min.css">
  <link rel="icon" href="/gptify-app-icon.svg" type="image/svg+xml">
</head>
<body>
{generate_header(lang, current_page='arch')}

<main style="padding: 64px clamp(20px, 5vw, 80px) 88px; display: flex; flex-direction: column; gap: 48px; background: #FFFFFF">
  <div style="display: flex; flex-direction: column; gap: 18px; max-width: 860px">
    <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; color: #087F6A; text-transform: uppercase">{T[lang]['arch_badge']}</div>
    <h1 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(34px, 4vw, 56px); line-height: 1.08; letter-spacing: -0.02em; color: #172B2A">
      {T[lang]['arch_title']}
    </h1>
    <p style="margin: 0; font-size: 19px; line-height: 1.55; color: #5F6F6D">{T[lang]['arch_sub']}</p>
  </div>

  <!-- Patient Data & Privacy Callout -->
  <div style="background: #F3F8F7; border: 1px solid #DCE8E6; border-radius: 20px; padding: 28px 32px; display: flex; flex-direction: column; gap: 12px">
    <div style="display: inline-flex; align-items: center; gap: 8px; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: 14px; font-weight: 700; color: #087F6A; text-transform: uppercase; letter-spacing: 0.08em">
      <span aria-hidden="true" style="width: 8px; height: 8px; border-radius: 50%; background: #087F6A"></span>
      {T[lang]['arch_patient_tag']}
    </div>
    <p style="margin: 0; font-size: 17px; line-height: 1.6; color: #172B2A; font-weight: 500">{patient_lead}</p>
    <div style="display: flex; flex-wrap: wrap; gap: 20px; margin-top: 4px; font-size: 15px">
      <a href="{home_url}" style="display: inline-flex; align-items: center; min-height: 44px; font-weight: 600">{T[lang]['arch_patient_link_home']} →</a>
      <a href="{privacy_url}" style="display: inline-flex; align-items: center; min-height: 44px; font-weight: 600">{T[lang]['arch_patient_link_privacy']} →</a>
    </div>
  </div>

  <!-- 4 Pillars Grid -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 340px), 1fr)); gap: 24px">
    <div style="background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 28px; display: flex; flex-direction: column; gap: 14px">
      <div style="font-size: 13px; font-weight: 600; color: #087F6A; letter-spacing: 0.08em">PILLAR 01</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 22px; color: #172B2A">{T[lang]['arch_p1_title']}</h2>
      <p style="margin: 0; font-size: 16px; line-height: 1.55; color: #5F6F6D">{T[lang]['arch_p1_desc']}</p>
      <div style="margin-top: auto; padding-top: 12px; font-size: 13px; font-weight: 600; color: #087F6A; border-top: 1px solid #F3F8F7">{T[lang]['arch_p1_tags']}</div>
    </div>
    <div style="background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 28px; display: flex; flex-direction: column; gap: 14px">
      <div style="font-size: 13px; font-weight: 600; color: #087F6A; letter-spacing: 0.08em">PILLAR 02</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 22px; color: #172B2A">{T[lang]['arch_p2_title']}</h2>
      <p style="margin: 0; font-size: 16px; line-height: 1.55; color: #5F6F6D">{T[lang]['arch_p2_desc']}</p>
      <div style="margin-top: auto; padding-top: 12px; font-size: 13px; font-weight: 600; color: #087F6A; border-top: 1px solid #F3F8F7">{T[lang]['arch_p2_tags']}</div>
    </div>
    <div style="background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 28px; display: flex; flex-direction: column; gap: 14px">
      <div style="font-size: 13px; font-weight: 600; color: #087F6A; letter-spacing: 0.08em">PILLAR 03</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 22px; color: #172B2A">{T[lang]['arch_p3_title']}</h2>
      <p style="margin: 0; font-size: 16px; line-height: 1.55; color: #5F6F6D">{T[lang]['arch_p3_desc']}</p>
      <div style="margin-top: auto; padding-top: 12px; font-size: 13px; font-weight: 600; color: #087F6A; border-top: 1px solid #F3F8F7">{p3_tags}</div>
    </div>
    <div style="background: #FFFFFF; border: 1px solid #DCE8E6; border-radius: 20px; padding: 28px; display: flex; flex-direction: column; gap: 14px">
      <div style="font-size: 13px; font-weight: 600; color: #087F6A; letter-spacing: 0.08em">PILLAR 04</div>
      <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 22px; color: #172B2A">{T[lang]['arch_p4_title']}</h2>
      <p style="margin: 0; font-size: 16px; line-height: 1.55; color: #5F6F6D">{T[lang]['arch_p4_desc']}</p>
      <div style="margin-top: auto; padding-top: 12px; font-size: 13px; font-weight: 600; color: #087F6A; border-top: 1px solid #F3F8F7">{p4_tags}</div>
    </div>
  </div>

  <!-- Closing Callout -->
  <div style="background: #172B2A; border-radius: 24px; padding: clamp(28px, 4vw, 48px); display: flex; flex-direction: column; align-items: center; text-align: center; gap: 18px; color: #FFFFFF">
    <h2 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 700; font-size: clamp(24px, 3vw, 36px); color: #FFFFFF">{T[lang]['arch_cta_title']}</h2>
    <p style="margin: 0; max-width: 620px; font-size: 17px; line-height: 1.55; color: #EAF3F1">{T[lang]['arch_cta_desc']}</p>
    <a href="#demo" onclick="openLeadModal(); return false;" style="display: inline-flex; align-items: center; min-height: 52px; padding: 0 28px; background: #B7F34A; color: #172B2A; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 16px; border-radius: 10px; text-decoration: none; margin-top: 8px">
      {T[lang]['arch_cta_btn']}
    </a>
  </div>
</main>

{generate_footer(lang)}
{generate_modal(lang)}
</body>
</html>
"""

def generate_404_page():
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page Not Found | GPTify OS</title>
  <link rel="stylesheet" href="/style.min.css">
  <link rel="icon" href="/gptify-app-icon.svg" type="image/svg+xml">
</head>
<body style="min-height: 100vh; display: flex; flex-direction: column">
{generate_header('en', current_page='404')}

<main style="flex: 1; display: flex; align-items: center; justify-content: center; padding: 64px 20px; text-align: center; background: #FFFFFF">
  <div style="max-width: 580px; display: flex; flex-direction: column; align-items: center; gap: 20px">
    <div style="font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: clamp(64px, 10vw, 100px); font-weight: 700; color: #087F6A; line-height: 1">404</div>
    <h1 style="margin: 0; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-size: clamp(24px, 3.5vw, 36px); font-weight: 700; color: #172B2A">{T['en']['err404_h1']}</h1>
    <p style="margin: 0; font-size: 17px; line-height: 1.55; color: #5F6F6D">{T['en']['err404_sub']}</p>
    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 14px; margin-top: 12px">
      <a href="/" style="display: inline-flex; align-items: center; min-height: 50px; padding: 0 24px; background: #087F6A; color: #FFFFFF; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 16px; border-radius: 10px; text-decoration: none">{T['en']['err404_btn_home']}</a>
      <a href="/contact.html" style="display: inline-flex; align-items: center; min-height: 50px; padding: 0 24px; border: 1px solid #DCE8E6; background: #F3F8F7; color: #172B2A; font-family: 'Poppins', 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 16px; border-radius: 10px; text-decoration: none">{T['en']['err404_btn_contact']}</a>
    </div>
  </div>
</main>

{generate_footer('en')}
{generate_modal('en')}
</body>
</html>
"""

def generate_sitemap():
    pages = [
        "", "about.html", "contact.html", "architecture.html", "privacy.html", "terms.html"
    ]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">')
    
    for p in pages:
        for lang in ['en', 'uz', 'ru']:
            prefix = f"{lang}/" if lang != 'en' else ""
            url = f"https://gptify.si/{prefix}{p}"
            xml.append('  <url>')
            xml.append(f'    <loc>{url}</loc>')
            for alt_lang in ['en', 'uz', 'ru']:
                alt_prefix = f"{alt_lang}/" if alt_lang != 'en' else ""
                alt_url = f"https://gptify.si/{alt_prefix}{p}"
                xml.append(f'    <xhtml:link rel="alternate" hreflang="{alt_lang}" href="{alt_url}"/>')
            xml.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="https://gptify.si/{p}"/>')
            xml.append('  </url>')
            
    xml.append('</urlset>')
    return '\n'.join(xml)

def update_legal_page(file_name, title, lang='en'):
    prefix = '/uz/' if lang == 'uz' else ('/ru/' if lang == 'ru' else '/')
    canonical = f"https://gptify.si{prefix}{file_name}"
    
    header = generate_header(lang, current_page='legal')
    footer = generate_footer(lang)
    modal = generate_modal(lang)
    
    file_path = os.path.join(BASE_DIR, file_name)
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    import re
    main_m = re.search(r'<main[^>]*>(.*?)</main>', content, re.DOTALL)
    main_content = main_m.group(1) if main_m else ""
    
    # Clean old names
    main_content = main_content.replace('George Calceo', '').replace('Chris Briest', '')
    
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | GPTify OS</title>
  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="/style.min.css">
  <link rel="icon" href="/gptify-app-icon.svg" type="image/svg+xml">
</head>
<body>
{header}
<main style="padding: 64px clamp(20px, 5vw, 80px) 88px; max-width: 900px; margin: 0 auto; background: #FFFFFF">
  {main_content}
</main>
{footer}
{modal}
</body>
</html>
"""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    print("Writing style.min.css...")
    with open(os.path.join(BASE_DIR, 'style.min.css'), 'w', encoding='utf-8') as f:
        f.write(get_css())

    for lang in ['en', 'uz', 'ru']:
        out_dir = BASE_DIR if lang == 'en' else os.path.join(BASE_DIR, lang)
        os.makedirs(out_dir, exist_ok=True)
        
        # Homepage
        print(f"Generating homepage ({lang})...")
        with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(generate_homepage(lang))
            
        # About
        print(f"Generating about ({lang})...")
        with open(os.path.join(out_dir, 'about.html'), 'w', encoding='utf-8') as f:
            f.write(generate_about_page(lang))
            
        # Contact
        print(f"Generating contact ({lang})...")
        with open(os.path.join(out_dir, 'contact.html'), 'w', encoding='utf-8') as f:
            f.write(generate_contact_page(lang))
            
        # Architecture
        print(f"Generating architecture ({lang})...")
        with open(os.path.join(out_dir, 'architecture.html'), 'w', encoding='utf-8') as f:
            f.write(generate_architecture_page(lang))

    # 404 page
    print("Generating 404.html...")
    with open(os.path.join(BASE_DIR, '404.html'), 'w', encoding='utf-8') as f:
        f.write(generate_404_page())

    # Sitemap
    print("Generating sitemap.xml...")
    with open(os.path.join(BASE_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(generate_sitemap())

    # Legal pages
    print("Updating privacy.html and terms.html...")
    update_legal_page('privacy.html', 'Privacy Policy', 'en')
    update_legal_page('terms.html', 'Terms of Service', 'en')

    print("ALL FILES GENERATED SUCCESSFULLY!")

if __name__ == '__main__':
    main()
