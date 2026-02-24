/*

Reliable network links allow messages to be reordered. Give pseudocode for an algorithm

that strengthens the properties of a reliable point-to-point link such that messages are received in the order

they were sent (this is called a FIFO link), assuming an asynchronous crash-stop system model.

*/


using System;
using System.Collections.Generic;

public class Packet
{
    public required string Message { get; set; }
    public required int SequenceNumber { get; set; }
}

// -----------------------------------------
// SENDER LOGIC
// -----------------------------------------
public class FifoSender
{
    private int _sendSeq = 0;
    private readonly IReliableLink _underlyingLink;

    public FifoSender(IReliableLink underlyingLink)
    {
        _underlyingLink = underlyingLink;
    }

    public void SendFifo(string message, string destinationId)
    {
        var packet = new Packet 
        { 
            Message = message, 
            SequenceNumber = _sendSeq 
        };
        
        // Send using the underlying reorder-prone link
        _underlyingLink.ReliableSend(packet, destinationId);
        
        _sendSeq++; // Increment for the next message
    }
}

// -----------------------------------------
// RECEIVER LOGIC
// -----------------------------------------
public class FifoReceiver
{
    private int _deliverSeq = 0;
    
    // Dictionary to act as the out-of-order message buffer
    private readonly Dictionary<int, string> _buffer = new();

    public void ReceiveReliable(Packet packet, string senderId)
    {
        if (packet.SequenceNumber == _deliverSeq)
        {
            // 1. The message is the exact one we are waiting for
            DeliverToApplication(packet.Message, senderId);
            _deliverSeq++;

            // 2. Check the buffer to see if subsequent messages are already waiting
            while (_buffer.TryGetValue(_deliverSeq, out string? bufferedMsg))
            {
                DeliverToApplication(bufferedMsg, senderId);
                _buffer.Remove(_deliverSeq);
                _deliverSeq++;
            }
        }
        else if (packet.SequenceNumber > _deliverSeq)
        {
            // The message arrived too early (out of order). Buffer it for later.
            _buffer[packet.SequenceNumber] = packet.Message;
            Console.WriteLine($"[Buffered] Message {packet.SequenceNumber} arrived early.");
        }
        
        // If packet.SequenceNumber < _deliverSeq, it's a delayed duplicate. 
        // We simply ignore it by dropping out of the if/else block.
    }

    private void DeliverToApplication(string message, string senderId)
    {
        Console.WriteLine($"[Delivered in Order] From {senderId}: {message}");
    }
}

// Mock interface for the underlying network link
public interface IReliableLink
{
    void ReliableSend(Packet packet, string destinationId);
}