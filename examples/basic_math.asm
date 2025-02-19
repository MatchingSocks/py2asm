section .text
global _start
_start:
    mov rax, 10
    mov [x], rax
    mov rax, 0
    mov [y], rax