my_dict={'Alexander':2001,'Alexandra':2002,'Alex':2003}
print('Dic:',my_dict)
print('Existing value:',my_dict.get('Alexander'))
print('Not existing value:',my_dict.get('Ivan'))
my_dict.update({'Mira':2004,'Stef':2005})
print('Deleted value:',my_dict.pop('Alexandra'))
print('Modified dictionary:',my_dict)
Whitespace= 'ᅠ ᅠᅠ ᅠ'
print(Whitespace)
my_set={1,1,2,2,3,3,'Bob','Bob',(1,2,3),(1,2,3)}
print('Set:',my_set)
my_set.update({'Sokol',1905})
my_set.discard(1)
my_set.discard(2)
my_set.discard(3)
my_set.discard((1,2,3))
print('Modified set:',my_set)
