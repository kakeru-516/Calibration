#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os
import cv2 as cv
import numpy as np


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--file", type=str, default=None)
    parser.add_argument("--width", type=int, default=1024)
    parser.add_argument("--height", type=int, default=768)

    parser.add_argument("--square_len", type=float, default=23.0)
    parser.add_argument("--grid_size", type=str, default="10,7")

    parser.add_argument("--k_filename", type=str, default="K_fisheye.csv")
    parser.add_argument("--d_filename", type=str, default="d_fisheye.csv")

    parser.add_argument("--interval_time", type=int, default=500)
    parser.add_argument('--use_autoappend', action='store_true')

    args = parser.parse_args()

    return args


def main():
    # コマンドライン引数
    args = get_args()

    cap_device = args.device
    filepath = args.file
    cap_width = args.width
    cap_height = args.height

    # カメラ準備
    cap = None
    if filepath is None:
        cap = cv.VideoCapture(cap_device)
        cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)
    else:
        cap = cv.VideoCapture(filepath)

    __IMG_DIR = 'img/'
    if not os.path.exists(__IMG_DIR) :
        os.makedirs(__IMG_DIR)

    grid_intersection_size = eval(args.grid_size)  # チェスボード内の格子数

    capture_count = 0
    while (True):
        ret, frame = cap.read()
        frame_copy = frame.copy()
        key = cv.waitKey(1) & 0xFF
        if key == 13 :
            found, corner = cv.findChessboardCorners(frame, grid_intersection_size)
            if found :
                cv.imwrite('./img/' + str(capture_count) + '.jpg', frame)
                capture_count += 1
                cv.drawChessboardCorners(frame_copy, grid_intersection_size, corner, found)
        cv.imshow('original', frame_copy)

        if key == 27:  # ESC
            cap.release()
            cv.destroyAllWindows()
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()

