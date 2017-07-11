import ccircle
import connection

con = connection.create()
con.send('set_name', {'name': 'Alien'})





args = {
    'vx': 0,
    'vy':0,

}
while True:
    if ccircle.isKeyDown('down'):
        args['vy'] = 50
        args['vx'] = 0
        con.send('set_velocity', args)

    if ccircle.isKeyDown('up'):
        args['vy'] = -50
        args['vx'] = 0
        con.send('set_velocity', args)

    if ccircle.isKeyDown('right'):
        args['vy'] = 0
        args['vx'] = 50
        con.send('set_velocity', args)

    if ccircle.isKeyDown('left'):
        args['vy'] = 0
        args['vx'] = -50
        con.send('set_velocity', args)
    if ccircle.isKeyDown('space'):
        con.send('damage_boss', args)


# Write code to make money and kill the evil cat!
# See readme.txt !