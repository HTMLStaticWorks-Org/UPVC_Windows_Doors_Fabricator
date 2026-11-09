import os
from templates import get_head, get_header, get_footer

def build_gallery():
    content = get_head("Gallery - Architectural UPVC Fenestration Portfolio", "gallery")
    content += get_header("gallery")
    content += """
  <main class="flex-grow">
    <!-- SECTION 1: FULL-WIDTH GALLERY HERO -->
    <section class="relative min-h-[50vh] flex items-center justify-center overflow-hidden py-24 px-4 sm:px-8 bg-charcoal text-white">
      <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=2000&q=85" 
             alt="VISTRAL architectural window and door installations portfolio" 
             class="w-full h-full object-cover filter brightness-[0.38]">
        <div class="absolute inset-0 bg-gradient-to-t from-charcoal via-charcoal/70 to-transparent"></div>
      </div>

      <div class="relative z-10 max-w-4xl mx-auto text-center space-y-6" data-aos="fade-up">
        <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-bronze-200 text-xs uppercase tracking-widest font-mono font-semibold rtl:space-x-reverse">
          <span class="w-2 h-2 rounded-full bg-bronze"></span>
          <span>Architectural Fenestration Portfolio</span>
        </div>

        <h1 class="font-display font-extrabold text-4xl sm:text-6xl tracking-tight text-white leading-tight">
          Visualizing Structural Grandeur
        </h1>

        <p class="text-base sm:text-lg text-stone-200 max-w-2xl mx-auto font-normal leading-relaxed">
          Explore our completed residential villas, commercial high-rises, and custom interior architectural installations.
        </p>

        <!-- Interactive Category Filters -->
        <div class="flex flex-wrap items-center justify-center gap-2 pt-4" data-aos="fade-up" data-aos-delay="100">
          <button class="gallery-filter-btn active bg-amber-700 text-white px-5 py-2.5 rounded-full text-xs uppercase tracking-wider font-bold transition-all shadow-md" data-filter="all">
            All Projects
          </button>
          <button class="gallery-filter-btn bg-stone-200 dark:bg-stone-800 text-stone-700 dark:text-stone-300 px-5 py-2.5 rounded-full text-xs uppercase tracking-wider font-bold transition-all hover:bg-stone-300 dark:hover:bg-stone-700" data-filter="residential">
            Residential
          </button>
          <button class="gallery-filter-btn bg-stone-200 dark:bg-stone-800 text-stone-700 dark:text-stone-300 px-5 py-2.5 rounded-full text-xs uppercase tracking-wider font-bold transition-all hover:bg-stone-300 dark:hover:bg-stone-700" data-filter="commercial">
            Commercial
          </button>
          <button class="gallery-filter-btn bg-stone-200 dark:bg-stone-800 text-stone-700 dark:text-stone-300 px-5 py-2.5 rounded-full text-xs uppercase tracking-wider font-bold transition-all hover:bg-stone-300 dark:hover:bg-stone-700" data-filter="windows">
            Windows
          </button>
          <button class="gallery-filter-btn bg-stone-200 dark:bg-stone-800 text-stone-700 dark:text-stone-300 px-5 py-2.5 rounded-full text-xs uppercase tracking-wider font-bold transition-all hover:bg-stone-300 dark:hover:bg-stone-700" data-filter="doors">
            Doors
          </button>
        </div>
      </div>
    </section>

    <!-- SECTION 2: RESIDENTIAL UPVC WINDOW INSTALLATION PROJECTS -->
    <section class="gallery-tier-section py-20 px-4 sm:px-8 bg-ivory dark:bg-[#12181F] architectural-grid transition-all duration-300">
      <div class="max-w-7xl mx-auto space-y-12">
        <div class="flex items-center justify-between border-b border-charcoal/10 dark:border-white/10 pb-6" data-aos="fade-up">
          <div>
            <span class="text-xs uppercase font-bold tracking-widest text-bronze block mb-1">Portfolio Tier 01</span>
            <h2 class="font-display text-2xl sm:text-4xl font-extrabold text-charcoal dark:text-white">
              Residential Window Installations
            </h2>
          </div>
          <span class="text-xs font-mono text-bronze font-bold hidden sm:block">3 Featured Estates</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
          <!-- Project 1 -->
          <div class="gallery-item group relative rounded-3xl overflow-hidden shadow-lg cursor-pointer aspect-[4/3]" data-category="residential windows" data-aos="fade-up">
            <img src="https://images.unsplash.com/photo-1613977257363-707ba9348227?auto=format&fit=crop&w=900&q=80" 
                 alt="Bel-Air Modernist Villa UPVC Casements" 
                 class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
            <div class="absolute inset-0 bg-gradient-to-t from-black/95 via-black/80 to-black/35 backdrop-blur-[2px] opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-6 text-white">
              <span class="inline-block px-2.5 py-0.5 rounded-full bg-bronze/25 text-bronze-200 border border-bronze/40 text-[10px] font-mono uppercase font-bold tracking-wider w-max mb-1.5 shadow-sm">Residential &bull; Windows</span>
              <h3 class="gallery-title font-display text-xl font-extrabold text-white tracking-tight drop-shadow-md">Bel-Air Villa</h3>
              <p class="text-xs text-stone-200 mt-1.5 font-medium leading-relaxed drop-shadow-sm">Series 88mm triple-glazed acoustic casements with concealed friction hinges.</p>
              <div class="mt-3.5 inline-flex items-center space-x-1.5 text-xs text-bronze-300 font-bold rtl:space-x-reverse group-hover:text-bronze-200 transition-colors">
                <i data-lucide="maximize-2" class="w-3.5 h-3.5 text-bronze-300"></i>
                <span>Click to Expand</span>
              </div>
            </div>
          </div>

          <!-- Project 2 -->
          <div class="gallery-item group relative rounded-3xl overflow-hidden shadow-lg cursor-pointer aspect-[4/3]" data-category="residential windows" data-aos="fade-up" data-aos-delay="100">
            <img src="https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&w=900&q=80" 
                 alt="Aspen Solarium Chalet Fixed Picture Windows" 
                 class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
            <div class="absolute inset-0 bg-gradient-to-t from-black/95 via-black/80 to-black/35 backdrop-blur-[2px] opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-6 text-white">
              <span class="inline-block px-2.5 py-0.5 rounded-full bg-bronze/25 text-bronze-200 border border-bronze/40 text-[10px] font-mono uppercase font-bold tracking-wider w-max mb-1.5 shadow-sm">Residential &bull; Windows</span>
              <h3 class="gallery-title font-display text-xl font-extrabold text-white tracking-tight drop-shadow-md">Aspen Solarium</h3>
              <p class="text-xs text-stone-200 mt-1.5 font-medium leading-relaxed drop-shadow-sm">Multi-pane fixed picture glazing engineered to withstand 180cm heavy snow load.</p>
              <div class="mt-3.5 inline-flex items-center space-x-1.5 text-xs text-bronze-300 font-bold rtl:space-x-reverse group-hover:text-bronze-200 transition-colors">
                <i data-lucide="maximize-2" class="w-3.5 h-3.5 text-bronze-300"></i>
                <span>Click to Expand</span>
              </div>
            </div>
          </div>

          <!-- Project 3 -->
          <div class="md:col-span-2 md:w-[calc(50%-1rem)] md:mx-auto xl:col-span-1 xl:w-full xl:mx-0 gallery-item group relative rounded-3xl overflow-hidden shadow-lg cursor-pointer aspect-[4/3]" data-category="residential doors" data-aos="fade-up" data-aos-delay="200">
            <img src="https://images.unsplash.com/photo-1618773928121-c32242e63f39?auto=format&fit=crop&w=900&q=80" 
                 alt="Pacific Horizon Luxury French Patio Doors" 
                 class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
            <div class="absolute inset-0 bg-gradient-to-t from-black/95 via-black/80 to-black/35 backdrop-blur-[2px] opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-6 text-white">
              <span class="inline-block px-2.5 py-0.5 rounded-full bg-bronze/25 text-bronze-200 border border-bronze/40 text-[10px] font-mono uppercase font-bold tracking-wider w-max mb-1.5 shadow-sm">Residential &bull; Doors</span>
              <h3 class="gallery-title font-display text-xl font-extrabold text-white tracking-tight drop-shadow-md">Pacific Residence</h3>
              <p class="text-xs text-stone-200 mt-1.5 font-medium leading-relaxed drop-shadow-sm">Double-leaf UPVC French terrace doors with magnetic multi-point deadbolts.</p>
              <div class="mt-3.5 inline-flex items-center space-x-1.5 text-xs text-bronze-300 font-bold rtl:space-x-reverse group-hover:text-bronze-200 transition-colors">
                <i data-lucide="maximize-2" class="w-3.5 h-3.5 text-bronze-300"></i>
                <span>Click to Expand</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: COMMERCIAL BUILDING WINDOW AND DOOR INSTALLATIONS -->
    <section class="gallery-tier-section py-20 px-4 sm:px-8 bg-white dark:bg-[#182029] border-y border-charcoal/10 dark:border-white/10 transition-all duration-300">
      <div class="max-w-7xl mx-auto space-y-12">
        <div class="flex items-center justify-between border-b border-charcoal/10 dark:border-white/10 pb-6" data-aos="fade-up">
          <div>
            <span class="text-xs uppercase font-bold tracking-widest text-bronze block mb-1">Portfolio Tier 02</span>
            <h2 class="font-display text-2xl sm:text-4xl font-extrabold text-charcoal dark:text-white">
              Commercial High-Rise & Corporate Complexes
            </h2>
          </div>
          <span class="text-xs font-mono text-bronze font-bold hidden sm:block">Engineered For Wind Pressures</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
          <!-- Commercial 1 -->
          <div class="gallery-item group relative rounded-3xl overflow-hidden shadow-lg cursor-pointer aspect-[4/3]" data-category="commercial windows" data-aos="fade-up">
            <img src="https://images.unsplash.com/photo-1486325212027-8081e485255e?auto=format&fit=crop&w=900&q=80" 
                 alt="Vanguard Innovation Center Corporate Facade" 
                 class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
            <div class="absolute inset-0 bg-gradient-to-t from-black/95 via-black/80 to-black/35 backdrop-blur-[2px] opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-6 text-white">
              <span class="inline-block px-2.5 py-0.5 rounded-full bg-bronze/25 text-bronze-200 border border-bronze/40 text-[10px] font-mono uppercase font-bold tracking-wider w-max mb-1.5 shadow-sm">Commercial &bull; Windows</span>
              <h3 class="gallery-title font-display text-xl font-extrabold text-white tracking-tight drop-shadow-md">Vanguard Center</h3>
              <p class="text-xs text-stone-200 mt-1.5 font-medium leading-relaxed drop-shadow-sm">Continuous ribbon fenestration with acoustic class 5 traffic isolation.</p>
              <div class="mt-3.5 inline-flex items-center space-x-1.5 text-xs text-bronze-300 font-bold rtl:space-x-reverse group-hover:text-bronze-200 transition-colors">
                <i data-lucide="maximize-2" class="w-3.5 h-3.5 text-bronze-300"></i>
                <span>Click to Expand</span>
              </div>
            </div>
          </div>

          <!-- Commercial 2 -->
          <div class="gallery-item group relative rounded-3xl overflow-hidden shadow-lg cursor-pointer aspect-[4/3]" data-category="commercial doors" data-aos="fade-up" data-aos-delay="100">
            <img src="https://images.unsplash.com/photo-1554469384-e58fac16e23a?auto=format&fit=crop&w=900&q=80" 
                 alt="Stuttgart Financial Plaza Glazed Entrance" 
                 class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
            <div class="absolute inset-0 bg-gradient-to-t from-black/95 via-black/80 to-black/35 backdrop-blur-[2px] opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-6 text-white">
              <span class="inline-block px-2.5 py-0.5 rounded-full bg-bronze/25 text-bronze-200 border border-bronze/40 text-[10px] font-mono uppercase font-bold tracking-wider w-max mb-1.5 shadow-sm">Commercial &bull; Doors</span>
              <h3 class="gallery-title font-display text-xl font-extrabold text-white tracking-tight drop-shadow-md">Stuttgart Plaza</h3>
              <p class="text-xs text-stone-200 mt-1.5 font-medium leading-relaxed drop-shadow-sm">High-traffic commercial automatic sliding entrance with heavy steel box reinforcement.</p>
              <div class="mt-3.5 inline-flex items-center space-x-1.5 text-xs text-bronze-300 font-bold rtl:space-x-reverse group-hover:text-bronze-200 transition-colors">
                <i data-lucide="maximize-2" class="w-3.5 h-3.5 text-bronze-300"></i>
                <span>Click to Expand</span>
              </div>
            </div>
          </div>

          <!-- Commercial 3 -->
          <div class="md:col-span-2 md:w-[calc(50%-1rem)] md:mx-auto xl:col-span-1 xl:w-full xl:mx-0 gallery-item group relative rounded-3xl overflow-hidden shadow-lg cursor-pointer aspect-[4/3]" data-category="commercial windows" data-aos="fade-up" data-aos-delay="200">
            <img src="https://images.unsplash.com/photo-1577495508048-b635879837f1?auto=format&fit=crop&w=900&q=80" 
                 alt="Zurich Bio-Tech Research Labs" 
                 class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
            <div class="absolute inset-0 bg-gradient-to-t from-black/95 via-black/80 to-black/35 backdrop-blur-[2px] opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-6 text-white">
              <span class="inline-block px-2.5 py-0.5 rounded-full bg-bronze/25 text-bronze-200 border border-bronze/40 text-[10px] font-mono uppercase font-bold tracking-wider w-max mb-1.5 shadow-sm">Commercial &bull; Windows</span>
              <h3 class="gallery-title font-display text-xl font-extrabold text-white tracking-tight drop-shadow-md">Zurich Bio-Tech Labs</h3>
              <p class="text-xs text-stone-200 mt-1.5 font-medium leading-relaxed drop-shadow-sm">Hermetically sealed clean-room UPVC casement windows with hospital-grade antimicrobial gaskets.</p>
              <div class="mt-3.5 inline-flex items-center space-x-1.5 text-xs text-bronze-300 font-bold rtl:space-x-reverse group-hover:text-bronze-200 transition-colors">
                <i data-lucide="maximize-2" class="w-3.5 h-3.5 text-bronze-300"></i>
                <span>Click to Expand</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4: MODERN INTERIOR AND EXTERIOR UPVC DESIGN SHOWCASE -->
    <section class="gallery-tier-section py-20 px-4 sm:px-8 bg-ivory dark:bg-[#12181F] transition-all duration-300">
      <div class="max-w-7xl mx-auto space-y-12">
        <div class="flex items-center justify-between border-b border-charcoal/10 dark:border-white/10 pb-6" data-aos="fade-up">
          <div>
            <span class="text-xs uppercase font-bold tracking-widest text-bronze block mb-1">Portfolio Tier 03</span>
            <h2 class="font-display text-2xl sm:text-4xl font-extrabold text-charcoal dark:text-white">
              Interior & Exterior Design Integration
            </h2>
          </div>
          <span class="text-xs font-mono text-bronze font-bold hidden sm:block">Aesthetic Harmony</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
          <!-- Interior 1 -->
          <div class="gallery-item group relative rounded-3xl overflow-hidden shadow-lg cursor-pointer aspect-[4/3]" data-category="residential windows" data-aos="fade-up">
            <img src="https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=900&q=80" 
                 alt="Minimalist living salon with framed garden window" 
                 class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
            <div class="absolute inset-0 bg-gradient-to-t from-black/95 via-black/80 to-black/35 backdrop-blur-[2px] opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-6 text-white">
              <span class="inline-block px-2.5 py-0.5 rounded-full bg-bronze/25 text-bronze-200 border border-bronze/40 text-[10px] font-mono uppercase font-bold tracking-wider w-max mb-1.5 shadow-sm">Interior &bull; Windows</span>
              <h3 class="gallery-title font-display text-xl font-extrabold text-white tracking-tight drop-shadow-md">Scandinavian Salon</h3>
              <p class="text-xs text-stone-200 mt-1.5 font-medium leading-relaxed drop-shadow-sm">Matte White UPVC picture window framing private courtyard greenery.</p>
              <div class="mt-3.5 inline-flex items-center space-x-1.5 text-xs text-bronze-300 font-bold rtl:space-x-reverse group-hover:text-bronze-200 transition-colors">
                <i data-lucide="maximize-2" class="w-3.5 h-3.5 text-bronze-300"></i>
                <span>Click to Expand</span>
              </div>
            </div>
          </div>

          <!-- Interior 2 -->
          <div class="gallery-item group relative rounded-3xl overflow-hidden shadow-lg cursor-pointer aspect-[4/3]" data-category="residential doors" data-aos="fade-up" data-aos-delay="100">
            <img src="https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=900&q=80" 
                 alt="Kitchen patio access with sliding glass door" 
                 class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
            <div class="absolute inset-0 bg-gradient-to-t from-black/95 via-black/80 to-black/35 backdrop-blur-[2px] opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-6 text-white">
              <span class="inline-block px-2.5 py-0.5 rounded-full bg-bronze/25 text-bronze-200 border border-bronze/40 text-[10px] font-mono uppercase font-bold tracking-wider w-max mb-1.5 shadow-sm">Interior &bull; Doors</span>
              <h3 class="gallery-title font-display text-xl font-extrabold text-white tracking-tight drop-shadow-md">Kitchen Solarium</h3>
              <p class="text-xs text-stone-200 mt-1.5 font-medium leading-relaxed drop-shadow-sm">Zero-threshold sliding pocket door seamlessly hidden inside wall cavity.</p>
              <div class="mt-3.5 inline-flex items-center space-x-1.5 text-xs text-bronze-300 font-bold rtl:space-x-reverse group-hover:text-bronze-200 transition-colors">
                <i data-lucide="maximize-2" class="w-3.5 h-3.5 text-bronze-300"></i>
                <span>Click to Expand</span>
              </div>
            </div>
          </div>

          <!-- Interior 3 -->
          <div class="md:col-span-2 md:w-[calc(50%-1rem)] md:mx-auto xl:col-span-1 xl:w-full xl:mx-0 gallery-item group relative rounded-3xl overflow-hidden shadow-lg cursor-pointer aspect-[4/3]" data-category="residential windows" data-aos="fade-up" data-aos-delay="200">
            <img src="https://images.unsplash.com/photo-1616046229478-9901c5536a45?auto=format&fit=crop&w=900&q=80" 
                 alt="Master suite architectural corner glazing" 
                 class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
            <div class="absolute inset-0 bg-gradient-to-t from-black/95 via-black/80 to-black/35 backdrop-blur-[2px] opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-6 text-white">
              <span class="inline-block px-2.5 py-0.5 rounded-full bg-bronze/25 text-bronze-200 border border-bronze/40 text-[10px] font-mono uppercase font-bold tracking-wider w-max mb-1.5 shadow-sm">Interior &bull; Windows</span>
              <h3 class="gallery-title font-display text-xl font-extrabold text-white tracking-tight drop-shadow-md">Panoramic Suite</h3>
              <p class="text-xs text-stone-200 mt-1.5 font-medium leading-relaxed drop-shadow-sm">Concealed-profile butt joint corner glazing with micro-ventilation top-hung sashes.</p>
              <div class="mt-3.5 inline-flex items-center space-x-1.5 text-xs text-bronze-300 font-bold rtl:space-x-reverse group-hover:text-bronze-200 transition-colors">
                <i data-lucide="maximize-2" class="w-3.5 h-3.5 text-bronze-300"></i>
                <span>Click to Expand</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: PROJECT ENQUIRY CTA -->
    <section class="py-24 px-4 sm:px-8 bg-charcoal text-white relative overflow-hidden">
      <div class="max-w-5xl mx-auto text-center space-y-6" data-aos="zoom-in">
        <span class="text-xs uppercase font-bold tracking-widest text-bronze font-mono">Commission Your Architecture</span>
        <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-white tracking-tight">
          Want Similar Architectural Quality in Your Project?
        </h2>
        <p class="text-sm text-stone-300 max-w-2xl mx-auto leading-relaxed">
          Book a site visit from our senior installation architects or send us your elevations and CAD files for a comprehensive quotation and structural thermal review.
        </p>
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center justify-center gap-4 pt-4">
          <a href="contact.html#measurement-booking" class="w-full sm:w-auto bronze-gradient-btn px-8 py-4 rounded-xl text-xs uppercase font-bold tracking-wider inline-flex items-center justify-center space-x-2 rtl:space-x-reverse shadow-xl">
            <span>Book Free Site Measurement</span>
            <i data-lucide="calendar" class="w-4 h-4"></i>
          </a>
          <a href="contact.html" class="w-full sm:w-auto px-8 py-4 rounded-xl text-xs uppercase font-bold tracking-wider bg-white/10 hover:bg-white/20 border border-white/20 text-white inline-flex items-center justify-center space-x-2 rtl:space-x-reverse transition-all">
            <span>Upload Architectural Blueprints</span>
            <i data-lucide="upload" class="w-4 h-4 text-bronze"></i>
          </a>
        </div>
      </div>
    </section>
  </main>
"""
    content += get_footer()
    
    with open("gallery.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("gallery.html (Gallery - exactly 5 sections) generated successfully.")

if __name__ == "__main__":
    build_gallery()

