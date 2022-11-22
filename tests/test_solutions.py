import pytest

from src.solutions import Solutions


class TestSolutions:
    @pytest.mark.parametrize("nums, val, k",
                             [([3, 2, 2, 3], 2, 2),
                              ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5)
                              ])
    def test_remove_elements(self, nums, val, k):
        s = Solutions()
        res = s.removeElement(nums, val)
        assert res == k, f"Wrong answer, expected k to be {k} but got {res}."

    @pytest.mark.parametrize("strs, str",
                             [(["flower", "flow", "flight"], "fl"),
                              (["dog", "racecar", "car"], ""),
                              (["a"], "a"),
                              (["aaa", "aa", "aaa"], "aa"),
                              (["cir", "car"], "c")])
    def test_longest_common_prefix(self, strs, str):
        s = Solutions()
        res = s.longestCommonPrefix(strs)
        assert res == str, f"Wong answer. Expected {str} but got {res}."
