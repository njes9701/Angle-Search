
import math
import json

PLUGIN_METADATA = {
	'id': 'angle_search',
	'version': '1.0.0',
	'name': 'angle_searc',
	'author': ['NJ'],
	'link': 'https://github.com/njes9701/Angle-Search'
}

def inputXY(x, z, x1, z1,  server):
    dx = math.fabs(x-x1)
    dz = math.fabs(z-z1)
    qt = quadrant(x, z, x1, z1 )
    d = math.sqrt(math.pow(dx,2)+math.pow(dz,2))
    text =['§e距離=§a{}格§r'.format(float(round(d,2)))]
    server.execute('tellraw @a ' + json.dumps(text))
    angle = math.atan(weird_division(dx,dz))*180/math.pi
    output(qt,angle,server)
    
def weird_division(n, d):
    return n / d if d else 0    
  

def quadrant(x, z, x1, z1):
    dx = x1-x
    dz = z1-z
    if dx>0 and dz>0:     
        return 1
    if dx<0 and dz>0:
        return 2
    if dx<0 and dz<0:
        return 4
    if dx>0 and dz<0:
        return 3
    if dx==0 and dz>0:
        return 5
    if dx>0 and dz==0:
        return 6
    if dx==0 and dz<0:
        return 7
    if dx<0 and dz==0:
        return 8      

def  output(qt,angle,server):
    if qt==1:
        textot(-angle,server)
    elif qt==2:
        textot(angle,server)
    elif qt==3:
        textot(angle-180,server)
    elif qt==4:
        textot(180-angle,server)
    elif qt==5:
        textot(0,server)
    elif qt==6:
        textot(-90,server)
    elif qt==7:
        textot(180,server)
    elif qt==8:
        textot(90,server)

def textot (angle,server):
    text =['§e方位=§a{}度§r'.format(float(round(angle,2)))]
    server.execute('tellraw @a ' + json.dumps(text))

def on_info(server, info):
      if info.is_player:
        if info.content.startswith('!!goto'):
            cmdList = info.content.split(' ')
            cmdLen = len(cmdList)
            if cmdLen == 1:
                server.say(helpmessage)
            elif cmdLen == 5:
                try:
                    inputXY(int(cmdList[1]), int(cmdList[2]), int(cmdList[3]), int(cmdList[4]),  server)
                except:server.say('§4invalid literal for int() with base 10§r')
            else:
                server.say('§4錯誤格式§r')

helpmessage = '''--------查詢座標方位角度--------
§6幫助你更快的找到目標方位§r
格式:§a!!goto§r 起始座標 目標座標 §e只能輸入X,Z座標§r
範例:§a!!goto§r §d-87 -87 87 87§r
----------------------------'''

def on_load(server, old):
	server.register_help_message('!!goto', '查詢座標方位角度')