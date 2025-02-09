from src.parser import parse
from src.semantic import SemanticAnalyzer
from src.ir import IRGenerator
from src.interpreter import Interpreter

class DeathNoteCompiler:
    def __init__(self):
        self.ast = None

    def compile(self, code):
        """Compile Death Note code."""
        # Step 1: Parse the code
        self.ast = parse(code)

        # Step 2: Perform semantic analysis
        analyzer = SemanticAnalyzer(self.ast)
        analyzer.analyze()

        # Step 3: Generate IR (optional)
        ir_generator = IRGenerator()
        ir_module = ir_generator.generate(self.ast)

        # Step 4: Execute the code
        interpreter = Interpreter(self.ast)
        interpreter.execute()

        return ir_module