# Register Renaming Project
This project implements register renaming in a computer architecture context. Register renaming is a technique used to eliminate data hazards in a processor pipeline by assigning different names to destination registers. The code demonstrates how register renaming can be achieved using the Box-Muller method.

## Overview
The project includes three main functions:

destAlloc: Assigns different names to destination registers based on the Box-Muller method. It performs operations such as addition, subtraction, multiplication, division, bitwise AND/OR, left shift, right shift, greater than, less than, and bitwise XOR.

registerUpdate: Updates the register values in the Architectural Register File (ARF) from the Rename Register File (RRF) after all instructions are completed.

sourceOperandRead: Reads values of source operands from the ARF or RRF based on the provided source register.

## Usage
Initialize the Architectural Register File (ARF) and Rename Register File (RRF) with starting values.

Perform operations using the destAlloc function for different instructions.

Update register values in the ARF using the registerUpdate function after all instructions are completed.

Display the contents of register files at different stages of execution.

Example
The code includes an example demonstrating register renaming for three instructions:

Addition: R1 <= R2 + R3
Subtraction: R3 <= R1 - R2
Multiplication: R3 <= R1 * R2
The code outputs the contents of the register files at various stages of execution, providing insights into how register renaming eliminates data hazards.

#Note
This project serves as a simulation of register renaming and can be extended for more complex scenarios in computer architecture research and development.

Feel free to experiment with different instructions and observe the behavior of register renaming.
