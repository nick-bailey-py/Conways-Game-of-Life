import numpy as np
import imageio.v2 as imageio
import glob

fps = 4
hold_seconds = 3


frames = sorted(glob.glob("board*.png")) # stores and sorts frames

with imageio.get_writer("mov.mp4", fps=fps) as writer: # initialises mp4
    for filename in frames: # sorts through frames and writes them to the ifle
        image = imageio.imread(filename)
        writer.append_data(image)
    

    last_frame = imageio.imread(frames[-1]) # grabs last frame
    last2_frame = imageio.imread(frames[-2]) # grabs second last frame

    if "-steadystate" in frames[-1]: # checks if last frame is steady
        
        for _ in range(fps * hold_seconds): # repeats last frame so it can be seen
            writer.append_data(last_frame)
        print("COMPLETE - Steady State")

    elif "-Asteadystate" in frames[-1]: # checks if last frame is alternating

        for _ in range(int(np.floor(fps/2 * hold_seconds))): # repeats last two frames
           writer.append_data(last2_frame)
           writer.append_data(last_frame)
        print("COMPLETE - Alternating Steady State")
    
    else:
        print("COMPLETE - No Steady State")
