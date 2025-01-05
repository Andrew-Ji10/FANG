import pyrealsense2 as rs
import numpy as np
import cv2

# Configure the RealSense pipeline
pipeline = rs.pipeline()
config = rs.config()

# Enable the color stream
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start the pipeline
pipeline.start(config)

try:
    print("Press 'q' to exit the camera feed.")
    while True:
        # Wait for a new frame
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        if not color_frame:
            continue

        # Convert the color frame to a numpy array
        color_image = np.asanyarray(color_frame.get_data())

        # Display the color image
        cv2.imshow("Intel RealSense RGB Feed", color_image)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Stop the pipeline and close the window
    pipeline.stop()
    cv2.destroyAllWindows()
