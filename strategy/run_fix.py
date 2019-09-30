from pandas.core.frame import DataFrame
import os
from tools import next_day, annual_rate, plot

def run_fix(args, data, title):

    start = args.start_time
    col = data[data['time'].isin([start])]
    col = col["index"].tolist()
    if(len(col) == 0):
        print("Your start time is not a trading day. So I postpone it to the next trading day.\n")

    while(len(col) == 0):
        start = next_day(start)
        col = data[data['time'].isin([start])]

    
    start_idd = col.index.tolist()[0]
    end_idd = start_idd + 244 * args.duration
    if(end_idd > 1220):
        end_idd = 1220

    start_time = str(data["time"][data.index[start_idd]])[:-9]
    end_time = str(data["time"][data.index[end_idd]])[:-9]

    shares = []
    pays = []
    values = []
    yield_time = []

    i = 1
    while(start_idd <= end_idd):
        share = args.money / data["index"][data.index[start_idd]]
        yield_time.append(data["time"][data.index[start_idd]])
        shares.append(share)
        pays.append(args.money * i)				
        values.append(sum(shares) * data["index"][data.index[start_idd]])

        start_idd += args.interval
        i += 1

    return_value = values[-1]
    pay_value = pays[-1]

    yields = []
    for i in range(len(pays)):
        yield_rate = (values[i] - pays[i]) / pays[i] * 100.0
        yields.append(yield_rate)

    max_yield = max(yields)

    data = {"time":yield_time,
            "index":yields}
    data = DataFrame(data)

    path = os.path.join(os.getcwd(),'pics')
    name = "Yield-of-" + title.replace(' ', '-') + '.png' 
    plot(data, path = os.path.join(path, name), ylabel = "yield", title = "Yield of " + title, freq = "30D")

    print("Your strategy of investment is    {}\n".format(args.strategy))

    print("           Start investment at    {}".format(start_time))
    print("             End investment at    {}".format(end_time))
    print("        Investment duration is    {} year(s)".format(args.duration))
    print("        Investment interval is    {} trading day(s)".format(args.interval))
    print("         Captial investment is    {:.2f} RMB\n".format(args.money))

    print("         Your captial money is    {:.2f} RMB".format(pay_value))
    print("  Your ruturn of investment is    {:.2f} RMB\n".format(return_value))
    print("           Your final yield is    {:.2f}%".format(yields[-1]))
    print("          Your annual yield is    {:.2f}%\n".format(annual_rate((1+yields[-1]/100), args.duration) * 100))

    print("       Your final max yield is    {:.2f}%".format(max_yield))
    print("      Your annual max yield is    {:.2f}%".format(annual_rate((1+max_yield/100), args.duration) * 100))    

    print(" Your yield curve has saved in    {}".format(os.path.join(path, name)))
