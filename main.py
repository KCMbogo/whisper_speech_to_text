# import whisper

# model = whisper.load_model(name="base")
# result = model.transcribe("/home/kadilana/Downloads/intro.mp3")

# with open(file="transcription.txt", mode="w") as f:
#     f.write(f'TEXT: \n{result["text"]}\n\nLanguage: {result["language"]}')

import whisper

model = whisper.load_model("base")
result = model.transcribe("/home/kadilana/Downloads/Final.mp3")

segments = result['segments']

# Group segments into paragraphs based on silence gaps (e.g., > 1.5s)
paragraphs = []
current_para = []
prev_end = 0

for seg in segments:
    start = seg['start']
    text = seg['text'].strip()
    
    if start - prev_end > 1.5 and current_para:
        # If silence > 1.5s, start a new paragraph
        paragraphs.append(" ".join(current_para))
        current_para = []
    
    current_para.append(text)
    prev_end = seg['end']

# Add the last paragraph
if current_para:
    paragraphs.append(" ".join(current_para))

# Save to file
with open("transcription.txt", "w", encoding="utf-8") as f:
    for para in paragraphs:
        f.write(para.strip() + "\n\n")
