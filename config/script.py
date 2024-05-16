import os
import subprocess
import xml.etree.ElementTree as ET

# 定义变量
video_directory = "/media"
nfo_directory = "/media"

# 定义生成NFO文件的函数
def generate_nfo(video_file):
    video_name = os.path.splitext(os.path.basename(video_file))[0]
    title = " ".join(video_name.split()[1:])  # Remove date from video name
    date = video_name.split()[0]  # Extract date from video name

    root = ET.Element("episodedetails")
    title_element = ET.SubElement(root, "title")
    title_element.text = title
    aired_element = ET.SubElement(root, "aired")
    aired_element.text = date

    nfo_file = os.path.join(nfo_directory, video_name + ".nfo")
    tree = ET.ElementTree(root)
    tree.write(nfo_file)

# 定义提取视频封面的函数
def extract_thumbnail(video_file):
    thumbnail_file = os.path.splitext(video_file)[0] + ".jpg"
    subprocess.run(["ffmpeg", "-i", video_file, "-ss", "00:00:05", "-vframes", "1", thumbnail_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 定义提取视频海报的函数
def extract_poster(video_file):
    poster_file = os.path.splitext(video_file)[0] + "-poster.jpg"
    subprocess.run(["ffmpeg", "-i", video_file, "-vf", "thumbnail", "-vframes", "1", poster_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 定义处理视频的函数
def process_videos():
    for root, dirs, files in os.walk(video_directory):
        for file in files:
            if file.endswith(".mp4"):
                video_file = os.path.join(root, file)
                generate_nfo(video_file)
                extract_thumbnail(video_file)
                extract_poster(video_file)

# 执行处理视频的函数
process_videos()
