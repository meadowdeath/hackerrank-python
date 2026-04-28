def merge_the_tools(string, k):
    # your code goes here
    chunks = [string[i : i + k] for i in range(0, len(string), k)]
    for segment in chunks:
        unique_chars = "".join(dict.fromkeys(segment))
        print(unique_chars)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)