class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        st = []
        for p, s in sorted(pairs)[::-1]:
            t = (target-p)/s
            if st and t <= st[-1]:
                continue
            st.append(t)
        return len(st)

