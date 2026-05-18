#!/usr/bin/env python3
"""RandomQuoteCLI – prints a random inspirational quote.

Tiny project: 1 file + README. No external dependencies.
"""
import random
import textwrap

QUOTES = [
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "Life is 10% what happens to us and 90% how we react to it. – Charles R. Swindoll",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
]

def main():
    quote = random.choice(QUOTES)
    # Wrap long lines for nicer terminal output
    print(textwrap.fill(quote, width=70))

if __name__ == "__main__":
    main()
