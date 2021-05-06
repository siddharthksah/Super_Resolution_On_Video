import os, re
import moviepy.video.io.ImageSequenceClip
image_folder='Upscaled'
fps=30

image_files = [image_folder+'/'+img for img in os.listdir(image_folder) if img.endswith(".jpg")]

image_files.sort(key=lambda f: int(re.sub('\D', '', f)))

clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('video_without_audio.mp4')