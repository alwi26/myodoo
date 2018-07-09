# l = [
# {'credit': 0, 'partner_id': False, 'name': 'Ending Balance', 'debit': 4614300.0, 'product_uom_id': 3, 'quantity': 2.0, 'ref': 'Stock Variation', 'account_id': 597, 'product_id': 1156},
# # {'credit': 4614300.0, 'partner_id': False, 'name': 'Ending Balance', 'debit': 0, 'product_uom_id': 3, 'quantity': 2.0, 'ref': 'Stock Variation', 'account_id': 623, 'product_id': 1156},
# # {'credit': 4614300.0, 'partner_id': False, 'name': 'Ending Balance', 'debit': 0, 'product_uom_id': 3, 'quantity': 2.0, 'ref': 'Stock Variation', 'account_id': 597, 'product_id': 1156},
# {'credit': 0, 'partner_id': False, 'name': 'Ending Balance', 'debit': 4614300.0, 'product_uom_id': 3, 'quantity': 2.0, 'ref': 'Stock Variation', 'account_id': 623, 'product_id': 1156}
# ]

# # result = {}
# # for d in l:
# #     for key, value in d.items():
# #         if type(value) == float:
# #             if value in result:
# #                 result[value] += value
# #             else:
# #                 result[value] = value
# #         elif type(value) == str:
# #             if value not in result:
# #                 result[value] = str(value)
# #         else:
# #             if value not in result:
# #                 result[value] = value
# # print result

# new_data = []
# for i in l:
#     yes = False
#     for s in new_data:
#         if s['product_id'] == i['product_id']:
#             s['quantity'] += i['quantity']
#             s['debit'] += i['debit']
#             yes = True
#     if not yes:
#         new_data.append(i)
# print new_data




# [(0, 0, {'credit': 0, 'partner_id': False, 'name': 'Ending Balance', 'debit': 744520.0, 'product_uom_id': 104, 'quantity': 40.0, 'ref': 'Stock Variation', 'account_id': 597, 'product_id': 1392}), (0, 0, {'credit': 744520.0, 'partner_id': False, 'name': 'Ending Balance', 'debit': 0, 'product_uom_id': 104, 'quantity': 40.0, 'ref': 'Stock Variation', 'account_id': 626, 'product_id': 1392}), (0, 0, {'credit': 0, 'partner_id': False, 'name': 'Ending Balance', 'debit': 781746.0, 'product_uom_id': 104, 'quantity': 42.0, 'ref': 'Stock Variation', 'account_id': 597, 'product_id': 1392}), (0, 0, {'credit': 781746.0, 'partner_id': False, 'name': 'Ending Balance', 'debit': 0, 'product_uom_id': 104, 'quantity': 42.0, 'ref': 'Stock Variation', 'account_id': 626, 'product_id': 1392})]

# [(0, 0, {'ref': 'Stock Variation', 'name': 'Ending Balance', 'product_uom_id': 104, 'account_id': 626, 'credit': 1526266.0, 'product_id': 1392, 'debit': 0, 'partner_id': False, 'quantity': 82.0}), {'ref': 'Stock Variation', 'name': 'Ending Balance', 'product_uom_id': 104, 'account_id': 597, 'credit': 0, 'product_id': 1392, 'debit': 1526266.0, 'partner_id': False, 'quantity': 82.0}]

import ast
import json
import yaml

# string = "{'credit': 744520.0, 'partner_id': False, 'name': 'Ending Balance', 'debit': 0, 'product_uom_id': 104, 'quantity': 40.0, 'ref': 'Stock Variation', 'account_id': 626, 'product_id': 1392}, {'credit': 5123060.0, 'partner_id': False, 'name': 'Ending Balance', 'debit': 0, 'product_uom_id': 125, 'quantity': 155.0, 'ref': 'Stock Variation', 'account_id': 626, 'product_id': 1333}, {'credit': 237000.0, 'partner_id': False, 'name': 'Ending Balance', 'debit': 0, 'product_uom_id': 123, 'quantity': 75.0, 'ref': 'Stock Variation', 'account_id': 626, 'product_id': 1327}"
l = [{'credit': 744520.0, 'partner_id': False, 'name': 'Ending Balance', 'debit': 0, 'product_uom_id': 104, 'quantity': 40.0, 'ref': 'Stock Variation', 'account_id': 626, 'product_id': 1392}, {'credit': 5123060.0, 'partner_id': False, 'name': 'Ending Balance', 'debit': 0, 'product_uom_id': 125, 'quantity': 155.0, 'ref': 'Stock Variation', 'account_id': 626, 'product_id': 1333}, {'credit': 237000.0, 'partner_id': False, 'name': 'Ending Balance', 'debit': 0, 'product_uom_id': 123, 'quantity': 75.0, 'ref': 'Stock Variation', 'account_id': 626, 'product_id': 1327}]
# dict_format_string = "{'1':'one', '2' : 'two'}"
# d = {}
# elems = filter(str.isalnum, dict_format_string.split(","))
# print elems
# values = elems[1::2]
# print values
# keys   = elems[0::2]
# print keys
# d.update(zip(keys,values))
# print d
# str='{1:0,2:3,3:4}'
# contents = str[1:-1]        # strip off leading { and trailing }
# items = contents.split(',') # each individual item looks like key:value
# pairs = [item.split(':',1) for item in items] # ("key","value"), both strings
# d = dict((k,eval(v)) for (k,v) in pairs) # evaluate values but not strings

# print d

# string = "{'server1':'value','server2':'value'}"

#Now removing { and }
tes = False
for li in l:
	tes += li
	print tes