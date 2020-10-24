leet = ""
data = 'leet (or "1337"), also known as eleet or leetspeak, is a system of modified spellings used primarily on the Internet. It often uses character replacements in ways that play on the similarity of their glyphs via reflection or other resemblance. Additionally, it modifies certain words based on a system of suffixes and alternate meanings. There are many dialects or linguistic varieties in different online communities.'
leet_dic = {'a' : '@' , 'd' : '6' , 'e' : '3' , 'l' : '1' , 'o' : '0' , 'g' : '9' , 's' : '5' ,'t' : '7','A' : '4','T' : '7','B' : '8','z' : '2','Z' : '2','S' : '$'}
for i in data:
	if i in leet_dic:
		data = data.replace(i,leet_dic[i])
print(data)