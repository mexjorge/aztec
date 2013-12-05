# Program for computing the height of a ball in vertical motion.
v0 = 5 # initial velocity
g = 9.81 # acceleration of gravity
t = 0.76 # time
y = v0*t - 0.5*g*t**2 # vertical position
print y
print 'At t=%g s, the height of the ball is %.2f m.' % (t, y)