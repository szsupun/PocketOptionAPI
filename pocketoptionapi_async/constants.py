"""
Constants and configuration for the PocketOption API
"""

from typing import Dict, List
import random

# Asset mappings with their corresponding IDs
ASSETS: Dict[str, int] = {
    # Major Forex Pairs
    "EURUSD": 1,
    "GBPUSD": 56,
    "USDJPY": 63,
    "USDCHF": 62,
    "USDCAD": 61,
    "AUDUSD": 40,
    "NZDUSD": 60,
    "EURJPY": 48,
    "EURGBP": 47,
    "EURCHF": 46,
    "EURCAD": 45,
    "EURAUD": 44,
    "GBPJPY": 54,
    "GBPCHF": 53,
    "GBPCAD": 52,
    "GBPAUD": 51,
    "AUDJPY": 38,
    "AUDCHF": 37,
    "AUDCAD": 36,
    "CADJPY": 42,
    "CADCHF": 41,
    "CHFJPY": 43,
    
    # OTC Forex Pairs
    "EURUSD_otc": 66,
    "GBPUSD_otc": 86,
    "USDJPY_otc": 93,
    "USDCHF_otc": 92,
    "USDCAD_otc": 91,
    "AUDUSD_otc": 71,
    "NZDUSD_otc": 90,
    "EURJPY_otc": 79,
    "EURGBP_otc": 78,
    "EURCHF_otc": 77,
    "EURCAD_otc": 76,
    "EURAUD_otc": 75,
    "GBPJPY_otc": 84,
    "GBPCHF_otc": 83,
    "GBPCAD_otc": 82,
    "GBPAUD_otc": 81,
    "AUDJPY_otc": 69,
    "AUDCHF_otc": 68,
    "AUDCAD_otc": 67,
    "AUDNZD_otc": 70,
    "CADJPY_otc": 73,
    "CADCHF_otc": 72,
    "CHFJPY_otc": 74,
    "EURNZD_otc": 80,
    "NZDJPY_otc": 89,
    
    # Additional Currency Pairs
    "EURHUF_otc": 460,
    "EURRUB_otc": 200,
    "EURTRY_otc": 468,
    "USDRUB_otc": 199,
    "USDINR_otc": 202,
    "USDMXN_otc": 509,
    "USDPHP_otc": 511,
    "USDPKR_otc": 517,
    "USDSGD_otc": 526,
    "USDTHB_otc": 521,
    "USDVND_otc": 519,
    "USDARS_otc": 506,
    "USDBDT_otc": 500,
    "USDBRL_otc": 502,
    "USDCLP_otc": 525,
    "USDCNH_otc": 467,
    "USDCOP_otc": 515,
    "USDDZD_otc": 508,
    "USDEGP_otc": 513,
    "USDIDR_otc": 504,
    "CHFNOK_otc": 457,
    "AEDCNY_otc": 538,
    "BHDCNY_otc": 536,
    "JODCNY_otc": 546,
    "OMRCNY_otc": 544,
    "QARCNY_otc": 542,
    "SARCNY_otc": 540,
    "IRRUSD_otc": 548,
    "KESUSD_otc": 554,
    "LBPUSD_otc": 530,
    "MADUSD_otc": 534,
    "NGNUSD_otc": 552,
    "SYPUSD_otc": 550,
    "TNDUSD_otc": 532,
    "UAHUSD_otc": 558,
    "YERUSD_otc": 528,
    "ZARUSD_otc": 556,
    
    # Commodities
    "XAUUSD": 2,  # Gold
    "XAUUSD_otc": 169,
    "XAGUSD": 65,  # Silver
    "XAGUSD_otc": 167,
    "XAGEUR": 103,  # Silver/EUR
    "XAUEUR": 102,  # Gold/EUR
    "UKBrent": 50,  # Brent Oil
    "UKBrent_otc": 164,
    "USCrude": 64,  # WTI Crude Oil
    "USCrude_otc": 165,
    "XNGUSD": 311,  # Natural Gas
    "XNGUSD_otc": 399,
    "XPTUSD": 312,  # Platinum
    "XPTUSD_otc": 400,
    "XPDUSD": 313,  # Palladium
    "XPDUSD_otc": 401,
    
    # Cryptocurrencies
    "BTCUSD": 197,
    "BTCUSD_otc": 484,
    "ETHUSD": 272,
    "ETHUSD_otc": 487,
    "DASH_USD": 209,
    "BTCGBP": 453,
    "BTCJPY": 454,
    "BCHEUR": 450,
    "BCHGBP": 451,
    "BCHJPY": 452,
    "DOTUSD": 458,
    "DOTUSD_otc": 486,
    "LNKUSD": 464,  # Chainlink
    "LINK_otc": 478,
    "LTCUSD_otc": 488,  # Litecoin
    "ADA-USD_otc": 473,  # Cardano
    "AVAX_otc": 481,  # Avalanche
    "BNB-USD_otc": 470,  # BNB
    "BITB_otc": 494,  # Bitcoin ETF
    "DOGE_otc": 485,  # Dogecoin
    "MATIC_otc": 491,  # Polygon
    "SOL-USD_otc": 472,  # Solana
    "TON-USD_otc": 480,  # Toncoin
    "TRX-USD_otc": 476,  # TRON
    
    # Stock Indices
    "SP500": 321,
    "SP500_otc": 408,
    "NASUSD": 323,  # US100
    "NASUSD_otc": 410,
    "DJI30": 322,
    "DJI30_otc": 409,
    "JPN225": 317,
    "JPN225_otc": 405,
    "D30EUR": 318,
    "D30EUR_otc": 406,
    "E50EUR": 319,
    "E50EUR_otc": 407,
    "F40EUR": 316,
    "F40EUR_otc": 404,
    "E35EUR": 314,
    "E35EUR_otc": 402,
    "100GBP": 315,
    "100GBP_otc": 403,
    "AUS200": 305,
    "AUS200_otc": 306,
    "CAC40": 455,
    "AEX25": 449,
    "SMI20": 466,
    "H33HKD": 463,  # Hong Kong 33
    
    # US Stocks
    "#AAPL": 5,
    "#AAPL_otc": 170,
    "#MSFT": 24,
    "#MSFT_otc": 176,
    "#TSLA": 186,
    "#TSLA_otc": 196,
    "#FB": 177,
    "#FB_otc": 187,
    "#AMZN_otc": 412,
    "#NFLX": 182,
    "#NFLX_otc": 429,
    "#INTC": 180,
    "#INTC_otc": 190,
    "#BA": 8,
    "#BA_otc": 292,
    "#JPM": 20,
    "#JNJ": 144,
    "#JNJ_otc": 296,
    "#PFE": 147,
    "#PFE_otc": 297,
    "#XOM": 153,
    "#XOM_otc": 426,
    "#AXP": 140,
    "#AXP_otc": 291,
    "#MCD": 23,
    "#MCD_otc": 175,
    "#CSCO": 154,
    "#CSCO_otc": 427,
    "#VISA_otc": 416,
    "#CITI": 326,
    "#CITI_otc": 413,
    "#FDX_otc": 414,
    "#BABA": 183,
    "#BABA_otc": 428,
    
    # Additional Tech Stocks
    "AMD_otc": 568,  # Advanced Micro Devices
    "COIN_otc": 570,  # Coinbase Global
    "GME_otc": 566,  # GameStop Corp
    "MARA_otc": 572,  # Marathon Digital Holdings
    "PLTR_otc": 562,  # Palantir Technologies
    "VIX_otc": 560,  # VIX
}



# WebSocket regions with their URLs
class Regions:
    """WebSocket region endpoints"""

    _REGIONS = {
        "EUROPA": "wss://api-eu.po.market/socket.io/?EIO=4&transport=websocket",
        "SEYCHELLES": "wss://api-sc.po.market/socket.io/?EIO=4&transport=websocket",
        "HONGKONG": "wss://api-hk.po.market/socket.io/?EIO=4&transport=websocket",
        "SERVER1": "wss://api-spb.po.market/socket.io/?EIO=4&transport=websocket",
        "FRANCE2": "wss://api-fr2.po.market/socket.io/?EIO=4&transport=websocket",
        "UNITED_STATES4": "wss://api-us4.po.market/socket.io/?EIO=4&transport=websocket",
        "UNITED_STATES3": "wss://api-us3.po.market/socket.io/?EIO=4&transport=websocket",
        "UNITED_STATES2": "wss://api-us2.po.market/socket.io/?EIO=4&transport=websocket",
        "DEMO": "wss://demo-api-eu.po.market/socket.io/?EIO=4&transport=websocket",
        "DEMO_2": "wss://try-demo-eu.po.market/socket.io/?EIO=4&transport=websocket",
        "UNITED_STATES": "wss://api-us-north.po.market/socket.io/?EIO=4&transport=websocket",
        "RUSSIA": "wss://api-msk.po.market/socket.io/?EIO=4&transport=websocket",
        "SERVER2": "wss://api-l.po.market/socket.io/?EIO=4&transport=websocket",
        "INDIA": "wss://api-in.po.market/socket.io/?EIO=4&transport=websocket",
        "FRANCE": "wss://api-fr.po.market/socket.io/?EIO=4&transport=websocket",
        "FINLAND": "wss://api-fin.po.market/socket.io/?EIO=4&transport=websocket",
        "SERVER3": "wss://api-c.po.market/socket.io/?EIO=4&transport=websocket",
        "ASIA": "wss://api-asia.po.market/socket.io/?EIO=4&transport=websocket",
        "SERVER4": "wss://api-us-south.po.market/socket.io/?EIO=4&transport=websocket",
    }

    @classmethod
    def get_all(cls, randomize: bool = True) -> List[str]:
        """Get all region URLs"""
        urls = list(cls._REGIONS.values())
        if randomize:
            random.shuffle(urls)
        return urls

    @classmethod
    def get_all_regions(cls) -> Dict[str, str]:
        """Get all regions as a dictionary"""
        return cls._REGIONS.copy()

    from typing import Optional

    @classmethod
    def get_region(cls, region_name: str) -> Optional[str]:
        """Get specific region URL"""
        return cls._REGIONS.get(region_name.upper())

    @classmethod
    def get_demo_regions(cls) -> List[str]:
        """Get demo region URLs"""
        return [url for name, url in cls._REGIONS.items() if "DEMO" in name]


# Global constants
REGIONS = Regions()

# Timeframes (in seconds)
TIMEFRAMES = {
    "1m": 60,
    "5m": 300,
    "15m": 900,
    "30m": 1800,
    "1h": 3600,
    "4h": 14400,
    "1d": 86400,
    "1w": 604800,
}

# Connection settings
CONNECTION_SETTINGS = {
    "ping_interval": 20,  # seconds
    "ping_timeout": 10,  # seconds
    "close_timeout": 10,  # seconds
    "max_reconnect_attempts": 5,
    "reconnect_delay": 5,  # seconds
    "message_timeout": 30,  # seconds
}

# API Limits
API_LIMITS = {
    "min_order_amount": 1.0,
    "max_order_amount": 50000.0,
    "min_duration": 5,  # seconds
    "max_duration": 43200,  # 12 hours in seconds
    "max_concurrent_orders": 10,
    "rate_limit": 100,  # requests per minute
}

# Default headers
DEFAULT_HEADERS = {
    "Origin": "https://pocketoption.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
}
