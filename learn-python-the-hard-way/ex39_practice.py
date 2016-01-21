# -*- coding: gb2312 -*-
import hashmap

# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, '�Ĵ�', '��')
hashmap.set(states, '�㽭', '��')
hashmap.set(states, '����', 'ǭ')
hashmap.set(states, '����', '��')
hashmap.set(states, '����', '��')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, '��', '�ɶ�')
hashmap.set(cities, '��', '����')
hashmap.set(cities, 'ǭ', '����')

# add some more cities
hashmap.set(cities, '��', '����')
hashmap.set(cities, '��', '����')


# print out some cities
print '-' * 10
print "�� ��: %s" % hashmap.get(cities, '��')
print "�� ��: %s" % hashmap.get(cities, '��')

# print some states
print '-' * 10
print "����ļ����: %s" % hashmap.get(states, '����')
print "�㽭�ļ����: %s" % hashmap.get(states, '�㽭')

# do it by using the state then cities dict
print '-' * 10
print "������: %s" % hashmap.get(cities, hashmap.get(states, '����'))
print "�㽭��: %s" % hashmap.get(cities, hashmap.get(states, '�㽭'))

# print every state abbreviation
print '-' * 10
hashmap.list(states)

# print every city in state
print '-' * 10
hashmap.list(cities)

print '-' * 10
state = hashmap.get(states, '����')

if not state:
  print "Sorry, no ����."

# default values using ||= with the nil result
# can you do this on one line?
city = hashmap.get(cities, '��', '������')
print "����'��'�ĳ���: %s" % city