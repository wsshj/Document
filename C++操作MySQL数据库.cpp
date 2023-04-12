#define _CRT_SECURE_NO_WARNINGS
 
#include<iostream>
#include<mysql.h>
using namespace std;
 
int main()
{
	//创建句柄
	MYSQL mysql;
	//创建数据集变量
	MYSQL_RES* res = nullptr;
	//创建结果集变量
	MYSQL_ROW row;
	//创建一个结构体
	MYSQL_FIELD* field;
 
	//初始化数据库句柄
	mysql_init(&mysql);
	//设置字符集
	//mysql_options(&mysql, MYSQL_SET_CHARSET_NAME, "gbk");
	mysql_set_character_set(&mysql, "gbk");
	//开始连接数据库
	if (mysql_real_connect(&mysql, "localhost", "root", "Z20020803", "box_man", 3306, NULL, 0))
	{
		cout << "连接成功" << endl;
	}
	else
	{
		cout << "连接失败" << endl;
		return 0;
	}
	//设置事务
	mysql_autocommit(&mysql, "1");
	//增加数据
	string str1 = "insert into tb_912 values(2, 'xiaoming', '李四');";
	char ssql[1024];
	//使用sprintf拼出来的语句是一个标准的c语言字符串，可以使用该函数插入变量值
	sprintf(ssql, "insert into tb_912 values(%d, '%s', '%s');", 3, "daming", "17777777772");
	if (mysql_query(&mysql, ssql))//该语句提交成功返回0，失败放回1
	{
		cout << "提交失败" << endl;
	}
	else
	{
		cout << "提交成功" << endl;
	}
	//提交语句
	mysql_query(&mysql, str1.c_str());
	//删除数据
	string str3 = "delete from tb_912 where id = 2;";
	mysql_query(&mysql, str3.c_str());
	//修改数据
	string str4 = "update tb_912 set name = '张三' where id = 1;";
	mysql_query(&mysql, str4.c_str());
	//查询数据
	string str2 = "select * from tb_912;";
	mysql_query(&mysql, str2.c_str());
	//事务提交
	mysql_commit(&mysql);
	//获取里面的结果集
	res = mysql_store_result(&mysql);
	//拿到结果集得列数，调用的是 mysql_store_result() 的返回值，
	unsigned int a = mysql_num_fields(res);
	cout <<"表得列数："<< a << endl;
	//使用 mysql_fetch_fields() 函数获取列的名字，返回的是一个结构体数组
	field = mysql_fetch_fields(res);
	for (unsigned i = 0; i < a; i++)
	{
		cout << "当前列的名字：" << field[i].name << endl;//取出名字
	}
	unsigned long* lengths;
 
	//从结果集中获取到数据 mysql_fetch_row() 获取结果集中的一行数据，
	//成功：返回记录当前行中每个字段的值，失败：返回一个null
	while (row = mysql_fetch_row(res))
	{
		printf("%s %s %s \n", row[0], row[1], row[2]);
		//获取列中字段的长度
		lengths = mysql_fetch_lengths(res);//返回的是一个数组地址
		
		for (unsigned int i = 0; i < a; i++)
		{
			cout << "当前列的长度：" << lengths[i] << endl;//列数会构成一个数组
		}
	}
	//释放结果集
	mysql_free_result(res);
	//关闭mysql实例
	mysql_close(&mysql);
	return 0;
}