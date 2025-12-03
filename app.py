#!/usr/bin/env python3
import argparse

def fib(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def greet(name: str = "World") -> str:
    """Return a greeting for `name`."""
    return f"Hello, {name}!"

def main() -> None:
    parser = argparse.ArgumentParser(description="Simple demo app")
    sub = parser.add_subparsers(dest="cmd")

    g = sub.add_parser("greet", help="Print a greeting")
    g.add_argument("--name", "-n", default="World", help="Name to greet")

    f = sub.add_parser("fib", help="Compute fibonacci number")
    f.add_argument("n", type=int, help="Index (non-negative integer)")

    args = parser.parse_args()
    if args.cmd == "greet":
        print(greet(args.name))
    elif args.cmd == "fib":
        print(fib(args.n))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
