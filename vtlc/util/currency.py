CURRENCY_SYMBOL_MAP = {
    '$': 'USD',
    '£': 'GBP',
    '¥': 'JPY',
    '₩': 'KRW',
    '₪': 'ILS',
    '€': 'USD',
    '₱': 'PHP',
    '₹': 'INR',
    'A$': 'AUD',
    'AED': 'AED',
    'ARS': 'ARS',
    'BAM': 'BAM',
    'BGN': 'BGN',
    'BOB': 'BOB',
    'BYN': 'BYN',
    'CA$': 'CAD',
    'CHF': 'CHF',
    'CLP': 'CLP',
    'COP': 'COP',
    'CRC': 'CRC',
    'CZK': 'CZK',
    'DKK': 'DKK',
    'DOP': 'DOP',
    'EGP': 'EGP',
    'GTQ': 'GTQ',
    'HK$': 'HKD',
    'HNL': 'HNL',
    'HRK': 'HRK',
    'HUF': 'HUF',
    'INR': 'INR',
    'ISK': 'ISK',
    'MAD': 'MAD',
    'MKD': 'MKD',
    'MX$': 'MXN',
    'MYR': 'MYR',
    'NIO': 'NIO',
    'NOK': 'NOK',
    'NT$': 'TWD',
    'NZ$': 'NZD',
    'PEN': 'USD',
    'PHP': 'PHP',
    'PLN': 'PLN',
    'PYG': 'PYG',
    'QAR': 'QAR',
    'R$': 'BRL',
    'RON': 'RON',
    'RSD': 'RSD',
    'RUB': 'RUB',
    'SAR': "SAR",
    'SEK': 'SEK',
    'SGD': 'SGD',
    'TRY': 'TRY',
    'UYU': 'UYU',
    'ZAR': 'ZAR',
}

APPROX_RATES_TO_JPY = {
    'AED': 0.03,
    'ARS': 1.26136,
    'AUD': 0.0127098151,
    'BAM': 0.01460468,
    'BGN': 0.01460468,
    'BOB': 0.06285513,
    'BRL': 0.0501367157,
    'BYN': 236.83,
    'CAD': 0.0123889679,
    'CHF': 0.00819122,
    'CLP': 6.61,
    'COP': 33.63,
    'CRC': 5.72,
    'CZK': 0.208,
    'DKK': 0.05552193,
    'DOP': 0.53,
    'EGP': 0.14253745,
    'GBP': 0.0071446183,
    'GTQ': 0.07,
    'HKD': 0.0748624941,
    'HNL': 0.22,
    'HRK': 0.05606733,
    'HUF': 2.872293346,
    'ILS': 0.02960463,
    'INR': 0.69,
    'INY': 0.703,
    'ISK': 1.16,
    'JPY': 1,
    'KRW': 10.5964122017,
    'MAD': 0.08028517,
    'MKD': 0.47,
    'MXN': 0.1921416153,
    'MYR': 0.03763261,
    'NIO': 0.32,
    'NOK': 0.0835411728,
    'NZD': 0.03559,
    'PHP': 0.43425395,
    'PLN': 0.03559,
    'PYG': 60.2,
    'QAR': 0.03313398,
    'RON': 0.0367296,
    'RSD': 0.91,
    'RUB': 0.66471683,
    'SAR': 0.03413528,
    'SEK': 0.07562924,
    'SGD': 0.01204301,
    'TRY': 0.07782101,
    'TWD': 3.9583,
    'USD': 0.00910274,
    'UYU': 0.41,
    'ZAR': 0.13,
}


def convertToJPY(amount: float, currency: str):
    return amount / APPROX_RATES_TO_JPY[CURRENCY_SYMBOL_MAP[currency]]


def applyJPY(col):
    return convertToJPY(col['amount'], col['currency'])