class BankAccount:
    MAX_WITHDRAWALS = 3

    def __init__(self):
        """Inicializa uma nova instância da classe BankAccount."""
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.withdrawals_today = 0

    def deposit(self, amount):
        """Realiza um depósito na conta bancária.

        Args:
            amount (float): O valor a ser depositado.

        Raises:
            ValueError: O valor precisa ser maior do que zero.
        """
        if amount > 0:
            self.balance += amount
            self.deposits.append(amount)
        else:
            raise ValueError("O valor precisa ser maior do que zero.")

    def withdraw(self, amount):
        """Realiza um saque na conta bancária.

        Args:
            amount (float): O valor a ser sacado.

        Raises:
            ValueError: O valor precisa ser maior do que zero.
            ValueError: O valor precisa ser menor ou igual a R$ 500,00 e o saldo em conta deve ser suficiente.
            ValueError: Limite diário de saques atingido.
        """
        if amount > 0:
            if self.withdrawals_today < self.MAX_WITHDRAWALS:
                if amount <= 500 and amount <= self.balance:
                    self.balance -= amount
                    self.withdrawals.append(amount)
                    self.withdrawals_today += 1
                else:
                    raise ValueError("O valor precisa ser menor ou igual a R$ 500,00 e o saldo em conta deve ser suficiente.")
            else:
                raise ValueError("Limite diário de saques atingido.")
        else:
            raise ValueError("O valor precisa ser maior do que zero.")

    def get_statement(self):
        """Exibe o extrato da conta bancária."""
        print("Extrato:")
        for deposit in self.deposits:
            print(f"Depósito: R$ {deposit:.2f}")
        for withdrawal in self.withdrawals:
            print(f"Saque: R$ {withdrawal:.2f}")
        if not self.deposits and not self.withdrawals:
            print("Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {self.balance:.2f}")

account = BankAccount()

# Teste de depósito
account.deposit(100)
account.deposit(250)
account.deposit(50)
account.get_statement()

# Teste de saque
account.withdraw(50)
account.withdraw(200)
account.get_statement()

# Teste de limite diário de saques
try:
    account.withdraw(100)
    account.withdraw(200)
    account.withdraw(100)
except ValueError as error:
    print(f"Erro: {str(error)}")
account.get_statement()

# Teste de saldo insuficiente
try:
    account.withdraw(1000)
except ValueError as error:
    print(f"Erro: {str(error)}")
account.get_statement()

# Teste de valor inválido
try:
    account.deposit(-50)
except ValueError as error:
    print(f"Erro: {str(error)}")
try:
    account.withdraw(0)
except ValueError as error:
    print(f"Erro: {str(error)}")
account.get_statement()

