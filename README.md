[Ba]king [Br]ead
==================

[![CircleCI](https://circleci.com/gh/kosma/bakingbread.svg?style=svg)](https://circleci.com/gh/kosma/bakingbread)

Sound cards have been used as oscilloscopes for a really long time. Why not
connect them in reverse? If the input can work, the output should too. Let's
draw pretty pictures! Or, more accurately, ugly clocks.

[![ScreenShot](https://raw.github.com/kosma/bakingbread/master/youtube.png)](http://youtu.be/xPzrCnYasj0)

Usage
-----

Connect your stereo sound card output to your oscilloscope in XY mode. Note:
when preparing the cable, don't remove insulation with your teeth - you'll
damage the enamel.

If you have ``libao``, compile with ``make`` and run with:

``./baking.py | ./bread``

If you don't, substitute any other player capable of reading raw audio in
unsigned, 8-bit, stereo, 44100Hz sample rate mode. Linux example:

``./baking.py | aplay -f U8 -c 2 -r 44100``

which works exactly the same but isn't as hip.

Why?
----

Because I was bored; because no one did it before (as far as I searched).

Limitations
-----------

Sound card output is band-limited. The implications, amongst others, are that
it's really hard to just draw in a *goto(x,y)* manner. I used some crude tricks
to prevent the dot from swinging wildly around the screen; alas, they are not
perfect and may cause flickering as a result. See
[this presentation](http://xiph.org/video/vid2.shtml) to learn enough DSP basics
to know how band-limiting affects signals (especially square waves).

The program was tested on a really old analog oscilloscope. If you own a digital
one, you may be disappointed. They don't really make good oscilloscopes anymore.
