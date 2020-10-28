# 类的定义使用驼峰命名法
# 每个类中必须含有 _init_()方法；其作用是初始化属性。在类的所有函数中必须包含self形参用于操作属性
'''
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
'''

# 修改属性的值： 1.直接通过实例进行修改   2.通过方法进行设置   3.通过方法进行递增（增加特定的值）		

class Car:

	def __init__(self,name,model,year):
		"""初始化属性"""
		self.name = name
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""对汽车进行简单的描述"""
		compelete_info = f"{self.model} {self.name} {self.year}"
		print(compelete_info.title())


	def update_odometer(self, mileage):
		"""
		将里程表的读数设为指定的值
		禁止将里程表的读数向回调
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self,miles):
		"""增加里程表的值"""
		self.odometer_reading += miles

	def get_odometer(self):
		"""输出里程表信息"""
		print(f"This car has {self.odometer_reading} miles on it.")

	def fill_gas_tank(self):
		"""油箱储油量"""
		print("储油量不足")



'''
my_car = Car('subaru', "outback", 2021)
my_car.get_descriptive_name()
my_car.update_odometer(20)
my_car.increment_odometer(200)
my_car.get_odometer()

'''

class other:
	def __init__(self)

#继承  在已有类的基础上编写新类,通常要调用父类的方法 __init__(),这将让子类包含父类的属性
#电动车也是一种特殊的车  特殊值 电瓶电量   重写car类中的剩余油量为剩余电量
class electricCar(Car):

	def __init__(self,name.model,year):
		"""
		先初始化父类属性
		在初始化自己特有的属性
		"""
		super.__init__(name,model,year)
		self.battery_size = 75
		self.other = ocher()	#使用实例作为属性

	def fill_gas_tank(self):
		"""方法重写 重写后覆盖父类方法"""
		print("乘于电量不足！")

#模块及导入 与函数的使用方法相同
