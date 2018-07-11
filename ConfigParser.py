# create file
import configparser
config = configparser.RawConfigParser()
config.add_section('Section1')
config.set('Section1', 'an_int', '15')
config.set('Section1', 'a_bool', 'true')
config.set('Section1', 'a_float', '3.1415')
config.set('Section1', 'baz', 'fun')
config.set('Section1', 'bar', 'Python')
config.set('Section1', 'foo', '%(bar)s is %(baz)s!')
# Writing our configuration file to 'example.cfg'
with open('/Users/jimmy/Desktop/VAAK/example01.ini', 'w') as configfile:
    config.write(configfile)
    
# read file
for key in config ['Section1']:
    print(key)
    

# use module configparser to create an .ini file
# create file
import configparser
config = configparser.ConfigParser()
config['Section0'] = {'Camera': '0,285,172，276,0,480,270,480',
                     'Map': '528,181,774,173,551,595,765,604'}
config['Section1'] = {'Camera': 'x0,y0,x1,y1,x2,y2,x3,y3',
                     'Map': 'x0,y0,x1,y1,x2,y2,x3,y3'}
config['Section2'] = {'Camera': 'x0,y0,x1,y1,x2,y2,x3,y3',
                     'Map': 'x0,y0,x1,y1,x2,y2,x3,y3'}

with open('/Users/jimmy/Desktop/VAAK/pos.ini', 'w') as configfile:
    config.write(configfile)

# read the file
config['Section1']['Camera']
config['Section1']['Map']
for key in config['Section1']:
    print(key)
