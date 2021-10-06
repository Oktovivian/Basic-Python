def mystery74(n):
	if n <= 0:
		return 5
	else:
		return mystery74(n - 2) + 3
      