import sys
import os

def main():

    if len(sys.argv) == 2:
        filepath = sys.argv[1]
    else:
        print("Expects one argument of file path!")
        sys.exit()

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    count = 0
    total = 0
    with open(filepath) as fp:
        total = sum(1 for line in fp)

    with open(filepath) as fp:
        for line in fp:
            count+=1
            line = line.strip()
            
            query_words = ["SELECT", "FROM", "WHERE", "LIMIT", "ORDER BY", "AND", "OR"]
            first_word = line.split()[0]

            if first_word not in query_words:
                output = "\t'{} '".format(line)
            else:
                output = "'{} '".format(line)

            if count != total:
                output += " +"

            print(output)

if __name__ == '__main__':
    main()
