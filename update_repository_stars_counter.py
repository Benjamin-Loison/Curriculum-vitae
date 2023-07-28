import requests

def getContentFromURL(url):
    return requests.get(url).json()

youtubeOperationalApiGitHubRepositoryUrl = 'https://api.github.com/repos/Benjamin-Loison/YouTube-operational-API'

newStars = getContentFromURL(youtubeOperationalApiGitHubRepositoryUrl)['stargazers_count']

prefix = 'YouTube operational API} ('
suffix = '\hspace{'

filePath = 'CV-EN.tex'

with open(filePath) as f:
    lines = f.read().splitlines()
    for linesIndex, line in enumerate(lines):
        if prefix in line:
            oldStars = int(line.split(prefix)[1].split(suffix)[0])
            print(oldStars, newStars)
            newLine = line.split(prefix)[0] + prefix + str(newStars) + suffix + suffix.join(line.split(suffix)[1:])
            lines[linesIndex] = newLine

with open(filePath, 'w') as f:
    for linesIndex, line in enumerate(lines):
        f.write(line)
        if linesIndex < len(lines) - 1:
            f.write("\n")
