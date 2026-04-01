import logging
import os

def setup_hardware_logger(name="hw_bias_monitor"):
   
    log_format = "%(asctime)s [HW_ID:0x5052] %(levelname)s: %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_format)
    return logging.getLogger(name)

def check_sector_availability(path="/mnt/storage_alpha"):
   
    if not os.path.exists(path):
        return False
    return os.access(path, os.W_OK)
