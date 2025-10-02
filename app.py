import hashlib

def compute_hash(combined: str) -> str:
    return hashlib.sha256(combined.encode()).hexdigest()

def proof_of_work(client_id, application_id, location_id, instance_id, target_prefix):
    nonce = 0
    while True:
        combined = f"{client_id}:{application_id}:{location_id}:{instance_id}:{nonce}"
        hash_result = compute_hash(combined)

        # Print the first few attempts as samples
        if nonce < 5:
            print(f"Try nonce={nonce} -> {hash_result}")

        if hash_result.startswith(target_prefix):
            print(f"\n✅ Valid PoW Found!")
            print(f"Nonce: {nonce}")
            print(f"Hash:  {hash_result}")
            return nonce
        nonce += 1

if __name__ == "__main__":
    client_id = "SESSION_ID"
    application_id = "APP_ID"
    location_id = "LOC_ID"
    instance_id = "INST_ID"
    target_prefix = "0000"   # difficulty (more zeros = harder)

    proof_of_work(client_id, application_id, location_id, instance_id, target_prefix)