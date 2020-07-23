import sys, os, re, itertools, json

ignored = ['.git', 'node_modules', 'bower_components', '.sass-cache', '.png', '.ico', '.mov', '.jpeg', 'jpg', '.avi', '.gif']
ruleFile = "./pattern.json"
api_key_min_entropy_ratio = 0.5
api_key_min_length = 7
with open(ruleFile) as f:
  rule = json.load(f)

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)

def token_is_api_key(token):
	if len(token) < api_key_min_length:
		return (False, '')
	entropy = 0
	for a, b in pairwise(list(token)):
		if not ((str.islower(a) and str.islower(b)) or (str.isupper(a) and\
			str.isupper(b)) or (str.isdigit(a) and str.isdigit(b))):
			entropy += 1
	return (float(entropy) / len(token) > api_key_min_entropy_ratio, float(entropy) / len(token))

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
	f = open(pathToFile)
	number = 1
	for line in f:
		result = detect(line)
		if result[0]:
			print("\n\n")
			# print('\033[1m' + path_to_file + ' : Line ' + str(number) + ' : Entropy ' + str(result[1]) + '\033[0m')
			print("Path: " + pathToFile + ' : Line ' + str(number) + "\nReason: "+ str(result[0]) + "\n" + str(result[1]))
			# print(line)
		number += 1

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
	if len(sys.argv) == 1:
		print('Please specify path.')
		sys.exit(0)

	path = str(sys.argv[1])
	print('Scanning directory: ' + path)
	print('Ignoring: ' + str(ignored))

	scanDir(path)