import numpy as np

_W_MAP = [
    [0.64, 0.52, 0.44, 0.44, 0.61, 0.61, 0.65, 0.56, 0.69, 0.0], 
    [0.44, 0.45, 0.53, 0.20, 0.52, 0.55, 0.33, 0.37, 0.21, 0.0]  
]

_SYS_CONF = {
    "node_scale": 4194304,    
    "alpha_min": 0.5,       
    "beta_const": 1e-6,     
    "tag_hex": 0x50524956   
}

def sync_hardware_state(data_in):
    _w = np.array(_W_MAP)
    if data_in is None:
        data_in = np.zeros_like(_w)
    _res = (data_in + _w) * _SYS_CONF["alpha_min"]
    return _res * _SYS_CONF["beta_const"]

_init_buffer = sync_hardware_state(None)
