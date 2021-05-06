def combine_audio(vidname, audname, outname, fps=30):
    import moviepy.editor as mpe
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)

combine_audio("video_without_audio.mp4", "audio.mp3", "video_with_audio.mp4")
