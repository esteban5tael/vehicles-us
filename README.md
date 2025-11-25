# 🚗 US Vehicle Sales Dashboard

An interactive web application for analyzing vehicle sales data in the United States. Built with Streamlit, this dashboard provides insights into vehicle listings including price trends, mileage analysis, and distribution by various attributes.

## Features

- **Interactive Filtering**: Filter vehicles by price, model year, condition, and type
- **Data Visualizations**:
  - Price distribution histogram
  - Vehicle type breakdown
  - Price vs. mileage scatter plot
  - Price trends by model year
  - Condition-based price comparison
  - Days listed distribution
- **Real-time Metrics**: View key statistics like total listings, average price, and average mileage
- **Responsive Design**: Works seamlessly on different screen sizes

## Installation

1. Clone this repository:
```bash
git clone https://github.com/esteban5tael/vehicles-us.git
cd vehicles-us
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Data

The application uses a CSV file (`vehicles_us.csv`) containing vehicle listing data with the following attributes:
- Price
- Model year
- Model name
- Condition
- Number of cylinders
- Fuel type
- Odometer reading
- Transmission type
- Vehicle type
- Paint color
- 4WD status
- Date posted
- Days listed

## Technologies Used

- **Streamlit**: For building the interactive web application
- **Pandas**: For data manipulation and analysis
- **Plotly**: For creating interactive visualizations

## Project Structure

```
vehicles-us/
├── app.py              # Main Streamlit application
├── vehicles_us.csv     # Vehicle data
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Contributing

Feel free to open issues or submit pull requests to improve this dashboard.

## License

This project is open source and available under the MIT License.
