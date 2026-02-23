using System;
using System.Net.Http;
using System.Net.Http.Json;
using System.Threading.Tasks;

public class PaymentService
{
    // It's a best practice to reuse HttpClient instances in .NET
    private static readonly HttpClient _httpClient = new HttpClient();

    public async Task ProcessPaymentAsync()
    {
        // 1. Define the payload (using an anonymous object, similar to JS)
        var args = new { amount = 3.99m, currency = "GBP" };

        try
        {
            // 2. Make the POST request
            // PostAsJsonAsync automatically serializes 'args' to JSON 
            // and sets the 'Content-Type: application/json' header.
            HttpResponseMessage response = await _httpClient.PostAsJsonAsync("https://example.com/payments", args);

            // 3. Handle the response
            if (response.IsSuccessStatusCode)
            {
                // Read and deserialize the JSON response
                // You would typically replace 'object' with a specific C# class/record matching your response data
                var responseData = await response.Content.ReadFromJsonAsync<object>();
                Success(responseData);
            }
            else
            {
                // Server error (maps to JS: response.ok == false)
                Failure((int)response.StatusCode); 
            }
        }
        catch (HttpRequestException error)
        {
            // Network error (maps to JS: .catch())
            Failure(error.Message); 
        }
    }

    // Mock methods to represent the success/failure callbacks from your JS snippet
    private void Success(object data) => Console.WriteLine("Success!");
    private void Failure(object error) => Console.WriteLine($"Failure: {error}");
}
