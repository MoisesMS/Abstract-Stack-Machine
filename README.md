# DESCRIPTION
This is a simulator of a compiler for a pseudo lenguage writted in Python

# USAGE
- Clone the project
```
  git clone https://github.com/MoisesMS/PseudoCompiler.git
```

- Run the project
```
  python3 Abstract-Stack-Maachine
```


# How to program

This pseudo lenguage have a three instructions
- METE [number] Add a number to stack. Example:
  ```ADD 1```
- SUM Add up the two last numbers in the stack and put the result in the top of stack. Example ```SUM```
- SUB Substract up the two last numbers in the stack and put the result in the top of stack. Example ```SUB```
- MUL Multiply up the two last numbers in the stack and put the result in the top of stack. Example ```MUL```
- DIV Divide up the two las numbers in the stack and put the result in the top of stack. Example ```DIV```
- GET get the last number in the stack. Example ```GET```
- DEL delete the last number in the stack. Example ```DEL```
- SWAP Swap the two last numbers in the stack. Example ```SWAP```
- EXIT Exit of the program. Example ```EXIT```
  
## Example of program
Add two numbers and show it
```
  ADD 1
  ADD 2
  SUM
  GET
```


# TODO
- Add registers of memory
