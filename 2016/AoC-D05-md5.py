import md5

door_id = "uqwqemis"
door_code = ""
x = 0

##while True:
##    m = md5.new()
##    m.update(door_id+str(x))
##    hd = m.hexdigest()
##
##    #print door_id+str(x)
##    #print hd
##    
##    if hd[0:5] == '00000':
##        print hd
##        door_code += hd[5]
##        if len(door_code) == 8:
##            break
##    x += 1
##
##print door_code
    
door_code = {}
x = 0

while True:
    m = md5.new()
    m.update(door_id+str(x))
    hd = m.hexdigest()
    
    if hd[0:5] == '00000':
        position = str(hd[5])
        character = hd[6]
        
        if position.isdigit():
            if int(position) >= 0 and int(position) < 8:
                print hd, position, character

                if door_code.has_key(position):
                    print "position already filled"
                else:
                    door_code[position] = character

                if len(door_code) == 8:
                    break
    x += 1

print door_code
code = ""

for x in '01234567':
    code += door_code[x]

print code
