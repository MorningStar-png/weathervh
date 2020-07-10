# Podast searcher

> Search any podcast by name

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Code Coverage][coverage-image]][coverage-url]
[![Code Quality][quality-image]][quality-url]


## Installation

```sh
pip install podsearch
```

## Usage

```python
>>> import podsearch
>>> podcasts = podsearch.search("python")
>>> podcasts[0].name
'Talk Python To Me'
>>> podcasts[0].author
'Michael Kennedy (@mkennedy)'
>>> podcasts[0].url
'https://podcasts.apple.com/us/podcast/id979020229'
```

## Development setup

```sh
$ pip install black pytest
$ pytest -ra
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Make sure to add or update tests as appropriate.

Use [Black](https://black.readthedocs.io/en/stable/) for code formatting and [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/) for commit messages.

## [Changelog](CHANGELOG.md)

## License

[MIT](https://choosealicense.com/licenses/mit/)

<!-- Markdown link & img dfn's -->

[pypi-image]: https://img.shields.io/pypi/v/forecastvh?style=flat-square
[pypi-url]: https://pypi.org/project/forecastvh/
[build-image]: https://img.shields.io/travis/MorningStar-png/forecastvh-py?style=flat-square
[build-url]: https://travis-ci.org/MorningStar-png/forecastvh-py
[coverage-image]: https://img.shields.io/coveralls/github/MorningStar-png/forecastvh-py?style=flat-square
[coverage-url]: https://coveralls.io/github/MorningStar-png/forecastvh-py
[quality-image]: https://img.shields.io/codeclimate/maintainability/MorningStar-png/forecastvh-py?style=flat-square
[quality-url]: https://codeclimate.com/github/MorningStar-png/forecastvh-py