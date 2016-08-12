
def getd(user, token, start = None , stop = None, client = None):
	url = "https://toggl.com/reports/api/v2/details?workspace_id=%i&user_agent=alec.burslem@gmail.com" % user
	if start != None:
		url = url + "&since=%s" % start
	if stop != None:
		url = url + "&until=%s" % stop
	dets = requests.get(url, auth =(token, 'api_token'),)
	dets = dets.json()
	pages = [dets]
	if dets["total_count"] > dets["per_page"]:
		reps = dets["total_count"] / dets["per_page"]
		count=1
		for page in range(1, math.ceil(reps)):
			nurl = url + '&page=%i' % page
			data = requests.get(nurl, auth =(token, 'api_token'),)
			data = data.json()
			pages.append(data)
			count += 1
	return pages

def getsum():
	