from Seminar_2.checkout import checkout

path_dir = "/home/user/tst"
path_arx = "/home/user/arx2.7z"


def test_step6():
    assert checkout("cd {}; 7z l{}".format(path_dir, path_arx), "test1.sh"), "Test6 Fail"


def test_step7():
    assert checkout("cd {}; 7z x{}".format(path_dir, path_arx, path_dir), "Extracting"), "Test7 Fail"
