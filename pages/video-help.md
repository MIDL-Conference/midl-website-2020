---
title: "Recording help"
---

# Recording help

This page is to help authors to record their presentation. Requirements of the said presentation are available in the [author instructions](author-instructions.html#video_instructions).

While we are unable to provide individualized technical support to help you create these videos, we provide on this page several examples on how to record a video of your presentation, and some instructions to convert the recording if needed.

Quick reminder of the requirement:

* `16/9` aspect ratio
* Resolution at least `1920x1080p`
* `20 frame per second` or more
* Saved in `.mp4` format
* Audio channel in `mono or stereo` (no 5.1 or any creative setup)
* Less than `200MB` in total

## Recording on MacOS
Quicktime (available on all MacOS installations) allows to easily record and edit your entire screen:

* [Record your screen](https://support.apple.com/en-us/HT208721)
* [Trim the resulting video](https://support.apple.com/guide/quicktime-player/trim-a-movie-or-clip-qtpf2115f6fd/mac)

## Recording with zoom
One possible approach to record a compatible video from content displayed on your computer screen and voice recorded via the computer microphone, is to record the presentation using Zoom, available to users on most platforms and in most countries:

> [https://ieeetv.ieee.org/ieeetv-specials/recording-your-presentation-with-zoom](https://ieeetv.ieee.org/ieeetv-specials/recording-your-presentation-with-zoom)


## Converting formats
[`ffmpeg`](https://ffmpeg.org/) (available on Linux, OSX and Windows) can be used to easily reencode a recording into `.mp4`:
<pre><code>ffmpeg -i input.avi output.mp4</code></pre>


## Reducing the video size
If you are a bit above the size limit of OpenReview, you can always recompress the recording. [For instance](https://unix.stackexchange.com/questions/28803/how-can-i-reduce-a-videos-size-with-ffmpeg):
<pre><code> ffmpeg -i input.mp4 -vcodec libx265 -crf 28 output.mp4</code></pre>
You can increase the compression level by pushing the `-crf` value a bit.


## Trim bits of the video
You may end-up with some unwanted sequence, when you start and stop the recording process. It is possible to [cut those bits quite easily](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg):
<pre><code>ffmpeg -ss [start] -i in.mp4 -t [duration] -c copy out.mp4</code></pre>


## Advanced users
Advanced users might want have more control on the recording. While it is more complex, and will certainly require some tuning (with the encoder parameters), this might give them more options to get exatly what they want.

### Recording with ffmpeg
[Recording a screen](https://trac.ffmpeg.org/wiki/Capture/Desktop) is possible with ffmpeg.

For instance on Linux, with a screen of `3840x2160` resolution:

<pre><code>ffmpeg -video_size 3840x2160 -framerate 25 -f x11grab -i :0.0 \
	-f pulse -ac 2 -i default \
	-c:v libx264 -crf 0 -preset veryfast raw_output.mp4</code></pre>

And then downsample it to `1080p`:

<pre><code>ffmpeg -i raw_output.mp4 -vf scale=1920:1080 output_1080p.mp4</code></pre>

If you also want to [include your webcam](https://trac.ffmpeg.org/wiki/Capture/Webcam) on the [bottom right](https://superuser.com/questions/1432254/merge-x11grab-with-v4l2-into-single-output-file) corner of the video:

<pre><code>ffmpeg -video_size 1920x1080 -framerate 25 -f x11grab -i :0.0 \
	-f v4l2 -framerate 25 -video_size 640x480 -i /dev/video0 \
	-filter_complex "[0][1]overlay=x=W-w:y=H-h" \
	-f pulse -ac 2 -i default \
	-c:v libx264 -crf 0 -preset veryfast raw_output_webcam.mp4</code></pre>