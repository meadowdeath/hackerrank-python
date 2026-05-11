# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    k = int(input())
    rooms = map(int, input().split())

    seen_rooms = set()
    repeated_rooms = set()

    for person in rooms:
        if person not in seen_rooms:
            seen_rooms.add(person)
        else:
            repeated_rooms.add(person)

    print(list(seen_rooms.difference(repeated_rooms))[0])
