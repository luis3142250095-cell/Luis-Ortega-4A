
class SuscripcionExpiradaError(Exception):
    pass


class PuntosInsuficientesError(Exception):
    pass


class PerfilMovil:
    def __init__(self, username: str, gemas: int = 50):
        if gemas < 0:
            raise ValueError("Las gemas no pueden ser negativas.")

        self.username = username
        self.gemas = gemas
        self.racha_dias = 1
        self.notificaciones_activas = True

    def ganar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")

        self.gemas += cantidad
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")

        if cantidad > self.gemas:
            raise PuntosInsuficientesError(
                f"El usuario {self.username} no tiene gemas suficientes."
            )

        self.gemas -= cantidad
        return self.gemas


class PerfilPro(PerfilMovil):
    def __init__(
        self, username: str,
        meses_suscripcion: int,
        gemas: int = 50
    ):
        super().__init__(username, gemas)

        if meses_suscripcion <= 0:
            raise ValueError(
                "La suscripcion debe ser mayor a 0 meses."
            )

        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def descargar_contenido_offline(self) -> str: # <-- se llaman anotaciones de tipo (type hints) para indicar que el método devuelve un string
        if self.meses_suscripcion <= 0:
            self.es_pro = False
            raise SuscripcionExpiradaError(
                "La suscripcion ha expirado."
            )

        return "Contenido descargado correctamente."
