import os
from file_signatures import FILE_SIGNATURES
from log import setup_log
import logging

# Fossil Finder
# A digital forensic tool that identifies true file types by analyzing file signatures
# and detects mismatches between extensions and actual content.
#
# Every file type corresponds to a dinosaur species
# Files are treated as fossil imprints, and their signatures are used to
# determine their true "species" regardless of their label.

# Maps the files extensions to their correpsonding species
SPECIES_MAP = {
    "jpg": "T-Rex (jpg)",
    "png": "Triceratops (png)",
    "pdf": "Stegosaurus (pdf)",
    "exe": "Velociraptor (exe)",
    "zip": "Pterodactyl (zip)"
}

# Reads fossil imprint (file bytes)
def get_fossil_imprint(file_path, num_bytes=8):
    with open(file_path, "rb") as f:
        return f.read(num_bytes) # Reads the file headers bytes

# Identifies actual fossil species:
# Compares file bytes against known fossil signatures and returns the detected species (file type)
def identify_fossil(file_bytes):
    for species, signatures in FILE_SIGNATURES.items():
        for sig in signatures:
            if file_bytes.startswith(sig):
                return species
    return "unknown"

# Simulates excavation process: 
# Scan every file in a directory for clasification 
def excavate(directory):
    print("""
==================================
       🦴 FOSSIL FINDER 🦖
   Digital Archaeology System
==================================
""")

    print(" Dusting away sediment...\n")
    logging.info("Excavation started in: %s", directory)

    # Goes through every file in the directory 
    for root, _, files in os.walk(directory):
        for file in files:
            
            # Builds the file path
            path = os.path.join(root, file)

            try:
                # Gets the fossil imprint (file signature)
                fossil_imprint = get_fossil_imprint(path)
                
                # Identifies the actual file type
                actual_type = identify_fossil(fossil_imprint)

                # Gets the file extension (what type the file claims to be)
                claimed_type = file.split(".")[-1].lower()

                # Matches file type with its corresponding dinosaur species 
                actual_species = SPECIES_MAP.get(actual_type, "Unknown Species")
                claimed_species = SPECIES_MAP.get(claimed_type, "Unknown Species")

                print(f"Excavating Fossil and Identifying Species: {file}")

                # Compares the file extension (claimed identity) with the species (actual identity)
                # to see if they match 
                if claimed_species != actual_species:
                    print(f"WARNING: Fossil mismatch detected!")
                    print(f"    Labeled: {claimed_species}")
                    print(f"    Identified: {actual_species}\n")

                    # Mismatch files are suspicious 
                    # Logs suspicious files for further forensic review
                    logging.warning(
                        "Fossil mismatch: %s (labeled=%s, actual=%s)",
                        path, claimed_species, actual_species
                    )
                else:
                    print(f"Verified fossil: {actual_species}\n")
                    logging.info("Verified fossil: %s", path)

            # Handles unreadable files 
            except Exception as e:
                logging.error("Excavation error on %s: %s", path, str(e))

    # Indicates the excavation process is complete
    # Means all files have been scanned
    print("Excavation complete.")
    
    # Logs that the scan is complete 
    logging.info("Excavation completed.")

# Main entry point of the program
# Ensures Fossil Finder only starts execution when run directly 
if __name__ == "__main__":
    
    # Initializes logging system
    setup_log()
    
    # Prompts user for the excavation site (directory) to analyze
    folder = input("Enter excavation site (folder): ")
    
    # Starts the fossil excavation (runs the file scan process)
    excavate(folder)