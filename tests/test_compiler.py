import unittest
from src.compiler import DeathNoteCompiler
from lark import UnexpectedCharacters, UnexpectedToken

class TestDeathNoteCompiler(unittest.TestCase):
    def setUp(self):
        self.compiler = DeathNoteCompiler()

    def test_empty_notebook(self):
        code = """
        notebook() {
        }
        """
        result = self.compiler.compile(code)
        self.assertIsNotNone(result)

    def test_variable_declaration(self):
        code = """
        notebook() {
            apple name = "Light";
            apple age = 25;
            apple score = 98.6;
        }
        """
        result = self.compiler.compile(code)
        self.assertIsNotNone(result)

    def test_write_statement(self):
        code = """
        notebook() {
            write("Hello Death Note");
            apple msg = "Test";
            write(msg);
        }
        """
        result = self.compiler.compile(code)
        self.assertIsNotNone(result)

    def test_judgment_statement(self):
        code = """
        notebook() {
            apple age = 20;
            judgment (age > 18) {
                write("Adult");
            } eyem (age == 18) {
                write("Just turned adult");
            } otherwise {
                write("Minor");
            }
        }
        """
        result = self.compiler.compile(code)
        self.assertIsNotNone(result)

    def test_loop_statement(self):
        code = """
        notebook() {
            lifespan i in range(5) {
                write(i);
            }
        }
        """
        result = self.compiler.compile(code)
        self.assertIsNotNone(result)

    def test_function_declaration(self):
        code = """
        notebook() {
            shinigami rule calculate_age(birth_year) {
                apple current_year = 2024;
                apple age = current_year - birth_year;
                write(age);
            }
        }
        """
        result = self.compiler.compile(code)
        self.assertIsNotNone(result)

    def test_complex_program(self):
        code = """
        notebook() {
            apple count = 0;
            lifespan i in range(3) {
                judgment (i > 1) {
                    write("Greater than one");
                } otherwise {
                    write("Less than or equal to one");
                }
            }
        }
        """
        result = self.compiler.compile(code)
        self.assertIsNotNone(result)

    def test_invalid_syntax(self):
        invalid_codes = [
            # Missing notebook declaration
            """
            apple name = "Light";
            """,
            
            # Missing semicolon
            """
            notebook() {
                apple name = "Light"
            }
            """,
            
            # Invalid judgment syntax
            """
            notebook() {
                judgment age > 18 {
                    write("Adult");
                }
            }
            """,
            
            # Invalid variable name
            """
            notebook() {
                apple 123name = "Invalid";
            }
            """
        ]

        for code in invalid_codes:
            with self.assertRaises((UnexpectedCharacters, UnexpectedToken)):
                self.compiler.compile(code)

    def test_nested_statements(self):
        code = """
        notebook() {
            lifespan i in range(3) {
                judgment (i > 1) {
                    lifespan j in range(2) {
                        write(j);
                    }
                } otherwise {
                    write("Too small");
                }
            }
        }
        """
        result = self.compiler.compile(code)
        self.assertIsNotNone(result)
    
    def test_multiple_variables(self):
        code = """
        notebook() {
            apple name = "Light";
            apple age = 25;
            judgment (age > 20) {
                apple status = "Adult";
                write(status);
            }
        }
        """
        result = self.compiler.compile(code)
        self.assertIsNotNone(result)
    
    def test_arithmetic_operations(self):
        code = """
        notebook() {
            apple a = 10;
            apple b = 5;
            apple sum = a + b;
            apple diff = a - b;
            apple prod = a * b;
            apple quot = a / b;
            apple complex = (a + b) * (a - b);
            write(sum);
            write(diff);
            write(prod);
            write(quot);
            write(complex);
        }
        """
        result = self.compiler.compile(code)
        self.assertIsNotNone(result)

    def test_function_with_arithmetic(self):
        code = """
        notebook() {
            shinigami rule calculate_age(birth_year) {
                apple current_year = 2024;
                apple age = current_year - birth_year;
                apple next_year_age = age + 1;
                write(age);
                write(next_year_age);
            }
        }
        """
        result = self.compiler.compile(code)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main(verbosity=2)