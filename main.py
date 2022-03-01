from User import User

# Kenny = User("Kenny")
Julián = User("Julián")
Paul = User("Paul")
Rebeca = User("Rebeca")

Julián.hacer_deposito(100)
Julián.hacer_deposito(100)
Julián.hacer_deposito(100)
Julián.hacer_retiro(100)
Julián.mostrar_balance_usuario()

Paul.hacer_deposito(100)
Paul.hacer_deposito(100)
Paul.hacer_retiro(100)
Paul.hacer_retiro(100)
Paul.mostrar_balance_usuario()

Rebeca.hacer_deposito(100)
Rebeca.hacer_retiro(100)
Rebeca.hacer_retiro(100)
Rebeca.hacer_retiro(100)
Rebeca.mostrar_balance_usuario()

Julián.transf_dinero(Rebeca,100)
Julián.mostrar_balance_usuario()
Rebeca.mostrar_balance_usuario()

