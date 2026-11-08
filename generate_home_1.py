import os
from templates import get_head, get_header, get_footer

def build_home_1():
    content = get_head("Home 1", "home")
    content += get_header("home")
    content += """
  <main class="flex-grow">
    <!-- SECTION 1: PREMIUM HERO SECTION -->
    <section class="relative min-h-[92vh] flex items-center justify-center overflow-hidden py-20 px-4 sm:px-8">
      <!-- Full-Width Background Architectural Image with Gradient Overlays -->
      <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=2000&q=85" 
             alt="Modern luxury architectural estate with panoramic UPVC windows" 
             class="w-full h-full object-cover object-center filter brightness-[0.82] contrast-[1.05] transition-transform duration-1000 scale-105">
        <div class="absolute inset-0 bg-gradient-to-r from-charcoal/95 via-charcoal/70 to-transparent dark:from-[#0C1116]/95 dark:via-[#12181F]/80"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-charcoal/80 via-transparent to-charcoal/30"></div>
      </div>

      <!-- Hero Content Composition -->
      <div class="relative z-10 max-w-7xl mx-auto w-full grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-8 space-y-6" data-aos="fade-right">
          <!-- Floating Editorial Pill -->
          <div class="inline-flex items-center space-x-2.5 px-3.5 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-white rtl:space-x-reverse">
            <span class="w-2 h-2 rounded-full bg-bronze animate-ping"></span>
            <span class="text-xs font-semibold tracking-widest uppercase text-bronze-200">German Engineering Standard DIN 18055</span>
          </div>

          <!-- Main Headline -->
          <h1 class="font-display font-extrabold text-4xl sm:text-6xl lg:text-7xl text-white tracking-tight leading-[1.08]">
            Precision Crafted Windows. <br>
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-bronze-200 via-bronze to-bronze-400">Beautifully Designed</span> Living.
          </h1>

          <!-- Short Supporting Description -->
          <p class="text-base sm:text-xl text-stone-200 max-w-2xl font-normal leading-relaxed">
            Elevating modern architecture with bespoke multi-chamber UPVC profiles, multi-point acoustic sealing, and high-performance solar control glazing engineered for 50+ years of quiet serenity.
          </p>

          <!-- CTAs -->
          <div class="pt-4 flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
            <a href="products.html" class="w-full sm:w-auto bronze-gradient-btn px-8 py-4 rounded-xl text-xs uppercase font-bold tracking-wider inline-flex items-center justify-center space-x-2 rtl:space-x-reverse group shadow-2xl">
              <span>Explore Products</span>
              <i data-lucide="arrow-right" class="w-4 h-4 transform group-hover:translate-x-1 transition-transform icon-flip"></i>
            </a>
            <a href="contact.html#measurement-booking" class="w-full sm:w-auto px-8 py-4 rounded-xl text-xs uppercase font-bold tracking-wider text-white bg-white/10 hover:bg-white/20 backdrop-blur-md border border-white/25 inline-flex items-center justify-center space-x-2 rtl:space-x-reverse transition-all">
              <span>Get Free Quote</span>
              <i data-lucide="clipboard-check" class="w-4 h-4 text-bronze"></i>
            </a>
          </div>

          <!-- Floating Badges Feature Matrix -->
          <div class="pt-8 grid grid-cols-3 gap-4 border-t border-white/15 max-w-xl text-white">
            <div>
              <span class="block font-display text-2xl sm:text-3xl font-bold text-bronze-200">0.78</span>
              <span class="text-xs text-stone-300 font-medium tracking-wide">U-Value (W/m²K)</span>
            </div>
            <div>
              <span class="block font-display text-2xl sm:text-3xl font-bold text-bronze-200">46 dB</span>
              <span class="text-xs text-stone-300 font-medium tracking-wide">Acoustic Reduction</span>
            </div>
            <div>
              <span class="block font-display text-2xl sm:text-3xl font-bold text-bronze-200">Class 4</span>
              <span class="text-xs text-stone-300 font-medium tracking-wide">Air Permeability</span>
            </div>
          </div>
        </div>

        <!-- Floating Architectural Detail Card (Editorial Layer) -->
        <div class="lg:col-span-4 hidden lg:block" data-aos="fade-left">
          <div class="relative glass-card p-6 rounded-2xl border border-white/20 shadow-2xl space-y-4 animate-float-slow">
            <div class="flex items-center justify-between text-white">
              <div class="flex items-center space-x-2 rtl:space-x-reverse">
                <i data-lucide="shield-check" class="w-5 h-5 text-bronze"></i>
                <span class="text-xs uppercase font-bold tracking-wider">Reinforced Core</span>
              </div>
              <span class="px-2 py-0.5 rounded bg-bronze/30 text-[10px] text-bronze-100 font-mono font-bold">GALVANIZED STEEL</span>
            </div>
            <div class="rounded-xl overflow-hidden aspect-[4/3] relative">
              <img src="https://images.unsplash.com/photo-1541123437800-1bb1317badc2?auto=format&fit=crop&w=800&q=80" 
                   alt="Precision mitred UPVC corner detail" 
                   class="w-full h-full object-cover">
              <div class="absolute bottom-2 left-2 right-2 bg-charcoal/80 backdrop-blur-md px-3 py-1.5 rounded text-[11px] text-white flex justify-between">
                <span>Multi-Chambered Profile</span>
                <span class="text-bronze font-bold">Series 88mm</span>
              </div>
            </div>
            <p class="text-xs text-stone-200 leading-normal">
              Fused seamless corners resistant to tropical humidity, salt air corrosion, and heavy driving rainstorms.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2: WHY CHOOSE OUR UPVC SOLUTIONS -->
    <section class="py-24 px-4 sm:px-8 bg-ivory dark:bg-[#12181F] architectural-grid relative">
      <div class="max-w-7xl mx-auto">
        <!-- Section Header -->
        <div class="flex flex-col md:items-center xl:flex-row xl:items-end justify-between mb-16 md:text-center xl:text-left gap-6 max-w-2xl md:max-w-3xl xl:max-w-7xl md:mx-auto xl:mx-0" data-aos="fade-up">
          <div class="max-w-2xl">
            <div class="flex items-center md:justify-center xl:justify-start space-x-2 rtl:space-x-reverse mb-3">
              <span class="w-6 h-0.5 bg-bronze"></span>
              <span class="text-xs uppercase font-bold tracking-widest text-bronze">Engineering Performance</span>
            </div>
            <h2 class="font-display text-3xl sm:text-5xl font-extrabold tracking-tight text-charcoal dark:text-white">
              Why Architectural Masters Choose Our UPVC Solutions
            </h2>
          </div>
          <p class="text-charcoal/70 dark:text-stone-300 text-sm max-w-md md:max-w-xl xl:max-w-md leading-relaxed">
            Engineered through high-fusion compounding to outperform conventional aluminum and wood with superior thermal insulation, zero repainting, and decades of silent comfort.
          </p>
        </div>

        <!-- Creative Non-Ordinary Layout: Asymmetrical Feature Bento Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6">
          <!-- Item 1: Energy Efficiency (Hero Box) -->
          <div class="md:col-span-2 lg:col-span-2 p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 relative overflow-hidden group shadow-lg" data-aos="fade-up">
            <div class="absolute -right-8 -bottom-8 w-44 h-44 rounded-full bg-bronze/10 filter blur-2xl group-hover:bg-bronze/20 transition-all"></div>
            <div class="w-14 h-14 rounded-2xl bg-bronze/15 flex items-center justify-center text-bronze mb-6">
              <i data-lucide="zap-off" class="w-7 h-7"></i>
            </div>
            <span class="text-xs font-mono font-bold text-bronze uppercase tracking-wider">Thermal Barrier</span>
            <h3 class="font-display text-2xl font-bold mt-2 mb-3 text-charcoal dark:text-white">Ultra Energy Efficiency</h3>
            <p class="text-sm text-charcoal/70 dark:text-stone-300 leading-relaxed max-w-md">
              Multi-chambered insulating internal profiles eliminate thermal bridging. Slash HVAC cooling and heating expenses by up to 42% year-round with Low-E argon double and triple glazing.
            </p>
            <div class="mt-6 flex items-center space-x-4 text-xs font-semibold text-charcoal/80 dark:text-stone-200 rtl:space-x-reverse">
              <span class="flex items-center"><i data-lucide="check-circle-2" class="w-4 h-4 text-bronze mr-1 rtl:ml-1"></i> Passivhaus Certified</span>
              <span class="flex items-center"><i data-lucide="check-circle-2" class="w-4 h-4 text-bronze mr-1 rtl:ml-1"></i> Solar Heat Gain (SHGC 0.24)</span>
            </div>
          </div>

          <!-- Item 2: Sound Insulation -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 relative group shadow-lg" data-aos="fade-up" data-aos-delay="100">
            <div class="w-14 h-14 rounded-2xl bg-charcoal text-white dark:bg-stone-800 flex items-center justify-center mb-6">
              <i data-lucide="volume-x" class="w-7 h-7 text-bronze"></i>
            </div>
            <span class="text-xs font-mono font-bold text-bronze uppercase tracking-wider">Acoustic Shield</span>
            <h3 class="font-display text-xl font-bold mt-2 mb-3 text-charcoal dark:text-white">Sound Insulation</h3>
            <p class="text-sm text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Dampens high-traffic decibels, highway drones, and aircraft noise by up to 45 dB with double EPDM compression gaskets.
            </p>
          </div>

          <!-- Item 3: Weather Resistance -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 relative group shadow-lg" data-aos="fade-up" data-aos-delay="200">
            <div class="w-14 h-14 rounded-2xl bg-bronze/15 flex items-center justify-center text-bronze mb-6">
              <i data-lucide="cloud-lightning" class="w-7 h-7"></i>
            </div>
            <span class="text-xs font-mono font-bold text-bronze uppercase tracking-wider">Monsoon Proof</span>
            <h3 class="font-display text-xl font-bold mt-2 mb-3 text-charcoal dark:text-white">Weather Resistance</h3>
            <p class="text-sm text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Tested to withstand 240 km/h cyclone gusts and driving torrential rain without a single droplet penetrating internal seals.
            </p>
          </div>

          <!-- Item 4: Structural Durability -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 relative group shadow-lg" data-aos="fade-up" data-aos-delay="300">
            <div class="w-14 h-14 rounded-2xl bg-bronze/15 flex items-center justify-center text-bronze mb-6">
              <i data-lucide="hammer" class="w-7 h-7"></i>
            </div>
            <span class="text-xs font-mono font-bold text-bronze uppercase tracking-wider">Reinforced Core</span>
            <h3 class="font-display text-xl font-bold mt-2 mb-3 text-charcoal dark:text-white">Durability & Lifespan</h3>
            <p class="text-sm text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Resistant to yellowing, UV chalking, warping, termites, and corrosive coastal salt mist. Rated for 50+ years of operation.
            </p>
          </div>

          <!-- Item 5: Low Maintenance (Wide Box) -->
          <div class="md:col-span-2 lg:col-span-3 p-8 rounded-3xl bg-charcoal text-white dark:bg-[#182029] border border-bronze/20 relative overflow-hidden group shadow-xl flex flex-col md:flex-row items-center justify-between gap-6" data-aos="fade-up" data-aos-delay="400">
            <div class="space-y-3 max-w-xl">
              <span class="text-xs font-mono font-bold text-bronze uppercase tracking-wider">Zero Maintenance Hassle</span>
              <h3 class="font-display text-2xl font-bold text-white">Never Sand, Varnish, or Repaint Again</h3>
              <p class="text-sm text-stone-300 leading-relaxed">
                Our UV-stabilized German polymer formulations never peel or rust. A gentle wipe with warm soapy water restores their pristine factory sheen even after decades of desert heat or humid monsoon seasons.
              </p>
            </div>
            <div class="flex-shrink-0">
              <a href="about.html#quality-standards" class="bronze-gradient-btn px-6 py-3 rounded-xl text-xs uppercase tracking-wider font-bold inline-flex items-center space-x-2 rtl:space-x-reverse">
                <span>View Quality Audits</span>
                <i data-lucide="arrow-right" class="w-4 h-4 icon-flip"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: FEATURED UPVC PRODUCTS -->
    <section class="py-24 px-4 sm:px-8 bg-white dark:bg-[#182029] border-y border-charcoal/10 dark:border-white/10">
      <div class="max-w-7xl mx-auto">
        <!-- Section Header -->
        <div class="text-center max-w-3xl mx-auto mb-16" data-aos="fade-up">
          <span class="text-xs uppercase font-bold tracking-widest text-bronze block mb-2">Architectural Portfolio</span>
          <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight">
            Featured UPVC Systems
          </h2>
          <p class="text-charcoal/70 dark:text-stone-300 text-sm mt-3">
            Tailor-engineered casements, expansive sliders, and multi-leaf patio doors built to millimeter precision.
          </p>
        </div>

        <!-- 6 Featured Products Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 items-stretch">
          <!-- 1. Casement Windows -->
          <div class="group rounded-2xl overflow-hidden border border-charcoal/10 dark:border-white/10 bg-ivory dark:bg-[#12181F] transition-all hover:shadow-2xl flex flex-col h-full" data-aos="fade-up">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80" 
                   alt="Modern Casement Windows in luxury residence" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-6 flex-1 flex flex-col justify-between">
              <div class="space-y-3">
                <div class="flex justify-between items-center text-xs">
                  <span class="text-[10px] xl:text-[11px] font-mono uppercase tracking-wider text-bronze font-bold whitespace-nowrap">Side-Hung / Top-Hung</span>
                  <span class="text-[11px] xl:text-xs text-charcoal/60 dark:text-stone-400 whitespace-nowrap">90° Opening</span>
                </div>
                <h3 class="font-display text-xl font-bold text-charcoal dark:text-white">Casement Windows</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                  Maximum natural airflow and unobstructed panoramic views with heavy-duty friction stays and triple-seal perimeter gaskets.
                </p>
              </div>
              <div class="pt-4 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="products.html#casement-windows" class="text-xs uppercase font-bold text-bronze hover:text-bronze-600 inline-flex items-center space-x-1.5 rtl:space-x-reverse">
                  <span>Explore Specs</span>
                  <i data-lucide="chevron-right" class="w-4 h-4 icon-flip"></i>
                </a>
                <a href="contact.html?product=Casement+Windows" class="text-xs font-semibold text-charcoal/80 dark:text-stone-300 hover:text-bronze">Enquire</a>
              </div>
            </div>
          </div>

          <!-- 2. Sliding Windows -->
          <div class="group rounded-2xl overflow-hidden border border-charcoal/10 dark:border-white/10 bg-ivory dark:bg-[#12181F] transition-all hover:shadow-2xl flex flex-col h-full" data-aos="fade-up" data-aos-delay="100">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1600585154526-990dced4db0d?auto=format&fit=crop&w=800&q=80" 
                   alt="Panoramic multi-track sliding windows" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-6 flex-1 flex flex-col justify-between">
              <div class="space-y-3">
                <div class="flex justify-between items-center text-xs">
                  <span class="text-[10px] xl:text-[11px] font-mono uppercase tracking-wider text-bronze font-bold whitespace-nowrap">2, 3 & 4 Multi-Track</span>
                  <span class="text-[11px] xl:text-xs text-charcoal/60 dark:text-stone-400 whitespace-nowrap">Silent Glide</span>
                </div>
                <h3 class="font-display text-xl font-bold text-charcoal dark:text-white">Sliding Windows</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                  Precision stainless steel tandem rollers provide weightless, silent gliding across expansive architectural apertures.
                </p>
              </div>
              <div class="pt-4 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="products.html#sliding-windows" class="text-xs uppercase font-bold text-bronze hover:text-bronze-600 inline-flex items-center space-x-1.5 rtl:space-x-reverse">
                  <span>Explore Specs</span>
                  <i data-lucide="chevron-right" class="w-4 h-4 icon-flip"></i>
                </a>
                <a href="contact.html?product=Sliding+Windows" class="text-xs font-semibold text-charcoal/80 dark:text-stone-300 hover:text-bronze">Enquire</a>
              </div>
            </div>
          </div>

          <!-- 3. Tilt & Turn Windows -->
          <div class="group rounded-2xl overflow-hidden border border-charcoal/10 dark:border-white/10 bg-ivory dark:bg-[#12181F] transition-all hover:shadow-2xl flex flex-col h-full" data-aos="fade-up" data-aos-delay="200">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1600573472550-8090b5e0745e?auto=format&fit=crop&w=800&q=80" 
                   alt="German Dual-Action Tilt and Turn Windows" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-6 flex-1 flex flex-col justify-between">
              <div class="space-y-3">
                <div class="flex justify-between items-center text-xs">
                  <span class="text-[10px] xl:text-[11px] font-mono uppercase tracking-wider text-bronze font-bold whitespace-nowrap">Dual Action System</span>
                  <span class="text-[11px] xl:text-xs text-charcoal/60 dark:text-stone-400 whitespace-nowrap">Micro-Vent</span>
                </div>
                <h3 class="font-display text-xl font-bold text-charcoal dark:text-white">Tilt & Turn Windows</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                  Versatile European hardware tilts from the top for secure draft-free ventilation or swings inwards for effortless interior cleaning.
                </p>
              </div>
              <div class="pt-4 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="products.html#tilt-turn-windows" class="text-xs uppercase font-bold text-bronze hover:text-bronze-600 inline-flex items-center space-x-1.5 rtl:space-x-reverse">
                  <span>Explore Specs</span>
                  <i data-lucide="chevron-right" class="w-4 h-4 icon-flip"></i>
                </a>
                <a href="contact.html?product=Tilt+and+Turn" class="text-xs font-semibold text-charcoal/80 dark:text-stone-300 hover:text-bronze">Enquire</a>
              </div>
            </div>
          </div>

          <!-- 4. Fixed Panoramic Windows -->
          <div class="group rounded-2xl overflow-hidden border border-charcoal/10 dark:border-white/10 bg-ivory dark:bg-[#12181F] transition-all hover:shadow-2xl flex flex-col h-full" data-aos="fade-up" data-aos-delay="300">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=800&q=80" 
                   alt="Fixed architectural picture windows" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-6 flex-1 flex flex-col justify-between">
              <div class="space-y-3">
                <div class="flex justify-between items-center text-xs">
                  <span class="text-[10px] xl:text-[11px] font-mono uppercase tracking-wider text-bronze font-bold whitespace-nowrap">Non-Operable Glazing</span>
                  <span class="text-[11px] xl:text-xs text-charcoal/60 dark:text-stone-400 whitespace-nowrap">Acoustic Class 5</span>
                </div>
                <h3 class="font-display text-xl font-bold text-charcoal dark:text-white">Fixed Panoramic Windows</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                  Immaculate sightlines designed to frame dramatic landscapes, providing unmatched structural strength and zero air infiltration.
                </p>
              </div>
              <div class="pt-4 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="products.html#fixed-panoramic" class="text-xs uppercase font-bold text-bronze hover:text-bronze-600 inline-flex items-center space-x-1.5 rtl:space-x-reverse">
                  <span>Explore Specs</span>
                  <i data-lucide="chevron-right" class="w-4 h-4 icon-flip"></i>
                </a>
                <a href="contact.html?product=Fixed+Panoramic" class="text-xs font-semibold text-charcoal/80 dark:text-stone-300 hover:text-bronze">Enquire</a>
              </div>
            </div>
          </div>

          <!-- 5. Expansive Sliding Doors -->
          <div class="group rounded-2xl overflow-hidden border border-charcoal/10 dark:border-white/10 bg-ivory dark:bg-[#12181F] transition-all hover:shadow-2xl flex flex-col h-full" data-aos="fade-up" data-aos-delay="400">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=800&q=80" 
                   alt="Modern sliding glass patio doors" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-6 flex-1 flex flex-col justify-between">
              <div class="space-y-3">
                <div class="flex justify-between items-center text-xs">
                  <span class="text-[10px] xl:text-[11px] font-mono uppercase tracking-wider text-bronze font-bold whitespace-nowrap">Flush Threshold</span>
                  <span class="text-[11px] xl:text-xs text-charcoal/60 dark:text-stone-400 whitespace-nowrap">Multi-Locking</span>
                </div>
                <h3 class="font-display text-xl font-bold text-charcoal dark:text-white">Sliding Patio Doors</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                  Seamless indoor-outdoor transitions with flush zero-barrier floor sills, reinforced steel interlocks, and security anti-lift blocks.
                </p>
              </div>
              <div class="pt-4 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="products.html#sliding-doors" class="text-xs uppercase font-bold text-bronze hover:text-bronze-600 inline-flex items-center space-x-1.5 rtl:space-x-reverse">
                  <span>Explore Specs</span>
                  <i data-lucide="chevron-right" class="w-4 h-4 icon-flip"></i>
                </a>
                <a href="contact.html?product=Sliding+Doors" class="text-xs font-semibold text-charcoal/80 dark:text-stone-300 hover:text-bronze">Enquire</a>
              </div>
            </div>
          </div>

          <!-- 6. French Balcony Doors -->
          <div class="group rounded-2xl overflow-hidden border border-charcoal/10 dark:border-white/10 bg-ivory dark:bg-[#12181F] transition-all hover:shadow-2xl flex flex-col h-full" data-aos="fade-up" data-aos-delay="500">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=800&q=80" 
                   alt="Elegant French UPVC patio doors" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-6 flex-1 flex flex-col justify-between">
              <div class="space-y-3">
                <div class="flex justify-between items-center text-xs">
                  <span class="text-[10px] xl:text-[11px] font-mono uppercase tracking-wider text-bronze font-bold whitespace-nowrap">Double-Leaf System</span>
                  <span class="text-[11px] xl:text-xs text-charcoal/60 dark:text-stone-400 whitespace-nowrap">Classic Grandeur</span>
                </div>
                <h3 class="font-display text-xl font-bold text-charcoal dark:text-white">French Architectural Doors</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                  Timeless dual-leaf symmetrical opening with floating mullion for a wide, unencumbered entrance onto terraces and courtyards.
                </p>
              </div>
              <div class="pt-4 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="products.html#french-doors" class="text-xs uppercase font-bold text-bronze hover:text-bronze-600 inline-flex items-center space-x-1.5 rtl:space-x-reverse">
                  <span>Explore Specs</span>
                  <i data-lucide="chevron-right" class="w-4 h-4 icon-flip"></i>
                </a>
                <a href="contact.html?product=French+Doors" class="text-xs font-semibold text-charcoal/80 dark:text-stone-300 hover:text-bronze">Enquire</a>
              </div>
            </div>
          </div>
        </div>

        <div class="mt-12 text-center">
          <a href="products.html" class="inline-flex items-center space-x-2 bronze-gradient-btn px-8 py-3.5 rounded-xl text-xs uppercase font-bold tracking-wider rtl:space-x-reverse">
            <span>Browse Full Product Catalogue</span>
            <i data-lucide="arrow-right" class="w-4 h-4 icon-flip"></i>
          </a>
        </div>
      </div>
    </section>

    <!-- SECTION 4: INNOVATION & FABRICATION EXCELLENCE -->
    <section class="py-24 px-4 sm:px-8 bg-ivory dark:bg-[#12181F] overflow-hidden">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          <!-- Text Narrative -->
          <div class="lg:col-span-6 space-y-6" data-aos="fade-right">
            <div class="flex items-center space-x-2 rtl:space-x-reverse">
              <span class="w-6 h-0.5 bg-bronze"></span>
              <span class="text-xs uppercase font-bold tracking-widest text-bronze">Fabrication Facility</span>
            </div>
            <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight leading-tight">
              German CNC Precision. <br>
              Seamless Corner Fusion.
            </h2>
            <p class="text-sm sm:text-base text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Every VISTRAL system is precision-machined in our 75,000 sq.ft state-of-the-art facility utilizing 5-axis automated profile cutters, robotic 4-point hot plate corner welders, and computerized CNC deburring centers.
            </p>

            <div class="space-y-4 pt-2">
              <div class="flex items-start space-x-4 rtl:space-x-reverse">
                <div class="w-10 h-10 rounded-xl bg-bronze/15 text-bronze flex items-center justify-center flex-shrink-0 mt-0.5">
                  <i data-lucide="cpu" class="w-5 h-5"></i>
                </div>
                <div>
                  <h4 class="font-display font-bold text-base text-charcoal dark:text-white">Computerized Tolerances (±0.2mm)</h4>
                  <p class="text-xs text-charcoal/70 dark:text-stone-300 mt-1">Laser guided digital measurement ensuring zero frame distortion during thermal fluctuations.</p>
                </div>
              </div>

              <div class="flex items-start space-x-4 rtl:space-x-reverse">
                <div class="w-10 h-10 rounded-xl bg-bronze/15 text-bronze flex items-center justify-center flex-shrink-0 mt-0.5">
                  <i data-lucide="shield" class="w-5 h-5"></i>
                </div>
                <div>
                  <h4 class="font-display font-bold text-base text-charcoal dark:text-white">Integrated Galvanized Steel Core</h4>
                  <p class="text-xs text-charcoal/70 dark:text-stone-300 mt-1">2.0mm thick zinc-passivated reinforcement running continuously throughout sash and outer frame.</p>
                </div>
              </div>

              <div class="flex items-start space-x-4 rtl:space-x-reverse">
                <div class="w-10 h-10 rounded-xl bg-bronze/15 text-bronze flex items-center justify-center flex-shrink-0 mt-0.5">
                  <i data-lucide="layers" class="w-5 h-5"></i>
                </div>
                <div>
                  <h4 class="font-display font-bold text-base text-charcoal dark:text-white">Dual-Seal EPDM Weather Stripping</h4>
                  <p class="text-xs text-charcoal/70 dark:text-stone-300 mt-1">Ethylene propylene diene monomer gaskets prevent moisture seepage and withstand 40°C to +80°C extremes.</p>
                </div>
              </div>
            </div>

            <div class="pt-4">
              <a href="services.html#custom-fabrication" class="inline-flex items-center space-x-2 text-xs uppercase font-bold tracking-wider text-bronze hover:text-bronze-700 rtl:space-x-reverse">
                <span>Discover Our Manufacturing Workflow</span>
                <i data-lucide="arrow-right" class="w-4 h-4 icon-flip"></i>
              </a>
            </div>
          </div>

          <!-- Creative Overlapping Images Composition -->
          <div class="lg:col-span-6 relative" data-aos="fade-left">
            <div class="relative z-10 rounded-3xl overflow-hidden shadow-2xl border-4 border-white dark:border-[#182029] max-w-[90%]">
              <img src="https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=900&q=80" 
                   alt="Robotic precision CNC milling of UPVC profiles" 
                   class="w-full h-auto object-cover">
            </div>

            <div class="absolute -bottom-8 -right-4 w-2/3 rounded-2xl overflow-hidden shadow-2xl border-4 border-white dark:border-[#182029] z-20 hidden sm:block">
              <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=700&q=80" 
                   alt="Automated 4-point thermal weld fusion" 
                   class="w-full h-auto object-cover">
            </div>

            <!-- Floating Metric Badge -->
            <div class="absolute top-8 -left-6 z-30 bg-charcoal text-white px-5 py-3 rounded-2xl shadow-xl border border-bronze/30 hidden sm:flex items-center space-x-3 rtl:space-x-reverse">
              <div class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></div>
              <div>
                <span class="block text-xs uppercase text-stone-400 font-mono">Factory Output</span>
                <span class="text-sm font-bold font-display text-bronze-200">12,000+ Sashes / Month</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: OUR SIGNATURE PROJECTS -->
    <section class="py-24 px-4 sm:px-8 bg-white dark:bg-[#182029] border-t border-charcoal/10 dark:border-white/10">
      <div class="max-w-7xl mx-auto">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6" data-aos="fade-up">
          <div>
            <span class="text-xs uppercase font-bold tracking-widest text-bronze block mb-2">Architectural Showcase</span>
            <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight">
              Our Signature Projects
            </h2>
          </div>
          <a href="gallery.html" class="inline-flex items-center space-x-2 text-xs uppercase font-bold tracking-wider text-bronze hover:underline rtl:space-x-reverse">
            <span>View All Architectural Case Studies</span>
            <i data-lucide="arrow-right" class="w-4 h-4 icon-flip"></i>
          </a>
        </div>

        <!-- 3 Equal-Sized Signature Project Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8 items-stretch">
          <!-- Project 1 -->
          <div class="rounded-3xl overflow-hidden relative group shadow-xl flex flex-col justify-end min-h-[460px] p-8 border border-charcoal/10 dark:border-white/10" data-aos="fade-up">
            <img src="https://images.unsplash.com/photo-1600585152220-90363fe7e115?auto=format&fit=crop&w=1000&q=80" 
                 alt="The Glass Pavilion Luxury Estate UPVC Fenestration" 
                 class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
            <div class="absolute inset-0 bg-gradient-to-t from-charcoal/95 via-charcoal/45 to-transparent opacity-90 group-hover:opacity-95 transition-opacity"></div>
            
            <div class="relative z-10 space-y-3 text-white">
              <span class="inline-block px-3 py-1 rounded-full bg-bronze text-white text-[10px] font-mono uppercase font-bold tracking-wider">
                Residential Estate
              </span>
              <h3 class="font-display text-xl sm:text-2xl font-bold leading-snug">The Glass Pavilion</h3>
              <p class="text-xs text-stone-300 leading-relaxed">
                Custom triple-glazed sliding patio systems spanning 14m width with motorized insect screens and acoustic noise reduction.
              </p>
              <div class="pt-3 border-t border-white/15 flex items-center justify-between text-[11px] text-bronze-200 font-mono">
                <span>Beverly Hills, CA</span>
                <span>Completed 2025</span>
              </div>
            </div>
          </div>

          <!-- Project 2 -->
          <div class="rounded-3xl overflow-hidden relative group shadow-xl flex flex-col justify-end min-h-[460px] p-8 border border-charcoal/10 dark:border-white/10" data-aos="fade-up" data-aos-delay="100">
            <img src="https://images.unsplash.com/photo-1600607687644-c7171b42498f?auto=format&fit=crop&w=1000&q=80" 
                 alt="Skyline Commercial Centre UPVC Glazed Facade" 
                 class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
            <div class="absolute inset-0 bg-gradient-to-t from-charcoal/95 via-charcoal/45 to-transparent opacity-90 group-hover:opacity-95 transition-opacity"></div>
            
            <div class="relative z-10 space-y-3 text-white">
              <span class="inline-block px-3 py-1 rounded-full bg-white/20 backdrop-blur-md text-white text-[10px] font-mono uppercase font-bold tracking-wider">
                Commercial Tower
              </span>
              <h3 class="font-display text-xl sm:text-2xl font-bold leading-snug">Skyline Headquarters</h3>
              <p class="text-xs text-stone-300 leading-relaxed">
                Continuous thermal-break ribbon casement windows with acoustic Class 5 sound isolation and solar control glazing.
              </p>
              <div class="pt-3 border-t border-white/15 flex items-center justify-between text-[11px] text-bronze-200 font-mono">
                <span>Frankfurt, Germany</span>
                <span>Completed 2025</span>
              </div>
            </div>
          </div>

          <!-- Project 3 -->
          <div class="md:col-span-2 md:w-[calc(50%-1rem)] md:mx-auto xl:col-span-1 xl:w-full xl:mx-0 rounded-3xl overflow-hidden relative group shadow-xl flex flex-col justify-end min-h-[460px] p-8 border border-charcoal/10 dark:border-white/10" data-aos="fade-up" data-aos-delay="200">
            <img src="https://images.unsplash.com/photo-1600566752355-35792bedcfea?auto=format&fit=crop&w=1000&q=80" 
                 alt="Nordic Minimalist Retreat Fixed Corner Windows" 
                 class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
            <div class="absolute inset-0 bg-gradient-to-t from-charcoal/95 via-charcoal/45 to-transparent opacity-90 group-hover:opacity-95 transition-opacity"></div>
            
            <div class="relative z-10 space-y-3 text-white">
              <span class="inline-block px-3 py-1 rounded-full bg-white/20 backdrop-blur-md text-white text-[10px] font-mono uppercase font-bold tracking-wider">
                Modern Villa
              </span>
              <h3 class="font-display text-xl sm:text-2xl font-bold leading-snug">Nordic Solarium</h3>
              <p class="text-xs text-stone-300 leading-relaxed">
                Frameless corner butt-joint glazing with heavy reinforced UPVC perimeter and multi-point security deadbolts.
              </p>
              <div class="pt-3 border-t border-white/15 flex items-center justify-between text-[11px] text-bronze-200 font-mono">
                <span>Oslo, Norway</span>
                <span>Completed 2024</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 6: OUR INSTALLATION PROCESS -->
    <section class="py-24 px-4 sm:px-8 bg-ivory dark:bg-[#12181F] architectural-grid">
      <div class="max-w-7xl mx-auto">
        <div class="text-center max-w-2xl mx-auto mb-16" data-aos="fade-up">
          <span class="text-xs uppercase font-bold tracking-widest text-bronze block mb-2">Turnkey Execution</span>
          <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight">
            Our 6-Step Installation Process
          </h2>
          <p class="text-charcoal/70 dark:text-stone-300 text-sm mt-3">
            From laser scan to white-glove final inspection, every step is rigorously supervised by certified fenestration engineers.
          </p>
        </div>

        <!-- Creative Process Timeline -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 relative">
          <!-- Step 1 -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 relative group hover:shadow-xl transition-all" data-aos="fade-up">
            <span class="text-4xl font-display font-extrabold text-bronze/30 group-hover:text-bronze transition-colors">01</span>
            <h3 class="font-display text-xl font-bold mt-2 mb-2 text-charcoal dark:text-white min-h-[3.25rem] sm:min-h-[3.5rem] leading-snug">Architectural<br> Consultation</h3>
            <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
              In-depth assessment of sun exposure, wind pressure zones, sound pollution, and aesthetic sightlines tailored to your blueprints.
            </p>
          </div>

          <!-- Step 2 -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 relative group hover:shadow-xl transition-all" data-aos="fade-up" data-aos-delay="100">
            <span class="text-4xl font-display font-extrabold text-bronze/30 group-hover:text-bronze transition-colors">02</span>
            <h3 class="font-display text-xl font-bold mt-2 mb-2 text-charcoal dark:text-white min-h-[3.25rem] sm:min-h-[3.5rem] leading-snug">Precision Laser<br> Measurement</h3>
            <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
              3D digital site surveys capture opening diagonals and wall settlement to ensure airtight tolerance before production.
            </p>
          </div>

          <!-- Step 3 -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 relative group hover:shadow-xl transition-all" data-aos="fade-up" data-aos-delay="200">
            <span class="text-4xl font-display font-extrabold text-bronze/30 group-hover:text-bronze transition-colors">03</span>
            <h3 class="font-display text-xl font-bold mt-2 mb-2 text-charcoal dark:text-white min-h-[3.25rem] sm:min-h-[3.5rem] leading-snug">System Design &<br> Glass Curation</h3>
            <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Selection of multi-chamber profiles, profile colors (Anthracite Grey, Golden Oak), and double/triple glazing packages.
            </p>
          </div>

          <!-- Step 4 -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 relative group hover:shadow-xl transition-all" data-aos="fade-up" data-aos-delay="300">
            <span class="text-4xl font-display font-extrabold text-bronze/30 group-hover:text-bronze transition-colors">04</span>
            <h3 class="font-display text-xl font-bold mt-2 mb-2 text-charcoal dark:text-white min-h-[3.25rem] sm:min-h-[3.5rem] leading-snug">Computerized<br> Fabrication</h3>
            <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Automated 5-axis cutting, zinc reinforcement insertion, robotic hot-fusion corners, and pre-hanging hardware assembly.
            </p>
          </div>

          <!-- Step 5 -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 relative group hover:shadow-xl transition-all" data-aos="fade-up" data-aos-delay="400">
            <span class="text-4xl font-display font-extrabold text-bronze/30 group-hover:text-bronze transition-colors">05</span>
            <h3 class="font-display text-xl font-bold mt-2 mb-2 text-charcoal dark:text-white min-h-[3.25rem] sm:min-h-[3.5rem] leading-snug">Certified In-House<br> Installation</h3>
            <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Anchored with expansion fasteners, non-expanding polyurethane foam insulation, and structural silicone weather seals.
            </p>
          </div>

          <!-- Step 6 -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 relative group hover:shadow-xl transition-all" data-aos="fade-up" data-aos-delay="500">
            <span class="text-4xl font-display font-extrabold text-bronze/30 group-hover:text-bronze transition-colors">06</span>
            <h3 class="font-display text-xl font-bold mt-2 mb-2 text-charcoal dark:text-white min-h-[3.25rem] sm:min-h-[3.5rem] leading-snug">Acoustic & Water<br> Quality Audit</h3>
            <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Pressure nozzle water spray test, multi-point locking alignment check, and handover of your 20-Year Warranty Certificate.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 7: STRONG CONVERSION CTA -->
    <section class="relative py-28 px-4 sm:px-8 overflow-hidden bg-charcoal text-white">
      <!-- Background Visual with Texture Overlay -->
      <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1600607688969-a5bfcd646154?auto=format&fit=crop&w=2000&q=85" 
             alt="Architectural modern villa illuminated at twilight with UPVC windows" 
             class="w-full h-full object-cover filter brightness-[0.35]">
        <div class="absolute inset-0 bg-gradient-to-r from-charcoal via-charcoal/90 to-charcoal/60"></div>
      </div>

      <div class="relative z-10 max-w-5xl mx-auto text-center space-y-8" data-aos="zoom-in">
        <div class="inline-flex items-center space-x-2 px-4 py-1.5 rounded-full bg-bronze/20 border border-bronze/40 text-bronze-200 text-xs uppercase tracking-widest font-semibold rtl:space-x-reverse">
          <i data-lucide="sparkles" class="w-4 h-4"></i>
          <span>Engineered For Distinction</span>
        </div>

        <h2 class="font-display text-4xl sm:text-6xl font-extrabold tracking-tight text-white max-w-3xl mx-auto leading-tight">
          Upgrade Your Space with <span class="text-transparent bg-clip-text bg-gradient-to-r from-bronze-200 via-bronze to-bronze-400">Smarter Windows</span>.
        </h2>

        <p class="text-base sm:text-lg text-stone-300 max-w-2xl mx-auto leading-relaxed">
          Request a complimentary architectural site measurement, laser structural audit, and tailored quotation from our senior fenestration consultants.
        </p>

        <div class="flex flex-col sm:flex-row items-stretch sm:items-center justify-center gap-4 pt-4">
          <a href="contact.html#measurement-booking" class="w-full sm:w-auto bronze-gradient-btn px-8 py-4 rounded-xl text-xs uppercase font-bold tracking-wider inline-flex items-center justify-center space-x-2 rtl:space-x-reverse shadow-2xl">
            <span>Book Free Site Measurement</span>
            <i data-lucide="calendar-check" class="w-4 h-4"></i>
          </a>
          <a href="contact.html" class="w-full sm:w-auto px-8 py-4 rounded-xl text-xs uppercase font-bold tracking-wider bg-white/10 hover:bg-white/20 backdrop-blur-md border border-white/20 text-white inline-flex items-center justify-center space-x-2 rtl:space-x-reverse transition-all">
            <span>Speak With an Engineer</span>
            <i data-lucide="phone" class="w-4 h-4 text-bronze"></i>
          </a>
        </div>

        <div class="pt-8 flex flex-wrap items-center justify-center gap-8 text-xs text-stone-400 border-t border-white/10 max-w-2xl mx-auto">
          <span class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-1.5 rtl:ml-1.5"></i> Zero Obligation Estimate</span>
          <span class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-1.5 rtl:ml-1.5"></i> 20-Year Profile Warranty</span>
          <span class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-1.5 rtl:ml-1.5"></i> Factory Direct Pricing</span>
        </div>
      </div>
    </section>
  </main>
"""
    content += get_footer()
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("index.html (Home 1 - exactly 7 sections) generated successfully.")

if __name__ == "__main__":
    build_home_1()
