from src.app import sumar

def test_sumar_enteros():
    assert sumar(2, 3) == 5

def test_sumar_negativos():
    assert sumar(-1, -1) == -2

def test_sumar_cero():
    assert sumar(0, 5) == 5
