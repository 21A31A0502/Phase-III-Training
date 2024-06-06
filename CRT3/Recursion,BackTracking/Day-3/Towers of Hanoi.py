# Problem link:
#https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

# Below function is responsible for moving 
# n discs from src to dest using extra as temp space
def moveAllDiscs(n, src, extra, dest):
    if n == 1:
        print("Move 1st disc from", src, "to", dest)
        return 
    # Moving all (n - 1) discs from src to extra 
    # using dest as extraSpace
    moveAllDiscs(n - 1, src, dest, extra)
    print("Move", n, "th disc from", src, "to", dest)
    moveAllDiscs(n - 1, extra, src, dest)

moveAllDiscs(4, "source", "extraSpace", "destination")
print("\n\n\n\n\n")