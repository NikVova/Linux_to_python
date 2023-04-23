from Seminar_2.checkout import checkout

path_dir = "/home/user/tst"
path_arx = "/home/user/arx1"



def test_step1():
    assert checkout("cd {}; 7z a {}".format(path_dir, path_arx), "Everything is Ok"), "Test1 Fail"


def test_step2():
    assert checkout("cd {}; 7z u {}".format(path_dir, path_arx), "Everything is Ok"), "Test1 Fail"

# def test_step3():
#     assert checkout("cd {}; 7z d {}".format(path_dir, path_arx), "Everything is Ok"), "Test1 Fail"
