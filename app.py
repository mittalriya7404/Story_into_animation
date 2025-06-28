import nltk


from moviepy.editor import VideoFileClip, concatenate_videoclips
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string
nltk.download('stopwords')
nltk.download('punkt_tab')



# Define your category_keyword_mapping, functions, and other code here...
category_keyword_mapping = {
    "boy": {
        "walk": ["walking", "walked"],
        "jump": ["jumping", "boy jump", "jumped"],
        "run": ["running", "boy run", "ran"],
    },
    "girl": {
        "dance": ["dancing", "girl dance"],
        "talk": ["talking", "talked"],
        # Add more mappings for the "girl" category
    },
    "man": {
        "businessman": ["business", "man"],
        "gym": ["workout", "exercise"],
        "police": ["policeman", "trafficpolice", "inspector", "constable"],
        "play": ["playing", "played", "game"],
        "represent": ["representing", "explaining"],
        "working": ["job", "working"],
        "doctor": ["medical", "medicine"],
        "gardener": ["garden", "flowering", "gardening"],
        "zombie": ["horrorman", "ghost", "zombies"],
        # Add more mappings for the "man" category
    },
    "cat": {
        "angry": ["angrycat"],
        "sit": ["sitting", "sat"],
        # Add more mappings for the "cat" category
    },
     "chef": {
        "smile": ["smiling", "smiled"],
        # Add more mappings for the "cat" category
    },
    "cow": {
        "come": ["coming"],
        # Add more mappings for the "cat" category
    },
    "dog": {
        "go": ["going", "went", "gone"],
         "move": ["moving", "moved"],
        # Add more mappings for the "cat" category
    },
    # Add other mappings for categories
}

# Function to get the keyword mapping for a specific category
def get_keyword_mapping(keyword, category):
    if category in category_keyword_mapping and keyword in category_keyword_mapping[category]:
        return [keyword]
    return [keyword]

# Function to extract keywords from a sentence
def extract_keywords(sentence):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(sentence)
    keywords = []
    i = 0
    while i < len(words):
        if words[i].lower() not in stop_words and words[i] not in string.punctuation:
            phrase = words[i]
            j = i + 1
            while j < len(words) and (words[j].lower() not in stop_words and words[j] not in string.punctuation):
                phrase += " " + words[j]
                j += 1
            for category, mappings in category_keyword_mapping.items():
                for keyword in mappings:
                    if phrase.lower() in mappings[keyword]:
                        keywords.extend([category, keyword])
            i = j
        else:
            i += 1
    return keywords

# Function to play a video
def play_video(category, keyword):
    video_path = f"videos/{category}/{keyword}.mp4"
    clip = VideoFileClip(video_path)
    clip.preview()
    clip.close()

# Function to merge videos
def merge_videos(video_paths, output_path):
    clips = [VideoFileClip(path) for path in video_paths]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_path)
    final_clip.close()

# Main code

# Take input story from the user
story = input("Enter your story: ")

# Process the input story and create the animation
sentences = sent_tokenize(story)
video_paths = []
output_path = "output.mp4"

for sentence in sentences:
    keywords = extract_keywords(sentence)
    for keyword in keywords:
        for category in category_keyword_mapping.keys():
            if keyword in category_keyword_mapping[category]:
                mapped_keywords = get_keyword_mapping(keyword, category)
                for mapped_keyword in mapped_keywords:
                    video_path = f"videos/{category}/{mapped_keyword}.mp4"
                    try:
                        play_video(category, keyword)
                        video_paths.append(video_path)
                    except IOError:
                        print(f"No video found for keyword '{mapped_keyword}' in category '{category}'")
                break

if video_paths:
    merge_videos(video_paths, output_path)
    print(f"Videos merged successfully. Output saved as '{output_path}'")
else:
    print("No videos to merge.")
