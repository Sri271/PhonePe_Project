import git
import pandas as pd
import json
import os
import streamlit as st
from streamlit_option_menu import option_menu
import sqlite3
import plotly.express as px

# git.Repo.clone_from('https://github.com/PhonePe/pulse.git', 'PhonePe_Pulse')
path = "PhonePe_Pulse/data/aggregated/transaction/country/india/state"
Agg_state_list = os.listdir(path)

clm = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [], 'Transaction_amount': []}

for i in Agg_state_list:
    p_i = os.path.join(path, i)
    Agg_yr_list = os.listdir(p_i)
    for j in Agg_yr_list:
        p_j = os.path.join(p_i, j)
        Agg_qtr_list = os.listdir(p_j)
        for k in Agg_qtr_list:
            p_k = os.path.join(p_j, k)
            with open(p_k, 'r') as Data:
                D = json.load(Data)
            for z in D['data']['transactionData']:
                Name = z['name']
                count = z['paymentInstruments'][0]['count']
                amount = z['paymentInstruments'][0]['amount']
                clm['Transaction_type'].append(Name)
                clm['Transaction_count'].append(count)
                clm['Transaction_amount'].append(amount)
                clm['State'].append(i)
                clm['Year'].append(int(j.split('-')[0]))  # Extract year from folder name
                clm['Quarter'].append(int(k.strip('.json')))  # Extract quarter from filename

Agg_Trans = pd.DataFrame(clm)
Agg_Trans.to_csv('aggregated_transaction.csv', index=False)


path2 = "PhonePe_Pulse/data/aggregated/user/country/india/state"
user_list = os.listdir(path2)

clm2 = {'State': [], 'Year': [], 'Quarter': [], 'brands': [], 'Count': [], 'Percentage': []}

for i in user_list:
    p_i = os.path.join(path2, i)
    Agg_yr_list = os.listdir(p_i)

    for j in Agg_yr_list:
        p_j = os.path.join(p_i, j)
        Agg_qtr_list = os.listdir(p_j)

        for k in Agg_qtr_list:
            p_k = os.path.join(p_j, k)
            # print(p_k)
            with open(p_k, 'r') as Data:
                B = json.load(Data)

            try:
                for w in B["data"]["usersByDevice"]:
                    brand_name = w["brand"]
                    count_ = w["count"]
                    ALL_percentage = w["percentage"]
                    clm2["brands"].append(brand_name)
                    clm2["Count"].append(count_)
                    clm2["Percentage"].append(ALL_percentage)
                    clm2["State"].append(i)
                    clm2["Year"].append(int(j.split('-')[0]))  # Extract year from folder name
                    clm2["Quarter"].append(int(k.strip('.json')))  # Extract quarter from filename
            except:
                pass

df_aggregated_user = pd.DataFrame(clm2)
df_aggregated_user.to_csv('aggregated_user.csv', index=False)



path3 = "PhonePe_Pulse/data/map/transaction/hover/country/india/state"
hover_list = os.listdir(path3)

clm3 = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'count': [], 'amount': []}

for i in hover_list:
    p_i = os.path.join(path3, i)
    Agg_yr_list = os.listdir(p_i)

    for j in Agg_yr_list:
        p_j = os.path.join(p_i, j)
        Agg_qtr_list = os.listdir(p_j)

        for k in Agg_qtr_list:
            p_k = os.path.join(p_j, k)
            with open(p_k, 'r') as Data:
                C = json.load(Data)
            for x in C["data"]["hoverDataList"]:
                District = x["name"]
                count = x["metric"][0]["count"]
                amount = x["metric"][0]["amount"]
                clm3["District"].append(District)
                clm3["count"].append(count)
                clm3["amount"].append(amount)
                clm3['State'].append(i)
                clm3['Year'].append(j)
                clm3['Quarter'].append(int(k.strip('.json')))

df_map_transaction = pd.DataFrame(clm3)
df_map_transaction.to_csv('map_transaction.csv', index=False)


path4 = "PhonePe_Pulse/data/map/user/hover/country/india/state"
map_list = os.listdir(path4)

clm4 = {"State": [], "Year": [], "Quarter": [], "District": [], "RegisteredUser": []}

for i in map_list:
    p_i = os.path.join(path4, i)
    Agg_yr_list = os.listdir(p_i)

    for j in Agg_yr_list:
        p_j = os.path.join(p_i, j)
        Agg_qtr_list = os.listdir(p_j)

        for k in Agg_qtr_list:
            p_k = os.path.join(p_j, k)
            with open(p_k, 'r') as Data:
                D = json.load(Data)
            for u in D["data"]["hoverData"].items():
                district = u[0]
                registereduser = u[1]["registeredUsers"]
                clm4["District"].append(district)
                clm4["RegisteredUser"].append(registereduser)
                clm4['State'].append(i)
                clm4['Year'].append(j)
                clm4['Quarter'].append(int(k.strip('.json')))

df_map_user = pd.DataFrame(clm4)
df_map_user.to_csv('map_user.csv', index=False)


path5 = "PhonePe_Pulse/data/top/transaction/country/india/state"
TOP_list = os.listdir(path5)

clm5 = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Transaction_count': [], 'Transaction_amount': []}

for i in TOP_list:
    p_i = os.path.join(path5, i)
    Agg_yr_list = os.listdir(p_i)

    for j in Agg_yr_list:
        p_j = os.path.join(p_i, j)
        Agg_qtr_list = os.listdir(p_j)

        for k in Agg_qtr_list:
            p_k = os.path.join(p_j, k)
            with open(p_k, 'r') as Data:
                E = json.load(Data)
            for z in E['data']['pincodes']:
                Name = z['entityName']
                count = z['metric']['count']
                amount = z['metric']['amount']
                clm5['District'].append(Name)
                clm5['Transaction_count'].append(count)
                clm5['Transaction_amount'].append(amount)
                clm5['State'].append(i)
                clm5['Year'].append(j)
                clm5['Quarter'].append(int(k.strip('.json')))

df_top_transaction = pd.DataFrame(clm5)
df_top_transaction.to_csv('top_transaction.csv', index=False)


path6 = "PhonePe_Pulse/data/top/user/country/india/state"
USER_list = os.listdir(path6)

clm6 = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'RegisteredUser': []}

for i in USER_list:
    p_i = os.path.join(path6, i)
    Agg_yr_list = os.listdir(p_i)

    for j in Agg_yr_list:
        p_j = os.path.join(p_i, j)
        Agg_qtr_list = os.listdir(p_j)

        for k in Agg_qtr_list:
            p_k = os.path.join(p_j, k)
            with open(p_k, 'r') as Data:
                F = json.load(Data)
            for t in F['data']['pincodes']:
                Name = t['name']
                registeredUser = t['registeredUsers']
                clm6['District'].append(Name)
                clm6['RegisteredUser'].append(registeredUser)
                clm6['State'].append(i)
                clm6['Year'].append(j)
                clm6['Quarter'].append(int(k.strip('.json')))

df_top_user = pd.DataFrame(clm6)
df_top_user.to_csv('top_user.csv', index=False)


connection = sqlite3.connect("phonepe pulse.db")
cursor = connection.cursor()

Agg_Trans.to_sql('aggregated_transaction', connection, if_exists='replace')
df_aggregated_user.to_sql('aggregated_user', connection, if_exists='replace')
df_map_transaction.to_sql('map_transaction', connection, if_exists='replace')
df_map_user.to_sql('map_user', connection, if_exists='replace')
df_top_transaction.to_sql('top_transaction', connection, if_exists='replace')
df_top_user.to_sql('top_user', connection, if_exists='replace')

st.title("PhonePe Pulse Data Visualization and Exploration")
st.write( f'<h6 style="color:rgb(0,  102, 204, 255);">App Created by Sriram</h6>', unsafe_allow_html=True ) 
SELECT = option_menu(
        menu_title = None,
        options = ["Search Data", "Home", "Basic Insights"],
        icons =["search", "house", "toggles"],
        default_index=1,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "black","size":"cover"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
            "nav-link-selected": {"background-color": "#6F36AD"}
        }

    )


if SELECT == "Basic Insights":
    st.title("BASIC INSIGHTS")
    #st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--","Top 10 states based on year and amount of transaction","Least 10 states based on type and amount of transaction",
               "Top 10 mobile brands based on percentage of transaction","Top 10 Registered-users based on States and District(pincode)",
               "Top 10 Districts based on states and amount of transaction","Least 10 Districts based on states and amount of transaction",
               "Least 10 registered-users based on Districts and states","Top 10 transactions_type based on states and transaction_amount"]
    select = st.selectbox("Select the option",options)
    if select=="Top 10 states based on year and amount of transaction":
        cursor.execute("SELECT DISTINCT State,Transaction_amount,Year,Quarter FROM top_transaction GROUP BY State ORDER BY transaction_amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_amount','Year','Quarter'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 states based on type and amount of transaction")
            fig=px.bar(df,x="State",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Least 10 states based on type and amount of transaction":
        cursor.execute("SELECT DISTINCT State,Transaction_amount,Year,Quarter FROM top_transaction GROUP BY State ORDER BY transaction_amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_amount','Year','Quarter'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 states based on type and amount of transaction")
            fig=px.bar(df,x="State",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Top 10 mobile brands based on percentage of transaction":
        cursor.execute("SELECT DISTINCT brands,Percentage FROM aggregated_user GROUP BY brands ORDER BY Percentage DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['brands','Percentage'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 mobile brands based on percentage of transaction")
            fig=px.bar(df,x="brands",y="Percentage")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Top 10 Registered-users based on States and District(pincode)":
        cursor.execute("SELECT DISTINCT State,District,RegisteredUser FROM top_user GROUP BY State,District ORDER BY RegisteredUser DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','RegisteredUser'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 Registered-users based on States and District(pincode)")
            fig=px.bar(df,x="State",y="RegisteredUser")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Top 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT State,District,amount FROM map_transaction GROUP BY State,District ORDER BY amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Transaction_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 Districts based on states and amount of transaction")
            fig=px.bar(df,x="State",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Least 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT State,District,amount FROM map_transaction GROUP BY State,District ORDER BY amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Transaction_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 Districts based on states and amount of transaction")
            fig=px.bar(df,x="State",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Least 10 registered-users based on Districts and states":
        cursor.execute("SELECT DISTINCT State,District,RegisteredUser FROM top_user GROUP BY State,District ORDER BY RegisteredUser ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','RegisteredUser'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 registered-users based on Districts and states")
            fig=px.bar(df,x="State",y="RegisteredUser")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Top 10 transactions_type based on states and transaction_amount":
        cursor.execute("SELECT DISTINCT State,Transaction_type,Transaction_amount FROM aggregated_transaction GROUP BY State,Transaction_type ORDER BY Transaction_amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_type','Transaction_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 transactions_type based on states and transaction_amount")
            fig=px.bar(df,x="State",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

if SELECT == "Home":
    st.subheader(
        "PhonePe is an Indian digital payments and financial services company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface, went live in August 2016")
   

if SELECT =="Search Data":
    Topic = ["Brand","District","Registered-users","Top-Transactions","Transaction-Type"]
    choice_topic = st.selectbox("Search by",Topic)

#creating functions for query search in sqlite to get the data
    def type_(type):
        cursor.execute(f"SELECT DISTINCT State,Quarter,Year,Transaction_type,Transaction_amount FROM aggregated_transaction WHERE Transaction_type = '{type}' ORDER BY State,Quarter,Year");
        df = pd.DataFrame(cursor.fetchall(), columns=['State','Quarter', 'Year', 'Transaction_type', 'Transaction_amount'])
        return df
    def type_year(year,type):
        cursor.execute(f"SELECT DISTINCT State,Year,Quarter,Transaction_type,Transaction_amount FROM aggregated_transaction WHERE Year = '{year}' AND Transaction_type = '{type}' ORDER BY State,Quarter,Year");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'Transaction_type', 'Transaction_amount'])
        return df
    def type_state(state,year,type):
        cursor.execute(f"SELECT DISTINCT State,Year,Quarter,Transaction_type,Transaction_amount FROM aggregated_transaction WHERE State = '{state}' AND Transaction_type = '{type}' And Year = '{year}' ORDER BY State,Quarter,Year");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'Transaction_type', 'Transaction_amount'])
        return df
    def district_choice_state(_state):
        cursor.execute(f"SELECT DISTINCT State,Year,Quarter,District,amount FROM map_transaction WHERE State = '{_state}' ORDER BY State,Year,Quarter,District");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'amount'])
        return df
    def dist_year_state(year,_state):
        cursor.execute(f"SELECT DISTINCT State,Year,Quarter,District,amount FROM map_transaction WHERE Year = '{year}' AND State = '{_state}' ORDER BY State,Year,Quarter,District");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'amount'])
        return df
    def district_year_state(_dist,year,_state):
        cursor.execute(f"SELECT DISTINCT State,Year,Quarter,District,amount FROM map_transaction WHERE District = '{_dist}' AND State = '{_state}' AND Year = '{year}' ORDER BY State,Year,Quarter,District");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'amount'])
        return df
    def brand_(brand_type):
        cursor.execute(f"SELECT State,Year,Quarter,brands,Percentage FROM aggregated_user WHERE brands='{brand_type}' ORDER BY State,Year,Quarter,brands,Percentage DESC");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'brands', 'Percentage'])
        return df
    def brand_year(brand_type,year):
        cursor.execute(f"SELECT State,Year,Quarter,brands,Percentage FROM aggregated_user WHERE Year = '{year}' AND brands='{brand_type}' ORDER BY State,Year,Quarter,brands,Percentage DESC");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'brands', 'Percentage'])
        return df
    def brand_state(state,brand_type,year):
        cursor.execute(f"SELECT State,Year,Quarter,brands,Percentage FROM aggregated_user WHERE State = '{state}' AND brands='{brand_type}' AND Year = '{year}' ORDER BY State,Year,Quarter,brands,Percentage DESC");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'brands', 'Percentage'])
        return df
    def transaction_state(_state):
        cursor.execute(f"SELECT State,Year,Quarter,District,Transaction_count,Transaction_amount FROM top_transaction WHERE State = '{_state}' GROUP BY State,Year,Quarter")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'Transaction_count', 'Transaction_amount'])
        return df
    def transaction_year(_state,_year):
        cursor.execute(f"SELECT State,Year,Quarter,District,Transaction_count,Transaction_amount FROM top_transaction WHERE Year = '{_year}' AND State = '{_state}' GROUP BY State,Year,Quarter")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'Transaction_count', 'Transaction_amount'])
        return df
    def transaction_quarter(_state,_year,_quarter):
        cursor.execute(f"SELECT State,Year,Quarter,District,Transaction_count,Transaction_amount FROM top_transaction WHERE Year = '{_year}' AND Quarter = '{_quarter}' AND State = '{_state}' GROUP BY State,Year,Quarter")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'Transaction_count', 'Transaction_amount'])
        return df
    def registered_user_state(_state):
        cursor.execute(f"SELECT State,Year,Quarter,District,RegisteredUser FROM map_user WHERE State = '{_state}' ORDER BY State,Year,Quarter,District")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'RegisteredUser'])
        return df
    def registered_user_year(_state,_year):
        cursor.execute(f"SELECT State,Year,Quarter,District,RegisteredUser FROM map_user WHERE Year = '{_year}' AND State = '{_state}' ORDER BY State,Year,Quarter,District")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'RegisteredUser'])
        return df
    def registered_user_district(_state,_year,_dist):
        cursor.execute(f"SELECT State,Year,Quarter,District,RegisteredUser FROM map_user WHERE Year = '{_year}' AND State = '{_state}' AND District = '{_dist}' ORDER BY State,Year,Quarter,District")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'RegisteredUser'])
        return df

    if choice_topic == "Transaction-Type":
        select = st.selectbox('SELECT VIEW', ['Tabular view', 'Plotly View'], 0)
        if select=='Tabular view':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT TYPE OF TRANSACTION ")
                transaction_type = st.selectbox("search by", ["Peer-to-peer payments","Merchant payments", "Financial Services","Recharge & bill payments", "Others"], 0)
            with col2:
                st.subheader("SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT STATES ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu',
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh','lakshadweep', 'madhya-pradesh',
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                              'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)

            if transaction_type:
                col1, col2, col3, = st.columns(3)
                with col1:
                    st.subheader(f'Table view of {transaction_type}')
                    st.write(type_(transaction_type))

            if transaction_type and choice_year:
                with col2:
                    st.subheader(f' in {choice_year}')
                    st.write(type_year(choice_year, transaction_type))
            if transaction_type and choice_state and choice_year:
                with col3:
                    st.subheader(f' in {choice_state}')
                    st.write(type_state(choice_state, choice_year, transaction_type))
        else:
            col1, col2,col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT TYPE OF TRANSACTION ")
                transaction_type = st.selectbox("search by", ["Peer-to-peer payments","Merchant payments", "Financial Services","Recharge & bill payments", "Others"], 0)
                if transaction_type:
                    df = type_(transaction_type)
                    fig = px.bar(df, x="State", y="Transaction_amount", title=f'Plotly view of {transaction_type}',color='Year')
                    st.plotly_chart(fig, theme=None, use_container_width=True)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
                if transaction_type and choice_year:
                    df = type_year(choice_year, transaction_type)
                    fig = px.bar(df, x="State", y="Transaction_amount",title=f"Plotly view of {transaction_type} in {choice_year}",color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)
            with col3:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu',
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh','lakshadweep', 'madhya-pradesh',
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                              'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
                if transaction_type and choice_state and choice_year:
                    df = type_state(choice_state, choice_year, transaction_type)
                    fig = px.bar(df, x="Quarter", y="Transaction_amount",title=f" {transaction_type} in {choice_year} at {choice_state}",color="Quarter")
                    st.plotly_chart(fig, theme=None, use_container_width=True)
    if choice_topic == "District":
        select = st.selectbox('View', ['Tabular view', 'Plotly View'], 0)
        if select == 'Tabular view':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state =['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                             'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                             'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland','odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura',
                             'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT DISTRICT ")
                dist=df_map_transaction["District"].unique().tolist()
                dist.sort()
                district = st.selectbox("search by", dist)
            if choice_state:
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.subheader(f'{choice_state}')
                    st.write(district_choice_state(choice_state))
            if choice_year and choice_state:
                with col2:
                    st.subheader(f'in {choice_year} ')
                    st.write(dist_year_state(choice_year, choice_state))
            if district and choice_state and choice_year:
                with col3:
                    st.subheader(f'in {district} ')
                    st.write(district_year_state(district, choice_year, choice_state))
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                             'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                             'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland','odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura',
                             'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
                if choice_state:
                    df=district_choice_state(choice_state)
                    fig = px.bar(df, x="District", y="amount", title=f'Users in {choice_state}',color='Year')
                    st.plotly_chart(fig, theme=None, use_container_width=True)

            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
                df=dist_year_state(choice_year, choice_state)
                fig = px.bar(df, x="District", y="amount", title=f'Users in  {choice_state} in {choice_year}',color='Quarter')
                st.plotly_chart(fig, theme=None, use_container_width=True)
            with col3:
                st.subheader(" SELECT DISTRICT ")
                dist=df_map_transaction["District"].unique().tolist()
                dist.sort()
                district = st.selectbox("search by",dist )
                df=district_year_state(district, choice_year, choice_state)
                fig = px.bar(df, x="Quarter", y="amount",title=f"Users {district} in {choice_year} at {choice_state}",color='Quarter')
                st.plotly_chart(fig, theme=None, use_container_width=True)
    if choice_topic == "Brand":
        select = st.selectbox('View', ['Tabular view', 'Plotly View'], 0)
        if select == 'Tabular view':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT BRAND ")
                mobiles = ['', 'Apple', 'Asus', 'COOLPAD', 'Gionee', 'HMD Global', 'Huawei', 'Infinix', 'Lava', 'Lenovo',
                           'Lyf', 'Micromax', 'Motorola', 'OnePlus', 'Oppo', 'Others', 'Realme', 'Samsung', 'Tecno', 'Vivo', 'Xiaomi']
                brand_type = st.selectbox("search by", mobiles, 0)
            with col2:
                st.subheader(" SELECT YEAR")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha',
                              'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            if brand_type:
                col1, col2, col3, = st.columns(3)
                with col1:
                    st.subheader(f'{brand_type}')
                    st.write(brand_(brand_type))
            if brand_type and choice_year:
                with col2:
                    st.subheader(f' in {choice_year}')
                    st.write(brand_year(brand_type, choice_year))
            if brand_type and choice_state and choice_year:
                with col3:
                    st.subheader(f' in {choice_state}')
                    st.write(brand_state(choice_state, brand_type, choice_year))
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT BRAND ")
                mobiles =  ['', 'Apple', 'Asus', 'COOLPAD', 'Gionee', 'HMD Global', 'Huawei', 'Infinix', 'Lava', 'Lenovo',
                           'Lyf', 'Micromax', 'Motorola', 'OnePlus', 'Oppo', 'Others', 'Realme', 'Samsung', 'Tecno', 'Vivo', 'Xiaomi']
                brand_type = st.selectbox("search by", mobiles, 0)
                if brand_type:
                    df=brand_(brand_type)
                    fig = px.bar(df, x="State", y="Percentage",title=f" {brand_type} Users ",color='Year')
                    st.plotly_chart(fig, theme=None, use_container_width=True)

            with col2:
                st.subheader(" SELECT YEAR")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
                if brand_type and choice_year:
                    df=brand_year(brand_type, choice_year)
                    fig = px.bar(df, x="State", y="Percentage",title=f"{brand_type} Users in {choice_year}",color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)
            with col3:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha',
                              'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
                if brand_type and choice_state and choice_year:
                    df=brand_state(choice_state, brand_type, choice_year)
                    fig = px.bar(df, x="Quarter", y="Percentage",title=f"{brand_type} Users in {choice_year} at {choice_state}",color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)

    if choice_topic == "Top-Transactions":
        select = st.selectbox('View', ['Tabular view', 'Plotly View'], 0)
        if select == 'Tabular view':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                              'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            with col2:
                st.subheader(" SELECT  YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT Quarter ")
                menu_quarter = ["", "1", "2", "3", "4"]
                choice_quarter = st.selectbox("Quarter", menu_quarter, 0)

            if choice_state:
                with col1:
                    st.subheader(f'{choice_state}')
                    st.write(transaction_state(choice_state))
            if choice_state and choice_year:
                with col2:
                    st.subheader(f'{choice_year}')
                    st.write(transaction_year(choice_state, choice_year))
            if choice_state and choice_quarter:
                with col3:
                    st.subheader(f'{choice_quarter}')
                    st.write(transaction_quarter(choice_state, choice_year, choice_quarter))
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                              'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
                if choice_state:
                    df=transaction_state(choice_state)
                    fig = px.bar(df, x="Year", y="Transaction_count",title=f"Transactions in {choice_state}", color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)

            with col2:
                st.subheader(" SELECT  YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
                if choice_state and choice_year:
                    df=transaction_year(choice_state, choice_year)
                    fig = px.bar(df, x="Year", y="Transaction_count",title=f"Transactions{choice_year} at {choice_state}", color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)

            with col3:
                st.subheader(" SELECT Quarter ")
                menu_quarter = ["", "1", "2", "3", "4"]
                choice_quarter = st.selectbox("Quarter", menu_quarter, 0)
                if choice_state and choice_quarter:
                    df=transaction_quarter(choice_state, choice_year, choice_quarter)
                    fig = px.bar(df, x="Quarter", y="Transaction_count",title=f"Transactions in {choice_year} at {choice_state} in Quarter {choice_quarter}", color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)

    if choice_topic == "Registered-users":
        select = st.selectbox('View', ['Tabular view', 'Plotly View'], 0)
        if select == 'Tabular view':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab',
                              'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT DISTRICT ")
                dist=df_map_transaction["District"].unique().tolist()
                dist.sort()
                district = st.selectbox("search by",dist )

            if choice_state:
                with col1:
                    st.subheader(f'{choice_state}')
                    st.write(registered_user_state(choice_state))
            if choice_state and choice_year:
                with col2:
                    st.subheader(f'{choice_year}')
                    st.write(registered_user_year(choice_state, choice_year))
            if choice_state and choice_year and district:
                with col3:
                    st.subheader(f'{district}')
                    st.write(registered_user_district(choice_state, choice_year, district))
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab',
                              'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
                if choice_state:
                    df=registered_user_state(choice_state)
                    fig = px.bar(df, x="District", y="RegisteredUser",title=f"Registered users at {choice_state} ",color='Year')
                    st.plotly_chart(fig, theme=None, use_container_width=True)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
                if choice_state and choice_year:
                    df=registered_user_year(choice_state, choice_year)
                    fig = px.bar(df, x="District", y="RegisteredUser",title=f"Registered users in {choice_state} in {choice_year}",color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)
            with col3:
                st.subheader("SELECT DISTRICT ")
                dist=df_map_transaction["District"].unique().tolist()
                dist.sort()
                district = st.selectbox("search by",dist)
                if choice_state and choice_year and district:
                    df=registered_user_district(choice_state, choice_year, district)
                    fig = px.bar(df, x="Quarter", y="RegisteredUser",title=f"Registered users at {choice_state} in {choice_year} in {district}",color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)



