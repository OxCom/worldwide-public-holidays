import logging
from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from datetime import datetime
import holidays

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
        lang: str = Query(default="EN", pattern=r'^[A-Za-z]{2}$'),
):
    logger.debug(f"GET /holidays year={year}, country={country}, state={state}, lang={lang}")

    try:
        h_list = holidays.country_holidays(country.upper(), years=year, subdiv=state.upper(), language=lang.upper())

        holidays_list = [{"date": str(holiday), "name": name} for holiday, name in h_list.items()]

        return holidays_list
    except KeyError:
        raise HTTPException(status_code=400, detail=f"Country code '{country}' is not supported.")
    except Exception as e:
        logger.error(f"Unable to handle request: {e}")
        raise HTTPException(status_code=500, detail=str(e))
