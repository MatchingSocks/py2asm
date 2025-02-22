import ast
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python astview.py <file.py>")
        return

    pyexpr = sys.argv[1]

    # Parse the expression into an AST
    tree = ast.parse(pyexpr)

    # Print the AST structure
    print(ast.dump(tree, indent=2))


if __name__ == "__main__":
    main()
