#!/usr/bin/env python
#coding=utf-8

'''①
mobile_str = raw_input("请输入您要注册的手机号码:")
try: 
   mobile_num = int(mobile_str)
except ValueError: 
   print '您好，你输入的手机有非数字字符，请重新输入.'
else: 
   if (len(mobile_str) != 11): 
      print '您的手机号码位数不正确.' 
   else:
      print '您的手机正确，正在获取验证码'

password_str_0 = raw_input("请输入您的密码:")
try: 
   password_num_0 = int(password_str_0) 
except ValueError: 
   print '您好，你输入的密码不是纯数字，请重新输入'
else: 
   if (len(password_str_0) != 8): 
      print '您的密码位数不正确' 
   #如果输入的密码是8位数，再次输入密码验证
   else: 
      password_str_1 = raw_input("请再次输入您的密码") 
      try: 
          password_num_1 = int(password_str_1)
      except ValueError: 
          print '您好，你输入的密码不是纯数字，请重新输入' 
      else: 
        if (password_num_0 != password_num_1): 
          print '您好，你输入的密码与前一次不同，请重新输入'
        else: 
          print '您已成功注册' 
          fo = open("foo.txt", "wb") 
          fo.write('用户账号：' + mobile_str + ' ' + '用户密码：' + password_str_0);
'''


'② '
counter = 3
while counter > 0:
    mobile_str = raw_input("请输入您要注册的手机号码:")
    try: 
         mobile_num = int(mobile_str)
    except ValueError: 
         print '您好，你输入的手机有非数字字符，请重新输入.'
    else: 
         if (len(mobile_str) != 11): 
            print '您的手机号码位数不正确' 
         else:
            print '手机号码位数正确'
            break
    counter -= 1
    if (counter == 0):
         print('您登录次数频繁，请过1分钟再次登录!')

while counter > 0:
      password_str_0 = raw_input("请输入您的密码:")
      try: 
          password_num_0 = int(password_str_0) 
      except ValueError: 
          print '您好，你输入的密码不是纯数字，请重新输入'
      else: 
          if (len(password_str_0) != 8): 
             print '您的密码位数不正确' 
          #如果输入的密码是8位数，再次输入密码验证
          else: 
             password_str_1 = raw_input("请再次输入您的密码:") 
             try: 
                password_num_1 = int(password_str_1)
             except ValueError: 
                print '您好，你输入的密码不是纯数字，请重新输入' 
             else: 
                if (password_num_0 != password_num_1): 
                   print '您好，你输入的密码与前一次不同，请重新输入'
                else: 
                   print '您已成功注册' 
                   fo = open("foo.txt", "wb") 
                   fo.write('用户账号：' + mobile_str + ' ' + '用户密码：' + password_str_0);
                   break
      counter -=1
      if (counter == 0):
         print('您账号被锁住')
     
