from vectordb import insert_data


def main():
    text_file = open("resources/data.txt", "r")
    lines = text_file.readlines()
    insert_data(lines)

if __name__ == '__main__':
    main()
