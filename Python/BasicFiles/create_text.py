def create_file():
    with open("Basic_text.txt", "w+") as f:
        for i in range(24):
            f.write(f"HelloWorld!{i}\n")


def main():
    create_file()


if __name__ == "__main__":
    main()
