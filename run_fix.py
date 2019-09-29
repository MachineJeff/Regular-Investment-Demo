from plot import plot
def run_fix(args, data):

    print("Use {} strategy...".format(args.strategy))

    col = data[data['time'].isin(["2019-9-27"])]
    col = col["index"].tolist()
    print(col)
'''
    start = args.start_time
    end = args.start_time + args.duration
    if(end >= len(data)):
        end = len(data) - 1
    duration = end - start + 1

    print("   Start investment in {}".format(start))
    print("     End investment in {}".format(end))
    print("Investment duration is {} trading days".format(duration))
    print("Investment interval is {} trading days".format(args.interval))
    print(" Captial investment is {}".format(args.money))
    print()

    shares = []
    pays = []
    values = []

    i = 1
    while(start <= end):
        share = args.money / data[start]

        shares.append(share)
        pays.append(args.money * i)				
        values.append(sum(shares) * data[start])

        start += args.interval
        i += 1

    return_value = values[-1]
    pay_value = pays[-1]

    yields = []
    for i in range(len(pays)):
        yield_rate = (values[i] - pays[i]) / pays[i] * 100.0
        yields.append(yield_rate)

    max_yield = max(yields)
    plot(yields, path='pics/2.png')
    print("       Your captial money is {:.2f}".format(pay_value))
    print("Your ruturn of investment is {:.2f}".format(return_value))
    print("               Your yield is {:.2f}%".format(yields[-1]))
    print("           Your max yield is {:.2f}%".format(max_yield))
'''