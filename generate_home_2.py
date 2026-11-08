import os
from templates import get_head, get_header, get_footer

def build_home_2():
    content = get_head("Home 2 - Architectural Edition", "home2")
    content += get_header("home2")
    content += """
  <main class="flex-grow">
    <!-- SECTION 1: ARCHITECTURAL SPLIT-SCREEN HERO -->
    <section class="min-h-[92vh] flex flex-col lg:flex-row bg-charcoal text-white overflow-hidden relative">
      <!-- Left Screen: Editorial Typography & Value Proposition -->
      <div class="lg:w-1/2 p-8 sm:p-16 lg:p-20 flex flex-col justify-center space-y-8 z-10" data-aos="fade-right">
        <div class="inline-flex items-center space-x-2 rtl:space-x-reverse px-3.5 py-1.5 rounded-full bg-white/10 border border-white/20 w-fit">
          <span class="w-2 h-2 rounded-full bg-bronze"></span>
          <span class="text-xs uppercase tracking-widest text-bronze-200 font-mono font-semibold">Architectural Edition 2026</span>
        </div>

        <h1 class="font-display font-extrabold text-4xl sm:text-6xl tracking-tight leading-[1.08] text-white">
          Where Structural Precision Meets <span class="text-transparent bg-clip-text bg-gradient-to-r from-bronze-200 to-bronze">Pure Panorama</span>.
        </h1>

        <p class="text-sm sm:text-base text-stone-300 max-w-lg leading-relaxed">
          Pioneering next-generation UPVC thermal engineering. We fabricate custom architectural glazed fenestrations that maximize natural light while insulating against ambient urban noise.
        </p>

        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4 pt-2">
          <a href="#interactive-styles" class="w-full sm:w-auto bronze-gradient-btn px-7 py-3.5 rounded-xl text-xs uppercase font-bold tracking-wider inline-flex items-center justify-center space-x-2 rtl:space-x-reverse">
            <span>Explore Window Styles</span>
            <i data-lucide="arrow-down" class="w-4 h-4"></i>
          </a>
          <a href="contact.html#measurement-booking" class="w-full sm:w-auto px-7 py-3.5 rounded-xl text-xs uppercase font-bold tracking-wider bg-white/10 hover:bg-white/20 border border-white/20 text-white inline-flex items-center justify-center space-x-2 rtl:space-x-reverse transition-all">
            <span>Schedule Laser Audit</span>
            <i data-lucide="calendar" class="w-4 h-4 text-bronze"></i>
          </a>
        </div>

        <!-- Metric Ticker -->
        <div class="grid grid-cols-3 gap-6 pt-6 border-t border-white/15">
          <div>
            <div class="text-2xl sm:text-3xl font-display font-bold text-bronze-200" data-counter="50" data-suffix="yr+">0</div>
            <div class="text-[11px] text-stone-400 uppercase font-mono mt-0.5">Profile Life</div>
          </div>
          <div>
            <div class="text-2xl sm:text-3xl font-display font-bold text-bronze-200" data-counter="100" data-suffix="%">0</div>
            <div class="text-[11px] text-stone-400 uppercase font-mono mt-0.5">Water Tightness</div>
          </div>
          <div>
            <div class="text-2xl sm:text-3xl font-display font-bold text-bronze-200" data-counter="45" data-suffix="dB">0</div>
            <div class="text-[11px] text-stone-400 uppercase font-mono mt-0.5">Noise Shield</div>
          </div>
        </div>
      </div>

      <!-- Right Screen: Architectural Split Imagery with Hover Peek -->
      <div class="lg:w-1/2 relative min-h-[450px] lg:min-h-full grid grid-cols-2 gap-2 p-2 bg-charcoal-light">
        <div class="relative overflow-hidden group h-full">
          <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80" 
               alt="Cantilever modern villa with UPVC fenestrations" 
               class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-1000">
          <div class="absolute bottom-4 left-4 right-4 bg-charcoal/80 backdrop-blur-md p-3 rounded-xl border border-white/10 text-xs">
            <span class="text-bronze font-mono font-bold block text-[10px] uppercase">Exterior Facade</span>
            <span class="font-bold text-white">Triple Glazed Sashes</span>
          </div>
        </div>
        <div class="relative overflow-hidden group h-full">
          <img src="https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?auto=format&fit=crop&w=1200&q=80" 
               alt="Interior minimalist view through UPVC panoramic frame" 
               class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-1000">
          <div class="absolute bottom-4 left-4 right-4 bg-charcoal/80 backdrop-blur-md p-3 rounded-xl border border-white/10 text-xs">
            <span class="text-bronze font-mono font-bold block text-[10px] uppercase">Interior Ambience</span>
            <span class="font-bold text-white">Flush Concealed Hinges</span>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2: COMPANY INTRODUCTION WITH STATISTICS & CREATIVE IMAGE COMPOSITION -->
    <section class="py-24 px-4 sm:px-8 bg-ivory dark:bg-[#12181F]">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          <!-- Creative Image Composition -->
          <div class="lg:col-span-6 relative" data-aos="fade-right">
            <div class="rounded-3xl overflow-hidden shadow-2xl border border-charcoal/10 dark:border-white/10 aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1600573472592-401b489a3cdc?auto=format&fit=crop&w=1000&q=80" 
                   alt="Modern structural glass corner with UPVC mullions" 
                   class="w-full h-full object-cover">
            </div>

            <!-- Overlapping Floating Stat Badge -->
            <div class="absolute -bottom-8 right-6 bg-white dark:bg-[#182029] p-6 rounded-2xl shadow-2xl border border-bronze/30 max-w-xs text-charcoal dark:text-white" data-aos="zoom-in" data-aos-delay="200">
              <div class="flex items-center space-x-3 rtl:space-x-reverse mb-2">
                <i data-lucide="award" class="w-6 h-6 text-bronze"></i>
                <span class="text-xs uppercase font-bold tracking-wider font-mono">Certified Fabricator</span>
              </div>
              <p class="text-xs text-charcoal/70 dark:text-stone-300">
                Authorized German profile processor adhering to EN 12608 European polymer durability benchmarks.
              </p>
            </div>
          </div>

          <!-- Narrative and Counters -->
          <div class="lg:col-span-6 space-y-6" data-aos="fade-left">
            <div class="flex items-center space-x-2 rtl:space-x-reverse">
              <span class="w-6 h-0.5 bg-bronze"></span>
              <span class="text-xs uppercase font-bold tracking-widest text-bronze">About VISTRAL</span>
            </div>

            <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight leading-tight">
              28 Years of Crafting Fenestration Excellence
            </h2>

            <p class="text-sm sm:text-base text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Founded by architectural facade engineers, VISTRAL transforms architectural blueprints into living masterpieces. We synthesize heavy galvanized reinforcement, virgin UPVC profiles, and precision German hardware to create windows that endure extreme climates while maintaining whisper-quiet interiors.
            </p>

            <!-- 4 Distinct Animated Statistic Tiles -->
            <div class="grid grid-cols-2 gap-6 pt-4">
              <div class="p-5 rounded-2xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm">
                <span class="block text-3xl font-display font-extrabold text-bronze" data-counter="45000" data-suffix="+">0</span>
                <span class="text-xs font-semibold text-charcoal/80 dark:text-stone-300 uppercase tracking-wider mt-1 block">Units Fabricated</span>
              </div>
              <div class="p-5 rounded-2xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm">
                <span class="block text-3xl font-display font-extrabold text-bronze" data-counter="1800" data-suffix="+">0</span>
                <span class="text-xs font-semibold text-charcoal/80 dark:text-stone-300 uppercase tracking-wider mt-1 block">Luxury Villas Completed</span>
              </div>
              <div class="p-5 rounded-2xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm">
                <span class="block text-3xl font-display font-extrabold text-bronze" data-counter="99" data-suffix="%">0</span>
                <span class="text-xs font-semibold text-charcoal/80 dark:text-stone-300 uppercase tracking-wider mt-1 block">Client Recommendation</span>
              </div>
              <div class="p-5 rounded-2xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm">
                <span class="block text-3xl font-display font-extrabold text-bronze" data-counter="20" data-suffix=" Years">0</span>
                <span class="text-xs font-semibold text-charcoal/80 dark:text-stone-300 uppercase tracking-wider mt-1 block">Full System Warranty</span>
              </div>
            </div>

            <div class="pt-2">
              <a href="about.html" class="inline-flex items-center space-x-2 text-xs uppercase font-bold tracking-wider text-bronze hover:underline rtl:space-x-reverse">
                <span>Read Our Manufacturing Heritage</span>
                <i data-lucide="arrow-right" class="w-4 h-4 icon-flip"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: EXPLORE UPVC WINDOW STYLES (INTERACTIVE PRODUCT SHOWCASE) -->
    <section id="interactive-styles" class="py-24 px-4 sm:px-8 bg-white dark:bg-[#182029] border-y border-charcoal/10 dark:border-white/10">
      <div class="max-w-7xl mx-auto">
        <div class="text-center max-w-3xl mx-auto mb-12" data-aos="fade-up">
          <span class="text-xs uppercase font-bold tracking-widest text-bronze block mb-2">Interactive Showcase</span>
          <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight">
            Explore UPVC Window Styles
          </h2>
          <p class="text-charcoal/70 dark:text-stone-300 text-sm mt-3">
            Select an architectural style below to view its functional characteristics, profile cross-section, and ideal home placement.
          </p>
        </div>

        <!-- Interactive Style Switcher Tabs -->
        <div class="flex flex-wrap items-center justify-center gap-3 mb-12" data-aos="fade-up">
          <button class="style-tab-btn active px-5 py-2.5 rounded-full border-2 border-bronze text-bronze font-bold text-xs uppercase tracking-wider transition-all" data-target="tab-casement">
            Casement Windows
          </button>
          <button class="style-tab-btn px-5 py-2.5 rounded-full border-2 border-transparent text-charcoal/70 dark:text-stone-300 hover:border-charcoal/20 font-bold text-xs uppercase tracking-wider transition-all" data-target="tab-sliding">
            Sliding Windows
          </button>
          <button class="style-tab-btn px-5 py-2.5 rounded-full border-2 border-transparent text-charcoal/70 dark:text-stone-300 hover:border-charcoal/20 font-bold text-xs uppercase tracking-wider transition-all" data-target="tab-fixed">
            Fixed Picture Glazing
          </button>
        </div>

        <!-- Tab Pane 1: Casement -->
        <div id="tab-casement" class="style-tab-pane grid grid-cols-1 lg:grid-cols-12 gap-8 items-center bg-ivory dark:bg-[#12181F] p-8 sm:p-12 rounded-3xl border border-charcoal/10 dark:border-white/10">
          <div class="lg:col-span-7 img-zoom-wrapper rounded-2xl overflow-hidden aspect-[16/10] shadow-lg">
            <img src="https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=1200&q=80" 
                 alt="Casement Window in modern architecture" 
                 class="w-full h-full object-cover">
          </div>
          <div class="lg:col-span-5 space-y-4">
            <span class="text-xs font-mono font-bold text-bronze uppercase">Series 70mm High-Performance</span>
            <h3 class="font-display text-2xl font-bold text-charcoal dark:text-white">Side-Hung Architectural Casement</h3>
            <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Designed with 90-degree opening angles for unhindered airflow and effortless exterior glass cleaning. Outfitted with stainless steel friction hinges that keep the window solidly stationed even in stiff breezes.
            </p>
            <ul class="text-xs space-y-2 text-charcoal/80 dark:text-stone-200">
              <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-2 rtl:ml-2"></i> Multi-point locking pins around full perimeter</li>
              <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-2 rtl:ml-2"></i> Concealed drainage channels with exterior caps</li>
              <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-2 rtl:ml-2"></i> Accommodates glass thicknesses up to 36mm</li>
            </ul>
            <div class="pt-2">
              <a href="products.html#casement-windows" class="bronze-gradient-btn px-5 py-2.5 rounded-lg text-xs uppercase font-bold tracking-wider inline-flex items-center space-x-2 rtl:space-x-reverse">
                <span>View Full Dimensions</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 icon-flip"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Tab Pane 2: Sliding (Hidden by default) -->
        <div id="tab-sliding" class="style-tab-pane hidden grid-cols-1 lg:grid-cols-12 gap-8 items-center bg-ivory dark:bg-[#12181F] p-8 sm:p-12 rounded-3xl border border-charcoal/10 dark:border-white/10">
          <div class="lg:col-span-7 img-zoom-wrapper rounded-2xl overflow-hidden aspect-[16/10] shadow-lg">
            <img src="https://images.unsplash.com/photo-1507089947368-19c1da9775ae?auto=format&fit=crop&w=1200&q=80" 
                 alt="Smooth Sliding UPVC Window system" 
                 class="w-full h-full object-cover">
          </div>
          <div class="lg:col-span-5 space-y-4">
            <span class="text-xs font-mono font-bold text-bronze uppercase">Series 88mm Heavy Slider</span>
            <h3 class="font-display text-2xl font-bold text-charcoal dark:text-white">Multi-Track Sliding Systems</h3>
            <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Engineered with precision extruded UPVC sashes reinforced with hot-dip galvanized steel cores. Stainless steel tracks and nylon-encased needle rollers allow effortless finger-touch gliding.
            </p>
            <ul class="text-xs space-y-2 text-charcoal/80 dark:text-stone-200">
              <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-2 rtl:ml-2"></i> Integrated flyscreen / mosquito mesh track</li>
              <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-2 rtl:ml-2"></i> Anti-lift security blocks prevent sash removal</li>
              <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-2 rtl:ml-2"></i> Wool-pile weather seals on interlocking stiles</li>
            </ul>
            <div class="pt-2">
              <a href="products.html#sliding-windows" class="bronze-gradient-btn px-5 py-2.5 rounded-lg text-xs uppercase font-bold tracking-wider inline-flex items-center space-x-2 rtl:space-x-reverse">
                <span>View Full Dimensions</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 icon-flip"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Tab Pane 3: Fixed (Hidden by default) -->
        <div id="tab-fixed" class="style-tab-pane hidden grid-cols-1 lg:grid-cols-12 gap-8 items-center bg-ivory dark:bg-[#12181F] p-8 sm:p-12 rounded-3xl border border-charcoal/10 dark:border-white/10">
          <div class="lg:col-span-7 img-zoom-wrapper rounded-2xl overflow-hidden aspect-[16/10] shadow-lg">
            <img src="https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?auto=format&fit=crop&w=1200&q=80" 
                 alt="Fixed picture panoramic glazing" 
                 class="w-full h-full object-cover">
          </div>
          <div class="lg:col-span-5 space-y-4">
            <span class="text-xs font-mono font-bold text-bronze uppercase">Series 60mm Architectural Frame</span>
            <h3 class="font-display text-2xl font-bold text-charcoal dark:text-white">Fixed Architectural Picture Frames</h3>
            <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Provides the purest, thinnest profile frames to maximize visible glass area and embrace majestic surrounding landscapes with zero wind rattling.
            </p>
            <ul class="text-xs space-y-2 text-charcoal/80 dark:text-stone-200">
              <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-2 rtl:ml-2"></i> 100% airtight and storm-proof sealed glass unit</li>
              <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-2 rtl:ml-2"></i> Seamless pairing with operable flanking windows</li>
              <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-2 rtl:ml-2"></i> Ideal for double-height architectural living halls</li>
            </ul>
            <div class="pt-2">
              <a href="products.html#fixed-panoramic" class="bronze-gradient-btn px-5 py-2.5 rounded-lg text-xs uppercase font-bold tracking-wider inline-flex items-center space-x-2 rtl:space-x-reverse">
                <span>View Full Dimensions</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5 icon-flip"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4: CUSTOM UPVC DOOR COLLECTIONS (EDITORIAL STYLE) -->
    <section class="py-24 px-4 sm:px-8 bg-ivory dark:bg-[#12181F]">
      <div class="max-w-7xl mx-auto space-y-16">
        <div class="flex flex-col md:items-center xl:flex-row xl:items-end justify-between md:text-center xl:text-left gap-6 max-w-2xl md:max-w-3xl xl:max-w-7xl md:mx-auto xl:mx-0" data-aos="fade-up">
          <div class="max-w-2xl">
            <span class="text-xs uppercase font-bold tracking-widest text-bronze block mb-2">Grand Entrances & Patios</span>
            <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight">
              Custom UPVC Door Collections
            </h2>
          </div>
          <p class="text-charcoal/70 dark:text-stone-300 text-sm max-w-md md:max-w-xl xl:max-w-md">
            Engineered to support heavy architectural glazing units up to 350kg per sash with zero sag, whisper gliding, and bank-vault multi-point security.
          </p>
        </div>

        <!-- 2 Large Editorial Door Features -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-10">
          <!-- Door Collection 1: Bi-Fold & Sliding -->
          <div class="group rounded-3xl overflow-hidden bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-xl" data-aos="fade-up">
            <div class="aspect-[16/11] overflow-hidden relative">
              <img src="https://images.unsplash.com/photo-1600566753151-384129cf4e3e?auto=format&fit=crop&w=1200&q=80" 
                   alt="Modern folding bi-fold doors open to pool patio" 
                   class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
              <div class="absolute top-4 left-4 bg-charcoal/90 text-white px-3 py-1 rounded-full text-xs font-mono font-bold">
                FOLDING & BI-FOLD
              </div>
            </div>
            <div class="p-8 space-y-4">
              <h3 class="font-display text-2xl font-bold text-charcoal dark:text-white">Multi-Leaf Concertina Folding Doors</h3>
              <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                Stack up to 7 leaves seamlessly against the wall to dissolve the boundary between your living salon and outdoor swimming patio. Includes flush sunken track for tripping-free movement.
              </p>
              <div class="pt-2 flex items-center justify-between border-t border-charcoal/10 dark:border-white/10 text-xs">
                <span class="font-semibold text-charcoal dark:text-stone-200">Max Aperture: 8.5m</span>
                <a href="products.html#folding-bifold" class="font-bold text-bronze hover:underline inline-flex items-center space-x-1 rtl:space-x-reverse">
                  <span>Custom Configurator</span>
                  <i data-lucide="chevron-right" class="w-4 h-4 icon-flip"></i>
                </a>
              </div>
            </div>
          </div>

          <!-- Door Collection 2: Entrance & Pivot -->
          <div class="group rounded-3xl overflow-hidden bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-xl" data-aos="fade-up" data-aos-delay="100">
            <div class="aspect-[16/11] overflow-hidden relative">
              <img src="https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?auto=format&fit=crop&w=1200&q=80" 
                   alt="High-security entrance door with architectural glass sidelights" 
                   class="w-full h-full object-cover object-center transition-transform duration-700 group-hover:scale-105">
              <div class="absolute top-4 left-4 bg-charcoal/90 text-white px-3 py-1 rounded-full text-xs font-mono font-bold">
                HIGH SECURITY ENTRANCE
              </div>
            </div>
            <div class="p-8 space-y-4">
              <h3 class="font-display text-2xl font-bold text-charcoal dark:text-white">Architectural Master Entrance Systems</h3>
              <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                Featuring 5-point claw deadbolts, biometric fingerprint integration, and internal thermal cores that maintain a cool interior even under scorching exterior midday sun.
              </p>
              <div class="pt-2 flex items-center justify-between border-t border-charcoal/10 dark:border-white/10 text-xs">
                <span class="font-semibold text-charcoal dark:text-stone-200">Burglar Resistance RC3</span>
                <a href="products.html#entrance-doors" class="font-bold text-bronze hover:underline inline-flex items-center space-x-1 rtl:space-x-reverse">
                  <span>Custom Configurator</span>
                  <i data-lucide="chevron-right" class="w-4 h-4 icon-flip"></i>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: ENERGY EFFICIENCY & SOUNDPROOFING WITH VISUAL COMPARISONS -->
    <section class="py-24 px-4 sm:px-8 bg-charcoal text-white relative overflow-hidden">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          <!-- Left: Narrative & Interactive Decibel Simulator -->
          <div class="lg:col-span-7 space-y-6" data-aos="fade-right">
            <div class="flex items-center space-x-2 rtl:space-x-reverse">
              <span class="w-6 h-0.5 bg-bronze"></span>
              <span class="text-xs uppercase font-bold tracking-widest text-bronze">Acoustic & Thermal Physics</span>
            </div>

            <h2 class="font-display text-3xl sm:text-5xl font-extrabold tracking-tight text-white leading-tight">
              Silence the City. <br>
              Master Your Indoor Climate.
            </h2>

            <p class="text-sm text-stone-300 leading-relaxed max-w-xl">
              Standard single-pane aluminum frames leak indoor cooling and allow exterior traffic roar to permeate your sanctum. VISTRAL's multi-chamber fusion profiles and double-barrier EPDM seals drop noise pollution down to an imperceptible whisper.
            </p>

            <!-- Interactive Decibel Visualizer Widget -->
            <div class="p-6 rounded-2xl bg-white/5 border border-white/10 space-y-4 max-w-xl">
              <div class="flex items-center justify-between">
                <span class="text-xs uppercase tracking-wider text-stone-400 font-mono">Interactive Acoustic Simulator</span>
                <span id="decibelDisplay" class="font-display text-2xl font-bold text-bronze-200">30 dB</span>
              </div>
              
              <input id="soundproofSlider" type="range" min="20" max="85" value="30" class="w-full h-2 bg-stone-700 rounded-lg appearance-none cursor-pointer accent-bronze">
              
              <div class="flex items-center justify-between text-[11px] text-stone-400 font-mono">
                <span>20 dB (Forest Rustle)</span>
                <span>55 dB (Normal Traffic)</span>
                <span>85 dB (Heavy Highway)</span>
              </div>

              <div class="pt-2 border-t border-white/10 flex items-center space-x-2 rtl:space-x-reverse">
                <i data-lucide="info" class="w-4 h-4 text-bronze"></i>
                <p id="soundStatus" class="text-xs text-emerald-400 font-semibold">
                  Whisper Quiet (VISTRAL Multi-Chamber Glazed)
                </p>
              </div>
            </div>

            <!-- Comparison Metric Columns -->
            <div class="grid grid-cols-2 gap-4 max-w-xl pt-2">
              <div class="p-4 rounded-xl bg-white/5 border border-white/10">
                <span class="block text-xs uppercase text-stone-400 font-mono">Aluminum Window</span>
                <span class="text-xl font-bold text-rose-400 font-display">U-Val: 3.8 W/m²K</span>
                <span class="block text-[11px] text-stone-400 mt-1">High heat transfer & condensation</span>
              </div>
              <div class="p-4 rounded-xl bg-bronze/10 border border-bronze/30">
                <span class="block text-xs uppercase text-bronze font-mono">VISTRAL UPVC</span>
                <span class="text-xl font-bold text-emerald-400 font-display">U-Val: 0.78 W/m²K</span>
                <span class="block text-[11px] text-stone-300 mt-1">79% lower thermal loss</span>
              </div>
            </div>
          </div>

          <!-- Right: Visual Image with Floating Performance Badges -->
          <div class="lg:col-span-5 relative" data-aos="fade-left">
            <div class="rounded-3xl overflow-hidden shadow-2xl border-4 border-white/10 aspect-[4/5] relative">
              <img src="https://images.unsplash.com/photo-1513519245088-0e12902e5a38?auto=format&fit=crop&w=900&q=80" 
                   alt="Peaceful interior with acoustic insulated UPVC window" 
                   class="w-full h-full object-cover">
              <div class="absolute inset-0 bg-gradient-to-t from-charcoal/90 via-transparent to-transparent"></div>
              
              <div class="absolute bottom-6 left-6 right-6 space-y-3">
                <div class="p-4 rounded-xl bg-charcoal/90 backdrop-blur-md border border-white/15">
                  <div class="flex items-center justify-between text-xs font-mono text-bronze mb-1">
                    <span>ARGON GAS DOUBLE GLAZING</span>
                    <span>99% UV BLOCK</span>
                  </div>
                  <p class="text-xs text-stone-200">
                    Dual Low-E silver coating reflects infrared radiant heat while admitting 76% clear daylight.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 6: RECENT RESIDENTIAL & COMMERCIAL INSTALLATION PROJECTS -->
    <section class="py-24 px-4 sm:px-8 bg-ivory dark:bg-[#12181F]">
      <div class="max-w-7xl mx-auto space-y-16">
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-6" data-aos="fade-up">
          <div class="max-w-2xl">
            <span class="text-xs uppercase font-bold tracking-widest text-bronze block mb-2">Realized Architecture</span>
            <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight">
              Recent Installations
            </h2>
          </div>
          <a href="gallery.html" class="inline-flex items-center space-x-2 text-xs uppercase font-bold tracking-wider text-bronze hover:underline rtl:space-x-reverse">
            <span>Filter All Case Studies</span>
            <i data-lucide="arrow-right" class="w-4 h-4 icon-flip"></i>
          </a>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
          <!-- Project 1 -->
          <div class="group rounded-3xl overflow-hidden bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-lg" data-aos="fade-up">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1580587771525-78b9dba3b914?auto=format&fit=crop&w=800&q=80" 
                   alt="Hillside Cantilever Residence UPVC installation" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-6 space-y-2">
              <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Residential Luxury</span>
              <h3 class="font-display text-xl font-bold text-charcoal dark:text-white">Hillside Villa</h3>
              <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                48 sashes of flush Anthracite Grey casements paired with oversized solar-control sliding doors.
              </p>
            </div>
          </div>

          <!-- Project 2 -->
          <div class="group rounded-3xl overflow-hidden bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-lg" data-aos="fade-up" data-aos-delay="100">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=800&q=80" 
                   alt="Modernist Glasshouse residential project" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-6 space-y-2">
              <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Passive Solarium</span>
              <h3 class="font-display text-xl font-bold text-charcoal dark:text-white">Modernist Glasshouse</h3>
              <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                Passivhaus compliant triple-glazed fixed frames and concealed motorized tilt ventilation windows.
              </p>
            </div>
          </div>

          <!-- Project 3 -->
          <div class="md:col-span-2 md:w-[calc(50%-1rem)] md:mx-auto xl:col-span-1 xl:w-full xl:mx-0 group rounded-3xl overflow-hidden bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-lg" data-aos="fade-up" data-aos-delay="200">
            <div class="img-zoom-wrapper aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80" 
                   alt="Metropolitan Corporate HQ commercial installation" 
                   class="w-full h-full object-cover">
            </div>
            <div class="p-6 space-y-2">
              <span class="text-[10px] font-mono uppercase tracking-wider text-bronze font-bold">Commercial Complex</span>
              <h3 class="font-display text-xl font-bold text-charcoal dark:text-white">Metropolitan Tower</h3>
              <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
                Acoustically certified continuous ribbon UPVC fenestration dampening 46dB of downtown traffic.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 7: CUSTOMER TESTIMONIALS & PREMIUM QUOTE-REQUEST CTA -->
    <section class="py-24 px-4 sm:px-8 bg-white dark:bg-[#182029] border-t border-charcoal/10 dark:border-white/10">
      <div class="max-w-7xl mx-auto">
        <!-- Centered Section Heading -->
        <div class="text-center max-w-3xl mx-auto mb-16" data-aos="fade-up">
          <div class="inline-flex items-center space-x-2 rtl:space-x-reverse justify-center mb-2">
            <span class="w-6 h-0.5 bg-bronze"></span>
            <span class="text-xs uppercase font-bold tracking-widest text-bronze font-mono">Architectural Endorsements</span>
            <span class="w-6 h-0.5 bg-bronze"></span>
          </div>
          <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight leading-tight">
            Trusted by Leading Architects & Estate Builders
          </h2>
          <p class="text-xs sm:text-sm text-charcoal/70 dark:text-stone-300 mt-3 max-w-xl mx-auto leading-relaxed">
            Verified performance reviews from award-winning architectural firms and luxury development directors.
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          <!-- Testimonials Column -->
          <div class="lg:col-span-6 space-y-4" data-aos="fade-right">
            <!-- Testimonial Cards Carousel / Stack -->
            <div class="p-6 rounded-2xl bg-ivory dark:bg-[#12181F] border border-charcoal/10 dark:border-white/10 shadow-sm space-y-3">
              <div class="flex items-center space-x-1 text-bronze">
                <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                <i data-lucide="star" class="w-4 h-4 fill-current"></i>
              </div>
              <p class="text-xs sm:text-sm text-charcoal/80 dark:text-stone-300 italic leading-relaxed">
                "VISTRAL fabricated and installed 62 bespoke window systems for our cliffside villa project. The acoustic dampening against 70 km/h ocean gales is remarkable. Not a whisper of air leaks."
              </p>
              <div class="flex items-center space-x-3 rtl:space-x-reverse pt-2">
                <div class="w-9 h-9 rounded-full bg-bronze/20 text-bronze font-bold flex items-center justify-center text-xs">
                  MK
                </div>
                <div>
                  <span class="block text-xs font-bold text-charcoal dark:text-white">Marcus Klein, AIA</span>
                  <span class="text-[11px] text-charcoal/60 dark:text-stone-400">Principal Architect, Klein & Partners</span>
                </div>
              </div>
            </div>

            <div class="p-6 rounded-2xl bg-ivory dark:bg-[#12181F] border border-charcoal/10 dark:border-white/10 shadow-sm space-y-3">
              <div class="flex items-center space-x-1 text-bronze">
                <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                <i data-lucide="star" class="w-4 h-4 fill-current"></i>
              </div>
              <p class="text-xs sm:text-sm text-charcoal/80 dark:text-stone-300 italic leading-relaxed">
                "The flush threshold sliding doors glide like silk despite the heavy 3-ply acoustic glass. Their laser measurement crew was within 1 millimeter across our 12-meter aperture."
              </p>
              <div class="flex items-center space-x-3 rtl:space-x-reverse pt-2">
                <div class="w-9 h-9 rounded-full bg-bronze/20 text-bronze font-bold flex items-center justify-center text-xs">
                  EL
                </div>
                <div>
                  <span class="block text-xs font-bold text-charcoal dark:text-white">Elena Rostova</span>
                  <span class="text-[11px] text-charcoal/60 dark:text-stone-400">Managing Director, Vanguard Luxury Developments</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Quote Request CTA Card -->
          <div class="lg:col-span-6" data-aos="fade-left">
            <div class="p-8 sm:p-12 rounded-3xl bg-charcoal text-white relative overflow-hidden shadow-2xl border border-bronze/30 space-y-6">
              <div class="absolute -right-12 -bottom-12 w-48 h-48 rounded-full bg-bronze/10 filter blur-2xl"></div>
              
              <div class="space-y-2">
                <span class="text-xs uppercase font-bold tracking-widest text-bronze font-mono">Immediate Quotation</span>
                <h3 class="font-display text-2xl sm:text-4xl font-extrabold text-white">
                  Begin Your Architectural Project
                </h3>
                <p class="text-xs sm:text-sm text-stone-300 leading-relaxed">
                  Submit your window dimensions or architectural drawing package. Our senior engineering estimator will provide an itemized specification within 24 hours.
                </p>
              </div>

              <div class="pt-2 space-y-3">
                <a href="contact.html#measurement-booking" class="w-full bronze-gradient-btn py-4 px-6 rounded-xl text-center text-xs uppercase font-bold tracking-wider inline-flex items-center justify-center space-x-2 rtl:space-x-reverse shadow-xl">
                  <span>Book Free Measurement & Laser Audit</span>
                  <i data-lucide="calendar" class="w-4 h-4"></i>
                </a>
                <a href="contact.html" class="w-full text-center py-4 px-6 rounded-xl border border-white/20 bg-white/5 hover:bg-white/10 text-white text-xs uppercase font-bold tracking-wider inline-flex items-center justify-center space-x-2 rtl:space-x-reverse transition-all">
                  <span>Send Architectural Blueprints</span>
                  <i data-lucide="upload" class="w-4 h-4 text-bronze"></i>
                </a>
              </div>

              <div class="flex items-center justify-between pt-4 border-t border-white/10 text-[11px] text-stone-400">
                <span class="flex items-center"><i data-lucide="shield-check" class="w-3.5 h-3.5 text-bronze mr-1 rtl:ml-1"></i> ISO 9001:2015 Certified</span>
                <span class="flex items-center"><i data-lucide="clock" class="w-3.5 h-3.5 text-bronze mr-1 rtl:ml-1"></i> Fast 24h Turnaround</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
"""
    content += get_footer()
    
    with open("home-2.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("home-2.html (Home 2 - exactly 7 sections) generated successfully.")

if __name__ == "__main__":
    build_home_2()

