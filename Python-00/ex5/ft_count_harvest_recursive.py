def ft_count_harvest_recursive(i=1, count=0):
    if count == 0:
        count = int(input("Days until harvest: "))
    if i <= count:
        print(f"Day {i}")
        ft_count_harvest_recursive(i + 1, count)
    if i == count:
        print("Harvest time!")
        return 1
