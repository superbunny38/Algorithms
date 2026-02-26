using System;
using System.Collections.Generic;

public enum NodeRole 
{
    Follower,
    Candidate,
    Leader
}

public class LogEntry 
{
    public string Msg { get; set; }
    public int Term { get; set; }
}

public class VoteRequestMsg 
{
    public string NodeId { get; set; }
    public int CurrentTerm { get; set; }
    public int LogLength { get; set; }
    public int LastTerm { get; set; }
}

public class RaftNode 
{
    // Node identifier and cluster peers
    private string nodeId;
    private List<string> nodes; 

    // Persistent state on all servers (Updated on stable storage before responding to RPCs)
    private int currentTerm;
    private string votedFor;
    private List<LogEntry> log;

    // Volatile state on all servers
    private int commitLength;
    private NodeRole currentRole;
    private string currentLeader;

    // Volatile state on leaders (Reinitialized after election)
    private HashSet<string> votesReceived;
    private Dictionary<string, int> sentLength;
    private Dictionary<string, int> ackedLength;

    public RaftNode(string id, List<string> clusterNodes) 
    {
        this.nodeId = id;
        this.nodes = clusterNodes;
    }

    // 1. on initialisation do
    public void OnInitialisation() 
    {
        currentTerm = 0;
        votedFor = null;
        log = new List<LogEntry>();
        commitLength = 0;
        currentRole = NodeRole.Follower;
        currentLeader = null;
        votesReceived = new HashSet<string>();
        sentLength = new Dictionary<string, int>();
        ackedLength = new Dictionary<string, int>();
    }

    // 2. on recovery from crash do
    public void OnRecoveryFromCrash() 
    {
        // Note: In a real implementation, currentTerm, votedFor, and log 
        // would be loaded from stable storage here.
        currentRole = NodeRole.Follower;
        currentLeader = null;
        votesReceived = new HashSet<string>();
        sentLength = new Dictionary<string, int>();
        ackedLength = new Dictionary<string, int>();
    }

    // 3. on node nodeId suspects leader has failed, or on election timeout do
    public void OnElectionTimeout() 
    {
        currentTerm++;
        currentRole = NodeRole.Candidate;
        votedFor = nodeId;
        
        votesReceived = new HashSet<string> { nodeId };

        int lastTerm = 0;
        if (log.Count > 0) 
        {
            lastTerm = log[log.Count - 1].Term;
        }

        var msg = new VoteRequestMsg 
        {
            NodeId = this.nodeId,
            CurrentTerm = this.currentTerm,
            LogLength = this.log.Count,
            LastTerm = lastTerm
        };

        foreach (var node in nodes) 
        {
            if (node != this.nodeId) 
            {
                SendMsgToNode(node, msg);
            }
        }

        StartElectionTimer();
    }

    // --- Helper Methods (Implementation abstracted for pseudocode) ---
    private void SendMsgToNode(string targetNode, object msg) { /* Network dispatch */ }
    private void StartElectionTimer() { /* Reset and start randomized timer */ }
}
