class CashMachine:

    def __init__(self):
        self._bills = []

    def put_money(self, bills):
        self._bills.extend(bills)

    @property
    def is_avaliable(self):
        if self._bills:
            return True
        return False

    def withdraw_money(self, amount):
        to_withdraw = []
        for bill in sorted(self._bills, reverse=True):
            if sum(to_withdraw) + bill <= amount:
                to_withdraw.append(bill)
        if sum(to_withdraw) == amount:
            for bill in to_withdraw:
                self._bills.remove(bill)
        else:
            return []
        return to_withdraw

class TestCashMachine:

    def test_initialization(self):
        cash_machine = CashMachine()
        assert cash_machine

    def test_is_avaliable(self):
        cash_machine = CashMachine()
        assert not cash_machine.is_avaliable

    def test_cash_machine_is_avaliable_after_put_money(self):
        cash_machine = CashMachine()
        assert not cash_machine.is_avaliable
        cash_machine.put_money([100, 100])
        assert cash_machine.is_avaliable

    def test_withdraw_money(self):
        cash_machine = CashMachine()
        cash_machine.put_money([100, 100])
        assert cash_machine.withdraw_money(200) == [100, 100]
        assert cash_machine.is_avaliable is False

        cash_machine.put_money([100, 100, 100])
        assert cash_machine.withdraw_money(200) == [100, 100]
        assert cash_machine.is_avaliable is True

        cash_machine = CashMachine()
        cash_machine.put_money([50, 50, 50])
        assert cash_machine.withdraw_money(200) == []
        assert cash_machine.is_avaliable is True

        cash_machine = CashMachine()
        cash_machine.put_money([100, 50, 100])
        assert cash_machine.withdraw_money(200) == [100, 100]
        assert cash_machine.is_avaliable is True