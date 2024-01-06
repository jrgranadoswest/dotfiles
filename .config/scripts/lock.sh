#!/bin/sh

B='#00000000'  # blank
P='#000000cc' # 'pitch' black
C='#ffffff22'  # clear ish
D='#00995bff'  # default
T='#00995bee'  # text
W='#c94d70cc'  # wrong
# V='#bb00bbbb'  # verifying
V='#00aa6ccc'  # verifying

/usr/bin/i3lock \
--insidever-color=$P   \
--ringver-color=$V     \
\
--insidewrong-color=$P \
--ringwrong-color=$W   \
\
--inside-color=$B      \
--ring-color=$D        \
--line-color=$B        \
--separator-color=$D   \
\
--verif-color=$T        \
--wrong-color=$W        \
--time-color=$T        \
--date-color=$T        \
--layout-color=$T      \
--keyhl-color=$W	\
--bshl-color=$W        \
\
--screen 0            \
--time-str="%H:%M:%S"  \
--date-str="%A, %m %Y" \
--ring-width 15.0	\
--verif-text="verifying"	\
--date-size=18		\
--radius=180		\
--time-size=40		\
\
--fill	\
--image=/home/jrgw/images/arch.PNG \

# --pointer=win \

#--clock               \
#--indicator           \
# --blur 5              \


# --wrongtext="Nope!"
# --modsize=10
# --timefont=comic-sans
# --datefont=monofur
# etc

