import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
import pandas as pd
 
API_URL = 'https://road-damage-detector-api.onrender.com'
 
SEVERITY_COLOR = {
    'Severe':   'red',
    'Moderate': 'orange',
    'Minor':    'green'
}
 
def show():
    st.title('Road Damage Map')
 
    # Fetch reports from API
    response = requests.get(f'{API_URL}/reports?limit=500')
    if response.status_code != 200:
        st.error('Could not load reports')
        return
 
    reports = response.json()
    df = pd.DataFrame(reports)
 
    if df.empty or 'latitude' not in df.columns:
        st.warning('No geotagged reports yet. Upload images with GPS coordinates.')
        return
 
    df = df.dropna(subset=['latitude', 'longitude'])
 
    # Summary metrics
    c1, c2, c3 = st.columns(3)
    c1.metric('Total Reports', len(df))
    c2.metric('Severe Cases', len(df[df['severity']=='Severe']))
    c3.metric('Locations', df[['latitude','longitude']].drop_duplicates().shape[0])
 
    # Build map centered on data
    center_lat = df['latitude'].mean()
    center_lon = df['longitude'].mean()
    m = folium.Map(location=[center_lat, center_lon], zoom_start=13)
 
    # Add markers
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=10 if row['severity']=='Severe' else 6,
            color=SEVERITY_COLOR.get(row['severity'], 'blue'),
            fill=True,
            fill_opacity=0.7,
            popup=folium.Popup(
                f"<b>{row['class_name'].title()}</b><br>"
                f"Severity: {row['severity']}<br>"
                f"Confidence: {row['confidence']}<br>"
                f"Time: {row['timestamp']}",
                max_width=200
            )
        ).add_to(m)
 
    st_folium(m, width=800, height=500)
 
    # Data table below map
    st.subheader('Recent Reports')
    st.dataframe(
        df[['timestamp','class_name','severity','confidence','latitude','longitude']]
        .rename(columns={'class_name':'Type','confidence':'Confidence'}),
        use_container_width=True
    )