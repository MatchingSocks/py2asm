import sys
from .src.transpiler import Transpiler


def main():
    if len(sys.argv) < 2:
        print("Usage: python transpile.py <file.py>")
        return

    filename = sys.argv[1]
    with open(filename, "r") as f:
        code = f.read()

    transpiler = Transpiler()
    assembly_code = transpiler.compile(code)

    output_file = filename.replace(".py", ".asm")
    with open(output_file, "w") as f:
        f.write(assembly_code)

    print(f"Transpiled to {output_file}")


if __name__ == "__main__":
    main()
