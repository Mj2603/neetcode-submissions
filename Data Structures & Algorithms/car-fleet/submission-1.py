class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
           pair= [[pos, (target-pos)/s] for pos, s in zip(position, speed)]
           pair.sort(reverse=True)

           stack= []

           for p, t in pair:
            if not stack or t> stack[-1]:
                stack.append(t)
           return len(stack) 


