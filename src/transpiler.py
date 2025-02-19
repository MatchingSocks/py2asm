import ast


class Transpiler:
    def compile(self, code):
        tree = ast.parse(code)
        asm_code = ["section .text", "global _start", "_start:"]

        for node in tree.body:
            if isinstance(node, ast.Assign):
                var_name = node.targets[0].id
                value = node.value.n if isinstance(node.value, ast.Constant) else 0
                asm_code.append(f"    mov rax, {value}")
                asm_code.append(f"    mov [{var_name}], rax")

        return "\n".join(asm_code)
