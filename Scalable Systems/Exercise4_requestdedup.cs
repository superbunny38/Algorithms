/*

Reliable network links allow messages to be reordered. Give pseudocode for an algorithm

that strengthens the properties of a reliable point-to-point link such that messages are received in the order

they were sent (this is called a FIFO link), assuming an asynchronous crash-stop system model.

*/



using System;
using System.Threading.Tasks;
using Microsoft.Extensions.Caching.Memory;

pubic class RpcRequest{
    pubic required string IdempotencyKey { get; set; }
    pubic required string Payload { get; set; }

}


public class RpcResponse{
    pubic required bool Success { get; set; }
    public string? Data { get; set; }
}

public class RpcServer
{
    private readonly IMemoryCache _cache;

    // Dependency injection provides the cache instance
    public RpcServer(IMemoryCache cache)
    {
        _cache = cache;
    }

    public async Task<RpcResponse> ProcessRequestAsync(RpcRequest request)
    {
        // 1. Check if we've already processed this exact request ID
        if (_cache.TryGetValue(request.IdempotencyKey, out RpcResponse? cachedResponse))
        {
            Console.WriteLine($"[Cache Hit] Duplicate request. Returning previous response for {request.IdempotencyKey}");
            return cachedResponse!;
        }

        // 2. Not in cache -> Process it (New Request)
        Console.WriteLine($"[New Request] Processing {request.IdempotencyKey}...");
        RpcResponse newResponse = await PerformOperationAsync(request.Payload);

        // 3. Store the result in the cache with a Time-To-Live (TTL)
        var cacheOptions = new MemoryCacheEntryOptions()
            .SetAbsoluteExpiration(TimeSpan.FromHours(24)); // Remember this ID for 24 hours

        _cache.Set(request.IdempotencyKey, newResponse, cacheOptions);

        return newResponse;
    }

    // Mock of the actual business logic
    private Task<RpcResponse> PerformOperationAsync(string payload)
    {
        return Task.FromResult(new RpcResponse 
        { 
            Success = true, 
            Data = $"Successfully processed: {payload}" 
        });
    }
}