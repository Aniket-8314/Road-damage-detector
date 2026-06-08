import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
 
API_URL = 'http://localhost:8000'

 
def show():
    st.title('Road Damage Analytics')
 
    resp = requests.get(f'{API_URL}/reports?limit=1000')
    if resp.status_code != 200:
        st.error('Could not load data')
        return
 
    df = pd.DataFrame(resp.json())
    if df.empty:
        st.info('No data yet. Start detecting road damage first!')
        return
 
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date
 
    k1, k2, k3, k4 = st.columns(4)
    k1.metric('Total Detections', len(df))
    k2.metric('Potholes', len(df[df['class_name']=='pothole']))
    k3.metric('Cracks', len(df[df['class_name']=='crack']))
    k4.metric('Avg Confidence', f"{df['confidence'].mean():.1%}")
 
    st.divider()
 
    c1, c2 = st.columns(2)
 
    with c1:
        fig = px.pie(
            df, names='severity',
            title='Damage Severity Distribution',
            color='severity',
            color_discrete_map={'Severe':'#CC0000','Moderate':'#E07000','Minor':'#2E7D32'}
        )
        st.plotly_chart(fig, use_container_width=True)
 
    with c2:
        fig2 = px.histogram(
            df, x='class_name', color='severity',
            title='Damage Type Breakdown',
            color_discrete_map={'Severe':'#CC0000','Moderate':'#E07000','Minor':'#2E7D32'},
            barmode='group'
        )
        st.plotly_chart(fig2, use_container_width=True)
 
    daily = df.groupby(['date','severity']).size().reset_index(name='count')
    fig3 = px.line(
        daily, x='date', y='count', color='severity',
        title='Detections Over Time',
        color_discrete_map={'Severe':'#CC0000','Moderate':'#E07000','Minor':'#2E7D32'}
    )
    st.plotly_chart(fig3, use_container_width=True)