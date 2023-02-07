T = int(input())
for tc in range(1, 1+T):
	n = int(input())    
	
	def odd(n):
		mcri = (n+1)//2 - 1 # n = 5 ~ cri = 3

		lst = sorted(list(i for i in range(1, 1+n**2)), reverse=True) # 오리지널 리스트 정의
		mat = list([0]*n for _ in range(n)) # 매트릭스 정의
		idx=[1]+list(i-1 for i in range(1,n+1,2) if i != 1) # 인덱스 리스트 생성
	
		for itera,ida in enumerate(idx): # [1, 2, 4]
			if itera == 0:
				mat[mcri][mcri] = lst.pop(0)
				continue
			else:
				for i in range(ida):
					mat[mcri-(itera-1)+i][mcri-itera] = lst.pop(0)
				for i in range(ida):
					mat[mcri+itera][mcri-(itera-1)+i] = lst.pop(0)
				for i in range(ida):
					mat[mcri+(itera-1)-i][mcri+itera] = lst.pop(0)  # 두개의 리스트 동시에 덮어쓸 수 없음.
				for i in range(ida):
					mat[mcri-itera][mcri+(itera-1)-i] = lst.pop(0)
		return mat
		
	def even(n):
		center = [n//2-1, n//2] # n = 5 ~ cri = 3

		lst = sorted(list(i for i in range(1, 1+n**2)), reverse=True) # 오리지널 리스트 정의
		mat = list([0]*n for _ in range(n)) # 매트릭스 정의
		idx=[1]+[2]+list(i+1 for i in range(3,n+2,2)) # 인덱스 리스트 생성
	
		for itera,ida in enumerate(idx): # [1, 2, 4]
			if n <= 2:
				for i in range(1,-1,-1):
					for j in range(2):
						mat[i][j] = lst.pop(0)
				break	
			if itera == 0:
				mat[center[0]][center[1]] = lst.pop(0)
				continue
			else:
				for i in range(ida):
					mat[center[0]+(itera-1)-i][center[1]+itera] = lst.pop(0)  # 두개의 리스트 동시에 덮어쓸 수 없음.
				for i in range(ida):
					mat[center[0]-itera][center[1]+(itera-1)-i] = lst.pop(0)
				for i in range(ida):
					mat[center[0]-(itera-1)+i][center[1]-itera] = lst.pop(0)
	
		return mat

	if n % 2: 
		ans = odd(n)
	else:
		ans = even(n)

	for lst in ans:
		print(*lst)