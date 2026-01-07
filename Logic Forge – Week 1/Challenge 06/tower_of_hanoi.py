N=int(input())
def towerOfHanoi(N, from_rod, to_rod, aux_rod):
    if N == 0:
        return
    towerOfHanoi(N - 1, from_rod, aux_rod, to_rod)
    print(f"Move disk {N} from {from_rod} to {to_rod}")
    towerOfHanoi(N - 1, aux_rod, to_rod, from_rod)
towerOfHanoi(N, "A", "C", "B")
