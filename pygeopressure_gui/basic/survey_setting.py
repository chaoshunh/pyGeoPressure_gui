# -*- coding: utf-8 -*-
"""
A survey setting class

Created on Sat Jan 20 2018
"""
from __future__ import absolute_import, print_function, division
from __future__ import unicode_literals, with_statement

__author__ = "Yu Hao"

import json
import math

from pathlib2 import Path
import numpy as np


class SurveySetting( object):
    """
    class to hold survey settings and compute additional coordination property
    """
    def __init__(self, file_path=None):
        self.startInline = None
        self.endInline = None
        self.stepInline = None
        self.startCrline = None
        self.endCrline = None
        self.stepCrline = None
        self.startDepth = None
        self.endDepth = None
        self.stepDepth = None
        self.zType = None
        self.inline_A = None
        self.crline_A = None
        self.east_A = None
        self.north_A = None
        self.inline_B = None
        self.crline_B = None
        self.east_B = None
        self.north_B = None
        self.inline_C = None
        self.crline_C = None
        self.east_C = None
        self.north_C = None
        #--------------------
        self.inline_bin = None
        self.crline_bin = None
        self.area = None
        self.invertedAxis = None
        self.azimuth = None
        if file is not None:
            self._read_from_file(file_path)
            self._bin_size()
            self._basic()
            self._coordinate_conversion()
            self.azimuth_and_invertedAxis()

    def _basic(self):
        self.nEast = (self.endInline - self.startInline) // \
            self.stepInline + 1
        self.nNorth = (self.endCrline - self.startCrline) // \
            self.stepCrline + 1
        self.stepEast = math.sqrt(
            (self.north_C - self.north_B)**2 + (self.east_C - self.east_B)**2) / \
                ((self.inline_C - self.inline_B) / self.stepInline)
        self.stepNorth = math.sqrt(
            (self.north_B - self.north_A)**2 + (self.east_B - self.east_A)**2) / \
                ((self.crline_B - self.crline_A) / self.stepCrline)

    def _read_from_file(self, file_path):
        with file_path.open('r') as rf:
            survey_dict = json.load(rf)
        self.startInline = survey_dict["inline_range"][0]
        self.endInline = survey_dict["inline_range"][1]
        self.stepInline = survey_dict["inline_range"][2]
        self.startCrline = survey_dict["crline_range"][0]
        self.endCrline = survey_dict["crline_range"][1]
        self.stepCrline = survey_dict["crline_range"][2]
        self.startDepth = survey_dict["z_range"][3]
        self.endDepth = survey_dict["z_range"][0]
        self.stepDepth = survey_dict["z_range"][1]
        self.zType = survey_dict["z_range"][2]
        self.inline_A, self.crline_A, self.east_A, self.north_A = \
            survey_dict["point_A"]
        self.inline_B, self.crline_B, self.east_B, self.north_B = \
            survey_dict["point_B"]
        self.inline_C, self.crline_C, self.east_C, self.north_C = \
            survey_dict["point_C"]

    @classmethod
    def angle(x, y):
        """
        Return angle from 0 to pi

        x : tuple
        y : tuple
        """
        dx = x[1] - x[0]
        dy = y[1] - y[1]
        arctan = math.atan(dy / dx)

        if dx > 0 and dy > 0:
            angle = arctan
        elif dx > 0 and dy < 0:
            angle = 2 * math.pi + arctan
        elif dx < 0 and dy > 0:
            angle = math.pi + arctan
        elif dx < 0 and dy < 0:
            angle = math.pi + arctan
        return angle

    def _bin_size(self):
        dist_ab = np.sqrt((self.north_B - self.north_A) *\
                          (self.north_B - self.north_A) + \
                          (self.east_B - self.east_A) * \
                          (self.east_B - self.east_A))
        dist_bc = np.sqrt((self.north_C - self.north_B) *\
                          (self.north_C - self.north_B) + \
                          (self.east_C - self.east_B) * \
                          (self.east_C - self.east_B))
        self.crline_bin = np.round(dist_ab / (self.crline_B - self.crline_A),
                                   decimals=2)
        self.inline_bin = np.round(dist_bc / (self.inline_C - self.inline_B),
                                   decimals=2)
        self.area = np.round(
            self.inline_bin * (self.endInline - self.startInline) * \
            self.crline_bin * (self.endCrline - self.startCrline) * 10**(-6),
            decimals=2)

    def _coordinate_conversion(self):
        """"
        calculate coefficients for line/coordination conversion
        """
        self.gamma_x = (self.east_B - self.east_A) / \
            (self.crline_B - self.crline_A)
        self.beta_x = (self.east_C - self.east_B) / \
            (self.inline_C - self.inline_B)
        self.alpha_x = self.east_A - \
            self.beta_x * self.inline_A - \
            self.gamma_x * self.crline_A
        self.gamma_y = (self.north_B - self.north_A) / \
            (self.crline_B - self.crline_A)
        self.beta_y = (self.north_C - self.north_B) / \
            (self.inline_C - self.inline_B)
        self.alpha_y = self.north_A - \
            self.beta_y * self.inline_A - \
            self.gamma_y * self.crline_A

    def line_2_coord(self, inline, crline):
        x = self.alpha_x + self.beta_x * inline + self.gamma_x * crline
        y = self.alpha_y + self.beta_y * inline + self.gamma_y * crline
        return (x, y)

    def coord_2_line(self, coordinate):
        x = coordinate[0]
        y = coordinate[1]
        d = np.matrix([[x - self.alpha_x],
                       [y - self.alpha_y]])
        G = np.matrix([[self.beta_x, self.gamma_x],
                       [self.beta_y, self.gamma_y]])
        m = G.I * d
        # m = m.astype(int)

        inline, crline = m[0][0], m[1][0]
        param_in = (inline - self.startInline) // self.stepInline + \
            ((inline - self.startInline) % self.stepInline) // \
            (self.stepInline / 2)
        inline = self.startInline + self.stepInline * param_in
        param_cr = (crline - self.startCrline) // self.stepCrline + \
            ((inline - self.startCrline) % self.stepCrline) // \
            (self.stepCrline)
        crline = self.startCrline + self.stepCrline * param_cr
        return (inline, crline)

    def azimuth_and_invertedAxis(self):
        """
        Determine azimuth (Crossline axis direction from Coordination North)
        and Inline axis is positive to the right (invertedAxis=False) or
        to the left (invertedAxis=True)
        """
        self.inclination = 0 # radius
        b_a_north = self.north_B - self.north_A
        b_a_east = self.east_B - self.east_A
        c_b_east = self.east_C - self.east_B
        c_b_north = self.north_C - self.north_B
        # crline axis in quadrant I
        if b_a_north > 0 and b_a_east > 0:
            self.azimuth = math.atan(b_a_east / b_a_north)
            if c_b_east > 0:
                self.invertedAxis = False
            else:
                self.invertedAxis = True
        # crline axis in quadrant IV
        elif b_a_north < 0 and b_a_east > 0:
            self.azimuth = -math.atan(b_a_east / (-b_a_north)) + math.pi
            if c_b_east > 0:
                self.invertedAxis = True
            else:
                self.invertedAxis = False
        # crline axis in quadrant II
        elif b_a_north > 0 and b_a_east < 0:
            self.azimuth = -math.atan(-b_a_east / b_a_north) + 2 * math.pi
            if c_b_east > 0:
                self.invertedAxis = False
            else:
                self.invertedAxis = True
        # crline axis in quadrant III
        elif b_a_north < 0 and b_a_east < 0:
            self.azimuth = math.atan(b_a_east / (-b_a_north)) + math.pi
            if c_b_east > 0:
                self.invertedAxis = True
            else:
                self.invertedAxis = False
        # crline axis on positive x
        elif b_a_north == 0 and b_a_east > 0:
            self.azimuth = 0.5 * math.pi
            if c_b_north > 0:
                self.invertedAxis = True
            else:
                self.invertedAxis = False
        # crline axis on negtive x
        elif b_a_north == 0 and b_a_east < 0:
            self.azimuth = 1.5 * math.pi
            if c_b_north < 0:
                self.invertedAxis = True
            else:
                self.invertedAxis = False
        # crline axis on positive y
        elif b_a_north > 0 and b_a_east == 0:
            self.azimuth = 0
            if c_b_east < 0:
                self.invertedAxis = True
            else:
                self.invertedAxis = False
        # crline axis on negative y
        elif b_a_north < 0 and b_a_east == 0:
            self.azimuth = math.pi
            if c_b_east > 0:
                self.invertedAxis = True
            else:
                self.invertedAxis = False

        self.azimuth = self.azimuth / math.pi * 180  # turn into degree

    def four_corner_on_canvas(self, canvas_width, canvas_height, scale_factor=0.8):
        """
        get the coordinaiton of four corners of survey area on canvas
        """
        # get four corner xy coordination
        inlines = np.array([self.startInline, self.startInline,
                            self.endInline, self.endInline])
        crlines = np.array([self.startCrline, self.endCrline,
                            self.endCrline, self.startCrline])
        x_coord, y_coord = self.line_2_coord(inlines, crlines)
        # find the minimum and maximum value of x and y
        x_sorted = np.sort(x_coord)
        y_sorted = np.sort(y_coord)
        x_min = x_sorted[0]
        x_max = x_sorted[-1]
        y_min = y_sorted[0]
        y_max = y_sorted[-1]
        # shift x y to zero
        x_coord = x_coord - x_min
        y_coord = y_coord - y_min
        # find the longer one in width and height
        width = x_max - x_min
        height = y_max - y_min
        max_dimen = max(width, height)
        # calculate shift value
        shift_x = canvas_width * (1-scale_factor)/2
        shift_y = canvas_height * (1-scale_factor)/2
        # shrink
        canvas_width *= scale_factor
        canvas_height *= scale_factor
        canvas_min_dimen = min(canvas_width, canvas_height)
        to_canvas_ratio = canvas_min_dimen / max_dimen
        x_coord = x_coord * to_canvas_ratio
        y_coord = y_coord * to_canvas_ratio
        # mirror y because origin of canvas is the upper left corner
        y_coord = canvas_height - y_coord
        # shift
        x_coord += shift_x
        y_coord += shift_y
        return x_coord, y_coord

if __name__ == '__main__':
    survey_file = Path("C:\\Users", 'yuhao', 'dropbox', 'ui_pygeopressure',
                       'pygeo_root', 'F3', '.survey')
    new_survey = SurveySetting(survey_file)
    print(new_survey.invertedAxis)
