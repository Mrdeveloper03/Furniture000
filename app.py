import streamlit as st
from streamlit.components.v1 import html

# --- Page Config ---
st.set_page_config(page_title="Sagar Sofa's", page_icon="🛋️", layout="wide")

# --- CSS Styling ---
st.markdown("""
<style>
body {
    font-family: 'Poppins', sans-serif;
    color: #333;
    background: #f6f7f9;
}
h1, h2, h3 {
    font-weight: 600;
    color: #222;
}
.section {
    padding: 80px 0;
    text-align: center;
}
.hero {
    background: linear-gradient(to right, #D4AF37, #c5a24a);
    color: white;
    padding: 120px 20px;
    border-radius: 12px;
    transition: transform 0.6s ease, box-shadow 0.6s ease;
}
.hero:hover {
    transform: scale(1.02);
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
}
.card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}
img {
    border-radius: 12px;
    transition: transform 0.6s ease;
}
img:hover {
    transform: scale(1.05);
}
.footer {
    text-align: center;
    padding: 40px;
    font-size: 0.9em;
    color: #666;
}
</style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
<div class='hero'>
  <h1>🛋️ Modern Furniture Studio</h1>
  <p>Elevate your space with elegant, sustainable furniture designed for modern living.</p>
</div>
""", unsafe_allow_html=True)

# --- Featured Section ---
st.markdown("<div class='section'><h2>🌟 Featured Collections</h2></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://images.unsplash.com/photo-1616627986744-8ad597d07c96", caption="Minimalist Sofa")
    st.markdown("<div class='card'><h3>Minimalist Comfort</h3><p>Soft, stylish, and sustainable.</p></div>", unsafe_allow_html=True)
with col2:
    st.image("https://images.unsplash.com/photo-1598300056226-0f8c9e99d8cc", caption="Modern Chair")
    st.markdown("<div class='card'><h3>Scandinavian Charm</h3><p>Designed for relaxation and elegance.</p></div>", unsafe_allow_html=True)
with col3:
    st.image("https://images.unsplash.com/photo-1598300007898-0f8c9e44d8cc", caption="Wood Table")
    st.markdown("<div class='card'><h3>Natural Finish</h3><p>Premium quality handcrafted wood.</p></div>", unsafe_allow_html=True)

# --- About Section ---
st.markdown("""
<div class='section'>
  <h2>About Us</h2>
  <p>At <b>Sagar Sofa's</b>, we blend craftsmanship with modern design to create timeless pieces that transform your home into a sanctuary of style and comfort.</p>
</div>
""", unsafe_allow_html=True)

# --- Parallax Section (HTML component for smooth scroll) ---
html("""
<div style="background-image:url('https://images.unsplash.com/photo-1615874959474-d609969a20ed'); 
background-attachment: fixed; background-size: cover; background-position: center; 
height: 300px; border-radius: 12px; margin: 60px 0;">
</div>
""")

# --- Contact Section ---
st.markdown("""
<div class='section'>
  <h2>Contact Us</h2>
  <p>📧 sb76@gmaio.com<br>📞 +91 9885916770</p>
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<div class='footer'>© 2025 Sagar Sofa's | Designed with ❤️ using Streamlit</div>", unsafe_allow_html=True)
