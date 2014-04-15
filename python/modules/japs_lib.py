
def get_dict_jap_month():
	months_dict = {'January':'Ichigatsu','February':'Nigatsu','March':'Sangatsu','April':'Shigatsu','May':'Gogatsu','June':'Rokugatsu','July':'Shichigatsu','August':'Hachigatsu','September':'Kugatsu','October':'Juugatsu','November':'Juuichigatsu','December':'Juunigatsu'}
	return months_dict

def get_list_jap_days(initial):
	days_list = []
	days_list.append([initial,['Tsuitachi'],['Futsuka'],['Mikka'],['Yokka'],['Itsuka'],['Muika'],['Nanoka'],['Yooka','Youka'],['Kokonoka'],['Tooka','Touka']])
	days_list.append([initial,'ichi','ni','san','yokka','go','roku','shichi','hachi','ku'])
	days_list.append([initial,'juu','nijuu','sanjuu'])
	return days_list

def get_list_jap_nums(initial):
	nums_list = []
	nums_list.append([initial,'ichi','ni','san','yon','go','roku','nana','hachi','kyuu'])
	nums_list.append([initial,'juu','nijuu','sanjuu','yonjuu','gojuu','rokujuu','nanajuu','hachijuu','kyuujuu'])
	nums_list.append([initial,'hyaku','nihyaku','sanbyaku','yonhyaku','gohyaku','roppyaku','nanahyaku','happyaku','kyuuhyaku'])
	nums_list.append([initial,'sen','nisen','sanzen','yonsen','gosen','rokusen','nanasen','hassen','kyuusen'])
	nums_list.append(['man','ichiman','niman','sanman','yonman','goman','rokuman','nanaman','hachiman','kyuuman'])
	nums_list.append([initial,'juu','nijuu','sanjuu','yonjuu','gojuu','rokujuu','nanajuu','hachijuu','kyuujuu'])
	nums_list.append([initial,'hyaku','nihyaku','sanbyaku','yonhyaku','gohyaku','roppyaku','nanahyaku','happyaku','kyuuhyaku'])
	nums_list.append([initial,'sen','nisen','sanzen','yonsen','gosen','rokusen','nanasen','hassen','kyuusen'])
	nums_list.append(['oku','ichioku','nioku','sanoku','yonoku','gooku','rokuoku','nanaoku','hachioku','kyuuoku'])
	nums_list.append([initial,'juu','nijuu','sanjuu','yonjuu','gojuu','rokujuu','nanajuu','hachijuu','kyuujuu'])
	nums_list.append([initial,'hyaku','nihyaku','sanbyaku','yonhyaku','gohyaku','roppyaku','nanahyaku','happyaku','kyuuhyaku'])
	nums_list.append([initial,'sen','nisen','sanzen','yonsen','gosen','rokusen','nanasen','hassen','kyuusen'])
	return nums_list

def get_list_jap_mins(initial):
	mins_list = []
	mins_list.append(['pun','ippun','nifun','sanpun','yonpun','gofun','roppun','nanafun','happun','kyuufun','juppun'])
	mins_list.append([initial,'juu','nijuu','sanjuu','yonjuu','gojuu'])
	return mins_list

def get_list_jap_hours(initial):
	hours_list = []
	hours_list.append([initial,'ichiji','niji','sanji','yoji','goji','rokuji','shichiji','hachiji','kuji','juuji','juuichiji','juuniji'])
	return hours_list
