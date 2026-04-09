import streamlit as st

st.set_page_config(
    page_title="TechZone Laptops",
    page_icon="💻",
    layout="wide"
)

# ── CSS ─────────────────────────────────────────────
st.markdown("""
<style>
body {
    background-color: #f4f6f8;
}

.hero {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    padding: 60px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}
.hero h1 {
    font-size: 3rem;
    margin-bottom: 10px;
}
.section-title {
    font-size: 1.8rem;
    font-weight: bold;
    margin-bottom: 20px;
    color: #1f2a44;
}

.card {
    background: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
    text-align: center;
}
.card:hover {
    transform: translateY(-5px);
    transition: 0.2s;
}
.price {
    color: #e63946;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ── Hero ─────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>💻 TechZone Laptops</h1>
    <p>Power · Performance · Portability</p>
</div>
""", unsafe_allow_html=True)

# ── Laptop Data (WITH IMAGES) ─────────────────────────
laptops = [
    {
        "name": "HP Pavilion",
        "price": "₹55,000",
        "desc": "i5 | 8GB RAM | 512GB SSD",
        "img": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed"
    },
    {
        "name": "Dell Inspiron",
        "price": "₹60,000",
        "desc": "i5 | 16GB RAM | 512GB SSD",
        "img": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8"
    },
    {
        "name": "Lenovo IdeaPad",
        "price": "₹50,000",
        "desc": "Ryzen 5 | 8GB RAM | 512GB SSD",
        "img": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853"
    },
    {
        "name": "MacBook Air",
        "price": "₹95,000",
        "desc": "M1 Chip | 8GB RAM | 256GB SSD",
        "img": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4"
    },
]

# ── Display Cards ────────────────────────────────────
st.markdown('<div class="section-title">Available Laptops</div>', unsafe_allow_html=True)

cols = st.columns(4)

for col, l in zip(cols, laptops):
    with col:
        st.image(l["img"], use_container_width=True)
        st.markdown(f"""
        <div class="card">
            <h3>{l['name']}</h3>
            <p class="price">{l['price']}</p>
            <p>{l['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

st.write("")

# ── Order Form ───────────────────────────────────────
st.markdown('<div class="section-title">Place Your Order</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    product = st.selectbox(
        "Select Laptop",
        ["Select", "HP Pavilion", "Dell Inspiron", "Lenovo IdeaPad", "MacBook Air"]
    )
    budget = st.slider("Budget (₹)", 30000, 150000, 60000)

with col2:
    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    address = st.text_area("Delivery Address")

st.write("")

# ── Button ───────────────────────────────────────────
if st.button("🛒 Buy Now"):
    if product == "Select":
        st.warning("Please select a laptop")
    elif not name or not phone or not address:
        st.warning("Please fill all required details")
    else:
        st.success("✅ Order placed successfully!")
        st.balloons()

        st.write("### 📦 Order Summary")
        st.write(f"**Product:** {product}")
        st.write(f"**Budget:** ₹{budget}")
        st.write(f"**Name:** {name}")
        st.write(f"**Phone:** {phone}")
        st.write(f"**Address:** {address}")

# ── Footer ───────────────────────────────────────────
st.markdown("""
<hr>
<center>© 2026 TechZone Laptops | All Rights Reserved</center>
""", unsafe_allow_html=True)
