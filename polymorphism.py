from abc import ABC, abstractmethod

class PaymentType(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        ...
    
class CreditCard(PaymentType):
    def process_payment(self, amount: float) -> None:
        print(f"Processing credit card payment of ${amount}")
        
class Cash(PaymentType):
    def process_payment(self, amount: float) -> None:
        print(f"Processing  Cash payment of ${amount}")
        
        
class IOU(PaymentType):
    def process_payment(self, amount: float) -> None:
        print(f"Processing IOU payment of ${amount}")
        
        
def checkout(payment_type:PaymentType, amount:float) -> None:
    payment_type.process_payment(amount)
    
credit_card: CreditCard = CreditCard()
cash:Cash = Cash()
iou:IOU = IOU()

checkout(credit_card, 100)
checkout(cash, 600)
checkout(iou, 300)