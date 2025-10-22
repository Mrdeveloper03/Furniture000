Awesome! Let’s make your showroom even more interactive with scroll-triggered card animations. When a card enters the viewport, it will gently pop up with a light reflection, making the user feel like the furniture is “appearing” in 3D.

Here’s the upgraded version:

import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Sagar Sofa's 3D Showroom", page_icon="🛋️", layout="wide")

# --- Static image URLs ---
sofa1_url = "https://raw.githubusercontent.com/username/repo/main/images/sofa1.jpg"
sofa2_url = "https://raw.githubusercontent.com/username/repo/main/images/sofa2.jpg"
table_url = "https://raw.githubusercontent.com/username/repo/main/images/table.jpg"
bg1_url = "https://raw.githubusercontent.com/username/repo/main/images/bg1.jpg"
bg2_url = "https://raw.githubusercontent.com/username/repo/main/images/bg2.jpg"

# --- Full HTML page ---
showroom_page = f'''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
<style>
:root {{
    --accent:#000;
    --bg-color:#fff;
    --text-color:#111;
    --card-shadow: rgba(0,0,0,0.25);
}}
body {{
    font-family:'Poppins',sans-serif;
    background: var(--bg-color);
    color: var(--text-color);
    margin:0; padding:0;
    scroll-behavior:smooth;
    perspective:1500px;
    overflow-x:hidden;
}}

/* Navbar */
.navbar {{
    position: fixed; top:0; left:0; width:100%;
    background: rgba(255,255,255,0.95);
    backdrop-filter: blur(10px);
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    z-index:1000; display:flex; align-items:center; justify-content:space-between;
    padding:14px 40px; transition: all 0.4s ease;
}}
.navbar.scrolled {{ background:white; box-shadow:0 4px 12px rgba(0,0,0,0.1); }}
.navbar h1 {{ font-size:1.3rem; color: var(--accent); font-weight:600; margin:0; }}
.nav-links {{ display:flex; gap:25px; }}
.nav-links a {{ text-decoration:none; color:var(--text-color); font-weight:500; transition: color 0.3s ease; }}
.nav-links a:hover {{ color:var(--accent); }}
.hamburger {{ display:none; flex-direction:column; cursor:pointer; width:25px; height:20px; justify-content:space-between; }}
.hamburger div {{ height:3px; background: var(--text-color); border-radius:5px; transition:0.4s; }}
.mobile-menu {{ display:none; flex-direction:column; background:white; text-align:center; position:absolute; top:60px; left:0; width:100%; box-shadow:0 4px 12px rgba(0,0,0,0.1); }}
.mobile-menu a {{ padding:15px 0; border-bottom:1px solid #eee; color:var(--text-color); text-decoration:none; font-weight:500; }}
.mobile-menu a:hover {{ color: var(--accent); }}

/* Hero */
.hero {{
    background: linear-gradient(135deg, #000, #333);
    color:white; padding:160px 20px 120px; border-radius:12px;
    text-align:center; margin-top:80px; transform-style: preserve-3d;
    transition: transform 0.5s ease, box-shadow 0.5s ease;
}}
.hero h1 {{ font-size:2.2rem; margin-bottom:15px; transform:translateZ(30px); }}
.hero p {{ font-size:1.1rem; transform:translateZ(20px); }}

/* Sections */
.section {{ padding:70px 20px; text-align:center; max-width:1200px; margin:auto; }}
.section h2 {{ font-size:1.8rem; color: var(--text-color); margin-bottom:25px; }}

/* Parallax */
.parallax {{ background-size: cover; background-position: center; height:400px; border-radius:12px; margin:80px 0; transform-style: preserve-3d; transition: transform 0.5s ease; }}

/* Grid Cards */
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:30px; margin-top:40px; perspective:1200px; }}
.card {{
    background:white; padding:20px; border-radius:16px; box-shadow:0 15px 25px var(--card-shadow);
    text-align:center; transition: transform 0.3s ease, box-shadow 0.3s ease, filter 0.3s ease; transform-style: preserve-3d;
    position:relative; overflow:hidden;
    opacity:0; transform: translateY(50px);
}}
.card.show {{
    opacity:1; transform: translateY(0); transition: all 0.7s ease-out;
}}
.card img {{ width:100%; height:auto; border-radius:12px; transition: transform 0.3s ease; transform-style: preserve-3d; }}
.card h3, .card p {{ transform:translateZ(20px); }}
.card button {{ margin-top:12px; padding:10px 18px; background: var(--accent); color:white; border:none; border-radius:6px; cursor:pointer; font-weight:500; transition: background 0.3s; }}
.card button:hover {{ background:#555; }}

/* Highlight effect */
.card::before {{
    content:'';
    position:absolute; top:0; left:0; width:100%; height:100%;
    pointer-events:none;
    background: radial-gradient(circle at var(--mouse-x,50%) var(--mouse-y,50%), rgba(255,255,255,0.15) 0%, transparent 80%);
    transition: background 0.2s ease;
    border-radius:16px;
}}

/* Footer */
.footer {{ text-align:center; padding:40px; font-size:0.9em; color:#666; background:#fff; border-top:1px solid #eee; margin-top:50px; }}

/* Mobile */
@media(max-width:768px) {{
    .nav-links{{display:none;}}
    .hamburger{{display:flex;}}
    .hero h1{{font-size:1.6rem;}}
    .section h2{{font-size:1.5rem;}}
    .grid {{ gap:20px; }}
}}
main{{padding-bottom:60px;}}
</style>
</head>
<body>
<div class="navbar" id="navbar">
<h1>🛋️ Sagar Sofa's 3D</h1>
<div class="nav-links">
  <a href="#home">Home</a>
  <a href="#collections">Collections</a>
  <a href="#reviews">Reviews</a>
  <a href="#contact">Contact</a>
</div>
<div class="hamburger"><div></div><div></div><div></div></div>
</div>

<div class="mobile-menu">
  <a href="#home">Home</a>
  <a href="#collections">Collections</a>
  <a href="#reviews">Reviews</a>
  <a href="#contact">Contact</a>
</div>

<main>
<section id="home" class="hero" data-aos="fade-zoom-in">
  <h1>Elegant Furniture for Modern Living</h1>
  <p>Crafted with passion, designed for comfort.</p>
</section>

<section id="collections" class="section">
<h2 data-aos="fade-up">🌟 Featured Collections</h2>
<div class="grid">
<div class="card" data-aos="fade-right">
  <img src="{sofa1_url}" alt="Minimalist Sofa"/>
  <h3>Minimalist Comfort</h3>
  <p>Soft, stylish, and sustainable.</p>
  <button onclick="window.open('https://wa.me/919494828592?text=Hi','_blank')">Get Quote</button>
</div>
<div class="card" data-aos="zoom-in-up">
  <img src="{sofa2_url}" alt="Modern Chair"/>
  <h3>Scandinavian Charm</h3>
  <p>Designed for relaxation and elegance.</p>
  <button onclick="window.open('https://wa.me/919494828592?text=Hi','_blank')">Get Quote</button>
</div>
<div class="card" data-aos="fade-left">
  <img src="{table_url}" alt="Wood Table"/>
  <h3>Natural Finish</h3>
  <p>Premium quality handcrafted wood.</p>
  <button onclick="window.open('https://wa.me/919494828592?text=Hi','_blank')">Get Quote</button>
</div>
</div>
</section>

<section class="parallax" style="background-image:url('{bg1_url}');"></section>

<section id="reviews" class="section" data-aos="fade-up">
<h2>What Our Customers Say</h2>
<p>“Amazing quality and elegant design. Completely satisfied!” — Ananya K.</p>
<p>“Comfortable sofas, worth every penny.” — Rajesh M.</p>
<p>“Sagar Sofa's transformed my living room.” — Priya S.</p>
</section>

<section class="parallax" style="background-image:url('{bg2_url}');"></section>

<section id="contact" class="section" data-aos="fade-up">
<h2>Contact Us</h2>
<p>📧 sb76@gmail.com<br>📞 +91 9885916770</p>
</section>

<div class="footer">© 2025 | Sagar Sofa's — Crafted with ❤️</div>
</main>

<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function(){{
  if(window.AOS) AOS.init({{duration:1200,easing:'ease-in-out',once:true,mirror:false}});

  // Hamburger toggle
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');
  hamburger.addEventListener('click', ()=> {{
    const isShown = mobileMenu.style.display==='flex';
    mobileMenu.style.display = isShown?'none':'flex';
  }});
  mobileMenu.querySelectorAll('a').forEach(a=>a.addEventListener('click', ()=> mobileMenu.style.display='none'));

  // Navbar scroll effect
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', ()=> {{
    if(window.scrollY>50) navbar.classList.add('scrolled');
    else navbar.classList.remove('scrolled');
  }});

  // 3D hover effect for hero
  const hero = document.querySelector('.hero');
  hero.addEventListener('mousemove', e=> {{
    const x = (window.innerWidth/2 - e.pageX)/25;
    const y = (window.innerHeight/2 - e.pageY)/25;
    hero.style.transform = `rotateY(${x}deg) rotateX(${y}deg) scale(1.03)`;
  }});
  hero.addEventListener('mouseleave', ()=> hero.style.transform='rotateY(0deg) rotateX(0deg) scale(1)');

  // 3D hover effect with light reflection for cards
  const cards = document.querySelectorAll('.card');
  cards.forEach(card => {{
    card.addEventListener('mousemove', e => {{
      const rect = card.getBoundingClientRect();
      const x = (e.clientX - rect.left - rect.width/2)/15;
      const y = (e.clientY - rect.top - rect.height/2)/15;
      card.style.transform = `rotateY(${x}deg) rotateX(${-y}deg) scale(1.05)`;
      card.style.setProperty('--mouse-x', ((e.clientX - rect.left)/rect.width*100)+'%');
      card.style.setProperty('--mouse-y', ((e.clientY - rect.top)/rect.height*100)+'%');
    }});
    card.addEventListener('mouseleave', () => {{
      card.style.transform = 'rotateY(0deg) rotateX(0deg) scale(1)';
      card.style.setProperty('--mouse-x','50%');
      card.style.setProperty('--mouse-y','50%');
    }});
  }});

  // Scroll-triggered card pop-up animation
  const observer = new IntersectionObserver(entries => {{
    entries.forEach(entry => {{
      if(entry.isIntersecting){{
        entry.target.classList.add('show');
      }}
    }});
  }},

