from src.validation.holidays import validate_country, validate_language


def test_validate_country():
    assert validate_country('DE') == True
    assert validate_country('RU') == True
    assert validate_country('FR') == True
    assert validate_country('US') == True
    assert validate_country('QWE') == False
    assert validate_country('') == False
    assert validate_country('IDDQD') == False


def test_validate_language():
    assert validate_language('DE', 'de') == True
    assert validate_language('DE', 'en') == False
    assert validate_language('DE', 'en_US') == True
    assert validate_language('RU', 'ru') == True
    assert validate_language('RU', 'de') == False
    assert validate_language('RU', 'en_US') == True
    assert validate_language('FR', 'de') == False
    assert validate_language('FR', 'en_US') == True
    assert validate_language('FR', 'ru') == False
    assert validate_language('QWE', 'en_US') == False
    assert validate_language('', 'en_US') == False
    assert validate_language('IDDQD', 'en_US') == False