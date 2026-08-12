#方法一
import pizza_2
pizza_2.make_pizza(16, 'pepperoni')
pizza_2.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#方法二
import pizza_2 as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#方法三
from pizza_2 import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#方法四
from pizza_2 import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#方法五
from pizza_2 import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')