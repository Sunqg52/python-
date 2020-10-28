import unittest
from _test_fun import get_formatted_name
from _test_class import AnonymouSurvey

#针对函数进行测试
class NameTestCase(unittest.TestCase):
	"""测试 name_function.py"""

	def test_first_last_name(self):
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')	#将formatted_name 与 janis joplin进行比较
'''
if __name__ == '__main__':
	unittest.main()
'''

'''
unittest模块中常用的断言方法:
	assertEqual(a,b)		核实	a == b 
	assertNotEqual(a,b)		核实	a != b
	assertTrue(x)			核实	x为True
	assertFalse(x)			核实	x为False
	assertIn(item, list)	核实	item在list中
	assertNotIn(item, list)	核实	item不再list中
'''

# 针对类进行测试
class TestAnonymouSurvey(unittest.TestCase):
	"""针对AnonymouSurvey类进行测试"""

	def setUp(self):
		"""
		创建一个调查对象和一组答案
		"""
		question = "what's your name?"
		self.survey = AnonymouSurvey(question)
		self.responses = {'sun', 'quan', 'gang'}

	def test_store_reponse(self):
		"""测试答案会被妥善的存储"""
		self.survey.store_response(self.responses)

if __name__ == '__main__':
	unittest.main()
