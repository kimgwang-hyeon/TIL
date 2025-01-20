N = int(input())
inputs = list(map(int, input().split()))

median_loc = (N-1)//2
inputs.sort()
print(inputs[median_loc])
