PRECIO_TICKET=70
PRIMARIO="Primario"
SECUNDARIO="Secundario"
DESACTIVADO="desactivado"
ACTIVADO="activado"

class UsuarioDesactivadoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass

class NoHaySaldoException(Exception):
    pass

class Sube():
    def __init__(self,saldo=0,grupo_beneficiario=None,estado=ACTIVADO):
        self.saldo=saldo
        self.grupo_beneficiario=grupo_beneficiario
        self.estado=estado 
    def obtener_precio_ticket(self):
        if self.grupo_beneficiario==None:
            return PRECIO_TICKET
        if self.grupo_beneficiario==PRIMARIO:
            return 35
        if self.grupo_beneficiario==SECUNDARIO:
            return 42


    def pagar_pasaje(self):
        if self.estado==DESACTIVADO:
            raise UsuarioDesactivadoException()
        if self.estado==ACTIVADO:
            if self.grupo_beneficiario==None:
                if self.saldo>PRECIO_TICKET:
                   self.saldo-=PRECIO_TICKET
                else: raise NoHaySaldoException()
            if self.grupo_beneficiario==PRIMARIO:
                if self.saldo>=self.obtener_precio_ticket():
                    self.saldo-=self.obtener_precio_ticket()
                elif self.saldo<self.obtener_precio_ticket():
                   raise NoHaySaldoException()
            if self.grupo_beneficiario==SECUNDARIO:
                if self.saldo>=self.obtener_precio_ticket():
                    self.saldo-=self.obtener_precio_ticket()
                elif self.saldo<self.obtener_precio_ticket():
                   raise NoHaySaldoException()
    
    def cambiar_estado(self,estado):
        if estado==DESACTIVADO:
            estado=ACTIVADO
            self.estado=estado
        elif estado==ACTIVADO:
            estado=DESACTIVADO
            self.estado=estado
        else: raise EstadoNoExistenteException()