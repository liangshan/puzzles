# -*- coding: utf-8 -*-
import sys
from getopt import getopt

def package(items,limit):
  print "Items list:"
	for i in items:
		item = items.get(i)
		print "%s weight:%s value:%s" % (item['n'],item['w'],item['v'])

	print "weight limit:%s" % limit	

	N = len(items)
	F = [[0 for col in range(limit+1)] for row in range(N+1)]
	P = [[0 for col in range(limit+1)] for row in range(N+1)]
	result = []

	print "stealing..."
	for i in range(1,N+1):
		for j in range(0,limit+1):
			if j >= items.get(i).get('w'):
				if F[i-1][j-items.get(i).get('w')] + items.get(i).get('v') > F[i-1][j]:
					F[i][j] = F[i-1][j-items.get(i).get('w')] + items.get(i).get('v')
					P[i][j] = 1
				else:
					F[i][j] = F[i-1][j]

	print "max value:%s" % F[N][limit]

	i = N
	j = limit 
	while i > 0:
		if P[i][j] == 1:
			result.append(i)
			j = j-items.get(i).get('w')
		
		i = i-1

	print "Items picked:"
	for i in result[::-1]:
		print items.get(i)['n']

if __name__ == '__main__':
    items = {1:{'n':'A','w':240,'v':5000},2:{'n':'B','w':200,'v':4300},3:{'n':'C','w':100,'v':8000}}
    weight = 500

    opts, args = getopt(sys.argv[1:], 'w:', ['weight='])
    for o, a in opts:
        if o in ('-w', '--weight'):
            weight = int(a)
        else:
            pass
            
    package(items, weight)
