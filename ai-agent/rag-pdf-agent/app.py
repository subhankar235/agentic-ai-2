import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from src.ingest import ingest_pdf
from src.agent import build_agent

def main():
    # Step 1: create DB if not exists
    if not os.path.exists("db"):
        ingest_pdf("data/notes.txt")

    # Step 2: run agent
    agent = build_agent()

    while True:
        try:
            q = input("Ask: ")
            if not q.strip():
                print("Please enter a question.")
                continue
            if q.lower() == "exit":
                break

            res = agent.run(q)
            print("\nAnswer:", res)
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    main()