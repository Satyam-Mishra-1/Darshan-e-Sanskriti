import logging
import os
from datetime import datetime
from from_root import from_root

# Generate a timestamped log filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the 'log' directory path
log_dir = os.path.join(from_root(), 'log')
os.makedirs(log_dir, exist_ok=True)  # Ensure 'log' directory exists

# Full log file path
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Setup logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
