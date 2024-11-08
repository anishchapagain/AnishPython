import pandas as pd
from scipy.stats import zscore

"""
Anamolies:
High Response Time
HTTP Status Codes
Unusual Behaviour - IP
"""

# Sample log data
data = {
    'date': ['2024-11-01', '2024-11-01', '2024-11-02', '2024-11-03', '2024-11-04', 
             '2024-11-04', '2024-11-05', '2024-11-06', '2024-11-07', '2024-11-07', 
             '2024-11-08', '2024-11-08', '2024-11-08', '2024-11-08'],
    'user_id': [102, 153, 204, 102, 301, 102, 153, 102, 153, 153, 153, 301, 204, 204],
    'endpoint': ['/accountInfo', '/balanceEnquiry', '/fundsTransfer', '/passwordUpdate', 
                 '/fundsTransfer', '/utilitiesPayment', '/fundsTransfer', '/accountInfo', 
                 '/balanceEnquiry', '/fundsTransfer', '/accountInfo', '/passwordUpdate', 
                 '/balanceEnquiry', '/fundsTransfer'],
    'method': ['GET', 'GET', 'POST', 'POST', 'POST', 'POST', 'POST', 'GET', 'GET', 'POST', 'GET', 'POST', 'GET', 'POST'],
    'status_code': [200, 200, 200, 200, 403, 200, 200, 200, 200, 200, 200, 403, 500, 500],
    'response_time': [0.34, 0.20, 1.05, 1.02, 0.55, 1.20, 0.90, 0.15, 0.25, 0.87, 0.33, 0.98, 1.75, 2.00],
    'ip_address': ['192.168.1.10', '203.12.34.56', '192.168.1.20', '198.51.100.34', 
                   '192.168.1.25', '192.168.1.10', '203.12.34.56', '192.168.1.10', 
                   '203.12.34.56', '203.12.34.56', '203.12.34.56', '198.51.100.20', 
                   '192.168.1.20', '192.168.1.20'],
    'device_type': ['mobile', 'desktop', 'mobile', 'desktop', 'mobile', 'mobile', 
                    'desktop', 'mobile', 'desktop', 'desktop', 'desktop', 'mobile', 
                    'tablet', 'tablet']
}

# Load data into DataFrame
df = pd.DataFrame(data)

# 1. Detect high response times (using Z-score for outliers)
df['response_time_zscore'] = zscore(df['response_time'])
high_response_time_anomalies = df[df['response_time_zscore'] > 2]  # Flag if z-score > 2

# 2. Detect unusual status codes (e.g., 4xx and 5xx errors)
unusual_status_codes = df[df['status_code'].isin([403, 500])]

# 3. Identify anomalies in user behavior (e.g., same user accessing from different IPs)
user_ip_counts = df.groupby(['user_id', 'ip_address']).size().unstack(fill_value=0)
multiple_ip_access_anomalies = user_ip_counts[user_ip_counts.gt(1).any(axis=1)]

# Display results
print("High Response Time Anomalies:")
print(high_response_time_anomalies[['date', 'user_id', 'endpoint', 'response_time']])

print("\nUnusual Status Codes:")
print(unusual_status_codes[['date', 'user_id', 'endpoint', 'status_code']])

print("\nMultiple IP Access for Single User:")
print(multiple_ip_access_anomalies)
