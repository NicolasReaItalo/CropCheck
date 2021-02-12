import cv2
import subprocess as sp
import numpy

from package import timecode

from ffprobe import FFProbe

import os


def get_resolution(path):
    metadata = FFProbe(path)
    return metadata.streams[0].frame_size()


def get_framerate(path):
    metadata = FFProbe(path)
    return metadata.streams[0].__dict__.get('framerate')

def get_timecode(path):
    metadata = FFProbe(path)
    return metadata.streams[0].__dict__.get('timecode')

def get_duration_frames(path):
    metadata = FFProbe(path)
    return metadata.streams[0].frames()

def get_codec(path):
    metadata = FFProbe(path)
    return metadata.streams[0].codec_description()


def play_video(path):
    x_res, y_res = get_resolution(path)
    end_frame = get_duration_frames(path)

    command = ["ffmpeg",
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
        image = image.reshape((y_res, x_res, 3))

        if image is not None:
            cv2.imshow(f'{os.path.basename(path)}: Analyse en cours. Appuyer sur q pour arrêter', image)

            img_number += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if img_number == end_frame:
            break

        pipe.stdout.flush()
    cv2.destroyAllWindows()
    cv2.waitKey(1)

def save_snapshot(image, img_number):
    path = "./snapshots"
    if not os.path.isdir(path):
        os.makedirs(path)
    filename = os.path.join(path, str(img_number))
    filename = filename + '.png'
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(filename, image_gray)


def analyse_video_pass_01(path, first_image_analysed, offset_top, offset_bottom, offset_left, offset_right):
    x_res, y_res = get_resolution(path)
    if x_res > 1920:
        scale_factor = 1
    else:
        scale_factor = 1

    end_frame = get_duration_frames(path)
    framerate = get_framerate(path)
    issues_list = []
    resize_frame = ()

    print("TEST")
    print(get_timecode(path))


    command = ["ffmpeg",
               '-i', path,  # fifo is the named pipe
               '-pix_fmt', 'bgr24',  # opencv requires bgr24 pixel format.
               '-vcodec', 'rawvideo',
               '-an', '-sn',  # we want to disable audio processing (there is no audio)
               '-f', 'image2pipe', '-']
    pipe = sp.Popen(command, stdout=sp.PIPE, bufsize=10 ** 8)

    img_number = 0
    black_h = numpy.zeros((1, x_res, 3), dtype='uint8')
    black_v = numpy.zeros((y_res, 1, 3), dtype='uint8')

    while True:
        # Capture frame-by-frame
        raw_image = pipe.stdout.read(x_res * y_res * 3)
        # transform the byte read into a numpy array
        image = numpy.frombuffer(raw_image, dtype='uint8')
        image = image.reshape((y_res, x_res, 3))  # Notice how height is specified first and then width
        crop_top = image[0:1, 0:x_res]
        crop_bottom = image[y_res - 1:y_res, 0:x_res]
        crop_left = image[0:y_res, 0:1]
        crop_right = image[0:y_res, x_res - 1:x_res]

        black_lines_detected = []

        print('....................')
        print(img_number)
        print(f" max: {numpy.amax(crop_left)}")
        print(f" min: {numpy.amin(crop_left)}")
        print('....................')


        if numpy.array_equal(crop_top, black_h):
            black_lines_detected.append('Ligne du haut')

        if numpy.array_equal(crop_bottom, black_h):
            black_lines_detected.append('Ligne du bas')

        if numpy.array_equal(crop_left, black_v):
            black_lines_detected.append('Ligne de gauche')

        if numpy.array_equal(crop_right, black_v):
            black_lines_detected.append('Ligne de droite')

        if black_lines_detected != []:
            issues_list.append((img_number, black_lines_detected))

        resized = cv2.resize(image, (int(x_res / scale_factor), int(y_res / scale_factor)), 1, 1)

        cv2.imshow(f'{os.path.basename(path)}: Analyse en cours... {x_res}x{y_res}  Appuyer sur q pour arreter',
                   resized)




        img_number += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if img_number == end_frame:
            break

        pipe.stdout.flush()
    cv2.destroyAllWindows()
    for issue in issues_list:
        print(f'{issue[0]} : {issue[1]}')
