import pandas as pd
def load_data(file_path1, file_path2):
    try:
        df=pd.read_csv(file_path1)
        df2=pd.read_csv(file_path2)
        return df, df2
    except Exception as e:
        print(f"Error loading data:{e}")
        return None
    
if __name__=="__main__":
    file_path= "dataset_1.csv"
    file_path2="dataset_2.csv"
    df1,df2= load_data(file_path,file_path2)
    print(df1,df2)

