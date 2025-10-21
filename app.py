
import streamlit as st
from streamlit.components.v1 import html

# --- Page Config ---
st.set_page_config(page_title="Sagar Sofa's", page_icon="🛋️", layout="wide")

# --- Include External CSS/JS ---
st.markdown("""
<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

body {
    font-family: 'Poppins', sans-serif;
    color: #333;
    background: #f6f7f9;
    margin: 0;
    padding: 0;
    scroll-behavior: smooth;
}

.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: white;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 14px 40px;
    transition: all 0.4s ease;
}

.navbar.scrolled {
    background: #fefefe;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.navbar h1 {
    font-size: 1.3rem;
    color: #D4AF37;
    font-weight: 600;
    margin: 0;
}

.nav-links {
    display: flex;
    gap: 25px;
}

.nav-links a {
    text-decoration: none;
    color: #333;
    font-weight: 500;
    transition: color 0.3s ease;
}
.nav-links a:hover {
    color: #D4AF37;
}

.hamburger {
    display: none;
    flex-direction: column;
    cursor: pointer;
    width: 25px;
    height: 20px;
    justify-content: space-between;
}
.hamburger div {
    height: 3px;
    background: #333;
    border-radius: 5px;
    transition: 0.4s;
}

.mobile-menu {
    display: none;
    flex-direction: column;
    background: white;
    text-align: center;
    position: absolute;
    top: 60px;
    left: 0;
    width: 100%;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.mobile-menu a {
    padding: 15px 0;
    border-bottom: 1px solid #eee;
    color: #333;
    text-decoration: none;
    font-weight: 500;
}
.mobile-menu a:hover {
    color: #D4AF37;
}

.hero {
    background: linear-gradient(135deg, #D4AF37, #c5a24a);
    color: white;
    padding: 140px 20px 100px;
    border-radius: 12px;
    text-align: center;
    transition: transform 0.6s ease, box-shadow 0.6s ease;
    margin-top: 80px;
}
.hero:hover {
    transform: scale(1.02);
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
}

.section {
    padding: 60px 20px;
    text-align: center;
    max-width: 1200px;
    margin: auto;
}

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
    transition: transform 0.5s ease, box-shadow 0.5s ease;
    perspective: 1000px;
}
.card:hover {
    transform: translateY(-5px) rotateX(3deg) rotateY(-3deg);
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}
.card img {
    width: 100%;
    height: auto;
    border-radius: 12px;
    transition: transform 0.5s ease;
}
.card img:hover {
    transform: scale(1.08);
}

.parallax {
    background-attachment: fixed;
    background-size: cover;
    background-position: center;
    height: 300px;
    border-radius: 12px;
    margin: 60px 0;
}

.footer {
    text-align: center;
    padding: 40px;
    font-size: 0.9em;
    color: #666;
    background: #fff;
    border-top: 1px solid #eee;
}

@media (max-width: 768px) {
    .nav-links { display: none; }
    .hamburger { display: flex; }
    .footer { font-size: 0.8em; padding: 30px; }
}
</style>
""", unsafe_allow_html=True)

# --- Navbar + Mobile Menu ---
html("""
<div class="navbar">
  <h1>🛋️ Sagar Sofa's</h1>
  <div class="nav-links">
    <a href="#home">Home</a>
    <a href="#collections">Collections</a>
    <a href="#about">About</a>
    <a href="#contact">Contact</a>
  </div>
  <div class="hamburger" onclick="toggleMenu()">
    <div></div><div></div><div></div>
  </div>
</div>

<div class="mobile-menu">
  <a href="#home" onclick="toggleMenu()">Home</a>
  <a href="#collections" onclick="toggleMenu()">Collections</a>
  <a href="#about" onclick="toggleMenu()">About</a>
  <a href="#contact" onclick="toggleMenu()">Contact</a>
</div>

<script>
AOS.init({ duration: 1000, once: true });

window.addEventListener('scroll', function() {
  const navbar = document.querySelector('.navbar');
  if(window.scrollY > 50) { navbar.classList.add('scrolled'); }
  else { navbar.classList.remove('scrolled'); }
});

function toggleMenu() {
  const menu = document.querySelector('.mobile-menu');
  menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';
}
</script>
""")

# --- Hero Section ---
st.markdown("""
<div id="home" class='hero' data-aos="zoom-in">
  <h1>Elegant Furniture for Modern Living</h1>
  <p>Crafted with passion, designed for comfort.</p>
</div>
""", unsafe_allow_html=True)

# --- Collections Section ---
st.markdown("""
<div id='collections' class='section'>
  <h2 data-aos='fade-up'>🌟 Featured Collections</h2>
  <div class="grid">
    <div class="card" data-aos="fade-right">
      <img src="https://images.unsplash.com/photo-1616627986744-8ad597d07c96" alt="Minimalist Sofa"/>
      <h3>Minimalist Comfort</h3>
      <p>Soft, stylish, and sustainable.</p>
    </div>
    <div class="card" data-aos="fade-up">
      <img src="https://images.unsplash.com/photo-1598300056226-0f8c9e99d8cc" alt="Modern Chair"/>
      <h3>Scandinavian Charm</h3>
      <p>Designed for relaxation and elegance.</p>
    </div>
    <div class="card" data-aos="fade-left">
      <img src="https://images.unsplash.com/photo-1598300007898-0f8c9e44d8cc" alt="Wood Table"/>
      <h3>Natural Finish</h3>
      <p>Premium quality handcrafted wood.</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# --- About Section ---
st.markdown("""
<div id='about' class='section' data-aos="fade-up">
  <h2>About Us</h2>
  <p>At <b>Sagar Sofa's</b>, we blend craftsmanship with modern design to create timeless pieces that make your home elegant, comfortable, and sustainable.</p>
</div>
""", unsafe_allow_html=True)

# --- Parallax Section ---
html("""
<div class="parallax" 
     style="background-image:url('https://images.unsplash.com/photo-1615874959474-d609969a20ed');">
</div>
""")

# --- Contact Section ---
st.markdown("""
<div id='contact' class='section' data-aos="zoom-in-up">
  <h2>Contact Us</h2>
  <p>📧 sb76@gmail.com<br>📞 +91 9885916770</p>
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<div class='footer'>© 2025 | Sagar Sofa's — Crafted with ❤️</div>", unsafe_allow_html=True)
