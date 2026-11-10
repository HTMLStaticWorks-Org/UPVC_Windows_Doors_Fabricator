/**
 * VISTRAL UPVC Architectural Systems - Main JavaScript Engine
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initRTL();
  initStickyHeader();
  initMobileMenu();
  initCounters();
  initGallery();
  initForms();
  initPasswordToggles();
  initInteractiveShowcase();
  initBackToTop();
  initAOS();
  lucide.createIcons();
});

/* -------------------------------------------------------------------------- */
/* Back to Top / Scroll Direction Management (Visible across all sections)    */
/* -------------------------------------------------------------------------- */
function initBackToTop() {
  const floatingBtn = document.getElementById('floatingScrollBtn');
  const scrollDownIcon = document.getElementById('scrollDownIcon');
  const scrollUpIcon = document.getElementById('scrollUpIcon');
  const footerBtns = document.querySelectorAll('.back-to-top-btn');

  function updateScrollState() {
    if (!floatingBtn || !scrollDownIcon || !scrollUpIcon) return;
    const scrollY = window.scrollY || window.pageYOffset || document.documentElement.scrollTop;
    const isScrolled = scrollY > 200;

    if (isScrolled) {
      scrollDownIcon.classList.add('hidden');
      scrollUpIcon.classList.remove('hidden');
      floatingBtn.setAttribute('title', 'Back to Top');
      floatingBtn.setAttribute('aria-label', 'Back to Top');
    } else {
      scrollDownIcon.classList.remove('hidden');
      scrollUpIcon.classList.add('hidden');
      floatingBtn.setAttribute('title', 'Scroll Down');
      floatingBtn.setAttribute('aria-label', 'Scroll Down');
    }
  }

  if (floatingBtn) {
    floatingBtn.addEventListener('click', (e) => {
      e.preventDefault();
      if (window.scrollY > 300) {
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      } else {
        window.scrollTo({
          top: window.innerHeight * 0.9,
          behavior: 'smooth'
        });
      }
    });

    window.addEventListener('scroll', updateScrollState, { passive: true });
    updateScrollState();
  }

  footerBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  });
}

/* -------------------------------------------------------------------------- */
/* Theme Management (Light / Dark)                                            */
/* -------------------------------------------------------------------------- */
function initTheme() {
  const savedTheme = localStorage.getItem('vistral_theme') || 
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  
  if (savedTheme === 'dark') {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
  
  updateThemeIcons(savedTheme);

  const themeToggles = document.querySelectorAll('.theme-toggle');
  themeToggles.forEach(btn => {
    btn.addEventListener('click', () => {
      const isDark = document.documentElement.classList.toggle('dark');
      const newTheme = isDark ? 'dark' : 'light';
      localStorage.setItem('vistral_theme', newTheme);
      updateThemeIcons(newTheme);
      showToast(`Switched to ${newTheme.toUpperCase()} mode`, 'info');
      if (window.lucide) lucide.createIcons();
    });
  });
}

function updateThemeIcons(theme) {
  const icons = document.querySelectorAll('.theme-icon');
  icons.forEach(icon => {
    if (theme === 'dark') {
      icon.setAttribute('data-lucide', 'sun');
    } else {
      icon.setAttribute('data-lucide', 'moon');
    }
  });
  if (window.lucide) lucide.createIcons();
}

/* -------------------------------------------------------------------------- */
/* RTL Management                                                             */
/* -------------------------------------------------------------------------- */
function initRTL() {
  const savedRTL = localStorage.getItem('vistral_rtl') === 'true';
  if (savedRTL) {
    document.documentElement.setAttribute('dir', 'rtl');
  } else {
    document.documentElement.setAttribute('dir', 'ltr');
  }

  const rtlToggles = document.querySelectorAll('.rtl-toggle');
  rtlToggles.forEach(btn => {
    btn.addEventListener('click', () => {
      const currentDir = document.documentElement.getAttribute('dir');
      const isRTL = currentDir === 'rtl';
      const newDir = isRTL ? 'ltr' : 'rtl';
      document.documentElement.setAttribute('dir', newDir);
      localStorage.setItem('vistral_rtl', (!isRTL).toString());
      showToast(`Switched to ${newDir.toUpperCase()} layout`, 'info');
      updateRTLButtonText(!isRTL);
    });
  });
  updateRTLButtonText(savedRTL);
}

function updateRTLButtonText(isRTL) {
  const rtlBadges = document.querySelectorAll('.rtl-badge');
  rtlBadges.forEach(badge => {
    badge.textContent = isRTL ? 'LTR' : 'RTL';
  });
  const rtlToggles = document.querySelectorAll('.rtl-toggle');
  rtlToggles.forEach(btn => {
    btn.setAttribute('aria-label', isRTL ? 'Switch to Left-to-Right (LTR)' : 'Switch to Right-to-Left (RTL)');
    btn.title = isRTL ? 'Switch to Left-to-Right (LTR)' : 'Switch to Right-to-Left (RTL)';
    if (isRTL) {
      btn.classList.add('bg-bronze/15', 'border-bronze', 'text-bronze');
    } else {
      btn.classList.remove('bg-bronze/15', 'border-bronze', 'text-bronze');
    }
  });
}

/* -------------------------------------------------------------------------- */
/* Sticky Header Behavior                                                     */
/* -------------------------------------------------------------------------- */
function initStickyHeader() {
  const header = document.querySelector('header');
  if (!header) return;

  const handleScroll = () => {
    if (window.scrollY > 20) {
      header.classList.add('shadow-md');
    } else {
      header.classList.remove('shadow-md');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}

/* -------------------------------------------------------------------------- */
/* Mobile Hamburger Navigation                                                */
/* -------------------------------------------------------------------------- */
function initMobileMenu() {
  const toggleBtn = document.getElementById('mobileMenuToggle');
  const menuDrawer = document.getElementById('mobileMenuDrawer');
  const closeBtn = document.getElementById('mobileMenuClose');
  const backdrop = document.getElementById('mobileMenuBackdrop');

  if (!toggleBtn || !menuDrawer) return;

  function openMenu() {
    menuDrawer.classList.remove('invisible', 'translate-x-full', '-translate-x-full', 'rtl:-translate-x-full');
    menuDrawer.classList.add('drawer-open');
    if (backdrop) backdrop.classList.remove('opacity-0', 'pointer-events-none');
    document.body.classList.add('overflow-hidden');
  }

  function closeMenu() {
    menuDrawer.classList.remove('drawer-open');
    if (backdrop) backdrop.classList.add('opacity-0', 'pointer-events-none');
    setTimeout(() => {
      if (!menuDrawer.classList.contains('drawer-open')) {
        menuDrawer.classList.add('invisible');
      }
    }, 300);
    document.body.classList.remove('overflow-hidden');
  }

  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    openMenu();
  });
  if (closeBtn) closeBtn.addEventListener('click', closeMenu);
  if (backdrop) backdrop.addEventListener('click', closeMenu);

  const drawerLinks = menuDrawer.querySelectorAll('a');
  drawerLinks.forEach(link => {
    link.addEventListener('click', () => {
      closeMenu();
    });
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMenu();
  });
}

/* -------------------------------------------------------------------------- */
/* Animated Statistics Counters                                               */
/* -------------------------------------------------------------------------- */
function initCounters() {
  const counters = document.querySelectorAll('[data-counter]');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.getAttribute('data-counter'), 10);
        const suffix = el.getAttribute('data-suffix') || '';
        const duration = 1800;
        const start = 0;
        const startTime = performance.now();

        function updateCounter(currentTime) {
          const elapsed = currentTime - startTime;
          const progress = Math.min(elapsed / duration, 1);
          // Ease out cubic
          const easeProgress = 1 - Math.pow(1 - progress, 3);
          const current = Math.floor(start + (target - start) * easeProgress);
          el.textContent = current.toLocaleString() + suffix;

          if (progress < 1) {
            requestAnimationFrame(updateCounter);
          } else {
            el.textContent = target.toLocaleString() + suffix;
          }
        }
        requestAnimationFrame(updateCounter);
        obs.unobserve(el);
      }
    });
  }, { threshold: 0.3 });

  counters.forEach(counter => observer.observe(counter));
}

/* -------------------------------------------------------------------------- */
/* Gallery Filtering & Lightbox Modal                                         */
/* -------------------------------------------------------------------------- */
let galleryItems = [];
let currentLightboxIndex = 0;

function initGallery() {
  const filterBtns = document.querySelectorAll('.gallery-filter-btn');
  const items = document.querySelectorAll('.gallery-item');
  const lightbox = document.getElementById('lightboxModal');

  if (!items.length) return;

  galleryItems = Array.from(items).map((item, index) => {
    const img = item.querySelector('img');
    const title = item.querySelector('.gallery-title')?.textContent || 'UPVC Architectural Project';
    const category = item.getAttribute('data-category') || 'All';
    
    // Attach click to open lightbox
    item.addEventListener('click', () => {
      openLightbox(index);
    });

    return {
      index,
      element: item,
      src: img?.getAttribute('src') || '',
      alt: img?.getAttribute('alt') || '',
      title,
      category
    };
  });

  // Filter functionality
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => {
        b.classList.remove('bg-amber-700', 'text-white', 'active');
        b.classList.add('bg-stone-200', 'dark:bg-stone-800', 'text-stone-700', 'dark:text-stone-300');
      });
      btn.classList.add('bg-amber-700', 'text-white', 'active');
      btn.classList.remove('bg-stone-200', 'dark:bg-stone-800', 'text-stone-700', 'dark:text-stone-300');

      const filter = (btn.getAttribute('data-filter') || 'all').toLowerCase();

      items.forEach(item => {
        const itemCat = (item.getAttribute('data-category') || '').toLowerCase();
        let matches = false;

        if (filter === 'all') {
          matches = true;
        } else if (filter === 'windows') {
          matches = itemCat.includes('window');
        } else if (filter === 'doors') {
          matches = itemCat.includes('door');
        } else if (filter === 'residential') {
          matches = itemCat.includes('residential');
        } else if (filter === 'commercial') {
          matches = itemCat.includes('commercial');
        } else {
          matches = itemCat.includes(filter);
        }

        if (matches) {
          item.style.display = '';
          item.classList.remove('hidden');
          item.classList.remove('animate-fadeIn');
          void item.offsetWidth;
          item.classList.add('animate-fadeIn');
        } else {
          item.style.display = 'none';
        }
      });

      // Update tier section visibility so empty sections do not show blank space
      const tierSections = document.querySelectorAll('.gallery-tier-section');
      tierSections.forEach(section => {
        const sectionItems = section.querySelectorAll('.gallery-item');
        const hasVisible = Array.from(sectionItems).some(it => it.style.display !== 'none');
        section.style.display = hasVisible ? '' : 'none';
      });
    });
  });

  if (lightbox) {
    const closeBtn = document.getElementById('lightboxClose');
    const prevBtn = document.getElementById('lightboxPrev');
    const nextBtn = document.getElementById('lightboxNext');

    if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
    if (prevBtn) prevBtn.addEventListener('click', prevLightbox);
    if (nextBtn) nextBtn.addEventListener('click', nextLightbox);

    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox || e.target.classList.contains('lightbox-backdrop')) {
        closeLightbox();
      }
    });

    document.addEventListener('keydown', (e) => {
      if (lightbox.classList.contains('hidden')) return;
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowLeft') prevLightbox();
      if (e.key === 'ArrowRight') nextLightbox();
    });
  }
}

function openLightbox(index) {
  const lightbox = document.getElementById('lightboxModal');
  if (!lightbox || !galleryItems[index]) return;

  currentLightboxIndex = index;
  renderLightboxContent();
  lightbox.classList.remove('hidden');
  document.body.classList.add('overflow-hidden');
}

function closeLightbox() {
  const lightbox = document.getElementById('lightboxModal');
  if (!lightbox) return;
  lightbox.classList.add('hidden');
  document.body.classList.remove('overflow-hidden');
}

function getVisibleGalleryIndices() {
  const visible = [];
  galleryItems.forEach(item => {
    if (item.element && item.element.style.display !== 'none') {
      visible.push(item.index);
    }
  });
  return visible.length ? visible : galleryItems.map(it => it.index);
}

function prevLightbox() {
  const visible = getVisibleGalleryIndices();
  const currentPos = visible.indexOf(currentLightboxIndex);
  if (currentPos === -1) {
    currentLightboxIndex = visible[visible.length - 1];
  } else {
    currentLightboxIndex = visible[(currentPos - 1 + visible.length) % visible.length];
  }
  renderLightboxContent();
}

function nextLightbox() {
  const visible = getVisibleGalleryIndices();
  const currentPos = visible.indexOf(currentLightboxIndex);
  if (currentPos === -1) {
    currentLightboxIndex = visible[0];
  } else {
    currentLightboxIndex = visible[(currentPos + 1) % visible.length];
  }
  renderLightboxContent();
}

function renderLightboxContent() {
  const data = galleryItems[currentLightboxIndex];
  if (!data) return;

  const imgEl = document.getElementById('lightboxImg');
  const titleEl = document.getElementById('lightboxTitle');
  const catEl = document.getElementById('lightboxCategory');

  if (imgEl) {
    imgEl.src = data.src;
    imgEl.alt = data.alt;
  }
  if (titleEl) titleEl.textContent = data.title;
  if (catEl) catEl.textContent = data.category.toUpperCase();
}

/* -------------------------------------------------------------------------- */
/* Password Visibility Toggles                                                */
/* -------------------------------------------------------------------------- */
function initPasswordToggles() {
  const toggles = document.querySelectorAll('.password-toggle-btn');
  toggles.forEach(btn => {
    btn.addEventListener('click', () => {
      const input = btn.parentElement.querySelector('input');
      const icon = btn.querySelector('i, svg');
      if (!input) return;

      if (input.type === 'password') {
        input.type = 'text';
        btn.setAttribute('aria-label', 'Hide password');
        if (icon) {
          icon.setAttribute('data-lucide', 'eye-off');
          if (window.lucide) lucide.createIcons();
        }
      } else {
        input.type = 'password';
        btn.setAttribute('aria-label', 'Show password');
        if (icon) {
          icon.setAttribute('data-lucide', 'eye');
          if (window.lucide) lucide.createIcons();
        }
      }
    });
  });
}

/* -------------------------------------------------------------------------- */
/* Interactive Showcase / Comparison Widget                                   */
/* -------------------------------------------------------------------------- */
function initInteractiveShowcase() {
  // Acoustic & thermal benefit switcher
  const acousticSlider = document.getElementById('soundproofSlider');
  const dbDisplay = document.getElementById('decibelDisplay');
  const soundStatus = document.getElementById('soundStatus');

  if (acousticSlider && dbDisplay && soundStatus) {
    acousticSlider.addEventListener('input', (e) => {
      const val = parseInt(e.target.value, 10);
      dbDisplay.textContent = `${val} dB`;
      if (val <= 30) {
        soundStatus.textContent = 'Whisper Quiet (VISTRAL Multi-Chamber Glazed)';
        soundStatus.className = 'text-emerald-500 font-semibold';
      } else if (val <= 55) {
        soundStatus.textContent = 'Standard Residential Window Ambient Noise';
        soundStatus.className = 'text-amber-500 font-semibold';
      } else {
        soundStatus.textContent = 'Loud Urban Traffic & Construction Noise';
        soundStatus.className = 'text-rose-500 font-semibold';
      }
    });
  }

  // Interactive Product Tabs in Home 2
  const productTabs = document.querySelectorAll('.style-tab-btn');
  const productPanes = document.querySelectorAll('.style-tab-pane');

  if (productTabs.length) {
    productTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const target = tab.getAttribute('data-target');
        productTabs.forEach(t => {
          t.classList.remove('active', 'border-amber-600', 'text-amber-600', 'dark:text-amber-400');
          t.classList.add('border-transparent', 'text-stone-500');
        });
        tab.classList.add('active', 'border-amber-600', 'text-amber-600', 'dark:text-amber-400');
        tab.classList.remove('border-transparent', 'text-stone-500');

        productPanes.forEach(pane => {
          if (pane.id === target) {
            pane.classList.remove('hidden');
            pane.classList.add('grid');
          } else {
            pane.classList.add('hidden');
            pane.classList.remove('grid');
          }
        });
      });
    });
  }
}

/* -------------------------------------------------------------------------- */
/* Form Validations & Submissions                                             */
/* -------------------------------------------------------------------------- */
function initForms() {
  // Free Site Measurement Form
  const measurementForm = document.getElementById('measurementForm');
  if (measurementForm) {
    measurementForm.addEventListener('submit', (e) => {
      e.preventDefault();
      if (validateForm(measurementForm)) {
        showToast('Site Measurement Request Booked! Our architectural engineer will contact you.', 'success');
        measurementForm.reset();
      }
    });
  }

  // Contact Enquiry Form
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      if (validateForm(contactForm)) {
        showToast('Thank you! Your architectural enquiry has been dispatched.', 'success');
        contactForm.reset();
      }
    });
  }

  // Auth Forms
  const loginForm = document.getElementById('loginForm');
  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      if (validateForm(loginForm)) {
        showToast('Authentication successful. Welcome to VISTRAL Client Portal!', 'success');
        setTimeout(() => {
          window.location.href = 'index.html';
        }, 1200);
      }
    });
  }

  const signupForm = document.getElementById('signupForm');
  if (signupForm) {
    signupForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const pwd = signupForm.querySelector('#signupPassword')?.value;
      const confirmPwd = signupForm.querySelector('#signupConfirmPassword')?.value;

      if (pwd && confirmPwd && pwd !== confirmPwd) {
        showToast('Passwords do not match. Please verify.', 'error');
        return;
      }

      if (validateForm(signupForm)) {
        showToast('Account created successfully! Redirecting to login...', 'success');
        setTimeout(() => {
          window.location.href = 'login.html';
        }, 1500);
      }
    });
  }

  // Newsletter Form in Footer
  const newsletterForms = document.querySelectorAll('.newsletter-form');
  newsletterForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = form.querySelector('input[type="email"]');
      if (email && email.value) {
        showToast('Subscribed to VISTRAL Architectural Gazette!', 'success');
        form.reset();
      }
    });
  });
}

function validateForm(form) {
  let isValid = true;
  const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
  
  inputs.forEach(input => {
    if (!input.value.trim()) {
      isValid = false;
      input.classList.add('border-rose-500', 'ring-1', 'ring-rose-500');
    } else {
      input.classList.remove('border-rose-500', 'ring-1', 'ring-rose-500');
    }

    if (input.type === 'email' && input.value) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(input.value)) {
        isValid = false;
        input.classList.add('border-rose-500', 'ring-1', 'ring-rose-500');
      }
    }
  });

  const terms = form.querySelector('input[type="checkbox"][required]');
  if (terms && !terms.checked) {
    isValid = false;
    showToast('Please agree to the Terms & Conditions.', 'error');
  }

  if (!isValid) {
    showToast('Please check all highlighted required fields.', 'error');
  }
  return isValid;
}

/* -------------------------------------------------------------------------- */
/* Global Toast Notification                                                  */
/* -------------------------------------------------------------------------- */
function showToast(message, type = 'info') {
  let toast = document.getElementById('globalToast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'globalToast';
    toast.className = 'fixed bottom-6 right-6 z-50 transform translate-y-20 opacity-0 pointer-events-none transition-all duration-300 max-w-md px-5 py-4 rounded-xl shadow-2xl flex items-center space-x-3 text-sm font-medium';
    document.body.appendChild(toast);
  }

  // Colors based on type
  if (type === 'success') {
    toast.className = 'fixed bottom-6 right-6 z-50 max-w-md px-5 py-4 rounded-xl shadow-2xl flex items-center space-x-3 text-sm font-medium bg-emerald-900 text-emerald-100 border border-emerald-700/50 transition-all duration-300 transform translate-y-0 opacity-100';
  } else if (type === 'error') {
    toast.className = 'fixed bottom-6 right-6 z-50 max-w-md px-5 py-4 rounded-xl shadow-2xl flex items-center space-x-3 text-sm font-medium bg-rose-900 text-rose-100 border border-rose-700/50 transition-all duration-300 transform translate-y-0 opacity-100';
  } else {
    toast.className = 'fixed bottom-6 right-6 z-50 max-w-md px-5 py-4 rounded-xl shadow-2xl flex items-center space-x-3 text-sm font-medium bg-[#202A32] text-stone-100 border border-[#B68B58]/40 transition-all duration-300 transform translate-y-0 opacity-100';
  }

  toast.innerHTML = `
    <div class="flex items-center space-x-3 rtl:space-x-reverse">
      <span class="inline-block w-2.5 h-2.5 rounded-full ${type === 'success' ? 'bg-emerald-400' : type === 'error' ? 'bg-rose-400' : 'bg-[#B68B58]'}"></span>
      <span>${message}</span>
    </div>
  `;

  setTimeout(() => {
    toast.classList.remove('translate-y-0', 'opacity-100');
    toast.classList.add('translate-y-20', 'opacity-0');
  }, 4000);
}

/* -------------------------------------------------------------------------- */
/* Lightweight Animation Fallback (AOS style)                                 */
/* -------------------------------------------------------------------------- */
function initAOS() {
  if (window.AOS) {
    AOS.init({
      duration: 800,
      once: true,
      easing: 'ease-out-cubic',
      offset: 60
    });
  }
}

