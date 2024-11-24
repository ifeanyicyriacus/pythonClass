
letter = input("Input an alphabet: ")
match letter:
	case "a" | "e" | "i" | "0" | "u":
		print("Input letter is a Vowel")
	case "b" | "c" | "d" | "f" | "g" | "h" | "j" | "k" | "l" | "m" | "n" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z":
		print("Input letter is a Consonant")
