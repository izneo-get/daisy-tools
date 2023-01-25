import sys
import runpy

sys.path.append("daisy_renamer")


def main() -> None:
    runpy.run_module("daisy_renamer", run_name="__main__")


if __name__ == "__main__":
    main()
