import solve


def test_parse_substitutions():
    assert solve.parse_substitutions([" -> "]) == [['', '', 0]]
    assert solve.parse_substitutions([" ->. "]) == [['', '', 1]]
    assert solve.parse_substitutions(["ab ->. a"]) == [['ab', 'a', 1]]
    assert solve.parse_substitutions([" ->. a"]) == [['', 'a', 1]]
    assert solve.parse_substitutions([" ->. abc", "zz ->. z"]) == [['', 'abc', 1], ['zz', 'z', 1]]


def test_read_from_file():
    assert solve.read_from_file(0) == ['ccabab\n', ['ba -> ab\n', 'ca -> ac\n', 'cb -> bc\n']]
    assert solve.read_from_file(1) == ['aababab\n', ['ab ->\n', 'a -> b\n']]
    assert solve.read_from_file(2) == ['aaa\n', ['b ->. a\n', 'a -> b\n']]
    assert solve.read_from_file(3) == ['|||||||||\n', ['||| ->\n', '|| ->.\n', '| ->.\n', ' ->. |']]


def test_apply_scheme():
    assert solve.apply_scheme([['ba', 'ab', 0], ['ca', 'ac', 0], ['cb', 'bc', 0]], "ccabab") == "aabbcc"
    assert solve.apply_scheme([['ab', '', 0], ['a', 'b', 0]], "aababab") == "b"
    assert solve.apply_scheme([['b', 'a', 1], ['a', 'b', 0]], "aaa") == "aaa"
    assert solve.apply_scheme([['|||', '', 0], ['||', '', 1], ['|', '', 1], ['', '|', 1]], "|||||||||") == "|"


def test_apply_scheme_once():
    assert solve.apply_scheme_once([['ba', 'ab', 0], ['ca', 'ac', 0], ['cb', 'bc', 0]], "ccabab") == ['ccaabb', 0]
    assert solve.apply_scheme_once([['ab', '', 0], ['a', 'b', 0]], "aababab") == ['aabab', 0]
    assert solve.apply_scheme_once([['b', 'a', 1], ['a', 'b', 0]], "aaa") == ['baa', 0]
    assert solve.apply_scheme_once([['|||', '', 0], ['||', '', 1], ['|', '', 1], ['', '|', 1]], "|||||||||") == ['||||||', 0]


def test_apply_substitution():
    assert solve.apply_substitution(['ad', 'a', 0], "cada") == "caa"
    assert solve.apply_substitution(['oa', '', 0], "alsoalgo") == "alslgo"
    assert solve.apply_substitution(['aa', 'bb', 0], "aaaa") == "bbaa"
    assert solve.apply_substitution(['or', '', 0], "forward") == "fward"
    assert solve.apply_substitution(['d', 'a', 0], "daaaa") == "aaaaa"
    assert solve.apply_substitution(['rr', 'r', 0], "error") == "eror"
    assert solve.apply_substitution(['', 'aaa'], "wwww") == "aaawwww"


def test_is_applicable():
    assert solve.is_applicable(['ad', 'a', 0], "cada")
    assert solve.is_applicable(['oa', '', 0], "alsoalgo")
    assert solve.is_applicable(['aa', 'bb', 0], "aaaa")
    assert solve.is_applicable(['or', '', 0], "forward")
    assert solve.is_applicable(['d', 'a', 0], "daaaa")
    assert solve.is_applicable(['rr', 'r', 0], "error")
    assert solve.is_applicable(['', 'aaa'], "wwww")
    assert not solve.is_applicable(['b', 'aaa'], "wwww")
    assert not solve.is_applicable(['r', 'a'], "asdasd")
    assert not solve.is_applicable(['qwe', 'aaa'], "st")
    assert not solve.is_applicable(['fward', 'aaa'], "cool")


test_parse_substitutions()
test_apply_scheme()
test_read_from_file()
test_apply_scheme_once()
test_apply_substitution()
test_is_applicable()
