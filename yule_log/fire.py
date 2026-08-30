from __future__ import print_function

import os
import sys

from asciimatics.effects import Print, Snow
from asciimatics.exceptions import ResizeScreenError
from asciimatics.renderers import ColourImageFile, FigletText, Fire, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen

TOP_TEXT = os.getenv("TOP_TEXT", "YULE")
BOTTOM_TEXT = os.getenv("BOTTOM_TEXT", "LOG")

YULE_LOG = ["""                                                                        .:'#'.         
                                                          `.,;;'+#@#####++++++#@;      
                                           .,::;'+#@@######++++++++++++++++++++++@'    
                       ````..:;+###@@@@@###+++++++++++++++++++++++++++++###+++++++#@`  
     .;++#######@@@###+++++++++++++++++++++++++++++++++++++#####++++++++++++++++++++#. 
   '+,`.,;@#+++++++++++++++++++++++++++++#############++++++++++++++++++++++++++++++#+`
 `#.:#+'#+.`'@++++#############+++++++++++++++++++++++++++++++++++++++++###++++++++++#:
 #:#:,+;#.'#`.##++++++++++++++++++++++++++++++++++++++++++++++++++####+++++++++++++++#+
;+;',:;,;:;,#,`+#+++++++++++++++###########################+++++++++++++++++++++++++++@
#;'.:'.``,':,+.`##+++++++++++++++++++++++++++++++++++++++++++++++++++#####+++++++++++##
@;+.:'.```;'`':`,@++++++++++++++++++++++++++++++++#++++#########+++++++++++++++++++++#'
'';:.;;```:;.:#``@#++#######+++++++++++++++++++++++++++++++++++++++++++++++++++++++++#.
.+;+`:::;'+@''#``'@++++++++++++++++++++++++++++++++++++++++++++######+##+++++++++++##. 
 ;;''`.+;:'.,#@@##@#####@@@@@@@++++++++++++++++++#########+++##################++#@;   
 `+,''``````.#.;@@@@@@@@##+++++++++++++#####+++++##@@####':,```               `..      
  `#,,@;```,@,``;@+++++++#####++++++++##@@##+:.``                                      
    ''``:;;,```;@++++++++++####@@+;:,.                                                 
     .+'.```,'@#####@#+';,.                                                            
        `;##':`                                                                        
"""]  # noqa: W291

x = YULE_LOG[0].split('\n')
LOG_HEIGHT = len(x)
LOG_LENGTH = len(x[0])
HALF_LOG_HEIGHT = LOG_HEIGHT // 2
HALF_LOG_LENGTH = LOG_LENGTH // 2

def figletfont(text):
    accented = [
        "à", "À",
        "â", "Â",
        "ä", "Ä",
        "á", "Á",
        "ç", "Ç",
        "è", "È",
        "é", "É",
        "ê", "Ê",
        "ë", "Ë",
        "ì", "Ì",
        "í", "Í",
        "î", "Î",
        "ï", "Ï",
        "ñ", "Ñ",
        "ò", "Ò",
        "ó", "Ó",
        "ô", "Ô",
        "ö", "Ö",
        "ß",
        "ù", "Ù",
        "ú", "Ú",
        "û", "Û",
        "ü", "Ü",
        "œ", "Œ",
        "æ", "Æ"
    ]
    for a in accented:
        if a in text:
            return "mono12"
        else:
            continue
    return "univers"

def yule_log(screen):
    screen_height = screen.height
    screen_width = screen.width
    log_x = (screen_width // 2) - HALF_LOG_LENGTH
    log_y = (screen_height // 2) + HALF_LOG_HEIGHT
    if screen_height < 30:
        log_y = screen_height // 3
    elif screen_height < 48:
        log_y = screen_height // 2

    scenes = []

    effects = [
        Snow(screen),
        Print(screen,
              Fire(screen.height - 10, 80, "*" * 70, 0.8, 60, screen.colours,
                   bg=screen.colours >= 256),
              0,
              speed=1,
              transparent=False),
        Print(screen,
              StaticRenderer(images=YULE_LOG),
              x=log_x,
              y=log_y,
              colour=1,
              speed=1,
              transparent=True),
    ]
    if screen_height > 40:
        effects += [
            Print(
                screen,
                FigletText(TOP_TEXT, font=figletfont(TOP_TEXT)),
                1,
                speed=1,
                start_frame=5),
            Print(
                screen,
                FigletText(BOTTOM_TEXT, font=figletfont(BOTTOM_TEXT)),
                10,
                speed=1,
                start_frame=15),
        ]

    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True)


def main():
    while True:
        try:
            Screen.wrapper(yule_log)
            sys.exit(0)
        except ResizeScreenError:
            pass


if __name__ == "__main__":
    main()
    # -p[hj p[[ hjh[]kj[] k ''[;hjuu]]]]     Hannah 24/12/2016
