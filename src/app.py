import holidays
from datetime import datetime
from flask import request
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return {"message": "Welcome to the Holidays API!"}


@app.route('/holidays', methods=['GET'])
def country_holidays():
    current_year = datetime.now().year
    country = request.args.get('country', 'DE')
    year = request.args.get('year', str(current_year))

    # Validate country (2-character ISO code)
    if not country.isalpha() or len(country) != 2:
        return jsonify({"error": "Invalid country code. It must be a 2-character alphabetic ISO code."}), 400

    # Validate year (numeric)
    if not year.isdigit():
        return jsonify({"error": "Invalid year. It must be a numeric value."}), 400

    try:
        year = int(year)
        hList = holidays.country_holidays(country, years=year)
        jList = [{"date": str(holiday), "name": name} for holiday, name in hList.items()]

        return jsonify({"holidays": jList})
    except KeyError:
        return jsonify({"error": f"Country code '{country}' is not supported."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
