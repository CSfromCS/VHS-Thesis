import time, board, busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
from scipy import ndimage

def set_up_thermal_camera(scl_port, sda_port):
    # i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
    i2c = busio.I2C(scl_port, sda_port, frequency=400000)
    mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
    mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_16_HZ # set refresh rate
    mlx_shape = (24,32) # mlx90640 shape

    return mlx

def set_up_plot():
    print("Wow!")

def get_thermal_cam_pic(file_name: str):
    print("Wow!")


"""
##########################################
# MLX90640 Thermal Camera w Raspberry Pi
# -- 2fps with Interpolation and Blitting
##########################################
#
import time,board,busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
from scipy import ndimage

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_16_HZ # set refresh rate
mlx_shape = (24,32) # mlx90640 shape

mlx_interp_val = 10 # interpolate # on each dimension
mlx_interp_shape = (mlx_shape[0]*mlx_interp_val,
                    mlx_shape[1]*mlx_interp_val) # new shape

fig = plt.figure(figsize=(12,9)) # start figure
ax = fig.add_subplot(111) # add subplot
fig.subplots_adjust(0.05,0.05,0.95,0.95) # get rid of unnecessary padding
therm1 = ax.imshow(np.zeros(mlx_interp_shape),interpolation='none',
                   cmap=plt.cm.bwr,vmin=25,vmax=45) # preemptive image
cbar = fig.colorbar(therm1) # setup colorbar
cbar.set_label('Temperature [$^{\circ}$C]',fontsize=14) # colorbar label

fig.canvas.draw() # draw figure to copy background
ax_background = fig.canvas.copy_from_bbox(ax.bbox) # copy background
fig.show() # show the figure before blitting

frame = np.zeros(mlx_shape[0]*mlx_shape[1]) # 768 pts
def plot_update():
    fig.canvas.restore_region(ax_background) # restore background
    mlx.getFrame(frame) # read mlx90640
    data_array = np.fliplr(np.reshape(frame,mlx_shape)) # reshape, flip data
    data_array = ndimage.zoom(data_array,mlx_interp_val) # interpolate
    therm1.set_array(data_array) # set data
    therm1.set_clim(vmin=np.min(data_array),vmax=np.max(data_array)) # set bounds
    cbar.on_mappable_changed(therm1) # update colorbar range

    ax.draw_artist(therm1) # draw new thermal image
    fig.canvas.blit(ax.bbox) # draw background
    fig.canvas.flush_events() # show the new image
    return

t_array = []
while True:
    t1 = time.monotonic() # for determining frame rate
    try:
        plot_update() # update plot
    except:
        continue
    # approximating frame rate
    t_array.append(time.monotonic()-t1)
    if len(t_array)>10:
        t_array = t_array[1:] # recent times for frame rate approx
    print('Frame Rate: {0:2.1f}fps'.format(len(t_array)/np.sum(t_array)))
"""

"""
##########################################
# MLX90640 Thermal Camera w Raspberry Pi
# -- 2Hz Sampling with Simple Routine
##########################################
#
import time,board,busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_8_HZ # set refresh rate
mlx_shape = (24,32)

# setup the figure for plotting
plt.ion() # enables interactive plotting
fig,ax = plt.subplots(figsize=(12,7))
therm1 = ax.imshow(np.zeros(mlx_shape),vmin=0,vmax=60) #start plot with zeros
cbar = fig.colorbar(therm1) # setup colorbar for temps
cbar.set_label('Temperature [$^{\circ}$C]',fontsize=14) # colorbar label

frame = np.zeros((24*32,)) # setup array for storing all 768 temperatures
t_array = []
while True:
    t1 = time.monotonic()
    try:
        mlx.getFrame(frame) # read MLX temperatures into frame var
        data_array = (np.reshape(frame,mlx_shape)) # reshape to 24x32
        therm1.set_data(np.fliplr(data_array)) # flip left to right
        therm1.set_clim(vmin=np.min(data_array),vmax=np.max(data_array)) # set bounds
        cbar.on_mappable_changed(therm1) # update colorbar range
        plt.pause(0.001) # required
        fig.savefig('mlx90640_test_fliplr.png',dpi=300,facecolor='#FCFCFC',
                    bbox_inches='tight') # comment out to speed up
        t_array.append(time.monotonic()-t1)
        print('Sample Rate: {0:2.1f}fps'.format(len(t_array)/np.sum(t_array)))
    except ValueError:
        continue # if error, just read again"""