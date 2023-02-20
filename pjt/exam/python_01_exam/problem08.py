# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    rst_char = ''
    for char in word:
        if ord(char) >= 97:
            if ord(char) + n <= 122:
                rst_char += chr(ord(char) + n)
            else:
                rst_char += chr(ord(char) + n - 26)
        else:
            if ord(char) + n <= 90:
                rst_char += chr(ord(char) + n)
            else:
                rst_char += chr(ord(char) + n - 26)
    return rst_char
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
