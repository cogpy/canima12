#!/usr/bin/env python3
"""Search and retrieve text from the Uniform Rules of Court.

Commands:
  search <keyword>: Search all rules for a keyword.
  get <rule_num> [rule_num...]: Get the full text of one or more rules.
"""
import json, sys, re

RULES_FILE = "/home/ubuntu/skills/uniform-rules-of-court/references/all_rules.json"

def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    with open(RULES_FILE, "r") as f:
        rules = json.load(f)

    if command == "search":
        keyword = args[0]
        print(f"Searching for '{keyword}' in {len(rules)} rules...\n")
        found = 0
        for rnum, data in rules.items():
            desc = data["description"]
            text = data["text"]
            if re.search(keyword, text, re.IGNORECASE):
                found += 1
                print(f"--- Rule {rnum}: {desc} ---")
                match = re.search(keyword, text, re.IGNORECASE)
                start = max(0, match.start() - 100)
                end = min(len(text), match.end() + 100)
                snippet = text[start:end]
                print(f"...{snippet}...\n")
        print(f"Found {found} matching rules.")

    elif command == "get":
        for rnum in args:
            if rnum in rules:
                desc = rules[rnum]["description"]
                text = rules[rnum]["text"]
                print(f"=== Rule {rnum}: {desc} ===\n")
                print(text)
                print()
            else:
                print(f"Rule {rnum} not found.")
    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)

if __name__ == "__main__":
    main()
