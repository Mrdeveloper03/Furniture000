import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Sagar Sofa's", page_icon="🛋️", layout="wide")

full_page = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
  <style>
    :root{ --accent: #D4AF37; }
    body {
        font-family: 'Poppins', sans-serif;
        background: #f6f7f9;
        color: #333;
        margin: 0;
        padding: 0;
        scroll-behavior: smooth;
    }

    /* Navbar */
    .navbar {
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(10px);
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 14px 40px;
        transition: all 0.4s ease;
    }
    .navbar.scrolled {
        background: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .navbar h1 {
        font-size: 1.3rem;
        color: var(--accent);
        font-weight: 600;
        margin: 0;
    }

    /* Navbar links */
    .nav-links { display: flex; gap: 25px; }
    .nav-links a {
        text-decoration: none; color: #333;
        font-weight: 500; transition: color 0.3s ease;
    }
    .nav-links a:hover { color: var(--accent); }

    /* Hamburger */
    .hamburger { display: none; flex-direction: column; cursor: pointer; width: 25px; height: 20px; justify-content: space-between; }
    .hamburger div { height: 3px; background: #333; border-radius: 5px; transition: 0.4s; }

    .mobile-menu {
        display: none; flex-direction: column;
        background: white; text-align: center;
        position: absolute; top: 60px; left: 0; width: 100%;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .mobile-menu a {
        padding: 15px 0; border-bottom: 1px solid #eee;
        color: #333; text-decoration: none; font-weight: 500;
    }
    .mobile-menu a:hover { color: var(--accent); }

    /* Hero */
    .hero {
        background: linear-gradient(135deg, var(--accent), #c5a24a);
        color: white; padding: 160px 20px 120px;
        border-radius: 12px; text-align: center;
        transition: transform 0.6s ease, box-shadow 0.6s ease;
        margin-top: 80px; overflow: hidden;
    }
    .hero h1 { font-size: 2.2rem; margin-bottom: 15px; }
    .hero p { font-size: 1.1rem; }
    .hero:hover { transform: scale(1.02); box-shadow: 0 20px 40px rgba(0,0,0,0.2); }

    /* Sections */
    .section {
        padding: 70px 20px;
        text-align: center;
        max-width: 1200px;
        margin: auto;
    }
    .section h2 { font-size: 1.8rem; color: #222; margin-bottom: 25px; }

    /* Grid cards */
    .grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 30px;
        margin-top: 40px;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        text-align: center;
        transition: transform 0.6s ease, box-shadow 0.6s ease;
        overflow: hidden;
    }
    .card:hover { transform: translateY(-8px) scale(1.03); box-shadow: 0 10px 25px rgba(0,0,0,0.15); }
    .card img {
        width: 100%; height: auto;
        border-radius: 12px;
        transition: transform 0.6s ease;
    }
    .card img:hover { transform: scale(1.08); }

    /* Parallax */
    .parallax {
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
        height: 320px;
        border-radius: 12px;
        margin: 80px 0;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 40px;
        font-size: 0.9em;
        color: #666;
        background: #fff;
        border-top: 1px solid #eee;
        margin-top: 50px;
    }

    /* Mobile */
    @media (max-width: 768px) {
        .nav-links { display: none; }
        .hamburger { display: flex; }
        .hero h1 { font-size: 1.6rem; }
        .section h2 { font-size: 1.5rem; }
    }

    /* small layout polish to avoid iframe scrollbar cut-off */
    main { padding-bottom: 60px; }
  </style>
</head>
<body>
  <div class="navbar" id="navbar">
    <h1>🛋️ Sagar Sofa's</h1>
    <div class="nav-links" id="navLinks">
      <a href="#home">Home</a>
      <a href="#collections">Collections</a>
      <a href="#about">About</a>
      <a href="#contact">Contact</a>
    </div>
    <div class="hamburger" id="hamburger" aria-label="Toggle menu">
      <div></div><div></div><div></div>
    </div>
  </div>

  <div class="mobile-menu" id="mobileMenu" aria-hidden="true">
    <a href="#home">Home</a>
    <a href="#collections">Collections</a>
    <a href="#about">About</a>
    <a href="#contact">Contact</a>
  </div>

  <main>
    <!-- HERO -->
    <section id="home" class="hero" data-aos="fade-zoom-in">
      <h1>Elegant Furniture for Modern Living</h1>
      <p>Crafted with passion, designed for comfort.</p>
    </section>

    <!-- COLLECTIONS -->
    <section id="collections" class="section">
      <h2 data-aos="fade-up">🌟 Featured Collections</h2>
      <div class="grid">
        <div class="card" data-aos="fade-right">
          <img loading="lazy" src="https://images.unsplash.com/photo-1616627986744-8ad597d07c96?w=1200&auto=format&fit=crop&q=80" alt="Minimalist Sofa"/>
          <h3>Minimalist Comfort</h3>
          <p>Soft, stylish, and sustainable.</p>
        </div>
        <div class="card" data-aos="zoom-in-up">
          <img loading="lazy" src="https://images.unsplash.com/photo-1598300056226-0f8c9e99d8cc?w=1200&auto=format&fit=crop&q=80" alt="Modern Chair"/>
          <h3>Scandinavian Charm</h3>
          <p>Designed for relaxation and elegance.</p>
        </div>
        <div class="card" data-aos="fade-left">
          <img loading="lazy" src="https://images.unsplash.com/photo-1598300007898-0f8c9e44d8cc?w=1200&auto=format&fit=crop&q=80" alt="Wood Table"/>
          <h3>Natural Finish</h3>
          <p>Premium quality handcrafted wood.</p>
        </div>
      </div>
    </section>

    <!-- ABOUT -->
    <section id="about" class="section" data-aos="fade-up">
      <h2>About Us</h2>
      <p>At <b>Sagar Sofa's</b>, we blend craftsmanship with modern design to create timeless pieces that make your home elegant, comfortable, and sustainable.</p>
    </section>

    <!-- PARALLAX -->
    <div class="parallax" style="background-image:url('https://images.unsplash.com/photo-1615874959474-d609969a20ed?w=1600&auto=format&fit=crop&q=80');" data-aos="zoom-in"></div>

    <!-- CONTACT -->
    <section id="contact" class="section" data-aos="fade-up">
      <h2>Contact Us</h2>
      <p>📧 sb76@gmail.com<br>📞 +91 9885916770</p>
    </section>

    <!-- FOOTER -->
    <div class="footer">© 2025 | Sagar Sofa's — Crafted with ❤️</div>
  </main>

  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <script>
    // DOM ready
    document.addEventListener('DOMContentLoaded', function() {
      // Initialize AOS
      if (window.AOS) {
        AOS.init({
          duration: 1200,
          easing: 'ease-in-out',
          once: true,
          mirror: false
        });
      }

      // Mobile menu toggle
      const hamburger = document.getElementById('hamburger');
      const mobileMenu = document.getElementById('mobileMenu');

      function toggleMenu() {
        const isShown = mobileMenu.style.display === 'flex';
        mobileMenu.style.display = isShown ? 'none' : 'flex';
        mobileMenu.setAttribute('aria-hidden', String(isShown));
      }

      hamburger.addEventListener('click', toggleMenu);

      // Close mobile menu when a link is clicked
      mobileMenu.querySelectorAll('a').forEach(a => {
        a.addEventListener('click', () => {
          mobileMenu.style.display = 'none';
        });
      });

      // Navbar shadow on scroll
      window.addEventListener('scroll', function() {
        const navbar = document.getElementById('navbar');
        if (window.scrollY > 50) navbar.classList.add('scrolled');
        else navbar.classList.remove('scrolled');
      });

      // Improve in-iframe anchor scrolling: offset to account for fixed navbar
      function offsetAnchor() {
        if(location.hash.length > 0) {
          window.scrollTo(window.scrollX, window.scrollY - 70);
        }
      }
      window.addEventListener("hashchange", offsetAnchor);
      window.setTimeout(offsetAnchor, 1);
    });
  </script>
</body>
</html>
"""

# Render as a single component. Adjust height to fit content; tweak as needed.
html(full_page, height=1400, scrolling=True)
