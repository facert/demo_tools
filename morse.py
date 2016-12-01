#! coding:utf-8

import morse_talk as mtalk

def morse(content):
    if content >= u'\u4e00' and content <= u'\u9fff':
            reply = u'摩斯密码只支持英文和数字'
    else:
        try:
            reply = mtalk.decode(content)
            reply = '摩尔斯密码解码为：%s' % reply
        except KeyError:
            reply = mtalk.encode(content)
            reply = '摩尔斯密码编码为：%s' % reply
        return reply

content = 'i love you'

print morse(content)
