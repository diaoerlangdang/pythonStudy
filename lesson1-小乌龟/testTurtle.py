#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2018-1-10

@author: wise
'''

import turtle


#绘制方形
def draw_square(brad, length, width):
	for y in xrange(0,4):
		if y%2 == 0:
			#宽
			brad.forward(width)
			pass
		else:
			#长
			brad.forward(length)
		
		#‘小乌龟’向右旋转90度
		brad.right(90)
	pass

def draw_graph():
	#获取窗口屏幕
	window = turtle.Screen()
	#设置窗口背景颜色
	window.bgcolor('red')
	#获取‘乌龟’类实例
	brad = turtle.Turtle()
	#设置画笔形状为小乌龟
	brad.shape('turtle')

	#设置颜色，线条颜色为blue， 小乌龟颜色为green
	brad.color("blue", "green")
	#设置绘制的速度
	brad.speed(6)
	brad.pensize(2)

	#旋转角度
	turnAngle = 10

	#旋转一周，每次旋转角度为10度
	for x in xrange(0,360/turnAngle):
		draw_square(brad, 100, 100)		
		brad.right(turnAngle)
		pass

	#圆的起始位置
	brad.setposition(0,-100)
	print(brad.position())
	#设置圆圈的颜色 yellow
	brad.color('yellow', "green")
	#绘制半径为100的圆
	brad.circle(100)

	#设置颜色，线条颜色为blue， 小乌龟颜色为green
	brad.color("blue", "green")
	#回到原点
	brad.setposition(0,0)

	brad.pensize(1)


	#旋转一周，每次旋转角度为10度
	for x in xrange(0,360/turnAngle):

		for y in xrange(0,4):
			if y == 1 or y == 2:
				#设置颜色，线条颜色为red， 小乌龟颜色为green
				brad.color("red", "green")
				pass
			else:
				#设置颜色，线条颜色为blue， 小乌龟颜色为green
				brad.color("blue", "green")

			#绘制一条长boardLen的直线
			brad.forward(100)
			#‘小乌龟’向右旋转90度
			brad.right(90)	

		brad.right(turnAngle)
		pass

	#绘制筐把手
	brad.setposition(100,0)
	brad.color("orange", "green")
	brad.pensize(3)
	brad.setposition(0,180)
	brad.setposition(-100,0)

	#回归原点位置
	#设置颜色，线条颜色为blue， 小乌龟颜色为green
	brad.color("blue", "green")
	brad.pensize(2)
	brad.setposition(0,0)


	#当点击屏幕时，退出程序
	window.exitonclick()
	pass


draw_graph()

