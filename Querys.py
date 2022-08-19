import pandas as pd
from requests import get
import streamlit as st

class Querys:


    @st.cache
    def getQuery(self, endpoint):
        BASE_URL = "https://seffaflik.epias.com.tr/transparency/service/"
        url = BASE_URL + endpoint
        response_data = get(url).json()
        return response_data

    @st.cache
    def getDate(self, endDate, startDate):
        endpoint = f"market/day-ahead-mcp?endDate={endDate}&startDate={startDate}"
        response_data = self.getQuery(endpoint)
        df = pd.DataFrame.from_dict(response_data['body']['dayAheadMCPList'])
        df = df["date"].str.split('T', expand=True)
        df.columns = ["date",  "time"]
        df['time'] = df['time'].str[:5]
        return df

    @st.cache
    def realTimeConsumption(self, endDate, startDate, selected_columns):
        if "Real Time Consumption (MWh)" in selected_columns:
            endpoint = f"consumption/real-time-consumption?endDate={endDate}&startDate={startDate}"
            response_data = self.getQuery(endpoint)
            df_realTimeConsumption = pd.DataFrame.from_dict(response_data['body']['hourlyConsumptions'])
            df_realTimeConsumption.rename(columns={
                "date":"date",
                "consumption":"Real Time Consumption (MWh)"
                }, inplace=True)
            return df_realTimeConsumption
        else:
            pass

    @st.cache
    def mcp(self, endDate, startDate, selected_columns):
        if "MCP (TL/MWh)" in selected_columns or "MCP (EUR/MWh)" in selected_columns or "MCP (USD/MWh)" in selected_columns:  
            endpoint = f"market/day-ahead-mcp?endDate={endDate}&startDate={startDate}"
            response_data = self.getQuery(endpoint)
            df_mcp = pd.DataFrame.from_dict(response_data['body']['dayAheadMCPList'])
            df_mcp.rename(columns={
                "date":"date",
                "price":"MCP (TL/MWh)",
                "priceEur":'MCP (EUR/MWh)',
                "priceUsd":'MCP (USD/MWh)'
                }, inplace=True)
            return df_mcp

        else:
            pass

    @st.cache
    def realTimeGeneration(self, endDate, startDate, selected_columns):
        if 'Asphaltite Coal' in selected_columns or 'Biomass' in selected_columns or 'Black Coal' in selected_columns or 'Dammed Hydro' in selected_columns or 'Fuel Oil' in selected_columns or 'Gas Oil' in selected_columns or 'Geothermal' in selected_columns or 'Import Coal' in selected_columns or 'Import Export' in selected_columns or 'Lignite' in selected_columns or 'Lng' in selected_columns or 'Naptha' in selected_columns or 'Natural Gas' in selected_columns or 'Nucklear' in selected_columns or 'River' in selected_columns or 'Sun' in selected_columns or 'Total Generation' in selected_columns or 'Wasteheat' in selected_columns or 'Wind' in selected_columns :  
            endpoint = f"production/real-time-generation?endDate={endDate}&startDate={startDate}"
            response_data = self.getQuery(endpoint)
            df_realTimeGeneration = pd.DataFrame.from_dict(response_data['body']['hourlyGenerations'])
            df_realTimeGeneration.rename(columns={'asphaltiteCoal':'Asphaltite Coal', 
                                                'biomass': 'Biomass', 
                                                'blackCoal':'Black Coal', 
                                                'dammedHydro' : 'Dammed Hydro', 
                                                'date' : 'date', 
                                                'fueloil' : 'Fuel Oil', 
                                                'gasOil' : 'Gas Oil', 
                                                'geothermal' : 'Geothermal', 
                                                'importCoal' : 'Import Coal', 
                                                'importExport' : 'Import Export', 
                                                'lignite' : 'Lignite', 
                                                'lng' : 'Lng', 
                                                'naphta' : 'Naptha', 
                                                'naturalGas' : 'Natural Gas', 
                                                'nucklear' : 'Nucklear', 
                                                'river' : 'River', 
                                                'sun' : 'Sun', 
                                                'total' : 'Total Generation', 
                                                'wasteheat' : 'Wasteheat' , 
                                                'wind' : 'Wind'
                                                }, inplace = True)
            return df_realTimeGeneration

        else:
            pass


    @st.cache
    def weightedAveragePriceIDM(self, endDate, startDate, selected_columns):
        if "IDM - Weighted Average Price" in selected_columns:
            endpoint = f"market/intra-day-aof?endDate={endDate}&startDate={startDate}"
            response_data = self.getQuery(endpoint)
            df_weightedAveragePriceIDM = pd.DataFrame.from_dict(response_data['body']['idmAofList'])
            df_weightedAveragePriceIDM.rename(columns={
                "date" : "date",
                "price" : "IDM - Weighted Average Price"
                }, inplace=True)
            return df_weightedAveragePriceIDM
        else:
            pass

#######

    @st.cache
    def primaryFrequenceCapacityPrice(self, endDate, startDate, selected_columns):
        if "Primary Frequence Capacity Price (TL/MWh)" in selected_columns:
            endpoint = f"market/pfc-price?endDate={endDate}&startDate={startDate}"
            response_data = self.getQuery(endpoint)
            df_primaryFrequenceCapacityPrice = pd.DataFrame.from_dict(response_data['body']['frequencyReservePriceList'])
            df_primaryFrequenceCapacityPrice.rename(columns={
                "effectiveDate":"date",
                "price":"Primary Frequence Capacity Price (TL/MWh)"
                }, inplace=True)
            return df_primaryFrequenceCapacityPrice
        else:
            pass

    @st.cache
    def primaryFrequenceCapacityAmount(self, endDate, startDate, selected_columns):
        if "Primary Frequence Capacity Amount (MWh)" in selected_columns:
            endpoint = f"market/pfc-amount?endDate={endDate}&startDate={startDate}"
            response_data = self.getQuery(endpoint)
            df_primaryFrequenceCapacityAmount = pd.DataFrame.from_dict(response_data['body']['frequencyReservePriceList'])
            df_primaryFrequenceCapacityAmount.rename(columns={
                "effectiveDate" : "date",
                "totalAmount" : "Primary Frequence Capacity Amount (MWh)"
                },inplace=True)
            return df_primaryFrequenceCapacityAmount
        else:
            pass


    @st.cache
    def secondaryFrequenceCapacityPrice(self, endDate, startDate, selected_columns):
        if "Secondary Frequence Capacity Price (TL/MWh)" in selected_columns:
            endpoint = f"market/sfc-price?endDate={endDate}&startDate={startDate}"
            response_data = self.getQuery(endpoint)
            df_secondaryFrequenceCapacityPrice = pd.DataFrame.from_dict(response_data['body']['frequencyReservePriceList'])
            df_secondaryFrequenceCapacityPrice.rename(columns={
                "effectiveDate": "date",
                "price" : "Secondary Frequence Capacity Price (TL/MWh)"
                }, inplace=True)
            return df_secondaryFrequenceCapacityPrice
        else:
            pass


    @st.cache
    def secondaryFrequenceCapacityAmount(self, endDate, startDate, selected_columns):
        if "Secondary Frequence Capacity Amount (MWh)" in selected_columns:
            endpoint = f"market/sfc-amount?endDate={endDate}&startDate={startDate}"
            response_data = self.getQuery(endpoint)
            df_secondaryFrequenceCapacityAmount = pd.DataFrame.from_dict(response_data['body']['frequencyReservePriceList'])
            df_secondaryFrequenceCapacityAmount.rename(columns={
                "effectiveDate":"date",
                "totalAmount" : "Secondary Frequence Capacity Amount (MWh)"
            }, inplace=True) 
            return df_secondaryFrequenceCapacityAmount
        else:
            pass

    @st.cache
    def smp(self, endDate, startDate, selected_columns):
        if "SMP (TL/MWh)" in selected_columns or "Regulation" in selected_columns:
            endpoint = f"market/smp?endDate={endDate}&startDate={startDate}"
            response_data = self.getQuery(endpoint)
            df_smp = pd.DataFrame.from_dict(response_data['body']['smpList'])
            df_smp.rename(columns={
              "price" : "SMP (TL/MWh)",
              "smpDirection" : "Regulation",
            }, inplace=True)
            return df_smp
        else:
            pass



    @st.cache
    def bpm(self, endDate, startDate, selected_columns):
        if "Net Regulation (MWh)" in selected_columns or "Up Regulation 0 Coded (MWh)" in selected_columns or "Up Regulation 1 Coded (MWh)" in selected_columns or "Up Regulation 2 Coded (MWh)" in selected_columns or "Down Regulation 0 Coded (MWh)" in selected_columns or "Down Regulation 1 Coded (MWh)" in selected_columns or "Down Regulation 2 Coded (MWh)" in selected_columns or "Up Regulation Delivered (MWh)" in selected_columns or "Down Regulation Delivered (MWh)" in selected_columns or "System's Direction" in selected_columns:
            endpoint = f"market/bpm-order-summary?endDate={endDate}&startDate={startDate}"
            response_data = self.getQuery(endpoint)
            df_bpm = pd.DataFrame.from_dict(response_data['body']['bpmOrderSummaryList'])
            df_bpm.rename(columns={
                "net" : "Net Regulation (MWh)",
                "upRegulationZeroCoded" : "Up Regulation 0 Coded (MWh)",
                "upRegulationOneCoded" : "Up Regulation 1 Coded (MWh)",
                "upRegulationTwoCoded" : "Up Regulation 2 Coded (MWh)",
                "downRegulationZeroCoded" : "Down Regulation 0 Coded (MWh)",
                "downRegulationOneCoded" : "Down Regulation 1 Coded (MWh)",
                "downRegulationTwoCoded" : "Down Regulation 2 Coded (MWh)",
                "upRegulationDelivered" : "Up Regulation Delivered (MWh)",
                "downRegulationDelivered" : "Down Regulation Delivered (MWh)",
                "direction" : "System's Direction"
            }, inplace=True)
            return df_bpm
        else:
            pass
