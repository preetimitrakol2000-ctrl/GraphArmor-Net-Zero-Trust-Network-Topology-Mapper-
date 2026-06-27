from graph_bridge import GraphBridge

def main():
    print("=== GRAPHARMOR-NET: ZERO-TRUST BREACH ACCELERATION ANALYZER ===")
    
    # Let's declare map topology nodes
    # 0: Firewalled Public Gate, 1: Active Directory Server, 2: User Workstation, 
    # 3: Financial Database, 4: Isolated Backup Server
    device_map = {
        0: "Public Edge Gateway",
        1: "Active Directory (Domain Controller)",
        2: "User Workstation LAN",
        3: "Core Production Database",
        4: "Isolated Backup Node"
    }

    # Initialize bridge for 5 devices
    analyzer = GraphBridge(num_nodes=len(device_map))

    # Build network paths (Source Node, Destination Node, Attack Likelihood Weight)
    analyzer.connect_devices(src=0, dest=2, vulnerability=0.85) # Gateway to Workstation
    analyzer.connect_devices(src=2, dest=1, vulnerability=0.60) # Workstation compromise leads to AD
    analyzer.connect_devices(src=1, dest=3, vulnerability=0.90) # AD compromised grants DB access
    analyzer.connect_devices(src=3, dest=4, vulnerability=0.10) # Strong zero-trust isolation to Backups

    # Simulate Breach on User Workstation (Node 2)
    breached_node = 2
    print(f"\n[!] ALERT: Simulated Compromise on: Asset {breached_node} [{device_map[breached_node]}]")
    
    # Process graph blast vector down the stack via C
    compromised_zone = analyzer.trace_blast_radius(breached_node)

    print("\n---------------------------------------------------------")
    print("CALCULATED BLAST RADIUS RESULTS (BFS Traversal Output):")
    print("---------------------------------------------------------")
    for idx, node in enumerate(compromised_zone):
        status = "CRITICAL PATH IMPACT" if idx > 0 else "PATIENT ZERO"
        print(f" -> Level {idx} Exposure: Device {node} ({device_map[node]}) [{status}]")

    print("\n[Isolation Recommendation]")
    unreachable = [node for node in device_map if node not in compromised_zone]
    for clean_node in unreachable:
        print(f"[SECURE]: Asset {clean_node} ({device_map[clean_node]}) remains partitioned via active Access Control Lists.")

if __name__ == "__main__":
    main()
