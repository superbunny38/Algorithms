var card = new Card 
{
    CardNumber = "1234 5678 8765 4321",
    ExpiryDate = "10/2024",
    CVC = "123"
};

var result = paymentsService.ProcessPayment(card, 3.99m, Currency.GBP);

if (result.IsSuccess) 
{
    FulfilOrder();
}