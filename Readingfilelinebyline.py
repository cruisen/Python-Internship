import pandas as pd
import os 

# Global Variables
path_to_data_files = "./Data"
data = None

def get_data_files(dir_path):
 return os.listdir(dir_path)

def get_df_from_file(file_path):
 return pd.read_table(my_file, delim_whitespace= True)

def get_one_datapoint_from_df(df):
  df = df[df1.A5016 == 0.0]
  df = df.iloc[:1]
  return df.drop(columns=["A5334", "A5335", "A5016"], axis = 1)
  
def combine_datapoints_from_dfs(file_list):
 for file in file_list:
   my_file = pathx + "/" + file
   df = get_df_from_file(my_file)
   data_point = get_one_datapoint_from_df(df)
   data = pd.concat([data, data_point], ignore_index=True)
 return data

def shape_df(df):
 df = df.astype({"Time": float, "P3114": float})
 df['Time'] = pd.to_datetime(df['Time'], unit='D', origin='julian')
 return df

def plot(df):
 plot = df.plot.line(x = "Time", y = "P3114") 
 plot.set_ylabel("P3114: XMM-Newton solar array power [A]")              
 figure = plot.get_figure()
 figure.savefig("XMM_solar_array_power_over_mission_lifetime.png")

def main():
 data_files = get_data_files(path_to_data_files)
 data = combine_datapoints_from_dfs(data_files)
 data = shape_df(data)
 plot(data)

if __name__ == '__main__':
 main()





  



          
