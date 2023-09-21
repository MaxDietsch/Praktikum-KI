import cv2
import os
frame_num = 0
def extract_frames(video_path, output_dir, frame_num, file):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print(f"Error opening video file {video_path}")
        return

    while True:
        ret, frame = cap.read()  # Read the next frame from the video
        if not ret:
            break  # Exit the loop if we're at the end of the video

        # Construct the output image path
        frame_filename = os.path.join(output_dir, f"LD_negative_{file}_{frame_num}.png")
        cv2.imwrite(frame_filename, frame)  # Save the frame as an image
        print(frame_num)

        frame_num += 1

        
        if frame_num >= 109553:
            break
        

    # Release the video file when done
    cap.release()

    #print(f"Extracted {frame_num} frames to {output_dir}")
    return frame_num

if __name__ == "__main__":
    video_dir = "./download_unzip/LD/negative/videos_without_polyps"
    output_directory = "../data_dir/LD/negative"

    for file in os.listdir(video_dir):
        filepath = os.path.join(video_dir, file)
        frame_num = extract_frames(filepath, output_directory, frame_num, file[2: -5])
