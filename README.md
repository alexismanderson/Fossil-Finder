# 🦴 Fossil Finder 🦖

## Author
Alexis Anderson

## Overview
Fossil Finder is a digital forensic tool that treats files as digital fossils. 
The program analyzes file signatures (fossil imprints) and compares them 
to file extensions to identify mismatches between a file’s claimed identity 
and its true content. 
Mismatches indicate either a mislabeled file or a suspicious file.

Each file type is represented as a dinosaur species, allowing Fossil Finder 
to classify files based on their actual signatures regardless of their labels.

## Purpose
IS a digital forensic analysis tool to identify mislabeled or suspicious files. 
It is very easy for someone to change a file extension in order to disguise a malicious file, however this does not chnage its file signature. 
This tool helps us to detect this mismatch in file extension and file signature in order to flag these potentially malicious files and stop users from opening them.

## Concept
- File signatures = fossil imprints
- File types = dinosaur species
- Scanning = excavation process

## Features
- Identifies actual file types through file signature analysis
- Detects mismatches between file extensions and the actual file signature 
- Recursive directory scanning
- Logs excavation findings (mismatched and verified files) to scan.log
- Flags potentially mislabeled or suspicious files
- Handles unreadable or inaccessible files with error logging

## Test Files
The Test_Files directory contains example files used to demonstrate Fossil Finder’s detection capabilities.

## How to Run
- Run python3 main.py
- Enter the folder you want scanned 
- Run open scan.log

## Example Output
==================================
       🦴 FOSSIL FINDER 🦖
   Digital Archaeology System
==================================

 Dusting away sediment...

Excavating Fossil and Identifying Species: example.jpg
WARNING: Fossil mismatch detected!
    Labeled: T-Rex (jpg)
    Identified: Velociraptor (exe)

Excavating Fossil and Identifying Species: example.pdf
Verified fossil: Stegosaurus (pdf)

Excavation complete.
