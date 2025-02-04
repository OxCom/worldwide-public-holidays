import holidays

countries = holidays.list_supported_countries()
loca = holidays.list_localized_countries()


def validate_country(code: str):
    return code.upper() in countries

def validate_language(code: str, lang: str):
    return code.upper() in loca and lang in loca[code.upper()]