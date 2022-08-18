import datetime
import dateutil.relativedelta
import streamlit as st
import pandas as pd
from Querys import Querys

query = Querys()

####### Side Bar ######

st.sidebar.header("Table Builder (EPIAS Transparency API)")
st.sidebar.write("Make your selection and create table")

st.sidebar.subheader("Date")

startDate = st.sidebar.date_input(
     "Start Date",
     datetime.date.today() + dateutil.relativedelta.relativedelta(months=-1))


endDate = st.sidebar.date_input(
     "End Date",
     datetime.date.today())


st.sidebar.markdown("***")

selected_columns = []

st.sidebar.subheader("Electricity Market")
select_market_item = st.sidebar.multiselect(
     "",
     ['MCP (TL/MWh)' , 'MCP (EUR/MWh)', 'MCP (USD/MWh)', 'SMP (TL/MWh)' ,'Regulation','IDM - Weighted Average Price', "Net Regulation (MWh)", "Up Regulation 0 Coded (MWh)", "Up Regulation 1 Coded (MWh)", "Up Regulation 2 Coded (MWh)", "Down Regulation 0 Coded (MWh)","Down Regulation 1 Coded (MWh)", "Down Regulation 2 Coded (MWh)","Up Regulation Delivered (MWh)","Down Regulation Delivered (MWh)", "System's Direction",'Primary Frequence Capacity Price (TL/MWh)', 'Primary Frequence Capacity Amount (MWh)','Secondary Frequence Capacity Price (TL/MWh)', 'Secondary Frequence Capacity Amount (MWh)' ],
     ['MCP (TL/MWh)'])
for i in select_market_item:
    if len(select_market_item) != 0:
        selected_columns.append(i)

st.sidebar.markdown("***")

st.sidebar.subheader("Electricity Consumption")
select_consumption = st.sidebar.multiselect(
     "",
     ['Real Time Consumption (MWh)'],
     ['Real Time Consumption (MWh)'])
for i in select_consumption:
    if len(select_consumption) != 0:
        selected_columns.append(i)

st.sidebar.markdown("***")

st.sidebar.subheader("Electricity Generation")
select_generation = st.sidebar.multiselect(
      "",
     ['Asphaltite Coal', 'Biomass', 'Black Coal', 'Dammed Hydro', 'Fuel Oil', 'Gas Oil', 'Geothermal', 'Import Coal', 'Import Export', 'Lignite', 'Lng', 'Naptha', 'Natural Gas', 'Nucklear', 'River', 'Sun', 'Total Generation', 'Wasteheat' , 'Wind'],
     ['Total Generation'])
for i in select_generation:
    if len(select_generation) != 0:
        selected_columns.append(i)

#st.write(selected_columns)

st.sidebar.markdown("***")


##### Main Page #####

st.header("Table Builder (EPIAS Transparency API)")

st.markdown("""
##### Hi 👋, I'm Fatih
- 📄 Know about my experiences [Linkedin](https://www.linkedin.com/in/fthky/)

- 👨‍💻 All of my projects are available at [Github](https://github.com/fthky)

- 📫 How to reach me [E-Mail](mailto:fatihkaaya@outlook.com)

""")

#### Create Table ####

column_names = {
    "Real Time Consumption (MWh)" : "Real Time Consumption (MWh)",
    "MCP (TL/MWh)" : "MCP (TL/MWh)",
    "MCP (EUR/MWh)" : "MCP (EUR/MWh)",
    "MCP (USD/MWh)" : "MCP (USD/MWh)",
    "Asphaltite Coal" : "Asphaltite Coal",
    "Biomass" : "Biomass",
    "Black Coal" : "Black Coal",
    "Dammed Hydro" : "Dammed Hydro",
    "Fuel Oil" : "Fuel Oil",
    "Gas Oil" : "Gas Oil",
    "Geothermal" : "Geothermal",
    "Import Coal" : "Import Coal",
    "Import Export" : "Import Export",
    "Lignite" : "Lignite",
    "Lng" : "Lng",
    "Naptha" : "Naptha",
    "Natural Gas" : "Natural Gas",
    "Nucklear" : "Nucklear",
    "River" : "River",
    "Sun" : "Sun",
    "Total Generation" : "Total Generation",
    "Wasteheat" : "Wasteheat",
    "Wind" : "Wind",
    "IDM - Weighted Average Price" : "IDM - Weighted Average Price",
    "Primary Frequence Capacity Price (TL/MWh)" : "Primary Frequence Capacity Price (TL/MWh)",
    "Primary Frequence Capacity Amount (MWh)" : "Primary Frequence Capacity Amount (MWh)",
    "Secondary Frequence Capacity Price (TL/MWh)" : "Secondary Frequence Capacity Price (TL/MWh)",
    "Secondary Frequence Capacity Amount (MWh)" : "Secondary Frequence Capacity Amount (MWh)",
    "SMP (TL/MWh)" : "SMP (TL/MWh)",
    "Regulation" : "Regulation",
    "Net Regulation (MWh)" : "Net Regulation (MWh)",
    "Up Regulation 0 Coded (MWh)" : "Up Regulation 0 Coded (MWh)",
    "Up Regulation 1 Coded (MWh)" : "Up Regulation 1 Coded (MWh)",
    "Up Regulation 2 Coded (MWh)" : "Up Regulation 2 Coded (MWh)",
    "Down Regulation 0 Coded (MWh)" : "Down Regulation 0 Coded (MWh)",
    "Down Regulation 1 Coded (MWh)" : "Down Regulation 1 Coded (MWh)",
    "Down Regulation 2 Coded (MWh)" : "Down Regulation 2 Coded (MWh)",
    "Up Regulation Delivered (MWh)" : "Up Regulation Delivered (MWh)",
    "Down Regulation Delivered (MWh)" : "Down Regulation Delivered (MWh)",
    "System's Direction" : "System's Direction",
    }

names=["date"]

for i in selected_columns:
    x = column_names.get(i)
    names.append(x)


def create_table():
    df_date = query.getDate(endDate,startDate)
    df_consumption = query.realTimeConsumption(endDate,startDate,selected_columns)
    df_mcp = query.mcp(endDate,startDate,selected_columns)
    df_generation = query.realTimeGeneration(endDate,startDate,selected_columns)
    df_weightedAveragePriceIDM = query.weightedAveragePriceIDM(endDate,startDate,selected_columns)
    df_pfcp = query.primaryFrequenceCapacityPrice(endDate, startDate, selected_columns)
    df_pfca = query.primaryFrequenceCapacityAmount(endDate, startDate, selected_columns)
    df_sfcp = query.secondaryFrequenceCapacityPrice(endDate, startDate, selected_columns)
    df_sfca = query.secondaryFrequenceCapacityAmount(endDate, startDate, selected_columns)
    df_smp = query.smp(endDate, startDate, selected_columns)
    df_bpm = query.bpm(endDate, startDate, selected_columns)

    df_all = pd.concat([
        df_date,
        df_mcp,
        df_consumption,
        df_generation,
        df_weightedAveragePriceIDM,
        df_pfcp,
        df_pfca,
        df_sfcp,
        df_sfca,
        df_smp,
        df_bpm,
        ], axis=1)
    df_merge= df_all.loc[:,~df_all.columns.duplicated()]

    result = df_merge[names]
   
    @st.cache
    def convert_df(result):
        return result.to_csv().encode('utf-8')


    csv = convert_df(result)

    st.download_button(
    "Download (CSV File)",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )

    st.write(result)
     
##### Show Table #####

if st.sidebar.button('Create Table'):
    if len(selected_columns)==0:
        st.markdown("""
        #### Please choose at least one column name
        """)
    else:
        st.markdown("""
        #### Your table is ready 👇

        You can download it in CSV format with the button.
        """)

        create_table()
       
else:
   st.markdown("""
                ##### About Application
                Have you created a dataset by taking columns from different excel files and combining them in another excel file? 
                If your answer is yes, you know how boring and time consuming activity this is. 
                In this application, you can create any data collection from hourly data in the 
                'EPİAŞ Transparency API'. All you have to do is select the dates and columns you want.
                
                ###### You can open the data selection tab on mobile devices by using the arrow in the upper left or you can choose to use full screen from the computer.

                ##### Built With

                [EPİAS Transparency API](https://seffaflik.epias.com.tr/transparency/) | [Python](https://www.python.org) | [Streamlit](https://streamlit.io) | [Pandas](https://pandas.pydata.org)
                """)

st.sidebar.markdown("***")
