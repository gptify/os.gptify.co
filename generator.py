# -*- coding: utf-8 -*-
"""
Main site builder and page generator for deploy_os.
Generates:
  - deploy_os/index.html (EN)
  - deploy_os/uz/index.html (UZ)
  - deploy_os/ru/index.html (RU)
  - deploy_os/architecture.html (EN)
  - deploy_os/uz/architecture.html (UZ)
  - deploy_os/ru/architecture.html (RU)
  - deploy_os/sitemap.xml
"""

import os
import json
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Load Translations
with open(os.path.join(BASE_DIR, 'translations.json'), 'r', encoding='utf-8') as f:
    TRANSLATIONS = json.load(f)

# Common Head elements
def get_head_html(title, desc, canonical, lang, is_arch=False):
    prefix = '../' if lang in ['uz', 'ru'] else ''
    home_url = 'https://gptify.si/' if not is_arch else 'https://gptify.si/architecture.html'
    en_url = home_url
    uz_url = f"https://gptify.si/uz/{'architecture.html' if is_arch else ''}"
    ru_url = f"https://gptify.si/ru/{'architecture.html' if is_arch else ''}"

    return f"""<!DOCTYPE html>
<html lang="{lang}" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="x-default" href="{en_url}">
  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="alternate" hreflang="uz" href="{uz_url}">
  <link rel="alternate" hreflang="ru" href="{ru_url}">
  <link rel="icon" type="image/svg+xml" href="/gptify-mark.svg">

  <!-- Open Graph / Meta -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="https://gptify.si/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:type" content="image/png">

  <!-- Twitter / X -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="{canonical}">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="https://gptify.si/og-image.png">

  <!-- Fonts & Compiled Tailwind CSS -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/style.min.css">

  <style>
    :root {{
      --font-serif: 'Instrument Serif', Georgia, serif;
      --accent: #087F6A;
    }}
    body {{
      background-color: #FAF9F5;
      color: #0F172A;
      font-family: 'Plus Jakarta Sans', sans-serif;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
      text-rendering: optimizeLegibility;
      font-size: 14px;
    }}

    /* Global font size guards (Requirement E.1 & E.2) */
    p, li, label {{
      font-size: max(14px, 0.875rem);
    }}
    .font-mono, code, pre {{
      font-size: max(12px, 0.75rem);
    }}
    input[type="text"], input[type="email"], input[type="tel"], select {{
      font-size: 16px !important;
    }}

    /* Tap targets & interactive elements (Requirement E.5) */
    .lang-pill-btn {{
      min-height: 44px;
      min-width: 44px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 8px 14px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 700;
      color: #64748B;
      transition: all 0.15s ease;
      cursor: pointer;
    }}
    .lang-pill-btn.active {{
      background-color: #FFFFFF;
      color: #0F172A;
      box-shadow: 0 1px 3px rgba(15, 23, 42, 0.1);
    }}

    /* Range slider 28px thumb + hit area */
    input[type=range] {{
      -webkit-appearance: none;
      background: #E7E5DF;
      border-radius: 9999px;
      height: 8px;
      padding: 12px 0;
      cursor: pointer;
    }}
    input[type=range]::-webkit-slider-thumb {{
      -webkit-appearance: none;
      height: 28px;
      width: 28px;
      border-radius: 50%;
      background: #087F6A;
      border: 3px solid #FFFFFF;
      box-shadow: 0 2px 8px rgba(0,0,0,0.2);
      cursor: pointer;
      transition: transform 0.15s ease;
    }}
    input[type=range]::-webkit-slider-thumb:hover {{
      transform: scale(1.15);
    }}
    input[type=range]::-moz-range-thumb {{
      height: 28px;
      width: 28px;
      border-radius: 50%;
      background: #087F6A;
      border: 3px solid #FFFFFF;
      box-shadow: 0 2px 8px rgba(0,0,0,0.2);
      cursor: pointer;
    }}

    /* Pulsing status dots */
    .badge-live-pulse {{
      box-shadow: 0 0 0 0 rgba(8, 127, 106, 0.7);
      animation: pulseGreen 2.2s infinite;
    }}
    @keyframes pulseGreen {{
      0% {{ box-shadow: 0 0 0 0 rgba(8, 127, 106, 0.7); }}
      70% {{ box-shadow: 0 0 0 8px rgba(8, 127, 106, 0); }}
      100% {{ box-shadow: 0 0 0 0 rgba(8, 127, 106, 0); }}
    }}

    /* Marquee animation */
    .marquee-track {{
      display: flex;
      gap: 1.5rem;
      width: max-content;
      animation: marquee 35s linear infinite;
    }}
    @keyframes marquee {{
      0% {{ transform: translateX(0); }}
      100% {{ transform: translateX(-50%); }}
    }}
    .marquee-track:hover {{
      animation-play-state: paused;
    }}

    /* Card styling */
    .card-elevated {{
      background: #FFFFFF;
      border: 1px solid #E7E5DF;
      box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03), 0 6px 16px rgba(15, 23, 42, 0.02);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .card-elevated:hover {{
      transform: translateY(-2px);
      box-shadow: 0 14px 34px -10px rgba(15, 23, 42, 0.07);
      border-color: #D8D5CD;
    }}

    /* FAQ accordion chevron */
    details > summary {{ list-style: none; cursor: pointer; }}
    details > summary::-webkit-details-marker {{ display: none; }}
    details[open] .faq-chevron {{ transform: rotate(180deg); }}

    /* Prefers-reduced-motion media query (Requirement E.7) */
    @media (prefers-reduced-motion: reduce) {{
      *, ::before, ::after {{
        animation-duration: 0.001ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.001ms !important;
        scroll-behavior: auto !important;
      }}
      .marquee-track {{
        animation: none !important;
      }}
      .badge-live-pulse {{
        animation: none !important;
      }}
    }}
  </style>
</head>
<body class="selection:bg-emerald-100 selection:text-emerald-900">
"""

def get_nav_html(lang, is_arch=False):
    home_prefix = '/' if lang == 'en' else f'/{lang}/'
    arch_link = '/architecture.html' if lang == 'en' else f'/{lang}/architecture.html'
    
    # Active states
    en_class = 'lang-pill-btn active' if lang == 'en' else 'lang-pill-btn'
    uz_class = 'lang-pill-btn active' if lang == 'uz' else 'lang-pill-btn'
    ru_class = 'lang-pill-btn active' if lang == 'ru' else 'lang-pill-btn'
    
    en_href = '/architecture.html' if is_arch else '/'
    uz_href = '/uz/architecture.html' if is_arch else '/uz/'
    ru_href = '/ru/architecture.html' if is_arch else '/ru/'

    return f"""
  <!-- ==================== STICKY NAVIGATION ==================== -->
  <header class="sticky top-0 z-50 bg-[#FAF9F5]/92 backdrop-blur-md border-b border-divider">
    <div class="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
      <div class="flex items-center gap-4 lg:gap-6">
        <a href="{home_prefix}" class="flex items-center gap-2.5 group cursor-pointer flex-shrink-0" aria-label="GPTify OS">
          <div class="w-9 h-9 rounded-xl bg-white border border-divider flex items-center justify-center p-1.5 shadow-2xs group-hover:border-emerald-400 group-hover:shadow-xs transition-all duration-200">
            <svg class="w-full h-full" viewBox="0 0 100 100" fill="none">
              <path fill="#087F6A" d="M51.4 9 A41 41 0 1 0 88 65.4 V42 H47 V58 H73.7 A25 25 0 1 1 50.9 25 Z"/>
              <path fill="#B7F34A" d="M61 9 H88 V36 H78 V19 H61 Z"/>
            </svg>
          </div>
          <div class="flex flex-col">
            <div class="flex items-center gap-1.5">
              <span class="text-lg font-bold tracking-tight text-slateDark" style="font-family:'Poppins', sans-serif;">GPTify</span>
              <span class="bg-[#087F6A] text-white font-bold text-xs tracking-wider uppercase px-1.5 py-0.5 rounded" style="font-family:'Poppins', sans-serif;">OS</span>
            </div>
            <span class="text-xs font-mono tracking-widest text-slateMuted uppercase font-bold" data-t="navTagline">SERVICE BUSINESS AI OS</span>
          </div>
        </a>

        <!-- Desktop Navigation Links (Buyer-focused: 5 Engines, Solutions, FAQ) -->
        <nav class="hidden lg:flex items-center gap-1 xl:gap-2 text-sm font-semibold text-slate-700 pl-3 xl:pl-4 border-l border-divider" aria-label="Navigation">
          <a href="{home_prefix}#services" class="px-3 py-1.5 rounded-lg hover:text-emeraldBrand hover:bg-subtle transition-colors duration-150 cursor-pointer whitespace-nowrap" data-t="navEngines">5 Engines</a>
          <a href="{home_prefix}#solutions" class="px-3 py-1.5 rounded-lg hover:text-emeraldBrand hover:bg-subtle transition-colors duration-150 cursor-pointer whitespace-nowrap" data-t="navSolutions">Solutions</a>
          <a href="{home_prefix}#faq" class="px-3 py-1.5 rounded-lg hover:text-emeraldBrand hover:bg-subtle transition-colors duration-150 cursor-pointer whitespace-nowrap" data-t="navFaq">FAQ</a>
        </nav>
      </div>

      <div class="flex items-center gap-2 sm:gap-3 flex-shrink-0">
        <!-- 3-Language Switcher (EN / UZ / RU) - min 44px tap targets -->
        <div class="flex items-center bg-[#EAE8E1] border border-divider rounded-full p-0.5 text-xs font-mono font-bold">
          <a href="{en_href}" id="btn-lang-en" class="{en_class}">EN</a>
          <a href="{uz_href}" id="btn-lang-uz" class="{uz_class}">UZ</a>
          <a href="{ru_href}" id="btn-lang-ru" class="{ru_class}">RU</a>
        </div>

        <button type="button" id="navBookBtn" onclick="openDemoModal('Navbar')" class="hidden sm:inline-flex items-center gap-1.5 px-4 py-2.5 rounded-xl bg-emeraldBrand hover:bg-emeraldDark text-white text-sm font-bold shadow-sm transition-all duration-200 cursor-pointer whitespace-nowrap">
          <span data-t="btnBookDemo">Book a Demo</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </button>

        <!-- Mobile Menu Toggle Button -->
        <button type="button" id="mobileMenuBtn" onclick="toggleMobileMenu()" class="lg:hidden p-2.5 rounded-xl bg-white border border-divider text-slateDark hover:bg-subtle transition-colors cursor-pointer min-h-[44px] min-w-[44px] flex items-center justify-center" aria-label="Toggle Navigation Menu" aria-expanded="false">
          <svg id="hamburgerIcon" class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"/></svg>
          <svg id="closeIcon" class="w-5 h-5 hidden" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>
    </div>

    <!-- Mobile Navigation Dropdown -->
    <div id="mobileMenuDropdown" class="hidden lg:hidden border-t border-divider bg-[#FAF9F5]/98 backdrop-blur-md px-4 py-4 shadow-lg">
      <nav class="flex flex-col gap-2 font-semibold text-slate-700 text-sm">
        <a href="{home_prefix}#services" onclick="closeMobileMenu()" class="px-3 py-2.5 rounded-lg hover:text-emeraldBrand hover:bg-subtle transition-colors" data-t="navEngines">5 Engines</a>
        <a href="{home_prefix}#solutions" onclick="closeMobileMenu()" class="px-3 py-2.5 rounded-lg hover:text-emeraldBrand hover:bg-subtle transition-colors" data-t="navSolutions">Solutions</a>
        <a href="{home_prefix}#faq" onclick="closeMobileMenu()" class="px-3 py-2.5 rounded-lg hover:text-emeraldBrand hover:bg-subtle transition-colors" data-t="navFaq">FAQ</a>
        <div class="flex items-center justify-between pt-3 border-t border-divider text-xs">
          <span class="text-slate-500 font-mono font-bold">Language</span>
          <div class="flex items-center bg-[#EAE8E1] border border-divider rounded-full p-0.5 text-xs font-mono font-bold">
            <a href="{en_href}" class="{en_class}">EN</a>
            <a href="{uz_href}" class="{uz_class}">UZ</a>
            <a href="{ru_href}" class="{ru_class}">RU</a>
          </div>
        </div>
        <button type="button" onclick="closeMobileMenu(); openDemoModal('Mobile Navbar')" class="w-full mt-3 inline-flex items-center justify-center gap-1.5 px-4 py-3 rounded-xl bg-emeraldBrand hover:bg-emeraldDark text-white text-sm font-bold shadow-sm transition-all min-h-[44px]">
          <span data-t="btnBookDemo">Book a Demo</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </button>
      </nav>
    </div>
  </header>
"""

# Common Footer
def get_footer_html(lang):
    arch_link = '/architecture.html' if lang == 'en' else f'/{lang}/architecture.html'
    home_prefix = '/' if lang == 'en' else f'/{lang}/'
    return f"""
  <!-- ==================== FOOTER ==================== -->
  <footer class="bg-white border-t border-divider py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6">
      <div class="flex items-center gap-3">
        <div class="w-8 h-8 rounded-lg bg-white border border-divider flex items-center justify-center p-1.5 shadow-2xs">
          <svg class="w-full h-full" viewBox="0 0 100 100" fill="none">
            <path fill="#087F6A" d="M51.4 9 A41 41 0 1 0 88 65.4 V42 H47 V58 H73.7 A25 25 0 1 1 50.9 25 Z"/>
            <path fill="#B7F34A" d="M61 9 H88 V36 H78 V19 H61 Z"/>
          </svg>
        </div>
        <div>
          <div class="flex items-center gap-1.5">
            <span class="font-bold text-slateDark text-sm" style="font-family:'Poppins', sans-serif;">GPTify</span>
            <span class="bg-[#087F6A] text-white font-bold text-xs tracking-wider uppercase px-1.5 py-0.5 rounded" style="font-family:'Poppins', sans-serif;">OS</span>
          </div>
          <span class="text-xs text-slateMuted block" data-t="footerDesc">The AI operating system for service businesses.</span>
        </div>
      </div>

      <div class="flex flex-wrap items-center gap-3 text-xs font-semibold text-slate-600">
        <a href="{home_prefix}#services" class="hover:text-emeraldBrand cursor-pointer">Ailo</a>
        <span>•</span>
        <a href="{home_prefix}#services" class="hover:text-amberBrand cursor-pointer">ILDAM</a>
        <span>•</span>
        <a href="{home_prefix}#services" class="hover:text-purpleBrand cursor-pointer">Bandla</a>
        <span>•</span>
        <a href="{home_prefix}#services" class="hover:text-skyBrand cursor-pointer">Mirzo</a>
        <span>•</span>
        <a href="{home_prefix}#services" class="hover:text-indigoBrand cursor-pointer">Izlai</a>
      </div>

      <!-- Compliance & Legal Links -->
      <div class="flex flex-wrap items-center gap-3 text-xs font-semibold text-slate-500">
        <a href="/privacy.html" class="hover:text-emeraldBrand transition cursor-pointer" data-t="footerPrivacy">Privacy Policy</a>
        <span>•</span>
        <a href="/terms.html" class="hover:text-emeraldBrand transition cursor-pointer" data-t="footerTerms">Terms of Service</a>
        <span>•</span>
        <a href="/privacy.html#security" class="hover:text-emeraldBrand transition cursor-pointer" data-t="footerSecurity">Security & Compliance</a>
        <span>•</span>
        <a href="mailto:contact@gptify.co" class="hover:text-emeraldBrand transition">contact@gptify.co</a>
        <span>•</span>
        <a href="https://gptify.uz" target="_blank" rel="noopener noreferrer" class="hover:text-emeraldBrand transition">gptify.uz</a>
      </div>

      <div class="text-xs text-slateMuted">
        © 2026 GPTify Technologies MChJ. <span data-t="footerRights">All rights reserved.</span>
      </div>
    </div>
  </footer>
"""

# Common Lead Capture Demo Modal
def get_modal_html(lang):
    name_ph = 'e.g. Alexander Vance' if lang == 'en' else ('Masalan: Dilshod Karimov' if lang == 'uz' else 'Например: Дильшод Каримов')
    comp_ph = 'e.g. Apex Clinic (Healthcare)' if lang == 'en' else ('Masalan: Smile Clinic (stomatologiya)' if lang == 'uz' else 'Например: Smile Clinic (стоматология)')
    contact_ph = '+1 555 123 4567 or @username' if lang == 'en' else ('+998 90 123 45 67 yoki @username' if lang == 'uz' else '+998 90 123 45 67 или @username')
    opts = ['1-5 employees', '6-20 employees', '20-50 employees', '50+ employees (Enterprise)'] if lang == 'en' else (
           ['1-5 xodim', '6-20 xodim', '20-50 xodim', '50+ xodim (Enterprise)'] if lang == 'uz' else
           ['1-5 сотрудников', '6-20 сотрудников', '20-50 сотрудников', '50+ сотрудников (Enterprise)'])

    return f"""
  <!-- ==================== LEAD CAPTURE DEMO MODAL ==================== -->
  <div id="demoModal" class="fixed inset-0 z-[100] hidden items-center justify-center p-4 sm:p-6 overflow-y-auto" role="dialog" aria-modal="true" aria-labelledby="modalTitle">
    <!-- Backdrop with blur -->
    <div class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm transition-opacity" onclick="closeDemoModal()"></div>

    <!-- Modal Card -->
    <div class="relative bg-white rounded-2xl sm:rounded-3xl border border-divider shadow-2xl max-w-lg w-full p-5 sm:p-6 z-10 my-auto text-left transition-all max-h-[92vh] overflow-y-auto">
      
      <!-- Close Button -->
      <button type="button" onclick="closeDemoModal()" class="absolute top-4 right-4 w-8 h-8 rounded-full bg-subtle hover:bg-slate-200 text-slate-500 hover:text-slate-800 flex items-center justify-center transition cursor-pointer" aria-label="Close">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/></svg>
      </button>

      <!-- Form Container -->
      <div id="leadFormContainer">
        <!-- Header -->
        <div class="mb-4 pr-6">
          <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-50 border border-emerald-200 text-xs font-mono font-bold text-emerald-800 uppercase tracking-wider mb-1.5">
            <span class="w-1.5 h-1.5 rounded-full bg-emeraldBrand badge-live-pulse"></span>
            <span data-t="modalBadge">LIVE DEMO & AUDIT</span>
          </div>
          <h3 id="modalTitle" class="text-xl sm:text-2xl font-black text-slateDark tracking-tight" data-t="modalTitle">
            Book a Live Demo & System Audit
          </h3>
          <p class="text-xs sm:text-sm text-slate-600 mt-1 leading-relaxed" data-t="modalSub">
            See GPTify OS running live on your workflow. We will contact you to schedule your session.
          </p>
        </div>

        <!-- Form with Context Tracking Hidden Input -->
        <form id="demoLeadForm" onsubmit="submitDemoLead(event)" class="space-y-3.5">
          <input type="hidden" id="leadInterest" name="interest" value="General">

          <!-- Row 1: Full Name & Company Name -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
            <div>
              <label for="leadName" class="block text-sm font-bold text-slateDark mb-1" data-t="lblModalName">
                Your Full Name
              </label>
              <input type="text" id="leadName" autocomplete="name" required placeholder="{name_ph}" class="w-full px-3 py-2.5 rounded-xl border border-divider bg-subtle/50 text-slateDark text-base focus:outline-none focus:ring-2 focus:ring-emeraldBrand focus:bg-white transition">
            </div>

            <div>
              <label for="leadCompany" class="block text-sm font-bold text-slateDark mb-1" data-t="lblModalCompany">
                Company & Industry
              </label>
              <input type="text" id="leadCompany" required placeholder="{comp_ph}" class="w-full px-3 py-2.5 rounded-xl border border-divider bg-subtle/50 text-slateDark text-base focus:outline-none focus:ring-2 focus:ring-emeraldBrand focus:bg-white transition">
            </div>
          </div>

          <!-- Row 2: Phone or Telegram -->
          <div>
            <label for="leadContact" class="block text-sm font-bold text-slateDark mb-1" data-t="lblModalContact">
              Phone Number or Telegram (@username)
            </label>
            <input type="text" id="leadContact" autocomplete="tel" required placeholder="{contact_ph}" class="w-full px-3 py-2.5 rounded-xl border border-divider bg-subtle/50 text-slateDark text-base focus:outline-none focus:ring-2 focus:ring-emeraldBrand focus:bg-white transition">
          </div>

          <!-- Row 3: Team Size & Channels to Connect -->
          <div class="grid grid-cols-1 sm:grid-cols-12 gap-2.5">
            <div class="sm:col-span-5">
              <label for="leadTeamSize" class="block text-sm font-bold text-slateDark mb-1" data-t="lblModalTeam">
                Team Size:
              </label>
              <select id="leadTeamSize" class="w-full px-3 py-2.5 rounded-xl border border-divider bg-subtle/50 text-slateDark text-base focus:outline-none focus:ring-2 focus:ring-emeraldBrand focus:bg-white transition cursor-pointer">
                <option value="{opts[0]}">{opts[0]}</option>
                <option value="{opts[1]}" selected>{opts[1]}</option>
                <option value="{opts[2]}">{opts[2]}</option>
                <option value="{opts[3]}">{opts[3]}</option>
              </select>
            </div>

            <div class="sm:col-span-7">
              <label class="block text-sm font-bold text-slateDark mb-1" data-t="lblModalChannels">
                Channels to Connect:
              </label>
              <div class="grid grid-cols-3 gap-1.5 text-xs">
                <label class="flex items-center gap-1.5 p-1.5 rounded-lg bg-subtle/60 border border-divider cursor-pointer hover:bg-emerald-50/50">
                  <input type="checkbox" name="channels" value="Telegram" checked class="accent-emerald-600 rounded w-4 h-4">
                  <span class="text-slate-700 font-medium truncate">Telegram</span>
                </label>
                <label class="flex items-center gap-1.5 p-1.5 rounded-lg bg-subtle/60 border border-divider cursor-pointer hover:bg-emerald-50/50">
                  <input type="checkbox" name="channels" value="WhatsApp" checked class="accent-emerald-600 rounded w-4 h-4">
                  <span class="text-slate-700 font-medium truncate">WhatsApp</span>
                </label>
                <label class="flex items-center gap-1.5 p-1.5 rounded-lg bg-subtle/60 border border-divider cursor-pointer hover:bg-emerald-50/50">
                  <input type="checkbox" name="channels" value="Instagram Direct" checked class="accent-emerald-600 rounded w-4 h-4">
                  <span class="text-slate-700 font-medium truncate">Instagram</span>
                </label>
                <label class="flex items-center gap-1.5 p-1.5 rounded-lg bg-subtle/60 border border-divider cursor-pointer hover:bg-emerald-50/50">
                  <input type="checkbox" name="channels" value="Corporate Email" class="accent-emerald-600 rounded w-4 h-4">
                  <span class="text-slate-700 font-medium truncate">Email</span>
                </label>
                <label class="flex items-center gap-1.5 p-1.5 rounded-lg bg-subtle/60 border border-divider cursor-pointer hover:bg-emerald-50/50">
                  <input type="checkbox" name="channels" value="LinkedIn Outreach" class="accent-emerald-600 rounded w-4 h-4">
                  <span class="text-slate-700 font-medium truncate">LinkedIn</span>
                </label>
                <label class="flex items-center gap-1.5 p-1.5 rounded-lg bg-subtle/60 border border-divider cursor-pointer hover:bg-emerald-50/50">
                  <input type="checkbox" name="channels" value="CRM & Calendar" checked class="accent-emerald-600 rounded w-4 h-4">
                  <span class="text-slate-700 font-medium truncate">CRM</span>
                </label>
              </div>
            </div>
          </div>

          <!-- Submit Button -->
          <div class="pt-2">
            <button type="submit" id="btnSubmitLead" class="w-full py-3 px-6 rounded-xl bg-emeraldBrand hover:bg-emeraldDark text-white font-bold text-sm shadow-md transition-all duration-200 flex items-center justify-center gap-2 cursor-pointer min-h-[44px]">
              <span id="btnSubmitText" data-t="modalSubmitBtn">Confirm & Book Demo</span>
              <svg id="btnSubmitIcon" class="w-4 h-4 text-limeSpark" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg>
              <svg id="btnSubmitSpinner" class="hidden animate-spin w-4 h-4 text-white" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            </button>
          </div>
        </form>
      </div>

      <!-- Success State Container -->
      <div id="leadSuccessContainer" class="hidden py-8 px-4 text-center space-y-4">
        <div class="w-16 h-16 rounded-full bg-emerald-50 text-emeraldBrand flex items-center justify-center mx-auto shadow-xs border border-emerald-100">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
        </div>

        <div class="space-y-2">
          <h3 class="text-2xl font-black text-slateDark" data-t="successTitle">
            Thank You! Request Received
          </h3>
          <p class="text-sm text-slate-600 max-w-sm mx-auto leading-relaxed" data-t="successDesc">
            Thank you for reaching out. We have received your details and our team will get back to you shortly.
          </p>
        </div>

        <div class="pt-4 max-w-xs mx-auto">
          <button type="button" onclick="closeDemoModal()" class="w-full py-3 px-6 rounded-xl bg-slateDark hover:bg-slate-800 text-white font-bold text-sm shadow-sm transition cursor-pointer min-h-[44px]" data-t="modalCloseBtn">
            Close Window
          </button>
        </div>
      </div>

    </div>
  </div>
"""

# Common Scripts (Lead handling, Modal, Mobile menu, Calculator)
def get_scripts_html(lang):
    return f"""
  <script>
    let currentLang = '{lang}';
    const SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzM3GZEDsWDc-3SUI4sySAWnJFn6ZolQaYkwo7W4VWG-79J3WVLYeQL7qs5jgAtkK_C_g/exec';

    function openDemoModal(interest) {{
      const modal = document.getElementById('demoModal');
      const interestInput = document.getElementById('leadInterest');
      if (interestInput && interest) {{
        interestInput.value = interest;
      }}
      if (modal) {{
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        document.body.style.overflow = 'hidden';
      }}
    }}

    function closeDemoModal() {{
      const modal = document.getElementById('demoModal');
      if (modal) {{
        modal.classList.add('hidden');
        modal.classList.remove('flex');
        document.body.style.overflow = '';
      }}
    }}

    function toggleMobileMenu() {{
      const menu = document.getElementById('mobileMenuDropdown');
      const btn = document.getElementById('mobileMenuBtn');
      const ham = document.getElementById('hamburgerIcon');
      const close = document.getElementById('closeIcon');
      if (!menu || !btn) return;
      const isExpanded = btn.getAttribute('aria-expanded') === 'true';

      if (isExpanded) {{
        closeMobileMenu();
      }} else {{
        menu.classList.remove('hidden');
        if (ham) ham.classList.add('hidden');
        if (close) close.classList.remove('hidden');
        btn.setAttribute('aria-expanded', 'true');
      }}
    }}

    function closeMobileMenu() {{
      const menu = document.getElementById('mobileMenuDropdown');
      const btn = document.getElementById('mobileMenuBtn');
      const ham = document.getElementById('hamburgerIcon');
      const close = document.getElementById('closeIcon');
      if (menu) menu.classList.add('hidden');
      if (ham) ham.classList.remove('hidden');
      if (close) close.classList.add('hidden');
      if (btn) btn.setAttribute('aria-expanded', 'false');
    }}

    function calculateLosses() {{
      const teamInput = document.getElementById('calcTeam');
      const rateInput = document.getElementById('calcRate');
      const hoursInput = document.getElementById('calcHours');

      if (!teamInput || !rateInput || !hoursInput) return;

      const team = parseInt(teamInput.value, 10) || 5;
      const rate = parseInt(rateInput.value, 10) || 12;
      const hoursPerWeek = parseInt(hoursInput.value, 10) || 10;

      const teamVal = document.getElementById('calcTeamVal');
      const rateVal = document.getElementById('calcRateVal');
      const hoursVal = document.getElementById('calcHoursVal');

      if (teamVal) teamVal.textContent = team + ' ' + (currentLang === 'ru' ? 'сотр.' : (currentLang === 'uz' ? 'xodim' : 'people'));
      if (rateVal) rateVal.textContent = '$' + rate + '/hr';
      if (hoursVal) hoursVal.textContent = hoursPerWeek + ' ' + (currentLang === 'ru' ? 'ч/нед' : (currentLang === 'uz' ? 's/hafta' : 'hrs/wk'));

      const monthlyHoursRecovered = Math.round(team * hoursPerWeek * 3.8);
      const monthlySaved = Math.round(monthlyHoursRecovered * rate * 0.85);
      const annualSaved = monthlySaved * 12;

      const resHours = document.getElementById('calcResHours');
      const resMonthly = document.getElementById('calcResMonthly');
      const resAnnual = document.getElementById('calcResAnnual');

      if (resHours) resHours.textContent = monthlyHoursRecovered.toLocaleString() + 'h';
      if (resMonthly) resMonthly.textContent = '$' + monthlySaved.toLocaleString();
      if (resAnnual) resAnnual.textContent = '$' + annualSaved.toLocaleString();
    }}

    async function sendLeadToBackend(leadData) {{
      const payload = {{
        source: 'gptify.si',
        full_name: leadData.name,
        company: leadData.company,
        phone: leadData.contact,
        contact: leadData.contact,
        category: 'GPTify OS Demo: ' + leadData.interest,
        course_name: 'GPTify OS Demo | Qiziqish: ' + leadData.interest + ' | Kompaniya: ' + leadData.company + ' | Jamoa: ' + leadData.teamSize + ' | Kanallar: ' + leadData.channels.join(', '),
        team_size: leadData.teamSize,
        channels: leadData.channels.join(', '),
        interest: leadData.interest,
        lang: currentLang,
        created_at: new Date().toISOString()
      }};

      try {{
        await fetch(SCRIPT_URL, {{
          method: 'POST',
          mode: 'no-cors',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify(payload)
        }});
      }} catch (err) {{
        console.warn('Lead submission error', err);
      }}
    }}

    async function submitDemoLead(e) {{
      e.preventDefault();
      const btnSubmit = document.getElementById('btnSubmitLead');
      const btnText = document.getElementById('btnSubmitText');
      const btnSpinner = document.getElementById('btnSubmitSpinner');
      const btnIcon = document.getElementById('btnSubmitIcon');

      if (btnSubmit) btnSubmit.disabled = true;
      if (btnSpinner) btnSpinner.classList.remove('hidden');
      if (btnIcon) btnIcon.classList.add('hidden');

      const name = document.getElementById('leadName').value.trim();
      const company = document.getElementById('leadCompany').value.trim();
      const contact = document.getElementById('leadContact').value.trim();
      const teamSize = document.getElementById('leadTeamSize').value;
      const interest = (document.getElementById('leadInterest') && document.getElementById('leadInterest').value) || 'General';

      const checkedBoxes = document.querySelectorAll('input[name="channels"]:checked');
      const channels = Array.from(checkedBoxes).map(cb => cb.value);

      const leadData = {{
        name,
        company,
        contact,
        teamSize,
        channels,
        interest,
        lang: currentLang,
        timestamp: new Date().toISOString()
      }};

      try {{
        await sendLeadToBackend(leadData);
      }} catch (e) {{
        console.warn('Send lead error', e);
      }}

      const formContainer = document.getElementById('leadFormContainer');
      const successContainer = document.getElementById('leadSuccessContainer');
      if (formContainer && successContainer) {{
        formContainer.classList.add('hidden');
        successContainer.classList.remove('hidden');
      }}

      if (btnSubmit) btnSubmit.disabled = false;
      if (btnSpinner) btnSpinner.classList.add('hidden');
      if (btnIcon) btnIcon.classList.remove('hidden');
    }}

    function switchIndustryTab(industry) {{
      const industries = ['clinics', 'education', 'auto', 'advisory'];
      industries.forEach(ind => {{
        const panel = document.getElementById('panel-' + ind);
        const btn = document.getElementById('tab-btn-' + ind);
        if (panel) {{
          if (ind === industry) {{
            panel.classList.remove('hidden');
          }} else {{
            panel.classList.add('hidden');
          }}
        }}
        if (btn) {{
          if (ind === industry) {{
            btn.classList.remove('bg-white', 'text-slate-700', 'border-divider');
            btn.classList.add('bg-slateDark', 'text-white', 'shadow-sm');
            btn.setAttribute('aria-selected', 'true');
          }} else {{
            btn.classList.remove('bg-slateDark', 'text-white', 'shadow-sm');
            btn.classList.add('bg-white', 'text-slate-700', 'border-divider');
            btn.setAttribute('aria-selected', 'false');
          }}
        }}
      }});
    }}

    window.addEventListener('DOMContentLoaded', () => {{
      calculateLosses();
    }});
  </script>
</body>
</html>
"""

print("Helper definitions loaded.")

# ==================== HOMEPAGE SECTIONS ====================
def get_homepage_body(lang):
    return f"""
  <!-- ==================== HERO SECTION WITH LIVE COMMAND CENTER ==================== -->
  <section class="pt-6 sm:pt-8 lg:pt-9 pb-12 lg:pb-14 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-b border-divider">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-center">
      
      <!-- Left Column: Value Proposition -->
      <div class="lg:col-span-6">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white border border-divider text-xs font-bold text-slateDark mb-3.5 shadow-2xs">
          <span class="w-2 h-2 rounded-full bg-emeraldBrand badge-live-pulse" aria-hidden="true"></span>
          <span data-t="heroBadge">AI Operating System for Service Businesses</span>
        </div>

        <h1 class="text-3xl sm:text-4xl lg:text-[40px] xl:text-[46px] font-black text-slateDark tracking-tight leading-[1.12] mb-3.5" data-t="heroH1">
          The AI Operating System <br>
          <span class="font-serif italic font-normal text-emeraldBrand text-[1.12em] tracking-normal">for Service Businesses.</span>
        </h1>

        <p class="text-sm sm:text-base text-slate-600 leading-relaxed mb-5 max-w-lg" data-t="heroSub">
          Connect customer conversations, CRM, scheduling, meetings, outreach and business data through a unified layer of AI agents. Zero manual data entry — running 24/7.
        </p>

        <!-- CTA & Strategy Session Details -->
        <div class="flex flex-col sm:flex-row items-start sm:items-center gap-3.5 mb-5">
          <button type="button" id="heroCtaPrimary" onclick="openDemoModal('Hero CTA')" class="w-full sm:w-auto px-6 py-3.5 rounded-xl bg-slateDark hover:bg-slate-800 text-white font-bold text-sm text-center shadow-md transition-all duration-200 flex items-center justify-center gap-2 cursor-pointer min-h-[44px]">
            <span data-t="btnBookDemo">Book a Demo</span>
            <svg class="w-4 h-4 text-limeSpark" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg>
          </button>
          <div class="text-xs text-slateMuted">
            <span class="font-bold text-slateDark block" data-t="heroCtaNote">Free · 30 Minutes · Zero Obligation</span>
            <span data-t="heroCtaSub">Custom architecture blueprint for your business model</span>
          </div>
        </div>

        <!-- Quick Proof Badges -->
        <div class="flex flex-wrap items-center gap-3 pt-3 border-t border-divider text-xs text-slate-600 font-medium">
          <span class="flex items-center gap-1.5">
            <svg class="w-4 h-4 text-emeraldBrand" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
            <span data-t="proof1">5 Specialized Engines: Ailo, ILDAM, Bandla, Mirzo & Izlai</span>
          </span>
          <span class="flex items-center gap-1.5">
            <svg class="w-4 h-4 text-emeraldBrand" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
            <span data-t="proof2">Clinics · Education · Automotive · Professional Services</span>
          </span>
        </div>

        <!-- Owner Proof Slot (Requirement D: hidden until content provided) -->
        <div id="hero-proof-slot" class="hidden my-4 p-4 rounded-2xl bg-white border border-divider shadow-xs">
          <!-- Proof content to be provided by owner -->
        </div>
      </div>

      <!-- Right Column: Live Operating Dashboard Mockup -->
      <div class="lg:col-span-6 relative">
        <div class="card-elevated rounded-3xl p-5 sm:p-6 bg-white border border-divider shadow-xl relative overflow-hidden">
          <div class="flex items-center justify-between pb-3.5 mb-3.5 border-b border-divider">
            <div class="flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-red-400"></span>
              <span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span>
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
              <span class="text-xs font-mono font-bold text-slate-500 ml-1">
                TLS 1.3 Verified
              </span>
            </div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded bg-slate-200 text-slate-600 font-mono text-xs uppercase font-bold tracking-wider">Sample Data</span>
              <div class="flex items-center gap-1.5 text-emerald-800 font-mono text-xs font-bold bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200">
                <span class="w-1.5 h-1.5 rounded-full bg-emeraldBrand"></span>
                <span data-t="dashStatus">5/5 FLEET LIVE</span>
              </div>
            </div>
          </div>

          <!-- KPI Strip -->
          <div class="grid grid-cols-3 gap-2 sm:gap-3 mb-4">
            <div class="p-3 rounded-2xl bg-subtle/70 border border-divider">
              <div class="flex items-center justify-between text-xs font-mono text-slateMuted">
                <span data-t="kpi1Label">LEADS</span>
                <span class="text-emeraldBrand font-bold">+18% Today</span>
              </div>
              <div class="text-lg font-mono font-black text-slateDark mt-0.5">42</div>
              <div class="text-xs font-mono text-slate-500 mt-0.5">Automated triage</div>
            </div>
            <div class="p-3 rounded-2xl bg-subtle/70 border border-divider">
              <div class="flex items-center justify-between text-xs font-mono text-slateMuted">
                <span data-t="kpi2Label">ENGINES</span>
                <span class="text-emeraldBrand font-bold" data-t="kpi2Active">Active</span>
              </div>
              <div class="text-lg font-mono font-black text-slateDark mt-0.5">5/5</div>
              <div class="text-xs font-mono text-slate-500 mt-0.5">All synced</div>
            </div>
            <div class="p-3 rounded-2xl bg-subtle/70 border border-divider">
              <div class="flex items-center justify-between text-xs font-mono text-slateMuted">
                <span data-t="kpi3Label">TIME SAVED</span>
                <span class="text-emeraldBrand font-bold" data-t="kpi3Sub">This Week</span>
              </div>
              <div class="text-lg font-mono font-black text-slateDark mt-0.5">52.5h</div>
              <div class="text-xs font-mono text-slate-500 mt-0.5" data-t="kpi3Value">Hours recovered</div>
            </div>
          </div>

          <!-- Live Event Feed ("What happened today") -->
          <div class="p-3.5 rounded-2xl bg-[#0F172A] text-slate-300 font-mono text-xs border border-slate-800">
            <div class="flex items-center justify-between pb-2 mb-2.5 border-b border-slate-800">
              <div class="flex items-center gap-1.5 text-xs text-slate-300 font-bold uppercase tracking-wider">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                <span data-t="telemetryTitle">What happened today</span>
              </div>
              <span class="text-slate-500 text-xs" data-t="telemetrySync">Synchronized</span>
            </div>
            <div class="space-y-2 text-xs leading-relaxed">
              <div class="flex items-start gap-2">
                <span class="text-emerald-400 shrink-0">16:42:01</span>
                <span data-t="tel1">Instagram DM inquiry qualified in 6s; appointment slot held via Bandla</span>
              </div>
              <div class="flex items-start gap-2">
                <span class="text-indigo-400 shrink-0">16:38:12</span>
                <span data-t="tel2">14 B2B accounts prospected via Email & LinkedIn; 3 replies</span>
              </div>
              <div class="flex items-start gap-2">
                <span class="text-amber-400 shrink-0">16:29:45</span>
                <span data-t="tel3">Deal moved to Proposal stage; advance invoice scheduled</span>
              </div>
              <div class="flex items-start gap-2">
                <span class="text-purple-400 shrink-0">16:15:20</span>
                <span data-t="tel4">Consultation confirmed for Thu 14:00; invites synced</span>
              </div>
              <div class="flex items-start gap-2">
                <span class="text-sky-400 shrink-0">15:58:02</span>
                <span data-t="tel5">42-min meeting summarized; 4 action items sent to Telegram</span>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ==================== THIRD-PARTY INTEGRATIONS MARQUEE STRIP (Requirement E.4) ==================== -->
  <section class="py-8 border-b border-divider bg-white overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 mb-4 text-center">
      <span class="text-xs font-mono font-bold uppercase tracking-widest text-slateMuted" data-t="marqueeTitle">
        Natively Integrates With Your Existing Enterprise Software
      </span>
    </div>

    <div class="relative w-full overflow-hidden [mask-image:linear-gradient(90deg,transparent,black_12%,black_88%,transparent)]">
      <div class="marquee-track font-mono text-xs font-bold text-slate-700">
        <!-- 8 Third-Party Tools Only -->
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <svg class="w-4 h-4 text-sky-500" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 00-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.75-.55 2.92-1.27 4.86-2.11 5.83-2.51 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .38z"/></svg>
          <span>Telegram Channels & Bots</span>
        </div>
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <svg class="w-4 h-4 text-emerald-500" fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
          <span>WhatsApp Business API</span>
        </div>
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <svg class="w-4 h-4 text-pink-600" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          <span>Instagram Direct</span>
        </div>
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <svg class="w-4 h-4 text-blue-700" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
          <span>LinkedIn Outreach</span>
        </div>
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <svg class="w-4 h-4 text-emerald-600" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5"/></svg>
          <span>Google Calendar</span>
        </div>
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <span class="px-1.5 py-0.5 rounded bg-amber-600 text-xs font-black text-white flex items-center justify-center">1C</span>
          <span>1C Enterprise (ERP)</span>
        </div>
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <span class="w-3 h-3 rounded-full bg-blue-500"></span>
          <span>Click.uz</span>
        </div>
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <span class="w-3 h-3 rounded-full bg-teal-400"></span>
          <span>Payme Business</span>
        </div>

        <!-- Duplicated Set for Smooth Continuous Loop -->
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <svg class="w-4 h-4 text-sky-500" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 00-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.75-.55 2.92-1.27 4.86-2.11 5.83-2.51 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .38z"/></svg>
          <span>Telegram Channels & Bots</span>
        </div>
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <svg class="w-4 h-4 text-emerald-500" fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
          <span>WhatsApp Business API</span>
        </div>
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <svg class="w-4 h-4 text-pink-600" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          <span>Instagram Direct</span>
        </div>
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <svg class="w-4 h-4 text-blue-700" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
          <span>LinkedIn Outreach</span>
        </div>
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <svg class="w-4 h-4 text-emerald-600" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5"/></svg>
          <span>Google Calendar</span>
        </div>
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <span class="px-1.5 py-0.5 rounded bg-amber-600 text-xs font-black text-white flex items-center justify-center">1C</span>
          <span>1C Enterprise (ERP)</span>
        </div>
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <span class="w-3 h-3 rounded-full bg-blue-500"></span>
          <span>Click.uz</span>
        </div>
        <div class="flex items-center gap-2.5 bg-subtle px-4 py-2 rounded-xl border border-divider">
          <span class="w-3 h-3 rounded-full bg-teal-400"></span>
          <span>Payme Business</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== LOOPING LIVE CHAT DEMO (Section 2) ==================== -->
  <section id="demo" class="py-12 sm:py-14 px-4 sm:px-6 lg:px-8 max-w-4xl mx-auto border-b border-divider">
    <div class="text-center max-w-2xl mx-auto mb-8">
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-emeraldBrand" data-t="demoEyebrow">Real-Time Instagram & Telegram Automation</span>
      <h2 class="text-3xl sm:text-4xl font-extrabold text-slateDark mt-2 tracking-tight" data-t="demoTitle">
        How Ailo, Bandla, and ILDAM Coordinate Instantly
      </h2>
      <p class="text-slate-600 text-sm sm:text-base mt-2" data-t="demoSub">
        Example conversation on Instagram Direct — dynamic qualification, calendar booking, and automatic CRM sync in seconds.
      </p>
    </div>

    <!-- Chat Window Mockup -->
    <div class="bg-white rounded-3xl border border-divider shadow-xl overflow-hidden max-w-xl mx-auto">
      <div class="flex items-center justify-between px-5 py-3.5 bg-[#F8FAFC] border-b border-divider">
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-full p-0.5 bg-gradient-to-tr from-amber-500 via-pink-500 to-purple-600">
            <div class="w-full h-full rounded-full bg-white flex items-center justify-center font-bold text-slateDark text-xs font-mono">
              MP
            </div>
          </div>
          <div>
            <div class="flex items-center gap-1.5">
              <span class="text-xs sm:text-sm font-bold text-slateDark">MedPro Clinic</span>
              <svg class="w-3.5 h-3.5 text-sky-500" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
            </div>
            <span class="text-xs text-slate-500 block" data-t="chatChannel">Instagram Direct · @medpro_clinic</span>
          </div>
        </div>
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emeraldBrand badge-live-pulse"></span>
          <span class="text-xs font-mono text-emeraldBrand font-bold">Ailo Live</span>
        </div>
      </div>

      <!-- Dialogue Body -->
      <div class="p-5 sm:p-6 space-y-4 bg-[#FAF9F5]/40 text-xs sm:text-sm">
        <!-- Customer Message -->
        <div class="flex items-end justify-end gap-2">
          <div class="bg-emeraldBrand text-white p-3.5 rounded-2xl rounded-tr-xs max-w-[82%] shadow-2xs leading-relaxed" data-t="chatMsg1">
            Hi! How much is teeth whitening and is Dr. Rustamov available tomorrow around 4 PM? 🦷
          </div>
        </div>

        <!-- Ailo Thinking -->
        <div class="flex items-center gap-2 text-xs font-mono text-slate-500 italic px-2">
          <span class="w-1.5 h-1.5 rounded-full bg-emeraldBrand animate-pulse"></span>
          <span data-t="chatTypingStatus">Ailo checking live doctor availability via Bandla...</span>
        </div>

        <!-- Ailo Response -->
        <div class="flex items-start gap-2.5">
          <div class="w-7 h-7 rounded-full bg-emeraldBrand text-white flex items-center justify-center font-mono font-bold text-xs shrink-0 mt-0.5">
            A
          </div>
          <div class="bg-white border border-divider p-3.5 rounded-2xl rounded-tl-xs max-w-[85%] shadow-xs text-slateDark space-y-2 leading-relaxed">
            <p data-t="chatMsg2">
              Hello! 👋 Professional Zoom Whitening is <strong>1,200,000 UZS</strong>.
            </p>
            <p data-t="chatMsg3">
              Dr. Rustamov has an opening tomorrow at <strong>16:00 (4:00 PM)</strong> at our Tashkent Central branch.
            </p>
            <div class="pt-2 border-t border-divider flex flex-col sm:flex-row gap-2">
              <button type="button" onclick="openDemoModal('Chat Demo')" class="px-3.5 py-2 rounded-xl bg-emeraldBrand hover:bg-emeraldDark text-white text-xs font-bold transition flex items-center justify-center gap-1.5 cursor-pointer">
                <span>Hold My 16:00 Slot</span>
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              </button>
              <button type="button" onclick="openDemoModal('Chat Demo')" class="px-3 py-2 rounded-xl border border-divider hover:bg-subtle text-slate-700 text-xs font-semibold transition text-center">
                See Other Times
              </button>
            </div>
          </div>
        </div>

        <!-- System Sync Confirmation Pill -->
        <div class="p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-xs font-mono text-emerald-900 flex items-center justify-between">
          <div class="flex items-center gap-2">
            <svg class="w-4 h-4 text-emeraldBrand shrink-0" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            <span data-t="chatSyncStatus">Bandla locked calendar · Deal pushed to ILDAM CRM</span>
          </div>
          <span class="font-bold text-emerald-700 text-xs">0.8s</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== THE 5 CORE ENGINES (Section 3) ==================== -->
  <section id="services" class="py-12 sm:py-14 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-b border-divider">
    <div class="max-w-3xl mb-8">
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-emeraldBrand" data-t="pillarsEyebrow">Core System</span>
      <h2 class="text-3xl sm:text-4xl font-extrabold text-slateDark mt-2 tracking-tight" data-t="pillarsTitle">
        5 Core Tools to Run Your Business
      </h2>
      <p class="text-slate-600 text-sm sm:text-base mt-2" data-t="pillarsSub">
        Use individual tools or connect them together into one seamless workflow.
      </p>
    </div>

    <!-- The Connected Loop Visual Flow Banner -->
    <div class="mb-8 p-4 sm:p-5 rounded-2xl bg-white border border-divider shadow-2xs">
      <div class="flex items-center justify-between mb-3">
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-slateDark flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emeraldBrand badge-live-pulse"></span>
          <span data-t="loopTitle">One Continuous Loop. Five Specialized Engines.</span>
        </span>
        <span class="text-xs font-mono text-slateMuted hidden sm:inline" data-t="loopSub">From first message until deal is closed</span>
      </div>
      <div class="grid grid-cols-2 sm:grid-cols-5 gap-2 text-xs font-mono font-bold">
        <div class="flex items-center justify-between p-2.5 rounded-xl bg-indigo-50/80 border border-indigo-200/80 text-indigo-950">
          <div class="flex items-center gap-1.5 min-w-0">
            <span class="w-5 h-5 rounded-md bg-indigo-600 text-white flex items-center justify-center text-xs font-bold shrink-0">01</span>
            <span class="truncate">Izlai (Find)</span>
          </div>
          <span class="text-indigo-400 font-bold shrink-0 hidden sm:inline ml-1">&rarr;</span>
        </div>
        <div class="flex items-center justify-between p-2.5 rounded-xl bg-emerald-50/80 border border-emerald-200/80 text-emerald-950">
          <div class="flex items-center gap-1.5 min-w-0">
            <span class="w-5 h-5 rounded-md bg-emeraldBrand text-white flex items-center justify-center text-xs font-bold shrink-0">02</span>
            <span class="truncate">Ailo (Engage)</span>
          </div>
          <span class="text-emerald-400 font-bold shrink-0 hidden sm:inline ml-1">&rarr;</span>
        </div>
        <div class="flex items-center justify-between p-2.5 rounded-xl bg-amber-50/80 border border-amber-200/80 text-amber-950">
          <div class="flex items-center gap-1.5 min-w-0">
            <span class="w-5 h-5 rounded-md bg-amber-600 text-white flex items-center justify-center text-xs font-bold shrink-0">03</span>
            <span class="truncate">ILDAM (Track)</span>
          </div>
          <span class="text-amber-400 font-bold shrink-0 hidden sm:inline ml-1">&rarr;</span>
        </div>
        <div class="flex items-center justify-between p-2.5 rounded-xl bg-purple-50/80 border border-purple-200/80 text-purple-950">
          <div class="flex items-center gap-1.5 min-w-0">
            <span class="w-5 h-5 rounded-md bg-purple-600 text-white flex items-center justify-center text-xs font-bold shrink-0">04</span>
            <span class="truncate">Bandla (Book)</span>
          </div>
          <span class="text-purple-400 font-bold shrink-0 hidden sm:inline ml-1">&rarr;</span>
        </div>
        <div class="col-span-2 sm:col-span-1 flex items-center justify-between p-2.5 rounded-xl bg-sky-50/80 border border-sky-200/80 text-sky-950">
          <div class="flex items-center gap-1.5 min-w-0">
            <span class="w-5 h-5 rounded-md bg-sky-600 text-white flex items-center justify-center text-xs font-bold shrink-0">05</span>
            <span class="truncate">Mirzo (Scribe)</span>
          </div>
          <span class="text-sky-600 font-bold shrink-0 text-xs">✓</span>
        </div>
      </div>
    </div>

    <!-- 5 Product Cards Grid (3 top, 2 bottom) -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-5 sm:gap-6 mb-6 sm:mb-8">
      
      <!-- Card 1: AILO -->
      <div class="card-elevated p-6 sm:p-7 rounded-3xl flex flex-col justify-between border-t-4 border-t-emeraldBrand">
        <div>
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center gap-2.5">
              <div class="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-800 font-extrabold flex items-center justify-center text-sm font-mono shrink-0">
                01
              </div>
              <div>
                <h3 class="text-xl font-extrabold text-slateDark">Ailo</h3>
                <span class="text-xs text-emeraldBrand font-mono font-bold block" data-t="ailoRole">Your AI Customer Agent</span>
              </div>
            </div>
            <span class="text-xs font-mono font-bold text-emeraldBrand bg-emerald-50 px-2 py-0.5 rounded whitespace-nowrap">
              Omnichannel AI
            </span>
          </div>

          <p class="text-slate-600 text-sm leading-relaxed mb-5" data-t="ailoDesc">
            Responds to inbound inquiries across WhatsApp, Instagram Direct, and Telegram within <strong>8 seconds</strong>. Qualifies budget and need, resolves objections, and routes sales-ready leads to CRM.
          </p>

          <div class="space-y-2 text-xs sm:text-sm text-slate-700 mb-6">
            <div class="flex items-start gap-2">
              <svg class="w-4 h-4 text-emeraldBrand shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              <span data-t="ailoB1"><strong>Official Meta Graph API:</strong> Fully verified, zero account ban risk.</span>
            </div>
            <div class="flex items-start gap-2">
              <svg class="w-4 h-4 text-emeraldBrand shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              <span data-t="ailoB2"><strong>Multilingual Context:</strong> Native audio and text comprehension.</span>
            </div>
            <div class="flex items-start gap-2">
              <svg class="w-4 h-4 text-emeraldBrand shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              <span data-t="ailoB3"><strong>Natural Human Flow:</strong> Dynamic intelligence instead of rigid button trees.</span>
            </div>
          </div>
        </div>

        <!-- Embedded Flywheel Handoff (Requirement A.3) -->
        <div class="pt-4 border-t border-divider">
          <div class="text-xs font-mono text-emeraldBrand font-bold mb-4" data-t="ailoHandoff">
            ↳ Syncs leads to ILDAM & reserves slots via Bandla
          </div>
          <button type="button" onclick="openDemoModal('Ailo Engine')" class="w-full py-3 px-4 rounded-xl bg-slateDark hover:bg-slate-800 text-white text-sm font-bold text-center transition cursor-pointer flex items-center justify-center gap-2 min-h-[44px]">
            <span data-t="btnBookDemo">Book a Demo</span>
            <svg class="w-4 h-4 text-limeSpark" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg>
          </button>
        </div>
      </div>

      <!-- Card 2: ILDAM CRM -->
      <div class="card-elevated p-6 sm:p-7 rounded-3xl flex flex-col justify-between border-t-4 border-t-amberBrand">
        <div>
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center gap-2.5">
              <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-800 font-extrabold flex items-center justify-center text-sm font-mono shrink-0">
                02
              </div>
              <div>
                <h3 class="text-xl font-extrabold text-slateDark">ILDAM</h3>
                <span class="text-xs text-amberBrand font-mono font-bold block" data-t="ildamRole">CRM That Keeps You Moving</span>
              </div>
            </div>
            <span class="text-xs font-mono font-bold text-amberBrand bg-amber-50 px-2 py-0.5 rounded whitespace-nowrap">
              CRM Pipeline
            </span>
          </div>

          <p class="text-slate-600 text-sm leading-relaxed mb-5" data-t="ildamDesc">
            Agile B2B pipeline management without enterprise bloat. Centralizes customer databases, tracks deal stages on Kanban, and enforces cash flow through automated payment milestones.
          </p>

          <div class="space-y-2 text-xs sm:text-sm text-slate-700 mb-6">
            <div class="flex items-start gap-2">
              <svg class="w-4 h-4 text-amberBrand shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              <span data-t="ildamB1"><strong>Visual Kanban Pipeline:</strong> Drag-and-drop deal management with automated stage transitions.</span>
            </div>
            <div class="flex items-start gap-2">
              <svg class="w-4 h-4 text-amberBrand shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              <span data-t="ildamB2"><strong>Milestone Cash Flow:</strong> Automated alerts for deposit invoices, progress billings, and deadlines.</span>
            </div>
            <div class="flex items-start gap-2">
              <svg class="w-4 h-4 text-amberBrand shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              <span data-t="ildamB3"><strong>Seamless Agent Sync:</strong> Automatically ingests qualified leads from Ailo and prospects from Izlai.</span>
            </div>
          </div>
        </div>

        <!-- Embedded Flywheel Handoff -->
        <div class="pt-4 border-t border-divider">
          <div class="text-xs font-mono text-amberBrand font-bold mb-4" data-t="ildamHandoff">
            ↳ Triggers bookings in Bandla & briefs Mirzo for calls
          </div>
          <button type="button" onclick="openDemoModal('ILDAM CRM')" class="w-full py-3 px-4 rounded-xl bg-slateDark hover:bg-slate-800 text-white text-sm font-bold text-center transition cursor-pointer flex items-center justify-center gap-2 min-h-[44px]">
            <span data-t="btnBookDemo">Book a Demo</span>
            <svg class="w-4 h-4 text-limeSpark" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg>
          </button>
        </div>
      </div>

      <!-- Card 3: BANDLA (Requirement E.8: subtitle and tag fit on one line each at 1280px) -->
      <div class="card-elevated p-6 sm:p-7 rounded-3xl flex flex-col justify-between border-t-4 border-t-purpleBrand">
        <div>
          <div class="flex items-start justify-between gap-2 mb-4">
            <div class="flex items-center gap-2.5 min-w-0">
              <div class="w-10 h-10 rounded-xl bg-purple-100 text-purple-800 font-extrabold flex items-center justify-center text-sm font-mono shrink-0">
                03
              </div>
              <div class="min-w-0">
                <h3 class="text-xl font-extrabold text-slateDark">Bandla</h3>
                <span class="text-xs text-purpleBrand font-mono font-bold block truncate" data-t="bandlaRole">Scheduling Built for Business</span>
              </div>
            </div>
            <span class="text-xs font-mono font-bold text-purpleBrand bg-purple-50 px-2 py-0.5 rounded whitespace-nowrap shrink-0">
              Booking Engine
            </span>
          </div>

          <p class="text-slate-600 text-sm leading-relaxed mb-5" data-t="bandlaDesc">
            Eliminates scheduling friction for service businesses. Connects directly with doctor, teacher, or team availability, locks slots instantly, and enforces attendance with automatic reminders.
          </p>

          <div class="space-y-2 text-xs sm:text-sm text-slate-700 mb-6">
            <div class="flex items-start gap-2">
              <svg class="w-4 h-4 text-purpleBrand shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              <span data-t="bandlaB1"><strong>Zero Double-Booking:</strong> Live synchronization with Google Calendar, Outlook, and internal shifts.</span>
            </div>
            <div class="flex items-start gap-2">
              <svg class="w-4 h-4 text-purpleBrand shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              <span data-t="bandlaB2"><strong>Automated No-Show Shield:</strong> Multi-channel Telegram and SMS reminders eliminate missed appointments.</span>
            </div>
            <div class="flex items-start gap-2">
              <svg class="w-4 h-4 text-purpleBrand shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              <span data-t="bandlaB3"><strong>Ailo & CRM Integration:</strong> Ailo reserves timeslots directly in the chat without external redirects.</span>
            </div>
          </div>
        </div>

        <!-- Embedded Flywheel Handoff -->
        <div class="pt-4 border-t border-divider">
          <div class="text-xs font-mono text-purpleBrand font-bold mb-4" data-t="bandlaHandoff">
            ↳ Prepares meeting agenda for Mirzo & syncs with 1C
          </div>
          <button type="button" onclick="openDemoModal('Bandla Engine')" class="w-full py-3 px-4 rounded-xl bg-slateDark hover:bg-slate-800 text-white text-sm font-bold text-center transition cursor-pointer flex items-center justify-center gap-2 min-h-[44px]">
            <span data-t="btnBookDemo">Book a Demo</span>
            <svg class="w-4 h-4 text-limeSpark" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg>
          </button>
        </div>
      </div>

    </div>

    <!-- Bottom Row (2 Cards: Mirzo & Izlai) -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5 sm:gap-6">
      
      <!-- Card 4: MIRZO -->
      <div class="card-elevated p-6 sm:p-7 rounded-3xl flex flex-col justify-between border-t-4 border-t-skyBrand">
        <div>
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center gap-2.5">
              <div class="w-10 h-10 rounded-xl bg-sky-100 text-sky-800 font-extrabold flex items-center justify-center text-sm font-mono shrink-0">
                04
              </div>
              <div>
                <h3 class="text-xl font-extrabold text-slateDark">Mirzo</h3>
                <span class="text-xs text-skyBrand font-mono font-bold block" data-t="mirzoRole">Your Private AI Scribe</span>
              </div>
            </div>
            <span class="text-xs font-mono font-bold text-skyBrand bg-sky-50 px-2 py-0.5 rounded whitespace-nowrap">
              Voice & Scribe
            </span>
          </div>

          <p class="text-slate-600 text-sm leading-relaxed mb-5" data-t="mirzoDesc">
            Private AI meeting notes. <strong>No bots in the call.</strong> Zero awkward avatars. Captures decisions, action items, and deadlines from Zoom, Teams, and Google Meet directly to Telegram and ILDAM CRM.
          </p>

          <div class="space-y-2 text-xs sm:text-sm text-slate-700 mb-6">
            <div class="flex items-start gap-2">
              <svg class="w-4 h-4 text-skyBrand shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              <span data-t="mirzoB1"><strong>Zero-Bot Presence:</strong> 100% confidential. No bot joins or disturbs your client conversations.</span>
            </div>
            <div class="flex items-start gap-2">
              <svg class="w-4 h-4 text-skyBrand shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              <span data-t="mirzoB2"><strong>Precise Action Protocols:</strong> Filters conversational noise into structured owner/deadline briefs.</span>
            </div>
            <div class="flex items-start gap-2">
              <svg class="w-4 h-4 text-skyBrand shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              <span data-t="mirzoB3"><strong>Instant Multi-Channel Dispatch:</strong> Summary and assigned tasks delivered within 60 seconds.</span>
            </div>
          </div>
        </div>

        <!-- Embedded Flywheel Handoff -->
        <div class="pt-4 border-t border-divider">
          <div class="text-xs font-mono text-skyBrand font-bold mb-4" data-t="mirzoHandoff">
            ↳ Updates deal stages & action items back into ILDAM
          </div>
          <button type="button" onclick="openDemoModal('Mirzo Scribe')" class="w-full py-3 px-4 rounded-xl bg-slateDark hover:bg-slate-800 text-white text-sm font-bold text-center transition cursor-pointer flex items-center justify-center gap-2 min-h-[44px]">
            <span data-t="btnBookDemo">Book a Demo</span>
            <svg class="w-4 h-4 text-limeSpark" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg>
          </button>
        </div>
      </div>

      <!-- Card 5: IZLAI -->
      <div class="card-elevated p-6 sm:p-7 rounded-3xl flex flex-col justify-between border-t-4 border-t-indigoBrand">
        <div>
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center gap-2.5">
              <div class="w-10 h-10 rounded-xl bg-indigo-100 text-indigo-800 font-extrabold flex items-center justify-center text-sm font-mono shrink-0">
                05
              </div>
              <div>
                <h3 class="text-xl font-extrabold text-slateDark">Izlai</h3>
                <span class="text-xs text-indigoBrand font-mono font-bold block" data-t="izlaiRole">Your AI Outbound Agent</span>
              </div>
            </div>
            <span class="text-xs font-mono font-bold text-indigoBrand bg-indigo-50 px-2 py-0.5 rounded whitespace-nowrap">
              Outbound Engine
            </span>
          </div>

          <p class="text-slate-600 text-sm leading-relaxed mb-5" data-t="izlaiDesc">
            Eliminates cold prospecting fatigue. Autonomously discovers target accounts, sends hyper-personalized outreach via <strong>Email, LinkedIn, Telegram, and WhatsApp</strong>, and qualifies replies in seconds.
          </p>

          <div class="space-y-2 text-xs sm:text-sm text-slate-700 mb-6">
            <div class="flex items-start gap-2">
              <svg class="w-4 h-4 text-indigoBrand shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              <span data-t="izlaiB1"><strong>Autonomous Account Discovery:</strong> Identifies decision-makers matching your ideal customer profile.</span>
            </div>
            <div class="flex items-start gap-2">
              <svg class="w-4 h-4 text-indigoBrand shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              <span data-t="izlaiB2"><strong>Contextual Reply Qualification:</strong> Analyzes responses, handles skepticism, and schedules warm demos.</span>
            </div>
            <div class="flex items-start gap-2">
              <svg class="w-4 h-4 text-indigoBrand shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
              <span data-t="izlaiB3"><strong>Automated Deal Handoff:</strong> Sales-ready accounts flow straight into ILDAM CRM for your sales closers.</span>
            </div>
          </div>
        </div>

        <!-- Embedded Flywheel Handoff -->
        <div class="pt-4 border-t border-divider">
          <div class="text-xs font-mono text-indigoBrand font-bold mb-4" data-t="izlaiHandoff">
            ↳ Hands warm interested leads directly to Ailo & ILDAM
          </div>
          <button type="button" onclick="openDemoModal('Izlai Outbound')" class="w-full py-3 px-4 rounded-xl bg-slateDark hover:bg-slate-800 text-white text-sm font-bold text-center transition cursor-pointer flex items-center justify-center gap-2 min-h-[44px]">
            <span data-t="btnBookDemo">Book a Demo</span>
            <svg class="w-4 h-4 text-limeSpark" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg>
          </button>
        </div>
      </div>

    </div>
  </section>

  <!-- ==================== INDUSTRY SOLUTIONS (Section 4) ==================== -->
  <section id="solutions" class="py-12 sm:py-14 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-b border-divider">
    <div class="max-w-3xl mb-8">
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-emeraldBrand" data-t="solutionsEyebrow">Ready-made setups for your industry</span>
      <h2 class="text-3xl sm:text-4xl font-extrabold text-slateDark mt-2 tracking-tight" data-t="solutionsTitle">
        Tailored for Your Exact Daily Workflow
      </h2>
      <p class="text-slate-600 text-sm sm:text-base mt-2 leading-relaxed" data-t="solutionsSub">
        Pre-built configurations designed for how your business communicates, books, and gets paid.
      </p>
    </div>

    <!-- 4 Industry Interactive Tab Switchers -->
    <div class="flex flex-wrap items-center gap-2.5 mb-6" role="tablist" aria-label="Industry Solutions">
      <button type="button" id="tab-btn-clinics" onclick="switchIndustryTab('clinics')" class="industry-tab-btn px-4 py-2.5 rounded-xl bg-slateDark text-white font-bold text-xs sm:text-sm shadow-sm transition-all duration-150 cursor-pointer min-h-[44px] flex items-center gap-2" role="tab" aria-selected="true" aria-controls="panel-clinics">
        <span class="w-2 h-2 rounded-full bg-emeraldBrand"></span>
        <span data-t="tabClinics">Clinics & Medical</span>
      </button>
      <button type="button" id="tab-btn-education" onclick="switchIndustryTab('education')" class="industry-tab-btn px-4 py-2.5 rounded-xl bg-white border border-divider hover:bg-subtle text-slate-700 font-bold text-xs sm:text-sm transition-all duration-150 cursor-pointer min-h-[44px] flex items-center gap-2" role="tab" aria-selected="false" aria-controls="panel-education">
        <span class="w-2 h-2 rounded-full bg-purpleBrand"></span>
        <span data-t="tabEducation">Education & Academies</span>
      </button>
      <button type="button" id="tab-btn-auto" onclick="switchIndustryTab('auto')" class="industry-tab-btn px-4 py-2.5 rounded-xl bg-white border border-divider hover:bg-subtle text-slate-700 font-bold text-xs sm:text-sm transition-all duration-150 cursor-pointer min-h-[44px] flex items-center gap-2" role="tab" aria-selected="false" aria-controls="panel-auto">
        <span class="w-2 h-2 rounded-full bg-amberBrand"></span>
        <span data-t="tabAuto">Auto Services & Workshops</span>
      </button>
      <button type="button" id="tab-btn-advisory" onclick="switchIndustryTab('advisory')" class="industry-tab-btn px-4 py-2.5 rounded-xl bg-white border border-divider hover:bg-subtle text-slate-700 font-bold text-xs sm:text-sm transition-all duration-150 cursor-pointer min-h-[44px] flex items-center gap-2" role="tab" aria-selected="false" aria-controls="panel-advisory">
        <span class="w-2 h-2 rounded-full bg-indigoBrand"></span>
        <span data-t="tabAdvisory">Professional & B2B</span>
      </button>
    </div>

    <!-- Master Interactive Dashboard Container -->
    <div class="card-elevated rounded-3xl bg-white border border-divider shadow-md overflow-hidden">
      
      <!-- Dashboard Top Window Header -->
      <div class="px-5 py-3.5 bg-subtle/80 border-b border-divider flex flex-wrap items-center justify-between gap-3">
        <div class="flex items-center gap-3">
          <div class="flex items-center gap-1.5">
            <span class="w-3 h-3 rounded-full bg-rose-400"></span>
            <span class="w-3 h-3 rounded-full bg-amber-400"></span>
            <span class="w-3 h-3 rounded-full bg-emerald-400"></span>
          </div>
          <span class="text-xs font-mono font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-emeraldBrand badge-live-pulse"></span>
            <span data-t="dashStatus">Live Operating Mode</span>
          </span>
        </div>
        <div class="text-xs font-mono font-semibold text-slate-500 flex items-center gap-2">
          <span data-t="dashChannels">Connected Channels:</span>
          <span class="px-2 py-0.5 rounded bg-white border border-divider text-slate-800 font-bold">Instagram Direct</span>
          <span class="px-2 py-0.5 rounded bg-white border border-divider text-slate-800 font-bold">Telegram</span>
          <span class="px-2 py-0.5 rounded bg-white border border-divider text-slate-800 font-bold">1C ERP</span>
        </div>
      </div>

      <!-- PANEL 1: CLINICS & HEALTHCARE -->
      <div id="panel-clinics" class="industry-panel p-6 sm:p-8" role="tabpanel" aria-labelledby="tab-btn-clinics">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 sm:gap-8 items-center">
          
          <!-- Left: Real Conversation & Booking Flow Simulation -->
          <div class="lg:col-span-7 bg-subtle/50 rounded-2xl p-5 border border-divider">
            <div class="flex items-center justify-between pb-3 mb-4 border-b border-divider text-xs font-mono">
              <span class="font-bold text-emeraldBrand">● MedPro Fleet · Patient Flow</span>
              <span class="text-slate-500">Instagram Direct · 14:22</span>
            </div>
            
            <div class="space-y-3 text-xs sm:text-sm">
              <div class="flex items-start gap-2.5">
                <div class="w-8 h-8 rounded-full bg-slate-200 text-slate-700 font-bold flex items-center justify-center shrink-0 text-xs">P</div>
                <div class="p-3.5 rounded-2xl rounded-tl-sm bg-white border border-divider shadow-2xs max-w-md text-slate-800">
                  Assalomu alaykum! Tish oqartirish qancha turadi va ertaga soat 16:00 ga yozilsa bo'ladimi?
                </div>
              </div>
              
              <div class="flex items-start gap-2.5 justify-end">
                <div class="p-3.5 rounded-2xl rounded-tr-sm bg-emerald-600 text-white shadow-2xs max-w-md">
                  Va alaykum assalom! Tish oqartirish narxi 450,000 so'mdan boshlanadi. Ertaga soat 16:00 da Dr. Rustamov qabuliga vaqtincha band qildim. Tasdiqlaysizmi?
                </div>
                <div class="w-8 h-8 rounded-full bg-emerald-800 text-white font-bold flex items-center justify-center shrink-0 text-xs">AI</div>
              </div>

              <div class="p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-xs font-mono text-emerald-900 flex items-center justify-between">
                <span>↳ Bandla: 15-daqiqalik slot band qilindi · 1C: Bemor kartasi tekshirildi</span>
                <span class="font-bold text-emerald-700">0.8s</span>
              </div>
            </div>
          </div>

          <!-- Right: Key Industry Metrics & Direct Action -->
          <div class="lg:col-span-5 flex flex-col justify-between h-full space-y-6">
            <div>
              <div class="inline-flex items-center gap-2 px-2.5 py-0.5 rounded-full bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs font-mono font-bold uppercase mb-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emeraldBrand"></span>
                <span data-t="sol1Tag">For clinics & healthcare</span>
              </div>
              <h3 class="text-2xl font-black text-slateDark mb-2" data-t="sol1Title">GPTify OS for Clinics</h3>
              <p class="text-slate-600 text-sm leading-relaxed mb-5" data-t="sol1Desc">
                Eliminate receptionist phone logjams and patient no-shows. Ailo answers patient queries in 8 seconds across WhatsApp and Telegram, Bandla books doctor appointment slots, ILDAM keeps medical consultation history, and Mirzo transcribes clinical consultations with zero bots.
              </p>

              <!-- 3 Impact Badges -->
              <div class="grid grid-cols-3 gap-2.5 mb-6 text-center">
                <div class="p-3 rounded-xl bg-subtle border border-divider">
                  <div class="text-xl sm:text-2xl font-black text-emeraldBrand">-45%</div>
                  <div class="text-xs font-mono font-bold text-slateMuted mt-0.5">No-Shows</div>
                </div>
                <div class="p-3 rounded-xl bg-subtle border border-divider">
                  <div class="text-xl sm:text-2xl font-black text-slateDark">&lt;8s</div>
                  <div class="text-xs font-mono font-bold text-slateMuted mt-0.5">Response</div>
                </div>
                <div class="p-3 rounded-xl bg-subtle border border-divider">
                  <div class="text-xl sm:text-2xl font-black text-slateDark">42h</div>
                  <div class="text-xs font-mono font-bold text-slateMuted mt-0.5">Saved/Mo</div>
                </div>
              </div>
            </div>

            <div>
              <div class="text-xs font-mono text-slate-500 mb-3 flex items-center gap-1.5 font-bold">
                <span data-t="dashPipeline">Connected Workflow:</span>
                <span class="text-slate-800">Ailo &rarr; Bandla &rarr; ILDAM &rarr; 1C</span>
              </div>
              <button type="button" onclick="openDemoModal('MedPro Clinics')" class="w-full py-3.5 px-4 rounded-xl bg-emeraldBrand hover:bg-emeraldDark text-white text-sm font-bold text-center transition cursor-pointer flex items-center justify-center gap-2 min-h-[44px]">
                <span data-t="dashCtaClinics">Book a Demo for Clinics</span>
                <svg class="w-4 h-4 text-limeSpark" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg>
              </button>
            </div>
          </div>

        </div>
      </div>

      <!-- PANEL 2: EDUCATION & ACADEMIES -->
      <div id="panel-education" class="industry-panel p-6 sm:p-8 hidden" role="tabpanel" aria-labelledby="tab-btn-education">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 sm:gap-8 items-center">
          
          <!-- Left: Real Conversation & Booking Flow Simulation -->
          <div class="lg:col-span-7 bg-subtle/50 rounded-2xl p-5 border border-divider">
            <div class="flex items-center justify-between pb-3 mb-4 border-b border-divider text-xs font-mono">
              <span class="font-bold text-purpleBrand">● EduPro Fleet · Student Admission Flow</span>
              <span class="text-slate-500">Telegram Bot · 16:05</span>
            </div>
            
            <div class="space-y-3 text-xs sm:text-sm">
              <div class="flex items-start gap-2.5">
                <div class="w-8 h-8 rounded-full bg-slate-200 text-slate-700 font-bold flex items-center justify-center shrink-0 text-xs">S</div>
                <div class="p-3.5 rounded-2xl rounded-tl-sm bg-white border border-divider shadow-2xs max-w-md text-slate-800">
                  Assalomu alaykum! IELTS kursingiz qachon boshlanadi? Sinov darsi bormi?
                </div>
              </div>
              
              <div class="flex items-start gap-2.5 justify-end">
                <div class="p-3.5 rounded-2xl rounded-tr-sm bg-purple-600 text-white shadow-2xs max-w-md">
                  Va alaykum assalom! Yangi guruh dushanba boshlanadi. Shanba soat 10:00 da bepul sinov darsi va daraja aniqlash testi mavjud. Joyingizni band qilaymi?
                </div>
                <div class="w-8 h-8 rounded-full bg-purple-800 text-white font-bold flex items-center justify-center shrink-0 text-xs">AI</div>
              </div>

              <div class="p-3 rounded-xl bg-purple-50 border border-purple-200 text-xs font-mono text-purple-900 flex items-center justify-between">
                <span>↳ Bandla: Sinov darsiga 1 ta o'rin ajratildi · ILDAM: 'Sinov darsi' bosqichiga kiritildi</span>
                <span class="font-bold text-purple-700">0.9s</span>
              </div>
            </div>
          </div>

          <!-- Right: Key Industry Metrics & Direct Action -->
          <div class="lg:col-span-5 flex flex-col justify-between h-full space-y-6">
            <div>
              <div class="inline-flex items-center gap-2 px-2.5 py-0.5 rounded-full bg-purple-50 border border-purple-200 text-purple-800 text-xs font-mono font-bold uppercase mb-2">
                <span class="w-1.5 h-1.5 rounded-full bg-purpleBrand"></span>
                <span data-t="sol2Tag">For academies & schools</span>
              </div>
              <h3 class="text-2xl font-black text-slateDark mb-2" data-t="sol2Title">GPTify OS for Education</h3>
              <p class="text-slate-600 text-sm leading-relaxed mb-5" data-t="sol2Desc">
                Convert social media inquiries into enrolled students. Ailo qualifies course interests, Bandla schedules free trial lessons and level evaluations, ILDAM tracks tuition milestones, and Mirzo produces academic review protocols for teachers.
              </p>

              <!-- 3 Impact Badges -->
              <div class="grid grid-cols-3 gap-2.5 mb-6 text-center">
                <div class="p-3 rounded-xl bg-subtle border border-divider">
                  <div class="text-xl sm:text-2xl font-black text-purpleBrand">+38%</div>
                  <div class="text-xs font-mono font-bold text-slateMuted mt-0.5">Attendance</div>
                </div>
                <div class="p-3 rounded-xl bg-subtle border border-divider">
                  <div class="text-xl sm:text-2xl font-black text-slateDark">100%</div>
                  <div class="text-xs font-mono font-bold text-slateMuted mt-0.5">Weekend Lead</div>
                </div>
                <div class="p-3 rounded-xl bg-subtle border border-divider">
                  <div class="text-xl sm:text-2xl font-black text-slateDark">55h</div>
                  <div class="text-xs font-mono font-bold text-slateMuted mt-0.5">Saved/Mo</div>
                </div>
              </div>
            </div>

            <div>
              <div class="text-xs font-mono text-slate-500 mb-3 flex items-center gap-1.5 font-bold">
                <span data-t="dashPipeline">Connected Workflow:</span>
                <span class="text-slate-800">Ailo &rarr; Bandla &rarr; ILDAM &rarr; Payme</span>
              </div>
              <button type="button" onclick="openDemoModal('EduPro Education')" class="w-full py-3.5 px-4 rounded-xl bg-purpleBrand hover:bg-purple-800 text-white text-sm font-bold text-center transition cursor-pointer flex items-center justify-center gap-2 min-h-[44px]">
                <span data-t="dashCtaEducation">Book a Demo for Academies</span>
                <svg class="w-4 h-4 text-limeSpark" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg>
              </button>
            </div>
          </div>

        </div>
      </div>

      <!-- PANEL 3: AUTO SERVICES & WORKSHOPS -->
      <div id="panel-auto" class="industry-panel p-6 sm:p-8 hidden" role="tabpanel" aria-labelledby="tab-btn-auto">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 sm:gap-8 items-center">
          
          <!-- Left: Real Conversation & Booking Flow Simulation -->
          <div class="lg:col-span-7 bg-subtle/50 rounded-2xl p-5 border border-divider">
            <div class="flex items-center justify-between pb-3 mb-4 border-b border-divider text-xs font-mono">
              <span class="font-bold text-amberBrand">● AutoPro Fleet · Workshop Bay Scheduling</span>
              <span class="text-slate-500">Telegram · 11:40</span>
            </div>
            
            <div class="space-y-3 text-xs sm:text-sm">
              <div class="flex items-start gap-2.5">
                <div class="w-8 h-8 rounded-full bg-slate-200 text-slate-700 font-bold flex items-center justify-center shrink-0 text-xs">D</div>
                <div class="p-3.5 rounded-2xl rounded-tl-sm bg-white border border-divider shadow-2xs max-w-md text-slate-800">
                  Assalomu alaykum! Malibu 2 tormoz kolodkalarini almashtirish qancha bo'ladi va bugun bo'sh joy bormi?
                </div>
              </div>
              
              <div class="flex items-start gap-2.5 justify-end">
                <div class="p-3.5 rounded-2xl rounded-tr-sm bg-amber-600 text-white shadow-2xs max-w-md">
                  Va alaykum assalom! Original kolodkalar bilan almashtirish 380,000 so'm. Bugun soat 15:30 da 2-chi boksda bo'sh joy bor. Joy band qilamizmi?
                </div>
                <div class="w-8 h-8 rounded-full bg-amber-800 text-white font-bold flex items-center justify-center shrink-0 text-xs">AI</div>
              </div>

              <div class="p-3 rounded-xl bg-amber-50 border border-amber-200 text-xs font-mono text-amber-900 flex items-center justify-between">
                <span>↳ Bandla: 2-chi boks 15:30 ga band qilindi · 1C: Ehtiyot qism zaxirasi tekshirildi</span>
                <span class="font-bold text-amber-700">0.7s</span>
              </div>
            </div>
          </div>

          <!-- Right: Key Industry Metrics & Direct Action -->
          <div class="lg:col-span-5 flex flex-col justify-between h-full space-y-6">
            <div>
              <div class="inline-flex items-center gap-2 px-2.5 py-0.5 rounded-full bg-amber-50 border border-amber-200 text-amber-800 text-xs font-mono font-bold uppercase mb-2">
                <span class="w-1.5 h-1.5 rounded-full bg-amberBrand"></span>
                <span data-t="sol3Tag">For auto services & workshops</span>
              </div>
              <h3 class="text-2xl font-black text-slateDark mb-2" data-t="sol3Title">GPTify OS for Automotive</h3>
              <p class="text-slate-600 text-sm leading-relaxed mb-5" data-t="sol3Desc">
                Maximize service bay capacity and vehicle sales. Ailo handles trade-in and maintenance inquiries, Bandla manages test-drive and bay appointments, ILDAM manages vehicle orders and spare part invoices, while Izlai conducts corporate fleet outreach.
              </p>

              <!-- 3 Impact Badges -->
              <div class="grid grid-cols-3 gap-2.5 mb-6 text-center">
                <div class="p-3 rounded-xl bg-subtle border border-divider">
                  <div class="text-xl sm:text-2xl font-black text-amberBrand">+28%</div>
                  <div class="text-xs font-mono font-bold text-slateMuted mt-0.5">Bay Capacity</div>
                </div>
                <div class="p-3 rounded-xl bg-subtle border border-divider">
                  <div class="text-xl sm:text-2xl font-black text-slateDark">0</div>
                  <div class="text-xs font-mono font-bold text-slateMuted mt-0.5">Missed Leads</div>
                </div>
                <div class="p-3 rounded-xl bg-subtle border border-divider">
                  <div class="text-xl sm:text-2xl font-black text-slateDark">35h</div>
                  <div class="text-xs font-mono font-bold text-slateMuted mt-0.5">Saved/Mo</div>
                </div>
              </div>
            </div>

            <div>
              <div class="text-xs font-mono text-slate-500 mb-3 flex items-center gap-1.5 font-bold">
                <span data-t="dashPipeline">Connected Workflow:</span>
                <span class="text-slate-800">Ailo &rarr; Bandla &rarr; ILDAM &rarr; 1C ERP</span>
              </div>
              <button type="button" onclick="openDemoModal('AutoPro Automotive')" class="w-full py-3.5 px-4 rounded-xl bg-amberBrand hover:bg-amber-700 text-white text-sm font-bold text-center transition cursor-pointer flex items-center justify-center gap-2 min-h-[44px]">
                <span data-t="dashCtaAuto">Book a Demo for Auto Services</span>
                <svg class="w-4 h-4 text-limeSpark" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg>
              </button>
            </div>
          </div>

        </div>
      </div>

      <!-- PANEL 4: PROFESSIONAL & B2B ADVISORY -->
      <div id="panel-advisory" class="industry-panel p-6 sm:p-8 hidden" role="tabpanel" aria-labelledby="tab-btn-advisory">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 sm:gap-8 items-center">
          
          <!-- Left: Real Conversation & Booking Flow Simulation -->
          <div class="lg:col-span-7 bg-subtle/50 rounded-2xl p-5 border border-divider">
            <div class="flex items-center justify-between pb-3 mb-4 border-b border-divider text-xs font-mono">
              <span class="font-bold text-indigoBrand">● AdvisoryPro Fleet · Inbound Discovery</span>
              <span class="text-slate-500">Website / LinkedIn · 10:15</span>
            </div>
            
            <div class="space-y-3 text-xs sm:text-sm">
              <div class="flex items-start gap-2.5">
                <div class="w-8 h-8 rounded-full bg-slate-200 text-slate-700 font-bold flex items-center justify-center shrink-0 text-xs">C</div>
                <div class="p-3.5 rounded-2xl rounded-tl-sm bg-white border border-divider shadow-2xs max-w-md text-slate-800">
                  Salom! Biz 25 kishilik sotuv bo'limimiz uchun CRM va lidlarni avtomatlashtirishni ko'rib chiqmoqchimiz.
                </div>
              </div>
              
              <div class="flex items-start gap-2.5 justify-end">
                <div class="p-3.5 rounded-2xl rounded-tr-sm bg-indigo-600 text-white shadow-2xs max-w-md">
                  Salom! 25 kishilik jamoa uchun ILDAM CRM va Ailo orqali kunlik 300+ lidlarni qayta ishlash mumkin. 30 daqiqalik audit uchun qaysi vaqt qulay?
                </div>
                <div class="w-8 h-8 rounded-full bg-indigo-800 text-white font-bold flex items-center justify-center shrink-0 text-xs">AI</div>
              </div>

              <div class="p-3 rounded-xl bg-indigo-50 border border-indigo-200 text-xs font-mono text-indigo-900 flex items-center justify-between">
                <span>↳ Bandla: Google Meet havolasi yaratildi · Mirzo: Uchrashuv brifi tayyorlandi</span>
                <span class="font-bold text-indigo-700">0.8s</span>
              </div>
            </div>
          </div>

          <!-- Right: Key Industry Metrics & Direct Action -->
          <div class="lg:col-span-5 flex flex-col justify-between h-full space-y-6">
            <div>
              <div class="inline-flex items-center gap-2 px-2.5 py-0.5 rounded-full bg-indigo-50 border border-indigo-200 text-indigo-800 text-xs font-mono font-bold uppercase mb-2">
                <span class="w-1.5 h-1.5 rounded-full bg-indigoBrand"></span>
                <span data-t="sol4Tag">For consulting & advisory firms</span>
              </div>
              <h3 class="text-2xl font-black text-slateDark mb-2" data-t="sol4Title">GPTify OS for Professional Services</h3>
              <p class="text-slate-600 text-sm leading-relaxed mb-5" data-t="sol4Desc">
                Run an end-to-end client engine. Izlai discovers and prospects ideal corporate clients, Ailo handles website and social leads, Bandla books consultations, ILDAM enforces retainer milestones, and Mirzo records partner meetings with zero-bot discretion.
              </p>

              <!-- 3 Impact Badges -->
              <div class="grid grid-cols-3 gap-2.5 mb-6 text-center">
                <div class="p-3 rounded-xl bg-subtle border border-divider">
                  <div class="text-xl sm:text-2xl font-black text-indigoBrand">3x</div>
                  <div class="text-xs font-mono font-bold text-slateMuted mt-0.5">Ready Deals</div>
                </div>
                <div class="p-3 rounded-xl bg-subtle border border-divider">
                  <div class="text-xl sm:text-2xl font-black text-slateDark">100%</div>
                  <div class="text-xs font-mono font-bold text-slateMuted mt-0.5">CRM Accuracy</div>
                </div>
                <div class="p-3 rounded-xl bg-subtle border border-divider">
                  <div class="text-xl sm:text-2xl font-black text-slateDark">50h</div>
                  <div class="text-xs font-mono font-bold text-slateMuted mt-0.5">Saved/Mo</div>
                </div>
              </div>
            </div>

            <div>
              <div class="text-xs font-mono text-slate-500 mb-3 flex items-center gap-1.5 font-bold">
                <span data-t="dashPipeline">Connected Workflow:</span>
                <span class="text-slate-800">Izlai &rarr; Ailo &rarr; ILDAM &rarr; Mirzo</span>
              </div>
              <button type="button" onclick="openDemoModal('AdvisoryPro B2B')" class="w-full py-3.5 px-4 rounded-xl bg-indigoBrand hover:bg-indigo-700 text-white text-sm font-bold text-center transition cursor-pointer flex items-center justify-center gap-2 min-h-[44px]">
                <span data-t="dashCtaAdvisory">Book a Demo for Advisory Firms</span>
                <svg class="w-4 h-4 text-limeSpark" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg>
              </button>
            </div>
          </div>

        </div>
      </div>

    </div>

    </div>
  </section>

  <!-- ==================== RECOVERABLE LOSS CALCULATOR (Section 5) ==================== -->
  <section id="calculator" class="py-12 sm:py-14 px-4 sm:px-6 lg:px-8 max-w-5xl mx-auto border-b border-divider">
    <div class="text-center max-w-2xl mx-auto mb-8">
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-emeraldBrand">Interactive Calculator</span>
      <h2 class="text-3xl sm:text-4xl font-extrabold text-slateDark mt-2 tracking-tight" data-t="calcTitle">
        How much time and money could you get back?
      </h2>
      <p class="text-slate-600 text-sm sm:text-base mt-2" data-t="calcSub">
        Adjust team size and average hourly rates to see your estimated savings with automated triage and scheduling.
      </p>
    </div>

    <div class="card-elevated rounded-3xl p-6 sm:p-10 bg-white border border-divider shadow-md">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        
        <!-- Controls Column -->
        <div class="lg:col-span-7 space-y-6">
          <!-- Slider 1 -->
          <div>
            <div class="flex items-center justify-between text-sm font-bold text-slateDark mb-2">
              <span>Customer-Facing Team Size</span>
              <span id="calcTeamVal" class="font-mono text-emeraldBrand font-black text-base">5 people</span>
            </div>
            <input type="range" id="calcTeam" min="1" max="50" value="5" oninput="calculateLosses()" class="w-full">
            <div class="flex justify-between text-xs text-slate-400 font-mono mt-1">
              <span>1</span>
              <span>25</span>
              <span>50+</span>
            </div>
          </div>

          <!-- Slider 2 -->
          <div>
            <div class="flex items-center justify-between text-sm font-bold text-slateDark mb-2">
              <span>Average Fully-Loaded Hourly Cost</span>
              <span id="calcRateVal" class="font-mono text-emeraldBrand font-black text-base">$12/hr</span>
            </div>
            <input type="range" id="calcRate" min="5" max="50" value="12" oninput="calculateLosses()" class="w-full">
            <div class="flex justify-between text-xs text-slate-400 font-mono mt-1">
              <span>$5/hr</span>
              <span>$25/hr</span>
              <span>$50/hr</span>
            </div>
          </div>

          <!-- Slider 3 -->
          <div>
            <div class="flex items-center justify-between text-sm font-bold text-slateDark mb-2">
              <span>Hours Spent on Manual Messaging & Booking</span>
              <span id="calcHoursVal" class="font-mono text-emeraldBrand font-black text-base">10 hrs/wk</span>
            </div>
            <input type="range" id="calcHours" min="3" max="25" value="10" oninput="calculateLosses()" class="w-full">
            <div class="flex justify-between text-xs text-slate-400 font-mono mt-1">
              <span>3h</span>
              <span>14h</span>
              <span>25h</span>
            </div>
          </div>
        </div>

        <!-- Result Box Column -->
        <div class="lg:col-span-5 bg-subtle/80 rounded-2xl p-6 sm:p-7 border border-divider flex flex-col justify-between text-center">
          <div>
            <span class="text-xs font-mono font-bold uppercase tracking-wider text-slate-500 block mb-2" data-t="calcResLabel">
              Estimated yearly savings
            </span>
            <div id="calcResAnnual" class="text-4xl sm:text-5xl font-black font-mono text-emeraldBrand tracking-tight mb-2">
              $19,380
            </div>
            <div class="flex items-center justify-center gap-4 text-xs font-mono text-slate-600 mb-6">
              <div>
                <span class="block text-slate-400">Monthly</span>
                <span id="calcResMonthly" class="font-bold text-slate-800 text-sm">$1,615</span>
              </div>
              <div class="h-6 w-px bg-divider"></div>
              <div>
                <span class="block text-slate-400">Hours Saved</span>
                <span id="calcResHours" class="font-bold text-slate-800 text-sm">190h/mo</span>
              </div>
            </div>
          </div>

          <button type="button" onclick="openDemoModal('ROI Calculator')" class="w-full py-3.5 px-4 rounded-xl bg-slateDark hover:bg-slate-800 text-white text-sm font-bold shadow-md transition cursor-pointer flex items-center justify-center gap-2 min-h-[44px]">
            <span data-t="btnBookDemo">Book a Demo</span>
            <svg class="w-4 h-4 text-limeSpark" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg>
          </button>
        </div>

      </div>
    </div>
  </section>

  <!-- ==================== FAQ ACCORDION + FINAL CALL TO ACTION (Section 6) ==================== -->
  <section id="faq" class="py-12 sm:py-14 px-4 sm:px-6 lg:px-8 max-w-4xl mx-auto">
    <!-- FAQ Header -->
    <div class="text-center max-w-2xl mx-auto mb-8">
      <span class="text-xs font-mono font-bold uppercase tracking-wider text-emeraldBrand" data-t="faqEyebrow">Answers & Transparency</span>
      <h2 class="text-3xl sm:text-4xl font-extrabold text-slateDark mt-2 tracking-tight" data-t="faqTitle">
        Frequently Asked Questions
      </h2>
    </div>

    <!-- FAQ Accordion -->
    <div class="space-y-3.5 mb-8">
      <details class="group bg-white border border-divider rounded-2xl p-5 shadow-xs" open>
        <summary class="flex items-center justify-between text-base font-bold text-slateDark">
          <span data-t="faqQ1">How do the 5 engines (Ailo, ILDAM, Bandla, Mirzo, Izlai) work together?</span>
          <svg class="faq-chevron w-5 h-5 text-slate-400 transition-transform duration-200" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5"/></svg>
        </summary>
        <div class="pt-3 text-sm text-slate-600 leading-relaxed border-t border-divider mt-3" data-t="faqA1">
          They form one continuous loop: Izlai discovers and prospects accounts, Ailo engages incoming inquiries in 8 seconds, ILDAM tracks the relationship and payment milestones, Bandla locks calendar appointments, and Mirzo records meeting action items without bots. Data flows between them seamlessly so no human enters data twice.
        </div>
      </details>

      <details class="group bg-white border border-divider rounded-2xl p-5 shadow-xs">
        <summary class="flex items-center justify-between text-base font-bold text-slateDark">
          <span data-t="faqQ2">How does Mirzo record meetings without a bot joining the call?</span>
          <svg class="faq-chevron w-5 h-5 text-slate-400 transition-transform duration-200" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5"/></svg>
        </summary>
        <div class="pt-3 text-sm text-slate-600 leading-relaxed border-t border-divider mt-3" data-t="faqA2">
          Unlike ordinary AI notetakers that force an awkward "Bot Assistant" into your Zoom or Google Meet room, Mirzo operates with zero-bot presence. Audio is processed via private executive audio streams or post-call recordings, delivering structured action items directly to your Telegram or ILDAM CRM in 60 seconds with 100% confidentiality.
        </div>
      </details>

      <details class="group bg-white border border-divider rounded-2xl p-5 shadow-xs">
        <summary class="flex items-center justify-between text-base font-bold text-slateDark">
          <span data-t="faqQ3">Can Bandla integrate with our existing calendars and prevent double-booking?</span>
          <svg class="faq-chevron w-5 h-5 text-slate-400 transition-transform duration-200" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5"/></svg>
        </summary>
        <div class="pt-3 text-sm text-slate-600 leading-relaxed border-t border-divider mt-3" data-t="faqA3">
          Yes. Bandla connects directly with Google Calendar, Outlook, and your internal staff shifts. When Ailo qualifies a patient or client, Bandla checks real-time availability and confirms the slot. It automatically sends reminder alerts to slash no-shows.
        </div>
      </details>

      <details class="group bg-white border border-divider rounded-2xl p-5 shadow-xs">
        <summary class="flex items-center justify-between text-base font-bold text-slateDark">
          <span data-t="faqQ4">How is our customer database and operational data protected?</span>
          <svg class="faq-chevron w-5 h-5 text-slate-400 transition-transform duration-200" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5"/></svg>
        </summary>
        <div class="pt-3 text-sm text-slate-600 leading-relaxed border-t border-divider mt-3" data-t="faqA4">
          All infrastructure runs on your dedicated cloud accounts or private enterprise servers. We avoid unverified third-party scrapers: we use official Meta Graph APIs, end-to-end encrypted databases, and strict access controls. Your client data remains 100% your enterprise property.
        </div>
      </details>

      <details class="group bg-white border border-divider rounded-2xl p-5 shadow-xs">
        <summary class="flex items-center justify-between text-base font-bold text-slateDark">
          <span data-t="faqQ5">How long does deployment and team onboarding take?</span>
          <svg class="faq-chevron w-5 h-5 text-slate-400 transition-transform duration-200" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5"/></svg>
        </summary>
        <div class="pt-3 text-sm text-slate-600 leading-relaxed border-t border-divider mt-3" data-t="faqA5">
          Core deployment installs within 48 hours to 5 business days. Following setup, we run live interactive team training sessions, deliver step-by-step video manuals, and provide dedicated monitoring during the initial 14-day operational ramp.
        </div>
      </details>
    </div>

    <!-- Final Strategy Call CTA Card -->
    <div class="bg-white rounded-3xl border border-divider p-6 sm:p-8 shadow-sm text-center relative overflow-hidden">
      <div class="max-w-2xl mx-auto">
        <div class="w-14 h-14 rounded-2xl bg-slateDark text-white font-black text-xl flex items-center justify-center mx-auto mb-5 shadow-sm">
          G
        </div>

        <!-- Roadmap note folded into final CTA (Requirement A & C) -->
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-50 border border-emerald-200 text-xs font-mono font-bold text-emerald-800 mb-4">
          <span class="w-1.5 h-1.5 rounded-full bg-emeraldBrand"></span>
          <span data-t="ctaHowWeStart">How we start: 1. Process Audit → 2. Quick Setup & Integration → 3. Live in 14 Days</span>
        </div>

        <h2 class="text-3xl sm:text-4xl font-extrabold text-slateDark tracking-tight mb-3" data-t="ctaTitle">
          Put your customer communication and bookings on autopilot
        </h2>

        <p class="text-slate-600 text-sm sm:text-base leading-relaxed mb-6" data-t="ctaSub">
          During this 30-minute session, we map where your business is losing hours and revenue, delivering a pragmatic action plan with zero sales pressure.
        </p>

        <!-- Owner Pricing Slot (Requirement D: hidden until rate provided) -->
        <div id="pricing-slot" class="hidden text-sm text-slate-500 font-medium mb-6" data-t="pricingSlot">
          Starting from $___ / month
        </div>

        <!-- Operational Guarantee -->
        <div class="p-4 rounded-xl bg-emerald-50 border border-emerald-100 text-xs sm:text-sm text-emerald-900 font-medium mb-8 max-w-lg mx-auto flex items-center gap-2.5 text-left">
          <svg class="w-5 h-5 text-emerald-600 shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z"/></svg>
          <div data-t="founderGuarantee">
            <strong>Our Guarantee:</strong> If we fail to identify at least $2,000+ in annual recoverable operational savings during the call, we will candidly say so and respect your time.
          </div>
        </div>

        <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
          <button type="button" onclick="openDemoModal('Final CTA')" class="w-full sm:w-auto px-8 py-3.5 rounded-xl bg-emeraldBrand hover:bg-emeraldDark text-white font-bold text-sm shadow-md transition duration-150 flex items-center justify-center gap-2.5 cursor-pointer min-h-[44px]">
            <span data-t="btnBookDemo">Book a Demo</span>
            <svg class="w-4 h-4 text-limeSpark" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg>
          </button>
          <a href="https://t.me/GPTify_uz_bot?start=os_demo" target="_blank" rel="noopener noreferrer" class="w-full sm:w-auto px-6 py-3.5 rounded-xl border border-divider hover:bg-subtle text-slateDark font-semibold text-sm transition duration-150 cursor-pointer min-h-[44px] flex items-center justify-center" data-t="founderCtaTelegram">
            Message on Telegram
          </a>
        </div>

        <div class="mt-8 pt-6 border-t border-divider text-center">
          <div class="text-sm font-bold text-slateDark">GPTify Architecture Team</div>
          <div class="text-xs text-slateMuted mt-0.5">Pragmatic Workflow & Operations Systems</div>
        </div>
      </div>
    </div>
  </section>
"""

# ==================== ARCHITECTURE PAGE BODY ====================
def get_architecture_body(lang):
    return f"""
  <!-- ==================== ARCHITECTURE & API PLATFORM (Dedicated Page) ==================== -->
  <main class="py-14 sm:py-20 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
    
    <!-- Hero Header -->
    <div class="text-center max-w-3xl mx-auto mb-14">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white border border-divider text-xs font-bold text-slateDark mb-3.5 shadow-2xs">
        <span class="w-2 h-2 rounded-full bg-emeraldBrand badge-live-pulse" aria-hidden="true"></span>
        <span data-t="archPageTitle">Enterprise Cloud & AI Foundation</span>
      </div>
      <h1 class="text-3xl sm:text-4xl font-extrabold text-slateDark tracking-tight" data-t="archHeroH1">
        Engineered for High-Throughput Inference, Zero Data Leakage, and Seamless Scale.
      </h1>
      <p class="text-slate-600 text-sm sm:text-base mt-3 leading-relaxed" data-t="archPageSub">
        Built on multi-model LLM routing, isolated tenant data boundaries, and event-driven webhooks for scale and enterprise compliance.
      </p>
    </div>

    <!-- 4 Architectural Pillars Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      
      <!-- Pillar 1 -->
      <div class="card-elevated p-6 rounded-2xl bg-white border border-divider flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-emerald-50 border border-emerald-100 flex items-center justify-center text-emeraldBrand mb-4">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9.75 3.104v5.714a2.25 2.25 0 01-.659 1.591L5 14.5M9.75 3.104c-.251.023-.501.05-.75.082m.75-.082a24.301 24.301 0 014.5 0m0 0v5.714c0 .597.237 1.17.659 1.591L19.8 15.3M14.25 3.104c.251.023.501.05.75.082M19.8 15.3l-1.57.393A9.065 9.065 0 0112 15a9.065 9.065 0 00-6.23.693L5 14.5m14.8.8l1.402 1.402c1.232 1.232.65 3.318-1.067 3.611A48.309 48.309 0 0112 21c-2.773 0-5.491-.235-8.135-.687-1.718-.293-2.3-2.379-1.067-3.61L5 14.5"/></svg>
          </div>
          <h3 class="text-base font-bold text-slateDark mb-1.5" data-t="archP1Title">Multi-Model Foundation Routing</h3>
          <p class="text-xs sm:text-sm text-slate-600 leading-relaxed mb-4" data-t="archP1Desc">
            Dual-routed inference between Google Gemini 2.0 Flash (sub-800ms triage) and Azure OpenAI GPT-4o (complex clinical reasoning). Automatic fallback and local context caching.
          </p>
        </div>
        <div class="pt-3 border-t border-divider flex flex-wrap gap-1.5 text-xs font-mono font-semibold text-slate-600">
          <span class="px-2 py-0.5 rounded bg-subtle border border-divider">Gemini 2.0 Flash</span>
          <span class="px-2 py-0.5 rounded bg-subtle border border-divider">Azure OpenAI</span>
          <span class="px-2 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-200">&lt;800ms Latency</span>
        </div>
      </div>

      <!-- Pillar 2 -->
      <div class="card-elevated p-6 rounded-2xl bg-white border border-divider flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-sky-50 border border-sky-100 flex items-center justify-center text-skyBrand mb-4">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 18.75a6 6 0 006-6v-1.5m-6 7.5a6 6 0 01-6-6v-1.5m6 7.5v3.75m-3.75 0h7.5M12 15.75a3 3 0 01-3-3V4.5a3 3 0 116 0v8.25a3 3 0 01-3 3z"/></svg>
          </div>
          <h3 class="text-base font-bold text-slateDark mb-1.5" data-t="archP2Title">Real-Time Audio & Speech (Mirzo)</h3>
          <p class="text-xs sm:text-sm text-slate-600 leading-relaxed mb-4" data-t="archP2Desc">
            Whisper Large-v3 and Gemini Multimodal audio pipelines transcribing staff voice notes and client calls. Native Uzbek & Russian dialect processing with clinical action synthesis.
          </p>
        </div>
        <div class="pt-3 border-t border-divider flex flex-wrap gap-1.5 text-xs font-mono font-semibold text-slate-600">
          <span class="px-2 py-0.5 rounded bg-subtle border border-divider">Whisper Large-v3</span>
          <span class="px-2 py-0.5 rounded bg-subtle border border-divider">Gemini Multimodal</span>
          <span class="px-2 py-0.5 rounded bg-sky-50 text-sky-800 border border-sky-200">UZ/RU Speech</span>
        </div>
      </div>

      <!-- Pillar 3 -->
      <div class="card-elevated p-6 rounded-2xl bg-white border border-divider flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-indigo-50 border border-indigo-100 flex items-center justify-center text-indigoBrand mb-4">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z"/></svg>
          </div>
          <h3 class="text-base font-bold text-slateDark mb-1.5" data-t="archP3Title">Enterprise Data Boundaries</h3>
          <p class="text-xs sm:text-sm text-slate-600 leading-relaxed mb-4" data-t="archP3Desc">
            Strict row-level multi-tenancy with tenant data isolation. Zero customer data is retained for external LLM training. Encrypted at rest via AES-256 and in transit via TLS 1.3.
          </p>
        </div>
        <div class="pt-3 border-t border-divider flex flex-wrap gap-1.5 text-xs font-mono font-semibold text-slate-600">
          <span class="px-2 py-0.5 rounded bg-subtle border border-divider">AES-256</span>
          <span class="px-2 py-0.5 rounded bg-subtle border border-divider">Row-Level Security</span>
          <span class="px-2 py-0.5 rounded bg-indigo-50 text-indigo-800 border border-indigo-200">HIPAA Ready</span>
        </div>
      </div>

      <!-- Pillar 4 -->
      <div class="card-elevated p-6 rounded-2xl bg-white border border-divider flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-purple-50 border border-purple-100 flex items-center justify-center text-purpleBrand mb-4">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.19 8.688a4.5 4.5 0 011.242 7.244l-4.5 4.5a4.5 4.5 0 01-6.364-6.364l1.757-1.757m13.35-.622l1.757-1.757a4.5 4.5 0 00-6.364-6.364l-4.5 4.5a4.5 4.5 0 001.242 7.244"/></svg>
          </div>
          <h3 class="text-base font-bold text-slateDark mb-1.5" data-t="archP4Title">Event-Driven Webhooks</h3>
          <p class="text-xs sm:text-sm text-slate-600 leading-relaxed mb-4" data-t="archP4Desc">
            Real-time webhook dispatcher powering instant synchronization with 1C:Enterprise, Click/Payme billing gateways, internal Telegram channels, and Google Calendar.
          </p>
        </div>
        <div class="pt-3 border-t border-divider flex flex-wrap gap-1.5 text-xs font-mono font-semibold text-slate-600">
          <span class="px-2 py-0.5 rounded bg-subtle border border-divider">1C ERP Webhooks</span>
          <span class="px-2 py-0.5 rounded bg-subtle border border-divider">Idempotent</span>
          <span class="px-2 py-0.5 rounded bg-purple-50 text-purple-800 border border-purple-200">&lt;200ms Dispatch</span>
        </div>
      </div>

    </div>

    <!-- Developer Platform & Live API Dispatch (Requirement E.6: mobile scroll + non-overlapping header) -->
    <div class="bg-[#0B1120] rounded-3xl border border-slate-800 overflow-hidden shadow-2xl mb-8">
      <!-- Terminal Header -->
      <div class="px-6 py-4 bg-[#0F172A] border-b border-slate-800 flex flex-wrap items-center justify-between gap-3">
        <div class="flex items-center gap-3">
          <div class="flex items-center gap-1.5">
            <span class="w-3 h-3 rounded-full bg-rose-500/80"></span>
            <span class="w-3 h-3 rounded-full bg-amber-500/80"></span>
            <span class="w-3 h-3 rounded-full bg-emerald-500/80"></span>
          </div>
          <span class="text-xs font-mono text-slate-400 font-semibold hidden sm:inline">
            GPTify OS · Fleet Dispatch Runtime
          </span>
        </div>

        <!-- Language Code Tabs (44px min tap targets) -->
        <div class="flex items-center bg-slate-900 rounded-xl p-1 border border-slate-800 text-xs font-mono font-bold">
          <button type="button" id="tab-btn-curl" onclick="switchApiTab('curl')" class="api-tab-btn px-3 py-2 rounded-lg bg-white text-slateDark shadow-2xs cursor-pointer min-h-[44px]">cURL</button>
          <button type="button" id="tab-btn-python" onclick="switchApiTab('python')" class="api-tab-btn px-3 py-2 rounded-lg text-slateMuted hover:text-white cursor-pointer min-h-[44px]">Python</button>
          <button type="button" id="tab-btn-node" onclick="switchApiTab('node')" class="api-tab-btn px-3 py-2 rounded-lg text-slateMuted hover:text-white cursor-pointer min-h-[44px]">Node.js</button>
          <button type="button" id="tab-btn-response" onclick="switchApiTab('response')" class="api-tab-btn px-3 py-2 rounded-lg text-slateMuted hover:text-white cursor-pointer min-h-[44px]">Response</button>
        </div>
      </div>

      <!-- Code Snippet Area -->
      <div class="grid grid-cols-1 lg:grid-cols-12 text-xs font-mono">
        <!-- Left Code Block (Col 7) -->
        <div class="lg:col-span-7 p-6 border-b lg:border-b-0 lg:border-r border-slate-800 overflow-x-auto">
          <!-- Request Bar: flex-wrap to avoid overlapping URL on mobile (Requirement E.6) -->
          <div class="flex flex-wrap items-center justify-between gap-2 text-xs text-slate-400 font-semibold mb-4">
            <div class="flex flex-wrap items-center gap-2">
              <span class="px-2 py-1 rounded bg-amber-500/20 text-amber-300 font-mono text-xs font-bold uppercase tracking-wider">Example Request</span>
              <span class="px-2 py-1 rounded bg-emerald-500/20 text-emerald-400 font-bold">POST</span>
              <span class="text-slate-300 break-all">https://api.gptify.co/v1/fleet/dispatch</span>
            </div>
            <span class="px-2 py-1 rounded bg-slate-800 text-slate-400 font-mono text-xs shrink-0">Bearer Token Auth</span>
          </div>

          <!-- cURL Tab Content -->
          <pre id="api-snippet-curl" class="text-slate-300 leading-relaxed overflow-x-auto text-xs sm:text-sm"><code>curl -X POST https://api.gptify.co/v1/fleet/dispatch \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{{
    "tenant_id": "clinic_tashkent_medpro",
    "channel": "instagram_direct",
    "sender_id": "user_ig_99214a",
    "message": "Hi, how much is teeth whitening and is Dr. Rustamov free tomorrow at 16:00?",
    "engines": ["ailo", "bandla", "ildam"]
  }}'</code></pre>

          <!-- Python Tab Content -->
          <pre id="api-snippet-python" class="hidden text-slate-300 leading-relaxed overflow-x-auto text-xs sm:text-sm"><code>import httpx

async with httpx.AsyncClient() as client:
    response = await client.post(
        "https://api.gptify.co/v1/fleet/dispatch",
        headers={{"Authorization": "Bearer YOUR_API_KEY"}},
        json={{
            "tenant_id": "clinic_tashkent_medpro",
            "channel": "instagram_direct",
            "sender_id": "user_ig_99214a",
            "message": "Hi, how much is teeth whitening?",
            "engines": ["ailo", "bandla", "ildam"]
        }}
    )
    result = response.json()
    print(result["status"], result["execution_time_ms"])</code></pre>

          <!-- Node.js Tab Content -->
          <pre id="api-snippet-node" class="hidden text-slate-300 leading-relaxed overflow-x-auto text-xs sm:text-sm"><code>import {{ GPTifyOS }} from '@gptify/sdk';

const client = new GPTifyOS({{ apiKey: 'YOUR_API_KEY' }});

const event = await client.fleet.dispatch({{
  tenantId: 'clinic_tashkent_medpro',
  channel: 'instagram_direct',
  senderId: 'user_ig_99214a',
  message: 'Hi, how much is teeth whitening?',
  engines: ['ailo', 'bandla', 'ildam']
}});

console.log(`Autonomous execution verified: ${{event.executionId}}`);</code></pre>

          <!-- Response Tab Content -->
          <pre id="api-snippet-response" class="hidden text-emerald-400 leading-relaxed overflow-x-auto text-xs sm:text-sm"><code>{{
  "status": "success",
  "execution_id": "exec_live_89a3f2b1c",
  "latency_ms": 182,
  "telemetry": {{
    "ailo": {{
      "intent": "service_inquiry_and_booking",
      "service": "Teeth Whitening",
      "price_quoted": "1,200,000 UZS"
    }},
    "bandla": {{
      "slot_held": "2026-11-16T16:00:00+05:00",
      "doctor": "Dr. Rustamov",
      "conflict_status": "zero_conflicts"
    }},
    "ildam": {{
      "lead_id": "crm_lead_44810a",
      "stage": "qualified_appointment_held"
    }}
  }}
}}</code></pre>
        </div>

        <!-- Right Explanation Block (Col 5) -->
        <div class="lg:col-span-5 p-6 bg-[#0E1526] flex flex-col justify-between">
          <div class="space-y-4">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
              <span class="text-xs text-slate-400 uppercase tracking-wider font-bold">Latency Benchmark</span>
              <span class="text-xs text-emerald-400 font-bold bg-emerald-500/10 px-2 py-0.5 rounded">200 OK · 182ms</span>
            </div>

            <div class="space-y-3 text-xs sm:text-sm text-slate-300 leading-relaxed">
              <div class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mt-2 shrink-0"></span>
                <span><strong>Multi-Engine Triage:</strong> Ailo evaluates intent, Bandla locks available doctor calendar slots, and ILDAM registers deal records in 182ms.</span>
              </div>
              <div class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mt-2 shrink-0"></span>
                <span><strong>Zero Token Waste:</strong> Cached prompts and semantic vector routing eliminate redundant LLM overhead.</span>
              </div>
              <div class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mt-2 shrink-0"></span>
                <span><strong>Webhook Dispatch:</strong> Outbound sync to 1C ERP, Click, Payme, and Telegram dispatches asynchronously.</span>
              </div>
            </div>
          </div>

          <div class="pt-6 border-t border-slate-800 mt-6">
            <button type="button" onclick="openDemoModal('Architecture API')" class="w-full py-3 px-4 rounded-xl bg-emeraldBrand hover:bg-emeraldDark text-white text-sm font-bold text-center transition cursor-pointer flex items-center justify-center gap-2 min-h-[44px]">
              <span data-t="btnBookDemo">Book a Demo</span>
              <svg class="w-4 h-4 text-limeSpark" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg>
            </button>
          </div>
        </div>

      </div>
    </div>

    <!-- Return to Homepage & CTA Banner -->
    <div class="p-8 rounded-3xl bg-white border border-divider shadow-sm text-center max-w-2xl mx-auto">
      <h3 class="text-xl sm:text-2xl font-black text-slateDark mb-2">Ready to deploy GPTify OS for your enterprise?</h3>
      <p class="text-sm text-slate-600 mb-6">Schedule a 30-minute architecture review with our systems engineers.</p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-3">
        <button type="button" onclick="openDemoModal('Architecture Bottom CTA')" class="w-full sm:w-auto px-6 py-3.5 rounded-xl bg-slateDark hover:bg-slate-800 text-white font-bold text-sm shadow-md transition cursor-pointer min-h-[44px]">
          <span data-t="btnBookDemo">Book a Demo</span>
        </button>
        <a href="/" class="w-full sm:w-auto px-6 py-3.5 rounded-xl border border-divider hover:bg-subtle text-slateDark font-semibold text-sm transition cursor-pointer min-h-[44px] flex items-center justify-center">
          &larr; Return to Homepage
        </a>
      </div>
    </div>

  </main>
"""

# ==================== BUILD AND RENDER PAGES ====================
def build_all_pages():
    pages = [
        # Homepage
        {
            'type': 'home',
            'lang': 'en',
            'rel_path': 'index.html',
            'canonical': 'https://gptify.si/',
            'title': "GPTify OS — The AI Operating System for Service Businesses | GPTify",
            'desc': "GPTify OS connects customer conversations, CRM, scheduling, meetings, and automation through a unified layer of AI agents."
        },
        {
            'type': 'home',
            'lang': 'uz',
            'rel_path': os.path.join('uz', 'index.html'),
            'canonical': 'https://gptify.si/uz/',
            'title': "GPTify OS — Xizmat Ko'rsatish Bizneslari Uchun AI Operatsion Tizimi | GPTify",
            'desc': "GPTify OS — xizmat ko'rsatish bizneslari uchun AI operatsion tizimi. Mijozlar bilan muloqot, CRM, uchrashuvlar, savdo va avtomatlashtirishni yagona AI agentlar qatlamida birlashtiradi."
        },
        {
            'type': 'home',
            'lang': 'ru',
            'rel_path': os.path.join('ru', 'index.html'),
            'canonical': 'https://gptify.si/ru/',
            'title': "GPTify OS — AI операционная система для сферы услуг | GPTify",
            'desc': "GPTify OS — это AI операционная система для сферы услуг, объединяющая коммуникации с клиентами, CRM, планирование, встречи, продажи и автоматизацию через единый слой ИИ-агентов."
        }
    ]

    for p in pages:
        lang = p['lang']
        is_arch = False
        
        # Assemble HTML structure
        head_html = get_head_html(p['title'], p['desc'], p['canonical'], lang, is_arch=False)
        nav_html = get_nav_html(lang, is_arch=False)
        body_html = get_homepage_body(lang)
        footer_html = get_footer_html(lang)
        modal_html = get_modal_html(lang)
        scripts_html = get_scripts_html(lang)

        raw_page = head_html + nav_html + body_html + footer_html + modal_html + scripts_html
        soup = BeautifulSoup(raw_page, 'html.parser')

        # Translate all elements with data-t attribute
        lang_dict = TRANSLATIONS.get(lang, {})
        for el in soup.find_all(attrs={'data-t': True}):
            key = el['data-t']
            if key in lang_dict:
                val = lang_dict[key]
                frag = BeautifulSoup(val, 'html.parser')
                el.clear()
                for child in list(frag.contents):
                    el.append(child)

        # Write output file
        target_path = os.path.join(BASE_DIR, p['rel_path'])
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Generated {p['rel_path']} ({len(str(soup))} bytes)")

    # Update Sitemap XML
    sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://gptify.si/</loc>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://gptify.si/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://gptify.si/"/>
    <xhtml:link rel="alternate" hreflang="uz" href="https://gptify.si/uz/"/>
    <xhtml:link rel="alternate" hreflang="ru" href="https://gptify.si/ru/"/>
    <lastmod>2026-11-15</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://gptify.si/uz/</loc>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://gptify.si/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://gptify.si/"/>
    <xhtml:link rel="alternate" hreflang="uz" href="https://gptify.si/uz/"/>
    <xhtml:link rel="alternate" hreflang="ru" href="https://gptify.si/ru/"/>
    <lastmod>2026-11-15</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://gptify.si/ru/</loc>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://gptify.si/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://gptify.si/"/>
    <xhtml:link rel="alternate" hreflang="uz" href="https://gptify.si/uz/"/>
    <xhtml:link rel="alternate" hreflang="ru" href="https://gptify.si/ru/"/>
    <lastmod>2026-11-15</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://gptify.si/privacy.html</loc>
    <lastmod>2026-11-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://gptify.si/terms.html</loc>
    <lastmod>2026-11-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>'''

    with open(os.path.join(BASE_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    print("Generated sitemap.xml")

if __name__ == '__main__':
    build_all_pages()
