# Fossil Species Classification Table
# Every file type corresponds to a dinosaur species
# (File signatures = fossil imprints)

FILE_SIGNATURES = {
    #JPG files = T-rex
    "jpg": [b"\xFF\xD8\xFF"],     # T-Rex fossil
    
    #PNG files = Triceratops
    "png": [b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"],     # Triceratops fossil
    
    #PDF files = Stegosaurus
    "pdf": [b"\x25\x50\x44\x46\x2D"],     # Stegosaurus fossil 
    
    #EXE files = Velociraptor
    "exe": [b"\x4D\x5A"],     # Velociraptor fossil
    
    #ZIP files = Pterodactyl
    "zip": [b"\x50\x4B\x03\x04"]     # Pterodactyl fossil
}