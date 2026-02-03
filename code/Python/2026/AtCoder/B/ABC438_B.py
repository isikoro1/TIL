def main():
    N, M = map(int, input().split())
    S = input().strip() #stripは文字列の前後にある余計な空白や改行を消す
    T = input().strip()

    ans = 10**18

    for i in range(N - M + 1):
        total = 0
        for j in range(M):
            x = ord(T[j]) - ord('0')
            y = ord(S[i + j]) - ord('0')
            total += (y - x) % 10
        ans = min(ans, total)

    print(ans)

if __name__ == "__main__":
    main()
