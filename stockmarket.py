import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf


st.title("Stock market application.Enjoy!!")

st.write("We can now see the stock price of a company")
user_input=st.text_input("Enter your desired stock market company analysis")

ticket_data=yf.Ticker(user_input)

# hist_data=ticket_data.history(start="2022-05-01", end='2024-05-01')
start_date=st.date_input("Enter the start data",value=pd.to_datetime("21-08-10"))
end_date=st.date_input("Enter the end date", value=pd.to_datetime("today"))

hist_data=ticket_data.history(start=start_date, end=end_date)
# hist_data.info

st.write("Now we are able to see apple stock price")

st.write(hist_data)

# st.write("This is for volume line chart")
# st.line_chart(hist_data.Volume)

# st.write("Show me the closing price")

# st.line_chart(hist_data.Close)


col1,col2=st.columns(2)

with col1:
    st.line_chart(hist_data.Volume)
with col2:
    st.line_chart(hist_data.Close)




