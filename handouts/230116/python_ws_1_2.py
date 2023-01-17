total_files = int(input("게시글의 총 갯수를 입력하시오 : "))
files_in_page = int(input("한 페이지에 필요한 게시글 수를 구하시오 : "))

total_pages = total_files / files_in_page
print(total_pages)

