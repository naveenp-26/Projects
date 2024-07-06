#importing built-in speedtest package for calculating the speed of the internet 
import speedtest
from colorama import Fore,Back,Style
#importing built-in datetime package for calculating the time
from datetime import datetime
#importing built-in system package for getting the system configuration
import sys
#importing built-in time package for getting current time
import time
try:
    #assinging the function Speedtest() from speedtest package to st and also checking that you are connected to internet connection
    st=speedtest.Speedtest(secure=False)
    print("Well...Internet Connection has been Detected...!")
    print("Retreiving Informations from the server..............",)
    print(Fore.RED+'This may take a while.....')
    start = time.time()
    #storing download internet speed in downspeed variable
    downspeed=st.download()
    #storing upload internet speed in upspeed variable
    upspeed=st.upload()
    #creating empty list named as servernames
    servernames =[]
    #getting the server details using get_servers() function form speedtest package
    st.get_servers(servernames)
    #printing internet provider
    print("\nNetwork provider     : ",st.config['client']['isp'])
    #printing IP address of the network
    print("Server/IP Address    : ",st.config['client']['ip'])
    #printing the latitude of the server using key value 'lat' in server dictionary
    print("Server Latitude      : ",st.results.server['lat'])
    #printing the longitude of the server using key value 'lon' in server dictionary
    print("Server Longitude     : ",st.results.server['lon'])
    #printing the name of the server using key value 'name' in server dictionary
    print("Server city          : ",st.results.server['name'])
    #printing the country of the server using key value 'country' in server dictionary
    print("Server country       : ",st.results.server['country'])
    #printing the host of the server using key value 'host' in server dictionary
    print("Server host          : ",st.results.server['host'])
    #printing the download speed of the server in terms of Mbps
    print("Download Speed       : ",round((downspeed/(1024*1024)),3),"Mbps")
    #printing the upload speed of the server in terms of Mbps
    print("Upload Speed         : ",round((upspeed/(1024*1024)),3),"Mbps")
    #printing the ping of the server in terms of ms 
    print("Server Ping/Latency  : ",st.results.ping,"ms")
    end = time.time()
    #printing its appropriate time while getting information from server
    print("Generated time       : ",datetime.now().strftime("%H:%M:%S"))
    print("Time taken to show   : ",int(end-start),"seconds")
except:
    #this block of code will be thrown when the internet connection is false
    print("Please make sure that your internet connection is available...!")
finally:
    print("\t  Thank you...")

