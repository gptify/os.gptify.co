# -*- coding: utf-8 -*-
"""
Builder script to generate deploy_os/index.html and deploy_os/architecture.html with:
- Streamlined 6-section buyer-focused homepage (under 6,500px @ 1280px, under 11,000px @ 375px)
- The 5-Product Family: Ailo, ILDAM, Bandla, Mirzo, Izlai (with embedded flywheel handoffs)
- The 4 Packaged Industry Solutions (Clinics, Education, Automotive, Professional Services)
- Interactive Loss/ROI Calculator
- Dedicated /architecture.html for Enterprise Cloud & AI Foundation + API samples
- Unified button naming: "Book a Demo" with context-tracking hidden input
- Plain-language buyer copy (EN, UZ, RU)
- Strict UI requirements: 14px+ body, 12px+ mono, 16px inputs, 44px tap targets, 28px slider thumb
- Prefers-reduced-motion media query
- Trilingual support across /, /uz/, /ru/
"""

import os
import json
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load translations
TRANS_PATH = os.path.join(BASE_DIR, 'translations.json')
with open(TRANS_PATH, 'r', encoding='utf-8') as f:
    TRANSLATIONS = json.load(f)

# Ensure all new plain-language keys are populated
NEW_PLAIN_KEYS = {
    'en': {
        'navEngines': '5 Engines',
        'navSolutions': 'Solutions',
        'navArchitecture': 'Architecture',
        'navCalculator': 'Calculator',
        'navFaq': 'FAQ',
        'navBook': 'Book a Demo',
        'btnBookDemo': 'Book a Demo',
        'telemetryTitle': 'What happened today',
        'pillarsEyebrow': 'Core System',
        'pillarsTitle': '5 Core Tools to Run Your Business',
        'pillarsSub': 'Use individual tools or connect them together into one seamless workflow.',
        'solutionsEyebrow': 'Ready-made setups for your industry',
        'solutionsTitle': 'Tailored for Your Exact Daily Workflow',
        'solutionsSub': 'Pre-built configurations designed for how your business communicates, books, and gets paid.',
        'sol1Tag': 'For clinics & healthcare',
        'sol2Tag': 'For academies & schools',
        'sol3Tag': 'For auto services & workshops',
        'sol4Tag': 'For consulting & advisory firms',
        'calcTitle': 'How much time and money could you get back?',
        'calcSub': 'Adjust team size and average hourly rates to see your estimated savings with automated triage and scheduling.',
        'calcResLabel': 'Estimated yearly savings',
        'ctaHowWeStart': 'How we start: 1. Process Audit → 2. Quick Setup & Integration → 3. Live in 14 Days',
        'ctaTitle': 'Put your customer communication and bookings on autopilot',
        'ctaSub': 'During this 30-minute session, we map where your business is losing hours and revenue, delivering a pragmatic action plan with zero sales pressure.',
        'ailoHandoff': '↳ Syncs leads to ILDAM & reserves slots via Bandla',
        'ildamHandoff': '↳ Triggers bookings in Bandla & briefs Mirzo for calls',
        'bandlaHandoff': '↳ Prepares meeting agenda for Mirzo & syncs with 1C',
        'mirzoHandoff': '↳ Updates deal stages & action items back into ILDAM',
        'izlaiHandoff': '↳ Hands warm interested leads directly to Ailo & ILDAM',
        'pricingSlot': 'Starting from $___ / month',
        'archPageTitle': 'Enterprise Cloud & AI Foundation',
        'archPageSub': 'Built on multi-model LLM routing, isolated tenant data boundaries, and event-driven webhooks for scale and enterprise compliance.',
        'archHeroH1': 'Engineered for High-Throughput Inference, Zero Data Leakage, and Seamless Scale.'
    },
    'uz': {
        'navEngines': '5 Tizim',
        'navSolutions': 'Yechimlar',
        'navArchitecture': 'Arxitektura',
        'navCalculator': 'Kalkulyator',
        'navFaq': 'FAQ',
        'navBook': 'Demoni band qilish',
        'btnBookDemo': 'Demoni band qilish',
        'telemetryTitle': 'Bugun nimalar bajarildi',
        'pillarsEyebrow': 'Asosiy tizim',
        'pillarsTitle': 'Biznesingizni boshqaruvchi 5 ta asosiy vosita',
        'pillarsSub': 'Alohida vositalardan foydalaning yoki ularni yagona uzluksiz tizimga birlashtiring.',
        'solutionsEyebrow': 'Sohangiz uchun tayyor yechimlar',
        'solutionsTitle': 'Kundalik ish jarayoningizga to\'liq moslashtirilgan',
        'solutionsSub': 'Sizning sohangizdagi real muloqot, yozilishlar va to\'lov jarayonlari uchun oldindan sozlangan tizimlar.',
        'sol1Tag': 'Klinikalar va tibbiyot markazlari uchun',
        'sol2Tag': 'O\'quv markazlari va maktablar uchun',
        'sol3Tag': 'Avtoservis va ustaxonalar uchun',
        'sol4Tag': 'Konsalting va professional xizmatlar uchun',
        'calcTitle': 'Qancha vaqt va mablag\'ni tejab qolishingiz mumkin?',
        'calcSub': 'Xodimlar soni va soatlik xarajatlarni belgilab, avtomatlashtirish orqali tejaladigan yillik mablag\'ni hisoblang.',
        'calcResLabel': 'Taxminiy yillik tejamkorlik',
        'ctaHowWeStart': 'Ishni qanday boshlaymiz: 1. Jarayonlarni tahlil qilish → 2. Tezkor sozlash va ulash → 3. 14 kunda ishga tushirish',
        'ctaTitle': 'Mijozlar bilan muloqot va yozilishlarni avtopilotga qo\'ying',
        'ctaSub': '30 daqiqalik audit davomida biznesingiz qayerda vaqt va daromad yo\'qotayotganini aniqlab, amaliy harakat rejasini taqdim etamiz.',
        'btnBookDemo': 'Demoni band qilish',
        'ailoHandoff': '↳ Lid ma\'lumotlarini ILDAM ga uzatadi va Bandla orqali joy band qiladi',
        'ildamHandoff': '↳ Bandla orqali uchrashuv belgilaydi va Mirzo ga brif tayyorlaydi',
        'bandlaHandoff': '↳ Mirzo uchun kun tartibini tayyorlaydi va 1C ga sinxronlaydi',
        'mirzoHandoff': '↳ Uchrashuv qarorlari va vazifalarini ILDAM CRM ga kiritadi',
        'izlaiHandoff': '↳ Qiziqish bildirgan issiq mijozlarni Ailo va ILDAM ga topshiradi',
        'pricingSlot': 'Oyiga $___ dan boshlab',
        'archPageTitle': 'Bulutli Arxitektura va Korporativ AI Poydevori',
        'archPageSub': 'Ko\'p modelli LLM marshrutlash, izolyatsiyalangan ma\'lumotlar chegaralari va hodisalarga asoslangan veb-huklar.',
        'archHeroH1': 'Yuqori tezlikdagi xulosa chiqarish, nol ma\'lumotlar sizib chiqishi va uzluksiz masshtablash uchun ishlab chiqilgan.'
    },
    'ru': {
        'navEngines': '5 Движков',
        'navSolutions': 'Решения',
        'navArchitecture': 'Архитектура',
        'navCalculator': 'Калькулятор',
        'navFaq': 'FAQ',
        'navBook': 'Записаться на демо',
        'btnBookDemo': 'Записаться на демо',
        'telemetryTitle': 'Что произошло за сегодня',
        'pillarsEyebrow': 'Основная система',
        'pillarsTitle': '5 основных инструментов для управления бизнесом',
        'pillarsSub': 'Используйте отдельные инструменты или объедините их в единую рабочую систему.',
        'solutionsEyebrow': 'Готовые решения для вашей сферы',
        'solutionsTitle': 'Адаптировано под ваши ежедневные процессы',
        'solutionsSub': 'Готовые конфигурации, настроенные под реальную коммуникацию, запись клиентов и учет оплат в вашей сфере.',
        'sol1Tag': 'Для клиник и медицинских центров',
        'sol2Tag': 'Для учебных центров и школ',
        'sol3Tag': 'Для автосервисов и мастерских',
        'sol4Tag': 'Для консалтинга и сервисных компаний',
        'calcTitle': 'Сколько времени и денег вы сможете сэкономить?',
        'calcSub': 'Укажите размер команды и почасовую ставку, чтобы рассчитать примерную годовую экономию от автоматизации.',
        'calcResLabel': 'Оценочная годовая экономия',
        'ctaHowWeStart': 'Как мы начинаем: 1. Аудит процессов → 2. Быстрая настройка и интеграция → 3. Запуск за 14 дней',
        'ctaTitle': 'Переведите общение с клиентами и бронирование на автопилот',
        'ctaSub': 'За 30 минут аудита мы разберем, где ваш бизнес теряет время и заявки, и подготовим четкий план действий без навязчивых продаж.',
        'btnBookDemo': 'Записаться на демо',
        'ailoHandoff': '↳ Передает лидов в ILDAM и бронирует слоты через Bandla',
        'ildamHandoff': '↳ Запускает бронь в Bandla и готовит бриф для Mirzo',
        'bandlaHandoff': '↳ Передает детали встречи в Mirzo и синхронизирует с 1C',
        'mirzoHandoff': '↳ Обновляет этапы сделки и задачи в ILDAM CRM',
        'izlaiHandoff': '↳ Передает заинтересованных клиентов сразу в Ailo и ILDAM',
        'pricingSlot': 'От $___ в месяц',
        'archPageTitle': 'Облачная Архитектура и Корпоративный AI',
        'archPageSub': 'Маршрутизация мультимодельных LLM, изолированные границы клиентских данных и масштабируемые вебхуки.',
        'archHeroH1': 'Спроектировано для высокой скорости, защиты от утечек данных и надежного масштабирования.'
    }
}

for lang in ['en', 'uz', 'ru']:
    TRANSLATIONS[lang].update(NEW_PLAIN_KEYS[lang])

with open(TRANS_PATH, 'w', encoding='utf-8') as f:
    json.dump(TRANSLATIONS, f, ensure_ascii=False, indent=2)

print("Translations refreshed and saved to deploy_os/translations.json")

# Import and execute generator to rebuild all pages and sitemap
import generator
generator.build_all_pages()
print("All pages successfully built by build_page.py!")
