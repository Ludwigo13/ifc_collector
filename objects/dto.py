class IFC_DTO:
    def __init__(self, previous_close, open_price, bid, ask, days_range, week_52_range, volume, avg_volume,
                 market_cap, beta, pe_ratio, eps, earnings_date, forward_dividend_yield, ex_dividend_date,
                 target_est):
        self.previous_close = previous_close
        self.open_price = open_price
        self.bid = bid
        self.ask = ask
        self.days_range = days_range
        self.week_52_range = week_52_range
        self.volume = volume
        self.avg_volume = avg_volume
        self.market_cap = market_cap
        self.beta = beta
        self.pe_ratio = pe_ratio
        self.eps = eps
        self.earnings_date = earnings_date
        self.forward_dividend_yield = forward_dividend_yield
        self.ex_dividend_date = ex_dividend_date
        self.target_est = target_est