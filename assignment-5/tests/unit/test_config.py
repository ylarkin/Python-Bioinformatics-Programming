"""
testing of Config module
"""
import sys
from assignment5.config import get_directory_for_unigene, get_extension_for_unigene, get_keywords_for_hosts
sys.path.insert(0, 'assignment5/assignment5')
# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_filehandle_for_OSError
# " doesn't conform to snake_case naming style"
# pylint: disable=C0103
# io_utils Program only
# test file for writing or reading respective to test


def test_get_directory_for_unigene():
    # return config module global variable directory_for_unigene
    assert get_directory_for_unigene() is "assignment5_data"


def test_get_extension_for_unigene():
    # return config module global variable file_ending_for_unigene
    assert get_extension_for_unigene() is "unigene"


def test_get_keywords_for_hosts():
    host_keywords = get_keywords_for_hosts()
    # assert each object variable to their string value
    # assert each key to its value object
    bos_tarus = "Bos_tarus"
    equus_caballus = "Equus_caballus"
    homo_sapiens = "Homo_sapiens"
    mus_musculus = "Mus_musculus"
    ovis_aries = "Ovis_aries"
    rattus_norvegicus = "Rattus_norvegicus"
    assert host_keywords["bos taurus"] is bos_tarus, "Key Value pair incorrect"
    assert host_keywords["cow"] is bos_tarus, "Key Value pair incorrect"
    assert host_keywords["cows"] is bos_tarus, "Key Value pair incorrect"
    assert host_keywords["equus caballus"] is equus_caballus, "Key Value pair incorrect"
    assert host_keywords["horse"] is equus_caballus, "Key Value pair incorrect"
    assert host_keywords["horses"] is equus_caballus, "Key Value pair incorrect"
    assert host_keywords["homo sapiens"] is homo_sapiens, "Key Value pair incorrect"
    assert host_keywords["human"] is homo_sapiens, "Key Value pair incorrect"
    assert host_keywords["humans"] is homo_sapiens, "Key Value pair incorrect"
    assert host_keywords["mus musculus"] is mus_musculus, "Key Value pair incorrect"
    assert host_keywords["mouse"] is mus_musculus, "Key Value pair incorrect"
    assert host_keywords["mice"] is mus_musculus, "Key Value pair incorrect"
    assert host_keywords["ovis aries"] is ovis_aries, "Key Value pair incorrect"
    assert host_keywords["sheep"] is ovis_aries, "Key Value pair incorrect"
    assert host_keywords["sheeps"] is ovis_aries, "Key Value pair incorrect"
    assert host_keywords["rattus norvegicus"] is rattus_norvegicus, "Key Value pair incorrect"
    assert host_keywords["rat"] is rattus_norvegicus, "Key Value pair incorrect"
    assert host_keywords["rats"] is rattus_norvegicus, "Key Value pair incorrect"
