# 40. Stock Price Analyzer

def sma(prices, window):
    if len(prices) < window: return []
    out=[]
    for i in range(window-1, len(prices)):
        out.append(sum(prices[i-window+1:i+1])/window)
    return out

def ema(prices, window):
    if not prices: return []
    k = 2/(window+1)
    ema_vals=[prices[0]]
    for p in prices[1:]:
        ema_vals.append(p*k + ema_vals[-1]*(1-k))
    return ema_vals

def trend(prices):
    return "up" if prices[-1] > prices[0] else "down" if prices[-1] < prices[0] else "flat"

if __name__ == "__main__":
    data = [10,11,12,11,13,14,15]
    print("SMA(3):", sma(data,3))
    print("EMA(3):", ema(data,3))
    print("Trend:", trend(data))
