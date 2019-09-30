import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import pandas as pd
import matplotlib.dates as mdate
import datetime

def next_day(day):
    day = day.split("-")

    year = int(day[0])
    month = int(day[1])
    da = int(day[2])

    if(da < 31):
        return str(year) + '-' + str(month) + '-' + str(da + 1)
    if(month < 12):
        return str(year) + '-' + str(month + 1) + '-' + str(1)
    if(year < 2019):
        return str(year + 1) + '-' + str(1) + '-' + str(1)

def annual_rate(rate, duration):

    return np.power(rate, 1/duration) - 1


def plot(data, path, 
        figsize = (28,12),
        xlabel = "Time",
        xlabel_size = 20,
        ylabel = "Index",
        ylabel_size = 20, 
        title = "SSE Composite Index", 
        title_size = 24,
        freq = '60D',
        format = "index"):
    
    fig = plt.figure(figsize = figsize)
    plt.style.use('ggplot')
    ax = fig.add_subplot(1,1,1)
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y/%m/%d'))

    start_time = data["time"][data.index[0]]
    end_time = data["time"][data.index[-1]]

    plt.xticks(pd.date_range(start_time, end_time, freq = freq), rotation = 40)
    data.time = pd.to_datetime(data.time)
    
    plt.plot(data["time"], data["index"])

    plt.title(title, fontsize = title_size, fontstyle = 'italic')
    plt.ylabel(ylabel, fontsize = ylabel_size)
    plt.grid(color="k", linestyle=":")
    plt.savefig(path)