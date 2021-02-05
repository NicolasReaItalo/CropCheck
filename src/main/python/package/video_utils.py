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

def analyse_video_pass_01(path,offset_top,offset_bottom, offset_left,offset_right):

    x_res, y_res = get_resolution(path)
    end_frame = get_duration_frames(path)
    framerate = get_framerate(path)
    up_left_corner = (0 + offset_top, 0 + offset_left)
    up_right_corner = (0 + offset_top, x_res - offset_right - 1)
    down_right_corner = (y_res - offset_bottom, x_res - offset_right - 1)
    down_left_corner = (y_res - offset_bottom, 0 + offset_left)


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
            new_image = numpy.copy(image)
            b = image.item(0, 0, 0)
            g = image.item(0, 0, 1)
            r = image.item(0, 0, 2)
           # print(f"image: {timecode.frame_to_tc_02(img_number, framerate)} -> ({r}:{g}:{b})")
            if r == 0 and g == 0 and b == 0:
                print(f"image: {timecode.frame_to_tc_02(img_number, framerate)} -> ({image[0,0]})")

                new_image.itemset((int(y_res/2),int(x_res/2),2),255)
            cv2.imshow('Video', new_image)
            img_number += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if img_number == end_frame:
            break

        pipe.stdout.flush()
    cv2.destroyAllWindows()