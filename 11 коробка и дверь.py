"""
11. Имеется коробка со сторонами А*В*С.
Определить, пройдет ли она в дверь с размером М*К
"""
dk  =  int ( input ( "Длинна коробки = " ))
shk  =  int ( input ( "Ширина коробки = " ))
vk  =  int ( input ( "Высота коробки = " ))
m  =  int ( input ( "Ширина двери = " ))
vd  =  int ( input ( "Высота двери = " ))

if (( vk  <=  vd  and  shk  <=  vd )
    or ( vk  <=  vd  and  dk  <=  vd )
        or ( dk  <=  vd  and  shk  <=  vd )):
    print ( "Коробка пройдет в дверь" )
else :
    print ( "Коробка не пройдет в дверь" )
