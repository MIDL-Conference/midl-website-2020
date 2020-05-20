---
title: "Video help"
---

# Video help

While we are unable to provide individualized technical support to help you create these videos, we provide on this page several examples on how to record a video of your presentation, and some instructions to convert the recording if needed

## Recording with zoom
One possible approach to record a compatible video from content displayed on your computer screen and voice recorded via the computer microphone, is to record the presentation using Zoom, available to users on most platforms and in most countries:

> [https://ieeetv.ieee.org/ieeetv-specials/recording-your-presentation-with-zoom](https://ieeetv.ieee.org/ieeetv-specials/recording-your-presentation-with-zoom)


## Converting formats
[`ffmpeg`](https://ffmpeg.org/) (available on Linux, OSX and Windows) can be used to easily reencode a recording into `.mp4`:

```
ffmpeg -i input.avi output.mp4
```
## Advanced users
Advanced users might want have more control on the recording process. While it is more complex, and will certainly require some tuning (with the encoder parameters), this might give them more options to get exatly what they want.

### Recording with ffmpeg
[Recording a screen](https://trac.ffmpeg.org/wiki/Capture/Desktop) is possible with ffmpeg.

For instance on Linux, with a screen with a resolution of `3840x2160`:

```
ffmpeg -video_size 3840x2160 -framerate 25 -f x11grab -i :0.0 -f pulse -ac 2 -i default -c:v libx264 -crf 0 -preset veryfast raw_output.mp4
```

And then downsample it to `1080p`:

```
ffmpeg -i raw_output.mp4 -vf scale=1920:1080 output_1080p.mp4
```

If you also want to [include your webcam](https://trac.ffmpeg.org/wiki/Capture/Webcam) on the [bottom right](https://superuser.com/questions/1432254/merge-x11grab-with-v4l2-into-single-output-file) corner of the video:

```
ffmpeg -video_size 1920x1080 -framerate 25 -f x11grab -i :0.0
	-f v4l2 -framerate 25 -video_size 640x480 -i /dev/video0
	-filter_complex "[0][1]overlay=x=W-w:y=H-h"
	-f pulse -ac 2 -i default
	-c:v libx264 -crf 0 -preset veryfast raw_output_webcam.mp4
```