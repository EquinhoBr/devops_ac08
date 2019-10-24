import pytest
from com.ac08.calculadora import cvHora


def test_convertHora():
    assert cvHora.converteHora(20, 50) == '08:50 PM', ("O resultado tem que ser 08:50 PM")
    assert cvHora.converteHora(60, 70) == None, ("O resultado tem que ser None")
    assert cvHora.converteHora(11, 30) == '11:30 AM', ("O resultado tem que ser 11:30 AM")
    assert cvHora.converteHora(0, 0) == '12:00 AM', ("O resultado tem que ser 12:00 AM")
