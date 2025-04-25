from Initialization.network import initialize_network
from Initialization.routing_path import initialize_routing
from Message_encryption.encryption import encrypt_data, decrypt_data
from Initialization.network import initialize_network
import matplotlib.pyplot as plt
import networkx as nx
import base64
from Original_data_recovery.original_data import recover_original_data
from Message_encryption.share_generation import generate_shares

G, sensor_nodes, sink_node, positions = initialize_network(num_nodes=10)

message = input("Enter message to encrypt and send to sink node: ")
start_encrypt = time.perf_counter()
encrypted = encrypt_data(message, sink_node)
end_encrypt = time.perf_counter()
T_encrypt = end_encrypt - start_encrypt

routing_table = {
    "node0": ["node1", "node5", "node13"]
}

t=len(routing_table["node0"])-1
start_share_tx = time.perf_counter()
shares = generate_shares(encrypted, t, routing_table, "node0")
end_share_tx = time.perf_counter()
T_share_tx = end_share_tx - start_share_tx

start_share_tx = time.perf_counter()
shares = generate_shares(encrypted, t, routing_table, "node0")
end_share_tx = time.perf_counter()
T_share_tx = end_share_tx - start_share_tx

decrypted = recover_original_data(shares,sink_node,"node0",routing_table,sink_node.private_key)
print("original data is: ",decrypted)
