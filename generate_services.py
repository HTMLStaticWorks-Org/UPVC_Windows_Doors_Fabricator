import os
from templates import get_head, get_header, get_footer

def build_services():
    content = get_head("Services - Architectural UPVC Fabrication & Installation", "services")
    content += get_header("services")
    content += """
  <main class="flex-grow">
    <!-- SECTION 1: PREMIUM SERVICES HERO SECTION -->
    <section class="relative min-h-[50vh] flex items-center justify-center overflow-hidden py-24 px-4 sm:px-8 bg-charcoal text-white">
      <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=2000&q=85" 
             alt="VISTRAL expert fenestration artisan craftsmanship" 
             class="w-full h-full object-cover filter brightness-[0.38]">
        <div class="absolute inset-0 bg-gradient-to-t from-charcoal via-charcoal/70 to-transparent"></div>
      </div>

      <div class="relative z-10 max-w-4xl mx-auto text-center space-y-6" data-aos="fade-up">
        <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-bronze-200 text-xs uppercase tracking-widest font-mono font-semibold rtl:space-x-reverse">
          <span class="w-2 h-2 rounded-full bg-bronze"></span>
          <span>End-to-End Architectural Fenestration</span>
        </div>

        <h1 class="font-display font-extrabold text-4xl sm:text-6xl tracking-tight text-white leading-tight">
          Comprehensive Architectural Services
        </h1>

        <p class="text-base sm:text-lg text-stone-200 max-w-2xl mx-auto font-normal leading-relaxed">
          From computerized precision fabrication and laser site auditing to turnkey structural installation and lifelong maintenance.
        </p>
      </div>
    </section>

    <!-- SECTION 2: CUSTOM UPVC FABRICATION SERVICES -->
    <section id="custom-fabrication" class="py-24 px-4 sm:px-8 bg-ivory dark:bg-[#12181F] architectural-grid">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          <!-- Visual Workshop Feature -->
          <div class="lg:col-span-6 relative" data-aos="fade-right">
            <div class="rounded-3xl overflow-hidden shadow-2xl border-4 border-white dark:border-[#182029] aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1581092334651-ddf26d9a09d0?auto=format&fit=crop&w=1000&q=80" 
                   alt="Precision CNC profile fabrication machine" 
                   class="w-full h-full object-cover">
            </div>
            <!-- Floating Spec Badge -->
            <div class="absolute -bottom-6 -left-4 bg-charcoal text-white p-5 rounded-2xl shadow-xl border border-bronze/30 max-w-xs hidden sm:block">
              <span class="text-[10px] font-mono uppercase text-bronze font-bold block">TOLERANCE SPECIFICATION</span>
              <span class="text-base font-bold font-display text-white">±0.2mm Digital Calibrated Precision</span>
            </div>
          </div>

          <!-- Narrative -->
          <div class="lg:col-span-6 space-y-6" data-aos="fade-left">
            <div class="flex items-center space-x-2 rtl:space-x-reverse">
              <span class="w-6 h-0.5 bg-bronze"></span>
              <span class="text-xs uppercase font-bold tracking-widest text-bronze">Service 01</span>
            </div>

            <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight leading-tight">
              Bespoke UPVC Architectural Fabrication
            </h2>

            <p class="text-sm sm:text-base text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Every home has a unique architectural soul. We do not manufacture mass-produced standard stock. Our fabrication service custom-tailors multi-chamber profiles, glass units, and custom RAL foil laminates directly from your architectural elevation plans.
            </p>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
              <div class="p-4 rounded-2xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10">
                <h4 class="font-display font-bold text-sm text-charcoal dark:text-white flex items-center">
                  <i data-lucide="check-circle-2" class="w-4 h-4 text-bronze mr-2 rtl:ml-2"></i>
                  Robotic 4-Corner Welding
                </h4>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 mt-1">Homogeneous fusion of corners eliminating structural weakness.</p>
              </div>

              <div class="p-4 rounded-2xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10">
                <h4 class="font-display font-bold text-sm text-charcoal dark:text-white flex items-center">
                  <i data-lucide="check-circle-2" class="w-4 h-4 text-bronze mr-2 rtl:ml-2"></i>
                  Continuous Steel Reinforcement
                </h4>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 mt-1">Heavy-gauge galvanized steel chambers prevent thermal sag.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: PROFESSIONAL MEASUREMENT AND CONSULTATION SERVICES -->
    <section class="py-24 px-4 sm:px-8 bg-white dark:bg-[#182029] border-y border-charcoal/10 dark:border-white/10">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          <div class="lg:col-span-6 space-y-6" data-aos="fade-right">
            <div class="flex items-center space-x-2 rtl:space-x-reverse">
              <span class="w-6 h-0.5 bg-bronze"></span>
              <span class="text-xs uppercase font-bold tracking-widest text-bronze">Service 02</span>
            </div>

            <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight leading-tight">
              3D Laser Site Survey & Acoustic Consultation
            </h2>

            <p class="text-sm sm:text-base text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Masonry apertures are rarely completely square. Our fenestration engineers utilize Leica 3D laser scanners to measure diagonals, wall moisture levels, and wind exposure vectors before a single profile is cut.
            </p>

            <ul class="text-xs sm:text-sm space-y-3 text-charcoal/80 dark:text-stone-200">
              <li class="flex items-start space-x-3 rtl:space-x-reverse">
                <i data-lucide="scan" class="w-5 h-5 text-bronze flex-shrink-0 mt-0.5"></i>
                <span><strong>Aperture Diagonal & Plumb Inspection:</strong> Detects wall settlement deviations down to 0.5 millimeter.</span>
              </li>
              <li class="flex items-start space-x-3 rtl:space-x-reverse">
                <i data-lucide="mic" class="w-5 h-5 text-bronze flex-shrink-0 mt-0.5"></i>
                <span><strong>Acoustic Ambient Audit:</strong> Analyzes surrounding traffic or industrial frequencies to determine optimal decibel drop.</span>
              </li>
              <li class="flex items-start space-x-3 rtl:space-x-reverse">
                <i data-lucide="sun-medium" class="w-5 h-5 text-bronze flex-shrink-0 mt-0.5"></i>
                <span><strong>Solar Heat Load Modelling:</strong> Calculates SHGC to recommend double vs. triple glazing for each building facade.</span>
              </li>
            </ul>

            <div class="pt-2">
              <a href="contact.html#measurement-booking" class="w-full sm:w-auto bronze-gradient-btn px-6 py-3 rounded-xl text-xs uppercase font-bold tracking-wider inline-flex items-center justify-center space-x-2 rtl:space-x-reverse">
                <span>Book Free Site Measurement</span>
                <i data-lucide="calendar" class="w-4 h-4"></i>
              </a>
            </div>
          </div>

          <div class="lg:col-span-6 relative" data-aos="fade-left">
            <div class="rounded-3xl overflow-hidden shadow-2xl border-4 border-white dark:border-[#12181F] aspect-[4/3]">
              <img src="https://images.unsplash.com/photo-1581094794329-c8112a89af12?auto=format&fit=crop&w=1000&q=80" 
                   alt="Digital 3D laser measurement and blueprint verification" 
                   class="w-full h-full object-cover">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4: UPVC INSTALLATION, REPLACEMENT & MAINTENANCE SERVICES -->
    <section class="py-24 px-4 sm:px-8 bg-ivory dark:bg-[#12181F]">
      <div class="max-w-7xl mx-auto space-y-16">
        <div class="flex flex-col md:items-center xl:flex-row xl:items-end justify-between md:text-center xl:text-left gap-6 max-w-2xl md:max-w-3xl xl:max-w-7xl md:mx-auto xl:mx-0" data-aos="fade-up">
          <div class="max-w-2xl">
            <span class="text-xs uppercase font-bold tracking-widest text-bronze block mb-2">Service 03 & 04</span>
            <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight">
              Turnkey Installation & Lifelong Maintenance
            </h2>
          </div>
          <p class="text-charcoal/70 dark:text-stone-300 text-sm max-w-md md:max-w-xl xl:max-w-md">
            Executed exclusively by VISTRAL certified factory crews adhering strictly to European DIN 18055 anchoring protocols.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
          <!-- 1. New Construction Installation -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 space-y-4 shadow-sm" data-aos="fade-up">
            <div class="w-12 h-12 rounded-2xl bg-bronze/15 text-bronze flex items-center justify-center">
              <i data-lucide="building" class="w-6 h-6"></i>
            </div>
            <h3 class="font-display text-xl font-bold text-charcoal dark:text-white">New Build Glazing</h3>
            <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Full structural anchoring using heavy masonry fixings, non-expanding polyurethane perimeter insulation, and weather-tight EPDM vapor membranes.
            </p>
          </div>

          <!-- 2. Retrofit Replacement -->
          <div class="p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 space-y-4 shadow-sm" data-aos="fade-up" data-aos-delay="100">
            <div class="w-12 h-12 rounded-2xl bg-bronze/15 text-bronze flex items-center justify-center">
              <i data-lucide="refresh-cw" class="w-6 h-6"></i>
            </div>
            <h3 class="font-display text-xl font-bold text-charcoal dark:text-white">Retrofit Replacement</h3>
            <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Surgically remove aged leaking wooden or aluminum windows with zero damage to interior plaster walls, tiles, or wallpaper. Completed within a single day.
            </p>
          </div>

          <!-- 3. Annual Maintenance & Gasket Audits -->
          <div class="md:col-span-2 md:w-[calc(50%-1rem)] md:mx-auto xl:col-span-1 xl:w-full xl:mx-0 p-8 rounded-3xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 space-y-4 shadow-sm" data-aos="fade-up" data-aos-delay="200">
            <div class="w-12 h-12 rounded-2xl bg-bronze/15 text-bronze flex items-center justify-center">
              <i data-lucide="wrench" class="w-6 h-6"></i>
            </div>
            <h3 class="font-display text-xl font-bold text-charcoal dark:text-white">Maintenance & Tune-Up</h3>
            <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Hardware lubrication with silicone spray, gasket elasticity verification, roller realignment, and sash tension adjustment for smooth lifelong gliding.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: SERVICE PROCESS, CUSTOMER SUPPORT & FREE QUOTATION CTA -->
    <section class="py-24 px-4 sm:px-8 bg-charcoal text-white relative overflow-hidden">
      <div class="max-w-7xl mx-auto space-y-16">
        <div class="text-center max-w-3xl mx-auto" data-aos="fade-up">
          <span class="text-xs uppercase font-bold tracking-widest text-bronze font-mono block mb-2">Service Lifecycle</span>
          <h2 class="font-display text-3xl sm:text-5xl font-extrabold tracking-tight text-white">
            The VISTRAL Service Guarantee
          </h2>
          <p class="text-sm text-stone-300 mt-3">
            Clear communication, predictable delivery milestones, and 24/7 dedicated customer service.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6 text-center" data-aos="fade-up">
          <div class="p-6 rounded-2xl bg-white/5 border border-white/10 space-y-2">
            <span class="text-3xl font-display font-extrabold text-bronze">24h</span>
            <h4 class="font-display font-bold text-base text-white">Quotation Turnaround</h4>
            <p class="text-xs text-stone-300">Detailed itemized pricing delivered within 1 business day.</p>
          </div>

          <div class="p-6 rounded-2xl bg-white/5 border border-white/10 space-y-2">
            <span class="text-3xl font-display font-extrabold text-bronze">14 Days</span>
            <h4 class="font-display font-bold text-base text-white">Rapid Fabrication</h4>
            <p class="text-xs text-stone-300">Fast-track computerized manufacturing queue.</p>
          </div>

          <div class="p-6 rounded-2xl bg-white/5 border border-white/10 space-y-2">
            <span class="text-3xl font-display font-extrabold text-bronze">100%</span>
            <h4 class="font-display font-bold text-base text-white">Certified Technicians</h4>
            <p class="text-xs text-stone-300">No third-party untrained subcontracting.</p>
          </div>

          <div class="p-6 rounded-2xl bg-white/5 border border-white/10 space-y-2">
            <span class="text-3xl font-display font-extrabold text-bronze">20 Yrs</span>
            <h4 class="font-display font-bold text-base text-white">Direct Warranty</h4>
            <p class="text-xs text-stone-300">Comprehensive profile & hardware guarantee.</p>
          </div>
        </div>

        <div class="p-8 sm:p-12 rounded-3xl bg-gradient-to-r from-bronze/20 via-white/5 to-bronze/10 border border-bronze/30 text-center space-y-6" data-aos="zoom-in">
          <h3 class="font-display text-2xl sm:text-4xl font-extrabold text-white">
            Request Your Complimentary Site Measurement & Quote
          </h3>
          <p class="text-xs sm:text-sm text-stone-300 max-w-xl mx-auto leading-relaxed">
            Our fenestration engineer will visit your property with physical profile swatches and laser survey tools to provide a precise estimate.
          </p>
          <div class="flex flex-col sm:flex-row items-stretch sm:items-center justify-center gap-4">
            <a href="contact.html#measurement-booking" class="w-full sm:w-auto bronze-gradient-btn px-8 py-4 rounded-xl text-xs uppercase font-bold tracking-wider inline-flex items-center justify-center space-x-2 rtl:space-x-reverse shadow-xl">
              <span>Book Appointment Online</span>
              <i data-lucide="calendar" class="w-4 h-4"></i>
            </a>
            <a href="tel:18004827832" class="w-full sm:w-auto px-8 py-4 rounded-xl text-xs uppercase font-bold tracking-wider bg-white/10 hover:bg-white/20 border border-white/20 text-white inline-flex items-center justify-center space-x-2 rtl:space-x-reverse transition-all">
              <i data-lucide="phone" class="w-4 h-4 text-bronze"></i>
              <span>Call Toll Free: +1 (800) 482-7832</span>
            </a>
          </div>
        </div>
      </div>
    </section>
  </main>
"""
    content += get_footer()
    
    with open("services.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("services.html (Services - exactly 5 sections) generated successfully.")

if __name__ == "__main__":
    build_services()

