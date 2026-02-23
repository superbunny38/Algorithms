using System;
using System.Threading.Tasks;

// 1. The Request Message
public class PaymentRequest
{
    // C# 11 'required' keyword mirrors the proto 'required' rule
    public required Card CardDetails { get; set; }
    
    // int64 in proto maps to long in C#
    public required long Amount { get; set; }
    
    public required Currency Currency { get; set; }
}

// Nested Message from the IDL
public class Card
{
    public required string CardNumber { get; set; }
    
    // 'optional' in proto maps perfectly to Nullable types (?) in C#
    public int? ExpiryMonth { get; set; }
    public int? ExpiryYear { get; set; }
    public int? Cvc { get; set; }
}

// Enum from the IDL
public enum Currency
{
    Gbp = 1,
    Usd = 2
}

// 2. The Response Message
public class PaymentStatus
{
    public required bool Success { get; set; }
    
    // Optional string becomes a nullable reference type
    public string? ErrorMessage { get; set; }
}

// 3. The Service
// gRPC services in C# map to interfaces with asynchronous (Task-returning) methods
public interface IPaymentService
{
    Task<PaymentStatus> ProcessPaymentAsync(PaymentRequest request);
}
