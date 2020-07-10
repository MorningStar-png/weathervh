import pytest
import forecastvh

def test_search():
    w = forecastvh.get_weather('Minsk', lang='ru')
    assert w.city == 'Минск'