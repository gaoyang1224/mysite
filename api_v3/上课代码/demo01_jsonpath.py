from jsonpath import jsonpath

json_dict = {
	'code': 0,
	'msg': 'OK',
	'data': {
		'id': 31,
		'leave_amount': 600.0,
		'mobile_phone': '18211112222',
		'reg_name': '小柠檬',
		'reg_time': '2021-01-28 15:27:07.0',
		'type': 1,
		'token_info': {
			'token_type': 'Bearer',
			'expires_in': '2021-01-29 20:40:00',
			'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjMxLCJleHAiOjE2MTE5MjQwMDB9.I20fFTVt5i8lK86GR7HOwCMMYPeaiTqSLVEiCJbxuXYvGtefg7JzFmK-fP6eOtTJyvSoSrMPaugwmFpaoIWSCA'
		}
	},
	'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'
}

# 匹配的结果放在列表，如果没有匹配，False
resp = jsonpath(json_dict, '$..token')
print(resp)