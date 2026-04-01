import numpy as np
import pandas as pd
from cryptography.hazmat.primitives import hashes

def format_tensor_stream(raw_buffer):
    data = pd.DataFrame(raw_buffer)
    return data.to_numpy(dtype=np.float32)

def compute_hw_checksum(payload):

    digest = hashes.Hash(hashes.SHA256())
    digest.update(payload)
    return digest.finalize().hex()[:8]
