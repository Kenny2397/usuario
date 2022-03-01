from User import User

# Kenny = User("Kenny")
Julián = User("Julián")
Paul = User("Paul")
Rebeca = User("Rebeca")

Julián.hacer_deposito(100).hacer_deposito(100).hacer_deposito(100).hacer_retiro(100).mostrar_balance_usuario()


Paul.hacer_deposito(100).hacer_deposito(100).hacer_retiro(100).hacer_retiro(100).mostrar_balance_usuario()


Rebeca.hacer_deposito(100).hacer_retiro(100).hacer_retiro(100).hacer_retiro(100).mostrar_balance_usuario()


Julián.transf_dinero(Rebeca,100).mostrar_balance_usuario()

Rebeca.mostrar_balance_usuario()

