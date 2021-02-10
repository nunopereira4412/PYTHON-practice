vowels = ['a', 'e', 'i', 'o', 'u']

def pigLatin(word):
	firstLetter = word[0]
	for vowel in vowels:
		if firstLetter == vowel:
			return word + 'ay'
	return word[1:] + firstLetter + 'ay'

def pigLatin2(word):
	firstLetter = word[0]
	if firstLetter in 'aeiou':
		return word + 'ay'
	return word[1:] + firstLetter + 'ay'

print(pigLatin('apple'))
print(pigLatin('word'))


print(pigLatin2('apple'))
print(pigLatin2('word'))



