import OKay

while True:
		text = input('OKay > ')
		if text.strip() == "": continue
		if text[0] == "#": continue
		result, error = OKay.khelo('<stdin>', text)

		if error: print(error.as_string())
		elif result:
			if len(result.elements) == 1:print(repr(result.elements[0]))
		else:
			print(repr(result))