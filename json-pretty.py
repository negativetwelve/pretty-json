import sys
import json

def jsonify(text):
    return json.dumps(text, sort_keys=True, indent=4, separators=(',', ': '))

def main():
    print jsonify(json.loads(sys.stdin.read()))

if __name__ == "__main__":
    main()
