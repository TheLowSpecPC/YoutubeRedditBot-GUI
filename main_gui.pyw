import time
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import con_gui
import threading
import praw, sys
import requests, os
from pathlib import Path
from RedDownloader import RedDownloader
from moviepy.editor import concatenate_videoclips, VideoFileClip
from os.path import isfile, join
from collections import defaultdict
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

root = Tk()
cwd = os.getcwd()
root.geometry("1000x600")
root.title("Youtube Reddit Bot (Made By: The Low Spec PC)")
root.iconbitmap(cwd + "/icon.ico")
root.config(bg="gray")


def reddit():
    root1 = Tk()
    root1.geometry("500x300")
    root1.config(bg="gray")
    root1.title("Setting (Reddit API)")
    root1.iconbitmap(cwd + "/icon.ico")

    def client_id():
        with open(cwd + "/Bot/Info/client id.txt", "w") as a1:
            a1.write(a.get())
            a1.close()

    def client_secret():
        with open(cwd + "/Bot/Info/client secret.txt", "w") as b1:
            b1.write(b.get())
            b1.close()

    def user_agent():
        with open(cwd + "/Bot/Info/user agent.txt", "w") as c1:
            c1.write(c.get())
            c1.close()

    def username():
        with open(cwd + "/Bot/Info/username.txt", "w") as d1:
            d1.write(d.get())
            d1.close()

    Label(root1, text="Client ID", font="Raleway", bg="black", fg="white").pack()
    a = Entry(root1, width="70")
    a.pack()
    a.insert(0, con_gui.client_id1)
    Button(root1, text="Save", command=client_id).pack()

    Label(root1, text="Client Secret", font="Raleway", bg="black", fg="white").pack()
    b = Entry(root1, width="70")
    b.pack()
    b.insert(0, con_gui.client_secret1)
    Button(root1, text="Save", command=client_secret).pack()

    Label(root1, text="User Agent", font="Raleway", bg="black", fg="white").pack()
    c = Entry(root1, width="70")
    c.pack()
    c.insert(0, con_gui.user_agent)
    Button(root1, text="Save", command=user_agent).pack()

    Label(root1, text="Username", font="Raleway", bg="black", fg="white").pack()
    d = Entry(root1, width="70")
    d.pack()
    d.insert(0, con_gui.username)
    Button(root1, text="Save", command=username).pack()


def download():
    root2 = Tk()
    root2.geometry("500x460")
    root2.config(bg="gray")
    root2.title("Setting (Downloader)")
    root2.iconbitmap(cwd + "/icon.ico")

    def lim():
        with open(cwd + "/Bot/Info/limit.txt", "w") as e1:
            e1.write(e.get())
            e1.close()

    def sub1():
        if f.get()!="":
            if os.path.exists(cwd+"/Bot/Info/Sub/"+f.get()+".txt"):
                os.remove(cwd+"/Bot/Info/Sub/"+f.get()+".txt")
            open(cwd+"/Bot/Info/Sub/"+f.get()+".txt", "w")

    def sub2():
        if n.get()!="":
            if os.path.exists(cwd+"/Bot/Info/Sub/"+n.get()+".txt"):
                os.remove(cwd+"/Bot/Info/Sub/"+n.get()+".txt")

    Label(root2, text="No: Of Videos", font="Raleway", bg="black", fg="white").pack()
    e = Entry(root2, width="70")
    e.pack()
    e.insert(0, con_gui.limit)
    Button(root2, text="Save", command=lim).pack()

    Label(root2, text="Subreddit", font="Raleway", bg="black", fg="white").pack()
    f = Entry(root2, width="25")
    f.place(x=75, y=100)
    Button(root2, text="Save", command=sub1).place(x=125, y=125)

    n = Entry(root2, width="25")
    n.place(x=275, y=100)
    Button(root2, text="Delete", command=sub2).place(x=325, y=125)

    x=1
    sub = Text(root2, width="60", height="17")
    sub.place(x=10, y=175)
    for i in con_gui.subreddit:
        sub.insert(END, str(x)+": "+i+"\n")
        x+=1


def google():
    root3 = Tk()
    root3.geometry("500x300")
    root3.config(bg="gray")
    root3.title("Setting (Youtube)")
    root3.iconbitmap(cwd + "/icon.ico")

    def mail():
        with open(cwd + "/Bot/Info/gmail.txt", "w") as g1:
            g1.write(g.get())
            g1.close()

    def password():
        with open(cwd + "/Bot/Info/password.txt", "w") as h1:
            h1.write(h.get())
            h1.close()

    def link():
        with open(cwd + "/Bot/Info/link.txt", "w") as i1:
            i1.write(i.get())
            i1.close()

    def che():
        global check
        check = con_gui.check
        if check == "No":
            with open(cwd + "/Bot/Info/check.txt", "w") as q1:
                check = "Yes"
                q1.write(check)
                q1.close()
        elif check == "Yes":
            with open(cwd + "/Bot/Info/check.txt", "w") as q1:
                check = "No"
                q1.write(check)
                q1.close()

    Label(root3, text="Gmail", font="Raleway", bg="black", fg="white").pack()
    g = Entry(root3, width="70")
    g.pack()
    g.insert(0, con_gui.gmail)
    Button(root3, text="Save", command=mail).pack()

    Label(root3, text="Password", font="Raleway", bg="black", fg="white").pack()
    h = Entry(root3, width="70")
    h.pack()
    h.insert(0, con_gui.password1)
    Button(root3, text="Save", command=password).pack()

    Label(root3, text="Upload Button", font="Raleway", bg="black", fg="white").pack()
    i = Entry(root3, width="70")
    i.pack()
    i.insert(0, con_gui.upload_button)
    Button(root3, text="Save", command=link).pack()

    Label(
        root3, text="Automated Youtube Upload", font="Raleway", bg="black", fg="white"
    ).pack()
    Button(root3, text=con_gui.check, command=che, width="20", height="2").place(
        x=175, y=240
    )


def edit():
    root4 = Tk()
    root4.geometry("500x300")
    root4.config(bg="gray")
    root4.title("Setting (Editor)")
    root4.iconbitmap(cwd + "/icon.ico")

    def intro():
        with open(cwd + "/Bot/Info/intro video.txt", "w") as j1:
            j = filedialog.askopenfilename(initialdir="C:/", title="Select a Video")
            j1.write(j)
            j1.close()

    def transition():
        with open(cwd + "/Bot/Info/transition video.txt", "w") as k1:
            k = filedialog.askopenfilename(initialdir="C:/", title="Select a Video")
            k1.write(k)
            k1.close()

    def outro():
        with open(cwd + "/Bot/Info/outro video.txt", "w") as l1:
            l = filedialog.askopenfilename(initialdir="C:/", title="Select a Video")
            l1.write(l)
            l1.close()

    Label(
        root4,
        text="Intro Video",
        font="Raleway",
        bg="black",
        fg="white",
        width="20",
        height="1",
    ).pack()
    Button(root4, text="Select A File", command=intro, width="10", height="1").pack(
        pady=10
    )

    Label(
        root4,
        text="Transition Video",
        font="Raleway",
        bg="black",
        fg="white",
        width="20",
        height="1",
    ).pack()
    Button(
        root4, text="Select A File", command=transition, width="10", height="1"
    ).pack(pady=10)

    Label(
        root4,
        text="Outro Video",
        font="Raleway",
        bg="black",
        fg="white",
        width="20",
        height="1",
    ).pack()
    Button(root4, text="Select A File", command=outro, width="10", height="1").pack(
        pady=10
    )


def auto():
    root5 = Tk()
    root5.geometry("500x300")
    root5.config(bg="gray")
    root5.title("Automation")
    root5.iconbitmap(cwd + "/icon.ico")

    def sta():
        Label(
            root,
            text="Please Wait Until The Progressbar Is Filled",
            font=("Raleway", 20),
            bg="red",
            fg="white",
            height="1",
        ).place(x=240, y=225)
        progress = ttk.Progressbar(
            root, orient=HORIZONTAL, length=500, mode="determinate"
        )
        progress.place(x=250, y=275)
        down = str(Path.home() / "Downloads")

        if (
            con_gui.client_id
            and con_gui.client_secret
            and con_gui.user_agent
            and con_gui.username != ""
        ):
            if con_gui.na != "":
                if con_gui.gmail and con_gui.password and con_gui.upload_button != "":
                    part = con_gui.part
                    while True:
                        # Links
                        cmd.insert(END, "____Downloader____\n")
                        cmd.see("end")
                        reddit = praw.Reddit(
                            client_id=con_gui.client_id,
                            client_secret=con_gui.client_secret,
                            user_agent=con_gui.user_agent,
                            username=con_gui.username,
                        )

                        x = 0
                        no = 0
                        sub = con_gui.subreddit

                        # Clearing the folder
                        cmd.insert(END, "Clearing old Videos\n")
                        cmd.see("end")
                        for i in os.listdir(cwd + "/Bot/Reddit"):
                            try:
                                os.remove(cwd + "/Bot/Reddit/" + i)
                                cmd.insert(END, i + " Deleted\n")
                                cmd.see("end")
                            except:
                                continue
                        # Grabbing links
                        cmd.insert(END, "Downloading new videos\n")
                        cmd.see("end")
                        progress["value"] = 5
                        for s in sub:
                            cmd.insert(END, "____Subreddit = " + s + "____\n")
                            cmd.see("end")
                            progress["value"] += 10
                            no += round(con_gui.limit / len(sub))
                            no1 = no + 1
                            try:
                                for submission in reddit.subreddit(s).new(
                                    limit=None
                                ):  # can use hot,top,new,rising
                                    if x == no or x == no1 == True:
                                        break
                                    else:
                                        if (
                                            submission.over_18 == False
                                            and submission.is_video == True
                                        ):
                                            urls = submission.url
                                            link = requests.get(urls).url
                                            x += 1
                                            RedDownloader.Download(
                                                url=link,
                                                output=cwd
                                                + "/Bot/Reddit/Output %04i" % x,
                                                quality=1080,
                                            )

                                            cmd.insert(
                                                END, "No: of videos = %04i" % x + "\n"
                                            )
                                            cmd.insert(END, "Link = " + link + "\n")
                                            cmd.see("end")
                                        else:
                                            cmd.insert(
                                                END,
                                                "NSFW or Image will not be downloaded\n",
                                            )
                                            cmd.see("end")
                            except:
                                cmd.insert(
                                    END,
                                    "Enter Proper Details in Reddit API Settings or Downloader Settings\n",
                                )
                                cmd.see("end")
                                sys.exit(1)
                            if s == sub[-1]:
                                break

                        cmd.insert(END, "Downloading Complete\n")
                        cmd.see("end")

                        # Editor
                        cmd.insert(END, "____Editor____\n")
                        cmd.see("end")
                        path = cwd + "/Bot/Reddit"
                        introName = "intro_vid"
                        outroName = "Outro_vid"
                        name1 = con_gui.na + " " + str(part) + ".mp4"
                        outputFile = down + "/" + name1

                        allVideos = []
                        seenLengths = defaultdict(list)
                        totalLength = 0
                        cmd.insert(END, "Searching Video Folder\n")
                        cmd.see("end")
                        progress["value"] = 50
                        for fileName in os.listdir(path):
                            filePath = join(path, fileName)
                            if isfile(filePath) and fileName.endswith(".mp4"):
                                cmd.insert(END, fileName + "\n")
                                cmd.see("end")
                                # Destination path
                                clip = VideoFileClip(filePath)
                                clip = clip.resize((1920, 1080))
                                duration = clip.duration
                                cmd.insert(END, duration)
                                cmd.insert(END, "\n")
                                cmd.see("end")
                                allVideos.append(clip)
                                seenLengths[duration].append(fileName)
                                totalLength += duration

                        # Add intro vid
                        cmd.insert(END, "Editing Video\n")
                        cmd.see("end")
                        videos = []
                        progress["value"] = 55
                        try:
                            if introName != "":
                                introVid = VideoFileClip(con_gui.intro_video)
                                introVid = introVid.resize((1920, 1080))
                                videos.append(introVid)
                                duration += introVid.duration
                                cmd.insert(END, duration)
                                cmd.insert(END, "\n")
                                cmd.see("end")
                        except:
                            cmd.insert(END, "Intro Video Not Found\n")
                            cmd.see("end")

                        # Create videos
                        progress["value"] = 60
                        try:
                            transition = VideoFileClip(con_gui.transition_video)
                            transition = transition.resize((1920, 1080))
                        except:
                            cmd.insert(END, "Transition Video Not Found\n")
                            cmd.see("end")

                        for clip in allVideos:
                            videos.append(clip)
                            duration += clip.duration
                            if con_gui.transition_video != "":
                                videos.append(transition)
                                duration += transition.duration
                            cmd.insert(END, duration)
                            cmd.insert(END, "\n")
                            cmd.see("end")

                        # Add outro vid
                        progress["value"] = 65
                        try:
                            if outroName != "":
                                outroVid = VideoFileClip(con_gui.outro_video)
                                outroVid = outroVid.resize((1920, 1080))
                                videos.append(outroVid)
                                duration += outroVid.duration
                                cmd.insert(END, duration)
                                cmd.insert(END, "\n")
                                cmd.see("end")
                        except:
                            cmd.insert(END, "Outro Video Not Found\n")
                            cmd.see("end")

                        finalClip = concatenate_videoclips(videos, method="compose")

                        progress["value"] = 70
                        cmd.insert(
                            END,
                            "Exporting The Video, This Might Take a Long Time Please wait\n",
                        )
                        cmd.see("end")

                        finalClip.write_videofile(
                            outputFile,
                            threads=8,
                            remove_temp=True,
                            codec="libx264",
                            audio_codec="aac",
                            preset="medium",
                            fps=20,
                        )

                        progress["value"] = 90
                        cmd.insert(END, "Editing Complete\n")
                        cmd.see("end")

                        # Upload
                        cmd.insert(END, "____Uploading____\n")
                        cmd.see("end")
                        a = 0
                        progress["value"] = 95
                        while a == 0:
                            try:
                                # Login
                                cmd.insert(END, "Login\n")
                                cmd.see("end")
                                driver = uc.Chrome(use_subprocess=True)
                                driver.get(
                                    "https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin"
                                )
                                sleep(1)
                                mail = WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable((By.NAME, "identifier"))
                                )
                                mail.send_keys(con_gui.gmail)
                                driver.find_element("id", "identifierNext").click()
                                sleep(1)
                                passwd = WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable((By.NAME, "Passwd"))
                                )
                                passwd.send_keys(con_gui.password)
                                driver.find_element("id", "passwordNext").click()
                                sleep(2)

                                # Upload
                                driver.get(con_gui.upload_button)
                                sleep(2)
                                driver.find_element(
                                    By.CSS_SELECTOR, "#content > input[type=file]"
                                ).send_keys(down + "/" + name1)
                                sleep(2)
                                notkids = WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable(
                                        (By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK")
                                    )
                                )
                                notkids.click()
                                sleep(1)
                                next1 = WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable((By.ID, "next-button"))
                                )
                                next1.click()
                                sleep(1)
                                next2 = WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable((By.ID, "next-button"))
                                )
                                next2.click()
                                sleep(1)
                                next3 = WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable((By.ID, "next-button"))
                                )
                                next3.click()
                                sleep(1)
                                driver.find_elemente(By.NAME, "PUBLIC").click()
                                sleep(1)
                                done = WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable((By.ID, "done-button"))
                                )
                                done.click()
                                sleep(5)
                                a += 1
                            except:
                                cmd.insert(END, "Error, Please Wait\n")
                                cmd.see("end")
                        progress["value"] = 100
                        cmd.insert(END, "____Uploading Complete____\n")
                        cmd.see("end")

                        part += 1
                        time.sleep(con_gui.num)

                else:
                    cmd.insert(END, "Details are missing from Youtube Settings\n")
                    cmd.see("end")
                    sys.exit(1)
            else:
                cmd.insert(END, "Enter the Video Name\n")
                cmd.see("end")
                sys.exit(1)
        else:
            cmd.insert(END, "Details are missing from Reddit API Settings\n")
            cmd.see("end")
            sys.exit(1)

    def sto():
        os._exit(0)

    def entr():
        with open(cwd + "/Bot/Info/vid_no.txt", "w") as en1:
            en1.write(en.get())
            en1.close()

    def par():
        with open(cwd + "/Bot/Info/part.txt", "w") as pa1:
            pa1.write(pa.get())
            pa1.close()

    Label(
        root5,
        text="No: Of Videos per day",
        font=("Raleway", 14),
        bg="black",
        fg="white",
        width="20",
        height="1",
    ).pack()
    en = Entry(root5, width="30")
    en.insert(0, con_gui.vid_no)
    en.pack(pady=10)
    Button(root5, text="Save", command=entr).pack(pady=10)

    Label(
        root5,
        text="Part",
        font=("Raleway", 14),
        bg="black",
        fg="white",
        width="6",
        height="1",
    ).pack()
    pa = Entry(root5, width="30")
    pa.insert(0, con_gui.part)
    pa.pack(pady=10)
    Button(root5, text="Save", command=par).pack(pady=10)

    Button(
        root5,
        text="Start",
        command=threading.Thread(target=sta).start,
        width="20",
        height="2",
    ).pack(side=LEFT, padx=50)
    Button(root5, text="Stop", command=sto, width="20", height="2").pack(
        side=RIGHT, padx=50
    )


def run():
    def link():
        cmd.insert(END, "____Downloader____\n")
        cmd.see("end")
        reddit = praw.Reddit(
            client_id=con_gui.client_id,
            client_secret=con_gui.client_secret,
            user_agent=con_gui.user_agent,
            username=con_gui.username,
        )

        x = 0
        no = 0
        sub = con_gui.subreddit

        # Clearing the folder
        cmd.insert(END, "Clearing old Videos\n")
        cmd.see("end")
        for i in os.listdir(cwd + "/Bot/Reddit"):
            try:
                os.remove(cwd + "/Bot/Reddit/" + i)
                cmd.insert(END, i + " Deleted\n")
                cmd.see("end")
            except:
                continue
        # Grabbing links
        cmd.insert(END, "Downloading new videos\n")
        cmd.see("end")
        progress["value"] = 5
        for s in sub:
            cmd.insert(END, "____Subreddit = " + s + "____\n")
            cmd.see("end")
            progress["value"] += 10
            no += round(con_gui.limit / len(sub))
            no1 = no + 1
            try:
                for submission in reddit.subreddit(s).new(
                    limit=None
                ):  # can use hot,top,new,rising
                    if x == no or x == no1 == True:
                        break
                    else:
                        if submission.over_18 == False and submission.is_video == True:
                            urls = submission.url
                            link = requests.get(urls).url
                            x += 1
                            RedDownloader.Download(
                                url=link,
                                output=cwd + "/Bot/Reddit/Output %04i" % x,
                                quality=1080,
                            )

                            cmd.insert(END, "No: of videos = %04i" % x + "\n")
                            cmd.insert(END, "Link = " + link + "\n")
                            cmd.see("end")
                        else:
                            cmd.insert(END, "NSFW or Image will not be downloaded\n")
                            cmd.see("end")
            except:
                cmd.insert(
                    END,
                    "Enter Proper Details in Reddit API Settings or Downloader Settings\n",
                )
                cmd.see("end")
                sys.exit(1)
            if s == sub[-1]:
                break

        cmd.insert(END, "Downloading Complete\n")
        cmd.see("end")

    def editor():
        cmd.insert(END, "____Editor____\n")
        cmd.see("end")
        path = cwd + "/Bot/Reddit"
        introName = "intro_vid"
        outroName = "Outro_vid"
        outputFile = down + "/" + con_gui.name

        allVideos = []
        seenLengths = defaultdict(list)
        totalLength = 0
        cmd.insert(END, "Searching Video Folder\n")
        cmd.see("end")
        progress["value"] = 50
        for fileName in os.listdir(path):
            filePath = join(path, fileName)
            if isfile(filePath) and fileName.endswith(".mp4"):
                cmd.insert(END, fileName + "\n")
                cmd.see("end")
                # Destination path
                clip = VideoFileClip(filePath)
                clip = clip.resize((1920, 1080))
                duration = clip.duration
                cmd.insert(END, duration)
                cmd.insert(END, "\n")
                cmd.see("end")
                allVideos.append(clip)
                seenLengths[duration].append(fileName)
                totalLength += duration

        # Add intro vid
        cmd.insert(END, "Editing Video\n")
        cmd.see("end")
        videos = []
        progress["value"] = 55
        try:
            if introName != "":
                introVid = VideoFileClip(con_gui.intro_video)
                introVid = introVid.resize((1920, 1080))
                videos.append(introVid)
                duration += introVid.duration
                cmd.insert(END, duration)
                cmd.insert(END, "\n")
                cmd.see("end")
        except:
            cmd.insert(END, "Intro Video Not Found\n")
            cmd.see("end")

        # Create videos
        progress["value"] = 60
        try:
            transition = VideoFileClip(con_gui.transition_video)
            transition = transition.resize((1920, 1080))
        except:
            cmd.insert(END, "Transition Video Not Found\n")
            cmd.see("end")

        for clip in allVideos:
            videos.append(clip)
            duration += clip.duration
            if con_gui.transition_video != "":
                videos.append(transition)
                duration += transition.duration
            cmd.insert(END, duration)
            cmd.insert(END, "\n")
            cmd.see("end")

        # Add outro vid
        progress["value"] = 65
        try:
            if outroName != "":
                outroVid = VideoFileClip(con_gui.outro_video)
                outroVid = outroVid.resize((1920, 1080))
                videos.append(outroVid)
                duration += outroVid.duration
                cmd.insert(END, duration)
                cmd.insert(END, "\n")
                cmd.see("end")
        except:
            cmd.insert(END, "Outro Video Not Found\n")
            cmd.see("end")

        finalClip = concatenate_videoclips(videos, method="compose")

        progress["value"] = 70
        cmd.insert(
            END, "Exporting The Video, This Might Take a Long Time Please wait\n"
        )
        cmd.see("end")

        finalClip.write_videofile(
            outputFile,
            threads=8,
            remove_temp=True,
            codec="libx264",
            audio_codec="aac",
            preset="medium",
            fps=20,
        )

        if con_gui.check == "Yes":
            progress["value"] = 90
            cmd.insert(END, "Editing Complete\n")
            cmd.see("end")
        elif con_gui.check == "No":
            progress["value"] = 100
            cmd.insert(END, "Process Complete\n")
            cmd.insert(END, "Final Video = " + outputFile)
            cmd.see("end")

    def chrome():
        cmd.insert(END, "____Uploading____\n")
        cmd.see("end")
        a = 0
        progress["value"] = 95
        while a == 0:
            try:
                # Login
                cmd.insert(END, "Login\n")
                cmd.see("end")
                driver = uc.Chrome(use_subprocess=True)
                driver.get(
                    "https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin"
                )
                sleep(1)
                mail = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.NAME, "identifier"))
                )
                mail.send_keys(con_gui.gmail)
                driver.find_element("id", "identifierNext").click()
                sleep(1)
                passwd = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.NAME, "Passwd"))
                )
                passwd.send_keys(con_gui.password)
                driver.find_element("id", "passwordNext").click()
                sleep(2)

                # Upload
                driver.get(con_gui.upload_button)
                sleep(2)
                driver.find_element(
                    By.CSS_SELECTOR, "#content > input[type=file]"
                ).send_keys(down + "/" + con_gui.name)
                sleep(2)
                notkids = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK"))
                )
                notkids.click()
                sleep(1)
                next1 = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "next-button"))
                )
                next1.click()
                sleep(1)
                next2 = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "next-button"))
                )
                next2.click()
                sleep(1)
                next3 = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "next-button"))
                )
                next3.click()
                sleep(1)
                driver.find_element(By.NAME, "PUBLIC").click()
                sleep(1)
                done = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "done-button"))
                )
                done.click()
                sleep(5)
                a += 1
            except:
                cmd.insert(END, "Error, Please Wait\n")
                cmd.see("end")
        progress["value"] = 100
        cmd.insert(END, "____Uploading Complete____\n")
        cmd.see("end")

    Label(
        root,
        text="Please Wait Until The Progressbar Is Filled",
        font=("Raleway", 20),
        bg="red",
        fg="white",
        height="1",
    ).place(x=240, y=225)
    progress = ttk.Progressbar(root, orient=HORIZONTAL, length=500, mode="determinate")
    progress.place(x=250, y=275)

    down = str(Path.home() / "Downloads")

    if (
        con_gui.client_id
        and con_gui.client_secret
        and con_gui.user_agent
        and con_gui.username != ""
    ):
        if con_gui.na != "":
            if con_gui.check == "Yes":
                if con_gui.gmail and con_gui.password and con_gui.upload_button != "":
                    link()
                    editor()
                    chrome()
                else:
                    cmd.insert(END, "Details are missing from Youtube Settings\n")
                    cmd.see("end")
                    sys.exit(1)
            elif con_gui.check == "No":
                link()
                editor()
        else:
            cmd.insert(END, "Enter the Video Name\n")
            cmd.see("end")
            sys.exit(1)
    else:
        cmd.insert(END, "Details are missing from Reddit API Settings\n")
        cmd.see("end")
        sys.exit(1)


def name():
    with open(cwd + "/Bot/Info/name.txt", "w") as m1:
        m1.write(m.get())
        m1.close()


def exit():
    os._exit(0)


Label(
    root,
    text="Settings (Please Restart The App After Saving)",
    bg="black",
    fg="white",
    font=("Raleway", 20),
    width="500",
    height="1",
).pack()
Button(root, text="Reddit API (Praw)", command=reddit, width="20", height="2").place(
    x=125, y=50
)
Button(root, text="Downloader", command=download, width="20", height="2").place(
    x=325, y=50
)
Button(root, text="Youtube", command=google, width="20", height="2").place(x=525, y=50)
Button(root, text="Editor", command=edit, width="20", height="2").place(x=725, y=50)
Button(root, text="Automated", command=auto, width="20", height="2").place(x=125, y=150)

Label(
    root, text="Video Name", font=("Raleway", 20), bg="black", fg="white", height="1"
).place(x=425, y=100)
m = Entry(root, width="50")
m.place(x=350, y=150)
m.insert(0, con_gui.na)
Button(root, text="Save", command=name, width="10", height="0").place(x=675, y=150)

Button(
    root,
    text="Start",
    command=threading.Thread(target=run).start,
    width="20",
    height="2",
).place(x=430, y=175)

root.wm_protocol("WM_DELETE_WINDOW", exit)

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
cmd = Text(root, width="120", height="17")
cmd.place(x=10, y=300)
scrollbar.config(command=cmd.yview)
cmd.config(yscrollcommand=scrollbar.set)

root.mainloop()
