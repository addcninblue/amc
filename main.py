#!/bin/env python


def main():
    scores = getCounts()
    print(f'scores from {2016 - len(scores) + 1} to 2016')
    begin = int(input("begin: ")) - 2016 + len(scores) - 1
    end = int(input("end: ")) - 2016 + len(scores)
    numStart = int(input("Num to start at: ")) - 1
    numEnd = int(input("Num to end at: "))
    letter = input("letter (all): ")
    if letter == 'all':
        for i in ['A', 'B', 'C', 'D', 'E']:
            print(sum([y.count(i) for x in scores[begin:end]
                       for y in x[numStart:numEnd]]))
            # print(sum([x.count(i) for x in scores[begin:end]]))
    else:
        print(sum([x.count(letter) for x in scores[begin:end]]))


def getCounts():
    scores = []
    thisYear = []
    for index, line in enumerate(open('./12b', 'r')):
        if index % 27 == 0:
            continue
        elif index % 27 == 26:
            scores.append(thisYear)
            thisYear = []
        else:
            thisYear.extend(line[0])
    return scores


if __name__ == "__main__":
    main()
