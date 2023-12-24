import base64
import re
import py_mini_racer

#totally pasted from another repo ofc,im just trying to fill my github
def _shiftBits(solution,sessionToken):
	decodedToken = base64.b64decode(sessionToken).decode('utf-8', 'strict')
	solChars = [ord(s) for s in solution]
	sessChars = [ord(s) for s in decodedToken]
	return "".join([chr(sessChars[i] ^ solChars[i % len(solChars)]) for i in range(len(sessChars))])

def solveChallenge(text,sessionToken):
		text = text.replace('\t', '', -1).encode('ascii', 'ignore').decode('utf-8')
		text = re.split("[{};]", text)
		replaceFunction = "return message.replace(/./g, function(char, position) {"
		rebuilt = [text[1] + "{", text[2] + ";", replaceFunction, text[7] + ";})};", text[0]]

		jsEngine = py_mini_racer.MiniRacer()
		solution = jsEngine.eval("".join(rebuilt))

		return _shiftBits(solution,sessionToken)


