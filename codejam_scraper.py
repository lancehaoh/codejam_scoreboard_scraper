import urllib, base64, json, math, time

while 1:
    for i in xrange(1, 1500 + 1, 200):
      param = "{\"min_rank\":%d,\"num_consecutive_users\":200}" % i
      en = base64.b64encode(param)

      while en[-1] == "=":
          en = en[:-1]
      url = "https://codejam.googleapis.com/scoreboard/0000000000051706/poll?p=%s" % en
      en = en[:len(en) - 1]
      response = urllib.urlopen(url)
      data = response.read() + "==="
      
      de = base64.urlsafe_b64decode(data)
      j = json.loads(de)
      
      scores = j['user_scores']
      
      if len(scores) == 0:
          break
      
      for score in scores:
          try:
            name = score['displayname'].decode('utf-8')
          except:
            name = "???"
          #if score['country'] == 'Singapore':
          print "%-15s %-35s %-15s %-50s" % (score['rank'], score['country'], score['score_1'], name)
    print "*" * 50, "end of results", "*" * 50
    break
