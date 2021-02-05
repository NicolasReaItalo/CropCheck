import cv2
import subprocess as sp
import numpy

from package import timecode

from ffprobe import FFProbe


def get_resolution(path):
    metadata = FFProbe(path)
    return  metadata.streams[0].frame_size()


def get_framerate(path):
    metadata = FFProbe(path)
    return metadata.streams[0].__dict__.get('framerate')


def get_duration_frames(path):
    metadata = FFProbe(path)
    return metadata.streams[0].frames()


def play_video(path):

    x_res, y_res = get_resolution(path)
    end_frame = get_duration_frames(path)
    FFMPEG_BIN = "ffmpeg"
    command = [FFMPEG_BIN,
               '-i', path,  # fifo is the named pipe
               '-pix_fmt', 'bgr24',  # opencv requires bgr24 pixel format.
               '-vcodec', 'rawvideo',
               '-an', '-sn',  # we want to disable audio processing (there is no audio)
               '-f', 'image2pipe', '-']
    pipe = sp.Popen(command, stdout=sp.PIPE, bufsize=10 ** 8)

    img_number = 0
    while True:
        # Capture frame-by-frame
        raw_image = pipe.stdout.read(x_res * y_res * 3)
        # transform the byte read into a numpy array
        image = numpy.frombuffer(raw_image, dtype='uint8')
        image = image.reshape((y_res, x_res, 3))  # Notice how height is specified first and then width
        if image is not None:
            cv2.imshow('Video', image)

            img_number += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if img_number == end_frame:
            break

        pipe.stdout.flush()
    cv2.destroyAllWindows()
