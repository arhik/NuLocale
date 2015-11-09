#!/usr/bin/env python
# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""A simple client to read CPU usage and predict it in real time."""
import rospy
from std_msgs.msg import Float32MultiArray,Float32

import sys
import random
import math
import time

from collections import deque
import time

import psutil
import matplotlib.pyplot as plt


from nupic.data.inference_shifter import InferenceShifter
from nupic.frameworks.opf.modelfactory import ModelFactory

import model_params

SECONDS_PER_STEP = 0.1
WINDOW = 60

# # turn matplotlib interactive mode on (ion)
# plt.ion()
# fig = plt.figure()
# # plot title, legend, etc
# plt.title('CPU prediction example')
# plt.xlabel('time [s]')
# plt.ylabel('CPU usage [%]')


# pygame.init()
# pygame.mouse.set_visible(False)

# windowSize = (800,800)

# screen = pygame.display.set_mode(windowSize)

# font = pygame.font.SysFont("Times New Roman", 48)

# rendered_dot = font.render("*", 1, (25, 120, 120), (250,250,250))

# rendered_dot_size = rendered_dot.get_size()



x,y = 0,0


# def run():
#   """Poll CPU usage, make predictions, and plot the results. Runs forever."""
#   # Create the model for predicting CPU usage.
#   # model = ModelFactory.create(model_params.MODEL_PARAMS)
#   # model.enableInference({'predictedField': 'x'})
#   # # The shifter will align prediction and actual values.
#   # shifter = InferenceShifter()
#   # # Keep the last WINDOW predicted and actual values for plotting.
#   # actHistory = deque([0.0] * WINDOW, maxlen=60)
#   # predHistory = deque([0.0] * WINDOW, maxlen=60)

#   # # Initialize the plot lines that we will update with each new record.
#   # actline, = plt.plot(range(WINDOW), actHistory)
#   # predline, = plt.plot(range(WINDOW), predHistory)
#   # # Set the y-axis range.
#   # actline.axes.set_ylim(0, 100)
#   # predline.axes.set_ylim(0, 100)

#   while True:
    


def callback(data):
  rospy.loginfo(rospy.get_caller_id()+"I heard %s",data)
  print(data)
  [d1, d2, d3, d4, theta] = data.data

  print(str([d1, d2, d3, d4, theta]))
  # for event in pygame.event.get():
  #   if event.type == pygame.QUIT:
  #     sys.exit()


  # screen.fill((250,250,250))


  
  

  # s = time.time()

  # Get the CPU usage.
  #cpu = psutil.cpu_percent()  

  # Run the input through the model and shift the resulting prediction.
  modelInput = {'d1': d1,'d2':d2, 'd3': d3, 'd4': d4, 'theta': theta}
  result = shifter.shift(model.run(modelInput))

  # Update the trailing predicted and actual value deques.
  inference = result.inferences['multiStepBestPredictions'][5]
  # print(type(inference))
  # print("Inference %s",inference)
  global infer_pub
  infer_pub.publish(inference)
  
  
  if inference is not None:
    # screen.blit(rendered_dot, (inference,y))
    actHistory.append(result.rawInput['d2'])
    predHistory.append(inference)
    # pygame.display.update()
  # Redraw the chart with the new data.
  #actline.set_ydata(actHistory)  # update the data
  #predline.set_ydata(predHistory)  # update the data
  #plt.draw()
  #plt.legend( ('actual','predicted') )    

  # Make sure we wait a total of 2 seconds per iteration.
  # try: 
  #   plt.pause(SECONDS_PER_STEP)
  # except:
  #   pass
  

def sensory_input_subscriber():
  rospy.init_node("sensory_input_subscriber",anonymous=True)
  rospy.Subscriber("dist_theta",Float32MultiArray, callback)


  
  #rospy.init_node('sensor_inference_input_publisher', anonymous=True)

  rospy.spin()

if __name__=="__main__":
  model = ModelFactory.create(model_params.MODEL_PARAMS)
  model.enableInference({'predictedField': 'd2'})
  #model.enableInference({'predictedField': 'y'})
  # The shifter will align prediction and actual values.
  shifter = InferenceShifter()
  # Keep the last WINDOW predicted and actual values for plotting.
  actHistory = deque([0.0] * WINDOW, maxlen=60)
  predHistory = deque([0.0] * WINDOW, maxlen=60)

  # Initialize the plot lines that we will update with each new record.
  # actline, = plt.plot(range(WINDOW), actHistory)
  # predline, = plt.plot(range(WINDOW), predHistory)
  # # Set the y-axis range.
  # actline.axes.set_ylim(0, 800)
  # predline.axes.set_ylim(0, 800)
  infer_pub = rospy.Publisher('sensory_inference_stream_d2', Float32, queue_size=10)

  sensory_input_subscriber()
