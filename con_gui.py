#Reddit Looter
with open("Bot\\Info\\client id.txt", "r")as a:
    client_id = a.readline()
    a.close()
with open("Bot\\Info\\client secret.txt", "r")as b:
    client_secret = b.readline()
    b.close()
with open("Bot\\Info\\user agent.txt", "r")as c:
    user_agent = c.readline()
    c.close()
with open("Bot\\Info\\username.txt", "r")as d:
    username = d.readline()
    d.close()
with open("Bot\\Info\\limit.txt", "r")as e:
    limits = e.readline()
    e.close()
if(limits != ""):
    limit = int(limits)
else:
    limit = 50
with open("Bot\\Info\\subreddit1.txt", "r")as f:
    sub1 = f.readline()
    f.close()
with open("Bot\\Info\\subreddit2.txt", "r")as n:
    sub2 = n.readline()
    n.close()
with open("Bot\\Info\\subreddit3.txt", "r")as o:
    sub3 = o.readline()
    o.close()
with open("Bot\\Info\\subreddit4.txt", "r")as p:
    sub4 = p.readline()
    p.close()
subre = sub1,sub2,sub3,sub4
subreddit = []
for i in subre:
    if(i!=""):
        subreddit.append(i)

#YouTube Bot
with open("Bot\\Info\\gmail.txt", "r")as g:
    gmail = g.readline()
    g.close()
with open("Bot\\Info\\password.txt", "r")as h:
    password = h.readline()
    h.close()
with open("Bot\\Info\\link.txt", "r")as i:
    upload_button = i.readline()
    i.close()
with open("Bot\\Info\\check.txt", "r")as q:
    chec= q.readline()
    q.close()
if chec != "Yes" and "No":
    with open("Bot\\Info\\check.txt", "w")as q1:
        q1.write("No")
        check = "No"
else:
    check = chec

#Output Video Name
with open("Bot\\Info\\intro video.txt", "r")as j:
    intro_video = j.readline()
    j.close()
with open("Bot\\Info\\transition video.txt", "r")as k:
    transition_video = k.readline()
    k.close()
with open("Bot\\Info\\outro video.txt", "r")as l:
    outro_video = l.readline()
    l.close()
with open("Bot\\Info\\name.txt", "r")as m:
    na = m.readline()
    name = na+".mp4"
    m.close()