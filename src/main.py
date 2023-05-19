from customdecorators import ttime, cache, loginfo


@cache
#@loginfo
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@ttime
def main():
    print(fibonacci(350))

if __name__ == "__main__":
    main()