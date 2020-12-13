import pyaudio
import struct
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

%matplotlib tk

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = int(RATE/20)

p = pyaudio.PyAudio()
# print(p.get_device_info_by_index(0)['defaultSampleRate'])
print(p.get_device_info_by_index(1))

stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                input=True, output=True, frames_per_buffer=CHUNK)


plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')

#fig, ax = plt.subplots()
#fig, (ax, ax2) = plt.subplots(2, figsize=(15, 8))

while True:

    data = stream.read(CHUNK)
    data = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')
    f, t, Sxx = signal.spectrogram(data, fs=CHUNK)
    dBS = 10 * np.log10(Sxx)
    plt.pcolormesh(t, f, dBS)
    plt.pause(0.05)

    # waveform

    # data = stream.read(CHUNK)
    # data_int = np.array(struct.unpack(
    #     str(2 * CHUNK) + 'B', data), dtype='b')[::2] + 127

    # ax.plot(data_int, '-')
    # plt.show()

    # spectrum

    # # variable for plotting
    # x = np.arange(0, 2 * CHUNK, 2)
    # x_fft = np.linspace(0, RATE, CHUNK)

    # # create a line object with random data
    # line = ax.plot(x, np.random.rand(CHUNK), '-', lw=2)
    # line_fft, = ax2.plot(x_fft
