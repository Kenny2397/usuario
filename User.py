class User:
    balance=8000
    def __init__(self, nombre):
        self.nombre=nombre
        return self
        
        
    def hacer_deposito(self, monto):
        self.balance+=monto
        return self
    
    def hacer_retiro(self, monto):
        self.balance-=monto
        return self    
    
    def mostrar_balance_usuario(self):
        print(f"Usuario:{self.nombre}, Balance:{self.balance}")
        return self
        
    def transf_dinero(self, otro_usuario,monto):
        self.balance-=monto
        otro_usuario.balance +=monto
        return self
