alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''
  
Msg = input('Please enter a message: ').lower()

key = int(input('Enter a key (1-26): '))

for character in Msg:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = int((position + key) % 26)
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character
print('Your Orignal message is:', Msg)
print('Your new message is:', newMessage)