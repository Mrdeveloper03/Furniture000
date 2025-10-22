import streamlit as st
import requests

st.set_page_config(page_title="Sagar Sofa's 3D Showroom", page_icon="🛋️", layout="wide")

# --- GitHub repo info ---
user = "username"  # replace with your GitHub username
repo = "repo"      # replace with your repo name
folder = "images"  # folder containing showroom images

# --- GitHub API: List files in /images ---
api_url = f"https://api.github.com/repos/{user}/{repo}/contents/{folder}"
resp = requests.get(api_url).json()

# --- Filter image URLs ---
image_urls = [file['download_url'] for file in resp if file['name'].lower().endswith(('.png','.jpg','.jpeg','.webp'))]

# --- Assign images automatically ---
sofa1_url = image_urls[0] if len(image_urls) > 0 else ""
sofa2_url = image_urls[1] if len(image_urls) > 1 else ""
table_url = image_urls[2] if len(image_urls) > 2 else ""
bg1_url = image_urls[3] if len(image_urls) > 3 else ""
bg2_url = image_urls[4] if len(image_urls) > 4 else ""

# --- Full HTML page ---
showroom_page = f'''
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
<style>
:root {{
  --accent:#000;
  --bg-color:#fff;
  --text-color:#111;
  --card-shadow: rgba(0,0,0,0.3);
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
.navbar {{
  position: fixed; top:0; left:0; width:100%; background: rgba(255,255,255,0.95);
  backdrop-filter: blur(10px); box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  z-index:1000; display:flex; align-items:center; justify-content:space-between; padding:14px 40px; transition: all 0.4s ease;
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

.hero {{ background: linear-gradient(135deg, #000, #333); color:white; padding:160px 20px 120px; border-radius:12px; text-align:center; margin-top:80px; transform-style: preserve-3d; transition: transform 0.5s ease, box-shadow 0.5s ease; }}
.hero h1 {{ font-size:2.2rem; margin-bottom:15px; transform:translateZ(30px); }}
.hero p {{ font-size:1.1rem; transform:translateZ(20px); }}

.section {{ padding:70px 20px; text-align:center; max-width:1200px; margin:auto; }}
.section h2 {{ font-size:1.8rem; color: var(--text-color); margin-bottom:25px; }}

.parallax {{ background-size: cover; background-position: center; height:400px; border-radius:12px; margin:80px 0; transform-style: preserve-3d; transition: transform 0.5s ease; }}

.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:30px; margin-top:40px; perspective:1200px; }}
.card {{ background:white; padding:20px; border-radius:16px; box-shadow:0 10px 20px var(--card-shadow); text-align:center; transition: transform 0.5s ease, box-shadow 0.5s ease; transform-style: preserve-3d; }}
.card img {{ width:100%; height:auto; border-radius:12px; transition: transform 0.5s ease; transform-style: preserve-3d; }}
.card h3, .card p {{ transform:translateZ(20px); }}
.card button {{ margin-top:12px; padding:10px 18px; background: var(--accent); color:white; border:none; border-radius:6px; cursor:pointer; font-weight:500; transition: background 0.3s; }}
.card button:hover {{ background:#555; }}

.footer {{ text-align:center; padding:40px; font-size:0.9em; color:#666; background:#fff; border-top:1px solid #eee; margin-top:50px; }}

@media(max-width:768px){{.nav-links{{display:none;}}.hamburger{{display:flex;}}.hero h1{{font-size:1.6rem;}}.section h2{{font-size:1.5rem;}}}}
main{{padding-bottom:60px;}}
</style>
</head>
<body>
<div class="navbar" id="navbar">
<h1>🛋️ Sagar Sofa's 3D</h1>
<div class="nav-links" id="navLinks">
  <a href="#home">Home</a>
  <a href="#collections">Collections</a>
  <a href="#reviews">Reviews</a>
  <a href="#contact">Contact</a>
</div>
<div class="hamburger" id="hamburger" aria-label="Toggle menu"><div></div><div></div><div></div></div>
</div>

<div class="mobile-menu" id="mobileMenu" aria-hidden="true">
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

  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  hamburger.addEventListener('click', ()=>{{
      const isShown = mobileMenu.style.display==='flex';
      mobileMenu.style.display = isShown?'none':'flex';
      mobileMenu.setAttribute('aria-hidden', String(isShown));
  }});
  mobileMenu.querySelectorAll('a').forEach(a=>{{a.addEventListener('click',()=>{{mobileMenu.style.display='none';}});}});

  window.addEventListener('scroll', ()=>{{
      const navbar=document.getElementById('navbar');
      if(window.scrollY>50) navbar.classList.add('scrolled');
      else navbar.classList.remove('scrolled');
  }});

  const hero = document.querySelector('.hero');
  hero.addEventListener('mousemove', e=>{{
      const x = (window.innerWidth/2 - e.pageX)/25;
      const y = (window.innerHeight/2 - e.pageY)/25;
      hero.style.transform = `rotateY(${x}deg) rotateX(${y}deg) scale(1.03)`;
  }});
  hero.addEventListener('mouseleave', ()=>{{ hero.style.transform='rotateY(0deg) rotateX(0deg) scale(1)'; }});

  const cards=document.querySelectorAll('.card');
  cards.forEach(card=>{{
      card.addEventListener('mousemove', e=>{{
          const rect=card.getBoundingClientRect();
          const x=(rect.width/2-(e.clientX-rect.left))/15;
          const y=(rect.height/2-(e.clientY-rect.top))/15;
          card.style.transform = `rotateY(${x}deg) rotateX(${y}deg) scale(1.05)`;
      }});
      card.addEventListener('mouseleave', ()=>{{ card.style.transform='rotateY(0deg) rotateX(0deg) scale(1)'; }});
  }});

  window.addEventListener('scroll', ()=>{{
      const scrollY = window.scrollY;
      hero.style.transform = `translateZ(${scrollY/15}px) rotateX(${scrollY/50}deg)`;
      cards.forEach((card,i)=>{{ card.style.transform = `translateZ(${scrollY/30 + i*2}px)`; }});
      document.querySelectorAll('.parallax').forEach((layer,i)=>{{ layer.style.transform = `translateY(${scrollY/10*(i+1)}px)`; }});
  }});
}});
</script>
</body>
</html>
'''

# --- Render HTML in Streamlit ---
st.components.v1.html(showroom_page, height=3000, scrolling=True)
