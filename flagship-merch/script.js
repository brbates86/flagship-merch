// Mobile Navigation
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
        const expanded = hamburger.classList.contains('active');
        hamburger.setAttribute('aria-expanded', expanded);
    });

    document.querySelectorAll('.nav-link, .nav-cta').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
        });
    });
}

// Navbar scroll state
const navbar = document.querySelector('.navbar');
if (navbar) {
    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 40);
    }, { passive: true });
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href.length <= 1) return;
        const target = document.querySelector(href);
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// Hash-based filter on shop page
function applyHashFilter() {
    const hash = window.location.hash.replace('#', '');
    if (!hash) return;
    const btn = document.querySelector(`.filter-btn[data-filter="${hash}"], .filter-btn#${hash}`);
    if (btn) btn.click();
}

// Shop filters
const filterBtns = document.querySelectorAll('.filter-btn');
const shopCards = document.querySelectorAll('#shopGrid .product-card[data-category]');

if (filterBtns.length && shopCards.length) {
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const filter = btn.dataset.filter;
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            shopCards.forEach(card => {
                const show = filter === 'all' || card.dataset.category === filter;
                card.style.display = show ? '' : 'none';
            });
        });
    });
    applyHashFilter();
    window.addEventListener('hashchange', applyHashFilter);
}

// Scroll reveal
const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// Back to top
const backToTopButton = document.getElementById('backToTop');
if (backToTopButton) {
    window.addEventListener('scroll', () => {
        backToTopButton.classList.toggle('visible', window.scrollY > 400);
    }, { passive: true });

    backToTopButton.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// Cart toast helper
function showToast(message) {
    const toast = document.getElementById('cartToast');
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 2800);
}

// Product page: gallery thumbs
document.querySelectorAll('.product-thumb').forEach(thumb => {
    thumb.addEventListener('click', () => {
        const src = thumb.dataset.src;
        const main = document.getElementById('mainProductImg');
        if (!src || !main) return;
        main.src = src;
        document.querySelectorAll('.product-thumb').forEach(t => t.classList.remove('active'));
        thumb.classList.add('active');
    });
});

// Product page: size selection
document.querySelectorAll('.size-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.size-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    });
});

// Product page: quantity
const qtyInput = document.getElementById('qtyInput');
const qtyMinus = document.getElementById('qtyMinus');
const qtyPlus = document.getElementById('qtyPlus');

if (qtyInput && qtyMinus && qtyPlus) {
    qtyMinus.addEventListener('click', () => {
        const val = Math.max(1, parseInt(qtyInput.value, 10) - 1);
        qtyInput.value = val;
    });
    qtyPlus.addEventListener('click', () => {
        const val = Math.min(10, parseInt(qtyInput.value, 10) + 1);
        qtyInput.value = val;
    });
}

// Add to cart
const addToCartBtn = document.getElementById('addToCart');
if (addToCartBtn) {
    addToCartBtn.addEventListener('click', () => {
        const size = document.querySelector('.size-btn.active')?.dataset.size || 'M';
        const qty = qtyInput?.value || '1';
        showToast(`Added ${qty} × Hoodie (${size}) — WEAR THE FLAG.`);
    });
}

// Newsletter form
const newsletterForm = document.getElementById('newsletterForm');
if (newsletterForm) {
    newsletterForm.addEventListener('submit', (e) => {
        e.preventDefault();
        showToast('Welcome to the Merch Club — WEAR THE FLAG.');
        newsletterForm.reset();
    });
}

// Contact form
const contactForm = document.getElementById('contactForm');
const formMessage = document.getElementById('formMessage');

if (contactForm && formMessage) {
    contactForm.addEventListener('submit', function () {
        formMessage.className = 'form-message loading';
        formMessage.textContent = 'Sending...';

        setTimeout(() => {
            formMessage.className = 'form-message success';
            formMessage.textContent = "Message sent. We'll holler back within 24 hours. WEAR THE FLAG.";
            contactForm.reset();
        }, 1000);
    });
}

// Form validation styling
function validateForm(form) {
    const requiredFields = form.querySelectorAll('[required]');
    let isValid = true;

    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            field.style.boxShadow = '4px 4px 0 #dc3545';
            isValid = false;
        } else {
            field.style.boxShadow = '';
        }
    });

    const emailField = form.querySelector('input[type="email"]');
    if (emailField?.value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(emailField.value)) {
            emailField.style.boxShadow = '4px 4px 0 #dc3545';
            isValid = false;
        }
    }

    return isValid;
}

if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        if (!validateForm(contactForm)) {
            e.preventDefault();
        }
    });
}
