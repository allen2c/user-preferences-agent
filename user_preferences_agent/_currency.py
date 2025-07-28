# user_preferences_agent/_currency.py
import enum
import types
import typing


class CurrencyCode(enum.StrEnum):
    AFN = "AFN"
    EUR = "EUR"
    ALL = "ALL"
    DZD = "DZD"
    USD = "USD"
    AOA = "AOA"
    XCD = "XCD"
    ARS = "ARS"
    AMD = "AMD"
    AWG = "AWG"
    AUD = "AUD"
    AZN = "AZN"
    BSD = "BSD"
    BHD = "BHD"
    BDT = "BDT"
    BBD = "BBD"
    BYN = "BYN"
    BZD = "BZD"
    BMD = "BMD"
    INR = "INR"
    BTN = "BTN"
    BOP = "BOP"
    BOB = "BOB"
    BWP = "BWP"
    NOK = "NOK"
    BRL = "BRL"
    BND = "BND"
    BGN = "BGN"
    BIF = "BIF"
    CVE = "CVE"
    KHR = "KHR"
    CAD = "CAD"
    KYD = "KYD"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    KMF = "KMF"
    CDF = "CDF"
    NZD = "NZD"
    CRC = "CRC"
    XOF = "XOF"
    CUP = "CUP"
    ANG = "ANG"
    CZK = "CZK"
    DKK = "DKK"
    DJF = "DJF"
    DOP = "DOP"
    EGP = "EGP"
    SVC = "SVC"
    ERN = "ERN"
    SZL = "SZL"
    ETB = "ETB"
    FKP = "FKP"
    FJD = "FJD"
    GMD = "GMD"
    GEL = "GEL"
    GHS = "GHS"
    GIP = "GIP"
    GTQ = "GTQ"
    GBP = "GBP"
    GNF = "GNF"
    GYD = "GYD"
    HTG = "HTG"
    HNL = "HNL"
    HKD = "HKD"
    HUF = "HUF"
    ISK = "ISK"
    IDR = "IDR"
    IRR = "IRR"
    IQD = "IQD"
    ILS = "ILS"
    JMD = "JMD"
    JPY = "JPY"
    JOD = "JOD"
    KZT = "KZT"
    KES = "KES"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KGS = "KGS"
    LAK = "LAK"
    LBP = "LBP"
    LSL = "LSL"
    ZAR = "ZAR"
    LRD = "LRD"
    LYD = "LYD"
    CHF = "CHF"
    MOP = "MOP"
    MKD = "MKD"
    MYR = "MYR"
    MVR = "MVR"
    MUR = "MUR"
    MXN = "MXN"
    MDL = "MDL"
    MNT = "MNT"
    MAD = "MAD"
    MZN = "MZN"
    MMK = "MMK"
    NAD = "NAD"
    NPR = "NPR"
    OMR = "OMR"
    PKR = "PKR"
    PHP = "PHP"
    PLN = "PLN"
    QAR = "QAR"
    RON = "RON"
    RUB = "RUB"
    RWF = "RWF"
    SHP = "SHP"
    SAR = "SAR"
    RSD = "RSD"
    SCR = "SCR"
    SLL = "SLL"
    SLE = "SLE"
    SGD = "SGD"
    SBD = "SBD"
    SOS = "SOS"
    SSP = "SSP"
    LKR = "LKR"
    SDG = "SDG"
    SRD = "SRD"
    SEK = "SEK"
    SYP = "SYP"
    TWD = "TWD"
    TJS = "TJS"
    TZS = "TZS"
    THB = "THB"
    TTD = "TTD"
    TND = "TND"
    TRY = "TRY"
    TMT = "TMT"
    UGX = "UGX"
    UAH = "UAH"
    AED = "AED"
    UZS = "UZS"
    VES = "VES"
    VED = "VED"
    YER = "YER"
    ZMW = "ZMW"
    ZWL = "ZWL"
    VND = "VND"
    NGN = "NGN"
    VUV = "VUV"
    PAB = "PAB"
    PGK = "PGK"
    PYG = "PYG"
    PEN = "PEN"
    WST = "WST"
    STN = "STN"
    MGA = "MGA"
    MWK = "MWK"
    MRU = "MRU"
    UYU = "UYU"
    TOP = "TOP"
    NIO = "NIO"
    CUC = "CUC"
    BAM = "BAM"
    XPF = "XPF"
    XAF = "XAF"
    BTC = "BTC"
    XBT = "XBT"
    LTC = "LTC"
    NMC = "NMC"
    PPC = "PPC"
    XRP = "XRP"
    DOGE = "DOGE"
    GRC = "GRC"
    XPM = "XPM"
    OMG = "OMG"
    NXT = "NXT"
    AUR = "AUR"
    BLZ = "BLZ"
    DASH = "DASH"
    NEO = "NEO"
    MZC = "MZC"
    XMR = "XMR"
    TIT = "TIT"
    XVG = "XVG"
    VTC = "VTC"
    XLM = "XLM"
    ETH = "ETH"
    ETC = "ETC"
    XNO = "XNO"
    USDT = "USDT"
    FIRO = "FIRO"
    ZEC = "ZEC"
    ZRX = "ZRX"
    AAVE = "AAVE"
    BNT = "BNT"
    BAT = "BAT"
    BCH = "BCH"
    BTG = "BTG"
    BNB = "BNB"
    ADA = "ADA"
    COTI = "COTI"
    LINK = "LINK"
    MANA = "MANA"
    ENS = "ENS"
    EOS = "EOS"
    ENJ = "ENJ"
    FET = "FET"
    NMR = "NMR"
    MLN = "MLN"
    MATIC = "MATIC"
    STORJ = "STORJ"
    LRC = "LRC"
    BCC = "BCC"
    ACH = "ACH"
    BSV = "BSV"
    CRO = "CRO"
    FTM = "FTM"
    CKB = "CKB"
    USTC = "USTC"
    LUNA = "LUNA"
    USDC = "USDC"
    UNI = "UNI"
    MDT = "MDT"
    SNX = "SNX"
    QNT = "QNT"
    PTR = "PTR"
    ALGO = "ALGO"
    ANKR = "ANKR"
    AXS = "AXS"
    BAND = "BAND"
    BICO = "BICO"
    BUSD = "BUSD"
    ATOM = "ATOM"
    CHZ = "CHZ"
    OXT = "OXT"
    TRB = "TRB"
    WBTC = "WBTC"
    _1INCH = "1INCH"
    AVAX = "AVAX"
    API3 = "API3"
    AMP = "AMP"
    BAL = "BAL"
    BOND = "BOND"
    FIDA = "FIDA"
    BCHA = "BCHA"
    CELO = "CELO"
    COMP = "COMP"
    CRV = "CRV"
    FIL = "FIL"
    CAKE = "CAKE"
    DOT = "DOT"
    MIR = "MIR"
    GRT = "GRT"
    SHIB = "SHIB"
    SOL = "SOL"
    SUSHI = "SUSHI"
    YFI = "YFI"
    FORTH = "FORTH"
    BIT = "BIT"
    CTSI = "CTSI"
    DESO = "DESO"
    SFM = "SFM"
    APE = "APE"
    APT = "APT"
    XPD = "XPD"
    XPT = "XPT"
    XAU = "XAU"
    XAG = "XAG"
    XSU = "XSU"
    XDR = "XDR"
    XUA = "XUA"
    XBA = "XBA"
    XBB = "XBB"
    XBC = "XBC"
    XBD = "XBD"
    XXX = "XXX"
    MXV = "MXV"
    USN = "USN"
    UYW = "UYW"
    CHE = "CHE"
    CHW = "CHW"
    UYI = "UYI"
    BOV = "BOV"
    CLF = "CLF"
    COU = "COU"


currency_descriptions: typing.Mapping[CurrencyCode, str] = types.MappingProxyType(
    {
        CurrencyCode.AFN: "Afghani",
        CurrencyCode.EUR: "Euro",
        CurrencyCode.ALL: "Lek",
        CurrencyCode.DZD: "Algerian Dinar",
        CurrencyCode.USD: "US Dollar",
        CurrencyCode.AOA: "Kwanza",
        CurrencyCode.XCD: "East Caribbean Dollar",
        CurrencyCode.ARS: "Argentine Peso",
        CurrencyCode.AMD: "Armenian Dram",
        CurrencyCode.AWG: "Aruban Florin",
        CurrencyCode.AUD: "Australian Dollar",
        CurrencyCode.AZN: "Azerbaijan Manat",
        CurrencyCode.BSD: "Bahamian Dollar",
        CurrencyCode.BHD: "Bahraini Dinar",
        CurrencyCode.BDT: "Taka",
        CurrencyCode.BBD: "Barbados Dollar",
        CurrencyCode.BYN: "Belarusian Ruble",
        CurrencyCode.BZD: "Belize Dollar",
        CurrencyCode.BMD: "Bermudian Dollar",
        CurrencyCode.INR: "Indian Rupee",
        CurrencyCode.BTN: "Ngultrum",
        CurrencyCode.BOP: "Bolivian peso",
        CurrencyCode.BOB: "Boliviano",
        CurrencyCode.BWP: "Pula",
        CurrencyCode.NOK: "Norwegian Krone",
        CurrencyCode.BRL: "Brazilian Real",
        CurrencyCode.BND: "Brunei Dollar",
        CurrencyCode.BGN: "Bulgarian Lev",
        CurrencyCode.BIF: "Burundi Franc",
        CurrencyCode.CVE: "Cabo Verde Escudo",
        CurrencyCode.KHR: "Riel",
        CurrencyCode.CAD: "Canadian Dollar",
        CurrencyCode.KYD: "Cayman Islands Dollar",
        CurrencyCode.CLP: "Chilean Peso",
        CurrencyCode.CNY: "Yuan Renminbi",
        CurrencyCode.COP: "Colombian Peso",
        CurrencyCode.KMF: "Comorian Franc ",
        CurrencyCode.CDF: "Congolese Franc",
        CurrencyCode.NZD: "New Zealand Dollar",
        CurrencyCode.CRC: "Costa Rican Colon",
        CurrencyCode.XOF: "CFA Franc BCEAO",
        CurrencyCode.CUP: "Cuban Peso",
        CurrencyCode.ANG: "Netherlands Antillean Guilder",
        CurrencyCode.CZK: "Czech Koruna",
        CurrencyCode.DKK: "Danish Krone",
        CurrencyCode.DJF: "Djibouti Franc",
        CurrencyCode.DOP: "Dominican Peso",
        CurrencyCode.EGP: "Egyptian Pound",
        CurrencyCode.SVC: "El Salvador Colon",
        CurrencyCode.ERN: "Nakfa",
        CurrencyCode.SZL: "Lilangeni",
        CurrencyCode.ETB: "Ethiopian Birr",
        CurrencyCode.FKP: "Falkland Islands Pound",
        CurrencyCode.FJD: "Fiji Dollar",
        CurrencyCode.GMD: "Dalasi",
        CurrencyCode.GEL: "Lari",
        CurrencyCode.GHS: "Ghana Cedi",
        CurrencyCode.GIP: "Gibraltar Pound",
        CurrencyCode.GTQ: "Quetzal",
        CurrencyCode.GBP: "Pound Sterling",
        CurrencyCode.GNF: "Guinean Franc",
        CurrencyCode.GYD: "Guyana Dollar",
        CurrencyCode.HTG: "Gourde",
        CurrencyCode.HNL: "Lempira",
        CurrencyCode.HKD: "Hong Kong Dollar",
        CurrencyCode.HUF: "Forint",
        CurrencyCode.ISK: "Iceland Krona",
        CurrencyCode.IDR: "Rupiah",
        CurrencyCode.IRR: "Iranian Rial",
        CurrencyCode.IQD: "Iraqi Dinar",
        CurrencyCode.ILS: "New Israeli Sheqel",
        CurrencyCode.JMD: "Jamaican Dollar",
        CurrencyCode.JPY: "Yen",
        CurrencyCode.JOD: "Jordanian Dinar",
        CurrencyCode.KZT: "Tenge",
        CurrencyCode.KES: "Kenyan Shilling",
        CurrencyCode.KPW: "North Korean Won",
        CurrencyCode.KRW: "Won",
        CurrencyCode.KWD: "Kuwaiti Dinar",
        CurrencyCode.KGS: "Som",
        CurrencyCode.LAK: "Lao Kip",
        CurrencyCode.LBP: "Lebanese Pound",
        CurrencyCode.LSL: "Loti",
        CurrencyCode.ZAR: "Rand",
        CurrencyCode.LRD: "Liberian Dollar",
        CurrencyCode.LYD: "Libyan Dinar",
        CurrencyCode.CHF: "Swiss Franc",
        CurrencyCode.MOP: "Pataca",
        CurrencyCode.MKD: "Denar",
        CurrencyCode.MYR: "Malaysian Ringgit",
        CurrencyCode.MVR: "Rufiyaa",
        CurrencyCode.MUR: "Mauritius Rupee",
        CurrencyCode.MXN: "Mexican Peso",
        CurrencyCode.MDL: "Moldovan Leu",
        CurrencyCode.MNT: "Tugrik",
        CurrencyCode.MAD: "Moroccan Dirham",
        CurrencyCode.MZN: "Mozambique Metical",
        CurrencyCode.MMK: "Kyat",
        CurrencyCode.NAD: "Namibia Dollar",
        CurrencyCode.NPR: "Nepalese Rupee",
        CurrencyCode.OMR: "Rial Omani",
        CurrencyCode.PKR: "Pakistan Rupee",
        CurrencyCode.PHP: "Philippine Peso",
        CurrencyCode.PLN: "Zloty",
        CurrencyCode.QAR: "Qatari Rial",
        CurrencyCode.RON: "Romanian Leu",
        CurrencyCode.RUB: "Russian Ruble",
        CurrencyCode.RWF: "Rwanda Franc",
        CurrencyCode.SHP: "Saint Helena Pound",
        CurrencyCode.SAR: "Saudi Riyal",
        CurrencyCode.RSD: "Serbian Dinar",
        CurrencyCode.SCR: "Seychelles Rupee",
        CurrencyCode.SLL: "Leone",
        CurrencyCode.SLE: "Leone",
        CurrencyCode.SGD: "Singapore Dollar",
        CurrencyCode.SBD: "Solomon Islands Dollar",
        CurrencyCode.SOS: "Somali Shilling",
        CurrencyCode.SSP: "South Sudanese Pound",
        CurrencyCode.LKR: "Sri Lanka Rupee",
        CurrencyCode.SDG: "Sudanese Pound",
        CurrencyCode.SRD: "Surinam Dollar",
        CurrencyCode.SEK: "Swedish Krona",
        CurrencyCode.SYP: "Syrian Pound",
        CurrencyCode.TWD: "New Taiwan Dollar",
        CurrencyCode.TJS: "Somoni",
        CurrencyCode.TZS: "Tanzanian Shilling",
        CurrencyCode.THB: "Baht",
        CurrencyCode.TTD: "Trinidad and Tobago Dollar",
        CurrencyCode.TND: "Tunisian Dinar",
        CurrencyCode.TRY: "Turkish Lira",
        CurrencyCode.TMT: "Turkmenistan New Manat",
        CurrencyCode.UGX: "Uganda Shilling",
        CurrencyCode.UAH: "Hryvnia",
        CurrencyCode.AED: "UAE Dirham",
        CurrencyCode.UZS: "Uzbekistan Sum",
        CurrencyCode.VES: "Bolívar Soberano",
        CurrencyCode.VED: "Bolívar Soberano",
        CurrencyCode.YER: "Yemeni Rial",
        CurrencyCode.ZMW: "Zambian Kwacha",
        CurrencyCode.ZWL: "Zimbabwe Dollar",
        CurrencyCode.VND: "Dong",
        CurrencyCode.NGN: "Naira",
        CurrencyCode.VUV: "Vatu",
        CurrencyCode.PAB: "Balboa",
        CurrencyCode.PGK: "Kina",
        CurrencyCode.PYG: "Guarani",
        CurrencyCode.PEN: "Sol",
        CurrencyCode.WST: "Tala",
        CurrencyCode.STN: "Dobra",
        CurrencyCode.MGA: "Malagasy Ariary",
        CurrencyCode.MWK: "Malawi Kwacha",
        CurrencyCode.MRU: "Ouguiya",
        CurrencyCode.UYU: "Peso Uruguayo",
        CurrencyCode.TOP: "Pa'anga",
        CurrencyCode.NIO: "Nicaraguan Córdoba",
        CurrencyCode.CUC: "Peso Convertible",
        CurrencyCode.BAM: "Convertible Mark",
        CurrencyCode.XPF: "CFP Franc",
        CurrencyCode.XAF: "CFA Franc BEAC",
        CurrencyCode.BTC: "Bitcoin",
        CurrencyCode.XBT: "Bitcoin",
        CurrencyCode.LTC: "Litecoin",
        CurrencyCode.NMC: "Namecoin",
        CurrencyCode.PPC: "Peercoin",
        CurrencyCode.XRP: "Ripple",
        CurrencyCode.DOGE: "Dogecoin",
        CurrencyCode.GRC: "Gridcoin",
        CurrencyCode.XPM: "Primecoin",
        CurrencyCode.OMG: "OMG Network",
        CurrencyCode.NXT: "Nxt",
        CurrencyCode.AUR: "Auroracoin",
        CurrencyCode.BLZ: "Bluzelle",
        CurrencyCode.DASH: "Dash",
        CurrencyCode.NEO: "Neo",
        CurrencyCode.MZC: "MazaCoin",
        CurrencyCode.XMR: "Monero",
        CurrencyCode.TIT: "Titcoin",
        CurrencyCode.XVG: "Verge",
        CurrencyCode.VTC: "Vertcoin",
        CurrencyCode.XLM: "Stellar",
        CurrencyCode.ETH: "Ethereum",
        CurrencyCode.ETC: "Ethereum Classic",
        CurrencyCode.XNO: "Nano",
        CurrencyCode.USDT: "Tether",
        CurrencyCode.FIRO: "Firo",
        CurrencyCode.ZEC: "Zcash",
        CurrencyCode.ZRX: "0x",
        CurrencyCode.AAVE: "Aave",
        CurrencyCode.BNT: "Bancor",
        CurrencyCode.BAT: "Basic Attention Token",
        CurrencyCode.BCH: "Bitcoin Cash",
        CurrencyCode.BTG: "Bitcoin Gold",
        CurrencyCode.BNB: "Binance Coin",
        CurrencyCode.ADA: "Cardano",
        CurrencyCode.COTI: "COTI",
        CurrencyCode.LINK: "Chainlink",
        CurrencyCode.MANA: "Decentraland",
        CurrencyCode.ENS: "Ethereum Name Service",
        CurrencyCode.EOS: "EOS.IO",
        CurrencyCode.ENJ: "Enjin",
        CurrencyCode.FET: "Fetch.ai",
        CurrencyCode.NMR: "Numeraire",
        CurrencyCode.MLN: "Melon",
        CurrencyCode.MATIC: "Polygon",
        CurrencyCode.STORJ: "Storj",
        CurrencyCode.LRC: "Loopring",
        CurrencyCode.BCC: "Bitconnect",
        CurrencyCode.ACH: "Alchemy Pay",
        CurrencyCode.BSV: "Bitcoin SV",
        CurrencyCode.CRO: "Cronos",
        CurrencyCode.FTM: "Fantom",
        CurrencyCode.CKB: "Nervos Network",
        CurrencyCode.USTC: "TerraClassicUSD",
        CurrencyCode.LUNA: "Terra",
        CurrencyCode.USDC: "USD Coin",
        CurrencyCode.UNI: "Uniswap",
        CurrencyCode.MDT: "Measurable Data Token",
        CurrencyCode.SNX: "Synthetix",
        CurrencyCode.QNT: "Quant",
        CurrencyCode.PTR: "Petro",
        CurrencyCode.ALGO: "Algorand",
        CurrencyCode.ANKR: "Ankr",
        CurrencyCode.AXS: "Axie Infinity",
        CurrencyCode.BAND: "Band Protocol",
        CurrencyCode.BICO: "Biconomy",
        CurrencyCode.BUSD: "Binance USD",
        CurrencyCode.ATOM: "Cosmos",
        CurrencyCode.CHZ: "Chiliz",
        CurrencyCode.OXT: "Orchid",
        CurrencyCode.TRB: "Tellor",
        CurrencyCode.WBTC: "Wrapped Bitcoin",
        CurrencyCode._1INCH: "1inch Network",
        CurrencyCode.AVAX: "Avalanche",
        CurrencyCode.API3: "API3",
        CurrencyCode.AMP: "Amp",
        CurrencyCode.BAL: "Balancer",
        CurrencyCode.BOND: "BarnBridge",
        CurrencyCode.FIDA: "Bonfida",
        CurrencyCode.BCHA: "Bitcoin Cash ABC",
        CurrencyCode.CELO: "Celo",
        CurrencyCode.COMP: "Compound",
        CurrencyCode.CRV: "Curve",
        CurrencyCode.FIL: "Filecoin",
        CurrencyCode.CAKE: "PancakeSwap",
        CurrencyCode.DOT: "Polkadot",
        CurrencyCode.MIR: "Mirror Protocol",
        CurrencyCode.GRT: "The Graph",
        CurrencyCode.SHIB: "Shiba Inu",
        CurrencyCode.SOL: "Solana",
        CurrencyCode.SUSHI: "SushiSwap",
        CurrencyCode.YFI: "Yearn.finance",
        CurrencyCode.FORTH: "Ampleforth Governance Token",
        CurrencyCode.BIT: "BitDAO",
        CurrencyCode.CTSI: "Cartesi",
        CurrencyCode.DESO: "Decentralized Social",
        CurrencyCode.SFM: "SafeMoon",
        CurrencyCode.APE: "ApeCoin",
        CurrencyCode.APT: "Aptos",
        CurrencyCode.XPD: "Palladium",
        CurrencyCode.XPT: "Platinum",
        CurrencyCode.XAU: "Gold",
        CurrencyCode.XAG: "Silver",
        CurrencyCode.XSU: "Sucre",
        CurrencyCode.XDR: "SDR (Special Drawing Right)",
        CurrencyCode.XUA: "ADB Unit of Account",
        CurrencyCode.XBA: "Bond Markets Unit European Composite Unit (EURCO)",
        CurrencyCode.XBB: "Bond Markets Unit European Monetary Unit (E.M.U.-6)",
        CurrencyCode.XBC: "Bond Markets Unit European Unit of Account 9 (E.U.A.-9)",
        CurrencyCode.XBD: "Bond Markets Unit European Unit of Account 17 (E.U.A.-17)",
        CurrencyCode.XXX: "The codes assigned for transactions where no currency is involved",  # noqa: E501
        CurrencyCode.MXV: "Mexican Unidad de Inversion (UDI)",
        CurrencyCode.USN: "US Dollar (Next day)",
        CurrencyCode.UYW: "Unidad Previsional",
        CurrencyCode.CHE: "WIR Euro",
        CurrencyCode.CHW: "WIR Franc",
        CurrencyCode.UYI: "Uruguay Peso en Unidades Indexadas (UI)",
        CurrencyCode.BOV: "MVDOL",
        CurrencyCode.CLF: "Unidad de Fomento",
        CurrencyCode.COU: "Unidad de Valor Real",
    }
)
