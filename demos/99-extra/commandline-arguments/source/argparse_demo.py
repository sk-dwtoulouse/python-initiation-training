import argparse

if __name__ == "__main__":
    # Argparse demo: accept running this script with options like command tools.
    parser = argparse.ArgumentParser(description="Demonstration argument parser")
    parser.add_argument("--plop", required=True, help="Argument inutile", type=int)
    parser.add_argument("--plip", required=False, default=None, help="Autre argument inutile", type=int)
    options = parser.parse_args()

    print(options)
    print(options.plip)
    print(options.plop)
    print(options.__dict__)
