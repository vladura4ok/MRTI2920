def  max_of_brakets ( строка ):
    max_of_brakets  =  0
    list_of_brakets  = []
    для  i  в  строке :
        если  я  ==  "(" :
            max_of_brakets  + =  1
        elif  i  ==  ")" :
            list_of_brakets . добавить ( max_of_brakets )
            max_of_brakets  =  0
    вернуть  макс ( list_of_brakets )


def  raskukoz_op ( v , op ):
    v  =  v . replace ( '+ -' , '-' )
    v  =  v . заменить ( '-' , '+' )
    v1_splitted  =  v . сплит ( op )
    v1  = []
    для  i  в  v1_splitted :
        v1 . расширить ([ i , op ])
    v1  =  v1 [: - 1 ]
    вернуть  v1


def  raskukoz ( v ):
    res  =  raskukoz_op ( v , '*' )
    результат  = []
    для  элемента  в  разрешении :
        res1  =  raskukoz_op ( элемент , '/' )
        для  item1  в  res1 :
            res2  =  raskukoz_op ( элемент1 , '+' )
            для  item2  в  res2 :
                res3  =  raskukoz_op ( элемент2 , '-' )
                результат . продлить ( res3 )
    вернуть  результат


def  вычислить ( v_rask ):
    результат  =  v_rask [:]
    а  "*"  в  результате :
        index_of_first_op  =  результат . index ( "*" )
        a  =  float ( результат [ index_of_first_op  - 1 ]) *  float ( результат [ index_of_first_op  +  1 ])
        результат [ index_of_first_op  - 1 : index_of_first_op  +  2 ] = [ a ]
    в то время как  "/"  в  результате :
        index_of_first_op  =  результат . индекс ( "/" )
        a  =  float ( результат [ index_of_first_op  - 1 ]) /  float ( результат [ index_of_first_op  +  1 ])
        результат [ index_of_first_op  - 1 : index_of_first_op  +  2 ] = [ a ]
    а  "-"  в  результате :
        index_of_first_op  =  результат . index ( "-" )
        a  =  float ( результат [ index_of_first_op  - 1 ]) -  float ( результат [ index_of_first_op  +  1 ])
        результат [ index_of_first_op  - 1 : index_of_first_op  +  2 ] = [ a ]
    а  "+"  в  результате :
        index_of_first_op  =  результат . индекс ( "+" )
        a  =  float ( результат [ index_of_first_op  - 1 ]) +  float ( результат [ index_of_first_op  +  1 ])
        результат [ index_of_first_op  - 1 : index_of_first_op  +  2 ] = [ a ]
    вернуть  результат [ 0 ]


def  упрощать ( v ):
    brakets  =  max_of_brakets ( v )
    max_of_brakets2  =  0
    для  indx , i  в  enumerate ( v ):
        если  я  ==  "(" :
            max_of_brakets2  + =  1
        elif  i  ==  ')' :
            max_of_brakets2  - =  1
        если  max_of_brakets2  ==  brakets :
            перемена
    для  indx2 , i2  в  enumerate ( v [ indx :]):
        если  i2  ==  ")" :
            перемена
    indx2  + =  indx

    v_rask  =  raskukoz ( v [ indx + 1 : indx2 ])
    calced  =  вычислить ( v_rask )
    v  =  v [: indx ] +  str ( вычислено ) +  v [ indx2 + 1 :]
    вернуть  v


v  =  input ( 'Введите вычисление:' )

а  '('  в  v :
    v  =  упрощать ( v )

результат  =  вычислить ( раскукоз ( v ))
печать ( результат )
