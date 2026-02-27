import pandas as pd

def load_data(path):
    
    # Step 1: Read CSV
    df = pd.read_csv(path)
    
    if 'date' in df.columns:
        df['date']=pd.to_datetime(df['date'])
        df = df.sort_values('date')
    
    # Step 4: Reset index
    df = df.reset_index(drop=True)
    df['time'] = df.index
    return df