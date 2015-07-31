from django.template import loader, Context
from django.http import HttpResponse
import requests
import bs4
	
def zephyr(request):
	response = requests.get("http://www.onthecasemusic.co.uk/bands/717/zephyr")
	soup = bs4.BeautifulSoup(response.text, "html.parser")
	dates = [x.text for x in soup.select('h2[style=font-size:19px;]')]
	venues = [x.text for x in soup.select('div.name a[href^=/venues]')]
	venuelinks = ["http://www.onthecasemusic.co.uk" + x.attrs.get('href') for x in soup.select('div.name a[href^=/venues]')]
	times = [x.text for x in soup.select('div.price')]		
	gigs = zip(dates[:5], venuelinks[:5], venues[:5], times[:5])
	t = loader.get_template('index.html')
	html = t.render({'gig': gigs})	
	return HttpResponse(html)