from  graphIO import *
from basicgraphs import graph


def sortlist(_l):
	array = []
	for i in range(len(_l)):
		array.append([len(_l[i].V()), len(_l[i].E())])
	print(array)
	returnarray = []
	i = 0
	temp = 1
	while i < len(array)-1: #for i in range(len(array)-1):
		temparray = []
		temparray.append(_l[i])
		for g in range(i+1,len(array)):
			if array[g][0] == array[i][0] and array[g][1] == array[i][1]:
				temparray.append(_l[g])
				temp += 1
		returnarray.append(temparray)
		i += temp
		temp = 0
	print(returnarray)

G = loadgraph('examplegraph.gr')
H = loadgraph('examplegraph.gr')
J = loadgraph('examplegraph.gr')
T = loadgraph('examplegraph2.gr')
Q = loadgraph('examplegraph2.gr')

blaat = [T]


def colorrefine(_l):
	colorarray = [[] for x in range(len(_l[0].V()) + len(_l)*len(_l[0].V()))]
	counter = len(_l[0].V())
	for elem in _l:
		for v in elem.V():
			v.colornum = v.deg()
	i = 0
	notfinished = True
	listshit = _l.copy()
	oldgraph = listshit[0]
	while notfinished:
		for v in range(len(_l[0].V())):
			buur = []
			for n in oldgraph[v].nbs():
				buur.append(n.colornum)
			buur.sort()
			print(buur)
			found = False
			for i in range(len(_l[0].V()), len(colorarray)):
				if colorarray[i] == buur:
					_l[0][v].colornum = i
					found = True
					break
			if not found:
				colorarray[counter] = buur
				_l[0][v].colornum = counter
				counter += 1
		if _l[0] == oldgraph:
			notfinished = False
		else:
			oldgraph = _l[0]
	print(colorarray)
	print(_l[0])
	for v in _l[0].V():
		print(v.colornum)


colorrefine(blaat)
