import re, os, requests

# Create a videos directory if it doesn't exist
if not os.path.exists("videos"):
    os.mkdir("videos")

# open and read the markdown file
with open("videos.md", "r") as f:
    md_content = f.read()

# define regex pattern to match the video links
pattern = r"\[(.*?)\]\((.*?)\)"

# search for all matches in the markdown file
matches = re.findall(pattern, md_content)

# loop through the matches and download the videos
for title, url in matches:
    # check if the file already exists
    if os.path.exists(f"videos/{title}.mp4"):
        print(f"videos/{title} already downloaded, skipping...")
        continue

    # extract the video ID from the Vimeo URL
    video_id = url.split("/")[-2]

    # construct the API endpoint URL
    api_url = f"https://player.vimeo.com/video/{video_id}/config"

    # send a GET request to the API endpoint
    response = requests.get(api_url)

    # extract the video URL from the API response
    video_url = response.json()["request"]["files"]["progressive"][-1]["url"]

    # download the video
    response = requests.get(video_url)

    # save the video to a file
    with open(f"videos/{title}.mp4", "wb") as f:
        f.write(response.content)
        print(f"videos/{title} downloaded successfully!")
