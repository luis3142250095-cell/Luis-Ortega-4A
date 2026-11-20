import pytest


import pytest

from app_movil import (
    PerfilMovil,
    PerfilPro,
    SuscripcionExpiradaError,
    PuntosInsuficientesError
)


@pytest.fixture
def perfil():
    return PerfilMovil("Christian")


def test_atributos_iniciales(perfil):
    assert perfil.username == "Christian"
    assert perfil.gemas == 50
    assert perfil.racha_dias == 1
    assert perfil.notificaciones_activas is True


def test_gemas_negativas():
    with pytest.raises(ValueError):
        PerfilMovil("Christian", -10)


def test_ganar_gemas(perfil):
    resultado = perfil.ganar_gemas(20)

    assert resultado == 70
    assert perfil.gemas == 70


@pytest.mark.parametrize("cantidad", [0, -5, -10])
def test_ganar_gemas_invalidas(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.ganar_gemas(cantidad)


def test_gastar_gemas(perfil):
    resultado = perfil.gastar_gemas(20)

    assert resultado == 30
    assert perfil.gemas == 30


@pytest.mark.parametrize("cantidad", [0, -1, -20])
def test_gastar_gemas_invalidas(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.gastar_gemas(cantidad)


def test_puntos_insuficientes(perfil):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(100)


def test_herencia_perfil_pro():
    usuario = PerfilPro("Christian", 3)

    assert isinstance(usuario, PerfilMovil)
    assert isinstance(usuario, PerfilPro)
    assert usuario.es_pro is True


def test_suscripcion_invalida():
    with pytest.raises(ValueError):
        PerfilPro("Christian", 0)


def test_descarga_correcta():
    usuario = PerfilPro("Christian", 3)

    resultado = usuario.descargar_contenido_offline()

    assert resultado == "Contenido descargado correctamente."


def test_suscripcion_expirada():
    usuario = PerfilPro("Christian", 1)

    usuario.meses_suscripcion = 0

    with pytest.raises(SuscripcionExpiradaError):
        usuario.descargar_contenido_offline()

    assert usuario.es_pro is False
