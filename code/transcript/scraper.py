from youtube_transcript_api import YouTubeTranscriptApi

# Function to get the transcript and save it to a file
def get_transcript(video_id, start_time, end_time, output_file):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    with open(output_file, 'w') as file:
        for entry in transcript:
            start = entry['start']
            if start_time <= start <= end_time:
                file.write(f"{entry['text']}\n")

# YouTube video ID for the new video
video_id = "IgUaEMUKrU8"

# Start and end times in seconds
start_time = 4 * 60 + 19
end_time = 8 * 60 + 0

# Output file name
output_file = 'transcript.txt'

# Get the transcript and save it
get_transcript(video_id, start_time, end_time, output_file)
print("Transcript saved to", output_file)