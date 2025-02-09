# Death Note Compiler

This repository contains the source code for the **Death Note Compiler**, a custom programming language inspired by the Death Note anime. The language provides an immersive and intuitive coding experience, with constructs and keywords based on the anime's themes.

## Features
- **Brace-based syntax** similar to C/Java
- **No explicit data types**, making it flexible like Python
- Keywords and logic inspired by the Death Note anime, such as `notebook`, `write`, `judgment`, `shinigami`, etc.
- Supports core programming concepts like variables, loops, conditionals, functions, and more.

## Grammar and Syntax

The language's grammar is defined using the Lark parser, and here is a detailed explanation of the constructs and syntax:

### Main Function (Program Entry Point)
```plaintext
notebook() { ... }
```
- Defines the entry point of the program.
- The program execution starts inside the `notebook()` block.

### Variable Declaration
```plaintext
apple variable_name = value;
```
- Declares and initializes a variable, where `apple` is used as the keyword for variable declaration.

### Output Statement
```plaintext
write(expression);
```
- Outputs the result of the `expression`.

### Conditional Statements
```plaintext
judgment(condition) { ... }
eyem(condition) { ... }
otherwise { ... }
```
- `judgment` is used for evaluating a condition and executing the code inside the block if the condition is true.
- `eyem` is used to define an alternative condition within the `judgment` block.
- `otherwise` specifies the block to execute when no conditions are met.

### Loops
#### For Loop
```plaintext
lifespan days in range(10) { ... }
```
- Iterates over a range of values (like a `for` loop in traditional programming languages).

#### While Loop
```plaintext
haunt(condition) { ... }
```
- Executes the loop as long as the condition evaluates to true (similar to a `while` loop).

### Functions
#### Function Declaration
```plaintext
shinigami rule(function_name(parameters)) { ... }
```
- Defines a function with the `shinigami rule` keyword.

#### Function Call
```plaintext
function_name(parameters);
```
- Calls a defined function with the specified parameters.

### Boolean and Special Keywords
- `justice` represents `true`
- `evil` represents `false`
- `void` represents `None`

### Loop Controls
- `sacrifice;` - Breaks the loop
- `resurrect;` - Skips to the next iteration (continue)
- `realm;` - Passes the current iteration (similar to `pass` in Python)

### Return Statement
```plaintext
banish value;
```
- Exits a function and returns the specified value.

---
### How to Use the Death Note Compiler (Using Binary)

1. **Download the Latest Release**:
   - Download the pre-compiled binary (`death_note_compiler_linux.tar.gz`).

2. **Extract the Binary**:
   - After downloading, extract the archive using the following command:
     ```bash
     tar -xvzf death_note_compiler_linux.tar.gz
     ```

3. **Run the Compiler**:
   - Navigate to the extracted folder where the `death_note` binary is located.
   - Run the compiler directly from the command line:
     ```bash
     ./death_note <path_to_your_code_file.dn>
     ```

   - Example usage:
     ```bash
     ./death_note examples/example.dn
     ```

4. **Check the Output**:
   - The compiler will process the provided `.dn` file and display the output based on the logic in the code.

---

### Example

If you want to run the example code from the `examples/` folder:

1. **Navigate to the folder**:
   ```bash
   cd death_note_compiler/dist
   ```

2. **Run an example `.dn` file**:
   ```bash
   ./death_note examples/hello.dn
   ```

---

This method allows you to quickly use the Death Note compiler without needing to install any dependencies manually. Just download, extract, and run the binary!

---

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. If you find any bugs or have suggestions for improvements, please create an issue in the GitHub repository.

---
