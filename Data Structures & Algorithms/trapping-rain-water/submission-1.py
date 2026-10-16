class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height)-1

        mx_l, mx_r = height[l], height[r]

        res = 0

        while l < r:
            if mx_l < mx_r:
                l+=1
                mx_l = max(mx_l, height[l])
                res+=(mx_l-height[l])

            else:
                r-=1
                mx_r = max(mx_r, height[r])
                res+=(mx_r-height[r])

        return res