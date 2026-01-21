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
    raw_code = str(row['종목코드']).split('.')[0]
    code = raw_code.zfill(6)

    try:
        price_df = fdr.DataReader(code, '2026-01-01')

        if not price_df.empty:
            current_price = price_df['Close'].iloc[-1]
            real_volume = price_df['Volume'].iloc[-1]

            stock_pool.append({
                'Stock_Name': row['종목명'],
                'Stock_Code': code,
                'Volatility': round(random.uniform(0.01, 0.05), 4),
                'Trading_Volume': real_volume,
                'Current_Price': float(current_price)
            })
        else:

        time.sleep(0.3)

    except Exception as e:
        continue

data_list = []
if len(stock_pool) >= 10:
    for u_idx in range(1, 101):
        user_id = f'user_{u_idx:03d}'
        user_stocks = random.sample(stock_pool, 10)
        for stock in user_stocks:
            p_price = stock['Current_Price'] * random.uniform(0.9, 1.1)
            qty = random.randint(1, 100)
            data_list.append({
                'Customer_ID': user_id,
                'Stock_Name': stock['Stock_Name'],
                'Volatility': stock['Volatility'],
                'Trading_Volume': stock['Trading_Volume'],
                'Purchase_Price': round(p_price, -1),
                'Quantity': float(qty),
                'Current_Price': stock['Current_Price']
            })

    df_final = pd.DataFrame(data_list)
    output_path = 'kospi_1000_rows.csv'
    df_final.to_csv(output_path, index=False, encoding='utf-8-sig')
