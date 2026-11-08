import os

def get_head(title, active_page="home"):
    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | VISTRAL - UPVC Architectural Systems</title>
  <meta name="description" content="Precision crafted UPVC windows, sliding systems, and panoramic doors. European engineering, superior thermal insulation, and bespoke architectural glazing.">
  <link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
  
  <!-- Tailwind CSS Play CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            bronze: {{
              DEFAULT: '#B68B58',
              50: '#FBF8F3',
              100: '#F4ECE1',
              200: '#E7D5BF',
              300: '#D9BC9B',
              400: '#CAA477',
              500: '#B68B58',
              600: '#9E7443',
              700: '#7E5B32',
              800: '#5E4324',
              900: '#3F2C17',
            }},
            charcoal: {{
              DEFAULT: '#202A32',
              50: '#F2F4F6',
              100: '#E1E5EA',
              200: '#C0C8D1',
              300: '#9EABB8',
              400: '#5F7386',
              500: '#202A32',
              600: '#1A232A',
              700: '#141B21',
              800: '#0E1317',
              900: '#070A0C',
            }},
            ivory: {{
              DEFAULT: '#F7F6F1',
              50: '#FFFFFF',
              100: '#FBFBF9',
              200: '#F7F6F1',
              300: '#EBE9DD',
              400: '#DEDBC7',
            }},
            softgrey: '#DDE2E5'
          }},
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            display: ['"Space Grotesk"', 'sans-serif'],
          }}
        }}
      }}
    }}
  </script>
  
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  
  <!-- AOS CSS -->
  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>

  <!-- Custom Stylesheet -->
  <link rel="stylesheet" href="css/style.css">
</head>
<body class="bg-ivory dark:bg-[#12181F] text-charcoal dark:text-stone-100 transition-colors duration-300 min-h-screen flex flex-col font-sans">
"""

def get_header(active_page="home"):
    pages = [
        ("index.html", "Home 1", active_page == "home"),
        ("home-2.html", "Home 2", active_page == "home2"),
        ("about.html", "About Us", active_page == "about"),
        ("products.html", "Products", active_page == "products"),
        ("gallery.html", "Gallery", active_page == "gallery"),
        ("services.html", "Services", active_page == "services"),
        ("contact.html", "Contact Us", active_page == "contact"),
    ]
    
    nav_links = ""
    mobile_nav_links = ""
    for url, name, is_active in pages:
        active_class = "text-bronze font-bold active" if is_active else "text-charcoal/80 dark:text-stone-300 hover:text-bronze dark:hover:text-bronze"
        nav_links += f'<a href="{url}" class="nav-link text-xs xl:text-sm uppercase tracking-wider whitespace-nowrap transition-colors duration-200 {active_class}">{name}</a>\n'
        mobile_nav_links += f'<a href="{url}" class="block py-3 px-4 rounded-lg text-base font-medium {active_class} transition-colors">{name}</a>\n'

    return f"""
  <!-- Site Header -->
  <header class="fixed top-0 left-0 right-0 z-40 w-full glass-nav transition-shadow duration-200 py-3.5 px-4 sm:px-6 xl:px-8 border-b border-charcoal/10 dark:border-white/10 shadow-sm">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <!-- Brand Logo -->
      <a href="index.html" class="flex items-center space-x-2.5 sm:space-x-3 group rtl:space-x-reverse flex-shrink-0">
        <img src="assets/logo.svg" alt="VISTRAL Logo" class="w-8 h-8 sm:w-9 sm:h-9 transform group-hover:rotate-6 transition-transform">
        <div class="flex flex-col">
          <span class="font-display font-bold text-xl sm:text-2xl tracking-tight text-charcoal dark:text-white uppercase leading-none">VISTRAL</span>
          <span class="text-[9px] sm:text-[10px] tracking-[0.25em] text-bronze uppercase font-semibold">UPVC Systems</span>
        </div>
      </a>

      <!-- Desktop Navigation Links (Responsive Spacing: never wraps at 1024px) -->
      <nav class="hidden lg:flex items-center space-x-3 xl:space-x-6 2xl:space-x-7 rtl:space-x-reverse flex-shrink-0">
        {nav_links}
      </nav>

      <!-- Utility Controls & Actions -->
      <div class="hidden lg:flex items-center space-x-2 xl:space-x-3 rtl:space-x-reverse flex-shrink-0">
        <!-- RTL Toggle Icon -->
        <button class="rtl-toggle p-2 rounded-full border border-charcoal/15 dark:border-white/15 hover:border-bronze transition-all text-charcoal dark:text-stone-200 hover:text-bronze flex items-center justify-center" title="Toggle Layout Direction (LTR / RTL)" aria-label="Toggle Layout Direction">
          <svg class="w-4 h-4 fill-none stroke-current stroke-2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
            <path d="m16 3 4 4-4 4"/><path d="M20 7H4"/><path d="m8 21-4-4 4-4"/><path d="M4 17h16"/>
          </svg>
        </button>

        <!-- Theme Toggle -->
        <button class="theme-toggle p-2 rounded-full border border-charcoal/15 dark:border-white/15 hover:border-bronze transition-all text-charcoal dark:text-stone-200" aria-label="Toggle Theme">
          <i data-lucide="moon" class="theme-icon w-4 h-4"></i>
        </button>

        <!-- Login Link -->
        <a href="login.html" class="text-xs xl:text-sm font-semibold text-charcoal/90 dark:text-stone-200 hover:text-bronze px-2 py-1 transition-colors whitespace-nowrap">
          Login
        </a>

        <!-- Free Quote CTA -->
        <a href="contact.html#measurement-booking" class="bronze-gradient-btn px-3 py-2 xl:px-4 xl:py-2 rounded-lg text-xs uppercase tracking-wider font-semibold inline-flex items-center space-x-1.5 xl:space-x-2 rtl:space-x-reverse whitespace-nowrap flex-shrink-0">
          <span>Get Quote</span>
          <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 icon-flip"></i>
        </a>
      </div>

      <!-- Mobile / Tablet Controls (< 1024px) -->
      <div class="flex items-center lg:hidden">
        <button id="mobileMenuToggle" class="p-2 rounded-lg border border-charcoal/20 dark:border-white/20 text-charcoal dark:text-white" aria-label="Open Navigation">
          <i data-lucide="menu" class="w-6 h-6"></i>
        </button>
      </div>
    </div>
  </header>

  <!-- Header Spacer for Fixed Navigation -->
  <div class="h-[68px] sm:h-[72px] w-full shrink-0" aria-hidden="true"></div>

  <!-- Mobile Drawer Backdrop -->
  <div id="mobileMenuBackdrop" class="fixed inset-0 bg-black/60 z-50 opacity-0 pointer-events-none transition-opacity duration-300"></div>

  <!-- Mobile Navigation Drawer -->
  <div id="mobileMenuDrawer" class="invisible fixed top-0 right-0 rtl:right-auto rtl:left-0 w-80 max-w-[85%] h-full bg-ivory dark:bg-[#182029] z-50 shadow-2xl transform translate-x-full rtl:-translate-x-full transition-transform duration-300 ease-in-out p-6 flex flex-col justify-between overflow-y-auto">
    <div>
      <div class="flex items-center justify-between pb-6 border-b border-charcoal/10 dark:border-white/10">
        <div class="flex items-center space-x-2.5 rtl:space-x-reverse">
          <img src="assets/logo.svg" alt="VISTRAL Logo" class="w-8 h-8">
          <span class="font-display font-bold text-xl uppercase tracking-tight text-charcoal dark:text-white">VISTRAL</span>
        </div>
        <button id="mobileMenuClose" class="p-2 rounded-full hover:bg-stone-200 dark:hover:bg-stone-800 text-charcoal dark:text-white" aria-label="Close Navigation">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <nav class="mt-6 space-y-1">
        {mobile_nav_links}
      </nav>
    </div>

    <div class="pt-6 border-t border-charcoal/10 dark:border-white/10 space-y-4">
      <div class="flex items-center justify-between">
        <span class="text-xs uppercase tracking-wider text-charcoal/60 dark:text-stone-400 font-semibold">Direction / Theme</span>
        <div class="flex items-center space-x-2 rtl:space-x-reverse">
          <button class="rtl-toggle p-2 rounded-full border border-charcoal/20 dark:border-white/20 hover:border-bronze transition-all text-charcoal dark:text-stone-200 hover:text-bronze flex items-center justify-center" title="Toggle Layout Direction (LTR / RTL)" aria-label="Toggle Layout Direction">
            <svg class="w-4 h-4 fill-none stroke-current stroke-2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
              <path d="m16 3 4 4-4 4"/><path d="M20 7H4"/><path d="m8 21-4-4 4-4"/><path d="M4 17h16"/>
            </svg>
          </button>
          <button class="theme-toggle p-2 rounded-full border border-charcoal/20 dark:border-white/20">
            <i data-lucide="moon" class="theme-icon w-4 h-4"></i>
          </button>
        </div>
      </div>
      <div class="grid grid-cols-2 gap-2">
        <a href="login.html" class="text-center py-2.5 rounded-lg border border-charcoal/20 dark:border-white/20 text-xs uppercase font-bold tracking-wider hover:border-bronze">
          Login
        </a>
        <a href="signup.html" class="text-center py-2.5 rounded-lg bg-charcoal dark:bg-stone-800 text-white text-xs uppercase font-bold tracking-wider">
          Sign Up
        </a>
      </div>
      <a href="contact.html#measurement-booking" class="w-full bronze-gradient-btn py-3 rounded-lg text-center text-xs uppercase font-bold tracking-wider inline-flex items-center justify-center space-x-2 rtl:space-x-reverse">
        <span>Get Quote</span>
        <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 icon-flip"></i>
      </a>
    </div>
  </div>
"""

def get_footer():
    return """
  <!-- Premium Footer -->
  <footer class="bg-white dark:bg-charcoal text-charcoal dark:text-white pt-16 pb-12 border-t border-charcoal/10 dark:border-bronze/20 mt-auto transition-colors duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 pb-12 border-b border-charcoal/10 dark:border-white/10">
        <!-- Col 1: Brand & Bio -->
        <div class="lg:col-span-2 space-y-4">
          <div class="flex items-center space-x-3 rtl:space-x-reverse">
            <img src="assets/logo.svg" alt="VISTRAL Logo" class="w-9 h-9">
            <div>
              <span class="font-display font-bold text-2xl tracking-tight text-charcoal dark:text-white uppercase leading-none">VISTRAL</span>
              <span class="block text-[10px] tracking-[0.25em] text-bronze uppercase font-semibold">UPVC Architectural Systems</span>
            </div>
          </div>
          <p class="text-charcoal/70 dark:text-stone-300 text-sm leading-relaxed max-w-sm">
            Engineering luxury architectural glazing, ultra-energy-efficient UPVC window frames, and precision sliding patio doors. Certified German profiles engineered for tropical resilience, acoustic silence, and lifelong architectural elegance.
          </p>
          <div class="flex items-center space-x-3 rtl:space-x-reverse pt-2">
            <!-- LinkedIn (Official #0A66C2) -->
            <a href="https://linkedin.com" target="_blank" rel="noopener" class="social-btn-linkedin w-9 h-9 rounded-full bg-charcoal/5 dark:bg-white/5 border border-charcoal/10 dark:border-white/10 flex items-center justify-center text-charcoal/70 dark:text-stone-300" aria-label="LinkedIn">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
                <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 8.76a1.67 1.67 0 1 0 0-3.34 1.67 1.67 0 0 0 0 3.34m1.39 9.74v-8.37H5.07v8.37h2.78z"/>
              </svg>
            </a>
            <!-- Instagram (Official Gradient) -->
            <a href="https://instagram.com" target="_blank" rel="noopener" class="social-btn-instagram w-9 h-9 rounded-full bg-charcoal/5 dark:bg-white/5 border border-charcoal/10 dark:border-white/10 flex items-center justify-center text-charcoal/70 dark:text-stone-300" aria-label="Instagram">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
              </svg>
            </a>
            <!-- YouTube (Official #FF0000) -->
            <a href="https://youtube.com" target="_blank" rel="noopener" class="social-btn-youtube w-9 h-9 rounded-full bg-charcoal/5 dark:bg-white/5 border border-charcoal/10 dark:border-white/10 flex items-center justify-center text-charcoal/70 dark:text-stone-300" aria-label="YouTube">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
                <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
              </svg>
            </a>
            <!-- Pinterest (Official #E60023) -->
            <a href="https://pinterest.com" target="_blank" rel="noopener" class="social-btn-pinterest w-9 h-9 rounded-full bg-charcoal/5 dark:bg-white/5 border border-charcoal/10 dark:border-white/10 flex items-center justify-center text-charcoal/70 dark:text-stone-300" aria-label="Pinterest">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
                <path d="M12 0a12 12 0 0 0-4.37 23.18c-.06-.94-.12-2.39.02-3.42.14-.99.96-4.08.96-4.08s-.24-.49-.24-1.22c0-1.14.66-2 1.49-2 .7 0 1.04.53 1.04 1.16 0 .71-.45 1.77-.69 2.75-.2 8.35.41 1.51 1.22 1.51 1.47 0 2.6-1.55 2.6-3.79 0-1.98-1.42-3.36-3.46-3.36-2.52 0-4 1.89-4 3.85 0 .76.29 1.58.66 2.03.07.09.08.17.06.26-.07.29-.23.94-.26 1.07-.04.18-.15.22-.34.13-1.25-.58-2.03-2.4-2.03-3.87 0-3.15 2.29-6.04 6.6-6.04 3.46 0 6.16 2.47 6.16 5.77 0 3.44-2.17 6.21-5.18 6.21-1.01 0-1.97-.53-2.29-1.15l-.62 2.38c-.23.87-.84 1.96-1.25 2.63A12 12 0 1 0 12 0z"/>
              </svg>
            </a>
          </div>
        </div>

        <!-- Col 2: Window Solutions -->
        <div class="space-y-3">
          <h4 class="font-display text-sm uppercase tracking-wider font-bold text-bronze">UPVC Windows</h4>
          <ul class="space-y-2 text-sm text-charcoal/70 dark:text-stone-300">
            <li><a href="products.html#casement-windows" class="hover:text-bronze transition-colors">Casement Windows</a></li>
            <li><a href="products.html#sliding-windows" class="hover:text-bronze transition-colors">Sliding Windows</a></li>
            <li><a href="products.html#tilt-turn-windows" class="hover:text-bronze transition-colors">Tilt & Turn Systems</a></li>
            <li><a href="products.html#fixed-panoramic" class="hover:text-bronze transition-colors">Fixed Panoramic</a></li>
            <li><a href="products.html#bay-windows" class="hover:text-bronze transition-colors">Bay & Combination</a></li>
            <li><a href="products.html#arch-windows" class="hover:text-bronze transition-colors">Architectural Arches</a></li>
          </ul>
        </div>

        <!-- Col 3: Door Systems -->
        <div class="space-y-3">
          <h4 class="font-display text-sm uppercase tracking-wider font-bold text-bronze">UPVC Doors</h4>
          <ul class="space-y-2 text-sm text-charcoal/70 dark:text-stone-300">
            <li><a href="products.html#sliding-doors" class="hover:text-bronze transition-colors">Panoramic Sliding Doors</a></li>
            <li><a href="products.html#french-doors" class="hover:text-bronze transition-colors">Classic French Doors</a></li>
            <li><a href="products.html#folding-bifold" class="hover:text-bronze transition-colors">Folding Bi-Fold Systems</a></li>
            <li><a href="products.html#lift-slide" class="hover:text-bronze transition-colors">Heavy Lift & Slide</a></li>
            <li><a href="products.html#entrance-doors" class="hover:text-bronze transition-colors">High-Security Entrance</a></li>
            <li><a href="products.html#balcony-doors" class="hover:text-bronze transition-colors">Balcony & Terrace Doors</a></li>
          </ul>
        </div>

        <!-- Col 4: Newsletter & Direct Contact -->
        <div class="space-y-3">
          <h4 class="font-display text-sm uppercase tracking-wider font-bold text-bronze">Architectural Gazette</h4>
          <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
            Receive technical whitepapers, acoustic glazing updates, and new profile releases directly in your inbox.
          </p>
          <form class="newsletter-form flex flex-col space-y-2">
            <div class="relative">
              <input type="email" required placeholder="Enter your work email" class="w-full bg-ivory dark:bg-white/5 border border-charcoal/15 dark:border-white/15 focus:border-bronze rounded-lg px-3.5 py-2.5 text-xs text-charcoal dark:text-white placeholder-charcoal/40 dark:placeholder-stone-400 focus:outline-none">
            </div>
            <button type="submit" class="bronze-gradient-btn py-2 px-4 rounded-lg text-xs uppercase font-bold tracking-wider text-center">
              Subscribe
            </button>
          </form>
          <div class="pt-2 text-xs text-charcoal/70 dark:text-stone-400 space-y-1">
            <div class="flex items-center space-x-2 rtl:space-x-reverse">
              <i data-lucide="phone-call" class="w-3.5 h-3.5 text-bronze"></i>
              <span>+1 (800) 482-7832 (Toll Free)</span>
            </div>
            <div class="flex items-center space-x-2 rtl:space-x-reverse">
              <i data-lucide="mail" class="w-3.5 h-3.5 text-bronze"></i>
              <span>architects@vistralsystems.com</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="pt-8 flex flex-col md:flex-row items-center justify-between text-xs text-charcoal/60 dark:text-stone-400 gap-4">
        <p>&copy; 2026 VISTRAL Architectural UPVC Systems Inc. All rights reserved.</p>
        <div class="flex items-center space-x-5 rtl:space-x-reverse">
          <a href="about.html" class="hover:text-bronze transition-colors">Quality Standards</a>
          <a href="contact.html" class="hover:text-bronze transition-colors">Factory Audits</a>
          <a href="login.html" class="hover:text-bronze transition-colors">Partner Portal</a>
          <a href="contact.html#faq" class="hover:text-bronze transition-colors">Warranty & FAQ</a>
          
          <!-- Back to Top Arrow in Right Corner -->
          <button type="button" class="back-to-top-btn w-9 h-9 rounded-full bg-charcoal/5 dark:bg-white/10 hover:bg-bronze dark:hover:bg-bronze border border-charcoal/15 dark:border-white/20 text-charcoal dark:text-stone-200 hover:text-white dark:hover:text-white flex items-center justify-center transition-all duration-300 transform hover:-translate-y-1 hover:shadow-[0_0_15px_rgba(182,139,88,0.4)] ml-2 rtl:ml-0 rtl:mr-2 group cursor-pointer" title="Back to Top" aria-label="Back to Top">
            <i data-lucide="arrow-up" class="w-4 h-4 transform group-hover:-translate-y-0.5 transition-transform"></i>
          </button>
        </div>
      </div>
    </div>
  </footer>

  <!-- Lightbox Modal Container -->
  <div id="lightboxModal" class="hidden fixed inset-0 z-50 bg-black/90 flex items-center justify-center p-4">
    <button id="lightboxClose" class="absolute top-6 right-6 rtl:right-auto rtl:left-6 text-white hover:text-bronze p-2" aria-label="Close Lightbox">
      <i data-lucide="x" class="w-8 h-8"></i>
    </button>
    <button id="lightboxPrev" class="absolute left-6 rtl:left-auto rtl:right-6 top-1/2 -translate-y-1/2 text-white hover:text-bronze p-3 bg-white/10 rounded-full" aria-label="Previous Image">
      <i data-lucide="chevron-left" class="w-6 h-6 icon-flip"></i>
    </button>
    <button id="lightboxNext" class="absolute right-6 rtl:right-auto rtl:left-6 top-1/2 -translate-y-1/2 text-white hover:text-bronze p-3 bg-white/10 rounded-full" aria-label="Next Image">
      <i data-lucide="chevron-right" class="w-6 h-6 icon-flip"></i>
    </button>
    <div class="max-w-4xl max-h-[85vh] flex flex-col items-center">
      <img id="lightboxImg" src="" alt="Project Preview" class="max-h-[75vh] w-auto object-contain rounded-lg shadow-2xl">
      <div class="mt-4 text-center">
        <span id="lightboxCategory" class="text-xs uppercase tracking-widest text-bronze font-bold"></span>
        <h3 id="lightboxTitle" class="text-lg font-bold text-white font-display mt-0.5"></h3>
      </div>
    </div>
  </div>

  <!-- Scripts -->
  <script src="js/main.js"></script>
</body>
</html>
"""

print("Common template generators ready")
