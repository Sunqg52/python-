from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('https://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))		# can_fetch判断是否可以被抓取
print(rp.can_fetch('*', 'http://www.jianshu.com/p/search?q=python&page=1&type=collections'))