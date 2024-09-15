import pandas as pd

def save_csv(data, file_name, headers):
    if not data:
        print(f"No data in {file_name}.csv")
        return
    df = pd.DataFrame(data)
    df.to_csv(f'{file_name}.csv', index=False, header=headers)

def read_csv(file_name, headers):
    return pd.read_csv(f'{file_name}.csv', header=0, names=headers)