import FinanceDataReader as fdr
import pandas as pd
import random
import time

path = 'KOSPI_100.csv'
try:
    df_raw = pd.read_csv(path, encoding='cp949')
except:
    df_raw = pd.read_csv(path, encoding='utf-8')

df_raw['시가총액'] = df_raw['시가총액'].astype(str).str.replace(',', '').astype(float)
df_100 = df_raw.sort_values(by='시가총액', ascending=False).head(100).copy()

stock_pool = []

for i, row in df_100.iterrows():
    code = str(row['종목코드']).split('.')[0].zfill(6)
    try:
        price_df = fdr.DataReader(code, '2026-01-01')
        if not price_df.empty:
            stock_pool.append({
                'Stock_Name': row['종목명'],
                'Stock_Code': code,
                'Trading_Volume': price_df['Volume'].iloc[-1], 
                'Current_Price': float(price_df['Close'].iloc[-1]) 
            })
        time.sleep(0.3)
    except:
        continue

data_list = []
if len(stock_pool) >= 10:
    for u_idx in range(1, 101):
        user_id = f'user_{u_idx:03d}'
        user_stocks = random.sample(stock_pool, 10)
        for stock in user_stocks:
            p_price = stock['Current_Price'] * random.uniform(0.9, 1.1)
            data_list.append({
                'Customer_ID': user_id,
                'Stock_Name': stock['Stock_Name'],
                'Trading_Volume': stock['Trading_Volume'],
                'Purchase_Price': round(p_price, -1),
                'Quantity': float(random.randint(1, 100)),
                'Current_Price': stock['Current_Price']
            })

    df_final = pd.DataFrame(data_list)
    df_final.to_csv('kospi_1000_rows.csv', index=False, encoding='utf-8-sig')
