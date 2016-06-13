import requests

from lxml import etree

BASE = "http://wonder.cdc.gov/controller/datarequest/"

def make_parameter(name,value):
	parameter = etree.Element('parameter')
	name_tag = etree.Element('name')
	name_tag.text = name
	value_tag = etree.Element('value')
	value_tag.text = value
	
	parameter.append(name_tag)
	parameter.append(value_tag)

	return parameter

'''
<parameter>
<name>accept_datause_restrictions</name>
<value>true</value>
</parameter>'''

root = etree.Element('request-parameters')
root.append(make_parameter('accept_datause_restrictions','true'))

print etree.tostring(root,pretty_print=True)