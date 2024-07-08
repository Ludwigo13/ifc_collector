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

    @classmethod
    def map_to_dto(cls, data):
        data_dict = {item[0]: item[1] for item in data}

        return cls(
            previous_close=data_dict.get('Previous Close'),
            open_price=data_dict.get('Open'),
            bid=data_dict.get('Bid'),
            ask=data_dict.get('Ask'),
            days_range=data_dict.get("Day's Range"),
            week_52_range=data_dict.get('52 Week Range'),
            volume=data_dict.get('Volume'),
            avg_volume=data_dict.get('Avg. Volume'),
            market_cap=data_dict.get('Market Cap'),
            beta=data_dict.get('Beta (5Y Monthly)'),
            pe_ratio=data_dict.get('PE Ratio (TTM)'),
            eps=data_dict.get('EPS (TTM)'),
            earnings_date=data_dict.get('Earnings Date'),
            forward_dividend_yield=data_dict.get('Forward Dividend & Yield'),
            ex_dividend_date=data_dict.get('Ex-Dividend Date'),
            target_est=data_dict.get('1y Target Est')
        )
