from typing import Dict, List, Set
from daisy_renamer import chapter, select_folder, get_sub_smil, get_audiofile_from_smil, batch_rename

MASTER_FILE: str = "master.smil"
DEFAULT_OUTPUT: str = "OUTPUT"

__VERSION__: str = "0.1.0"


def main() -> None:
    daisy_folder = select_folder(MASTER_FILE)
    sub_smil = get_sub_smil(f"{daisy_folder}/{MASTER_FILE}")
    chapters: List = []
    for index, elem in enumerate(sub_smil):
        title, smil = elem
        if audio_file := get_audiofile_from_smil(f"{daisy_folder}/{smil}"):
            chapters.append(chapter(index + 1, title, f"{daisy_folder}/{audio_file}"))
    batch_rename(chapters, output_folder=f"{daisy_folder}/{DEFAULT_OUTPUT}")


if __name__ == "__main__":
    main()
