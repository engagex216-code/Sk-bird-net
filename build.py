import re
import urllib.parse

WHATSAPP_NUMBER = "918878020513"

def wa_link(message):
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(message)}"

WA_GENERIC = wa_link("Hi SK Bird Net, I'd like a free quote.")

HERO_URI = "assets/hero-balcony.jpg"
BIRD_NETTING_URI = "assets/bird-netting-service.jpg"
CHILD_SAFETY_URI = "assets/child-safety-net.jpg"
SPORT_NET_URI = "assets/sport-net.jpg"
BALCONY_NET_URI = "assets/balcony-netting.jpg"
RESIDENTIAL_URI = "assets/residential-bird-net.jpg"
INVISIBLE_GRILL_URI = "assets/invisible-grill.jpg"
BAMBOO_CHICK_URI = "assets/bamboo-chick.jpg"
FEEDBACK_PHOTO_URI = "assets/feedback-photo.jpg"
FEEDBACK_VIDEO1_URI = "assets/feedback-video1.mp4"
FEEDBACK_VIDEO2_URI = "assets/feedback-video2.mp4"

with open('/home/claude/lucide.min.js') as f:
    LUCIDE_JS = f.read()

HEAD = """<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="manifest" href="site.webmanifest">
<meta name="theme-color" content="#12233F">
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<script>__LUCIDE_JS__</script>
<style>
  :root{{ --navy:#12233F; --blue:#1E3A8A; --orange:#F97316; --sky:#2E6FB8; }}
  body{{ font-family:'Poppins',sans-serif; color:#1f2937; }}
  .carousel-track{{ display:flex; gap:16px; overflow-x:auto; scroll-behavior:smooth; scrollbar-width:none; }}
  .carousel-track::-webkit-scrollbar{{ display:none; }}
  .wa-float{{ bottom: calc(1.25rem + env(safe-area-inset-bottom)); }}
  @media (max-width: 640px){{
    .wa-float{{ padding: 0.9rem; right: 1rem; }}
  }}
</style>
"""

def header(active):
    def link(label, href, id_):
        cls = "text-[var(--orange)]" if active == id_ else "hover:text-[var(--orange)]"
        return f'<a href="{href}" class="{cls} block py-2">{label}</a>'
    return f"""<header class="w-full border-b border-gray-100 sticky top-0 bg-white z-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 h-16 md:h-20 flex items-center justify-between">
    <a href="index.html" class="flex items-center gap-2">
      <svg width="30" height="30" viewBox="0 0 34 34" fill="none" class="md:w-[34px] md:h-[34px]">
        <path d="M5 25C5 25 10 15 17 15C24 15 29 25 29 25" stroke="var(--blue)" stroke-width="2"/>
        <circle cx="17" cy="9" r="4" fill="var(--orange)"/>
        <path d="M10 25H24" stroke="var(--blue)" stroke-width="2"/>
      </svg>
      <div class="leading-tight">
        <p class="font-extrabold text-[var(--navy)] text-base md:text-lg tracking-tight">SK BIRD NET</p>
        <p class="text-[9px] md:text-[10px] tracking-[0.2em] text-gray-500 font-medium -mt-1">SOLUTIONS</p>
      </div>
    </a>
    <nav class="hidden md:flex items-center gap-7 text-sm font-semibold text-[var(--navy)]">
      {link('Home','index.html','home')}
      {link('Services','services.html','services')}
      {link('About Us','about.html','about')}
      {link('Contact Us','contact.html','contact')}
    </nav>
    <div class="hidden md:flex items-center gap-3">
      <a href="{WA_GENERIC}" target="_blank" rel="noopener" class="flex items-center gap-2 bg-[#25D366] text-white text-sm font-semibold px-5 py-2.5 rounded-md hover:brightness-95">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.46 1.32 4.96L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm0 18.15c-1.53 0-3.03-.41-4.34-1.19l-.31-.18-3.11.82.83-3.04-.2-.31a8.2 8.2 0 01-1.26-4.34c0-4.54 3.7-8.23 8.24-8.23 2.2 0 4.27.86 5.83 2.41a8.18 8.18 0 012.41 5.83c0 4.54-3.7 8.23-8.24 8.23z"/></svg>
        Chat on WhatsApp
      </a>
    </div>
    <div class="flex items-center gap-2 md:hidden">
      <a href="{WA_GENERIC}" target="_blank" rel="noopener"
         class="flex items-center gap-1.5 bg-[#25D366] text-white text-xs font-semibold px-3 py-2 rounded-md">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.46 1.32 4.96L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm0 18.15c-1.53 0-3.03-.41-4.34-1.19l-.31-.18-3.11.82.83-3.04-.2-.31a8.2 8.2 0 01-1.26-4.34c0-4.54 3.7-8.23 8.24-8.23 2.2 0 4.27.86 5.83 2.41a8.18 8.18 0 012.41 5.83c0 4.54-3.7 8.23-8.24 8.23z"/></svg>
        Chat
      </a>
      <button id="menuBtn" aria-label="Open menu" class="p-2 -mr-2 text-[var(--navy)]">
        <i data-lucide="menu" class="w-6 h-6"></i>
      </button>
    </div>
  </div>
  <div id="mobileMenu" class="hidden md:hidden border-t border-gray-100 px-6 py-4 bg-white">
    <nav class="flex flex-col text-sm font-semibold text-[var(--navy)] divide-y divide-gray-100">
      {link('Home','index.html','home')}
      {link('Services','services.html','services')}
      {link('About Us','about.html','about')}
      {link('Contact Us','contact.html','contact')}
    </nav>
    <a href="{WA_GENERIC}" target="_blank" rel="noopener" class="mt-3 flex items-center justify-center gap-2 bg-[#25D366] text-white text-sm font-semibold px-5 py-2.5 rounded-md hover:brightness-95">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.46 1.32 4.96L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm0 18.15c-1.53 0-3.03-.41-4.34-1.19l-.31-.18-3.11.82.83-3.04-.2-.31a8.2 8.2 0 01-1.26-4.34c0-4.54 3.7-8.23 8.24-8.23 2.2 0 4.27.86 5.83 2.41a8.18 8.18 0 012.41 5.83c0 4.54-3.7 8.23-8.24 8.23z"/></svg>
      Chat on WhatsApp
    </a>
  </div>
</header>"""

STATS = """<section class="bg-[var(--navy)] py-12">
  <div class="max-w-7xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-8 text-center text-white">
    <div>
      <p class="counter text-3xl md:text-4xl font-extrabold text-[var(--orange)]" data-target="2400">0</p>
      <p class="text-xs md:text-sm text-gray-300 mt-1 tracking-wide">Nets Installed</p>
    </div>
    <div>
      <p class="counter text-3xl md:text-4xl font-extrabold text-[var(--orange)]" data-target="1800">0</p>
      <p class="text-xs md:text-sm text-gray-300 mt-1 tracking-wide">Happy Customers</p>
    </div>
    <div>
      <p class="counter text-3xl md:text-4xl font-extrabold text-[var(--orange)]" data-target="10">0</p>
      <p class="text-xs md:text-sm text-gray-300 mt-1 tracking-wide">Years Experience</p>
    </div>
    <div>
      <p class="counter text-3xl md:text-4xl font-extrabold text-[var(--orange)]" data-target="15">0</p>
      <p class="text-xs md:text-sm text-gray-300 mt-1 tracking-wide">Cities Served</p>
    </div>
  </div>
</section>"""

def footer():
    return f"""<footer id="contact-footer" class="bg-[var(--navy)] text-gray-300 mt-6">
  <div class="max-w-7xl mx-auto px-6 py-12 grid md:grid-cols-3 gap-10">
    <div>
      <p class="font-extrabold text-white text-lg mb-3">SK BIRD NET</p>
      <ul class="space-y-2 text-sm">
        <li class="flex items-start gap-2"><i data-lucide="map-pin" class="w-4 h-4 mt-0.5"></i>Sector 3A, Ashok Vihar Phase-1, Gurugram, Haryana 122006</li>
        <li class="flex items-center gap-2"><i data-lucide="phone" class="w-4 h-4"></i>+91 88780 20513</li>
        <li class="flex items-center gap-2"><i data-lucide="mail" class="w-4 h-4"></i>info@skbirdnet.com</li>
      </ul>
      <div class="flex gap-3 mt-4">
        <i data-lucide="facebook" class="w-4 h-4"></i>
        <i data-lucide="instagram" class="w-4 h-4"></i>
        <i data-lucide="linkedin" class="w-4 h-4"></i>
        <i data-lucide="youtube" class="w-4 h-4"></i>
      </div>
    </div>
    <div>
      <p class="text-white font-semibold mb-3 text-sm">Company Info</p>
      <ul class="space-y-2 text-sm">
        <li><a href="about.html" class="hover:text-white">About Us</a></li>
        <li><a href="services.html" class="hover:text-white">Services</a></li>
        <li><a href="contact.html" class="hover:text-white">Contact Us</a></li>
      </ul>
    </div>
    <div class="bg-white text-gray-800 rounded-xl p-5 text-center">
      <p class="font-bold text-[var(--navy)] mb-1 text-sm">Ready to get started?</p>
      <p class="text-xs text-gray-500 mb-4">Skip the form — message us directly and we'll reply fast.</p>
      <a href="{WA_GENERIC}" target="_blank" rel="noopener" class="flex items-center justify-center gap-2 w-full bg-[#25D366] text-white text-sm font-semibold py-3 rounded-md hover:brightness-95">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.46 1.32 4.96L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm0 18.15c-1.53 0-3.03-.41-4.34-1.19l-.31-.18-3.11.82.83-3.04-.2-.31a8.2 8.2 0 01-1.26-4.34c0-4.54 3.7-8.23 8.24-8.23 2.2 0 4.27.86 5.83 2.41a8.18 8.18 0 012.41 5.83c0 4.54-3.7 8.23-8.24 8.23z"/></svg>
        Chat on WhatsApp
      </a>
    </div>
  </div>
  <div class="border-t border-white/10 py-4 text-center text-xs">© 2026 SK Bird Net Solutions. All rights reserved.</div>
</footer>"""

SCRIPT = """<script>
  lucide.createIcons();
  const counters = document.querySelectorAll('.counter');
  const animateCounter = (el) => {
    const target = parseInt(el.getAttribute('data-target'), 10);
    const duration = 1500;
    const startTime = performance.now();
    const step = (now) => {
      const progress = Math.min((now - startTime) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.floor(eased * target).toLocaleString() + (progress >= 1 ? '+' : '');
      if (progress < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) { animateCounter(entry.target); counterObserver.unobserve(entry.target); }
    });
  }, { threshold: 0.4 });
  counters.forEach(c => counterObserver.observe(c));

  const menuBtn = document.getElementById('menuBtn');
  const mobileMenu = document.getElementById('mobileMenu');
  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', () => {
      const isOpen = !mobileMenu.classList.contains('hidden');
      mobileMenu.classList.toggle('hidden');
      menuBtn.innerHTML = isOpen ? '<i data-lucide="menu" class="w-6 h-6"></i>' : '<i data-lucide="x" class="w-6 h-6"></i>';
      lucide.createIcons();
    });
    mobileMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
      mobileMenu.classList.add('hidden');
      menuBtn.innerHTML = '<i data-lucide="menu" class="w-6 h-6"></i>';
      lucide.createIcons();
    }));
  }
</script>"""

WHATSAPP = """<a href="https://wa.me/918878020513?text=Hi%20SK%20Bird%20Net%2C%20I%27d%20like%20a%20free%20quote."
   target="_blank" rel="noopener" aria-label="Chat on WhatsApp"
   class="wa-float fixed z-[60] bottom-5 right-5 flex items-center gap-2 bg-[#25D366] text-white font-semibold rounded-full shadow-lg px-4 py-3 hover:brightness-95 active:scale-95 transition">
  <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" class="shrink-0">
    <path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.08-.3-.15-1.25-.46-2.38-1.47-.88-.79-1.47-1.75-1.64-2.05-.17-.3-.02-.46.13-.6.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.6-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.47s1.06 2.87 1.21 3.07c.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.69.63.71.22 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.28.17-1.41-.07-.13-.27-.2-.57-.35z"/>
    <path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.46 1.32 4.96L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm0 18.15c-1.53 0-3.03-.41-4.34-1.19l-.31-.18-3.11.82.83-3.04-.2-.31a8.2 8.2 0 01-1.26-4.34c0-4.54 3.7-8.23 8.24-8.23 2.2 0 4.27.86 5.83 2.41a8.18 8.18 0 012.41 5.83c0 4.54-3.7 8.23-8.24 8.23z"/>
  </svg>
  <span class="wa-label hidden sm:inline text-sm">WhatsApp</span>
</a>"""

def page(title, active, body):
    head_filled = HEAD.format(title=title).replace('__LUCIDE_JS__', LUCIDE_JS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head_filled}
</head>
<body class="bg-white">
{header(active)}
{body}
{footer()}
{WHATSAPP}
{SCRIPT}
</body>
</html>"""

SERVICES = [
    ("Bird Netting Service", "Effective pigeon control with durable, UV-resistant bird nets for balconies, windows, and rooftops.", BIRD_NETTING_URI, "shield", "bird-netting-service"),
    ("Child Safety Net", "Designed to prevent accidental falls from high-rise balconies and staircases, especially for children.", CHILD_SAFETY_URI, "baby", "child-safety-net"),
    ("Sport Net Installation", "Custom nets for cricket, football, and badminton practice areas. Durable and weather-resistant solutions.", SPORT_NET_URI, "trophy", "sport-net-installation"),
    ("Balcony Netting", "Protect open spaces from birds without blocking air or light. Ideal for apartment balconies in metro cities.", BALCONY_NET_URI, "wind", "balcony-netting"),
    ("Residential Bird Net", "Discreet and long-lasting netting systems to keep birds away from your windows and air conditioning units.", RESIDENTIAL_URI, "home", "residential-bird-net"),
    ("Invisible Grill Installation", "Modern safety solution that offers protection without obstructing your view.", INVISIBLE_GRILL_URI, "scan", "invisible-grill-installation"),
    ("Bamboo Chick", "Natural bamboo chick blinds for balconies and verandas — cuts heat and glare while keeping airflow and privacy.", BAMBOO_CHICK_URI, "blinds", "bamboo-chick"),
]

# ---------------- INDEX ----------------
service_picker_items = ""
for name, desc, img, icon, slug in SERVICES:
    service_picker_items += f"""
    <a href="services.html#{slug}" class="group flex items-center gap-3 border border-gray-200 rounded-lg px-4 py-3.5 hover:border-[var(--orange)] hover:bg-orange-50 transition">
      <span class="flex items-center justify-center w-10 h-10 rounded-full bg-[var(--navy)]/5 text-[var(--blue)] group-hover:bg-[var(--orange)] group-hover:text-white transition shrink-0">
        <i data-lucide="{icon}" class="w-5 h-5"></i>
      </span>
      <span class="text-sm font-semibold text-[var(--navy)]">{name}</span>
      <i data-lucide="chevron-right" class="w-4 h-4 text-gray-400 ml-auto group-hover:text-[var(--orange)] transition"></i>
    </a>"""

index_body = f"""
<!-- Hero -->
<section class="relative w-full">
  <img src="{HERO_URI}" class="w-full h-[300px] sm:h-[380px] md:h-[520px] object-cover" alt="Balcony bird netting">
  <div class="absolute inset-0 bg-gradient-to-r from-[var(--navy)]/80 via-[var(--navy)]/35 to-transparent"></div>
  <div class="absolute inset-0 flex items-center">
    <div class="max-w-7xl w-full mx-auto px-6">
      <div class="max-w-lg text-white">
        <h1 class="text-2xl sm:text-3xl md:text-5xl font-extrabold leading-tight mb-4">SAY GOODBYE TO<br>PIGEON PROBLEMS.</h1>
        <p class="text-sm md:text-base text-gray-200 mb-6">Expert, Durable &amp; Aesthetic Bird Netting Solutions for Homes &amp; Businesses.</p>
        <a href="{WA_GENERIC}" target="_blank" rel="noopener" class="inline-block bg-[var(--orange)] text-white text-sm font-semibold px-6 py-3 rounded-md hover:brightness-95">Get a Free Consultation</a>
      </div>
    </div>
  </div>
</section>

<!-- Service Picker -->
<section id="services" class="max-w-3xl mx-auto px-6 pt-14 pb-10">
  <div class="border border-gray-200 rounded-2xl shadow-sm p-6 md:p-8 bg-white">
    <div class="text-center mb-6">
      <p class="text-[var(--orange)] text-sm font-bold tracking-widest mb-2">WHAT DO YOU NEED?</p>
      <h2 class="text-xl md:text-2xl font-extrabold text-[var(--navy)]">Choose Your Service</h2>
      <p class="text-xs text-gray-500 mt-2">Pick what you need protection for — we'll take you straight to the details.</p>
    </div>
    <div class="grid sm:grid-cols-2 gap-3">
      {service_picker_items}
    </div>
  </div>
</section>

{STATS}

<!-- Why choose us + testimonials -->
<section class="max-w-7xl mx-auto px-6 py-14 grid md:grid-cols-2 gap-10 items-start">
  <div>
    <h2 class="text-xl font-extrabold text-[var(--navy)] mb-4">WHY CHOOSE SK BIRD NET?</h2>
    <ul class="space-y-2 mb-8 text-sm text-gray-700 font-medium">
      <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-green-600"></i>Quality Nets</li>
      <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-green-600"></i>Expert Installation</li>
      <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-green-600"></i>10-Year Warranty</li>
      <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-green-600"></i>Affordable Pricing</li>
    </ul>
    <div class="grid grid-cols-2 gap-6">
      <div>
        <div class="flex items-center gap-2 mb-2">
          <div class="w-9 h-9 rounded-full bg-[var(--blue)] text-white flex items-center justify-center text-xs font-bold">RS</div>
          <div class="flex text-[var(--orange)] text-xs">★★★★★</div>
        </div>
        <p class="text-xs text-gray-600 italic mb-1">"Transformed my balcony!"</p>
        <p class="text-xs font-semibold text-[var(--navy)]">Rohit Sharma</p>
      </div>
      <div>
        <div class="flex items-center gap-2 mb-2">
          <div class="w-9 h-9 rounded-full bg-[var(--orange)] text-white flex items-center justify-center text-xs font-bold">PN</div>
          <div class="flex text-[var(--orange)] text-xs">★★★★★</div>
        </div>
        <p class="text-xs text-gray-600 italic mb-1">"Professional team!"</p>
        <p class="text-xs font-semibold text-[var(--navy)]">Priya Nair</p>
      </div>
    </div>
  </div>
  <div class="rounded-xl overflow-hidden">
    <img src="{RESIDENTIAL_URI}" class="w-full h-72 object-cover" alt="Installer fitting bird net">
  </div>
</section>

<!-- Customer Feedback -->
<section id="feedback" class="bg-gray-50 py-14 border-y border-gray-100">
  <div class="max-w-7xl mx-auto px-6">
    <h2 class="text-center text-lg font-extrabold text-[var(--navy)] tracking-wide mb-8">CUSTOMER FEEDBACK</h2>
    <div class="grid md:grid-cols-3 gap-6">
      <div class="bg-white rounded-xl overflow-hidden shadow-sm border border-gray-100">
        <img src="{FEEDBACK_PHOTO_URI}" class="w-full h-56 object-cover" alt="Industrial bird netting installation feedback">
        <div class="p-4">
          <p class="text-xs text-gray-600 italic">"Clean install, finished on time — exactly what we needed for the loading bay."</p>
          <p class="text-xs font-semibold text-[var(--navy)] mt-2">Facility Manager, Industrial Client</p>
        </div>
      </div>
      <div class="bg-white rounded-xl overflow-hidden shadow-sm border border-gray-100">
        <video controls playsinline class="w-full h-56 object-cover bg-black">
          <source src="{FEEDBACK_VIDEO1_URI}" type="video/mp4">
        </video>
        <div class="p-4">
          <p class="text-xs text-gray-600 italic">"Watch what our customer had to say right after installation."</p>
          <p class="text-xs font-semibold text-[var(--navy)] mt-2">Verified Customer</p>
        </div>
      </div>
      <div class="bg-white rounded-xl overflow-hidden shadow-sm border border-gray-100">
        <video controls playsinline class="w-full h-56 object-cover bg-black">
          <source src="{FEEDBACK_VIDEO2_URI}" type="video/mp4">
        </video>
        <div class="p-4">
          <p class="text-xs text-gray-600 italic">"Another happy customer sharing their experience with SK Bird Net."</p>
          <p class="text-xs font-semibold text-[var(--navy)] mt-2">Verified Customer</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Gallery -->
<section id="gallery" class="max-w-7xl mx-auto px-6 py-10">
  <h2 class="text-center text-lg font-extrabold text-[var(--navy)] tracking-wide mb-6">OUR WORK GALLERY</h2>
  <div class="relative">
    <div class="carousel-track" id="galleryTrack">
      <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=500&auto=format&fit=crop" class="w-64 h-40 object-cover rounded-lg shrink-0" alt="Gallery 1">
      <img src="https://images.unsplash.com/photo-1560184897-ae75f418493e?q=80&w=500&auto=format&fit=crop" class="w-64 h-40 object-cover rounded-lg shrink-0" alt="Gallery 2">
      <img src="https://images.unsplash.com/photo-1580128637416-64e5f0a2f9b6?q=80&w=500&auto=format&fit=crop" class="w-64 h-40 object-cover rounded-lg shrink-0" alt="Gallery 3">
      <img src="https://images.unsplash.com/photo-1613977257363-707ba9348227?q=80&w=500&auto=format&fit=crop" class="w-64 h-40 object-cover rounded-lg shrink-0" alt="Gallery 4">
    </div>
    <button onclick="document.getElementById('galleryTrack').scrollBy({{left:-280,behavior:'smooth'}})" class="hidden md:flex items-center justify-center absolute -left-4 top-1/2 -translate-y-1/2 w-9 h-9 bg-white rounded-full shadow"><i data-lucide="chevron-left" class="w-4 h-4"></i></button>
    <button onclick="document.getElementById('galleryTrack').scrollBy({{left:280,behavior:'smooth'}})" class="hidden md:flex items-center justify-center absolute -right-4 top-1/2 -translate-y-1/2 w-9 h-9 bg-white rounded-full shadow"><i data-lucide="chevron-right" class="w-4 h-4"></i></button>
  </div>
</section>
"""

with open('/mnt/user-data/outputs/index.html','w') as f:
    f.write(page("SK Bird Net | Bird Netting Solutions for Homes & Businesses", "home", index_body))

# ---------------- SERVICES PAGE ----------------
service_blocks = ""
for i, (name, desc, img, icon, slug) in enumerate(SERVICES):
    reverse = "md:flex-row-reverse" if i % 2 else ""
    wa_service_link = wa_link(f"Hey SK Bird Net, I want to discuss about {name}.")
    service_blocks += f"""
  <div id="{slug}" class="scroll-mt-24 flex flex-col {reverse} md:flex-row items-center gap-8 py-10 border-b border-gray-100 last:border-0">
    <img src="{img}" class="w-full md:w-1/2 h-64 object-cover rounded-xl" alt="{name}">
    <div class="md:w-1/2">
      <i data-lucide="{icon}" class="w-8 h-8 text-[var(--orange)] mb-3"></i>
      <h3 class="text-xl font-extrabold text-[var(--navy)] mb-3">{name}</h3>
      <p class="text-sm text-gray-600 leading-relaxed mb-4">{desc}</p>
      <a href="{wa_service_link}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 bg-[#25D366] text-white text-sm font-semibold px-5 py-2.5 rounded-md hover:brightness-95">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.46 1.32 4.96L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm0 18.15c-1.53 0-3.03-.41-4.34-1.19l-.31-.18-3.11.82.83-3.04-.2-.31a8.2 8.2 0 01-1.26-4.34c0-4.54 3.7-8.23 8.24-8.23 2.2 0 4.27.86 5.83 2.41a8.18 8.18 0 012.41 5.83c0 4.54-3.7 8.23-8.24 8.23z"/></svg>
        Discuss on WhatsApp
      </a>
    </div>
  </div>"""

services_body = f"""
<section class="bg-[var(--navy)] py-16 text-center text-white">
  <p class="text-[var(--orange)] text-sm font-bold tracking-widest mb-2">SERVICES</p>
  <h1 class="text-3xl md:text-4xl font-extrabold">Our Main Services</h1>
  <p class="text-sm text-gray-300 mt-3 max-w-xl mx-auto">Complete netting and safety solutions for homes, offices, and sports facilities.</p>
</section>
<section class="max-w-5xl mx-auto px-6 py-4">
  {service_blocks}
</section>
{STATS}
"""
with open('/mnt/user-data/outputs/services.html','w') as f:
    f.write(page("Our Services | SK Bird Net", "services", services_body))

# ---------------- ABOUT PAGE ----------------
about_body = f"""
<section class="bg-[var(--navy)] py-16 text-center text-white">
  <p class="text-[var(--orange)] text-sm font-bold tracking-widest mb-2">ABOUT US</p>
  <h1 class="text-3xl md:text-4xl font-extrabold">Who We Are</h1>
</section>
<section class="max-w-5xl mx-auto px-6 py-14 grid md:grid-cols-2 gap-10 items-center">
  <img src="https://images.unsplash.com/photo-1621905251189-08b45d6a269e?q=80&w=900&auto=format&fit=crop" class="w-full h-80 object-cover rounded-xl" alt="SK Bird Net team">
  <div>
    <h2 class="text-2xl font-extrabold text-[var(--navy)] mb-4">Protecting Homes &amp; Businesses Across India</h2>
    <p class="text-sm text-gray-600 leading-relaxed mb-4">SK Bird Net has been installing durable, UV-resistant bird netting, child safety nets, sport nets, and invisible grills for homes and businesses across India. Every installation is handled by trained, certified crews and backed by a written warranty.</p>
    <p class="text-sm text-gray-600 leading-relaxed">From apartment balconies to commercial rooftops, our focus stays the same — clean installation, honest pricing, and netting that holds up for years.</p>
  </div>
</section>
{STATS}
<section class="max-w-5xl mx-auto px-6 py-14 grid sm:grid-cols-3 gap-6 text-center">
  <div>
    <i data-lucide="shield-check" class="w-8 h-8 text-[var(--orange)] mx-auto mb-3"></i>
    <p class="font-bold text-[var(--navy)] mb-1 text-sm">Quality First</p>
    <p class="text-xs text-gray-500">Only high-tensile, UV-resistant materials in every installation.</p>
  </div>
  <div>
    <i data-lucide="hard-hat" class="w-8 h-8 text-[var(--orange)] mx-auto mb-3"></i>
    <p class="font-bold text-[var(--navy)] mb-1 text-sm">Certified Installers</p>
    <p class="text-xs text-gray-500">Trained crews who install it right the first time.</p>
  </div>
  <div>
    <i data-lucide="receipt" class="w-8 h-8 text-[var(--orange)] mx-auto mb-3"></i>
    <p class="font-bold text-[var(--navy)] mb-1 text-sm">Transparent Pricing</p>
    <p class="text-xs text-gray-500">One quote, no hidden charges after the crew arrives.</p>
  </div>
</section>
"""
with open('/mnt/user-data/outputs/about.html','w') as f:
    f.write(page("About Us | SK Bird Net", "about", about_body))

# ---------------- CONTACT PAGE ----------------
contact_body = f"""
<section class="bg-[var(--navy)] py-16 text-center text-white">
  <p class="text-[var(--orange)] text-sm font-bold tracking-widest mb-2">CONTACT US</p>
  <h1 class="text-3xl md:text-4xl font-extrabold">Get In Touch</h1>
</section>
<section class="max-w-5xl mx-auto px-6 py-14 grid md:grid-cols-2 gap-10 items-center">
  <div class="border border-gray-200 rounded-2xl p-8 text-center shadow-sm">
    <div class="flex items-center justify-center w-16 h-16 rounded-full bg-[#25D366]/10 mx-auto mb-5">
      <svg width="30" height="30" viewBox="0 0 24 24" fill="#25D366"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.46 1.32 4.96L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm0 18.15c-1.53 0-3.03-.41-4.34-1.19l-.31-.18-3.11.82.83-3.04-.2-.31a8.2 8.2 0 01-1.26-4.34c0-4.54 3.7-8.23 8.24-8.23 2.2 0 4.27.86 5.83 2.41a8.18 8.18 0 012.41 5.83c0 4.54-3.7 8.23-8.24 8.23z"/></svg>
    </div>
    <h2 class="text-xl font-extrabold text-[var(--navy)] mb-2">Chat With Us on WhatsApp</h2>
    <p class="text-sm text-gray-500 mb-6">Skip the form — tell us what you need and we'll get back to you fast.</p>
    <a href="{WA_GENERIC}" target="_blank" rel="noopener" class="inline-flex items-center justify-center gap-2 w-full bg-[#25D366] text-white font-semibold py-3.5 rounded-md hover:brightness-95">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.46 1.32 4.96L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm0 18.15c-1.53 0-3.03-.41-4.34-1.19l-.31-.18-3.11.82.83-3.04-.2-.31a8.2 8.2 0 01-1.26-4.34c0-4.54 3.7-8.23 8.24-8.23 2.2 0 4.27.86 5.83 2.41a8.18 8.18 0 012.41 5.83c0 4.54-3.7 8.23-8.24 8.23z"/></svg>
      Chat on WhatsApp
    </a>
    <p class="text-xs text-gray-400 mt-3">+91 88780 20513</p>
  </div>
  <div class="space-y-4">
    <div class="flex items-start gap-3">
      <i data-lucide="map-pin" class="w-5 h-5 text-[var(--orange)] mt-0.5"></i>
      <p class="text-sm text-gray-600">Sector 3A, Ashok Vihar Phase-1, Gurugram, Haryana 122006</p>
    </div>
    <div class="flex items-start gap-3">
      <i data-lucide="phone" class="w-5 h-5 text-[var(--orange)] mt-0.5"></i>
      <p class="text-sm text-gray-600">+91 88780 20513</p>
    </div>
    <div class="flex items-start gap-3">
      <i data-lucide="mail" class="w-5 h-5 text-[var(--orange)] mt-0.5"></i>
      <p class="text-sm text-gray-600">info@skbirdnet.com</p>
    </div>
    <div class="flex items-start gap-3">
      <i data-lucide="clock" class="w-5 h-5 text-[var(--orange)] mt-0.5"></i>
      <p class="text-sm text-gray-600">Mon - Sat: 9:00 AM - 7:00 PM</p>
    </div>
    <img src="{FEEDBACK_PHOTO_URI}" class="w-full h-56 object-cover rounded-xl mt-4" alt="Service area">
  </div>
</section>
"""
with open('/mnt/user-data/outputs/contact.html','w') as f:
    f.write(page("Contact Us | SK Bird Net", "contact", contact_body))

print("done")
