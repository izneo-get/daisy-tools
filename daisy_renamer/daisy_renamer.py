from typing import Dict, List, Set
from dataclasses import dataclass
from bs4 import BeautifulSoup
from collections import defaultdict
import os
import shutil
import re


MASTER_FILE: str = "master.smil"
DEFAULT_OUTPUT: str = "OUTPUT"


def clean_filename(filename: str) -> str:
    chars = '\\/:*<>?"|'
    for c in chars:
        filename = filename.replace(c, "_")
    filename = re.sub(r"\s+", " ", filename)
    filename = re.sub(r"\.+$", "", filename)
    filename = filename.strip()
    return filename


@dataclass
class chapter:
    chapter_no: int
    title: str
    audio_file: str


def select_folder(master_file: str = MASTER_FILE) -> str:
    daisy_folder = "?"
    while not os.path.isdir(daisy_folder) or not os.path.exists(f"{daisy_folder}/{master_file}"):
        daisy_folder = input('Répertoire du livre audio (doit contenir un fichier "master.smil") : ')
        if daisy_folder[0] == '"' and daisy_folder[-1] == '"':
            daisy_folder = daisy_folder[1:-1]
    return daisy_folder


def get_sub_smil(mater_smil_file: str) -> List[Set]:
    sub_smil_files: List = []
    with open(mater_smil_file, "r") as f:
        content = f.read()
    soup = BeautifulSoup(content, "xml")
    for elem in soup.find_all("ref"):
        title = elem["title"] or ""
        src = elem["src"] or ""
        title = title.encode("cp1252").decode()
        if title and src:
            sub_smil_files.append((title, src))
    return sub_smil_files


def get_audiofile_from_smil(smil_file: str) -> str:
    with open(smil_file, "r") as f:
        content = f.read()
    soup = BeautifulSoup(content, "xml")
    candidates = defaultdict(int)
    for elem in soup.find_all("audio"):
        candidates[elem["src"]] += 1

    if not candidates:
        print(f'WARNING : aucun nom de fichiers trouvé pour le chapitre "{smil_file}".')
        return ""

    audio_file = sorted(candidates.items(), key=lambda elem: elem[1], reverse=True)[0][0]

    if len(candidates) > 1:
        print(f'WARNING : plusieurs noms de fichiers ont été trouvés pour le chapitre "{smil_file}".')
        print(f'Le plus fréquent sera utilisé : "{audio_file}"')

    return audio_file


def batch_rename(chapters: List[chapter], output_folder: str = DEFAULT_OUTPUT) -> None:
    padding_length = len(str(len(chapters)))
    padding = padding_length * "0"
    os.makedirs(output_folder, exist_ok=True)
    for chapter in chapters:
        chapter_no: str = f"{padding}{chapter.chapter_no}"
        ext: str = os.path.splitext(chapter.audio_file)[1]
        new_file_name: str = (
            f'{output_folder}/{clean_filename(f"{chapter_no[-padding_length:]}. {chapter.title}{ext}")}'
        )
        print(f'Copie de "{chapter.audio_file}" vers "{new_file_name}".')
        shutil.copy(chapter.audio_file, new_file_name)
