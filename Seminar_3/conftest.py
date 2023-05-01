import random
import string
import subprocess
import pytest
import yaml

from checkout import checkout_positive

# folder_in = "/home/user/tst/file"
# folder_out = "/home/user/tst/out"
# folder_ext = "/home/user/tst/ext"
# folder_ext2 = "/home/user/tst/ext2"
# folder_badarx = "/home/user/tst/badarx"

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return checkout_positive(
        "mkdir {} {} {} {} {}".format(data["folder_in"], data["folder_out"], data["folder_ext"], data["folder_ext2"],
                                      data["folder_badarx"]), "")


@pytest.fixture()
def clear_folders():
    return checkout_positive(
        "rm -rf {}/* {}/* {}/* {}/* {}/*".format(data["folder_in"], data["folder_out"], data["folder_ext"],
                                                 data["folder_ext2"], data["folder_badarx"]), "")


@pytest.fixture()
def make_files():
    list_off_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout_positive(
                "cd {}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"], filename),
                ""):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout_positive("cd {}; mkdir {}".format(data["folder_in"], subfoldername), ""):
        return None, None
    if not checkout_positive(
            "cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"], subfoldername,
                                                                                      testfilename), ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture()
def make_bad_arx(make_folders, clear_folders, make_files):
    checkout_positive("cd {}; 7z a {}/badarx.7z".format(data["folder_in"], data["folder_badarx"]),
                      "Everything is Ok"), "Test1 Fail"
    return checkout_positive("truncate -s 1 {}/badarx.7z".format(data["folder_badarx"]), ""), "Test1 Fail"
