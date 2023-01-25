import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from daisy_renamer.daisy_renamer import get_audiofile_from_smil, get_sub_smil


def test_get_audiofile_from_smil() -> None:
    test_smil = "tests/resources/test0002.smil"
    filename = get_audiofile_from_smil(test_smil)
    assert filename == "chapter_1.mp3"


def test_get_audiofile_from_smil_error() -> None:
    test_smil = "tests/resources/test_no_audio.smil"
    filename = get_audiofile_from_smil(test_smil)
    assert filename == ""


def test_get_sub_smil() -> None:
    test_smil = "tests/resources/master.smil"
    sub_smil = get_sub_smil(test_smil)
    assert len(sub_smil) == 3
    assert sub_smil[-1] == ("Fin de l'enregistrement", "test0003.smil")
