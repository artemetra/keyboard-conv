
eng_to_rus = {
	r"q": "й",
	r"w": "ц",
	r"e": "у",
    r"r": "к",
    r"t": "е",
    r"y": "н",
	r"u": "г",
	r"i": "ш",
	r"o": "щ",
	r"p": "з",
	r"[": "х",
	r"]": "ъ",
	r"a": "ф",
	r"s": "ы",
	r"d": "в",
	r"f": "а",
	r"g": "п",
	r"h": "р",
	r"j": "о",
	r"k": "л",
	r"l": "д",
	r";": "ж",
	r"'": "э",
	r"z": "я",
	r"x": "ч",
	r"c": "с",
	r"v": "м",
	r"b": "и",
	r"n": "т",
	r"m": "ь",
	r",": "б",
	r".": "ю"
}

if __name__ == '__main__':
    results = open("trans-keyboard rus eng conv.txt", 'w', encoding='utf-8')

    with open("trans-keyboard rus eng.txt", 'r', encoding='utf-8') as orig:
        num = 0
        for line in orig:
            print(f"Parsing line #{num}", end='\r')
            results.write(
                ''.join([eng_to_rus.get(tr.lower(), tr.lower()) for tr in line])
            )
            num += 1
            print('', end='', flush=True)
        
        
    print("\nFinished")
    results.close()
    
            
