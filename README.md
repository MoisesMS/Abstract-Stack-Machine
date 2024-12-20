# DESCRIPTION
This is a simulator of a compiler for a pseudo lenguage writted in Python

# USAGE
- Clone the project
```
  git clone https://github.com/MoisesMS/PseudoCompiler.git
```

- Go to the project
```
  cd PseudoCompiler
```

- Run by adding the program as an argument
  
```
  Compiler.py program
```

# How to program

This pseudo lenguage have a three instructions
- ADD [number] Add a number to stack. Example:
  ```ADD 1```
- SUM Add up the two last numbers in the stack and put the result in the top of stack. Example ```SUM```
- GET get the last number in the stack. Example ```GET```
  
## Example of program
Add two numbers and show it
```
  ADD 1
  ADD 2
  SUM
  GET
```


# TODO
- Add operation of subtract
- Add operation of multiply
- Add operation of divide
- Add registers of memory