import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch PubMed papers by query")
    parser.add_argument("query", type=str, help="PubMed query")
    args = parser.parse_args()
    print(f"Running query: {args.query}")

if __name__ == "__main__":
    main()
