import pandas as pd

excel_data_df = pd.read_excel('sample_data.xlsx', sheet_name='data1', skiprows=7, usecols='X')
df = pd.DataFrame(excel_data_df, columns= ["MFD"])
# print("df", df)

df_mfd_query_1 = df.query("`MFD` > 9.0 and `MFD` <= 9.2")
# df_mfd_query_2 = df.query("`MFD` > 9.0 and `MFD` <= 9.4")

query_1_percentage = str(round(len(df_mfd_query_1) / len(df) * 100, 2))
# query_2_percentage = str(round(len(df_mfd_query_2) / len(df) * 100, 2))

print('[9.0 ~ 9.2]:', query_1_percentage)
# print('[9.0 ~ 9.4]:', query_2_percentage)