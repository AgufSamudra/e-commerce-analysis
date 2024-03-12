import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

orders_df = pd.read_csv("E-commerce-public-dataset/E-Commerce Public Dataset/orders_dataset.csv")
orders_payments_df = pd.read_csv("E-commerce-public-dataset/E-Commerce Public Dataset/order_payments_dataset.csv")
orders_customers_df = pd.read_csv("E-commerce-public-dataset/E-Commerce Public Dataset/customers_dataset.csv")
orders_items_df = pd.read_csv("E-commerce-public-dataset/E-Commerce Public Dataset/order_items_dataset.csv")

products_df = pd.read_csv("E-commerce-public-dataset/E-Commerce Public Dataset/products_dataset.csv")

geolocation_df = pd.read_csv("E-commerce-public-dataset/E-Commerce Public Dataset/geolocation_dataset.csv")

# merge orders_df with orders_customers_df
orders_with_customers_df = pd.merge(orders_df, orders_customers_df, on="customer_id")

# Convert order_purchase_timestamp to datetime
orders_df['order_purchase_timestamp'] = pd.to_datetime(orders_df['order_purchase_timestamp'])

# Extract year and month from order_purchase_timestamp
orders_df['year'] = orders_df['order_purchase_timestamp'].dt.year
orders_df['month'] = orders_df['order_purchase_timestamp'].dt.month

# Group by year and month, count the number of orders
monthly_orders = orders_df.groupby(['year', 'month']).size().reset_index(name='count')

st.set_page_config(page_title="Dashboard Brazil E-Commerce")

st.header("Dashboard Brazil E-Commerce")

st.subheader("Question Goals")
st.markdown("""

- What percentage of payment types are used by users?
- Top 10 Which cities have the highest level of orders each year?
- See how orders grow each quarter each year?

""")

# cleaning data
# merge orders_df with orders_customers_df
orders_with_cutomers_df = pd.merge(orders_df, orders_customers_df, on="customer_id")
orders_with_cutomers_df.head(2)

# change data type object to datetime pandas
change_to_datetime = ["order_purchase_timestamp", "order_approved_at", 
                      "order_delivered_carrier_date", "order_delivered_customer_date", 
                      "order_estimated_delivery_date"]

for column in change_to_datetime:
    orders_with_cutomers_df[column] = pd.to_datetime(orders_with_cutomers_df[column], format="%Y-%m-%d %H:%M:%S")
    orders_df[column] = pd.to_datetime(orders_df[column], format="%Y-%m-%d %H:%M:%S")

# drop missing value in orders_with_cutomers_df
orders_with_cutomers_df.dropna(axis=0, inplace=True)

# drop missing value in orders_df
orders_df.dropna(axis=0, inplace=True)


tab1, tab2, tab3 = st.tabs(["Questions 1", "Questions 2", "Questions 3"])

with tab1:
    st.subheader("What percentage of payment types are used by users?")
    
    # Data value counts dari payment_type
    total_counts = orders_payments_df["payment_type"].count()
    value_counts = orders_payments_df["payment_type"].value_counts()

    payment_type_percentages = (value_counts / total_counts) * 100
    print(payment_type_percentages.round(2))

    # Plot barchart
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    barplot = sns.barplot(x=payment_type_percentages.index, y=payment_type_percentages.values, color="skyblue")
    plt.title('Distribusi Tipe Pembayaran')
    plt.xlabel('Tipe Pembayaran')
    plt.ylabel('Presentase (%)')

    # Menambahkan persentase pada setiap bar
    for i, percentage in enumerate(payment_type_percentages):
        barplot.text(i, percentage, f"{percentage:.2f}%", ha='center', va='bottom')

    plt.tight_layout()
    
    st.pyplot(plt)
    
    with st.expander("Conlusion"):
        st.markdown("""
                    We can observe that the predominant payment method is credit card, followed by boleto. `Boleto` is a popular payment method in Brazil for online transactions. 
                    However, it's clear that credit card payments constitute a significant percentage, almost `74%`.
                    """)

with tab2:
    st.subheader("Top 10 Which cities have the highest level of orders each year?")
    orders_with_cutomers_df = pd.merge(orders_df, orders_customers_df, on="customer_id")
    
    top_10_city_order = orders_with_cutomers_df["customer_city"].value_counts().head(10)

    plt.figure(figsize=(8, 6))
    sns.set_style("whitegrid")
    sns.barplot(x=top_10_city_order.values, y=top_10_city_order.index, color="skyblue")

    plt.title('Top 10 Cities from All Data')
    plt.xlabel('Order Count')
    plt.ylabel('City')
    plt.tight_layout()
    plt.show()
    
    st.pyplot(plt)
    
    # looks from each years
    orders_with_cutomers = orders_with_cutomers_df.copy()
    orders_with_cutomers = orders_with_cutomers[["order_purchase_timestamp", "customer_city"]]

    orders_with_cutomers["month"] = orders_with_cutomers["order_purchase_timestamp"].dt.month
    orders_with_cutomers["years"] = orders_with_cutomers["order_purchase_timestamp"].dt.year

    # lets seperate with years
    # 2016
    orders_with_cutomers_2016 = orders_with_cutomers[orders_with_cutomers["years"] == 2016].sort_values(by="month")

    # 2017
    orders_with_cutomers_2017 = orders_with_cutomers[orders_with_cutomers["years"] == 2017].sort_values(by="month")

    # 2018
    orders_with_cutomers_2018 = orders_with_cutomers[orders_with_cutomers["years"] == 2018].sort_values(by="month")
    
    
    # splitting visualize
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Highest orders at 2016.")
        top_10_city_order_2016 = orders_with_cutomers_2016["customer_city"].value_counts().head(10)

        plt.figure(figsize=(8, 6))
        sns.set_style("whitegrid")
        sns.barplot(x=top_10_city_order_2016.values, y=top_10_city_order_2016.index, color="skyblue")

        plt.title('Top 10 Cities in 2016')
        plt.xlabel('Order Count')
        plt.ylabel('City')
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
    
    with col2:
        st.subheader("Highest orders at 2017.")
        top_10_city_order_2017 = orders_with_cutomers_2017["customer_city"].value_counts().head(10)

        plt.figure(figsize=(8, 6))
        sns.set_style("whitegrid")
        sns.barplot(x=top_10_city_order_2017.values, y=top_10_city_order_2017.index, color="skyblue")

        plt.title('Top 10 Cities in 2017')
        plt.xlabel('Order Count')
        plt.ylabel('City')
        plt.tight_layout()
        plt.show()
        st.pyplot(plt)
    
    st.subheader("Highest orders at 2018.")
    top_10_city_order_2018 = orders_with_cutomers_2018["customer_city"].value_counts().head(10)

    plt.figure(figsize=(8, 6))
    sns.set_style("whitegrid")
    sns.barplot(x=top_10_city_order_2018.values, y=top_10_city_order_2018.index, color="skyblue")

    plt.title('Top 10 Cities in 2018')
    plt.xlabel('Order Count')
    plt.ylabel('City')
    plt.tight_layout()
    plt.show()
    st.pyplot(plt)
    
    with st.expander("Conlusion"):
        st.markdown("""
                    Looking at the top 10 cities with the highest number of orders, considering the entire dataset spanning 3 years, 
                    Sao Paulo stands out with the highest number of orders, even when broken down annually. 
                    It might be worthwhile to focus our target market efforts on this city.
                    """)

with tab3:
    st.subheader("See how orders grow each quarter each year?")

    # define data
    data_3_quarter = orders_df[["order_purchase_timestamp"]]
    data_3_quarter = data_3_quarter.sort_values(by="order_purchase_timestamp")
    data_3_quarter["order_purchase_timestamp"] = pd.to_datetime(data_3_quarter["order_purchase_timestamp"])

    # set quarter
    data_3_quarter["quarter"] = data_3_quarter["order_purchase_timestamp"].dt.to_period("Q")
    quarterly_counts = data_3_quarter.groupby(by="quarter").count()
    quarter_list = list(quarterly_counts.index.astype(str))

    # set plotting
    sns.set_theme(style="whitegrid")

    # Now plot using Seaborn
    plt.figure(figsize=(15, 6))
    sns.lineplot(data=quarterly_counts, x=[i for i in quarter_list], y='order_purchase_timestamp', marker="o")
    plt.title("Growth order by Quarter Years")
    plt.xlabel("Quarter for each Years")
    plt.ylabel("Total Order per Quarter")
    plt.tight_layout()
    plt.show()
    st.pyplot(plt)
    
    with st.expander("Conlusion"):
        st.markdown("""
                    Total orders experienced a significant increase from the 3rd quarter of 2016 until reaching a peak in the 1st quarter of 2018. 
                    After reaching a peak in the 1st quarter of 2018, total orders experienced a decline in the 3rd quarter of 2018.
                    """)
