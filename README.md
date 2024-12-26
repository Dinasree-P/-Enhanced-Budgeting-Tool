# Enhanced Budgeting Tool with Predictive Analytics
Overview
The Enhanced Budgeting Tool is a powerful web-based application designed to help users manage their finances effectively. This tool allows users to track expenses, upload historical data, forecast future spending, and set budget limits with predictive analytics. By leveraging models like Exponential Smoothing, the tool offers insights into monthly spending patterns and provides personalized budget alerts.

Features
User Registration & Login: Secure account creation and login functionality.
Expense Tracking: Users can view live mock transactions and upload their own historical expense data.
Expense Forecasting: Predict future expenses using the Holt-Winters Exponential Smoothing model with seasonal adjustments.
Customizable Forecasting: Users can adjust the forecast settings such as the number of months to predict, seasonal adjustment type, and date range.
Budget Alerts: Set monthly budget limits and receive alerts when spending exceeds the set limit.
Data Visualization: Interactive charts and tables display historical expenses and forecasted spending.

Tech Stack
Python: Backend development
Streamlit: Web framework for building the user interface
Pandas: Data handling and manipulation
Statsmodels: Time series forecasting (Exponential Smoothing)
Matplotlib & Seaborn: Data visualization
JSON: Storing user data for login and registration
Prerequisites
To run this project, ensure you have the following installed:

Python 3.6+
Required Python libraries:
streamlit
pandas
numpy
statsmodels
matplotlib
seaborn

You can install the required libraries using pip:
pip install streamlit pandas numpy statsmodels matplotlib seaborn

How to Run the Project
Clone the repository:
git clone https://github.com/your-username/budgeting-tool.git
cd budgeting-tool

Run the application:
streamlit run app.py
Navigate to the application: Once the application starts, open your browser and go to http://localhost:8501 to access the tool.

Usage
1. User Registration & Login:
When you first open the application, you will be prompted to either register a new account or log in if you already have one.
On successful login, you'll gain access to the main budgeting tool.
2. Expense Data Upload:
You can upload your own historical expense data in CSV format. The data should have at least two years of monthly expenses for accurate forecasting.
Example CSV structure:
csv
Copy code
Date,Description,Category,Amount
2022-01-01,Groceries,Food,200
2022-02-01,Rent,Housing,1200
...
3. Forecasting:
After uploading your historical data, you can forecast your future expenses.
You can customize the forecasting settings, such as:
Number of months to forecast
Seasonal adjustment type (add or mul)
Custom date range for the forecast
4. Budget Alerts:
Set a monthly budget limit.
The tool will display a status indicating if your predicted expenses are within budget or over budget.
5. Data Visualization:
The tool generates interactive line charts to visualize the forecasted expenses over time.
Example Data
The tool requires a dataset containing at least 24 months of expenses for accurate seasonal forecasting. Here's a sample dataset for reference:

csv formate

Date,Description,Category,Amount
2022-01-01,Groceries,Food,200
2022-01-15,Rent,Housing,1200
2022-02-01,Electricity Bill,Utilities,150

Troubleshooting

Error: "Cannot compute initial seasonals using heuristic method":
Ensure your dataset contains at least 24 months of historical data before attempting seasonal forecasting. The Exponential Smoothing model requires two full seasonal cycles to detect seasonality.
User login not working:
Ensure that the username and password are entered correctly. If the issue persists, check the users.json file for stored accounts.
