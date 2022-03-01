class User:
    balance=8000
    def __init__(self, nombre):
        self.nombre=nombre
        
        
    def hacer_deposito(self, monto):
        self.balance+=monto
    
    def hacer_retiro(self, monto):
        self.balance-=monto    
    
    def mostrar_balance_usuario(self):
        print(f"Usuario:{self.nombre}, Balance:{self.balance}")
        
    def transf_dinero(self, otro_usuario,monto):
        self.balance-=monto
        otro_usuario.balance +=monto
