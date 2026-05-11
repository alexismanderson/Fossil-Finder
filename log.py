import logging

# Configures the logging system for Fossil Finder
def setup_log():
    logging.basicConfig(
        filename="scan.log", # Output file where scanned activity is recorded
        level=logging.INFO, # Will record INFO, WARNING, and ERROR
        format="%(asctime)s - 🦴 %(levelname)s - %(message)s"
    )