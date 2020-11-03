import pymysql


# 声明一个mysql对象
db = pymysql.connect(host='localhost', user='username', password='passwd', port=3306, db='dbname')		
cursor = db.cursor()	# 获得mysql游标

def create_db(db_name):
	sql = f"CREATE DATABASE {db_name} DEFAULT CHARACTER SET utf8"
	cursor.execute(sql)
	db.close()

def create_table(table_name):
	sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY(id))'
	cursor.execute(sql)
	db.close()


def insert_update_data(data):
	"""
	对于新来的数据，如果主键存在则更新，若主键不错在则插入
	"""

	table = 'students'
	keys = ', '.join(data.keys())
	values = ', '.join(['%s'] * len(data))

	sql = f'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
	update = ','.join([" {key} = %s".format(key=key) for key in data])
	sql += update

	try:
		if cursor.execute(sql, tuple(data.values())*2):
			print("Successful")
			db.commit()
	except:
			print("error")
			db.rollback()
	db.close()

def delete_date(table, condition):
	sql = f'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()

def select_date(table):
	sql = f'SELECT * FROM {table} WHERE age >= 10'
	try:
		cursor.execute(sql)
		# cursor.fetchone()  # 获取第一条数据
		results = cursor.fetchall()		# 获取全部数据
		for row in results:
			print(row)
	except:
		print("error")


# insert_update_data(data)
# delete_date('students', 'age > 20')
# select_date('students')
