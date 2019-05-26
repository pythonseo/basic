'''
创建演员表
'''
Fuyao_yanyuanbiao={}
Fuyao_yanyuanbiao['杨幂']={ '角色':'扶摇', '配音演员':'王潇倩'}
Fuyao_yanyuanbiao['阮经天']={'角色':'长孙无极', '配音演员':'马正阳'}
Fuyao_yanyuanbiao['刘奕君']={'角色':'齐镇', '配音演员':'刘奕君'}
Fuyao_yanyuanbiao['王劲松']={'角色':'长孙迥', '配音演员':'王劲松'}
Fuyao_yanyuanbiao['黄宥明']={'角色':'燕惊尘', '配音演员':'文森'}
Fuyao_yanyuanbiao['高瀚宇']={'角色':'江枫', '配音演员':'袁聪宇'}
Fuyao_yanyuanbiao['顾又铭']={'角色':'战北恒', '配音演员':'林强'}
Fuyao_yanyuanbiao['秦焰']={'角色':'周叔', '配音演员':'宣晓鸣'}
Fuyao_yanyuanbiao['蒋龙']={'角色':'小七', '配音演员':'苏尚卿'}
print('《扶摇》的演员表：{}'.format(Fuyao_yanyuanbiao))   #打印演员表
'''
打印杨幂饰演角色
'''
print('杨幂饰演的角色是：{}'.format(Fuyao_yanyuanbiao['杨幂']['角色']))
'''
创建字典备份
'''
Copy_Fuyao=Fuyao_yanyuanbiao.copy()   
'''
去除阮经天，替换为陈晓，并根据第二张图更新字典
'''
del Fuyao_yanyuanbiao['阮经天']
Fuyao_yanyuanbiao['陈晓']={'角色':'长孙无极', '配音演员':'马正阳'}
Fuyao_yanyuanbiao['张雅钦']={'角色':'雅兰珠', '配音演员':'吟良犬'}
Fuyao_yanyuanbiao['王鹤润']={'角色':'凤净梵', '配音演员':'蔡娜'}
Fuyao_yanyuanbiao['周莉葳']={'角色':'时岚', '配音演员':'张晗'}
Fuyao_yanyuanbiao['魏晖倪']={'角色':'简雪', '配音演员':'曹一茜'}
print('更新后的演员表为：{}'.format(Fuyao_yanyuanbiao))    #打印更新后的演员表

'''
打印出阮经天所在的演员字典中的演员名以及角色名，并统计一个有多少个角色。
'''
print('演员表中的演员:{}'.format(Fuyao_yanyuanbiao.keys()))
for juese in Fuyao_yanyuanbiao.values():
    print('演员表中的角色:{}'.format(juese['角色']))
print('《扶摇》一共有{}个角色'.format(len(Fuyao_yanyuanbiao)))
'''
重点描述一下杨幂主演的角色信息，扶摇
'''
fuyao_detail={'扶摇':{'喜欢她的男角色':['长孙无极','战北野','小七'],'去过的国家':['太渊','天权','天煞','璇玑']}}   #扶摇的详细信息
print('扶摇的详细信息：{}'.format(fuyao_detail))