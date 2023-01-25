import pandas as pd
import os 

#with open("XMM_Data_year_1999.txt") as file:
 # print(file.readlines())

pathx = "./Data"
files = os.listdir(pathx)
#print(files)

data = None


for file in files:
  #print(file)
  my_file = pathx + "/" + file 

  df1 = pd.read_table(my_file, delim_whitespace= True)
  #print(df1.info())
  df2 = df1[df1.A5016 == 0.0]
  #print(df2.info())
  df3 = df2.iloc[:1]
  #print(df3)
  df4 = df3.drop(columns=["A5334", "A5335", "A5016"], axis = 1)
  #print(df4)
  data = pd.concat([data, df4], ignore_index=True)

data = data.astype({"Time": float, "P3114": float})
data['Time'] = pd.to_datetime(data['Time'], unit='D', origin='julian')
#print(data.info())
#print(data)
plot = data.plot.line(x = "Time", y = "P3114") 
plot.set_ylabel("P3114: XMM-Newton solar array power [A]")              
figure = plot.get_figure()
figure.savefig("XMM_solar_array_power_over_mission_lifetime.png")


          