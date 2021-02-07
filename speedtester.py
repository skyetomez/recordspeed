import speedtest 
import time as tm
import pandas as pd

#functions 
def measure_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    down = st.download()
    up = st.upload()
    datime = str(tm.asctime())

    print(f"the time is {datime}")
    print(f"this is cycle: {x+1}")
    print(f"The download speed is {down} and the upload speed is {up}")


    return [down, up, datime]


# Data frames

df = []

# DO this every 30 minutes for 3 hours

one_minute = 60 # sec / min
one_hour = 60 # min / hour
num = 20 # every num minutes
num_min = one_minute * num #number of secs in num mins   

hours = 1 #for how many hours. 

cycles = (hours * one_hour * one_minute) // num_min

cycles = int(cycles)

# build df

for x in range(cycles):
    
   hold = measure_speed()

   df.append(hold)

   tm.sleep(num_min) #counts in seconds


# save print to excel
df = pd.DataFrame(df, columns = ['dls', 'uls','time'])

df.to_excel('myDataFrame.xlsx',sheet_name= 'internetmonitor')








