import cv2
import subprocess as sp
import numpy

from package import timecode

from ffprobe import FFProbe

import os


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

def test_up_left_corner(img,offset_top,offset_left):

    b = img.item(0 + offset_top, 0 + offset_left, 0)
    g = img.item(0 + offset_top, 0 + offset_left, 1)
    r = img.item(0 + offset_top, 0 + offset_left, 2)
    if r == 0 and g == 0 and b == 0:
        return True
    return False

def test_up_right_corner(img,x_res, offset_top,offset_right):

    b = img.item(0 + offset_top, x_res - 1 - offset_right, 0)
    g = img.item(0 + offset_top, x_res - 1 - offset_right, 1)
    r = img.item(0 + offset_top, x_res - 1 - offset_right, 2)
    if r == 0 and g == 0 and b == 0:
        return True
    return False

def test_down_right_corner(img,x_res, y_res, offset_bottom,offset_right):

    b = img.item(y_res - 1 - offset_bottom, x_res - 1 - offset_right, 0)
    g = img.item(y_res - 1 - offset_bottom, x_res - 1 - offset_right, 1)
    r = img.item(y_res - 1 - offset_bottom, x_res - 1 - offset_right, 2)
    if r == 0 and g == 0 and b == 0:
        return True
    return False

def test_down_left_corner(img, y_res, offset_bottom,offset_left):

    b = img.item(y_res - 1 - offset_bottom, 0 + offset_left, 0)
    g = img.item(y_res - 1 - offset_bottom,0 + offset_left, 1)
    r = img.item(y_res - 1 - offset_bottom, 0 + offset_left, 2)
    if r == 0 and g == 0 and b == 0:
        return True
    return False


def save_snapshot(image,img_number):
    path = "./snapshots"
    if not os.path.isdir(path):
        os.makedirs(path)
    filename = os.path.join(path,str(img_number))
    filename = filename + '.png'
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(filename,image_gray)


def add_issue(image,issues_list,current_frame, corner ):
    if issues_list == []:   #  It's the first issue
        issues_list.append({
                            "start_frm": current_frame,
                            "end_frm": current_frame,
                            "corners" : []
        })

        issues_list[-1]["corners"].append(corner)
        save_snapshot(image,current_frame)  # saving a snasphot of the first image fo the issue

    else:  # the detected issue is part of an existing issue, we make sure that the corner is part of the list
        if issues_list[-1].get("end_frm") == (current_frame - 1):
            issues_list[-1]["end_frm"] = current_frame
            if corner not in issues_list[-1].get("corners"):
                issues_list[-1]["corners"].append(corner)


        else:  # It's a completely new issue
            issues_list.append({
                "start_frm": current_frame,
                "end_frm": current_frame,
                "corners": []
            })
            issues_list[-1]["corners"].append(corner)
            save_snapshot(image, current_frame)  # saving a snasphot of the first image fo the issue

    return issues_list



def analyse_video_pass_01(path,offset_top,offset_bottom, offset_left,offset_right):

    x_res, y_res = get_resolution(path)
    end_frame = get_duration_frames(path)
    framerate = get_framerate(path)
    issues_list = []
   # up_left_corner = (0 + offset_top, 0 + offset_left)
   # up_right_corner = (0 + offset_top, x_res - offset_right - 1)
   #  down_right_corner = (y_res - offset_bottom, x_res - offset_right - 1)
   # down_left_corner = (y_res - offset_bottom, 0 + offset_left)



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
        image = image.reshape((y_res, x_res, 3))  # Notice how height is specified first and then width
        #if image is not None:
       # if test_up_left_corner(img= image, offset_top= offset_top,offset_left = offset_left):
        #    issues_list = add_issue(image=image,issues_list=issues_list,current_frame= img_number,corner = "UP_LEFT")
        #if test_up_right_corner(img= image, x_res= x_res,offset_top=offset_top,offset_right=offset_right):
         #   issues_list = add_issue(image=image,issues_list=issues_list,current_frame= img_number,corner = "UP_RIGHT")
        if test_down_right_corner(img= image, x_res=x_res,y_res=y_res,offset_bottom=offset_bottom,offset_right=offset_right):
            issues_list = add_issue(image=image,issues_list=issues_list,current_frame= img_number,corner = "DOWN_RIGHT")
        if test_down_left_corner(img=image,y_res=y_res,offset_bottom=offset_bottom,offset_left=offset_left):
            issues_list = add_issue(image=image,issues_list=issues_list,current_frame= img_number,corner = "DOWN_LEFT")
        cv2.imshow(f'{os.path.basename(path)}: Analyse en cours... Appuyer sur q pour arreter', image)
        img_number += 1


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if img_number == end_frame:
            break

        pipe.stdout.flush()
    cv2.destroyAllWindows()