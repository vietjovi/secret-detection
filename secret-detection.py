import sys, os, re, itertools, json, getopt

ignored = ['.git', 'node_modules', 'bower_components', '.sass-cache', '.png', '.ico', '.mov', '.jpeg', 'jpg', '.avi', '.gif', '.apk', '.exe', '.jar', '.dmg', '.pdf', '.ipa', '.svg']
ruleFile = "./pattern.json"
api_key_min_entropy_ratio = 0.5
api_key_min_length = 7

def help():
	print("Usage: "+sys.argv[0]+" [OPTIONS]\n")
	print("\t-r --rule /path/to/rules\t\timport regexes from json file")
	print("\t-p --path /path/to/source_code/\t\tPath to scan")
	print("Example:")
	print("\tpython3 %s --rule pattern.json --path test/"%(sys.argv[0]))

def detect(line):
	for (k,v) in rule.items():
		# print(k,v)
		result = re.findall(v, line)
		if(len(result) > 0):
			# print(k,v)
			# print(len(result))
			return (k, result[0])
			# input()

	# for token in re.findall(r"[\w]+", line):
	# 	result = token_is_api_key(token)
	# 	if result[0]:
	# 		return (True, result[1])
	return (False, '')

def scanFile(pathToFile):
	try:
		f = open(pathToFile)
		number = 1
		try:
			for line in f:
				result = detect(line)
				if result[0]:
					print("~~~~~~~~~~~~~~~~~~~~~")
					# print('\033[1m' + path_to_file + ' : Line ' + str(number) + ' : Entropy ' + str(result[1]) + '\033[0m')
					print("Filepath: " + pathToFile + ' : Line ' + str(number) + "\nReason: "+ str(result[0]) + "\n\n" + str(result[1]))
					print("~~~~~~~~~~~~~~~~~~~~~\n\n")
					# print(line)
				number += 1
		except:
			pass
	except:
		pass

def scanDir(path):
	for dirpath, _, filenames in os.walk(path):
		for name in filenames:
			if name[0] == '.':
				# ignore hidden files
				continue
			fullpath = os.path.join(dirpath, name)
			skip = False
			for ignore in ignored:
				if ignore in fullpath:
					skip = True
			if not skip:
				scanFile(fullpath)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		help()
		sys.exit(0)
	try:
		opts,args = getopt.getopt(sys.argv[1:],'r:p:',['rule=','path='])
	except Exception as e:
		print(e)
		help()
		sys.exit(0)
		print(opts)
	for o,a in opts:
		if o in ('-r','--rule'):ruleFile = a
		if o in ('-p','--path'):path = a

	with open(ruleFile) as f:
  		rule = json.load(f)
	# print('Scanning directory: ' + path)
	# print('Ignoring: ' + str(ignored))

	scanDir(path)