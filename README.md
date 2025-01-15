### Galactic Cargo Management System (GCMS)

This repository contains the implementation of Galactic Cargo Management System (GCMS), a system designed to efficiently manage interstellar cargo bins and objects. The project aims to solve a specialized bin-packing problem with constraints based on the color of cargo.

### Background
In the galaxy, shipping companies face challenges in efficiently packing cargo into bins. Each cargo bin has a capacity, and each cargo object has a size and a unique color that determines how it should be packed.

The GCMS handles cargo based on the following rules:
1. **Blue Cargo (Compact Fit, Least ID)**: Assign to the smallest bin that can fit the object. If multiple bins qualify, choose the bin with the least ID.
2. **Yellow Cargo (Compact Fit, Greatest ID)**: Assign to the smallest bin that can fit the object. If multiple bins qualify, choose the bin with the greatest ID.
3. **Red Cargo (Largest Fit, Least ID)**: Assign to the largest bin that can fit the object. If multiple bins qualify, choose the bin with the least ID.
4. **Green Cargo (Largest Fit, Greatest ID)**: Assign to the largest bin that can fit the object. If multiple bins qualify, choose the bin with the greatest ID.

### File Structure
| File            | Description                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------|
| `gcms.py`       | Main class implementing the Galactic Cargo Management System.                                     |
| `bin.py`        | Class representing individual cargo bins, their properties, and operations.                      |
| `object.py`     | Class representing individual objects, their properties, and operations.                         |
| `avl.py`        | AVL tree implementation for efficient data storage and retrieval.                                |
| `node.py`       | Class for AVL tree nodes.                                                                        |
| `exceptions.py` | Custom exceptions for handling edge cases. **(Do not modify this file)**.                        |
| `main.py`       | Script for debugging and testing the GCMS implementation.                                        |

### Author
Developed as part of a university-level software engineering project by **GAJENDRA DHANOLIYA**.
