import os
from templates import get_head, get_header, get_footer

def build_about():
    content = get_head("About Us - Architectural Heritage & Precision", "about")
    content += get_header("about")
    content += """
  <main class="flex-grow">
    <!-- SECTION 1: PREMIUM ABOUT HERO -->
    <section class="relative min-h-[55vh] flex items-center justify-center overflow-hidden py-24 px-4 sm:px-8 bg-charcoal text-white">
      <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=2000&q=85" 
             alt="VISTRAL Architectural corporate headquarters and design atrium" 
             class="w-full h-full object-cover filter brightness-[0.38]">
        <div class="absolute inset-0 bg-gradient-to-t from-charcoal via-charcoal/70 to-transparent"></div>
      </div>

      <div class="relative z-10 max-w-4xl mx-auto text-center space-y-6" data-aos="fade-up">
        <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-bronze-200 text-xs uppercase tracking-widest font-mono font-semibold rtl:space-x-reverse">
          <span class="w-2 h-2 rounded-full bg-bronze"></span>
          <span>Architectural Fenestration Pioneers Since 1998</span>
        </div>

        <h1 class="font-display font-extrabold text-4xl sm:text-6xl tracking-tight text-white leading-tight">
          Crafting Architectural Clarity. <br>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-bronze-200 via-bronze to-bronze-400">Engineering Silence</span>.
        </h1>

        <p class="text-base sm:text-lg text-stone-200 max-w-2xl mx-auto font-normal leading-relaxed">
          From a boutique Bavarian extrusion studio to an international leader in custom UPVC architectural window and door engineering.
        </p>
      </div>
    </section>

    <!-- SECTION 2: COMPANY STORY, VISION, MISSION & FABRICATION EXPERTISE -->
    <section class="py-24 px-4 sm:px-8 bg-ivory dark:bg-[#12181F] architectural-grid">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          <!-- Editorial Overlapping Images -->
          <div class="lg:col-span-6 relative" data-aos="fade-right">
            <div class="rounded-3xl overflow-hidden shadow-2xl border-4 border-white dark:border-[#182029] aspect-[4/3] max-w-[88%]">
              <img src="https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1000&q=80" 
                   alt="VISTRAL precision design studio" 
                   class="w-full h-full object-cover">
            </div>
            <div class="absolute -bottom-8 -right-4 w-3/5 rounded-2xl overflow-hidden shadow-2xl border-4 border-white dark:border-[#182029] hidden sm:block">
              <img src="https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=700&q=80" 
                   alt="Architectural profile showroom" 
                   class="w-full h-full object-cover">
            </div>
          </div>

          <!-- Narrative: Story, Vision, Mission -->
          <div class="lg:col-span-6 space-y-6" data-aos="fade-left">
            <div class="flex items-center space-x-2 rtl:space-x-reverse">
              <span class="w-6 h-0.5 bg-bronze"></span>
              <span class="text-xs uppercase font-bold tracking-widest text-bronze">Our Heritage</span>
            </div>

            <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight leading-tight">
              A Legacy of Precision & Environmental Stewardship
            </h2>

            <p class="text-sm sm:text-base text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Founded on the belief that windows are not mere glass panes but living architectural filters, VISTRAL was established to overcome the severe limitations of ordinary aluminum and wood. Aluminum conductively bleeds thermal energy; timber warps, rots, and demands hazardous toxic varnishing.
            </p>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
              <div class="p-5 rounded-2xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm">
                <div class="w-10 h-10 rounded-xl bg-bronze/15 text-bronze flex items-center justify-center mb-3">
                  <i data-lucide="compass" class="w-5 h-5"></i>
                </div>
                <h4 class="font-display font-bold text-base text-charcoal dark:text-white">Our Mission</h4>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 mt-1.5 leading-relaxed">
                  To empower architects with high-performance, maintenance-free fenestration systems that dramatically decrease building energy footprints.
                </p>
              </div>

              <div class="p-5 rounded-2xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 shadow-sm">
                <div class="w-10 h-10 rounded-xl bg-bronze/15 text-bronze flex items-center justify-center mb-3">
                  <i data-lucide="eye" class="w-5 h-5"></i>
                </div>
                <h4 class="font-display font-bold text-base text-charcoal dark:text-white">Our Vision</h4>
                <p class="text-xs text-charcoal/70 dark:text-stone-300 mt-1.5 leading-relaxed">
                  A carbon-neutral global built environment where every residence enjoys acoustic silence and pristine natural illumination.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: MANUFACTURING CAPABILITIES & QUALITY STANDARDS -->
    <section id="quality-standards" class="py-24 px-4 sm:px-8 bg-white dark:bg-[#182029] border-y border-charcoal/10 dark:border-white/10">
      <div class="max-w-7xl mx-auto space-y-16">
        <div class="flex flex-col md:items-center xl:flex-row xl:items-end justify-between md:text-center xl:text-left gap-6 max-w-2xl md:max-w-3xl xl:max-w-7xl md:mx-auto xl:mx-0" data-aos="fade-up">
          <div class="max-w-2xl">
            <span class="text-xs uppercase font-bold tracking-widest text-bronze block mb-2">Industrial Prowess</span>
            <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight">
              Manufacturing Capabilities & Quality Standards
            </h2>
          </div>
          <p class="text-charcoal/70 dark:text-stone-300 text-sm max-w-md md:max-w-xl xl:max-w-md">
            Operating a 75,000 sq.ft computerized fabrication facility featuring German robotic lines certified under ISO 9001 and CE EN 14351-1.
          </p>
        </div>

        <!-- Bento Grid of Capabilities -->
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
          <!-- Card 1 -->
          <div class="p-8 rounded-3xl bg-ivory dark:bg-[#12181F] border border-charcoal/10 dark:border-white/10 space-y-4 shadow-sm" data-aos="fade-up">
            <div class="rounded-2xl overflow-hidden aspect-[16/9] mb-4">
              <img src="https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?auto=format&fit=crop&w=700&q=80" 
                   alt="Robotic corner welding machinery" 
                   class="w-full h-full object-cover">
            </div>
            <span class="text-xs font-mono font-bold text-bronze uppercase">01 &bull; Seamless Fusion</span>
            <h3 class="font-display text-xl font-bold text-charcoal dark:text-white">Robotic 4-Point Welding</h3>
            <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
              All 4 corners of sash and frame are heated to precisely 245°C and fused under 35 kN hydraulic pressure simultaneously for unbreakable structural joints.
            </p>
          </div>

          <!-- Card 2 -->
          <div class="p-8 rounded-3xl bg-ivory dark:bg-[#12181F] border border-charcoal/10 dark:border-white/10 space-y-4 shadow-sm" data-aos="fade-up" data-aos-delay="100">
            <div class="rounded-2xl overflow-hidden aspect-[16/9] mb-4">
              <img src="https://images.unsplash.com/photo-1581092162384-8987c1d64718?auto=format&fit=crop&w=700&q=80" 
                   alt="Quality assurance testing chamber" 
                   class="w-full h-full object-cover">
            </div>
            <span class="text-xs font-mono font-bold text-bronze uppercase">02 &bull; Hurricane Simulation</span>
            <h3 class="font-display text-xl font-bold text-charcoal dark:text-white">Wind & Water Testing</h3>
            <p class="text-xs text-charcoal/70 dark:text-stone-300 leading-relaxed">
              Every production batch is tested in a closed pneumatic test chamber simulating 2,400 Pa positive/negative wind loads and 45 liter/min water deluges.
            </p>
          </div>

          <!-- Card 3 -->
          <div class="md:col-span-2 md:w-[calc(50%-1rem)] md:mx-auto xl:col-span-1 xl:w-full xl:mx-0 p-8 rounded-3xl bg-ivory dark:bg-[#12181F] border border-charcoal/10 dark:border-white/10 space-y-4 shadow-sm" data-aos="fade-up" data-aos-delay="200">
            <div class="w-14 h-14 rounded-2xl bg-bronze/15 text-bronze flex items-center justify-center mb-6">
              <i data-lucide="check-check" class="w-7 h-7"></i>
            </div>
            <span class="text-xs font-mono font-bold text-bronze uppercase">03 &bull; Global Compliance</span>
            <h3 class="font-display text-xl font-bold text-charcoal dark:text-white">Certified Standards</h3>
            <ul class="text-xs space-y-2 text-charcoal/70 dark:text-stone-300 pt-2">
              <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-2 rtl:ml-2"></i> DIN 18055 (Air Permeability Class 4)</li>
              <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-2 rtl:ml-2"></i> BS 6375 (Weather Tightness Category E)</li>
              <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-2 rtl:ml-2"></i> ASTM E283 & E330 (Structural Load)</li>
              <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-bronze mr-2 rtl:ml-2"></i> Lead-Free Calcium-Zinc Green Formulation</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4: OUR TEAM, TECHNOLOGY & PROFESSIONAL INSTALLATION EXPERTISE -->
    <section class="py-24 px-4 sm:px-8 bg-ivory dark:bg-[#12181F]">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          <div class="lg:col-span-6 space-y-6" data-aos="fade-right">
            <div class="flex items-center space-x-2 rtl:space-x-reverse">
              <span class="w-6 h-0.5 bg-bronze"></span>
              <span class="text-xs uppercase font-bold tracking-widest text-bronze">Master Artisans & Engineers</span>
            </div>

            <h2 class="font-display text-3xl sm:text-5xl font-extrabold text-charcoal dark:text-white tracking-tight leading-tight">
              Certified In-House Technicians. Never Subcontracted.
            </h2>

            <p class="text-sm sm:text-base text-charcoal/70 dark:text-stone-300 leading-relaxed">
              The world's finest UPVC window system will fail if poorly anchored. That is why VISTRAL employs a dedicated in-house team of certified fenestration engineers, precision laser surveyors, and master installation craftsmen.
            </p>

            <div class="space-y-4 pt-2">
              <div class="p-4 rounded-2xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 flex items-center space-x-4 rtl:space-x-reverse">
                <div class="w-12 h-12 rounded-full bg-bronze/15 text-bronze flex items-center justify-center flex-shrink-0">
                  <i data-lucide="users" class="w-6 h-6"></i>
                </div>
                <div>
                  <h4 class="font-display font-bold text-sm text-charcoal dark:text-white">120+ Fenestration Specialists</h4>
                  <p class="text-xs text-charcoal/70 dark:text-stone-300">Continuous annual training at the Rosenheim Fenestration Institute.</p>
                </div>
              </div>

              <div class="p-4 rounded-2xl bg-white dark:bg-[#182029] border border-charcoal/10 dark:border-white/10 flex items-center space-x-4 rtl:space-x-reverse">
                <div class="w-12 h-12 rounded-full bg-bronze/15 text-bronze flex items-center justify-center flex-shrink-0">
                  <i data-lucide="shield-alert" class="w-6 h-6"></i>
                </div>
                <div>
                  <h4 class="font-display font-bold text-sm text-charcoal dark:text-white">Zero Dust & Clean Site Protocol</h4>
                  <p class="text-xs text-charcoal/70 dark:text-stone-300">Full protective floor draping, HEPA vacuum extraction, and white-glove site delivery.</p>
                </div>
              </div>
            </div>
          </div>

          <div class="lg:col-span-6 grid grid-cols-2 gap-4" data-aos="fade-left">
            <div class="rounded-3xl overflow-hidden shadow-xl aspect-[3/4]">
              <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=800&q=80" 
                   alt="Senior engineering leadership team" 
                   class="w-full h-full object-cover">
            </div>
            <div class="rounded-3xl overflow-hidden shadow-xl aspect-[3/4] mt-8">
              <img src="https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=800&q=80" 
                   alt="Certified fenestration installation technicians" 
                   class="w-full h-full object-cover">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: COMPANY ACHIEVEMENTS, CUSTOMER TESTIMONIALS & CONSULTATION CTA -->
    <section class="py-24 px-4 sm:px-8 bg-charcoal text-white relative overflow-hidden">
      <div class="max-w-7xl mx-auto space-y-16">
        <!-- Achievements Row -->
        <div class="grid grid-cols-2 xl:grid-cols-4 gap-6 border-b border-white/15 pb-16" data-aos="fade-up">
          <div class="text-center">
            <span class="block text-4xl sm:text-5xl font-display font-extrabold text-bronze" data-counter="28" data-suffix="+">0</span>
            <span class="text-xs uppercase text-stone-300 font-mono mt-1 block">Years of Innovation</span>
          </div>
          <div class="text-center">
            <span class="block text-4xl sm:text-5xl font-display font-extrabold text-bronze" data-counter="140" data-suffix="M+">0</span>
            <span class="text-xs uppercase text-stone-300 font-mono mt-1 block">Sq.Ft Glazed</span>
          </div>
          <div class="text-center">
            <span class="block text-4xl sm:text-5xl font-display font-extrabold text-bronze" data-counter="18" data-suffix=" Countries">0</span>
            <span class="text-xs uppercase text-stone-300 font-mono mt-1 block">International Presence</span>
          </div>
          <div class="text-center">
            <span class="block text-4xl sm:text-5xl font-display font-extrabold text-bronze" data-counter="32" data-suffix=" Awards">0</span>
            <span class="text-xs uppercase text-stone-300 font-mono mt-1 block">Architectural Honors</span>
          </div>
        </div>

        <!-- Testimonial Highlight & CTA Box -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center" data-aos="fade-up">
          <div class="lg:col-span-6 space-y-4">
            <span class="text-xs font-mono font-bold text-bronze uppercase">Client Spotlight</span>
            <h3 class="font-display text-2xl sm:text-3xl font-bold">
              "VISTRAL sets the global benchmark for fenestration engineering."
            </h3>
            <p class="text-xs sm:text-sm text-stone-300 italic leading-relaxed">
              "We specified VISTRAL systems for our 120-residence eco-development. The thermal performance helped us achieve Platinum LEED status, and the zero-maintenance finish has thrilled every homeowner."
            </p>
            <div class="text-xs text-bronze-200 font-mono">
              &mdash; Jonathan Vance, Chief Architect, Vance Global Design Group
            </div>
          </div>

          <div class="lg:col-span-6 p-8 rounded-3xl bg-white/5 border border-white/10 space-y-6">
            <h4 class="font-display text-2xl font-bold text-white">Consult With Our Engineering Board</h4>
            <p class="text-xs text-stone-300 leading-relaxed">
              Have an upcoming residential or commercial architectural project? Let our senior facade consultants review your structural specifications and suggest optimized profile configurations.
            </p>
            <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
              <a href="contact.html#measurement-booking" class="w-full sm:w-auto bronze-gradient-btn px-7 py-3.5 rounded-xl text-xs uppercase font-bold tracking-wider inline-flex items-center justify-center space-x-2 rtl:space-x-reverse shadow-xl">
                <span>Book Technical Consultation</span>
                <i data-lucide="calendar" class="w-4 h-4"></i>
              </a>
              <a href="products.html" class="w-full sm:w-auto px-7 py-3.5 rounded-xl text-xs uppercase font-bold tracking-wider bg-white/10 hover:bg-white/20 border border-white/20 text-white inline-flex items-center justify-center space-x-2 rtl:space-x-reverse transition-all">
                <span>Download Catalogue</span>
                <i data-lucide="download" class="w-4 h-4 text-bronze"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
"""
    content += get_footer()
    
    with open("about.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("about.html (About Us - exactly 5 sections) generated successfully.")

if __name__ == "__main__":
    build_about()
