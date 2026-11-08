import os
from templates import get_head, get_header, get_footer

def build_products():
    content = get_head("Products - UPVC Windows & Doors Systems", "products")
    content += get_header("products")
    content += """
  <main class="flex-grow">
    <!-- SECTION 1: PRODUCTS HERO SECTION -->
    <section class="relative min-h-[50vh] flex items-center justify-center overflow-hidden py-24 px-4 sm:px-8 bg-charcoal text-white">
      <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=2000&q=85" 
             alt="VISTRAL UPVC window and door systems in contemporary architecture" 
             class="w-full h-full object-cover filter brightness-[0.35]">
        <div class="absolute inset-0 bg-gradient-to-t from-charcoal via-charcoal/70 to-transparent"></div>
      </div>

      <div class="relative z-10 max-w-4xl mx-auto text-center space-y-6" data-aos="fade-up">
        <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-bronze-200 text-xs uppercase tracking-widest font-mono font-semibold rtl:space-x-reverse">
          <span class="w-2 h-2 rounded-full bg-bronze"></span>
          <span>Architectural Fenestration Systems Catalogue 2026</span>
        </div>

        <h1 class="font-display font-extrabold text-4xl sm:text-6xl tracking-tight text-white leading-tight">
          Precision UPVC Windows & Doors
        </h1>

        <p class="text-base sm:text-lg text-stone-200 max-w-2xl mx-auto font-normal leading-relaxed">
          Engineered with multi-chamber internal geometry, galvanized steel reinforcement cores, and high-performance Low-E solar glazing.
        </p>

        <!-- Quick Jump Filter Pills -->
        <div class="flex flex-wrap items-center justify-center gap-3 pt-4">
          <a href="#windows-collection" class="px-5 py-2.5 rounded-full bg-white/10 hover:bg-bronze text-white text-xs uppercase tracking-wider font-bold transition-all border border-white/20">
            Windows Collection (8 Models)
          </a>
          <a href="#doors-collection" class="px-5 py-2.5 rounded-full bg-white/10 hover:bg-bronze text-white text-xs uppercase tracking-wider font-bold transition-all border border-white/20">
            Doors Collection (7 Models)
          </a>
          <a href="#customization-features" class="px-5 py-2.5 rounded-full bg-white/10 hover:bg-bronze text-white text-xs uppercase tracking-wider font-bold transition-all border border-white/20">
            Glass & Hardware Finishes
          </a>
        </div>
      </div>
    </section>

    <!-- SECTION 2: UPVC WINDOWS COLLECTION (8 Specific Types) -->
    <section id="windows-collection" class="py-24 px-4 sm:px-8 bg-ivory dark:bg-[#12181F] architectural-grid">
      <div class="max-w-7xl mx-auto space-y-16">
        <div class="flex flex-col md:items-center xl:flex-row xl:items-end justify-between md:text-center xl:text-left gap-6 max-w-2xl md:max-w-3xl xl:max-w-7xl md:mx-auto xl:mx-0" data-aos="fade-up">
          <div class="max-w-2xl">
            <span class="text-xs uppercase font-bold tracking-widest text-bronze block mb-2">Category 01</span>
            <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight">
              UPVC Windows Collection
            </h2>
          </div>
          <p class="text-charcoal/70 dark:text-stone-300 text-sm max-w-md md:max-w-xl xl:max-w-md">
            Custom engineered across 8 distinct architectural opening configurations to suit contemporary facades, high-rise apartments, and luxury villas.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 items-stretch">
          <!-- 1. Casement Windows -->
          <div id="casement-windows" class="group rounded-2xl overflow-hidden bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm hover:shadow-xl transition-all flex flex-col h-full" data-aos="fade-up">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1509644851169-2acc08aa25b5?auto=format&fit=crop&w=700&q=80" 
                   alt="Casement Windows in modern home" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div class="space-y-2">
                <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Side-Hung / Top-Hung</span>
                <h3 class="font-display text-base xl:text-lg font-bold text-charcoal dark:text-white whitespace-nowrap">Casement Windows</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 line-clamp-3">
                  Classic 90° swinging sashes engineered with triple compression gaskets for unbeatable wind and monsoon driving-rain sealing.
                </p>
              </div>
              <div class="pt-3 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="contact.html?product=Casement+Windows#measurement-booking" class="text-xs font-bold text-bronze hover:underline">Enquire Now</a>
                <span class="text-[11px] text-charcoal/50 dark:text-stone-400 font-mono">Series 70mm</span>
              </div>
            </div>
          </div>

          <!-- 2. Sliding Windows -->
          <div id="sliding-windows" class="group rounded-2xl overflow-hidden bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm hover:shadow-xl transition-all flex flex-col h-full" data-aos="fade-up" data-aos-delay="50">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?auto=format&fit=crop&w=700&q=80" 
                   alt="Sliding Windows in luxury estate" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div class="space-y-2">
                <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">2, 3 & 4 Track</span>
                <h3 class="font-display text-base xl:text-lg font-bold text-charcoal dark:text-white whitespace-nowrap">Sliding Windows</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 line-clamp-3">
                  Space-efficient horizontal gliding with heavy-duty tandem stainless steel rollers and built-in anti-lift security blocks.
                </p>
              </div>
              <div class="pt-3 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="contact.html?product=Sliding+Windows#measurement-booking" class="text-xs font-bold text-bronze hover:underline">Enquire Now</a>
                <span class="text-[11px] text-charcoal/50 dark:text-stone-400 font-mono">Series 88mm</span>
              </div>
            </div>
          </div>

          <!-- 3. Tilt and Turn Windows -->
          <div id="tilt-turn-windows" class="group rounded-2xl overflow-hidden bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm hover:shadow-xl transition-all flex flex-col h-full" data-aos="fade-up" data-aos-delay="100">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?auto=format&fit=crop&w=700&q=80" 
                   alt="Tilt and Turn European window" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div class="space-y-2">
                <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Dual Opening Mode</span>
                <h3 class="font-display text-base xl:text-lg font-bold text-charcoal dark:text-white whitespace-nowrap">Tilt & Turn Windows</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 line-clamp-3">
                  European dual-action hardware allows micro-ventilation from the top or swings wide inward for effortless cleaning from inside.
                </p>
              </div>
              <div class="pt-3 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="contact.html?product=Tilt+and+Turn#measurement-booking" class="text-xs font-bold text-bronze hover:underline">Enquire Now</a>
                <span class="text-[11px] text-charcoal/50 dark:text-stone-400 font-mono">Series 76mm</span>
              </div>
            </div>
          </div>

          <!-- 4. Fixed Windows -->
          <div id="fixed-panoramic" class="group rounded-2xl overflow-hidden bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm hover:shadow-xl transition-all flex flex-col h-full" data-aos="fade-up" data-aos-delay="150">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1519710164239-da123dc03ef4?auto=format&fit=crop&w=700&q=80" 
                   alt="Fixed architectural picture windows" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div class="space-y-2">
                <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Picture Frame Glass</span>
                <h3 class="font-display text-base xl:text-lg font-bold text-charcoal dark:text-white whitespace-nowrap">Fixed Windows</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 line-clamp-3">
                  Ultra-slim sightline frames designed to maximize natural daylight admission while sealing 100% against air infiltration.
                </p>
              </div>
              <div class="pt-3 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="contact.html?product=Fixed+Windows#measurement-booking" class="text-xs font-bold text-bronze hover:underline">Enquire Now</a>
                <span class="text-[11px] text-charcoal/50 dark:text-stone-400 font-mono">Series 60mm</span>
              </div>
            </div>
          </div>

          <!-- 5. Combination Windows -->
          <div id="combination-windows" class="group rounded-2xl overflow-hidden bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm hover:shadow-xl transition-all flex flex-col h-full" data-aos="fade-up" data-aos-delay="200">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1544984243-ec57ea16fe25?auto=format&fit=crop&w=700&q=80" 
                   alt="Combination window setup with fixed and casement" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div class="space-y-2">
                <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Modular Composite</span>
                <h3 class="font-display text-base xl:text-lg font-bold text-charcoal dark:text-white whitespace-nowrap">Combo Windows</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 line-clamp-3">
                  Seamlessly couple fixed panorama picture panes with operable casements, awnings, or sliders into a unified structural frame.
                </p>
              </div>
              <div class="pt-3 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="contact.html?product=Combination+Windows#measurement-booking" class="text-xs font-bold text-bronze hover:underline">Enquire Now</a>
                <span class="text-[11px] text-charcoal/50 dark:text-stone-400 font-mono">Custom Coupled</span>
              </div>
            </div>
          </div>

          <!-- 6. Bay Windows -->
          <div id="bay-windows" class="group rounded-2xl overflow-hidden bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm hover:shadow-xl transition-all flex flex-col h-full" data-aos="fade-up" data-aos-delay="250">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1512915922686-57c11dde9b6b?auto=format&fit=crop&w=700&q=80" 
                   alt="Architectural bay window nook" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div class="space-y-2">
                <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Cantilever 90° - 150°</span>
                <h3 class="font-display text-base xl:text-lg font-bold text-charcoal dark:text-white whitespace-nowrap">Bay Windows</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 line-clamp-3">
                  Projects outward from exterior walls to form inviting seating alcoves with panoramic three-directional viewing and sunlight.
                </p>
              </div>
              <div class="pt-3 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="contact.html?product=Bay+Windows#measurement-booking" class="text-xs font-bold text-bronze hover:underline">Enquire Now</a>
                <span class="text-[11px] text-charcoal/50 dark:text-stone-400 font-mono">Structural Post</span>
              </div>
            </div>
          </div>

          <!-- 7. Top Hung Windows -->
          <div id="tophung-windows" class="group rounded-2xl overflow-hidden bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm hover:shadow-xl transition-all flex flex-col h-full" data-aos="fade-up" data-aos-delay="300">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=700&q=80" 
                   alt="Top hung awning bathroom and kitchen window" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div class="space-y-2">
                <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Awning Ventilation</span>
                <h3 class="font-display text-base xl:text-lg font-bold text-charcoal dark:text-white whitespace-nowrap">Top Hung Windows</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 line-clamp-3">
                  Sash hinges at the top and swings outward from the base, permitting continuous indoor fresh air ventilation even during rain showers.
                </p>
              </div>
              <div class="pt-3 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="contact.html?product=Top+Hung#measurement-booking" class="text-xs font-bold text-bronze hover:underline">Enquire Now</a>
                <span class="text-[11px] text-charcoal/50 dark:text-stone-400 font-mono">Heavy Stay 304</span>
              </div>
            </div>
          </div>

          <!-- 8. Arch Windows -->
          <div id="arch-windows" class="group rounded-2xl overflow-hidden bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm hover:shadow-xl transition-all flex flex-col h-full" data-aos="fade-up" data-aos-delay="350">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1516455590571-18256e5bb9ff?auto=format&fit=crop&w=700&q=80" 
                   alt="Curved and arch UPVC window system" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div class="space-y-2">
                <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Thermo-Bent Profile</span>
                <h3 class="font-display text-base xl:text-lg font-bold text-charcoal dark:text-white whitespace-nowrap">Arch Windows</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 line-clamp-3">
                  Crafted using computerized hot oil immersion profile bending to execute graceful semi-circular, gothic, and segmental arches.
                </p>
              </div>
              <div class="pt-3 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="contact.html?product=Arch+Windows#measurement-booking" class="text-xs font-bold text-bronze hover:underline">Enquire Now</a>
                <span class="text-[11px] text-charcoal/50 dark:text-stone-400 font-mono">CNC Bending</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: UPVC DOORS COLLECTION (7 Specific Types) -->
    <section id="doors-collection" class="py-24 px-4 sm:px-8 bg-white dark:bg-[#182029] border-y border-charcoal/10 dark:border-white/10">
      <div class="max-w-7xl mx-auto space-y-16">
        <div class="flex flex-col md:items-center xl:flex-row xl:items-end justify-between md:text-center xl:text-left gap-6 max-w-2xl md:max-w-3xl xl:max-w-7xl md:mx-auto xl:mx-0" data-aos="fade-up">
          <div class="max-w-2xl">
            <span class="text-xs uppercase font-bold tracking-widest text-bronze block mb-2">Category 02</span>
            <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight">
              UPVC Doors Collection
            </h2>
          </div>
          <p class="text-charcoal/70 dark:text-stone-300 text-sm max-w-md md:max-w-xl xl:max-w-md">
            Heavy-gauge reinforced door leaves with reinforced steel corner couplers designed for security, thermal insulation, and seamless traffic.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 items-stretch">
          <!-- 1. Sliding Doors -->
          <div id="sliding-doors" class="group rounded-2xl overflow-hidden bg-ivory dark:bg-[#12181F] border border-charcoal/10 dark:border-white/10 shadow-sm hover:shadow-xl transition-all flex flex-col h-full" data-aos="fade-up">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?auto=format&fit=crop&w=700&q=80" 
                   alt="Multi-track sliding UPVC patio doors" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div class="space-y-2">
                <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Expansive Apertures</span>
                <h3 class="font-display text-base xl:text-lg font-bold text-charcoal dark:text-white whitespace-nowrap">Sliding Doors</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 line-clamp-3">
                  Smooth gliding across stainless steel monorails or multi-rails with flush low-threshold options for zero-barrier living.
                </p>
              </div>
              <div class="pt-3 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="contact.html?product=Sliding+Doors#measurement-booking" class="text-xs font-bold text-bronze hover:underline">Enquire Now</a>
                <span class="text-[11px] text-charcoal/50 dark:text-stone-400 font-mono">Multi-Rail</span>
              </div>
            </div>
          </div>

          <!-- 2. French Doors -->
          <div id="french-doors" class="group rounded-2xl overflow-hidden bg-ivory dark:bg-[#12181F] border border-charcoal/10 dark:border-white/10 shadow-sm hover:shadow-xl transition-all flex flex-col h-full" data-aos="fade-up" data-aos-delay="50">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1513584684374-8bab748fbf90?auto=format&fit=crop&w=700&q=80" 
                   alt="French UPVC Doors opening to garden" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div class="space-y-2">
                <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Dual Leaf Opening</span>
                <h3 class="font-display text-base xl:text-lg font-bold text-charcoal dark:text-white whitespace-nowrap">French Doors</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 line-clamp-3">
                  Double leaf configuration with flying mullion, granting a completely clear entrance with no fixed central post in your way.
                </p>
              </div>
              <div class="pt-3 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="contact.html?product=French+Doors#measurement-booking" class="text-xs font-bold text-bronze hover:underline">Enquire Now</a>
                <span class="text-[11px] text-charcoal/50 dark:text-stone-400 font-mono">Master/Slave</span>
              </div>
            </div>
          </div>

          <!-- 3. Casement Doors -->
          <div id="casement-doors" class="group rounded-2xl overflow-hidden bg-ivory dark:bg-[#12181F] border border-charcoal/10 dark:border-white/10 shadow-sm hover:shadow-xl transition-all flex flex-col h-full" data-aos="fade-up" data-aos-delay="100">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1493809842364-78817add7ffb?auto=format&fit=crop&w=700&q=80" 
                   alt="Casement single-leaf glass door" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div class="space-y-2">
                <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Single-Leaf Utility</span>
                <h3 class="font-display text-base xl:text-lg font-bold text-charcoal dark:text-white whitespace-nowrap">Casement Doors</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 line-clamp-3">
                  Side-hung inward or outward swinging heavy-duty profile sashes with 3D adjustable security flag hinges and weather seals.
                </p>
              </div>
              <div class="pt-3 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="contact.html?product=Casement+Doors#measurement-booking" class="text-xs font-bold text-bronze hover:underline">Enquire Now</a>
                <span class="text-[11px] text-charcoal/50 dark:text-stone-400 font-mono">Heavy Duty</span>
              </div>
            </div>
          </div>

          <!-- 4. Entrance Doors -->
          <div id="entrance-doors" class="group rounded-2xl overflow-hidden bg-ivory dark:bg-[#12181F] border border-charcoal/10 dark:border-white/10 shadow-sm hover:shadow-xl transition-all flex flex-col h-full" data-aos="fade-up" data-aos-delay="150">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1517581177682-a085bb7ffb15?auto=format&fit=crop&w=700&q=80" 
                   alt="High-security main entrance door" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div class="space-y-2">
                <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Anti-Intruder RC3</span>
                <h3 class="font-display text-base xl:text-lg font-bold text-charcoal dark:text-white whitespace-nowrap">Entrance Doors</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 line-clamp-3">
                  Solid polyurethane insulated panel core coupled with architectural glass insets and 5-point motorized hook deadbolt locking.
                </p>
              </div>
              <div class="pt-3 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="contact.html?product=Entrance+Doors#measurement-booking" class="text-xs font-bold text-bronze hover:underline">Enquire Now</a>
                <span class="text-[11px] text-charcoal/50 dark:text-stone-400 font-mono">Reinforced Box</span>
              </div>
            </div>
          </div>

          <!-- 5. Folding / Bi-Fold Doors -->
          <div id="folding-bifold" class="group rounded-2xl overflow-hidden bg-ivory dark:bg-[#12181F] border border-charcoal/10 dark:border-white/10 shadow-sm hover:shadow-xl transition-all flex flex-col h-full" data-aos="fade-up" data-aos-delay="200">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=700&q=80" 
                   alt="Concertina Bi-Fold doors in modern patio" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div class="space-y-2">
                <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Concertina Stacking</span>
                <h3 class="font-display text-base xl:text-lg font-bold text-charcoal dark:text-white whitespace-nowrap">Bi-Fold Doors</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 line-clamp-3">
                  Folds and stacks 3 to 7 panels effortlessly away to reveal 90% of your aperture for unimpeded poolside entertaining.
                </p>
              </div>
              <div class="pt-3 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="contact.html?product=BiFold+Doors#measurement-booking" class="text-xs font-bold text-bronze hover:underline">Enquire Now</a>
                <span class="text-[11px] text-charcoal/50 dark:text-stone-400 font-mono">Concertina 7-Leaf</span>
              </div>
            </div>
          </div>

          <!-- 6. Lift and Slide Doors -->
          <div id="lift-slide" class="group rounded-2xl overflow-hidden bg-ivory dark:bg-[#12181F] border border-charcoal/10 dark:border-white/10 shadow-sm hover:shadow-xl transition-all flex flex-col h-full" data-aos="fade-up" data-aos-delay="250">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=700&q=80" 
                   alt="Heavy architectural lift and slide doors" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div class="space-y-2">
                <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Heavy Sash 400kg</span>
                <h3 class="font-display text-base xl:text-lg font-bold text-charcoal dark:text-white whitespace-nowrap">Lift & Slide Doors</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 line-clamp-3">
                  Rotating handle mechanically elevates the sash off weather seals for friction-free movement, locking down hermetically when closed.
                </p>
              </div>
              <div class="pt-3 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="contact.html?product=Lift+and+Slide#measurement-booking" class="text-xs font-bold text-bronze hover:underline">Enquire Now</a>
                <span class="text-[11px] text-charcoal/50 dark:text-stone-400 font-mono">Series 170mm</span>
              </div>
            </div>
          </div>

          <!-- 7. Balcony Doors -->
          <div id="balcony-doors" class="md:col-span-2 md:w-[calc(50%-0.75rem)] md:mx-auto lg:col-span-1 lg:w-full lg:mx-0 group rounded-2xl overflow-hidden bg-ivory dark:bg-[#12181F] border border-charcoal/10 dark:border-white/10 shadow-sm hover:shadow-xl transition-all flex flex-col h-full" data-aos="fade-up" data-aos-delay="300">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1507652313519-d4e9174996dd?auto=format&fit=crop&w=700&q=80" 
                   alt="Balcony glass terrace door" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div class="space-y-2">
                <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Terrace Access</span>
                <h3 class="font-display text-base xl:text-lg font-bold text-charcoal dark:text-white whitespace-nowrap">Balcony Doors</h3>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 line-clamp-3">
                  Integrated tilt ventilation feature allows refreshing breeze into high-rise bedrooms while locking securely against intruders.
                </p>
              </div>
              <div class="pt-3 mt-auto border-t border-charcoal/10 dark:border-white/10 flex items-center justify-between">
                <a href="contact.html?product=Balcony+Doors#measurement-booking" class="text-xs font-bold text-bronze hover:underline">Enquire Now</a>
                <span class="text-[11px] text-charcoal/50 dark:text-stone-400 font-mono">Tilt-First Action</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4: PRODUCT FEATURES & CUSTOMIZATION -->
    <section id="customization-features" class="py-24 px-4 sm:px-8 bg-ivory dark:bg-[#12181F] architectural-grid">
      <div class="max-w-7xl mx-auto space-y-16">
        <div class="text-center max-w-3xl mx-auto" data-aos="fade-up">
          <span class="text-xs uppercase font-bold tracking-widest text-bronze block mb-2">Bespoke Engineering</span>
          <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight">
            Features & Architectural Customization
          </h2>
          <p class="text-charcoal/70 dark:text-stone-300 text-sm mt-3">
            Every millimeter of profile, glass composition, finish foil, and locking mechanism is customizable to match your project's architectural language.
          </p>
        </div>

        <!-- 6 Customization Pillars -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 items-stretch">
          <!-- 1. Glass Options & Glazing -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm flex flex-col justify-between h-full space-y-4" data-aos="fade-up">
            <div class="space-y-4">
              <div class="w-12 h-12 rounded-2xl bg-bronze/15 text-bronze flex items-center justify-center">
                <i data-lucide="sun" class="w-6 h-6"></i>
              </div>
              <h3 class="font-display text-xl font-bold text-charcoal dark:text-white leading-snug min-h-[3.25rem] flex items-center">
                <span>Glass Options &<br class="hidden sm:inline"> Glazing</span>
              </h3>
              <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                Double and triple insulated glass units (IGU) with argon gas fills, Saint-Gobain Low-E reflective coatings, frosted privacy satin, and acoustic PVB lamination.
              </p>
            </div>
            <div class="text-[11px] font-mono text-bronze mt-auto pt-3 border-t border-charcoal/10 dark:border-white/10">Options: 24mm, 32mm, 44mm Triple</div>
          </div>

          <!-- 2. Frame Colours & Finishes -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm flex flex-col justify-between h-full space-y-4" data-aos="fade-up" data-aos-delay="100">
            <div class="space-y-4">
              <div class="w-12 h-12 rounded-2xl bg-bronze/15 text-bronze flex items-center justify-center">
                <i data-lucide="palette" class="w-6 h-6"></i>
              </div>
              <h3 class="font-display text-xl font-bold text-charcoal dark:text-white leading-snug min-h-[3.25rem] flex items-center">
                <span>Colours &<br class="hidden sm:inline"> Architectural Foils</span>
              </h3>
              <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                German Renolit exterior foils with cool-colors technology that deflect 80% solar heat: Anthracite Grey, Jet Black, Golden Oak, Walnut, and Natural White.
              </p>
            </div>
            <div class="text-[11px] font-mono text-bronze mt-auto pt-3 border-t border-charcoal/10 dark:border-white/10">18 Standard + Custom RAL Foils</div>
          </div>

          <!-- 3. Hardware & Locking Systems -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm flex flex-col justify-between h-full space-y-4" data-aos="fade-up" data-aos-delay="200">
            <div class="space-y-4">
              <div class="w-12 h-12 rounded-2xl bg-bronze/15 text-bronze flex items-center justify-center">
                <i data-lucide="key" class="w-6 h-6"></i>
              </div>
              <h3 class="font-display text-xl font-bold text-charcoal dark:text-white leading-snug min-h-[3.25rem] flex items-center">
                <span>German Certified<br class="hidden sm:inline"> Hardware</span>
              </h3>
              <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                Maco & Roto genuine hardware with corrosion-resistant nano-coatings, concealed flush hinges, key-lockable designer handles, and magnetic child-safety restrictors.
              </p>
            </div>
            <div class="text-[11px] font-mono text-bronze mt-auto pt-3 border-t border-charcoal/10 dark:border-white/10">Rated 25,000 Cycle Testing</div>
          </div>

          <!-- 4. Multi-Point Locking -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm flex flex-col justify-between h-full space-y-4" data-aos="fade-up" data-aos-delay="300">
            <div class="space-y-4">
              <div class="w-12 h-12 rounded-2xl bg-bronze/15 text-bronze flex items-center justify-center">
                <i data-lucide="shield-check" class="w-6 h-6"></i>
              </div>
              <h3 class="font-display text-xl font-bold text-charcoal dark:text-white leading-snug min-h-[3.25rem] flex items-center">
                <span>Multi-Point Locking<br class="hidden sm:inline"> Security</span>
              </h3>
              <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                Continuous perimeter mushroom cams and steel strike plates lock the sash at 4 to 8 individual anchor locations simultaneously with a single handle turn.
              </p>
            </div>
            <div class="text-[11px] font-mono text-bronze mt-auto pt-3 border-t border-charcoal/10 dark:border-white/10">Burglar Resistance Grade RC2/RC3</div>
          </div>

          <!-- 5. Custom Sizes & Configurations -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm flex flex-col justify-between h-full space-y-4" data-aos="fade-up" data-aos-delay="400">
            <div class="space-y-4">
              <div class="w-12 h-12 rounded-2xl bg-bronze/15 text-bronze flex items-center justify-center">
                <i data-lucide="maximize" class="w-6 h-6"></i>
              </div>
              <h3 class="font-display text-xl font-bold text-charcoal dark:text-white leading-snug min-h-[3.25rem] flex items-center">
                <span>Bespoke Millimeter<br class="hidden sm:inline"> Sizing</span>
              </h3>
              <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                No stock standard limitations. Sashes are custom fabricated to exact millimeter measurements for seamless architectural fitment in new builds or retrofits.
              </p>
            </div>
            <div class="text-[11px] font-mono text-bronze mt-auto pt-3 border-t border-charcoal/10 dark:border-white/10">Apertures up to 3.2m Height</div>
          </div>

          <!-- 6. Thermal & Acoustic Insulation -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm flex flex-col justify-between h-full space-y-4" data-aos="fade-up" data-aos-delay="500">
            <div class="space-y-4">
              <div class="w-12 h-12 rounded-2xl bg-bronze/15 text-bronze flex items-center justify-center">
                <i data-lucide="volume-x" class="w-6 h-6"></i>
              </div>
              <h3 class="font-display text-xl font-bold text-charcoal dark:text-white leading-snug min-h-[3.25rem] flex items-center">
                <span>Thermal & Acoustic<br class="hidden sm:inline"> Insulation</span>
              </h3>
              <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                Multi-chamber internal chambers act as natural air pockets, preventing heat conduction and dampening external noise by up to 45 decibels.
              </p>
            </div>
            <div class="text-[11px] font-mono text-bronze mt-auto pt-3 border-t border-charcoal/10 dark:border-white/10">U-Value down to 0.78 W/m²K</div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: PRODUCT ENQUIRY CTA WITH CONSULTATION & MEASUREMENT BOOKING -->
    <section class="py-24 px-4 sm:px-8 bg-charcoal text-white relative overflow-hidden">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          <div class="lg:col-span-7 space-y-6" data-aos="fade-right">
            <span class="text-xs uppercase font-bold tracking-widest text-bronze font-mono">Direct Factory Booking</span>
            <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-white tracking-tight leading-tight">
              Ready to Order Custom UPVC Profiles For Your Home?
            </h2>
            <p class="text-sm text-stone-300 leading-relaxed max-w-xl">
              Book a free on-site digital laser measurement appointment with a VISTRAL senior fenestration engineer. We bring actual profile cross-sections, glass tint samples, and provide itemized quotations.
            </p>
            <div class="pt-2 flex flex-col sm:flex-row items-stretch sm:items-center gap-3 xl:gap-4">
              <a href="contact.html#measurement-booking" class="w-full sm:w-auto bronze-gradient-btn px-6 py-3.5 xl:px-8 xl:py-4 rounded-xl text-xs uppercase font-bold tracking-wider inline-flex items-center justify-center space-x-2 rtl:space-x-reverse shadow-xl">
                <span>Book Free Measurement</span>
                <i data-lucide="calendar" class="w-4 h-4"></i>
              </a>
              <a href="gallery.html" class="w-full sm:w-auto px-6 py-3.5 xl:px-8 xl:py-4 rounded-xl text-xs uppercase font-bold tracking-wider bg-white/10 hover:bg-white/20 border border-white/20 text-white inline-flex items-center justify-center space-x-2 rtl:space-x-reverse transition-all">
                <span>View Installed Projects</span>
                <i data-lucide="arrow-right" class="w-4 h-4 icon-flip"></i>
              </a>
            </div>
          </div>

          <div class="lg:col-span-5 p-8 rounded-3xl bg-white/5 border border-white/10 space-y-4" data-aos="fade-left">
            <h3 class="font-display text-xl font-bold text-white">What You Receive:</h3>
            <ul class="text-xs space-y-3 text-stone-300">
              <li class="flex items-start space-x-2 rtl:space-x-reverse">
                <i data-lucide="check-circle" class="w-4 h-4 text-bronze mt-0.5 flex-shrink-0"></i>
                <span>Complimentary 3D laser aperture survey across all openings.</span>
              </li>
              <li class="flex items-start space-x-2 rtl:space-x-reverse">
                <i data-lucide="check-circle" class="w-4 h-4 text-bronze mt-0.5 flex-shrink-0"></i>
                <span>Thermal U-value and acoustic calculation report for your floorplan.</span>
              </li>
              <li class="flex items-start space-x-2 rtl:space-x-reverse">
                <i data-lucide="check-circle" class="w-4 h-4 text-bronze mt-0.5 flex-shrink-0"></i>
                <span>Physical profile and glass sample presentation at your site.</span>
              </li>
              <li class="flex items-start space-x-2 rtl:space-x-reverse">
                <i data-lucide="check-circle" class="w-4 h-4 text-bronze mt-0.5 flex-shrink-0"></i>
                <span>Fixed-price itemized estimate guaranteed for 60 days.</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  </main>
"""
    content += get_footer()
    
    with open("products.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("products.html (Products - exactly 5 sections) generated successfully.")

if __name__ == "__main__":
    build_products()

