import numpy as np
import pandas as pd
def test_1():
    df = pd.DataFrame({'cust': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'date': np.arange(0,60,10)}, columns=['cust', 'date'])
    customer_list = df.groupby('cust').sum().index
    
    for customer in customer_list:
        df_c = df[df['cust']== customer].copy()
        df_c['date_diff'] = df_c['date'].diff()
        df.loc[df['cust']=='A', 'date_diff'] = df_c['date_diff']
    print(df)
    pass