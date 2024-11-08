import pandas as pd
from scipy.stats import zscore
"""
Anamolies:
Geolocation
Device Change
TransactionAmount
Endpoints update
"""
# Sample log data
data = {
    'date': ['2024-11-01', '2024-11-01', '2024-11-01', '2024-11-02', '2024-11-02',
             '2024-11-03', '2024-11-04', '2024-11-05', '2024-11-05', '2024-11-06',
             '2024-11-06', '2024-11-07', '2024-11-08', '2024-11-08', '2024-11-08'],
    'user_id': [102, 102, 204, 204, 153, 153, 204, 301, 301, 102, 102, 204, 153, 102, 153],
    'endpoint': ['/accountInfo', '/fundsTransfer', '/balanceEnquiry', '/accountInfo', 
                 '/utilitiesPayment', '/fundsTransfer', '/balanceEnquiry', '/fundsTransfer',
                 '/accountInfo', '/fundsTransfer', '/passwordUpdate', '/utilitiesPayment', 
                 '/fundsTransfer', '/balanceEnquiry', '/accountInfo'],
    'method': ['GET', 'POST', 'GET', 'GET', 'POST', 'POST', 'GET', 'POST', 'GET', 'POST', 'POST', 'POST', 'POST', 'GET', 'GET'],
    'status_code': [200, 200, 200, 200, 200, 200, 200, 403, 200, 200, 200, 200, 200, 200, 200],
    'response_time': [0.34, 1.15, 0.25, 0.18, 1.20, 1.55, 0.22, 0.78, 0.24, 1.45, 1.10, 0.75, 2.20, 0.28, 0.20],
    'ip_address': ['192.168.1.10', '192.168.1.10', '10.1.1.56', '10.1.1.56', 
                   '172.18.1.24', '172.18.1.24', '10.1.1.56', '203.44.3.77', 
                   '203.44.3.77', '10.0.0.1', '10.0.0.1', '10.1.1.56', '203.55.4.89', 
                   '192.168.1.10', '203.55.4.89'],
    'device_type': ['mobile', 'mobile', 'desktop', 'desktop', 'mobile', 'desktop', 
                    'desktop', 'mobile', 'desktop', 'mobile', 'mobile', 'tablet', 
                    'mobile', 'desktop', 'mobile'],
    'location': ['US', 'US', 'CA', 'CA', 'US', 'US', 'CA', 'IN', 'IN', 'MX', 'MX', 'CA', 'JP', 'US', 'JP'],
    'transaction_amount': [0, 150, 0, 0, 80, 2500, 0, 120, 0, 200, 0, 95, 1500, 0, 0]
}

# Load data into DataFrame
df = pd.DataFrame(data)

# 1. Detect Unusual Geolocation Change
geo_changes = df.groupby('user_id')['location'].nunique()
geo_anomalies = geo_changes[geo_changes > 1]  # Users with more than one location

# 2. Detect Suspicious Device Change
device_changes = df.groupby('user_id')['device_type'].nunique()
device_anomalies = device_changes[device_changes > 1]  # Users with more than one device type

# 3. Detect Abnormal Transaction Amounts (using Z-score to find high-value transactions)
df['transaction_amount_zscore'] = zscore(df['transaction_amount'])
high_value_transactions = df[df['transaction_amount_zscore'] > 2]  # Flag if z-score > 2

# 4. Detect Frequent Requests on Endpoints
endpoint_usage = df.groupby(['user_id', 'endpoint']).size()
frequent_usage_anomalies = endpoint_usage[endpoint_usage > 2]  # Flag if usage > 2 times per endpoint

# Display results
print("Geolocation Change Anomalies:")
print(geo_anomalies)

print("\nDevice Type Change Anomalies:")
print(device_anomalies)

print(f"TODO {"-"*10}")
