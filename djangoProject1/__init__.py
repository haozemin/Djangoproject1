# seeting中配置默认split3数据库，但需要修改成mysql时并且在seeting.py的同级目录的init_.py惊醒如下配置
import pymysql
pymysql.install_as_MySQLdb()