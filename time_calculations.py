import time
from Message_encryption.encryption import encrypt_data, decrypt_data
from Message_encryption.share_generation import generate_shares
from Message_Transmission.msgtrans import simulate_message_transmission
start_encrypt = time.perf_counter()

end_encrypt = time.perf_counter()
T_encrypt = end_encrypt - start_encrypt

share_times = []
for share in shares:
    start_share = time.perf_counter()
    # Step 2: Simulate routing for this share
    ...
    end_share = time.perf_counter()
    share_times.append(end_share - start_share)

T_collect = max(share_times)

start_recon = time.perf_counter()
# Step 3: Reconstruct original ciphertext
...
end_recon = time.perf_counter()
T_reconstruct = end_recon - start_recon

T_total = T_encrypt + T_collect + T_reconstruct
print(f"Total Time Taken: {T_total:.4f} seconds")
