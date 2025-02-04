import logging
from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from datetime import datetime
import holidays
from validation.holidays import validate_country, validate_language

app = FastAPI(title="Holidays API")
logger = logging.getLogger('uvicorn.error')

@app.get("/")
async def hello_world():
    return {"message": "Welcome to the Holidays API!"}


@app.get("/holidays")
async def country_holidays(
        year: Optional[int] = Query(default=datetime.now().year, ge=1),
        country: str = Query(default="DE", pattern=r'^[A-Za-z]{2}$'),
        state: Optional[str] = Query(default=''),
        lang: str = Query(default="en_US", pattern=r'^[A-Za-z_]{2,5}$'),
):
    logger.debug(f"GET /holidays year={year}, country={country}, state={state}, lang={lang}")

    # custom validation of country and language
    if (validate_country(country) is not True):
        raise HTTPException(status_code=400, detail=f"Country code '{country}' is not supported.")

    if (validate_language(country, lang) is not True):
        raise HTTPException(status_code=400, detail=f"Language code '{lang}' is not supported by country '{country}'.")

    try:
        h_list = holidays.country_holidays(country.upper(), years=year, subdiv=state.upper(), language=lang)

        holidays_list = [{"date": str(holiday), "name": name} for holiday, name in h_list.items()]

        return holidays_list
    except KeyError:
        raise HTTPException(status_code=400, detail=f"Country code '{country}' is not supported.")
    except Exception as e:
        logger.error(f"Unable to handle request: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/debug")
async def debug():
    countries = holidays.list_supported_countries()
    list = holidays.list_localized_countries()

    return {"countries": countries, "localizations": list}
