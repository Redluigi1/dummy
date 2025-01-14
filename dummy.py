import streamlit as st
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
mongoURI = 'mongodb+srv://actedcone:dualipa@atlascluster.t9cnxbb.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster'
client = MongoClient(mongoURI)
db = client.ENCODE

# Collections
products_collection = db.products
customers_collection = db.customers

# Streamlit App
st.title("Customer and Product Viewer")

# Sidebar navigation
option = st.sidebar.radio("Choose a view:", ("Customers", "Products"))

if option == "Products":
    st.header("Products")
    
    # Fetch and display products
    products = list(products_collection.find())
    if products:
        for product in products:
            st.subheader(product["name"])
            st.write(f"**ID:** {product['id']}")
            st.write(f"**Price:** ${product['price']}")
            st.write(f"**Type:** {product['type']}")
            st.write(f"**Offers:** {product['offers']}")
            st.write(f"**Warranty:** {product['warranty_details']}")
            st.write(f"**Description:** {product['description']}")
            st.markdown("---")
    else:
        st.warning("No products found.")

elif option == "Customers":
    st.header("Customers")
    
    # Fetch and display customers
    customers = list(customers_collection.find())
    if customers:
        for customer in customers:
            st.subheader(customer["name"])
            st.write(f"**Customer Number:** {customer['customer_number']}")
            st.write(f"**Customer ID:** {customer['customer_id']}")
            st.write("**Products Purchased:**")
            
            for product in customer["products"]:
                date_bought = product["date_bought"].strftime("%Y-%m-%d") if isinstance(product["date_bought"], datetime) else product["date_bought"]
                st.write(f"- Product ID: {product['product_id']}, Date Bought: {date_bought}")
            st.markdown("---")
    else:
        st.warning("No customers found.")
