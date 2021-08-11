#coding 1创建列表、元组以及列表的重要几个操作
# list1 = ["car","bike"]
# list2 = ["airplane","jeep"]
# list1 = list1 * 2
# print(list1)
#extend只能用于列表
#append可以用的范围更广
#list1 = ["car", "bike"]
#list1.append("bus")
#list1.pop(1)
#del list1[1]
#print(list1)
# del list[i]和list.pop(i) 都能都能把（i+1）位置的元素删掉
# 但区别与list.remove(x)删了所有重复的元素的第一个


#coding2_创建字典以及对应的操作
#d = {key1:value1,key2:value2}
    # 键和值都在花括号中
    # 键和值中间用冒号隔开
    # 键值对之间用逗号隔开
    # 字典的常用方法
    #     clear（）
    #     copy(),浅拷贝
    #     has.key(k)
    #     get(k,[:,d])
    #     pop(k,[d])， pop 的写法和get有不同，加了冒号就错了
    #
    #     几个遍历器
    #     iterms()
    #     iteriterms()
    #     iterikey()
    #     iterivalues()
    #     将对应的值返回列表
    #     keys()
    #     values()
    #     update(E),#把E与原来的字典合并

#coding3_用try来改进猜数字小游戏
# a = 10
# count = 0
# try:
#     while count <= 4:
#         input = int(input("enter a number:"))
#         if input == a:
#             print("u r right")
#         else:
#             print("u r wrong")
#             count = count + 1
#     else:
#         print("game over")
# except:
#     print("proccess is done")

#coding 4_写一个幂函数
# a = float(input("enter two number:"))
# b = float(input("enter two number:"))
# def fuc1(a, b):
#     c = a ** b
#     d = a + b
#     print("the result is ", c, d)
#     return       #可以不写，但调用函数fuc1()一定不能忘记
# fuc1(a, b)

#形参（列如b）可以指定末位形参一个数值
#可以用关键字（keyword）来指定其他形参，而且不用考虑顺序，
    # 如fuc1(a = 1, b = 2),fuc1(a = 2)等，
    # 在调用函数时未提及的形参保留默认值

#coding 5 讨论函数中return返回值的问题
# def fuc2():
#     return
# fuc2()
# print(fuc2())
# #return之后可以返回数字、字符等，也可以不跟东西，默认返回None
    #把列表转换成元组，再把数字赋给元素
    # def fuc3(x,y,z):
    #     list = [x,y,z]
    #     list.reverse()
    #     number = tuple(list)
    #     return number
    # a, b, c = fuc3(3, 4, 5)
    # print('a is ', a,'b is ', b,'c is ', c )

#coding 6_递归函数
# n = int(input("enter a n:"))
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# factorial(n)
# print("factorial(n) is ", factorial(n))

#coding 7_generator函数
    #多次调用func()，实际上每次都是创建一个新的引用。
    # 你可以这样来理解，你每一次执行print(next(func()))，实际上就是在执行f = func() ;
    # print(next(f))。如果你每次都创建一个新的生成器，自然每次就只能取出一次元素。

    # def gen_number(n):
    #     for i in range(n):
    #         yield i
    # gen = gen_number(2)
    # print(next(gen))
    # print(next(gen))
    # #print(next(gen)),error type:StopIterationSS

#coding 8_简单结构
    #if-else
    #if-elif
    #while-else
    #for i in range():

#coding 9_编译python文件
# import py_compile
# py_complie.compile('test.py')

# import sys
# print(dir(sys))
#result:
# ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__',
#  '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable',
#  '_clear_type_cache', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework',
#  '_getframe', '_git', '_home', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix',
#  'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright',
#  'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit',
#  'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
#  'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding',
#  'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion',
#  'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode',
#  'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'pycache_prefix',
#  'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setcheckinterval', 'setprofile', 'setrecursionlimit',
#  'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version',
#  'version_info','warnoptions', 'winver']

#coding10_apply()函数的定义
    # apply(func,[,args[,kwargs]])
    # func是函数名
    # args是元组或者列表，如果函数不包括args则说说明函数不包括自定义参数
    # kwargs代表一个字典，其中key代表函数的参数名，value代表实参
    # apply的返回值就是自定义函数function()的返回值
    # def mutiple(a = 3, b = 4):
    #     return a*b
    #     mutiple(a, b)
    # print()
    #print(apply(mutiple, (1,3)))
#coding11_模块的属性
#__name__用来判断当前模块是不是程序入口
#英文状态下输入双下划线
#如果运行的是当前程序，则应该写为_main_
#_doc_用来输出模块中的字符串内容
    # if __name__ == '__main__':
    #     print("myModule主程序被调用")
    # else:
    #     print("myModule主程序未被调用")
    #
    # import myModule

#coding12_一个小例子来定义类
# class Hello:
#     '''hello! class'''
#     def printHello(self):
#         "hello world"
#         print("hello the world")
# print(Hello.__doc__)  #打印class中的文字
# print(Hello._doc_),  #对比165行的正确写法
# print(Hello.printHello.__doc__) # 打印函数的中的文字，因为是在类中，想要答应必须带上类名
#                                 # print(printHello.__doc__),错误1
#                                 # print(printHello._doc_),错误2
