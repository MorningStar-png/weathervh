# Weather finder

> Find any weather forecast

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Coverage Status](https://coveralls.io/repos/github/MorningStar-png/forecastvh-py/badge.svg?branch=master)](https://coveralls.io/github/MorningStar-png/forecastvh-py?branch=master)
[![Code Quality][quality-image]][quality-url]
![GitHub](https://img.shields.io/github/license/MorningStar-png/forecastvh-py)

`podsearch` finds podcasts via [OpenWeather API](https://openweathermap.org/current).'

Search parameters:

- *city* - search string (name, author etc)
- *country* - ISO alpha-2 country code (de, fr etc), default: en
- *units* - units format (imperial or metric), default: metric

Returned attributes for each podcast (https://openweathermap.org/current#current_JSON):

- *id* - City ID (e.g., `420006353`)
- *country* - Country code (`GB`)
- *city* - City name (`London`)
- *temp* - Temperature (Default: Metric). (`19.8`)
- *feels_like* - Temperature. This temperature parameter accounts for the human perception of weather. (`19`)
- *pressure* - Atmospheric pressure on the ground level, hPa (`1023`)
- *humidity* - Humidity, % (`100`)
- *wind_speed* - Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour. (`1.5`)
- *cloudiness* - Cloudiness, % (`80`)
- *status* - Status code, 200 or 404 (`200`)

## Installation

```sh
pip3 install forecastvh
```

## Usage

```python
>>> import forecastvh
>>> forecast = forecastvh.get_weather("London")
>>> forecast.country
'GB'
>>> forecast.temp
'18.01'
>>> forecast.cloudiness
'97	'
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Make sure to add or update tests as appropriate.

Use [Black](https://black.readthedocs.io/en/stable/) for code formatting and [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/) for commit messages.

## License

[MIT](https://choosealicense.com/licenses/mit/)

<!-- Markdown link & img dfn's -->

[pypi-image]: https://img.shields.io/pypi/v/forecastvh
[pypi-url]: https://pypi.org/project/forecastvh/
[build-image]: https://img.shields.io/travis/MorningStar-png/forecastvh-py
[build-url]: https://travis-ci.org/MorningStar-png/forecastvh-py
[coverage-image]: https://img.shields.io/coveralls/github/MorningStar-png/forecastvh-py
[coverage-url]: https://coveralls.io/github/MorningStar-png/forecastvh-py
[quality-image]: https://img.shields.io/codeclimate/maintainability/MorningStar-png/forecastvh-py
[quality-url]: https://codeclimate.com/github/MorningStar-png/forecastvh-py