import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data loading, replace with actual data loading
orders_payments_df = pd.read_csv('orders_payments.csv')
orders_with_customers_df = pd.read_csv('orders_with_customers.csv')
orders_df = pd.read_csv('orders.csv')

st.set_page_config(page_title="Dashboard Brazil E-Commerce")

st.header("Dashboard Brazil E-Commerce")

st.subheader("Question Goals")
st.markdown("""

- Viewing the percentage of payment types made by Users.
- Viewing the top 10 cities with the highest orders each year.
- Viewing the growth of orders each month throughout the year.

""")

tab1, tab2, tab3 = st.tabs(["Questions 1", "Questions 2", "Questions 3"])

with tab1:
    st.subheader("Viewing the percentage of payment types made by Users.")
    
    # Data value counts from payment_type
    total_counts = orders_payments_df["payment_type"].count()
    value_counts = orders_payments_df["payment_type"].value_counts()

    # Plot pie chart directly instead of using an image
    plt.figure(figsize=(8, 6))
    sns.set_style("whitegrid")
    plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Payment Type Distribution')
    plt.axis('equal')
    
    st.pyplot(plt)

with tab2:
    st.subheader("Viewing the top 10 cities with the highest orders each year.")
    
     # Replace this part with actual code to get top_10_city_order for each year 
     # This is just a placeholder for illustration purposes 
     top_10_city_order = orders_with_customers_df["customer_city"].value_counts().head(10)

     # Plot bar chart directly instead of using an image 
     plt.figure(figsize=(8, 6)) 
     sns.barplot(x=top_10_city_order.values, y=top_10_city_order.index) 
     
     st.pyplot(plt)

with tab3:
   st.subheader("Viewing the growth of orders each month throughout the year.")

   # Your existing code for preparing monthly_orders data remains here

   # Plot
   plt.figure(figsize=(10, 6))
   sns.set_style("whitegrid")
   sns.lineplot(data=monthly_orders, x='month', y='count', hue='year', marker='o')

   plt.title('Monthly Orders Growth by Year')
   plt.xlabel('Month')
   plt.ylabel('Number of Orders')
   plt.xticks(range(1, 13))
   plt.legend(title='Year')
   
   st.pyplot(plt)
