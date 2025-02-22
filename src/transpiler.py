import ast


class Transpiler:

    def compile(self, code):
        tree = ast.parse(code)
        asm_code = ["section .text", "global _start", "_start:"]

        for node in tree.body:
            # Basics
            if isinstance(node, ast.Assign):
                value = node.value.value
                asm_code.append(f"    mov rax, {value}")

            if isinstance(node, ast.BinOp):
                left = node.left.value
                right = node.right.value

                if isinstance(node.left, ast.Add):
                    asm_code.append(f"    mov eax, {left}")
                    asm_code.append(f"    add eax, {right}")
                elif isinstance(node.left, ast.Sub):
                    asm_code.append(f"    mov eax, {left}")
                    asm_code.append(f"    sub eax, {right}")
                elif isinstance(node.left, ast.Mult):
                    asm_code.append(f"    mov eax, {left}")
                    asm_code.append(f"    imul eax, {right}")
                elif isinstance(node.left, ast.Div):
                    asm_code.append(f"    mov eax, {left}")
                    asm_code.append(f"    mov ebx, {right}")
                    asm_code.append("    xor edx, edx")
                    asm_code.append("    div ebx")
                elif isinstance(node.left, ast.Mod):
                    asm_code.append(f"    mov eax, {left}")
                    asm_code.append(f"    mov ebx, {right}")
                    asm_code.append("    xor edx, edx")
                    asm_code.append("    div ebx")
                    asm_code.append("    mov eax, edx")
                elif isinstance(node.left, ast.FloorDiv):
                    asm_code.append(f"    mov eax, {left}")
                    asm_code.append(f"    mov ebx, {right}")
                    asm_code.append("    xor edx, edx")
                    asm_code.append("    div ebx")
                    asm_code.append("    mov eax, eax")
                elif isinstance(node.left, ast.Pow):
                    ...
                elif isinstance(node.left, ast.LShift):
                    ...
                elif isinstance(node.left, ast.RShift):
                    ...
                elif isinstance(node.left, ast.BitOr):
                    ...
                elif isinstance(node.left, ast.BitXor):
                    ...
                elif isinstance(node.left, ast.BitAnd):
                    ...
                elif isinstance(node.left, ast.MatMult):
                    ...

        return "\n".join(asm_code)
