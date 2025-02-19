import ast
from src.transpiler import Transpiler


def test_basic_assignment():
    transpiler = Transpiler()
    code = "x = 10"
    assembly = transpiler.compile(code)
    assert "mov rax, 10" in assembly
