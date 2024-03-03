def printPyramid(nums: int) -> None:
    for i in range(nums):
        for j in range(0, i + 1):
            print("*", end="")
        print()


def main():
    target = 4
    printPyramid(target)


if __name__ == "__main__":
    main()
