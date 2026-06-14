import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="MallQ",
    page_icon="🛍️",
    layout="wide"
)

# -------------------------
# SESSION STATE
# -------------------------

if "page" not in st.session_state:
    st.session_state.page = "login"

if "otp_sent" not in st.session_state:
    st.session_state.otp_sent = False

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

if "cart" not in st.session_state:
    st.session_state.cart = []

if "points" not in st.session_state:
    st.session_state.points = 1200

# -------------------------
# CSS
# -------------------------

st.markdown("""
<style>

.stApp{
    background:#f6f7fb;
}

/* HERO */

.hero{
    background:linear-gradient(90deg,#ff8c00,#ffb347);
    padding:30px;
    border-radius:20px;
    margin-bottom:20px;
}

.hero h1{
    color:white;
    font-size:45px;
}

.hero p{
    color:white;
    font-size:18px;
}

/* CARDS */

.mall-card{
    background:white;
    padding:20px;
    border-radius:20px;
    text-align:center;
    border:2px solid #eee;
    margin-bottom:15px;
}

.product-card{
    background:white;
    padding:20px;
    border-radius:20px;
    margin-bottom:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.08);
}

/* BUTTON */

.stButton button{
    background:#ff8c00 !important;
    color:white !important;
    border:none !important;
    border-radius:10px !important;
}

/* TEXT */

h1,h2,h3,h4,p,label{
    color:#222 !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# LOGIN PAGE
# -------------------------

if st.session_state.page == "login":

    st.markdown("""
    <div class='hero'>
    <h1>🛍️ Welcome To MallQ</h1>
    <p>Quick Shopping • Smart Queries • Quality Recommendations</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 📱 Sign In")

    phone = st.text_input(
        "Phone Number"
    )

    st.info(
        "Demo OTP = 1234"
    )

    if st.button("Send OTP"):
        st.session_state.otp_sent = True

    if st.session_state.otp_sent:

        otp = st.text_input(
            "Enter OTP"
        )

        if st.button("Verify OTP"):

            if otp == "1234":

                st.session_state.page = "profile"
                st.rerun()

            else:

                st.error(
                    "Incorrect OTP"
                )

# -------------------------
# PROFILE PAGE
# -------------------------

elif st.session_state.page == "profile":

    st.markdown("""
    <div class='hero'>
    <h1>👤 Complete Your Profile</h1>
    <p>Let's personalize your MallQ experience</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 👤 Full Name")
    name = st.text_input(
        "",
        key="name"
    )

    st.markdown("### 📧 Email Address")
    email = st.text_input(
        "",
        key="email"
    )

    st.markdown("### 🎂 Age Group")

    age = st.radio(
        "",
        [
            "18-24",
            "25-34",
            "35-44",
            "45+"
        ],
        horizontal=True
    )

    st.markdown("### 🛍 Shopping Interests")

    col1,col2,col3 = st.columns(3)

    with col1:
        fashion = st.checkbox("👗 Fashion")
        footwear = st.checkbox("👟 Footwear")

    with col2:
        electronics = st.checkbox("📱 Electronics")
        beauty = st.checkbox("💄 Beauty")

    with col3:
        luxury = st.checkbox("💎 Luxury")
        sports = st.checkbox("⚽ Sports")

    if st.button("🚀 Enter MallQ"):

        st.session_state.user_name = name

        st.session_state.page = "home"

        st.rerun()

# -------------------------
# PRODUCT DATA
# -------------------------

products = pd.DataFrame([

    {
        "Product":"Nike Air Max",
        "Store":"Nike",
        "Mall":"Inorbit Mall",
        "Locality":"Hitech City",
        "Price":7999,
        "Offer":"10% OFF"
    },

    {
        "Product":"Adidas Ultraboost",
        "Store":"Adidas",
        "Mall":"Inorbit Mall",
        "Locality":"Hitech City",
        "Price":9999,
        "Offer":"15% OFF"
    },

    {
        "Product":"iPhone 16",
        "Store":"Croma",
        "Mall":"Inorbit Mall",
        "Locality":"Hitech City",
        "Price":79999,
        "Offer":"Free AirPods"
    },

    {
        "Product":"Zara Jacket",
        "Store":"Zara",
        "Mall":"Nexus Hyderabad Mall",
        "Locality":"Kukatpally",
        "Price":4999,
        "Offer":"Buy 2 Get 1"
    },

    {
        "Product":"H&M Dress",
        "Store":"H&M",
        "Mall":"Sarath City Capital Mall",
        "Locality":"Kondapur",
        "Price":2999,
        "Offer":"20% OFF"
    },

    {
        "Product":"Sephora Kit",
        "Store":"Sephora",
        "Mall":"Nexus Hyderabad Mall",
        "Locality":"Kukatpally",
        "Price":3499,
        "Offer":"Free Gift"
    }

])

# -------------------------
# MALL DATA
# -------------------------

malls = {

    "Inorbit Mall":[
        "Nike",
        "Adidas",
        "Skechers",
        "Lifestyle",
        "Shoppers Stop",
        "Croma"
    ],

    "Sarath City Capital Mall":[
        "H&M",
        "Max",
        "Pantaloons",
        "Reliance Trends",
        "Lifestyle",
        "Decathlon"
    ],

    "Nexus Hyderabad Mall":[
        "Zara",
        "Sephora",
        "Aldo",
        "Steve Madden",
        "H&M",
        "Lifestyle"
    ],

    "GVK One Mall":[
        "Marks & Spencer",
        "Tommy Hilfiger",
        "Charles & Keith",
        "Benetton",
        "Shoppers Stop"
    ]

}

# -------------------------
# HOME PAGE
# -------------------------

if st.session_state.page == "home":

    user_name = st.session_state.get(
        "user_name",
        "Shopper"
    )

    st.markdown(f"""
    <div class='hero'>
        <h1>Welcome, {user_name} 👋</h1>
        <p>Discover products across Hyderabad malls instantly.</p>
    </div>
    """,
    unsafe_allow_html=True)

    st.markdown("## 🏬 Choose Your Mall")

    col1,col2,col3,col4 = st.columns(4)

    selected_mall = None

    with col1:
        if st.button("🏬 Inorbit Mall"):
            st.session_state.mall = "Inorbit Mall"

    with col2:
        if st.button("🏬 Sarath City"):
            st.session_state.mall = "Sarath City Capital Mall"

    with col3:
        if st.button("🏬 Nexus Mall"):
            st.session_state.mall = "Nexus Hyderabad Mall"

    with col4:
        if st.button("🏬 GVK One"):
            st.session_state.mall = "GVK One Mall"

    if "mall" not in st.session_state:
        st.session_state.mall = "Inorbit Mall"

    st.success(
        f"Selected Mall: {st.session_state.mall}"
    )

    st.write("")

    st.markdown("## 📍 Choose Locality")

    loc1,loc2,loc3,loc4 = st.columns(4)

    with loc1:
        if st.button("📍 Hitech City"):
            st.session_state.locality = "Hitech City"

    with loc2:
        if st.button("📍 Madhapur"):
            st.session_state.locality = "Madhapur"

    with loc3:
        if st.button("📍 Kondapur"):
            st.session_state.locality = "Kondapur"

    with loc4:
        if st.button("📍 Kukatpally"):
            st.session_state.locality = "Kukatpally"

    if "locality" not in st.session_state:
        st.session_state.locality = "Hitech City"

    st.info(
        f"Current Locality: {st.session_state.locality}"
    )

    st.write("")

    # -------------------------
    # QUICK STATS
    # -------------------------

    stat1,stat2,stat3 = st.columns(3)

    with stat1:
        st.metric(
            "🛍 Products",
            "15,000+"
        )

    with stat2:
        st.metric(
            "🏬 Stores",
            "500+"
        )

    with stat3:
        st.metric(
            "🎁 Deals Today",
            "250+"
        )

    st.write("")

    # -------------------------
    # TABS
    # -------------------------

    home_tab, search_tab, locator_tab, outfit_tab, wishlist_tab, cart_tab, rewards_tab, ai_tab = st.tabs([
        "🏠 Home",
        "🔍 Search",
        "📍 Locator",
        "🧥 Outfit Matcher",
        "❤️ Wishlist",
        "🛒 Cart",
        "🏆 Rewards",
        "🤖 Ask MallQ"
    ])

    # -------------------------
    # HOME TAB
    # -------------------------

    with home_tab:

        st.markdown("## 🔥 Trending Products")

        for _, row in products.iterrows():

            st.markdown(f"""
            <div class='product-card'>
                <h3>{row['Product']}</h3>
                <p><b>🏬 Store:</b> {row['Store']}</p>
                <p><b>📍 Mall:</b> {row['Mall']}</p>
                <p><b>📌 Locality:</b> {row['Locality']}</p>
                <p><b>💰 Price:</b> ₹{row['Price']}</p>
                <p><b>🎁 Offer:</b> {row['Offer']}</p>
            </div>
            """,
            unsafe_allow_html=True)

            c1,c2 = st.columns(2)

            with c1:
                if st.button(
                    f"❤️ Wishlist {row['Product']}",
                    key=f"wish_{row['Product']}"
                ):
                    if row["Product"] not in st.session_state.wishlist:
                        st.session_state.wishlist.append(
                            row["Product"]
                        )

            with c2:
                if st.button(
                    f"🛒 Add To Cart {row['Product']}",
                    key=f"cart_{row['Product']}"
                ):
                    st.session_state.cart.append(
                        row["Product"]
                    )

                    st.success(
                        "Added to cart!"
                    )

    # -------------------------
    # SEARCH TAB
    # -------------------------

    with search_tab:

        st.markdown("## 🔍 Search Products")

        search_query = st.text_input(
            "Search for a product"
        )

        if search_query:

            results = products[
                products["Product"].str.contains(
                    search_query,
                    case=False
                )
            ]

            if len(results) > 0:

                for _, row in results.iterrows():

                    st.markdown(f"""
                    <div class='product-card'>
                        <h3>{row['Product']}</h3>
                        <p>🏪 {row['Store']}</p>
                        <p>🏬 {row['Mall']}</p>
                        <p>📍 {row['Locality']}</p>
                        <p>💰 ₹{row['Price']}</p>
                        <p>🎁 {row['Offer']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True)

            else:

                st.warning(
                    "No products found."
                )

    # -------------------------
    # STORE LOCATOR
    # -------------------------

    with locator_tab:

        st.markdown("## 📍 Store Locator")

        st.markdown(f"""
        <div class='card'>
            <h3>🏬 {st.session_state.mall}</h3>
            <p>Stores Available:</p>
        </div>
        """,
        unsafe_allow_html=True)

        selected_stores = malls[
            st.session_state.mall
        ]

        for store in selected_stores:

            st.markdown(f"""
            <div class='product-card'>
                <h3>🏪 {store}</h3>
                <p>
                Available at
                {st.session_state.mall}
                </p>
            </div>
            """,
            unsafe_allow_html=True)

    # -------------------------
    # OUTFIT MATCHER
    # -------------------------

    with outfit_tab:

        st.markdown(
            "## 🧥 MallQ Outfit Matcher"
        )

        st.write(
            "Choose what you already own."
        )

        outfit_mode = st.radio(
            "",
            [
                "👕 I Have A Top",
                "👖 I Have Pants"
            ],
            horizontal=True
        )

        # ---------------------
        # TOP -> PANTS
        # ---------------------

        if outfit_mode == "👕 I Have A Top":

            top = st.radio(
                "Choose Your Top",
                [
                    "White Shirt",
                    "Black T-Shirt",
                    "Blue Denim Shirt",
                    "Pink Top",
                    "Green Kurti"
                ]
            )

            recommendations = {

                "White Shirt":
                "Black Trousers, Beige Chinos, Blue Jeans",

                "Black T-Shirt":
                "Grey Jeans, Cargo Pants",

                "Blue Denim Shirt":
                "White Pants, Khaki Chinos",

                "Pink Top":
                "White Jeans, Black Trousers",

                "Green Kurti":
                "White Palazzo, Leggings"
            }

            st.success(
                recommendations[top]
            )

        # ---------------------
        # PANTS -> TOP
        # ---------------------

        else:

            pant = st.radio(
                "Choose Your Pants",
                [
                    "Blue Jeans",
                    "Black Trousers",
                    "Cargo Pants",
                    "Beige Chinos"
                ]
            )

            recommendations = {

                "Blue Jeans":
                "White Shirt, Black Tee",

                "Black Trousers":
                "White Shirt, Grey Polo",

                "Cargo Pants":
                "Oversized Tee, Hoodie",

                "Beige Chinos":
                "Blue Shirt, White Polo"
            }

            st.success(
                recommendations[pant]
            )

        st.write("")

        st.markdown(
            "### 🎯 Occasion Styling"
        )

        occasion = st.radio(
            "",
            [
                "🎓 College",
                "💼 Office",
                "❤️ Date",
                "🎉 Party",
                "💍 Wedding"
            ]
        )

        tips = {

            "🎓 College":
            "Oversized Tee + Jeans + Sneakers",

            "💼 Office":
            "Formal Shirt + Trousers",

            "❤️ Date":
            "White Shirt + Beige Chinos",

            "🎉 Party":
            "Black Shirt + Slim Fit Trousers",

            "💍 Wedding":
            "Kurta + Loafers"
        }

        st.info(
            tips[occasion]
        )

    # -------------------------
    # WISHLIST TAB
    # -------------------------

    with wishlist_tab:

        st.markdown("## ❤️ My Wishlist")

        if len(st.session_state.wishlist) == 0:

            st.info(
                "No products in wishlist yet."
            )

        else:

            for item in st.session_state.wishlist:

                st.markdown(f"""
                <div class='product-card'>
                    ❤️ {item}
                </div>
                """,
                unsafe_allow_html=True)

    # -------------------------
    # CART TAB
    # -------------------------

    with cart_tab:

        st.markdown("## 🛒 My Cart")

        if len(st.session_state.cart) == 0:

            st.info(
                "Your cart is empty."
            )

        else:

            total = 0

            for item in st.session_state.cart:

                product_row = products[
                    products["Product"] == item
                ]

                if len(product_row) > 0:

                    price = int(
                        product_row.iloc[0]["Price"]
                    )

                    total += price

                    st.markdown(f"""
                    <div class='product-card'>
                        <h3>{item}</h3>
                        <p>💰 ₹{price}</p>
                    </div>
                    """,
                    unsafe_allow_html=True)

            st.success(
                f"🧾 Total Amount: ₹{total}"
            )

            if st.button(
                "💳 Checkout"
            ):

                st.balloons()

                st.success(
                    "Order placed successfully!"
                )

                st.session_state.points += 100

    # -------------------------
    # REWARDS TAB
    # -------------------------

    with rewards_tab:

        st.markdown(
            "## 🏆 MallQ Rewards"
        )

        st.metric(
            "Reward Points",
            st.session_state.points
        )

        progress = min(
            st.session_state.points / 5000,
            1.0
        )

        st.progress(progress)

        if st.session_state.points < 5000:

            st.info(
                f"{5000 - st.session_state.points} points away from Gold Membership."
            )

        else:

            st.success(
                "🎉 Gold Membership Unlocked!"
            )

        st.write("")

        st.markdown(
            "### 🎡 Spin & Win"
        )

        if st.button(
            "SPIN NOW"
        ):

            rewards = [

                "10% OFF Coupon",
                "20% OFF Coupon",
                "Free Coffee",
                "100 Reward Points",
                "Buy 1 Get 1",
                "Free Parking Pass"

            ]

            reward = random.choice(
                rewards
            )

            if reward == "100 Reward Points":

                st.session_state.points += 100

            st.balloons()

            st.success(
                f"You Won: {reward}"
            )

    # -------------------------
    # ASK MALLQ AI
    # -------------------------

    with ai_tab:

        st.markdown(
            "## 🤖 Ask MallQ"
        )

        question = st.text_input(
            "Ask MallQ anything..."
        )

        if question:

            q = question.lower()

            if "zara" in q:

                st.success(
                    "👗 Zara is available at Nexus Hyderabad Mall."
                )

            elif "nike" in q:

                st.success(
                    "👟 Nike is available at Inorbit Mall."
                )

            elif "iphone" in q:

                st.success(
                    "📱 iPhone 16 is available at Croma, Inorbit Mall."
                )

            elif "mall" in q:

                st.success(
                    "🏬 Popular malls: Inorbit, Sarath City Capital, Nexus Hyderabad and GVK One."
                )

            elif "outfit" in q:

                st.success(
                    "👕 Visit Outfit Matcher for styling suggestions."
                )

            elif "offer" in q:

                st.success(
                    "🎁 Current best offer: Zara Jacket - Buy 2 Get 1."
                )

            else:

                st.info(
                    "Try asking about stores, malls, products, offers or outfits."
                )

        st.write("")

        st.markdown(
            "### Suggested Questions"
        )

        st.write("• Where can I buy Zara?")
        st.write("• Which mall has Nike?")
        st.write("• Suggest an outfit for college")
        st.write("• What is the best offer today?")
        st.write("• Where can I buy an iPhone?")

    # -------------------------
    # FOOTER
    # -------------------------

    st.write("")
    st.write("---")

    col1, col2 = st.columns(2)

    with col1:

        st.caption(
            "🛍️ MallQ — Quick Shopping • Smart Queries • Quality Recommendations"
        )

    with col2:

        if st.button(
            "🚪 Logout"
        ):

            st.session_state.page = "login"
            st.rerun()