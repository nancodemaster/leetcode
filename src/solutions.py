from typing import List


class Solutions:
    def removeElement(self, nums: List[int], val: int) -> int:
        """Question 27. Remove Elements. [Easy]
        https://leetcode.com/problems/remove-element/
        """
        k = 0
        j = 0
        # Two pointer method.
        for idx, num in enumerate(nums):
            if num == val:
                k += 1
            else:
                nums[j] = nums[idx]
                j += 1
        return len(nums) - k

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Question 14. Longest Common Prefix. [Easy]
        https://leetcode.com/problems/longest-common-prefix/
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        comm_len = 0
        min_len = []
        lut = dict(enumerate(strs[0]))
        for input_word in strs[1:]:
            comm_len = 0
            for idx, s in enumerate(input_word):
                lut_value = lut.get(idx)
                if lut_value is not None and s == lut_value:
                    comm_len += 1
                else:
                    break
            min_len.append(comm_len)
        return strs[0][:min(min_len)]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """Question 34. Find First and Last Position of Elements in list. [Medium]
        https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
        """
        s_ptr = 0
        e_ptr = len(nums)-1
        s_pos = -1
        e_pos = -1
        s_found = False
        e_found = False
        while s_ptr <= e_ptr:
            if not s_found:
                if nums[s_ptr] == target:
                    s_pos = s_ptr
                    s_found = True
                else:
                    s_ptr += 1
            if not e_found:
                if nums[e_ptr] == target:
                    e_pos = e_ptr
                    e_found = True
                else:
                    e_ptr -= 1
            if e_found and s_found:
                break
        return [s_pos, e_pos]


def main():
    s = Solutions()
    print(s.longestCommonPrefix(["cir", "car"]))


if __name__ == "__main__":
    main()
