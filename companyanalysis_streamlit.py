# Importing Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
sns.set()

# st.write("Hello, Streamlit World")

# Displaying Text
# st.text("Text")
# st.write("Super function")
# st.header("Header")
# st.subheader("Sub Header")
# st.title("Title")
# st.markdown("***markdown***")
# st.code("print('Hello world')",language="python")

# Displaying Interactive Widgets
# btn = st.button("submit") 
# if btn:
#     st.info("info")
# option = st.radio("Select", ["A","B","C"])
# if option == "A":
#     st.warning("Warining")
# elif option == "B":
#     st.error("Error")
# elif option == "C":
#     st.success("Success :)") 

# check = st.checkbox("I agree")
# if check:
#     st.exception("Agreement")
# selectbox1 = st.selectbox("Select",["a","b","c"])
# st.slider("select",0,100)

df = pd.read_csv("company_all_data.csv.csv",encoding= 'iso-8859-1')
# btn = st.button("Show Data")
# if btn:
#         st.dataframe(df.sample(5))

# st.header("Matplotlib")
# st.subheader("Line Plot")

st.title("Company Sales Analysis")
st.sidebar.header("Sidebar List")
st.sidebar.markdown("Made with :revolving_hearts: by [Khaled Shaker](https://www.linkedin.com/in/khaledshakerrr/)	")
url_img1 = "sidebarimg.jpeg"
st.sidebar.image(url_img1)
sidebar_var = st.sidebar.radio("Select One: ",["Author","Data Overview","EDA","PowerBI Dashboard"]     )

if sidebar_var == "PowerBI Dashboard":
    st.subheader("Company Analysis Dashboard")
    url_img2 = "companysales_jpeg.jpg"
    st.image(url_img2,width=1000)
elif sidebar_var == "Data Overview":
    st.markdown("**this project aim to analyze commpany sales behavior using the online dataset and Python analytical functions and frameworks. It involves answering questions about the data through python frameworks.**")
    st.markdown("** The Data set used for this project is the `Online company sales dataset`, which contain information about company sales, including invoices total amount, product details, and customer IDS.**")
    st.dataframe(df.head())
    st.subheader("Show a sample")
    btn2 = st.button("Show me")
    if btn2:
        st.dataframe(df.sample(5))
elif sidebar_var == "EDA":
    st.subheader(":blue[Total Amount Distribution]",divider="rainbow")
    # Create the histogram plot
    fig2 = sns.histplot(data=df, x="TotalAmount", kde=True)
    plt.title("Distribution of Total amount of Invoices")
    plt.xlabel("Total Amount")
    plt.ylabel("Frequency")
    plt.axvline(df["TotalAmount"].mean(), color="r")
    plt.axvline(df["TotalAmount"].median(), color="black")
    # Save the plot as a PNG file
    # fig2.figure.savefig("total_amount_distribution.png")
    st.pyplot(fig=fig2.get_figure())
    st.markdown("""The histogram provides insights into the `billing patterns` of the company:  """)
    st.markdown("**Here's a concise description**")
    st.markdown("1. **Peak at Lower Amounts**: Most invoices cluster around the lower end of the total amount axis `(before 2.500)`.These likely represent routine transactions.")
    st.markdown("2. **Tail of High-Value Invoices**: While most invoices are smaller there's a tail streteching toward `17.500` These high value-invoices could be significant revenue or crutial transaction")
    st.divider()
    st.subheader(":blue[Total Amount Boxplot]",divider="rainbow")
    import plotly.express as px
    fig3= px.box(data_frame=df,x=df["TotalAmount"])
    st.plotly_chart(fig3)
    st.markdown(""" **In this boxplot, we explore the distribution of total invoice amounts within our company. The plot showcases key statistical points, revealing insights into billing patterns**""")
    st.markdown("""1. **Central Tendency**:
                The median invoice amount `(around $3,000)` represents the typical value. Most invoices fall within the interquartile range (Q1 to Q3), spanning approximately `$2,500 to $4,000.`""")
    st.markdown(""" 2. **Variability**:
                The whiskers extend beyond this range, indicating variability. Outliers (individual points beyond the whiskers) highlight exceptional cases—either unusually high or low invoice amounts. """)
    st.divider()
    st.subheader(":blue[Distribution Of Cities]",divider="rainbow")
    fig4 = px.bar(df["City"].value_counts(),title="Distribution of cities")
    st.plotly_chart(fig4)
    st.markdown("""**The bar chart represents the countries based on the total amount of invoices in a company.** """)
    st.markdown("- **London**: Leading the pack with the highest invoice count, London dominates the sales landscape. ")
    st.markdown("- **Vancouver**: Following London, Vancouver contributes significantly to the company’s invoicing activity. ")
    st.markdown("- **Reims, Torino, and Berlin**:These cities exhibit moderate invoice volumes.")
    st.markdown("- **Toulouse, Barquisimeto, and Oulu**: he least active cities in terms of invoicing.")
    st.divider()
    st.subheader("Pie Chart for the total amount invoices per Country",divider="rainbow")
    fig5= px.pie(df,names=df["Country"],title="Relavtive Frequency of countries sales")
    st.plotly_chart(fig5)
    date_total = df[["OrderDate","TotalAmount"]]
    date_total = date_total.set_index("OrderDate")
    st.divider()
    st.subheader("Time Series Data",divider="rainbow")
    fig6= px.line(date_total,width=1000,height=400)
    st.plotly_chart(fig6)
    st.divider()
    st.subheader("Bar Chart Number of orders per customer",divider="rainbow")
    cust_orders = {"fullname":df["FirstName"]+' '+df["LastName"],
              "totalamount":df["TotalAmount"]}
    cust_orders = pd.DataFrame(cust_orders)
    fig7 = px.bar(cust_orders.groupby("fullname")["totalamount"].count().sort_values(ascending=False).head(),text_auto=True,title="No. of orders per customer" )
    labels = {"fullname": "Full Name","value":"Frequency"}
    fig7.update_traces(marker_color="rgb(158,202,245)",marker_line_color="rgb(8,245,107)",
                    marker_line_width=1.5,opacity=0.6,textposition="outside")
                    
    st.plotly_chart(fig7)
    st.divider()
    # st.subheader("Grand Total Amount of all Countries per Month",divider="rainbow")
    # multivar = df[["OrderDate","Country","TotalAmount"]]
    # # multivar = multivar.set_index("OrderDate")
    # multivar = multivar.resample("1M").agg({"Country":"nunique",
    #                                    "TotalAmount":"sum"})
    # fig8 = px.bar(data_frame=multivar,x=multivar.index,y=round(multivar.TotalAmount,0),color=multivar.Country,text_auto=True,title="Grand total amount of all countries per Month")
    # fig8.update_traces(textposition="outside")
    # fig8.update_layout(title_x=0.5)
    # multivar2 = df[["OrderDate","Country","TotalAmount"]]
    # multivar2 = multivar2.groupby(["OrderDate","Country"],as_index=False)["TotalAmount"].sum().sort_values(by="TotalAmount",ascending=False)
    # fig9 = px.scatter(data_frame=multivar2,x=multivar2["OrderDate"],y=multivar2["TotalAmount"],color=multivar2["Country"],size=multivar2["TotalAmount"],width=1000)
    # st.plotly_chart(fig9)
elif sidebar_var == "Author":
    pass
    st.subheader("Author info")
    url_profile = "profile.png"
    st.image(url_profile,width=500,channels="RGB")
    st.markdown("## :blue[Meet Your Favourite Date Scientist]")
    st.markdown("**- Khaled Shaker : ITI Trainee, Versatile data scientist with a Radiology and medical imaging**")
    st.markdown("**- background, specializing in tailored machine learning solutions for real use cases.**  ")
    st.markdown("**- `Top 5%` graduate in Applied Medical Science Program, with a pre master's degree in medical physics.** ")
    st.markdown("**- Committed to continue learning and innovation, translating complex data into actionable strategies**")
    st.markdown("**- for business growth.**")
    st.markdown("**GitHUB Account**: [My GitHub](https://github.com/khaledshakerrr)")
    st.markdown("**Linkedin**: [Linkedin](https://www.linkedin.com/in/khaledshakerrr/)")
    st.markdown("**Phone**: +201113128114")