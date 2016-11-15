#!/usr/bin/env python3
import os
import sys
import json
import html

if len(sys.argv) < 4:
	print("usage: " + sys.argv[0] + " <from> <to> <your_uin>" + """
to represent a group, use "gid,g". (e.g. 123456,g).
to represent a user, use "uid,u". (e.g 123456,u)
you need to specify your own id, otherwsie you will always be the route.
	""") 
	exit(1)

route_map = {}
unames = {}
nodes = 0

ignores = []
if(os.environ.get('IGNORES')): ignores = (os.environ.get('IGNORES') + ' ').split(' ')

for group in os.listdir('save/groups'):
	gid = str(group.split('.')[0]) + ",g"
	route_map[gid] = []
	for mem in json.loads(open('save/groups/' + group).read())['mems']:
		uin = str(mem['uin']) + ",u"
		unames[mem['uin']] = mem['nick']
		if not route_map.get(uin): route_map[uin] = []
		if mem['uin'] != int(sys.argv[3]) and gid not in ignores and uin not in ignores:
			route_map[gid].append(uin)
			route_map[uin].append(gid)
			nodes += 2

def bfs(graph, start, end):
	visited = []
	visited.append([start])
	while visited:
		path = visited.pop(0)
		node = path[-1]
		if node == end:
			return path
		for adjacent in graph.get(node, []):
			new_path = list(path)
			new_path.append(adjacent)
			visited.append(new_path)

def getName(obj):
	objtype = obj.split(',')[1]
	objval = obj.split(',')[0]
	if objtype == 'u': return unames[int(objval)] + "(" + obj + ")";
	groups_obj = json.loads(open('save/groups.json').read())
	groups_lst = groups_obj['create'] + groups_obj['join'] + groups_obj['manage']
	for group in groups_lst:
		if group['gc'] == int(objval): return html.unescape(group['gn']) + "(" + obj + ")"
	return obj;

print(str(len(os.listdir('save/groups'))) + " group(s), " + 
      str(len(unames)) + " user(s), " + 
      str(len(route_map)) + " node(s), " + 
      str(nodes) + " route(s)." )

route = bfs(route_map, sys.argv[1], sys.argv[2])
for obj in route[:-1]: print(getName(obj), end=' -> ')
print(getName(route[-1]))
