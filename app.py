import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    """Load the vehicle dataset"""
    df = pd.read_csv('vehicles_us.csv')
    return df

# Page configuration
st.set_page_config(
    page_title="US Vehicle Sales Dashboard",
    page_icon="🚗",
    layout="wide"
)

# Load the data
df = load_data()

# Title and description
st.title('🚗 US Vehicle Sales Data Analysis')
st.markdown('### Explore and analyze vehicle listings in the United States')

# Sidebar filters
st.sidebar.header('Filter Options')

# Price filter
price_range = st.sidebar.slider(
    'Price Range',
    min_value=int(df['price'].min()),
    max_value=int(df['price'].max()),
    value=(int(df['price'].min()), int(df['price'].max()))
)

# Year filter
year_range = st.sidebar.slider(
    'Model Year',
    min_value=int(df['model_year'].min()),
    max_value=int(df['model_year'].max()),
    value=(int(df['model_year'].min()), int(df['model_year'].max()))
)

# Condition filter
conditions = ['All'] + sorted(df['condition'].dropna().unique().tolist())
selected_condition = st.sidebar.selectbox('Condition', conditions)

# Type filter
vehicle_types = ['All'] + sorted(df['type'].dropna().unique().tolist())
selected_type = st.sidebar.selectbox('Vehicle Type', vehicle_types)

# Apply filters
filtered_df = df[
    (df['price'] >= price_range[0]) &
    (df['price'] <= price_range[1]) &
    (df['model_year'] >= year_range[0]) &
    (df['model_year'] <= year_range[1])
]

if selected_condition != 'All':
    filtered_df = filtered_df[filtered_df['condition'] == selected_condition]

if selected_type != 'All':
    filtered_df = filtered_df[filtered_df['type'] == selected_type]

# Display metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Listings", len(filtered_df))
with col2:
    st.metric("Average Price", f"${filtered_df['price'].mean():,.0f}")
with col3:
    st.metric("Average Mileage", f"{filtered_df['odometer'].mean():,.0f} mi")
with col4:
    st.metric("Average Year", f"{filtered_df['model_year'].mean():.0f}")

# Create two columns for charts
col1, col2 = st.columns(2)

with col1:
    # Price distribution histogram
    st.subheader('Price Distribution')
    fig_price = px.histogram(
        filtered_df,
        x='price',
        nbins=30,
        title='Distribution of Vehicle Prices',
        labels={'price': 'Price ($)', 'count': 'Number of Vehicles'}
    )
    st.plotly_chart(fig_price, use_container_width=True)

with col2:
    # Vehicle type distribution
    st.subheader('Vehicle Types')
    type_counts = filtered_df['type'].value_counts()
    fig_type = px.pie(
        values=type_counts.values,
        names=type_counts.index,
        title='Distribution by Vehicle Type'
    )
    st.plotly_chart(fig_type, use_container_width=True)

# Create two more columns for additional charts
col3, col4 = st.columns(2)

with col3:
    # Price vs Odometer scatter plot
    st.subheader('Price vs Mileage')
    fig_scatter = px.scatter(
        filtered_df,
        x='odometer',
        y='price',
        color='condition',
        title='Vehicle Price vs Mileage',
        labels={'odometer': 'Mileage (miles)', 'price': 'Price ($)', 'condition': 'Condition'},
        hover_data=['model', 'model_year']
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with col4:
    # Average price by model year
    st.subheader('Price Trends by Year')
    avg_price_by_year = filtered_df.groupby('model_year')['price'].mean().reset_index()
    fig_year = px.line(
        avg_price_by_year,
        x='model_year',
        y='price',
        title='Average Price by Model Year',
        labels={'model_year': 'Model Year', 'price': 'Average Price ($)'},
        markers=True
    )
    st.plotly_chart(fig_year, use_container_width=True)

# Condition comparison
st.subheader('Price Distribution by Condition')
fig_condition = px.box(
    filtered_df,
    x='condition',
    y='price',
    title='Price Range by Vehicle Condition',
    labels={'condition': 'Condition', 'price': 'Price ($)'}
)
st.plotly_chart(fig_condition, use_container_width=True)

# Days Listed histogram
st.subheader('Days Listed Distribution')
checkbox = st.checkbox('Show Days Listed Histogram')
if checkbox:
    fig_days = px.histogram(
        filtered_df,
        x='days_listed',
        nbins=30,
        title='Distribution of Days Listed',
        labels={'days_listed': 'Days Listed', 'count': 'Number of Vehicles'}
    )
    st.plotly_chart(fig_days, use_container_width=True)

# Data table
st.subheader('Filtered Data')
st.dataframe(
    filtered_df[['price', 'model_year', 'model', 'condition', 'odometer', 'type']].head(20),
    use_container_width=True
)

# Footer
st.markdown('---')
st.markdown('**Note:** This dashboard provides an interactive visualization of vehicle listings data in the United States.')
