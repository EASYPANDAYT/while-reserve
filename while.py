#counter = 0
#while counter < 10 :
 #   counter += 1 #инкремент
    #print (counter, 'итерация')
  #  continue
#    break
name = 'Илья Муромец'


way_left = False
way_center = False
way_right = False
while way_left == False and way_center == False and way_right == False:
    print (name, 'приехал к камню, на нем надпись :')
    print ('Налево поехать - убитым быть,')
    print ('Прямо поехать - женатым быть,')
    print ('Направо поехать - богатым быть.')

    way = input ('В какую сторону поехать? ')
    if way == 'налево' :
        if way_left == False :
            print (name, 'убит')
            way_left == True
        else:
            print(name, 'уже был на левой дороге.')
    elif way == 'направо':
        if way_right == False :
            print (name, 'богат')
            way_right == True
    elif way == 'прямо':
        if way_center == False :
            print (name, 'женат')
            way_center == True
break
print ('Игра окончена')





