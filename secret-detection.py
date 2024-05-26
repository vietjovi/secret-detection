import sys, os, re, itertools, json, getopt

##############################
# Author: vietjovi@gmail.com #
##############################

ignored = ['node_modules', 'bower_components', '.sass-cache', '.png', '.ico', '.mov', '.jpeg', 'jpg', '.avi', '.gif', '.apk', '.exe', '.jar', '.dmg', '.pdf', '.ipa', '.svg']
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
        result = re.findall(v, line, re.IGNORECASE)
        if(len(result) > 0):
            return (k, result[0])

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
                    print("Filepath: " + pathToFile + ' : Line ' + str(number) + "\nReason: "+ str(result[0]) + "\n\n" + str(result[1]))
                    print("~~~~~~~~~~~~~~~~~~~~~\n\n")
                number += 1
        except:
            pass
    except:
        pass

def scanDir(path):
    if os.path.isfile(path):
        scanFile(path)
        return True
    for dirpath, _, filenames in os.walk(path):
        for name in filenames:
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
