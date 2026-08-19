#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on April 05, 2023, at 14:13
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.0'
expName = 'Day1'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'group': ['a','b','c','d'],
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='Z:\\FLACON\\Day1\\DAY1_rebuild_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='lightgray', colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcome" ---
welcome = visual.TextStim(win=win, name='welcome',
    text='Witamy w eksperymencie!',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
first = visual.TextStim(win=win, name='first',
    text='Naciśnij spację, aby kontynuować.',
    font='Open Sans',
    pos=(0, -0.35), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "instructions_1" ---
iText1 = visual.TextStim(win=win, name='iText1',
    text='CEL BADANIA\n\nW tym badaniu Twoim zadaniem będzie nauczenie się 40 słówek w języku obcym.\n\nNaciśnij spację, aby kontynuować.\n',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
iKey1 = keyboard.Keyboard()

# --- Initialize components for Routine "instructions2" ---
iText2 = visual.TextStim(win=win, name='iText2',
    text='PREZENTACJA SŁÓWEK\n\nNajpierw zobaczysz słowo w języku polskim lub grafikę odpowiadającą jego znaczeniu. Następnie zobaczysz odpowiednik tego słowa w języku obcym oraz usłyszysz jego wymowę. Na przykład:\n',
    font='Open Sans',
    pos=(0, 0.33), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
iImage1 = visual.ImageStim(
    win=win,
    name='iImage1', 
    image='Picture1.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, 0), size=(0.5, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
iImage2 = visual.ImageStim(
    win=win,
    name='iImage2', 
    image='Picture2.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, 0), size=(0.5, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
iText3 = visual.TextStim(win=win, name='iText3',
    text='Po przeczytaniu i wysłuchaniu słówka, naciśnij spację, aby przejść dalej.\n\nNaciśnij spację, aby kontynuować.\n',
    font='Open Sans',
    pos=(0, -0.38), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
instKey2 = keyboard.Keyboard()

# --- Initialize components for Routine "instructions3" ---
iText4 = visual.TextStim(win=win, name='iText4',
    text='TEST ZAPAMIĘTANIA SŁÓWEK\n\nPo prezentacji 4 słówek oraz ich odpowiedników, przejdziesz do krótkiego zadania sprawdzającego, jak dobrze udało Ci się zapamiętać zaprezentowane wcześniej słowa. \n\nW tym zadaniu, na środku ekranu zobaczysz słowo w języku polskim lub grafikę odpowiadającą jego znaczeniu. Jednocześnie, w czterech narożnikach ekranu zobaczysz cztery różne słówka w języku obcym. \n\nTwoim zadaniem będzie wybranie poprawnego odpowiednika tłumaczeniowego poprzez kliknięcie na nie myszką komputera.\n\nNaciśnij spację, aby kontynuować.\n',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
iKey3 = keyboard.Keyboard()

# --- Initialize components for Routine "isntructions4" ---
iText5 = visual.TextStim(win=win, name='iText5',
    text='Na przykład:',
    font='Open Sans',
    pos=(0, 0.3), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
iImage3 = visual.ImageStim(
    win=win,
    name='iImage3', 
    image='Picture3.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.35, 0), size=(0.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
iImage4 = visual.ImageStim(
    win=win,
    name='iImage4', 
    image='Picture4.png', mask=None, anchor='center',
    ori=0.0, pos=(0.35, 0), size=(0.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
iText6 = visual.TextStim(win=win, name='iText6',
    text='Naciśnij spację, aby kontynuować.',
    font='Open Sans',
    pos=(0, -0.35), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
iKey4 = keyboard.Keyboard()

# --- Initialize components for Routine "instructions5" ---
iText7 = visual.TextStim(win=win, name='iText7',
    text='Jeśli Twoja odpowiedź będzie poprawna, wybrane przez Ciebie słówko zostanie podświetlone na zielono:',
    font='Open Sans',
    pos=(0, 0.35), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
iImage5 = visual.ImageStim(
    win=win,
    name='iImage5', 
    image='Picture5.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.35, 0), size=(0.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
iImage6 = visual.ImageStim(
    win=win,
    name='iImage6', 
    image='Picture6.png', mask=None, anchor='center',
    ori=0.0, pos=(0.35, 0), size=(0.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
iText8 = visual.TextStim(win=win, name='iText8',
    text='Naciśnij spację, aby kontynuować.',
    font='Open Sans',
    pos=(0, -0.35), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
iKey6 = keyboard.Keyboard()

# --- Initialize components for Routine "instruction7" ---
iText7_2 = visual.TextStim(win=win, name='iText7_2',
    text='Jeśli Twoja odpowiedź będzie błędna, wybrane przez Ciebie słówko zostanie podświetlone na czerwono, a poprawna odpowiedź - na zielono:',
    font='Open Sans',
    pos=(0, 0.35), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
iImage5_2 = visual.ImageStim(
    win=win,
    name='iImage5_2', 
    image='Picture7.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.35, 0), size=(0.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
iImage6_2 = visual.ImageStim(
    win=win,
    name='iImage6_2', 
    image='Picture8.png', mask=None, anchor='center',
    ori=0.0, pos=(0.35, 0), size=(0.5, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
iText8_2 = visual.TextStim(win=win, name='iText8_2',
    text='Po naciśnięciu spacji przejdziesz do kolejnych słów.\n\n\n\nNaciśnij spację, aby kontynuować.\n',
    font='Open Sans',
    pos=(0, -0.35), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
iKey7 = keyboard.Keyboard()

# --- Initialize components for Routine "instruction8" ---
iText1_2 = visual.TextStim(win=win, name='iText1_2',
    text='Po zakończeniu testu zapamiętania słówek, przejdziesz do bloku kolejnych nowych słówek do nauczenia się, a następnie do kolejnych takich testów, których będzie łącznie 10 (po 4 nowe słówka w każdym bloku). \n\nPo ostatnim bloku przejdziesz do zadania podsumowującego, gdzie sprawdzisz, jak dobrze pamiętasz wszystkie 40 słów. \n\nNaciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
iKey1_2 = keyboard.Keyboard()

# --- Initialize components for Routine "exp1_1" ---
# Run 'Begin Experiment' code from e1Code1
#IMPORTS
import random

#COUNTERS
e1Count = 0
e1Focal1 = visual.TextStim(win=win, name='e1Focal1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e1PL = visual.TextStim(win=win, name='e1PL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "exp1_2" ---
e1Focal2 = visual.TextStim(win=win, name='e1Focal2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e1CON = visual.TextStim(win=win, name='e1CON',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
e1Sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='e1Sound')
e1Sound.setVolume(3.0)
e1Key = keyboard.Keyboard()
space0 = visual.TextStim(win=win, name='space0',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini1_1" ---
# Run 'Begin Experiment' code from m1Code1
m1Posi = [[-0.4,-0.4],[-0.4,0.4],[0.4,-0.4],[0.4,0.4]]

m1Count = 0
m1PL1 = visual.TextStim(win=win, name='m1PL1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
m1CON1 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m1CON1',
    depth=-2
)
m1CON1.buttonClock = core.Clock()
m1DIST1 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m1DIST1',
    depth=-3
)
m1DIST1.buttonClock = core.Clock()
m1DIST2 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m1DIST2',
    depth=-4
)
m1DIST2.buttonClock = core.Clock()
m1DIST3 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m1DIST3',
    depth=-5
)
m1DIST3.buttonClock = core.Clock()
m1Mouse = event.Mouse(win=win)
x, y = [None, None]
m1Mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "mini1_2" ---
m1CorrPL = visual.TextStim(win=win, name='m1CorrPL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
m1CorrCON = visual.TextStim(win=win, name='m1CorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m1Sound1 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m1Sound1')
m1Sound1.setVolume(3.0)
space1 = visual.TextStim(win=win, name='space1',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
m1Key1 = keyboard.Keyboard()

# --- Initialize components for Routine "mini1_3" ---
m1IncorrPL = visual.TextStim(win=win, name='m1IncorrPL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
m1IncorrCON = visual.TextStim(win=win, name='m1IncorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m1IncorrDIST = visual.TextStim(win=win, name='m1IncorrDIST',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
m1Sound2 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m1Sound2')
m1Sound2.setVolume(3.0)
space2 = visual.TextStim(win=win, name='space2',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
m1Key2 = keyboard.Keyboard()

# --- Initialize components for Routine "exp2_1" ---
# Run 'Begin Experiment' code from e2Code1
e2Count = 0
e2Focal1 = visual.TextStim(win=win, name='e2Focal1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e2PL = visual.ImageStim(
    win=win,
    name='e2PL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "exp2_2" ---
e2Focal2 = visual.TextStim(win=win, name='e2Focal2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e2CON = visual.TextStim(win=win, name='e2CON',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
e2Sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='e2Sound')
e2Sound.setVolume(3.0)
e2Key = keyboard.Keyboard()
space3 = visual.TextStim(win=win, name='space3',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini2_1" ---
# Run 'Begin Experiment' code from m2Code1
m2Posi = [[-0.4,-0.4],[-0.4,0.4],[0.4,-0.4],[0.4,0.4]]

m2Count = 0
m2PL1 = visual.ImageStim(
    win=win,
    name='m2PL1', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
m2CON = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m2CON',
    depth=-2
)
m2CON.buttonClock = core.Clock()
m2DIST1 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m2DIST1',
    depth=-3
)
m2DIST1.buttonClock = core.Clock()
m2DIST2 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m2DIST2',
    depth=-4
)
m2DIST2.buttonClock = core.Clock()
m2DIST3 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m2DIST3',
    depth=-5
)
m2DIST3.buttonClock = core.Clock()
m2Mouse = event.Mouse(win=win)
x, y = [None, None]
m2Mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "mini2_2" ---
m2CorrPL = visual.ImageStim(
    win=win,
    name='m2CorrPL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
m2CorrCON = visual.TextStim(win=win, name='m2CorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m2Sound1 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m2Sound1')
m2Sound1.setVolume(3.0)
m2key1 = keyboard.Keyboard()
space4 = visual.TextStim(win=win, name='space4',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini2_3" ---
m2IncorrPL = visual.ImageStim(
    win=win,
    name='m2IncorrPL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
m2IncorrCON = visual.TextStim(win=win, name='m2IncorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m2IncorrDIST = visual.TextStim(win=win, name='m2IncorrDIST',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
m2Sound2 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m2Sound2')
m2Sound2.setVolume(3.0)
m2Key2 = keyboard.Keyboard()
space5 = visual.TextStim(win=win, name='space5',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "exp3_1" ---
# Run 'Begin Experiment' code from e3Code1
#COUNTERS
e3Count = 0
e3Focal1 = visual.TextStim(win=win, name='e3Focal1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e3PL = visual.TextStim(win=win, name='e3PL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "exp3_2" ---
e3Focal2 = visual.TextStim(win=win, name='e3Focal2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e3Con = visual.TextStim(win=win, name='e3Con',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
e3Sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='e3Sound')
e3Sound.setVolume(3.0)
e3Key = keyboard.Keyboard()
space6 = visual.TextStim(win=win, name='space6',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini3_1" ---
# Run 'Begin Experiment' code from m3Code1
m3Posi = [[-0.4,-0.4],[-0.4,0.4],[0.4,-0.4],[0.4,0.4]]

m3Count = 0
m3PL = visual.TextStim(win=win, name='m3PL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
m3CON = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m3CON',
    depth=-2
)
m3CON.buttonClock = core.Clock()
m3DIST1 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m3DIST1',
    depth=-3
)
m3DIST1.buttonClock = core.Clock()
m3DIST2 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m3DIST2',
    depth=-4
)
m3DIST2.buttonClock = core.Clock()
m3DIST3 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m3DIST3',
    depth=-5
)
m3DIST3.buttonClock = core.Clock()
m3Mouse = event.Mouse(win=win)
x, y = [None, None]
m3Mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "mini3_2" ---
m3CorrPL = visual.TextStim(win=win, name='m3CorrPL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
m3CorrCON = visual.TextStim(win=win, name='m3CorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m3Sound1 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m3Sound1')
m3Sound1.setVolume(3.0)
m2Key1 = keyboard.Keyboard()
space7 = visual.TextStim(win=win, name='space7',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini3_3" ---
m3IncorrPL = visual.TextStim(win=win, name='m3IncorrPL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
m3IncorrCON = visual.TextStim(win=win, name='m3IncorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m3IncorrDIST = visual.TextStim(win=win, name='m3IncorrDIST',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
m3Sound2 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m3Sound2')
m3Sound2.setVolume(3.0)
m3Key2 = keyboard.Keyboard()
space8 = visual.TextStim(win=win, name='space8',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "exp4_1" ---
# Run 'Begin Experiment' code from e4Code1
e4Count = 0
e4Focal1 = visual.TextStim(win=win, name='e4Focal1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e4PL = visual.ImageStim(
    win=win,
    name='e4PL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "exp4_2" ---
e4Focal2 = visual.TextStim(win=win, name='e4Focal2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e4CON = visual.TextStim(win=win, name='e4CON',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
e4Sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='e4Sound')
e4Sound.setVolume(3.0)
e4Key = keyboard.Keyboard()
space9 = visual.TextStim(win=win, name='space9',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini4_1" ---
# Run 'Begin Experiment' code from m4Code1_2
m4Posi = [[-0.4,-0.4],[-0.4,0.4],[0.4,-0.4],[0.4,0.4]]

m4Count = 0
m4PL = visual.ImageStim(
    win=win,
    name='m4PL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
m4CON = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m4CON',
    depth=-2
)
m4CON.buttonClock = core.Clock()
m4DIST1 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m4DIST1',
    depth=-3
)
m4DIST1.buttonClock = core.Clock()
m4DIST2 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m4DIST2',
    depth=-4
)
m4DIST2.buttonClock = core.Clock()
m4DIST3 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m4DIST3',
    depth=-5
)
m4DIST3.buttonClock = core.Clock()
m4Mouse = event.Mouse(win=win)
x, y = [None, None]
m4Mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "mini4_2" ---
m4CorrPL = visual.ImageStim(
    win=win,
    name='m4CorrPL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
m4CorrCON = visual.TextStim(win=win, name='m4CorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m4Sound1 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m4Sound1')
m4Sound1.setVolume(3.0)
m4Key1 = keyboard.Keyboard()
space10 = visual.TextStim(win=win, name='space10',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini4_3" ---
m4IncorrPL = visual.ImageStim(
    win=win,
    name='m4IncorrPL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
m4IncorrCON = visual.TextStim(win=win, name='m4IncorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m4IncorrDIST = visual.TextStim(win=win, name='m4IncorrDIST',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
m4Sound2 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m4Sound2')
m4Sound2.setVolume(3.0)
m4Key2 = keyboard.Keyboard()
space11 = visual.TextStim(win=win, name='space11',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "exp5_1" ---
# Run 'Begin Experiment' code from e5Code1
#COUNTERS
e5Count = 0
e5Focal1 = visual.TextStim(win=win, name='e5Focal1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e5PL = visual.TextStim(win=win, name='e5PL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "exp5_2" ---
e5Focal2 = visual.TextStim(win=win, name='e5Focal2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e5Con = visual.TextStim(win=win, name='e5Con',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
e5Sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='e5Sound')
e5Sound.setVolume(3.0)
e5Key = keyboard.Keyboard()
space12 = visual.TextStim(win=win, name='space12',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini5_1" ---
# Run 'Begin Experiment' code from m5Code1
m5Posi = [[-0.4,-0.4],[-0.4,0.4],[0.4,-0.4],[0.4,0.4]]

m5Count = 0
m5PL = visual.TextStim(win=win, name='m5PL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
m5CON = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m5CON',
    depth=-2
)
m5CON.buttonClock = core.Clock()
m5DIST1 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m5DIST1',
    depth=-3
)
m5DIST1.buttonClock = core.Clock()
m5DIST2 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m5DIST2',
    depth=-4
)
m5DIST2.buttonClock = core.Clock()
m5DIST3 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m5DIST3',
    depth=-5
)
m5DIST3.buttonClock = core.Clock()
m5Mouse = event.Mouse(win=win)
x, y = [None, None]
m5Mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "mini5_2" ---
m5CorrPL = visual.TextStim(win=win, name='m5CorrPL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
m5CorrCON = visual.TextStim(win=win, name='m5CorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m5Sound1 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m5Sound1')
m5Sound1.setVolume(3.0)
m5Key1 = keyboard.Keyboard()
space13 = visual.TextStim(win=win, name='space13',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini5_3" ---
m5IncorrPL = visual.TextStim(win=win, name='m5IncorrPL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
m5IncorrCON = visual.TextStim(win=win, name='m5IncorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m5IncorrDIST = visual.TextStim(win=win, name='m5IncorrDIST',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
m5Sound2 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m5Sound2')
m5Sound2.setVolume(3.0)
m5Key2 = keyboard.Keyboard()
space14 = visual.TextStim(win=win, name='space14',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "exp6_1" ---
# Run 'Begin Experiment' code from e6Code1
e6Count = 0
e6Focal1 = visual.TextStim(win=win, name='e6Focal1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e6PL = visual.ImageStim(
    win=win,
    name='e6PL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "exp6_2" ---
e6Focal2 = visual.TextStim(win=win, name='e6Focal2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e6CON = visual.TextStim(win=win, name='e6CON',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
e6Sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='e6Sound')
e6Sound.setVolume(3.0)
e6Key = keyboard.Keyboard()
space15 = visual.TextStim(win=win, name='space15',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini6_1" ---
# Run 'Begin Experiment' code from m6Code1
m6Posi = [[-0.4,-0.4],[-0.4,0.4],[0.4,-0.4],[0.4,0.4]]

m6Count = 0
m6PL = visual.ImageStim(
    win=win,
    name='m6PL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
m6CON = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m6CON',
    depth=-2
)
m6CON.buttonClock = core.Clock()
m6DIST1 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m6DIST1',
    depth=-3
)
m6DIST1.buttonClock = core.Clock()
m6DIST2 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m6DIST2',
    depth=-4
)
m6DIST2.buttonClock = core.Clock()
m6DIST3 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m6DIST3',
    depth=-5
)
m6DIST3.buttonClock = core.Clock()
m6Mouse = event.Mouse(win=win)
x, y = [None, None]
m6Mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "mini6_2" ---
m6CorrPL = visual.ImageStim(
    win=win,
    name='m6CorrPL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
m6CorrCON = visual.TextStim(win=win, name='m6CorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m6Sound1 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m6Sound1')
m6Sound1.setVolume(3.0)
m6Key1 = keyboard.Keyboard()
space16 = visual.TextStim(win=win, name='space16',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini6_3" ---
m6IncorrPL = visual.ImageStim(
    win=win,
    name='m6IncorrPL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
m6IncorrCON = visual.TextStim(win=win, name='m6IncorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m6IncorrDIST = visual.TextStim(win=win, name='m6IncorrDIST',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
m6Sound2 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m6Sound2')
m6Sound2.setVolume(3.0)
m6Key2 = keyboard.Keyboard()
space17 = visual.TextStim(win=win, name='space17',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "exp7_1" ---
# Run 'Begin Experiment' code from e7Code1
#COUNTERS
e7Count = 0
e7Focal1 = visual.TextStim(win=win, name='e7Focal1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e7PL = visual.TextStim(win=win, name='e7PL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "exp7_2" ---
e7Focal2 = visual.TextStim(win=win, name='e7Focal2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e7CON = visual.TextStim(win=win, name='e7CON',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
e7Sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='e7Sound')
e7Sound.setVolume(3.0)
e7Key = keyboard.Keyboard()
space18 = visual.TextStim(win=win, name='space18',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini7_1" ---
# Run 'Begin Experiment' code from m7Code1
m7Posi = [[-0.4,-0.4],[-0.4,0.4],[0.4,-0.4],[0.4,0.4]]

m7Count = 0
m7PL = visual.TextStim(win=win, name='m7PL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
m7CON = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m7CON',
    depth=-2
)
m7CON.buttonClock = core.Clock()
m7DIST1 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m7DIST1',
    depth=-3
)
m7DIST1.buttonClock = core.Clock()
m7DIST2 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m7DIST2',
    depth=-4
)
m7DIST2.buttonClock = core.Clock()
m7DIST3 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m7DIST3',
    depth=-5
)
m7DIST3.buttonClock = core.Clock()
m7Mouse = event.Mouse(win=win)
x, y = [None, None]
m7Mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "mini7_2" ---
m7CorrPL = visual.TextStim(win=win, name='m7CorrPL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
m7CorrCON = visual.TextStim(win=win, name='m7CorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m7Sound1 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m7Sound1')
m7Sound1.setVolume(3.0)
m7Key1 = keyboard.Keyboard()
space19 = visual.TextStim(win=win, name='space19',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini7_3" ---
m7IncorrPL = visual.TextStim(win=win, name='m7IncorrPL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
m7IncorrCON = visual.TextStim(win=win, name='m7IncorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m7IncorrDIST = visual.TextStim(win=win, name='m7IncorrDIST',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
m7Sound2 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m7Sound2')
m7Sound2.setVolume(3.0)
m7Key2 = keyboard.Keyboard()
space20 = visual.TextStim(win=win, name='space20',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "exp8_1" ---
# Run 'Begin Experiment' code from e8Code1
e8Count = 0
e8Focal1 = visual.TextStim(win=win, name='e8Focal1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e8PL = visual.ImageStim(
    win=win,
    name='e8PL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "exp8_2" ---
e8Focal2 = visual.TextStim(win=win, name='e8Focal2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e8CON = visual.TextStim(win=win, name='e8CON',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
e8Sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='e8Sound')
e8Sound.setVolume(3.0)
e8Key = keyboard.Keyboard()
space21 = visual.TextStim(win=win, name='space21',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini8_1" ---
# Run 'Begin Experiment' code from m8Code1
m8Posi = [[-0.4,-0.4],[-0.4,0.4],[0.4,-0.4],[0.4,0.4]]

m8Count = 0
m8PL = visual.ImageStim(
    win=win,
    name='m8PL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
m8CON = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m8CON',
    depth=-2
)
m8CON.buttonClock = core.Clock()
m8DIST1 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m8DIST1',
    depth=-3
)
m8DIST1.buttonClock = core.Clock()
m8DIST2 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m8DIST2',
    depth=-4
)
m8DIST2.buttonClock = core.Clock()
m8DIST3 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m8DIST3',
    depth=-5
)
m8DIST3.buttonClock = core.Clock()
m8Mouse = event.Mouse(win=win)
x, y = [None, None]
m8Mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "mini8_2" ---
m8CorrPL = visual.ImageStim(
    win=win,
    name='m8CorrPL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
m8CorrCON = visual.TextStim(win=win, name='m8CorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m8Sound1 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m8Sound1')
m8Sound1.setVolume(3.0)
m8Key1 = keyboard.Keyboard()
space22 = visual.TextStim(win=win, name='space22',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini8_3" ---
m8IncorrPL = visual.ImageStim(
    win=win,
    name='m8IncorrPL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
m8IncorrCON = visual.TextStim(win=win, name='m8IncorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m8IncorrDIST = visual.TextStim(win=win, name='m8IncorrDIST',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
m8Sound2 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m8Sound2')
m8Sound2.setVolume(3.0)
m8Key2 = keyboard.Keyboard()
space23 = visual.TextStim(win=win, name='space23',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "exp9_1" ---
# Run 'Begin Experiment' code from e9Code1
#COUNTERS
e9Count = 0
e9Focal1 = visual.TextStim(win=win, name='e9Focal1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e9PL = visual.TextStim(win=win, name='e9PL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "exp9_2" ---
e9Focal2 = visual.TextStim(win=win, name='e9Focal2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e9CON = visual.TextStim(win=win, name='e9CON',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
e9Sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='e9Sound')
e9Sound.setVolume(3.0)
e9Key = keyboard.Keyboard()
space24 = visual.TextStim(win=win, name='space24',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini9_1" ---
# Run 'Begin Experiment' code from m9Code1
m9Posi = [[-0.4,-0.4],[-0.4,0.4],[0.4,-0.4],[0.4,0.4]]

m9Count = 0
m9PL = visual.TextStim(win=win, name='m9PL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
m9CON = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m9CON',
    depth=-2
)
m9CON.buttonClock = core.Clock()
m9DIST1 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m9DIST1',
    depth=-3
)
m9DIST1.buttonClock = core.Clock()
m9DIST2 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m9DIST2',
    depth=-4
)
m9DIST2.buttonClock = core.Clock()
m9DIST3 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m9DIST3',
    depth=-5
)
m9DIST3.buttonClock = core.Clock()
m9Mouse = event.Mouse(win=win)
x, y = [None, None]
m9Mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "mini9_2" ---
m9CorrPL = visual.TextStim(win=win, name='m9CorrPL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
m9CorrCON = visual.TextStim(win=win, name='m9CorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m9Sound1 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m9Sound1')
m9Sound1.setVolume(3.0)
m9Key1 = keyboard.Keyboard()
space25 = visual.TextStim(win=win, name='space25',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini9_3" ---
m9IncorrPL = visual.TextStim(win=win, name='m9IncorrPL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
m9IncorrCON = visual.TextStim(win=win, name='m9IncorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m9incorrDIST = visual.TextStim(win=win, name='m9incorrDIST',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
m9Sound2 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m9Sound2')
m9Sound2.setVolume(3.0)
m9Key2 = keyboard.Keyboard()
space26 = visual.TextStim(win=win, name='space26',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "exp10_1" ---
# Run 'Begin Experiment' code from e0Code1
e0Count = 0
e0Focal1 = visual.TextStim(win=win, name='e0Focal1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e0PL = visual.ImageStim(
    win=win,
    name='e0PL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "exp10_2" ---
e0Focal2 = visual.TextStim(win=win, name='e0Focal2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
e0CON = visual.TextStim(win=win, name='e0CON',
    text='',
    font='Times New Roman',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
e0Sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='e0Sound')
e0Sound.setVolume(3.0)
e0Key = keyboard.Keyboard()
space27 = visual.TextStim(win=win, name='space27',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini10_1" ---
# Run 'Begin Experiment' code from m0Code1
m0Posi = [[-0.4,-0.4],[-0.4,0.4],[0.4,-0.4],[0.4,0.4]]

m0Count = 0
m0PL = visual.ImageStim(
    win=win,
    name='m0PL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
m0CON = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m0CON',
    depth=-2
)
m0CON.buttonClock = core.Clock()
m0DIST1 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m0DIST1',
    depth=-3
)
m0DIST1.buttonClock = core.Clock()
m0DIST2 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m0DIST2',
    depth=-4
)
m0DIST2.buttonClock = core.Clock()
m0DIST3 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='m0DIST3',
    depth=-5
)
m0DIST3.buttonClock = core.Clock()
m0Mouse = event.Mouse(win=win)
x, y = [None, None]
m0Mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "mini10_2" ---
m0CorrPL = visual.ImageStim(
    win=win,
    name='m0CorrPL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
m0CorrCON = visual.TextStim(win=win, name='m0CorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m0Sound1 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m0Sound1')
m0Sound1.setVolume(3.0)
m0Key1 = keyboard.Keyboard()
space28 = visual.TextStim(win=win, name='space28',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "mini10_3" ---
m0IncorrPL = visual.ImageStim(
    win=win,
    name='m0IncorrPL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
m0IncorrCON = visual.TextStim(win=win, name='m0IncorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
m0IncorrDIST = visual.TextStim(win=win, name='m0IncorrDIST',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
m0Sound2 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='m0Sound2')
m0Sound2.setVolume(3.0)
m0Key2 = keyboard.Keyboard()
space29 = visual.TextStim(win=win, name='space29',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "learnTimer_End" ---

# --- Initialize components for Routine "instruction9" ---
iText1_3 = visual.TextStim(win=win, name='iText1_3',
    text='Przed Tobą 5-minutowa przerwa w eksperymencie.\n\nPo przerwie rozpoczniesz test sprawdzający, jak dobrze pamiętasz wszystkie 40 słów.\n\nNaciśnij spację, aby rozpocząć 5-minutową przerwę.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
iKey1_3 = keyboard.Keyboard()

# --- Initialize components for Routine "routine_5_minute_break" ---
timer_text = visual.TextStim(win=win, name='timer_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='Black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "instructions10" ---
iText1_4 = visual.TextStim(win=win, name='iText1_4',
    text='Za chwilę rozpoczniesz test sprawdzający, jak dobrze pamiętasz wszystkie 40 słów.\n\nNaciśnij spację, aby rozpocząć test.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
iKey1_4 = keyboard.Keyboard()

# --- Initialize components for Routine "afcRoute_Code" ---
# Run 'Begin Experiment' code from afcRoutingCode
orthoRep = 0
imgRep = 0
incorrCount = 0

# --- Initialize components for Routine "afc1_1" ---
# Run 'Begin Experiment' code from a1Code1
a1Posi = [[-0.4,-0.4],[-0.4,0.4],[0.4,-0.4],[0.4,0.4]]
orthoCount = 0
totalCount = 0
a1PL = visual.TextStim(win=win, name='a1PL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
a1CON = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='a1CON',
    depth=-2
)
a1CON.buttonClock = core.Clock()
a1DIST1 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='a1DIST1',
    depth=-3
)
a1DIST1.buttonClock = core.Clock()
a1DIST2 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='a1DIST2',
    depth=-4
)
a1DIST2.buttonClock = core.Clock()
a1DIST3 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='a1DIST3',
    depth=-5
)
a1DIST3.buttonClock = core.Clock()
a1Mouse = event.Mouse(win=win)
x, y = [None, None]
a1Mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "afc1_2" ---
a1CORRPL = visual.TextStim(win=win, name='a1CORRPL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
a1CorrCON = visual.TextStim(win=win, name='a1CorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
a1Sound1 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='a1Sound1')
a1Sound1.setVolume(3.0)
a1Key1 = keyboard.Keyboard()
space30 = visual.TextStim(win=win, name='space30',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "afc1_3" ---
a1IncorrPL = visual.TextStim(win=win, name='a1IncorrPL',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
a1IncorrCON = visual.TextStim(win=win, name='a1IncorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
a1IncorrDIST = visual.TextStim(win=win, name='a1IncorrDIST',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
a1Sound2 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='a1Sound2')
a1Sound2.setVolume(3.0)
a1Key2 = keyboard.Keyboard()
space31 = visual.TextStim(win=win, name='space31',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.06), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "afc1_4" ---

# --- Initialize components for Routine "afc2_1" ---
# Run 'Begin Experiment' code from a2Code1
a2Posi = [[-0.4,-0.4],[-0.4,0.4],[0.4,-0.4],[0.4,0.4]]
imgCount = 0
a2PL = visual.ImageStim(
    win=win,
    name='a2PL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
a2CON = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='a2CON',
    depth=-2
)
a2CON.buttonClock = core.Clock()
a2DIST1 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='a2DIST1',
    depth=-3
)
a2DIST1.buttonClock = core.Clock()
a2DIST2 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='a2DIST2',
    depth=-4
)
a2DIST2.buttonClock = core.Clock()
a2DIST3 = visual.ButtonStim(win, 
    text='', font='Times New Roman',
    pos=[0,0],
    letterHeight=0.07,
    size=None, borderWidth=0.0,
    fillColor='lightgray', borderColor=None,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    padding=None,
    anchor='center',
    name='a2DIST3',
    depth=-5
)
a2DIST3.buttonClock = core.Clock()
a2Mouse = event.Mouse(win=win)
x, y = [None, None]
a2Mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "afc2_2" ---
a2CorrPL = visual.ImageStim(
    win=win,
    name='a2CorrPL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
a2CorrCON = visual.TextStim(win=win, name='a2CorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
a2Sound1 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='a2Sound1')
a2Sound1.setVolume(3.0)
a2Key1 = keyboard.Keyboard()
space32 = visual.TextStim(win=win, name='space32',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "afc2_3" ---
a2IncorrPL = visual.ImageStim(
    win=win,
    name='a2IncorrPL', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
a2IncorrCON = visual.TextStim(win=win, name='a2IncorrCON',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='darkgreen', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
a2IncorrDIST = visual.TextStim(win=win, name='a2IncorrDIST',
    text='',
    font='Times New Roman',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='firebrick', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
a2Sound2 = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='a2Sound2')
a2Sound2.setVolume(3.0)
a2Key2 = keyboard.Keyboard()
space33 = visual.TextStim(win=win, name='space33',
    text='Naciśnij spację, aby kontynuować',
    font='Open Sans',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "afc2_4" ---

# --- Initialize components for Routine "afcEnd_Code" ---

# --- Initialize components for Routine "endOfExp" ---
endOfExp_text = visual.TextStim(win=win, name='endOfExp_text',
    text='Dziękujemy.\nZakończyłeś eksperyment!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
endofExp_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
WelcomeComponents = [welcome, key_resp, first]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome* updates
    
    # if welcome is starting this frame...
    if welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome.frameNStart = frameN  # exact frame index
        welcome.tStart = t  # local t and not account for scr refresh
        welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome, 'tStartRefresh')  # time at next scr refresh
        # update status
        welcome.status = STARTED
        welcome.setAutoDraw(True)
    
    # if welcome is active this frame...
    if welcome.status == STARTED:
        # update params
        pass
    
    # *key_resp* updates
    
    # if key_resp is starting this frame...
    if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # update status
        key_resp.status = STARTED
        # keyboard checking is just starting
        key_resp.clock.reset()  # now t=0
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *first* updates
    
    # if first is starting this frame...
    if first.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        first.frameNStart = frameN  # exact frame index
        first.tStart = t  # local t and not account for scr refresh
        first.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(first, 'tStartRefresh')  # time at next scr refresh
        # update status
        first.status = STARTED
        first.setAutoDraw(True)
    
    # if first is active this frame...
    if first.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions_1" ---
continueRoutine = True
# update component parameters for each repeat
iKey1.keys = []
iKey1.rt = []
_iKey1_allKeys = []
# keep track of which components have finished
instructions_1Components = [iText1, iKey1]
for thisComponent in instructions_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions_1" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *iText1* updates
    
    # if iText1 is starting this frame...
    if iText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iText1.frameNStart = frameN  # exact frame index
        iText1.tStart = t  # local t and not account for scr refresh
        iText1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iText1, 'tStartRefresh')  # time at next scr refresh
        # update status
        iText1.status = STARTED
        iText1.setAutoDraw(True)
    
    # if iText1 is active this frame...
    if iText1.status == STARTED:
        # update params
        pass
    
    # *iKey1* updates
    waitOnFlip = False
    
    # if iKey1 is starting this frame...
    if iKey1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iKey1.frameNStart = frameN  # exact frame index
        iKey1.tStart = t  # local t and not account for scr refresh
        iKey1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iKey1, 'tStartRefresh')  # time at next scr refresh
        # update status
        iKey1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(iKey1.clock.reset)  # t=0 on next screen flip
    if iKey1.status == STARTED and not waitOnFlip:
        theseKeys = iKey1.getKeys(keyList=['space'], waitRelease=False)
        _iKey1_allKeys.extend(theseKeys)
        if len(_iKey1_allKeys):
            iKey1.keys = _iKey1_allKeys[-1].name  # just the last key pressed
            iKey1.rt = _iKey1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_1" ---
for thisComponent in instructions_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions2" ---
continueRoutine = True
# update component parameters for each repeat
instKey2.keys = []
instKey2.rt = []
_instKey2_allKeys = []
# keep track of which components have finished
instructions2Components = [iText2, iImage1, iImage2, iText3, instKey2]
for thisComponent in instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *iText2* updates
    
    # if iText2 is starting this frame...
    if iText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iText2.frameNStart = frameN  # exact frame index
        iText2.tStart = t  # local t and not account for scr refresh
        iText2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iText2, 'tStartRefresh')  # time at next scr refresh
        # update status
        iText2.status = STARTED
        iText2.setAutoDraw(True)
    
    # if iText2 is active this frame...
    if iText2.status == STARTED:
        # update params
        pass
    
    # *iImage1* updates
    
    # if iImage1 is starting this frame...
    if iImage1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iImage1.frameNStart = frameN  # exact frame index
        iImage1.tStart = t  # local t and not account for scr refresh
        iImage1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iImage1, 'tStartRefresh')  # time at next scr refresh
        # update status
        iImage1.status = STARTED
        iImage1.setAutoDraw(True)
    
    # if iImage1 is active this frame...
    if iImage1.status == STARTED:
        # update params
        pass
    
    # *iImage2* updates
    
    # if iImage2 is starting this frame...
    if iImage2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iImage2.frameNStart = frameN  # exact frame index
        iImage2.tStart = t  # local t and not account for scr refresh
        iImage2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iImage2, 'tStartRefresh')  # time at next scr refresh
        # update status
        iImage2.status = STARTED
        iImage2.setAutoDraw(True)
    
    # if iImage2 is active this frame...
    if iImage2.status == STARTED:
        # update params
        pass
    
    # *iText3* updates
    
    # if iText3 is starting this frame...
    if iText3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iText3.frameNStart = frameN  # exact frame index
        iText3.tStart = t  # local t and not account for scr refresh
        iText3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iText3, 'tStartRefresh')  # time at next scr refresh
        # update status
        iText3.status = STARTED
        iText3.setAutoDraw(True)
    
    # if iText3 is active this frame...
    if iText3.status == STARTED:
        # update params
        pass
    
    # *instKey2* updates
    
    # if instKey2 is starting this frame...
    if instKey2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instKey2.frameNStart = frameN  # exact frame index
        instKey2.tStart = t  # local t and not account for scr refresh
        instKey2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instKey2, 'tStartRefresh')  # time at next scr refresh
        # update status
        instKey2.status = STARTED
        # keyboard checking is just starting
        instKey2.clock.reset()  # now t=0
    if instKey2.status == STARTED:
        theseKeys = instKey2.getKeys(keyList=['space'], waitRelease=False)
        _instKey2_allKeys.extend(theseKeys)
        if len(_instKey2_allKeys):
            instKey2.keys = _instKey2_allKeys[-1].name  # just the last key pressed
            instKey2.rt = _instKey2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions2" ---
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions3" ---
continueRoutine = True
# update component parameters for each repeat
iKey3.keys = []
iKey3.rt = []
_iKey3_allKeys = []
# keep track of which components have finished
instructions3Components = [iText4, iKey3]
for thisComponent in instructions3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *iText4* updates
    
    # if iText4 is starting this frame...
    if iText4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iText4.frameNStart = frameN  # exact frame index
        iText4.tStart = t  # local t and not account for scr refresh
        iText4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iText4, 'tStartRefresh')  # time at next scr refresh
        # update status
        iText4.status = STARTED
        iText4.setAutoDraw(True)
    
    # if iText4 is active this frame...
    if iText4.status == STARTED:
        # update params
        pass
    
    # *iKey3* updates
    waitOnFlip = False
    
    # if iKey3 is starting this frame...
    if iKey3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iKey3.frameNStart = frameN  # exact frame index
        iKey3.tStart = t  # local t and not account for scr refresh
        iKey3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iKey3, 'tStartRefresh')  # time at next scr refresh
        # update status
        iKey3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(iKey3.clock.reset)  # t=0 on next screen flip
    if iKey3.status == STARTED and not waitOnFlip:
        theseKeys = iKey3.getKeys(keyList=['space'], waitRelease=False)
        _iKey3_allKeys.extend(theseKeys)
        if len(_iKey3_allKeys):
            iKey3.keys = _iKey3_allKeys[-1].name  # just the last key pressed
            iKey3.rt = _iKey3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions3" ---
for thisComponent in instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "isntructions4" ---
continueRoutine = True
# update component parameters for each repeat
iKey4.keys = []
iKey4.rt = []
_iKey4_allKeys = []
# keep track of which components have finished
isntructions4Components = [iText5, iImage3, iImage4, iText6, iKey4]
for thisComponent in isntructions4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "isntructions4" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *iText5* updates
    
    # if iText5 is starting this frame...
    if iText5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iText5.frameNStart = frameN  # exact frame index
        iText5.tStart = t  # local t and not account for scr refresh
        iText5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iText5, 'tStartRefresh')  # time at next scr refresh
        # update status
        iText5.status = STARTED
        iText5.setAutoDraw(True)
    
    # if iText5 is active this frame...
    if iText5.status == STARTED:
        # update params
        pass
    
    # *iImage3* updates
    
    # if iImage3 is starting this frame...
    if iImage3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iImage3.frameNStart = frameN  # exact frame index
        iImage3.tStart = t  # local t and not account for scr refresh
        iImage3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iImage3, 'tStartRefresh')  # time at next scr refresh
        # update status
        iImage3.status = STARTED
        iImage3.setAutoDraw(True)
    
    # if iImage3 is active this frame...
    if iImage3.status == STARTED:
        # update params
        pass
    
    # *iImage4* updates
    
    # if iImage4 is starting this frame...
    if iImage4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iImage4.frameNStart = frameN  # exact frame index
        iImage4.tStart = t  # local t and not account for scr refresh
        iImage4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iImage4, 'tStartRefresh')  # time at next scr refresh
        # update status
        iImage4.status = STARTED
        iImage4.setAutoDraw(True)
    
    # if iImage4 is active this frame...
    if iImage4.status == STARTED:
        # update params
        pass
    
    # *iText6* updates
    
    # if iText6 is starting this frame...
    if iText6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iText6.frameNStart = frameN  # exact frame index
        iText6.tStart = t  # local t and not account for scr refresh
        iText6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iText6, 'tStartRefresh')  # time at next scr refresh
        # update status
        iText6.status = STARTED
        iText6.setAutoDraw(True)
    
    # if iText6 is active this frame...
    if iText6.status == STARTED:
        # update params
        pass
    
    # *iKey4* updates
    
    # if iKey4 is starting this frame...
    if iKey4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iKey4.frameNStart = frameN  # exact frame index
        iKey4.tStart = t  # local t and not account for scr refresh
        iKey4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iKey4, 'tStartRefresh')  # time at next scr refresh
        # update status
        iKey4.status = STARTED
        # keyboard checking is just starting
        iKey4.clock.reset()  # now t=0
    if iKey4.status == STARTED:
        theseKeys = iKey4.getKeys(keyList=['space'], waitRelease=False)
        _iKey4_allKeys.extend(theseKeys)
        if len(_iKey4_allKeys):
            iKey4.keys = _iKey4_allKeys[-1].name  # just the last key pressed
            iKey4.rt = _iKey4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in isntructions4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "isntructions4" ---
for thisComponent in isntructions4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "isntructions4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions5" ---
continueRoutine = True
# update component parameters for each repeat
iKey6.keys = []
iKey6.rt = []
_iKey6_allKeys = []
# keep track of which components have finished
instructions5Components = [iText7, iImage5, iImage6, iText8, iKey6]
for thisComponent in instructions5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions5" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *iText7* updates
    
    # if iText7 is starting this frame...
    if iText7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iText7.frameNStart = frameN  # exact frame index
        iText7.tStart = t  # local t and not account for scr refresh
        iText7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iText7, 'tStartRefresh')  # time at next scr refresh
        # update status
        iText7.status = STARTED
        iText7.setAutoDraw(True)
    
    # if iText7 is active this frame...
    if iText7.status == STARTED:
        # update params
        pass
    
    # *iImage5* updates
    
    # if iImage5 is starting this frame...
    if iImage5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iImage5.frameNStart = frameN  # exact frame index
        iImage5.tStart = t  # local t and not account for scr refresh
        iImage5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iImage5, 'tStartRefresh')  # time at next scr refresh
        # update status
        iImage5.status = STARTED
        iImage5.setAutoDraw(True)
    
    # if iImage5 is active this frame...
    if iImage5.status == STARTED:
        # update params
        pass
    
    # *iImage6* updates
    
    # if iImage6 is starting this frame...
    if iImage6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iImage6.frameNStart = frameN  # exact frame index
        iImage6.tStart = t  # local t and not account for scr refresh
        iImage6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iImage6, 'tStartRefresh')  # time at next scr refresh
        # update status
        iImage6.status = STARTED
        iImage6.setAutoDraw(True)
    
    # if iImage6 is active this frame...
    if iImage6.status == STARTED:
        # update params
        pass
    
    # *iText8* updates
    
    # if iText8 is starting this frame...
    if iText8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iText8.frameNStart = frameN  # exact frame index
        iText8.tStart = t  # local t and not account for scr refresh
        iText8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iText8, 'tStartRefresh')  # time at next scr refresh
        # update status
        iText8.status = STARTED
        iText8.setAutoDraw(True)
    
    # if iText8 is active this frame...
    if iText8.status == STARTED:
        # update params
        pass
    
    # *iKey6* updates
    
    # if iKey6 is starting this frame...
    if iKey6.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iKey6.frameNStart = frameN  # exact frame index
        iKey6.tStart = t  # local t and not account for scr refresh
        iKey6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iKey6, 'tStartRefresh')  # time at next scr refresh
        # update status
        iKey6.status = STARTED
        # keyboard checking is just starting
        iKey6.clock.reset()  # now t=0
    if iKey6.status == STARTED:
        theseKeys = iKey6.getKeys(keyList=['space'], waitRelease=False)
        _iKey6_allKeys.extend(theseKeys)
        if len(_iKey6_allKeys):
            iKey6.keys = _iKey6_allKeys[-1].name  # just the last key pressed
            iKey6.rt = _iKey6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions5" ---
for thisComponent in instructions5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction7" ---
continueRoutine = True
# update component parameters for each repeat
iKey7.keys = []
iKey7.rt = []
_iKey7_allKeys = []
# keep track of which components have finished
instruction7Components = [iText7_2, iImage5_2, iImage6_2, iText8_2, iKey7]
for thisComponent in instruction7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction7" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *iText7_2* updates
    
    # if iText7_2 is starting this frame...
    if iText7_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iText7_2.frameNStart = frameN  # exact frame index
        iText7_2.tStart = t  # local t and not account for scr refresh
        iText7_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iText7_2, 'tStartRefresh')  # time at next scr refresh
        # update status
        iText7_2.status = STARTED
        iText7_2.setAutoDraw(True)
    
    # if iText7_2 is active this frame...
    if iText7_2.status == STARTED:
        # update params
        pass
    
    # *iImage5_2* updates
    
    # if iImage5_2 is starting this frame...
    if iImage5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iImage5_2.frameNStart = frameN  # exact frame index
        iImage5_2.tStart = t  # local t and not account for scr refresh
        iImage5_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iImage5_2, 'tStartRefresh')  # time at next scr refresh
        # update status
        iImage5_2.status = STARTED
        iImage5_2.setAutoDraw(True)
    
    # if iImage5_2 is active this frame...
    if iImage5_2.status == STARTED:
        # update params
        pass
    
    # *iImage6_2* updates
    
    # if iImage6_2 is starting this frame...
    if iImage6_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iImage6_2.frameNStart = frameN  # exact frame index
        iImage6_2.tStart = t  # local t and not account for scr refresh
        iImage6_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iImage6_2, 'tStartRefresh')  # time at next scr refresh
        # update status
        iImage6_2.status = STARTED
        iImage6_2.setAutoDraw(True)
    
    # if iImage6_2 is active this frame...
    if iImage6_2.status == STARTED:
        # update params
        pass
    
    # *iText8_2* updates
    
    # if iText8_2 is starting this frame...
    if iText8_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iText8_2.frameNStart = frameN  # exact frame index
        iText8_2.tStart = t  # local t and not account for scr refresh
        iText8_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iText8_2, 'tStartRefresh')  # time at next scr refresh
        # update status
        iText8_2.status = STARTED
        iText8_2.setAutoDraw(True)
    
    # if iText8_2 is active this frame...
    if iText8_2.status == STARTED:
        # update params
        pass
    
    # *iKey7* updates
    
    # if iKey7 is starting this frame...
    if iKey7.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iKey7.frameNStart = frameN  # exact frame index
        iKey7.tStart = t  # local t and not account for scr refresh
        iKey7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iKey7, 'tStartRefresh')  # time at next scr refresh
        # update status
        iKey7.status = STARTED
        # keyboard checking is just starting
        iKey7.clock.reset()  # now t=0
    if iKey7.status == STARTED:
        theseKeys = iKey7.getKeys(keyList=['space'], waitRelease=False)
        _iKey7_allKeys.extend(theseKeys)
        if len(_iKey7_allKeys):
            iKey7.keys = _iKey7_allKeys[-1].name  # just the last key pressed
            iKey7.rt = _iKey7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction7" ---
for thisComponent in instruction7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instruction8" ---
continueRoutine = True
# update component parameters for each repeat
iKey1_2.keys = []
iKey1_2.rt = []
_iKey1_2_allKeys = []
# keep track of which components have finished
instruction8Components = [iText1_2, iKey1_2]
for thisComponent in instruction8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction8" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *iText1_2* updates
    
    # if iText1_2 is starting this frame...
    if iText1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iText1_2.frameNStart = frameN  # exact frame index
        iText1_2.tStart = t  # local t and not account for scr refresh
        iText1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iText1_2, 'tStartRefresh')  # time at next scr refresh
        # update status
        iText1_2.status = STARTED
        iText1_2.setAutoDraw(True)
    
    # if iText1_2 is active this frame...
    if iText1_2.status == STARTED:
        # update params
        pass
    
    # *iKey1_2* updates
    
    # if iKey1_2 is starting this frame...
    if iKey1_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iKey1_2.frameNStart = frameN  # exact frame index
        iKey1_2.tStart = t  # local t and not account for scr refresh
        iKey1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iKey1_2, 'tStartRefresh')  # time at next scr refresh
        # update status
        iKey1_2.status = STARTED
        # keyboard checking is just starting
        iKey1_2.clock.reset()  # now t=0
    if iKey1_2.status == STARTED:
        theseKeys = iKey1_2.getKeys(keyList=['space'], waitRelease=False)
        _iKey1_2_allKeys.extend(theseKeys)
        if len(_iKey1_2_allKeys):
            iKey1_2.keys = _iKey1_2_allKeys[-1].name  # just the last key pressed
            iKey1_2.rt = _iKey1_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction8" ---
for thisComponent in instruction8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ortho1 = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='ortho1')
thisExp.addLoop(ortho1)  # add the loop to the experiment
thisOrtho1 = ortho1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOrtho1.rgb)
if thisOrtho1 != None:
    for paramName in thisOrtho1:
        exec('{} = thisOrtho1[paramName]'.format(paramName))

for thisOrtho1 in ortho1:
    currentLoop = ortho1
    # abbreviate parameter names if possible (e.g. rgb = thisOrtho1.rgb)
    if thisOrtho1 != None:
        for paramName in thisOrtho1:
            exec('{} = thisOrtho1[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    exp1Loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("orthostim_" + expInfo['group'] + ".xlsx", selection='0:4'),
        seed=None, name='exp1Loop')
    thisExp.addLoop(exp1Loop)  # add the loop to the experiment
    thisExp1Loop = exp1Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExp1Loop.rgb)
    if thisExp1Loop != None:
        for paramName in thisExp1Loop:
            exec('{} = thisExp1Loop[paramName]'.format(paramName))
    
    for thisExp1Loop in exp1Loop:
        currentLoop = exp1Loop
        # abbreviate parameter names if possible (e.g. rgb = thisExp1Loop.rgb)
        if thisExp1Loop != None:
            for paramName in thisExp1Loop:
                exec('{} = thisExp1Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "exp1_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from e1Code1
        #learnStart = timer()
        e1PL.setText(plWord)
        # keep track of which components have finished
        exp1_1Components = [e1Focal1, e1PL]
        for thisComponent in exp1_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp1_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e1Focal1* updates
            
            # if e1Focal1 is starting this frame...
            if e1Focal1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                e1Focal1.frameNStart = frameN  # exact frame index
                e1Focal1.tStart = t  # local t and not account for scr refresh
                e1Focal1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e1Focal1, 'tStartRefresh')  # time at next scr refresh
                # update status
                e1Focal1.status = STARTED
                e1Focal1.setAutoDraw(True)
            
            # if e1Focal1 is active this frame...
            if e1Focal1.status == STARTED:
                # update params
                pass
            
            # if e1Focal1 is stopping this frame...
            if e1Focal1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e1Focal1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    e1Focal1.tStop = t  # not accounting for scr refresh
                    e1Focal1.frameNStop = frameN  # exact frame index
                    # update status
                    e1Focal1.status = FINISHED
                    e1Focal1.setAutoDraw(False)
            
            # *e1PL* updates
            
            # if e1PL is starting this frame...
            if e1PL.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
                # keep track of start time/frame for later
                e1PL.frameNStart = frameN  # exact frame index
                e1PL.tStart = t  # local t and not account for scr refresh
                e1PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e1PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                e1PL.status = STARTED
                e1PL.setAutoDraw(True)
            
            # if e1PL is active this frame...
            if e1PL.status == STARTED:
                # update params
                pass
            
            # if e1PL is stopping this frame...
            if e1PL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e1PL.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    e1PL.tStop = t  # not accounting for scr refresh
                    e1PL.frameNStop = frameN  # exact frame index
                    # update status
                    e1PL.status = FINISHED
                    e1PL.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp1_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp1_1" ---
        for thisComponent in exp1_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.100000)
        
        # --- Prepare to start Routine "exp1_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from e1Code2
        e1Count = e1Count+1
        e1CON.setText(conWord)
        e1Sound.setSound(audio, hamming=True)
        e1Sound.setVolume(3.0, log=False)
        e1Key.keys = []
        e1Key.rt = []
        _e1Key_allKeys = []
        # keep track of which components have finished
        exp1_2Components = [e1Focal2, e1CON, e1Sound, e1Key, space0]
        for thisComponent in exp1_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp1_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e1Focal2* updates
            
            # if e1Focal2 is starting this frame...
            if e1Focal2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                e1Focal2.frameNStart = frameN  # exact frame index
                e1Focal2.tStart = t  # local t and not account for scr refresh
                e1Focal2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e1Focal2, 'tStartRefresh')  # time at next scr refresh
                # update status
                e1Focal2.status = STARTED
                e1Focal2.setAutoDraw(True)
            
            # if e1Focal2 is active this frame...
            if e1Focal2.status == STARTED:
                # update params
                pass
            
            # if e1Focal2 is stopping this frame...
            if e1Focal2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e1Focal2.tStartRefresh + 1.1-frameTolerance:
                    # keep track of stop time/frame for later
                    e1Focal2.tStop = t  # not accounting for scr refresh
                    e1Focal2.frameNStop = frameN  # exact frame index
                    # update status
                    e1Focal2.status = FINISHED
                    e1Focal2.setAutoDraw(False)
            
            # *e1CON* updates
            
            # if e1CON is starting this frame...
            if e1CON.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e1CON.frameNStart = frameN  # exact frame index
                e1CON.tStart = t  # local t and not account for scr refresh
                e1CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e1CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                e1CON.status = STARTED
                e1CON.setAutoDraw(True)
            
            # if e1CON is active this frame...
            if e1CON.status == STARTED:
                # update params
                pass
            # start/stop e1Sound
            
            # if e1Sound is starting this frame...
            if e1Sound.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e1Sound.frameNStart = frameN  # exact frame index
                e1Sound.tStart = t  # local t and not account for scr refresh
                e1Sound.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                e1Sound.status = STARTED
                e1Sound.play(when=win)  # sync with win flip
            
            # *e1Key* updates
            
            # if e1Key is starting this frame...
            if e1Key.status == NOT_STARTED and t >= 2.1-frameTolerance:
                # keep track of start time/frame for later
                e1Key.frameNStart = frameN  # exact frame index
                e1Key.tStart = t  # local t and not account for scr refresh
                e1Key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e1Key, 'tStartRefresh')  # time at next scr refresh
                # update status
                e1Key.status = STARTED
                # keyboard checking is just starting
                e1Key.clock.reset()  # now t=0
            if e1Key.status == STARTED:
                theseKeys = e1Key.getKeys(keyList=['space'], waitRelease=False)
                _e1Key_allKeys.extend(theseKeys)
                if len(_e1Key_allKeys):
                    e1Key.keys = _e1Key_allKeys[-1].name  # just the last key pressed
                    e1Key.rt = _e1Key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *space0* updates
            
            # if space0 is starting this frame...
            if space0.status == NOT_STARTED and tThisFlip >= 3.1-frameTolerance:
                # keep track of start time/frame for later
                space0.frameNStart = frameN  # exact frame index
                space0.tStart = t  # local t and not account for scr refresh
                space0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space0, 'tStartRefresh')  # time at next scr refresh
                # update status
                space0.status = STARTED
                space0.setAutoDraw(True)
            
            # if space0 is active this frame...
            if space0.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp1_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp1_2" ---
        for thisComponent in exp1_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from e1Code2
        if e1Count == 4:
            exp1Loop.finished = True
        else:
            pass
        e1Sound.stop()  # ensure sound has stopped at end of routine
        # the Routine "exp1_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'exp1Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    mini1Loop = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("orthostim_" + expInfo['group'] + ".xlsx", selection='0:4'),
        seed=None, name='mini1Loop')
    thisExp.addLoop(mini1Loop)  # add the loop to the experiment
    thisMini1Loop = mini1Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMini1Loop.rgb)
    if thisMini1Loop != None:
        for paramName in thisMini1Loop:
            exec('{} = thisMini1Loop[paramName]'.format(paramName))
    
    for thisMini1Loop in mini1Loop:
        currentLoop = mini1Loop
        # abbreviate parameter names if possible (e.g. rgb = thisMini1Loop.rgb)
        if thisMini1Loop != None:
            for paramName in thisMini1Loop:
                exec('{} = thisMini1Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mini1_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from m1Code1
        random.shuffle(m1Posi)
        m1PL1.setText(plWord)
        m1CON1.setPos([m1Posi[0]])
        m1CON1.setText(conWord)
        # reset m1CON1 to account for continued clicks & clear times on/off
        m1CON1.reset()
        m1DIST1.setPos([m1Posi[1]])
        m1DIST1.setText(incorr1)
        # reset m1DIST1 to account for continued clicks & clear times on/off
        m1DIST1.reset()
        m1DIST2.setPos([m1Posi[2]])
        m1DIST2.setText(incorr2)
        # reset m1DIST2 to account for continued clicks & clear times on/off
        m1DIST2.reset()
        m1DIST3.setPos([m1Posi[3]])
        m1DIST3.setText(incorr3)
        # reset m1DIST3 to account for continued clicks & clear times on/off
        m1DIST3.reset()
        # setup some python lists for storing info about the m1Mouse
        m1Mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        mini1_1Components = [m1PL1, m1CON1, m1DIST1, m1DIST2, m1DIST3, m1Mouse]
        for thisComponent in mini1_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mini1_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *m1PL1* updates
            
            # if m1PL1 is starting this frame...
            if m1PL1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m1PL1.frameNStart = frameN  # exact frame index
                m1PL1.tStart = t  # local t and not account for scr refresh
                m1PL1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m1PL1, 'tStartRefresh')  # time at next scr refresh
                # update status
                m1PL1.status = STARTED
                m1PL1.setAutoDraw(True)
            
            # if m1PL1 is active this frame...
            if m1PL1.status == STARTED:
                # update params
                pass
            # *m1CON1* updates
            
            # if m1CON1 is starting this frame...
            if m1CON1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m1CON1.frameNStart = frameN  # exact frame index
                m1CON1.tStart = t  # local t and not account for scr refresh
                m1CON1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m1CON1, 'tStartRefresh')  # time at next scr refresh
                # update status
                m1CON1.status = STARTED
                m1CON1.setAutoDraw(True)
            
            # if m1CON1 is active this frame...
            if m1CON1.status == STARTED:
                # update params
                pass
                # check whether m1CON1 has been pressed
                if m1CON1.isClicked:
                    if not m1CON1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m1CON1.timesOn.append(m1CON1.buttonClock.getTime())
                        m1CON1.timesOff.append(m1CON1.buttonClock.getTime())
                    elif len(m1CON1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m1CON1.timesOff[-1] = m1CON1.buttonClock.getTime()
                    if not m1CON1.wasClicked:
                        # end routine when m1CON1 is clicked
                        continueRoutine = False
                    if not m1CON1.wasClicked:
                        # run callback code when m1CON1 is clicked
                        pass
            # take note of whether m1CON1 was clicked, so that next frame we know if clicks are new
            m1CON1.wasClicked = m1CON1.isClicked and m1CON1.status == STARTED
            # *m1DIST1* updates
            
            # if m1DIST1 is starting this frame...
            if m1DIST1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m1DIST1.frameNStart = frameN  # exact frame index
                m1DIST1.tStart = t  # local t and not account for scr refresh
                m1DIST1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m1DIST1, 'tStartRefresh')  # time at next scr refresh
                # update status
                m1DIST1.status = STARTED
                m1DIST1.setAutoDraw(True)
            
            # if m1DIST1 is active this frame...
            if m1DIST1.status == STARTED:
                # update params
                pass
                # check whether m1DIST1 has been pressed
                if m1DIST1.isClicked:
                    if not m1DIST1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m1DIST1.timesOn.append(m1DIST1.buttonClock.getTime())
                        m1DIST1.timesOff.append(m1DIST1.buttonClock.getTime())
                    elif len(m1DIST1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m1DIST1.timesOff[-1] = m1DIST1.buttonClock.getTime()
                    if not m1DIST1.wasClicked:
                        # end routine when m1DIST1 is clicked
                        continueRoutine = False
                    if not m1DIST1.wasClicked:
                        # run callback code when m1DIST1 is clicked
                        pass
            # take note of whether m1DIST1 was clicked, so that next frame we know if clicks are new
            m1DIST1.wasClicked = m1DIST1.isClicked and m1DIST1.status == STARTED
            # *m1DIST2* updates
            
            # if m1DIST2 is starting this frame...
            if m1DIST2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m1DIST2.frameNStart = frameN  # exact frame index
                m1DIST2.tStart = t  # local t and not account for scr refresh
                m1DIST2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m1DIST2, 'tStartRefresh')  # time at next scr refresh
                # update status
                m1DIST2.status = STARTED
                m1DIST2.setAutoDraw(True)
            
            # if m1DIST2 is active this frame...
            if m1DIST2.status == STARTED:
                # update params
                pass
                # check whether m1DIST2 has been pressed
                if m1DIST2.isClicked:
                    if not m1DIST2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m1DIST2.timesOn.append(m1DIST2.buttonClock.getTime())
                        m1DIST2.timesOff.append(m1DIST2.buttonClock.getTime())
                    elif len(m1DIST2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m1DIST2.timesOff[-1] = m1DIST2.buttonClock.getTime()
                    if not m1DIST2.wasClicked:
                        # end routine when m1DIST2 is clicked
                        continueRoutine = False
                    if not m1DIST2.wasClicked:
                        # run callback code when m1DIST2 is clicked
                        pass
            # take note of whether m1DIST2 was clicked, so that next frame we know if clicks are new
            m1DIST2.wasClicked = m1DIST2.isClicked and m1DIST2.status == STARTED
            # *m1DIST3* updates
            
            # if m1DIST3 is starting this frame...
            if m1DIST3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m1DIST3.frameNStart = frameN  # exact frame index
                m1DIST3.tStart = t  # local t and not account for scr refresh
                m1DIST3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m1DIST3, 'tStartRefresh')  # time at next scr refresh
                # update status
                m1DIST3.status = STARTED
                m1DIST3.setAutoDraw(True)
            
            # if m1DIST3 is active this frame...
            if m1DIST3.status == STARTED:
                # update params
                pass
                # check whether m1DIST3 has been pressed
                if m1DIST3.isClicked:
                    if not m1DIST3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m1DIST3.timesOn.append(m1DIST3.buttonClock.getTime())
                        m1DIST3.timesOff.append(m1DIST3.buttonClock.getTime())
                    elif len(m1DIST3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m1DIST3.timesOff[-1] = m1DIST3.buttonClock.getTime()
                    if not m1DIST3.wasClicked:
                        # end routine when m1DIST3 is clicked
                        continueRoutine = False
                    if not m1DIST3.wasClicked:
                        # run callback code when m1DIST3 is clicked
                        pass
            # take note of whether m1DIST3 was clicked, so that next frame we know if clicks are new
            m1DIST3.wasClicked = m1DIST3.isClicked and m1DIST3.status == STARTED
            # *m1Mouse* updates
            
            # if m1Mouse is starting this frame...
            if m1Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m1Mouse.frameNStart = frameN  # exact frame index
                m1Mouse.tStart = t  # local t and not account for scr refresh
                m1Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m1Mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'm1Mouse.started')
                # update status
                m1Mouse.status = STARTED
                m1Mouse.mouseClock.reset()
                prevButtonState = m1Mouse.getPressed()  # if button is down already this ISN'T a new click
            if m1Mouse.status == STARTED:  # only update if started and not finished!
                buttons = m1Mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = core.getFromNames([m1CON1,m1DIST1,m1DIST2,m1DIST3])
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(m1Mouse):
                                gotValidClick = True
                                m1Mouse.clicked_name.append(obj.name)
                        continueRoutine = False  # end routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mini1_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mini1_1" ---
        for thisComponent in mini1_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from m1Code1
        if m1Mouse.isPressedIn(m1CON1):
            nRepsM1Corr = True
            nRepsM1Incorr = False
            thisExp.addData("mCorr Response",m1CON1.text)
        else:
            nRepsM1Corr = False
            nRepsM1Incorr = True
        
        if m1Mouse.isPressedIn(m1DIST1):
            incorrAns1=m1DIST1.text
            incorrPosi1=m1DIST1.pos
            thisExp.addData("mIncorr Repsonse",m1DIST1.text)
        elif m1Mouse.isPressedIn(m1DIST2):
            incorrAns1=m1DIST2.text
            incorrPosi1=m1DIST2.pos
            thisExp.addData("mIncorr Repsonse",m1DIST2.text)
        elif m1Mouse.isPressedIn(m1DIST3):
            incorrAns1=m1DIST3.text
            incorrPosi1=m1DIST3.pos
            thisExp.addData("mIncorr Repsonse",m1DIST3.text)
        # store data for mini1Loop (TrialHandler)
        # the Routine "mini1_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        m1CorrLoop = data.TrialHandler(nReps=nRepsM1Corr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m1CorrLoop')
        thisExp.addLoop(m1CorrLoop)  # add the loop to the experiment
        thisM1CorrLoop = m1CorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM1CorrLoop.rgb)
        if thisM1CorrLoop != None:
            for paramName in thisM1CorrLoop:
                exec('{} = thisM1CorrLoop[paramName]'.format(paramName))
        
        for thisM1CorrLoop in m1CorrLoop:
            currentLoop = m1CorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM1CorrLoop.rgb)
            if thisM1CorrLoop != None:
                for paramName in thisM1CorrLoop:
                    exec('{} = thisM1CorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini1_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m1Code2
            m1Count = m1Count+1
            m1CorrPL.setText(plWord)
            m1CorrCON.setPos([m1Posi[0]])
            m1CorrCON.setText(conWord)
            m1Sound1.setSound(audio, secs=2, hamming=True)
            m1Sound1.setVolume(3.0, log=False)
            m1Key1.keys = []
            m1Key1.rt = []
            _m1Key1_allKeys = []
            # keep track of which components have finished
            mini1_2Components = [m1CorrPL, m1CorrCON, m1Sound1, space1, m1Key1]
            for thisComponent in mini1_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini1_2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m1CorrPL* updates
                
                # if m1CorrPL is starting this frame...
                if m1CorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m1CorrPL.frameNStart = frameN  # exact frame index
                    m1CorrPL.tStart = t  # local t and not account for scr refresh
                    m1CorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m1CorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m1CorrPL.status = STARTED
                    m1CorrPL.setAutoDraw(True)
                
                # if m1CorrPL is active this frame...
                if m1CorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m1CorrCON* updates
                
                # if m1CorrCON is starting this frame...
                if m1CorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m1CorrCON.frameNStart = frameN  # exact frame index
                    m1CorrCON.tStart = t  # local t and not account for scr refresh
                    m1CorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m1CorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m1CorrCON.status = STARTED
                    m1CorrCON.setAutoDraw(True)
                
                # if m1CorrCON is active this frame...
                if m1CorrCON.status == STARTED:
                    # update params
                    pass
                # start/stop m1Sound1
                
                # if m1Sound1 is starting this frame...
                if m1Sound1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m1Sound1.frameNStart = frameN  # exact frame index
                    m1Sound1.tStart = t  # local t and not account for scr refresh
                    m1Sound1.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m1Sound1.status = STARTED
                    m1Sound1.play(when=win)  # sync with win flip
                
                # if m1Sound1 is stopping this frame...
                if m1Sound1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m1Sound1.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m1Sound1.tStop = t  # not accounting for scr refresh
                        m1Sound1.frameNStop = frameN  # exact frame index
                        # update status
                        m1Sound1.status = FINISHED
                        m1Sound1.stop()
                
                # *space1* updates
                
                # if space1 is starting this frame...
                if space1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space1.frameNStart = frameN  # exact frame index
                    space1.tStart = t  # local t and not account for scr refresh
                    space1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space1.status = STARTED
                    space1.setAutoDraw(True)
                
                # if space1 is active this frame...
                if space1.status == STARTED:
                    # update params
                    pass
                
                # *m1Key1* updates
                
                # if m1Key1 is starting this frame...
                if m1Key1.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m1Key1.frameNStart = frameN  # exact frame index
                    m1Key1.tStart = t  # local t and not account for scr refresh
                    m1Key1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m1Key1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m1Key1.status = STARTED
                    # keyboard checking is just starting
                    m1Key1.clock.reset()  # now t=0
                if m1Key1.status == STARTED:
                    theseKeys = m1Key1.getKeys(keyList=['space'], waitRelease=False)
                    _m1Key1_allKeys.extend(theseKeys)
                    if len(_m1Key1_allKeys):
                        m1Key1.keys = _m1Key1_allKeys[-1].name  # just the last key pressed
                        m1Key1.rt = _m1Key1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini1_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini1_2" ---
            for thisComponent in mini1_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m1Code2
            if m1Count == 12:
                mini1Loop.finished = True
            m1Sound1.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini1_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM1Corr repeats of 'm1CorrLoop'
        
        
        # set up handler to look after randomisation of conditions etc
        m1IncorrLoop = data.TrialHandler(nReps=nRepsM1Incorr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m1IncorrLoop')
        thisExp.addLoop(m1IncorrLoop)  # add the loop to the experiment
        thisM1IncorrLoop = m1IncorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM1IncorrLoop.rgb)
        if thisM1IncorrLoop != None:
            for paramName in thisM1IncorrLoop:
                exec('{} = thisM1IncorrLoop[paramName]'.format(paramName))
        
        for thisM1IncorrLoop in m1IncorrLoop:
            currentLoop = m1IncorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM1IncorrLoop.rgb)
            if thisM1IncorrLoop != None:
                for paramName in thisM1IncorrLoop:
                    exec('{} = thisM1IncorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini1_3" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m1Code3
            m1Count = m1Count+1
            m1IncorrPL.setText(plWord)
            m1IncorrCON.setPos([m1Posi[0]])
            m1IncorrCON.setText(conWord)
            m1IncorrDIST.setPos(incorrPosi1)
            m1IncorrDIST.setText(incorrAns1)
            m1Sound2.setSound(audio, secs=2, hamming=True)
            m1Sound2.setVolume(3.0, log=False)
            m1Key2.keys = []
            m1Key2.rt = []
            _m1Key2_allKeys = []
            # keep track of which components have finished
            mini1_3Components = [m1IncorrPL, m1IncorrCON, m1IncorrDIST, m1Sound2, space2, m1Key2]
            for thisComponent in mini1_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini1_3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m1IncorrPL* updates
                
                # if m1IncorrPL is starting this frame...
                if m1IncorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m1IncorrPL.frameNStart = frameN  # exact frame index
                    m1IncorrPL.tStart = t  # local t and not account for scr refresh
                    m1IncorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m1IncorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m1IncorrPL.status = STARTED
                    m1IncorrPL.setAutoDraw(True)
                
                # if m1IncorrPL is active this frame...
                if m1IncorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m1IncorrCON* updates
                
                # if m1IncorrCON is starting this frame...
                if m1IncorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m1IncorrCON.frameNStart = frameN  # exact frame index
                    m1IncorrCON.tStart = t  # local t and not account for scr refresh
                    m1IncorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m1IncorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m1IncorrCON.status = STARTED
                    m1IncorrCON.setAutoDraw(True)
                
                # if m1IncorrCON is active this frame...
                if m1IncorrCON.status == STARTED:
                    # update params
                    pass
                
                # *m1IncorrDIST* updates
                
                # if m1IncorrDIST is starting this frame...
                if m1IncorrDIST.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m1IncorrDIST.frameNStart = frameN  # exact frame index
                    m1IncorrDIST.tStart = t  # local t and not account for scr refresh
                    m1IncorrDIST.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m1IncorrDIST, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m1IncorrDIST.status = STARTED
                    m1IncorrDIST.setAutoDraw(True)
                
                # if m1IncorrDIST is active this frame...
                if m1IncorrDIST.status == STARTED:
                    # update params
                    pass
                # start/stop m1Sound2
                
                # if m1Sound2 is starting this frame...
                if m1Sound2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m1Sound2.frameNStart = frameN  # exact frame index
                    m1Sound2.tStart = t  # local t and not account for scr refresh
                    m1Sound2.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m1Sound2.status = STARTED
                    m1Sound2.play(when=win)  # sync with win flip
                
                # if m1Sound2 is stopping this frame...
                if m1Sound2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m1Sound2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m1Sound2.tStop = t  # not accounting for scr refresh
                        m1Sound2.frameNStop = frameN  # exact frame index
                        # update status
                        m1Sound2.status = FINISHED
                        m1Sound2.stop()
                
                # *space2* updates
                
                # if space2 is starting this frame...
                if space2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space2.frameNStart = frameN  # exact frame index
                    space2.tStart = t  # local t and not account for scr refresh
                    space2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space2.status = STARTED
                    space2.setAutoDraw(True)
                
                # if space2 is active this frame...
                if space2.status == STARTED:
                    # update params
                    pass
                
                # *m1Key2* updates
                
                # if m1Key2 is starting this frame...
                if m1Key2.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m1Key2.frameNStart = frameN  # exact frame index
                    m1Key2.tStart = t  # local t and not account for scr refresh
                    m1Key2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m1Key2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m1Key2.status = STARTED
                    # keyboard checking is just starting
                    m1Key2.clock.reset()  # now t=0
                if m1Key2.status == STARTED:
                    theseKeys = m1Key2.getKeys(keyList=['space'], waitRelease=False)
                    _m1Key2_allKeys.extend(theseKeys)
                    if len(_m1Key2_allKeys):
                        m1Key2.keys = _m1Key2_allKeys[-1].name  # just the last key pressed
                        m1Key2.rt = _m1Key2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini1_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini1_3" ---
            for thisComponent in mini1_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m1Code3
            if m1Count==12:
                mini1Loop.finished = True
            m1Sound2.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini1_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM1Incorr repeats of 'm1IncorrLoop'
        
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'mini1Loop'
    
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'ortho1'


# set up handler to look after randomisation of conditions etc
img1 = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='img1')
thisExp.addLoop(img1)  # add the loop to the experiment
thisImg1 = img1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisImg1.rgb)
if thisImg1 != None:
    for paramName in thisImg1:
        exec('{} = thisImg1[paramName]'.format(paramName))

for thisImg1 in img1:
    currentLoop = img1
    # abbreviate parameter names if possible (e.g. rgb = thisImg1.rgb)
    if thisImg1 != None:
        for paramName in thisImg1:
            exec('{} = thisImg1[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    exp2Loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("imgstim_"+expInfo['group']+".xlsx", selection='0:4'),
        seed=None, name='exp2Loop')
    thisExp.addLoop(exp2Loop)  # add the loop to the experiment
    thisExp2Loop = exp2Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExp2Loop.rgb)
    if thisExp2Loop != None:
        for paramName in thisExp2Loop:
            exec('{} = thisExp2Loop[paramName]'.format(paramName))
    
    for thisExp2Loop in exp2Loop:
        currentLoop = exp2Loop
        # abbreviate parameter names if possible (e.g. rgb = thisExp2Loop.rgb)
        if thisExp2Loop != None:
            for paramName in thisExp2Loop:
                exec('{} = thisExp2Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "exp2_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        e2PL.setImage(img)
        # keep track of which components have finished
        exp2_1Components = [e2Focal1, e2PL]
        for thisComponent in exp2_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp2_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e2Focal1* updates
            
            # if e2Focal1 is starting this frame...
            if e2Focal1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                e2Focal1.frameNStart = frameN  # exact frame index
                e2Focal1.tStart = t  # local t and not account for scr refresh
                e2Focal1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e2Focal1, 'tStartRefresh')  # time at next scr refresh
                # update status
                e2Focal1.status = STARTED
                e2Focal1.setAutoDraw(True)
            
            # if e2Focal1 is active this frame...
            if e2Focal1.status == STARTED:
                # update params
                pass
            
            # if e2Focal1 is stopping this frame...
            if e2Focal1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e2Focal1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    e2Focal1.tStop = t  # not accounting for scr refresh
                    e2Focal1.frameNStop = frameN  # exact frame index
                    # update status
                    e2Focal1.status = FINISHED
                    e2Focal1.setAutoDraw(False)
            
            # *e2PL* updates
            
            # if e2PL is starting this frame...
            if e2PL.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
                # keep track of start time/frame for later
                e2PL.frameNStart = frameN  # exact frame index
                e2PL.tStart = t  # local t and not account for scr refresh
                e2PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e2PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                e2PL.status = STARTED
                e2PL.setAutoDraw(True)
            
            # if e2PL is active this frame...
            if e2PL.status == STARTED:
                # update params
                pass
            
            # if e2PL is stopping this frame...
            if e2PL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e2PL.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    e2PL.tStop = t  # not accounting for scr refresh
                    e2PL.frameNStop = frameN  # exact frame index
                    # update status
                    e2PL.status = FINISHED
                    e2PL.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp2_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp2_1" ---
        for thisComponent in exp2_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.100000)
        
        # --- Prepare to start Routine "exp2_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from e2Code2
        e2Count = e2Count+1
        e2CON.setText(conWord)
        e2Sound.setSound(audio, hamming=True)
        e2Sound.setVolume(3.0, log=False)
        e2Key.keys = []
        e2Key.rt = []
        _e2Key_allKeys = []
        # keep track of which components have finished
        exp2_2Components = [e2Focal2, e2CON, e2Sound, e2Key, space3]
        for thisComponent in exp2_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp2_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e2Focal2* updates
            
            # if e2Focal2 is starting this frame...
            if e2Focal2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                e2Focal2.frameNStart = frameN  # exact frame index
                e2Focal2.tStart = t  # local t and not account for scr refresh
                e2Focal2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e2Focal2, 'tStartRefresh')  # time at next scr refresh
                # update status
                e2Focal2.status = STARTED
                e2Focal2.setAutoDraw(True)
            
            # if e2Focal2 is active this frame...
            if e2Focal2.status == STARTED:
                # update params
                pass
            
            # if e2Focal2 is stopping this frame...
            if e2Focal2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e2Focal2.tStartRefresh + 1.1-frameTolerance:
                    # keep track of stop time/frame for later
                    e2Focal2.tStop = t  # not accounting for scr refresh
                    e2Focal2.frameNStop = frameN  # exact frame index
                    # update status
                    e2Focal2.status = FINISHED
                    e2Focal2.setAutoDraw(False)
            
            # *e2CON* updates
            
            # if e2CON is starting this frame...
            if e2CON.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e2CON.frameNStart = frameN  # exact frame index
                e2CON.tStart = t  # local t and not account for scr refresh
                e2CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e2CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                e2CON.status = STARTED
                e2CON.setAutoDraw(True)
            
            # if e2CON is active this frame...
            if e2CON.status == STARTED:
                # update params
                pass
            # start/stop e2Sound
            
            # if e2Sound is starting this frame...
            if e2Sound.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e2Sound.frameNStart = frameN  # exact frame index
                e2Sound.tStart = t  # local t and not account for scr refresh
                e2Sound.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                e2Sound.status = STARTED
                e2Sound.play(when=win)  # sync with win flip
            
            # *e2Key* updates
            
            # if e2Key is starting this frame...
            if e2Key.status == NOT_STARTED and t >= 2.1-frameTolerance:
                # keep track of start time/frame for later
                e2Key.frameNStart = frameN  # exact frame index
                e2Key.tStart = t  # local t and not account for scr refresh
                e2Key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e2Key, 'tStartRefresh')  # time at next scr refresh
                # update status
                e2Key.status = STARTED
                # keyboard checking is just starting
                e2Key.clock.reset()  # now t=0
            if e2Key.status == STARTED:
                theseKeys = e2Key.getKeys(keyList=['space'], waitRelease=False)
                _e2Key_allKeys.extend(theseKeys)
                if len(_e2Key_allKeys):
                    e2Key.keys = _e2Key_allKeys[-1].name  # just the last key pressed
                    e2Key.rt = _e2Key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *space3* updates
            
            # if space3 is starting this frame...
            if space3.status == NOT_STARTED and tThisFlip >= 3.1-frameTolerance:
                # keep track of start time/frame for later
                space3.frameNStart = frameN  # exact frame index
                space3.tStart = t  # local t and not account for scr refresh
                space3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space3, 'tStartRefresh')  # time at next scr refresh
                # update status
                space3.status = STARTED
                space3.setAutoDraw(True)
            
            # if space3 is active this frame...
            if space3.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp2_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp2_2" ---
        for thisComponent in exp2_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from e2Code2
        if e2Count ==4:
            exp2Loop.finished = True
        else:
            pass
        e2Sound.stop()  # ensure sound has stopped at end of routine
        # the Routine "exp2_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'exp2Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    mini2Loop = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("imgstim_"+expInfo['group']+".xlsx", selection='0:4'),
        seed=None, name='mini2Loop')
    thisExp.addLoop(mini2Loop)  # add the loop to the experiment
    thisMini2Loop = mini2Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMini2Loop.rgb)
    if thisMini2Loop != None:
        for paramName in thisMini2Loop:
            exec('{} = thisMini2Loop[paramName]'.format(paramName))
    
    for thisMini2Loop in mini2Loop:
        currentLoop = mini2Loop
        # abbreviate parameter names if possible (e.g. rgb = thisMini2Loop.rgb)
        if thisMini2Loop != None:
            for paramName in thisMini2Loop:
                exec('{} = thisMini2Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mini2_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from m2Code1
        random.shuffle(m2Posi)
        m2PL1.setImage(img)
        m2CON.setPos([m2Posi[0]])
        m2CON.setText(conWord)
        # reset m2CON to account for continued clicks & clear times on/off
        m2CON.reset()
        m2DIST1.setPos([m2Posi[1]])
        m2DIST1.setText(incorr1)
        # reset m2DIST1 to account for continued clicks & clear times on/off
        m2DIST1.reset()
        m2DIST2.setPos([m2Posi[2]])
        m2DIST2.setText(incorr2)
        # reset m2DIST2 to account for continued clicks & clear times on/off
        m2DIST2.reset()
        m2DIST3.setPos([m2Posi[3]])
        m2DIST3.setText(incorr3)
        # reset m2DIST3 to account for continued clicks & clear times on/off
        m2DIST3.reset()
        # setup some python lists for storing info about the m2Mouse
        m2Mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        mini2_1Components = [m2PL1, m2CON, m2DIST1, m2DIST2, m2DIST3, m2Mouse]
        for thisComponent in mini2_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mini2_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *m2PL1* updates
            
            # if m2PL1 is starting this frame...
            if m2PL1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m2PL1.frameNStart = frameN  # exact frame index
                m2PL1.tStart = t  # local t and not account for scr refresh
                m2PL1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m2PL1, 'tStartRefresh')  # time at next scr refresh
                # update status
                m2PL1.status = STARTED
                m2PL1.setAutoDraw(True)
            
            # if m2PL1 is active this frame...
            if m2PL1.status == STARTED:
                # update params
                pass
            # *m2CON* updates
            
            # if m2CON is starting this frame...
            if m2CON.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m2CON.frameNStart = frameN  # exact frame index
                m2CON.tStart = t  # local t and not account for scr refresh
                m2CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m2CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                m2CON.status = STARTED
                m2CON.setAutoDraw(True)
            
            # if m2CON is active this frame...
            if m2CON.status == STARTED:
                # update params
                pass
                # check whether m2CON has been pressed
                if m2CON.isClicked:
                    if not m2CON.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m2CON.timesOn.append(m2CON.buttonClock.getTime())
                        m2CON.timesOff.append(m2CON.buttonClock.getTime())
                    elif len(m2CON.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m2CON.timesOff[-1] = m2CON.buttonClock.getTime()
                    if not m2CON.wasClicked:
                        # end routine when m2CON is clicked
                        continueRoutine = False
                    if not m2CON.wasClicked:
                        # run callback code when m2CON is clicked
                        pass
            # take note of whether m2CON was clicked, so that next frame we know if clicks are new
            m2CON.wasClicked = m2CON.isClicked and m2CON.status == STARTED
            # *m2DIST1* updates
            
            # if m2DIST1 is starting this frame...
            if m2DIST1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m2DIST1.frameNStart = frameN  # exact frame index
                m2DIST1.tStart = t  # local t and not account for scr refresh
                m2DIST1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m2DIST1, 'tStartRefresh')  # time at next scr refresh
                # update status
                m2DIST1.status = STARTED
                m2DIST1.setAutoDraw(True)
            
            # if m2DIST1 is active this frame...
            if m2DIST1.status == STARTED:
                # update params
                pass
                # check whether m2DIST1 has been pressed
                if m2DIST1.isClicked:
                    if not m2DIST1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m2DIST1.timesOn.append(m2DIST1.buttonClock.getTime())
                        m2DIST1.timesOff.append(m2DIST1.buttonClock.getTime())
                    elif len(m2DIST1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m2DIST1.timesOff[-1] = m2DIST1.buttonClock.getTime()
                    if not m2DIST1.wasClicked:
                        # end routine when m2DIST1 is clicked
                        continueRoutine = False
                    if not m2DIST1.wasClicked:
                        # run callback code when m2DIST1 is clicked
                        pass
            # take note of whether m2DIST1 was clicked, so that next frame we know if clicks are new
            m2DIST1.wasClicked = m2DIST1.isClicked and m2DIST1.status == STARTED
            # *m2DIST2* updates
            
            # if m2DIST2 is starting this frame...
            if m2DIST2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m2DIST2.frameNStart = frameN  # exact frame index
                m2DIST2.tStart = t  # local t and not account for scr refresh
                m2DIST2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m2DIST2, 'tStartRefresh')  # time at next scr refresh
                # update status
                m2DIST2.status = STARTED
                m2DIST2.setAutoDraw(True)
            
            # if m2DIST2 is active this frame...
            if m2DIST2.status == STARTED:
                # update params
                pass
                # check whether m2DIST2 has been pressed
                if m2DIST2.isClicked:
                    if not m2DIST2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m2DIST2.timesOn.append(m2DIST2.buttonClock.getTime())
                        m2DIST2.timesOff.append(m2DIST2.buttonClock.getTime())
                    elif len(m2DIST2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m2DIST2.timesOff[-1] = m2DIST2.buttonClock.getTime()
                    if not m2DIST2.wasClicked:
                        # end routine when m2DIST2 is clicked
                        continueRoutine = False
                    if not m2DIST2.wasClicked:
                        # run callback code when m2DIST2 is clicked
                        pass
            # take note of whether m2DIST2 was clicked, so that next frame we know if clicks are new
            m2DIST2.wasClicked = m2DIST2.isClicked and m2DIST2.status == STARTED
            # *m2DIST3* updates
            
            # if m2DIST3 is starting this frame...
            if m2DIST3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m2DIST3.frameNStart = frameN  # exact frame index
                m2DIST3.tStart = t  # local t and not account for scr refresh
                m2DIST3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m2DIST3, 'tStartRefresh')  # time at next scr refresh
                # update status
                m2DIST3.status = STARTED
                m2DIST3.setAutoDraw(True)
            
            # if m2DIST3 is active this frame...
            if m2DIST3.status == STARTED:
                # update params
                pass
                # check whether m2DIST3 has been pressed
                if m2DIST3.isClicked:
                    if not m2DIST3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m2DIST3.timesOn.append(m2DIST3.buttonClock.getTime())
                        m2DIST3.timesOff.append(m2DIST3.buttonClock.getTime())
                    elif len(m2DIST3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m2DIST3.timesOff[-1] = m2DIST3.buttonClock.getTime()
                    if not m2DIST3.wasClicked:
                        # end routine when m2DIST3 is clicked
                        continueRoutine = False
                    if not m2DIST3.wasClicked:
                        # run callback code when m2DIST3 is clicked
                        pass
            # take note of whether m2DIST3 was clicked, so that next frame we know if clicks are new
            m2DIST3.wasClicked = m2DIST3.isClicked and m2DIST3.status == STARTED
            # *m2Mouse* updates
            
            # if m2Mouse is starting this frame...
            if m2Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m2Mouse.frameNStart = frameN  # exact frame index
                m2Mouse.tStart = t  # local t and not account for scr refresh
                m2Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m2Mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'm2Mouse.started')
                # update status
                m2Mouse.status = STARTED
                m2Mouse.mouseClock.reset()
                prevButtonState = m2Mouse.getPressed()  # if button is down already this ISN'T a new click
            if m2Mouse.status == STARTED:  # only update if started and not finished!
                buttons = m2Mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = core.getFromNames([m2CON,m2DIST1,m2DIST2,m2DIST3])
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(m2Mouse):
                                gotValidClick = True
                                m2Mouse.clicked_name.append(obj.name)
                        continueRoutine = False  # end routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mini2_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mini2_1" ---
        for thisComponent in mini2_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from m2Code1
        if m2Mouse.isPressedIn(m2CON):
            nRepsM2Corr = True
            nRepsM2Incorr = False
            thisExp.addData("mCorr Response",m2CON.text)
        else:
            nRepsM2Corr = False
            nRepsM2Incorr = True
        
        if m2Mouse.isPressedIn(m2DIST1):
            incorrAns2=m2DIST1.text
            incorrPosi2=m2DIST1.pos
            thisExp.addData("mIncorr Repsonse",m2DIST1.text)
        elif m2Mouse.isPressedIn(m2DIST2):
            incorrAns2=m2DIST2.text
            incorrPosi2=m2DIST2.pos
            thisExp.addData("mIncorr Repsonse",m2DIST2.text)
        elif m2Mouse.isPressedIn(m2DIST3):
            incorrAns2=m2DIST3.text
            incorrPosi2=m2DIST3.pos
            thisExp.addData("mIncorr Repsonse",m2DIST3.text)
        # store data for mini2Loop (TrialHandler)
        # the Routine "mini2_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        m2CorrLoop = data.TrialHandler(nReps=nRepsM2Corr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m2CorrLoop')
        thisExp.addLoop(m2CorrLoop)  # add the loop to the experiment
        thisM2CorrLoop = m2CorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM2CorrLoop.rgb)
        if thisM2CorrLoop != None:
            for paramName in thisM2CorrLoop:
                exec('{} = thisM2CorrLoop[paramName]'.format(paramName))
        
        for thisM2CorrLoop in m2CorrLoop:
            currentLoop = m2CorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM2CorrLoop.rgb)
            if thisM2CorrLoop != None:
                for paramName in thisM2CorrLoop:
                    exec('{} = thisM2CorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini2_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m2Code2
            m2Count = m1Count+1
            m2CorrPL.setImage(img)
            m2CorrCON.setPos([m2Posi[0]])
            m2CorrCON.setText(conWord)
            m2Sound1.setSound(audio, secs=2, hamming=True)
            m2Sound1.setVolume(3.0, log=False)
            m2key1.keys = []
            m2key1.rt = []
            _m2key1_allKeys = []
            # keep track of which components have finished
            mini2_2Components = [m2CorrPL, m2CorrCON, m2Sound1, m2key1, space4]
            for thisComponent in mini2_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini2_2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m2CorrPL* updates
                
                # if m2CorrPL is starting this frame...
                if m2CorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m2CorrPL.frameNStart = frameN  # exact frame index
                    m2CorrPL.tStart = t  # local t and not account for scr refresh
                    m2CorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m2CorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m2CorrPL.status = STARTED
                    m2CorrPL.setAutoDraw(True)
                
                # if m2CorrPL is active this frame...
                if m2CorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m2CorrCON* updates
                
                # if m2CorrCON is starting this frame...
                if m2CorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m2CorrCON.frameNStart = frameN  # exact frame index
                    m2CorrCON.tStart = t  # local t and not account for scr refresh
                    m2CorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m2CorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m2CorrCON.status = STARTED
                    m2CorrCON.setAutoDraw(True)
                
                # if m2CorrCON is active this frame...
                if m2CorrCON.status == STARTED:
                    # update params
                    pass
                # start/stop m2Sound1
                
                # if m2Sound1 is starting this frame...
                if m2Sound1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m2Sound1.frameNStart = frameN  # exact frame index
                    m2Sound1.tStart = t  # local t and not account for scr refresh
                    m2Sound1.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m2Sound1.status = STARTED
                    m2Sound1.play(when=win)  # sync with win flip
                
                # if m2Sound1 is stopping this frame...
                if m2Sound1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m2Sound1.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m2Sound1.tStop = t  # not accounting for scr refresh
                        m2Sound1.frameNStop = frameN  # exact frame index
                        # update status
                        m2Sound1.status = FINISHED
                        m2Sound1.stop()
                
                # *m2key1* updates
                
                # if m2key1 is starting this frame...
                if m2key1.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m2key1.frameNStart = frameN  # exact frame index
                    m2key1.tStart = t  # local t and not account for scr refresh
                    m2key1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m2key1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m2key1.status = STARTED
                    # keyboard checking is just starting
                    m2key1.clock.reset()  # now t=0
                if m2key1.status == STARTED:
                    theseKeys = m2key1.getKeys(keyList=['space'], waitRelease=False)
                    _m2key1_allKeys.extend(theseKeys)
                    if len(_m2key1_allKeys):
                        m2key1.keys = _m2key1_allKeys[-1].name  # just the last key pressed
                        m2key1.rt = _m2key1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space4* updates
                
                # if space4 is starting this frame...
                if space4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space4.frameNStart = frameN  # exact frame index
                    space4.tStart = t  # local t and not account for scr refresh
                    space4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space4.status = STARTED
                    space4.setAutoDraw(True)
                
                # if space4 is active this frame...
                if space4.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini2_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini2_2" ---
            for thisComponent in mini2_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m2Code2
            if m2Count == 12:
                mini2Loop.finished = True
            m2Sound1.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini2_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM2Corr repeats of 'm2CorrLoop'
        
        
        # set up handler to look after randomisation of conditions etc
        m2IncorrLoop = data.TrialHandler(nReps=nRepsM2Incorr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m2IncorrLoop')
        thisExp.addLoop(m2IncorrLoop)  # add the loop to the experiment
        thisM2IncorrLoop = m2IncorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM2IncorrLoop.rgb)
        if thisM2IncorrLoop != None:
            for paramName in thisM2IncorrLoop:
                exec('{} = thisM2IncorrLoop[paramName]'.format(paramName))
        
        for thisM2IncorrLoop in m2IncorrLoop:
            currentLoop = m2IncorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM2IncorrLoop.rgb)
            if thisM2IncorrLoop != None:
                for paramName in thisM2IncorrLoop:
                    exec('{} = thisM2IncorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini2_3" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m2Code3
            m2Count = m2Count+1
            m2IncorrPL.setImage(img)
            m2IncorrCON.setPos([m2Posi[0]])
            m2IncorrCON.setText(conWord)
            m2IncorrDIST.setPos(incorrPosi2)
            m2IncorrDIST.setText(incorrAns2)
            m2Sound2.setSound(audio, secs=2, hamming=True)
            m2Sound2.setVolume(3.0, log=False)
            m2Key2.keys = []
            m2Key2.rt = []
            _m2Key2_allKeys = []
            # keep track of which components have finished
            mini2_3Components = [m2IncorrPL, m2IncorrCON, m2IncorrDIST, m2Sound2, m2Key2, space5]
            for thisComponent in mini2_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini2_3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m2IncorrPL* updates
                
                # if m2IncorrPL is starting this frame...
                if m2IncorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m2IncorrPL.frameNStart = frameN  # exact frame index
                    m2IncorrPL.tStart = t  # local t and not account for scr refresh
                    m2IncorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m2IncorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m2IncorrPL.status = STARTED
                    m2IncorrPL.setAutoDraw(True)
                
                # if m2IncorrPL is active this frame...
                if m2IncorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m2IncorrCON* updates
                
                # if m2IncorrCON is starting this frame...
                if m2IncorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m2IncorrCON.frameNStart = frameN  # exact frame index
                    m2IncorrCON.tStart = t  # local t and not account for scr refresh
                    m2IncorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m2IncorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m2IncorrCON.status = STARTED
                    m2IncorrCON.setAutoDraw(True)
                
                # if m2IncorrCON is active this frame...
                if m2IncorrCON.status == STARTED:
                    # update params
                    pass
                
                # *m2IncorrDIST* updates
                
                # if m2IncorrDIST is starting this frame...
                if m2IncorrDIST.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m2IncorrDIST.frameNStart = frameN  # exact frame index
                    m2IncorrDIST.tStart = t  # local t and not account for scr refresh
                    m2IncorrDIST.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m2IncorrDIST, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m2IncorrDIST.status = STARTED
                    m2IncorrDIST.setAutoDraw(True)
                
                # if m2IncorrDIST is active this frame...
                if m2IncorrDIST.status == STARTED:
                    # update params
                    pass
                # start/stop m2Sound2
                
                # if m2Sound2 is starting this frame...
                if m2Sound2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m2Sound2.frameNStart = frameN  # exact frame index
                    m2Sound2.tStart = t  # local t and not account for scr refresh
                    m2Sound2.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m2Sound2.status = STARTED
                    m2Sound2.play(when=win)  # sync with win flip
                
                # if m2Sound2 is stopping this frame...
                if m2Sound2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m2Sound2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m2Sound2.tStop = t  # not accounting for scr refresh
                        m2Sound2.frameNStop = frameN  # exact frame index
                        # update status
                        m2Sound2.status = FINISHED
                        m2Sound2.stop()
                
                # *m2Key2* updates
                
                # if m2Key2 is starting this frame...
                if m2Key2.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m2Key2.frameNStart = frameN  # exact frame index
                    m2Key2.tStart = t  # local t and not account for scr refresh
                    m2Key2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m2Key2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m2Key2.status = STARTED
                    # keyboard checking is just starting
                    m2Key2.clock.reset()  # now t=0
                if m2Key2.status == STARTED:
                    theseKeys = m2Key2.getKeys(keyList=['space'], waitRelease=False)
                    _m2Key2_allKeys.extend(theseKeys)
                    if len(_m2Key2_allKeys):
                        m2Key2.keys = _m2Key2_allKeys[-1].name  # just the last key pressed
                        m2Key2.rt = _m2Key2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space5* updates
                
                # if space5 is starting this frame...
                if space5.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space5.frameNStart = frameN  # exact frame index
                    space5.tStart = t  # local t and not account for scr refresh
                    space5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space5.status = STARTED
                    space5.setAutoDraw(True)
                
                # if space5 is active this frame...
                if space5.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini2_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini2_3" ---
            for thisComponent in mini2_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m2Code3
            if m2Count==12:
                mini1Loop.finished = True
            m2Sound2.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini2_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM2Incorr repeats of 'm2IncorrLoop'
        
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'mini2Loop'
    
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'img1'


# set up handler to look after randomisation of conditions etc
ortho2 = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='ortho2')
thisExp.addLoop(ortho2)  # add the loop to the experiment
thisOrtho2 = ortho2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOrtho2.rgb)
if thisOrtho2 != None:
    for paramName in thisOrtho2:
        exec('{} = thisOrtho2[paramName]'.format(paramName))

for thisOrtho2 in ortho2:
    currentLoop = ortho2
    # abbreviate parameter names if possible (e.g. rgb = thisOrtho2.rgb)
    if thisOrtho2 != None:
        for paramName in thisOrtho2:
            exec('{} = thisOrtho2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    exp3Loop1 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("orthostim_" + expInfo['group'] + ".xlsx", selection='4:8'),
        seed=None, name='exp3Loop1')
    thisExp.addLoop(exp3Loop1)  # add the loop to the experiment
    thisExp3Loop1 = exp3Loop1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExp3Loop1.rgb)
    if thisExp3Loop1 != None:
        for paramName in thisExp3Loop1:
            exec('{} = thisExp3Loop1[paramName]'.format(paramName))
    
    for thisExp3Loop1 in exp3Loop1:
        currentLoop = exp3Loop1
        # abbreviate parameter names if possible (e.g. rgb = thisExp3Loop1.rgb)
        if thisExp3Loop1 != None:
            for paramName in thisExp3Loop1:
                exec('{} = thisExp3Loop1[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "exp3_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        e3PL.setText(plWord)
        # keep track of which components have finished
        exp3_1Components = [e3Focal1, e3PL]
        for thisComponent in exp3_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp3_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e3Focal1* updates
            
            # if e3Focal1 is starting this frame...
            if e3Focal1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                e3Focal1.frameNStart = frameN  # exact frame index
                e3Focal1.tStart = t  # local t and not account for scr refresh
                e3Focal1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e3Focal1, 'tStartRefresh')  # time at next scr refresh
                # update status
                e3Focal1.status = STARTED
                e3Focal1.setAutoDraw(True)
            
            # if e3Focal1 is active this frame...
            if e3Focal1.status == STARTED:
                # update params
                pass
            
            # if e3Focal1 is stopping this frame...
            if e3Focal1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e3Focal1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    e3Focal1.tStop = t  # not accounting for scr refresh
                    e3Focal1.frameNStop = frameN  # exact frame index
                    # update status
                    e3Focal1.status = FINISHED
                    e3Focal1.setAutoDraw(False)
            
            # *e3PL* updates
            
            # if e3PL is starting this frame...
            if e3PL.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
                # keep track of start time/frame for later
                e3PL.frameNStart = frameN  # exact frame index
                e3PL.tStart = t  # local t and not account for scr refresh
                e3PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e3PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                e3PL.status = STARTED
                e3PL.setAutoDraw(True)
            
            # if e3PL is active this frame...
            if e3PL.status == STARTED:
                # update params
                pass
            
            # if e3PL is stopping this frame...
            if e3PL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e3PL.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    e3PL.tStop = t  # not accounting for scr refresh
                    e3PL.frameNStop = frameN  # exact frame index
                    # update status
                    e3PL.status = FINISHED
                    e3PL.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp3_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp3_1" ---
        for thisComponent in exp3_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.100000)
        
        # --- Prepare to start Routine "exp3_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from e3Code2
        e3Count = e3Count+1
        e3Con.setText(conWord)
        e3Sound.setSound(audio, hamming=True)
        e3Sound.setVolume(3.0, log=False)
        e3Key.keys = []
        e3Key.rt = []
        _e3Key_allKeys = []
        # keep track of which components have finished
        exp3_2Components = [e3Focal2, e3Con, e3Sound, e3Key, space6]
        for thisComponent in exp3_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp3_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e3Focal2* updates
            
            # if e3Focal2 is starting this frame...
            if e3Focal2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                e3Focal2.frameNStart = frameN  # exact frame index
                e3Focal2.tStart = t  # local t and not account for scr refresh
                e3Focal2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e3Focal2, 'tStartRefresh')  # time at next scr refresh
                # update status
                e3Focal2.status = STARTED
                e3Focal2.setAutoDraw(True)
            
            # if e3Focal2 is active this frame...
            if e3Focal2.status == STARTED:
                # update params
                pass
            
            # if e3Focal2 is stopping this frame...
            if e3Focal2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e3Focal2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    e3Focal2.tStop = t  # not accounting for scr refresh
                    e3Focal2.frameNStop = frameN  # exact frame index
                    # update status
                    e3Focal2.status = FINISHED
                    e3Focal2.setAutoDraw(False)
            
            # *e3Con* updates
            
            # if e3Con is starting this frame...
            if e3Con.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e3Con.frameNStart = frameN  # exact frame index
                e3Con.tStart = t  # local t and not account for scr refresh
                e3Con.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e3Con, 'tStartRefresh')  # time at next scr refresh
                # update status
                e3Con.status = STARTED
                e3Con.setAutoDraw(True)
            
            # if e3Con is active this frame...
            if e3Con.status == STARTED:
                # update params
                pass
            # start/stop e3Sound
            
            # if e3Sound is starting this frame...
            if e3Sound.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e3Sound.frameNStart = frameN  # exact frame index
                e3Sound.tStart = t  # local t and not account for scr refresh
                e3Sound.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                e3Sound.status = STARTED
                e3Sound.play(when=win)  # sync with win flip
            
            # *e3Key* updates
            
            # if e3Key is starting this frame...
            if e3Key.status == NOT_STARTED and t >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                e3Key.frameNStart = frameN  # exact frame index
                e3Key.tStart = t  # local t and not account for scr refresh
                e3Key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e3Key, 'tStartRefresh')  # time at next scr refresh
                # update status
                e3Key.status = STARTED
                # keyboard checking is just starting
                e3Key.clock.reset()  # now t=0
            if e3Key.status == STARTED:
                theseKeys = e3Key.getKeys(keyList=['space'], waitRelease=False)
                _e3Key_allKeys.extend(theseKeys)
                if len(_e3Key_allKeys):
                    e3Key.keys = _e3Key_allKeys[-1].name  # just the last key pressed
                    e3Key.rt = _e3Key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *space6* updates
            
            # if space6 is starting this frame...
            if space6.status == NOT_STARTED and tThisFlip >= 3.2-frameTolerance:
                # keep track of start time/frame for later
                space6.frameNStart = frameN  # exact frame index
                space6.tStart = t  # local t and not account for scr refresh
                space6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space6, 'tStartRefresh')  # time at next scr refresh
                # update status
                space6.status = STARTED
                space6.setAutoDraw(True)
            
            # if space6 is active this frame...
            if space6.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp3_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp3_2" ---
        for thisComponent in exp3_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from e3Code2
        if e3Count == 4:
            exp3Loop1.finished = True
        else:
            pass
        e3Sound.stop()  # ensure sound has stopped at end of routine
        # the Routine "exp3_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'exp3Loop1'
    
    
    # set up handler to look after randomisation of conditions etc
    mini3Loop = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("orthostim_" + expInfo['group'] + ".xlsx", selection='4:8'),
        seed=None, name='mini3Loop')
    thisExp.addLoop(mini3Loop)  # add the loop to the experiment
    thisMini3Loop = mini3Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMini3Loop.rgb)
    if thisMini3Loop != None:
        for paramName in thisMini3Loop:
            exec('{} = thisMini3Loop[paramName]'.format(paramName))
    
    for thisMini3Loop in mini3Loop:
        currentLoop = mini3Loop
        # abbreviate parameter names if possible (e.g. rgb = thisMini3Loop.rgb)
        if thisMini3Loop != None:
            for paramName in thisMini3Loop:
                exec('{} = thisMini3Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mini3_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from m3Code1
        random.shuffle(m3Posi)
        m3PL.setText(plWord)
        m3CON.setPos([m3Posi[0]])
        m3CON.setText(conWord)
        # reset m3CON to account for continued clicks & clear times on/off
        m3CON.reset()
        m3DIST1.setPos([m3Posi[1]])
        m3DIST1.setText(incorr1)
        # reset m3DIST1 to account for continued clicks & clear times on/off
        m3DIST1.reset()
        m3DIST2.setPos([m3Posi[2]])
        m3DIST2.setText(incorr2)
        # reset m3DIST2 to account for continued clicks & clear times on/off
        m3DIST2.reset()
        m3DIST3.setPos([m3Posi[3]])
        m3DIST3.setText(incorr3)
        # reset m3DIST3 to account for continued clicks & clear times on/off
        m3DIST3.reset()
        # setup some python lists for storing info about the m3Mouse
        m3Mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        mini3_1Components = [m3PL, m3CON, m3DIST1, m3DIST2, m3DIST3, m3Mouse]
        for thisComponent in mini3_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mini3_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *m3PL* updates
            
            # if m3PL is starting this frame...
            if m3PL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m3PL.frameNStart = frameN  # exact frame index
                m3PL.tStart = t  # local t and not account for scr refresh
                m3PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m3PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                m3PL.status = STARTED
                m3PL.setAutoDraw(True)
            
            # if m3PL is active this frame...
            if m3PL.status == STARTED:
                # update params
                pass
            # *m3CON* updates
            
            # if m3CON is starting this frame...
            if m3CON.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m3CON.frameNStart = frameN  # exact frame index
                m3CON.tStart = t  # local t and not account for scr refresh
                m3CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m3CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                m3CON.status = STARTED
                m3CON.setAutoDraw(True)
            
            # if m3CON is active this frame...
            if m3CON.status == STARTED:
                # update params
                pass
                # check whether m3CON has been pressed
                if m3CON.isClicked:
                    if not m3CON.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m3CON.timesOn.append(m3CON.buttonClock.getTime())
                        m3CON.timesOff.append(m3CON.buttonClock.getTime())
                    elif len(m3CON.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m3CON.timesOff[-1] = m3CON.buttonClock.getTime()
                    if not m3CON.wasClicked:
                        # end routine when m3CON is clicked
                        continueRoutine = False
                    if not m3CON.wasClicked:
                        # run callback code when m3CON is clicked
                        pass
            # take note of whether m3CON was clicked, so that next frame we know if clicks are new
            m3CON.wasClicked = m3CON.isClicked and m3CON.status == STARTED
            # *m3DIST1* updates
            
            # if m3DIST1 is starting this frame...
            if m3DIST1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m3DIST1.frameNStart = frameN  # exact frame index
                m3DIST1.tStart = t  # local t and not account for scr refresh
                m3DIST1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m3DIST1, 'tStartRefresh')  # time at next scr refresh
                # update status
                m3DIST1.status = STARTED
                m3DIST1.setAutoDraw(True)
            
            # if m3DIST1 is active this frame...
            if m3DIST1.status == STARTED:
                # update params
                pass
                # check whether m3DIST1 has been pressed
                if m3DIST1.isClicked:
                    if not m3DIST1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m3DIST1.timesOn.append(m3DIST1.buttonClock.getTime())
                        m3DIST1.timesOff.append(m3DIST1.buttonClock.getTime())
                    elif len(m3DIST1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m3DIST1.timesOff[-1] = m3DIST1.buttonClock.getTime()
                    if not m3DIST1.wasClicked:
                        # end routine when m3DIST1 is clicked
                        continueRoutine = False
                    if not m3DIST1.wasClicked:
                        # run callback code when m3DIST1 is clicked
                        pass
            # take note of whether m3DIST1 was clicked, so that next frame we know if clicks are new
            m3DIST1.wasClicked = m3DIST1.isClicked and m3DIST1.status == STARTED
            # *m3DIST2* updates
            
            # if m3DIST2 is starting this frame...
            if m3DIST2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m3DIST2.frameNStart = frameN  # exact frame index
                m3DIST2.tStart = t  # local t and not account for scr refresh
                m3DIST2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m3DIST2, 'tStartRefresh')  # time at next scr refresh
                # update status
                m3DIST2.status = STARTED
                m3DIST2.setAutoDraw(True)
            
            # if m3DIST2 is active this frame...
            if m3DIST2.status == STARTED:
                # update params
                pass
                # check whether m3DIST2 has been pressed
                if m3DIST2.isClicked:
                    if not m3DIST2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m3DIST2.timesOn.append(m3DIST2.buttonClock.getTime())
                        m3DIST2.timesOff.append(m3DIST2.buttonClock.getTime())
                    elif len(m3DIST2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m3DIST2.timesOff[-1] = m3DIST2.buttonClock.getTime()
                    if not m3DIST2.wasClicked:
                        # end routine when m3DIST2 is clicked
                        continueRoutine = False
                    if not m3DIST2.wasClicked:
                        # run callback code when m3DIST2 is clicked
                        pass
            # take note of whether m3DIST2 was clicked, so that next frame we know if clicks are new
            m3DIST2.wasClicked = m3DIST2.isClicked and m3DIST2.status == STARTED
            # *m3DIST3* updates
            
            # if m3DIST3 is starting this frame...
            if m3DIST3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m3DIST3.frameNStart = frameN  # exact frame index
                m3DIST3.tStart = t  # local t and not account for scr refresh
                m3DIST3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m3DIST3, 'tStartRefresh')  # time at next scr refresh
                # update status
                m3DIST3.status = STARTED
                m3DIST3.setAutoDraw(True)
            
            # if m3DIST3 is active this frame...
            if m3DIST3.status == STARTED:
                # update params
                pass
                # check whether m3DIST3 has been pressed
                if m3DIST3.isClicked:
                    if not m3DIST3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m3DIST3.timesOn.append(m3DIST3.buttonClock.getTime())
                        m3DIST3.timesOff.append(m3DIST3.buttonClock.getTime())
                    elif len(m3DIST3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m3DIST3.timesOff[-1] = m3DIST3.buttonClock.getTime()
                    if not m3DIST3.wasClicked:
                        # end routine when m3DIST3 is clicked
                        continueRoutine = False
                    if not m3DIST3.wasClicked:
                        # run callback code when m3DIST3 is clicked
                        pass
            # take note of whether m3DIST3 was clicked, so that next frame we know if clicks are new
            m3DIST3.wasClicked = m3DIST3.isClicked and m3DIST3.status == STARTED
            # *m3Mouse* updates
            
            # if m3Mouse is starting this frame...
            if m3Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m3Mouse.frameNStart = frameN  # exact frame index
                m3Mouse.tStart = t  # local t and not account for scr refresh
                m3Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m3Mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'm3Mouse.started')
                # update status
                m3Mouse.status = STARTED
                m3Mouse.mouseClock.reset()
                prevButtonState = m3Mouse.getPressed()  # if button is down already this ISN'T a new click
            if m3Mouse.status == STARTED:  # only update if started and not finished!
                buttons = m3Mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = core.getFromNames([m3CON,m3DIST1,m3DIST2,m3DIST3])
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(m3Mouse):
                                gotValidClick = True
                                m3Mouse.clicked_name.append(obj.name)
                        continueRoutine = False  # end routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mini3_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mini3_1" ---
        for thisComponent in mini3_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from m3Code1
        if m3Mouse.isPressedIn(m3CON):
            nRepsM3Corr = True
            nRepsM3Incorr = False
            thisExp.addData("mCorr Response",m3CON.text)
        else:
            nRepsM3Corr = False
            nRepsM3Incorr = True
        
        if m3Mouse.isPressedIn(m3DIST1):
            incorrAns3=m3DIST1.text
            incorrPosi3=m3DIST1.pos
            thisExp.addData("mIncorr Repsonse",m3DIST1.text)
        elif m3Mouse.isPressedIn(m3DIST2):
            incorrAns3=m3DIST2.text
            incorrPosi3=m3DIST2.pos
            thisExp.addData("mIncorr Repsonse",m3DIST2.text)
        elif m3Mouse.isPressedIn(m3DIST3):
            incorrAns3=m3DIST3.text
            incorrPosi3=m3DIST3.pos
            thisExp.addData("mIncorr Repsonse",m3DIST3.text)
        # store data for mini3Loop (TrialHandler)
        # the Routine "mini3_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        m3CorrLoop = data.TrialHandler(nReps=nRepsM3Corr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m3CorrLoop')
        thisExp.addLoop(m3CorrLoop)  # add the loop to the experiment
        thisM3CorrLoop = m3CorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM3CorrLoop.rgb)
        if thisM3CorrLoop != None:
            for paramName in thisM3CorrLoop:
                exec('{} = thisM3CorrLoop[paramName]'.format(paramName))
        
        for thisM3CorrLoop in m3CorrLoop:
            currentLoop = m3CorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM3CorrLoop.rgb)
            if thisM3CorrLoop != None:
                for paramName in thisM3CorrLoop:
                    exec('{} = thisM3CorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini3_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m3Code2
            m3Count = m3Count+1
            m3CorrPL.setText(plWord)
            m3CorrCON.setPos([m3Posi[0]])
            m3CorrCON.setText(conWord)
            m3Sound1.setSound(audio, secs=2, hamming=True)
            m3Sound1.setVolume(3.0, log=False)
            m2Key1.keys = []
            m2Key1.rt = []
            _m2Key1_allKeys = []
            # keep track of which components have finished
            mini3_2Components = [m3CorrPL, m3CorrCON, m3Sound1, m2Key1, space7]
            for thisComponent in mini3_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini3_2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m3CorrPL* updates
                
                # if m3CorrPL is starting this frame...
                if m3CorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m3CorrPL.frameNStart = frameN  # exact frame index
                    m3CorrPL.tStart = t  # local t and not account for scr refresh
                    m3CorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m3CorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m3CorrPL.status = STARTED
                    m3CorrPL.setAutoDraw(True)
                
                # if m3CorrPL is active this frame...
                if m3CorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m3CorrCON* updates
                
                # if m3CorrCON is starting this frame...
                if m3CorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m3CorrCON.frameNStart = frameN  # exact frame index
                    m3CorrCON.tStart = t  # local t and not account for scr refresh
                    m3CorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m3CorrCON, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'm3CorrCON.started')
                    # update status
                    m3CorrCON.status = STARTED
                    m3CorrCON.setAutoDraw(True)
                
                # if m3CorrCON is active this frame...
                if m3CorrCON.status == STARTED:
                    # update params
                    pass
                # start/stop m3Sound1
                
                # if m3Sound1 is starting this frame...
                if m3Sound1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m3Sound1.frameNStart = frameN  # exact frame index
                    m3Sound1.tStart = t  # local t and not account for scr refresh
                    m3Sound1.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m3Sound1.status = STARTED
                    m3Sound1.play(when=win)  # sync with win flip
                
                # if m3Sound1 is stopping this frame...
                if m3Sound1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m3Sound1.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m3Sound1.tStop = t  # not accounting for scr refresh
                        m3Sound1.frameNStop = frameN  # exact frame index
                        # update status
                        m3Sound1.status = FINISHED
                        m3Sound1.stop()
                
                # *m2Key1* updates
                
                # if m2Key1 is starting this frame...
                if m2Key1.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m2Key1.frameNStart = frameN  # exact frame index
                    m2Key1.tStart = t  # local t and not account for scr refresh
                    m2Key1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m2Key1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m2Key1.status = STARTED
                    # keyboard checking is just starting
                    m2Key1.clock.reset()  # now t=0
                if m2Key1.status == STARTED:
                    theseKeys = m2Key1.getKeys(keyList=['space'], waitRelease=False)
                    _m2Key1_allKeys.extend(theseKeys)
                    if len(_m2Key1_allKeys):
                        m2Key1.keys = _m2Key1_allKeys[-1].name  # just the last key pressed
                        m2Key1.rt = _m2Key1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space7* updates
                
                # if space7 is starting this frame...
                if space7.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space7.frameNStart = frameN  # exact frame index
                    space7.tStart = t  # local t and not account for scr refresh
                    space7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space7, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space7.status = STARTED
                    space7.setAutoDraw(True)
                
                # if space7 is active this frame...
                if space7.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini3_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini3_2" ---
            for thisComponent in mini3_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m3Code2
            if m3Count == 12:
                mini3Loop.finished = True
            m3Sound1.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini3_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM3Corr repeats of 'm3CorrLoop'
        
        
        # set up handler to look after randomisation of conditions etc
        m3IncorrLoop = data.TrialHandler(nReps=nRepsM3Incorr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m3IncorrLoop')
        thisExp.addLoop(m3IncorrLoop)  # add the loop to the experiment
        thisM3IncorrLoop = m3IncorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM3IncorrLoop.rgb)
        if thisM3IncorrLoop != None:
            for paramName in thisM3IncorrLoop:
                exec('{} = thisM3IncorrLoop[paramName]'.format(paramName))
        
        for thisM3IncorrLoop in m3IncorrLoop:
            currentLoop = m3IncorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM3IncorrLoop.rgb)
            if thisM3IncorrLoop != None:
                for paramName in thisM3IncorrLoop:
                    exec('{} = thisM3IncorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini3_3" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m3Code3
            m3Count = m3Count+1
            m3IncorrPL.setText(plWord)
            m3IncorrCON.setPos([m3Posi[0]])
            m3IncorrCON.setText(conWord)
            m3IncorrDIST.setPos(incorrPosi3)
            m3IncorrDIST.setText(incorrAns3)
            m3Sound2.setSound(audio, secs=2, hamming=True)
            m3Sound2.setVolume(3.0, log=False)
            m3Key2.keys = []
            m3Key2.rt = []
            _m3Key2_allKeys = []
            # keep track of which components have finished
            mini3_3Components = [m3IncorrPL, m3IncorrCON, m3IncorrDIST, m3Sound2, m3Key2, space8]
            for thisComponent in mini3_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini3_3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m3IncorrPL* updates
                
                # if m3IncorrPL is starting this frame...
                if m3IncorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m3IncorrPL.frameNStart = frameN  # exact frame index
                    m3IncorrPL.tStart = t  # local t and not account for scr refresh
                    m3IncorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m3IncorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m3IncorrPL.status = STARTED
                    m3IncorrPL.setAutoDraw(True)
                
                # if m3IncorrPL is active this frame...
                if m3IncorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m3IncorrCON* updates
                
                # if m3IncorrCON is starting this frame...
                if m3IncorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m3IncorrCON.frameNStart = frameN  # exact frame index
                    m3IncorrCON.tStart = t  # local t and not account for scr refresh
                    m3IncorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m3IncorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m3IncorrCON.status = STARTED
                    m3IncorrCON.setAutoDraw(True)
                
                # if m3IncorrCON is active this frame...
                if m3IncorrCON.status == STARTED:
                    # update params
                    pass
                
                # *m3IncorrDIST* updates
                
                # if m3IncorrDIST is starting this frame...
                if m3IncorrDIST.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m3IncorrDIST.frameNStart = frameN  # exact frame index
                    m3IncorrDIST.tStart = t  # local t and not account for scr refresh
                    m3IncorrDIST.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m3IncorrDIST, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m3IncorrDIST.status = STARTED
                    m3IncorrDIST.setAutoDraw(True)
                
                # if m3IncorrDIST is active this frame...
                if m3IncorrDIST.status == STARTED:
                    # update params
                    pass
                # start/stop m3Sound2
                
                # if m3Sound2 is starting this frame...
                if m3Sound2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m3Sound2.frameNStart = frameN  # exact frame index
                    m3Sound2.tStart = t  # local t and not account for scr refresh
                    m3Sound2.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m3Sound2.status = STARTED
                    m3Sound2.play(when=win)  # sync with win flip
                
                # if m3Sound2 is stopping this frame...
                if m3Sound2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m3Sound2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m3Sound2.tStop = t  # not accounting for scr refresh
                        m3Sound2.frameNStop = frameN  # exact frame index
                        # update status
                        m3Sound2.status = FINISHED
                        m3Sound2.stop()
                
                # *m3Key2* updates
                
                # if m3Key2 is starting this frame...
                if m3Key2.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m3Key2.frameNStart = frameN  # exact frame index
                    m3Key2.tStart = t  # local t and not account for scr refresh
                    m3Key2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m3Key2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m3Key2.status = STARTED
                    # keyboard checking is just starting
                    m3Key2.clock.reset()  # now t=0
                if m3Key2.status == STARTED:
                    theseKeys = m3Key2.getKeys(keyList=['space'], waitRelease=False)
                    _m3Key2_allKeys.extend(theseKeys)
                    if len(_m3Key2_allKeys):
                        m3Key2.keys = _m3Key2_allKeys[-1].name  # just the last key pressed
                        m3Key2.rt = _m3Key2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space8* updates
                
                # if space8 is starting this frame...
                if space8.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space8.frameNStart = frameN  # exact frame index
                    space8.tStart = t  # local t and not account for scr refresh
                    space8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space8, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space8.status = STARTED
                    space8.setAutoDraw(True)
                
                # if space8 is active this frame...
                if space8.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini3_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini3_3" ---
            for thisComponent in mini3_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m3Code3
            if m3Count==12:
                mini3Loop.finished = True
            m3Sound2.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini3_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM3Incorr repeats of 'm3IncorrLoop'
        
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'mini3Loop'
    
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'ortho2'


# set up handler to look after randomisation of conditions etc
img2 = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='img2')
thisExp.addLoop(img2)  # add the loop to the experiment
thisImg2 = img2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisImg2.rgb)
if thisImg2 != None:
    for paramName in thisImg2:
        exec('{} = thisImg2[paramName]'.format(paramName))

for thisImg2 in img2:
    currentLoop = img2
    # abbreviate parameter names if possible (e.g. rgb = thisImg2.rgb)
    if thisImg2 != None:
        for paramName in thisImg2:
            exec('{} = thisImg2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    exp4Loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("imgstim_"+expInfo['group']+".xlsx", selection='4:8'),
        seed=None, name='exp4Loop')
    thisExp.addLoop(exp4Loop)  # add the loop to the experiment
    thisExp4Loop = exp4Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExp4Loop.rgb)
    if thisExp4Loop != None:
        for paramName in thisExp4Loop:
            exec('{} = thisExp4Loop[paramName]'.format(paramName))
    
    for thisExp4Loop in exp4Loop:
        currentLoop = exp4Loop
        # abbreviate parameter names if possible (e.g. rgb = thisExp4Loop.rgb)
        if thisExp4Loop != None:
            for paramName in thisExp4Loop:
                exec('{} = thisExp4Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "exp4_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        e4PL.setImage(img)
        # keep track of which components have finished
        exp4_1Components = [e4Focal1, e4PL]
        for thisComponent in exp4_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp4_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e4Focal1* updates
            
            # if e4Focal1 is starting this frame...
            if e4Focal1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                e4Focal1.frameNStart = frameN  # exact frame index
                e4Focal1.tStart = t  # local t and not account for scr refresh
                e4Focal1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e4Focal1, 'tStartRefresh')  # time at next scr refresh
                # update status
                e4Focal1.status = STARTED
                e4Focal1.setAutoDraw(True)
            
            # if e4Focal1 is active this frame...
            if e4Focal1.status == STARTED:
                # update params
                pass
            
            # if e4Focal1 is stopping this frame...
            if e4Focal1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e4Focal1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    e4Focal1.tStop = t  # not accounting for scr refresh
                    e4Focal1.frameNStop = frameN  # exact frame index
                    # update status
                    e4Focal1.status = FINISHED
                    e4Focal1.setAutoDraw(False)
            
            # *e4PL* updates
            
            # if e4PL is starting this frame...
            if e4PL.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
                # keep track of start time/frame for later
                e4PL.frameNStart = frameN  # exact frame index
                e4PL.tStart = t  # local t and not account for scr refresh
                e4PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e4PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                e4PL.status = STARTED
                e4PL.setAutoDraw(True)
            
            # if e4PL is active this frame...
            if e4PL.status == STARTED:
                # update params
                pass
            
            # if e4PL is stopping this frame...
            if e4PL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e4PL.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    e4PL.tStop = t  # not accounting for scr refresh
                    e4PL.frameNStop = frameN  # exact frame index
                    # update status
                    e4PL.status = FINISHED
                    e4PL.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp4_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp4_1" ---
        for thisComponent in exp4_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.100000)
        
        # --- Prepare to start Routine "exp4_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from e4Code2
        e4Count = e4Count+1
        e4CON.setText(conWord)
        e4Sound.setSound(audio, hamming=True)
        e4Sound.setVolume(3.0, log=False)
        e4Key.keys = []
        e4Key.rt = []
        _e4Key_allKeys = []
        # keep track of which components have finished
        exp4_2Components = [e4Focal2, e4CON, e4Sound, e4Key, space9]
        for thisComponent in exp4_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp4_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e4Focal2* updates
            
            # if e4Focal2 is starting this frame...
            if e4Focal2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                e4Focal2.frameNStart = frameN  # exact frame index
                e4Focal2.tStart = t  # local t and not account for scr refresh
                e4Focal2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e4Focal2, 'tStartRefresh')  # time at next scr refresh
                # update status
                e4Focal2.status = STARTED
                e4Focal2.setAutoDraw(True)
            
            # if e4Focal2 is active this frame...
            if e4Focal2.status == STARTED:
                # update params
                pass
            
            # if e4Focal2 is stopping this frame...
            if e4Focal2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e4Focal2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    e4Focal2.tStop = t  # not accounting for scr refresh
                    e4Focal2.frameNStop = frameN  # exact frame index
                    # update status
                    e4Focal2.status = FINISHED
                    e4Focal2.setAutoDraw(False)
            
            # *e4CON* updates
            
            # if e4CON is starting this frame...
            if e4CON.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e4CON.frameNStart = frameN  # exact frame index
                e4CON.tStart = t  # local t and not account for scr refresh
                e4CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e4CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                e4CON.status = STARTED
                e4CON.setAutoDraw(True)
            
            # if e4CON is active this frame...
            if e4CON.status == STARTED:
                # update params
                pass
            # start/stop e4Sound
            
            # if e4Sound is starting this frame...
            if e4Sound.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e4Sound.frameNStart = frameN  # exact frame index
                e4Sound.tStart = t  # local t and not account for scr refresh
                e4Sound.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                e4Sound.status = STARTED
                e4Sound.play(when=win)  # sync with win flip
            
            # *e4Key* updates
            
            # if e4Key is starting this frame...
            if e4Key.status == NOT_STARTED and t >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                e4Key.frameNStart = frameN  # exact frame index
                e4Key.tStart = t  # local t and not account for scr refresh
                e4Key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e4Key, 'tStartRefresh')  # time at next scr refresh
                # update status
                e4Key.status = STARTED
                # keyboard checking is just starting
                e4Key.clock.reset()  # now t=0
            if e4Key.status == STARTED:
                theseKeys = e4Key.getKeys(keyList=['space'], waitRelease=False)
                _e4Key_allKeys.extend(theseKeys)
                if len(_e4Key_allKeys):
                    e4Key.keys = _e4Key_allKeys[-1].name  # just the last key pressed
                    e4Key.rt = _e4Key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *space9* updates
            
            # if space9 is starting this frame...
            if space9.status == NOT_STARTED and tThisFlip >= 3.2-frameTolerance:
                # keep track of start time/frame for later
                space9.frameNStart = frameN  # exact frame index
                space9.tStart = t  # local t and not account for scr refresh
                space9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space9, 'tStartRefresh')  # time at next scr refresh
                # update status
                space9.status = STARTED
                space9.setAutoDraw(True)
            
            # if space9 is active this frame...
            if space9.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp4_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp4_2" ---
        for thisComponent in exp4_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from e4Code2
        if e4Count ==4:
            exp4Loop.finished = True
        else:
            pass
        e4Sound.stop()  # ensure sound has stopped at end of routine
        # the Routine "exp4_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'exp4Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    mini4Loop = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("imgstim_"+expInfo['group']+".xlsx", selection='4:8'),
        seed=None, name='mini4Loop')
    thisExp.addLoop(mini4Loop)  # add the loop to the experiment
    thisMini4Loop = mini4Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMini4Loop.rgb)
    if thisMini4Loop != None:
        for paramName in thisMini4Loop:
            exec('{} = thisMini4Loop[paramName]'.format(paramName))
    
    for thisMini4Loop in mini4Loop:
        currentLoop = mini4Loop
        # abbreviate parameter names if possible (e.g. rgb = thisMini4Loop.rgb)
        if thisMini4Loop != None:
            for paramName in thisMini4Loop:
                exec('{} = thisMini4Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mini4_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from m4Code1_2
        random.shuffle(m4Posi)
        m4PL.setImage(img)
        m4CON.setPos([m4Posi[0]])
        m4CON.setText(conWord)
        # reset m4CON to account for continued clicks & clear times on/off
        m4CON.reset()
        m4DIST1.setPos([m4Posi[1]])
        m4DIST1.setText(incorr1)
        # reset m4DIST1 to account for continued clicks & clear times on/off
        m4DIST1.reset()
        m4DIST2.setPos([m4Posi[2]])
        m4DIST2.setText(incorr2)
        # reset m4DIST2 to account for continued clicks & clear times on/off
        m4DIST2.reset()
        m4DIST3.setPos([m4Posi[3]])
        m4DIST3.setText(incorr3)
        # reset m4DIST3 to account for continued clicks & clear times on/off
        m4DIST3.reset()
        # setup some python lists for storing info about the m4Mouse
        m4Mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        mini4_1Components = [m4PL, m4CON, m4DIST1, m4DIST2, m4DIST3, m4Mouse]
        for thisComponent in mini4_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mini4_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *m4PL* updates
            
            # if m4PL is starting this frame...
            if m4PL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m4PL.frameNStart = frameN  # exact frame index
                m4PL.tStart = t  # local t and not account for scr refresh
                m4PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m4PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                m4PL.status = STARTED
                m4PL.setAutoDraw(True)
            
            # if m4PL is active this frame...
            if m4PL.status == STARTED:
                # update params
                pass
            # *m4CON* updates
            
            # if m4CON is starting this frame...
            if m4CON.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m4CON.frameNStart = frameN  # exact frame index
                m4CON.tStart = t  # local t and not account for scr refresh
                m4CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m4CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                m4CON.status = STARTED
                m4CON.setAutoDraw(True)
            
            # if m4CON is active this frame...
            if m4CON.status == STARTED:
                # update params
                pass
                # check whether m4CON has been pressed
                if m4CON.isClicked:
                    if not m4CON.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m4CON.timesOn.append(m4CON.buttonClock.getTime())
                        m4CON.timesOff.append(m4CON.buttonClock.getTime())
                    elif len(m4CON.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m4CON.timesOff[-1] = m4CON.buttonClock.getTime()
                    if not m4CON.wasClicked:
                        # end routine when m4CON is clicked
                        continueRoutine = False
                    if not m4CON.wasClicked:
                        # run callback code when m4CON is clicked
                        pass
            # take note of whether m4CON was clicked, so that next frame we know if clicks are new
            m4CON.wasClicked = m4CON.isClicked and m4CON.status == STARTED
            # *m4DIST1* updates
            
            # if m4DIST1 is starting this frame...
            if m4DIST1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m4DIST1.frameNStart = frameN  # exact frame index
                m4DIST1.tStart = t  # local t and not account for scr refresh
                m4DIST1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m4DIST1, 'tStartRefresh')  # time at next scr refresh
                # update status
                m4DIST1.status = STARTED
                m4DIST1.setAutoDraw(True)
            
            # if m4DIST1 is active this frame...
            if m4DIST1.status == STARTED:
                # update params
                pass
                # check whether m4DIST1 has been pressed
                if m4DIST1.isClicked:
                    if not m4DIST1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m4DIST1.timesOn.append(m4DIST1.buttonClock.getTime())
                        m4DIST1.timesOff.append(m4DIST1.buttonClock.getTime())
                    elif len(m4DIST1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m4DIST1.timesOff[-1] = m4DIST1.buttonClock.getTime()
                    if not m4DIST1.wasClicked:
                        # end routine when m4DIST1 is clicked
                        continueRoutine = False
                    if not m4DIST1.wasClicked:
                        # run callback code when m4DIST1 is clicked
                        pass
            # take note of whether m4DIST1 was clicked, so that next frame we know if clicks are new
            m4DIST1.wasClicked = m4DIST1.isClicked and m4DIST1.status == STARTED
            # *m4DIST2* updates
            
            # if m4DIST2 is starting this frame...
            if m4DIST2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m4DIST2.frameNStart = frameN  # exact frame index
                m4DIST2.tStart = t  # local t and not account for scr refresh
                m4DIST2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m4DIST2, 'tStartRefresh')  # time at next scr refresh
                # update status
                m4DIST2.status = STARTED
                m4DIST2.setAutoDraw(True)
            
            # if m4DIST2 is active this frame...
            if m4DIST2.status == STARTED:
                # update params
                pass
                # check whether m4DIST2 has been pressed
                if m4DIST2.isClicked:
                    if not m4DIST2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m4DIST2.timesOn.append(m4DIST2.buttonClock.getTime())
                        m4DIST2.timesOff.append(m4DIST2.buttonClock.getTime())
                    elif len(m4DIST2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m4DIST2.timesOff[-1] = m4DIST2.buttonClock.getTime()
                    if not m4DIST2.wasClicked:
                        # end routine when m4DIST2 is clicked
                        continueRoutine = False
                    if not m4DIST2.wasClicked:
                        # run callback code when m4DIST2 is clicked
                        pass
            # take note of whether m4DIST2 was clicked, so that next frame we know if clicks are new
            m4DIST2.wasClicked = m4DIST2.isClicked and m4DIST2.status == STARTED
            # *m4DIST3* updates
            
            # if m4DIST3 is starting this frame...
            if m4DIST3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m4DIST3.frameNStart = frameN  # exact frame index
                m4DIST3.tStart = t  # local t and not account for scr refresh
                m4DIST3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m4DIST3, 'tStartRefresh')  # time at next scr refresh
                # update status
                m4DIST3.status = STARTED
                m4DIST3.setAutoDraw(True)
            
            # if m4DIST3 is active this frame...
            if m4DIST3.status == STARTED:
                # update params
                pass
                # check whether m4DIST3 has been pressed
                if m4DIST3.isClicked:
                    if not m4DIST3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m4DIST3.timesOn.append(m4DIST3.buttonClock.getTime())
                        m4DIST3.timesOff.append(m4DIST3.buttonClock.getTime())
                    elif len(m4DIST3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m4DIST3.timesOff[-1] = m4DIST3.buttonClock.getTime()
                    if not m4DIST3.wasClicked:
                        # end routine when m4DIST3 is clicked
                        continueRoutine = False
                    if not m4DIST3.wasClicked:
                        # run callback code when m4DIST3 is clicked
                        pass
            # take note of whether m4DIST3 was clicked, so that next frame we know if clicks are new
            m4DIST3.wasClicked = m4DIST3.isClicked and m4DIST3.status == STARTED
            # *m4Mouse* updates
            
            # if m4Mouse is starting this frame...
            if m4Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m4Mouse.frameNStart = frameN  # exact frame index
                m4Mouse.tStart = t  # local t and not account for scr refresh
                m4Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m4Mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'm4Mouse.started')
                # update status
                m4Mouse.status = STARTED
                m4Mouse.mouseClock.reset()
                prevButtonState = m4Mouse.getPressed()  # if button is down already this ISN'T a new click
            if m4Mouse.status == STARTED:  # only update if started and not finished!
                buttons = m4Mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = core.getFromNames([m4CON,m4DIST1,m4DIST2,m4DIST3])
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(m4Mouse):
                                gotValidClick = True
                                m4Mouse.clicked_name.append(obj.name)
                        continueRoutine = False  # end routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mini4_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mini4_1" ---
        for thisComponent in mini4_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from m4Code1_2
        if m4Mouse.isPressedIn(m4CON):
            nRepsM4Corr = True
            nRepsM4Incorr = False
            thisExp.addData("mCorr Response",m4CON.text)
        else:
            nRepsM4Corr = False
            nRepsM4Incorr = True
        
        if m4Mouse.isPressedIn(m4DIST1):
            incorrAns4=m4DIST1.text
            incorrPosi4=m4DIST1.pos
            thisExp.addData("mIncorr Repsonse",m4DIST1.text)
        elif m4Mouse.isPressedIn(m4DIST2):
            incorrAns4=m4DIST2.text
            incorrPosi4=m4DIST2.pos
            thisExp.addData("mIncorr Repsonse",m4DIST2.text)
        elif m4Mouse.isPressedIn(m4DIST3):
            incorrAns4=m4DIST3.text
            incorrPosi4=m4DIST3.pos
            thisExp.addData("mIncorr Repsonse",m4DIST3.text)
        # store data for mini4Loop (TrialHandler)
        # the Routine "mini4_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        m4CorrLoop = data.TrialHandler(nReps=nRepsM4Corr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m4CorrLoop')
        thisExp.addLoop(m4CorrLoop)  # add the loop to the experiment
        thisM4CorrLoop = m4CorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM4CorrLoop.rgb)
        if thisM4CorrLoop != None:
            for paramName in thisM4CorrLoop:
                exec('{} = thisM4CorrLoop[paramName]'.format(paramName))
        
        for thisM4CorrLoop in m4CorrLoop:
            currentLoop = m4CorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM4CorrLoop.rgb)
            if thisM4CorrLoop != None:
                for paramName in thisM4CorrLoop:
                    exec('{} = thisM4CorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini4_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m4Code1
            m4Count = m4Count+1
            m4CorrPL.setImage(img)
            m4CorrCON.setPos([m4Posi[0]])
            m4CorrCON.setText(conWord)
            m4Sound1.setSound(audio, secs=2, hamming=True)
            m4Sound1.setVolume(3.0, log=False)
            m4Key1.keys = []
            m4Key1.rt = []
            _m4Key1_allKeys = []
            # keep track of which components have finished
            mini4_2Components = [m4CorrPL, m4CorrCON, m4Sound1, m4Key1, space10]
            for thisComponent in mini4_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini4_2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m4CorrPL* updates
                
                # if m4CorrPL is starting this frame...
                if m4CorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m4CorrPL.frameNStart = frameN  # exact frame index
                    m4CorrPL.tStart = t  # local t and not account for scr refresh
                    m4CorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m4CorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m4CorrPL.status = STARTED
                    m4CorrPL.setAutoDraw(True)
                
                # if m4CorrPL is active this frame...
                if m4CorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m4CorrCON* updates
                
                # if m4CorrCON is starting this frame...
                if m4CorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m4CorrCON.frameNStart = frameN  # exact frame index
                    m4CorrCON.tStart = t  # local t and not account for scr refresh
                    m4CorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m4CorrCON, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'm4CorrCON.started')
                    # update status
                    m4CorrCON.status = STARTED
                    m4CorrCON.setAutoDraw(True)
                
                # if m4CorrCON is active this frame...
                if m4CorrCON.status == STARTED:
                    # update params
                    pass
                # start/stop m4Sound1
                
                # if m4Sound1 is starting this frame...
                if m4Sound1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m4Sound1.frameNStart = frameN  # exact frame index
                    m4Sound1.tStart = t  # local t and not account for scr refresh
                    m4Sound1.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m4Sound1.status = STARTED
                    m4Sound1.play(when=win)  # sync with win flip
                
                # if m4Sound1 is stopping this frame...
                if m4Sound1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m4Sound1.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m4Sound1.tStop = t  # not accounting for scr refresh
                        m4Sound1.frameNStop = frameN  # exact frame index
                        # update status
                        m4Sound1.status = FINISHED
                        m4Sound1.stop()
                
                # *m4Key1* updates
                
                # if m4Key1 is starting this frame...
                if m4Key1.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m4Key1.frameNStart = frameN  # exact frame index
                    m4Key1.tStart = t  # local t and not account for scr refresh
                    m4Key1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m4Key1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m4Key1.status = STARTED
                    # keyboard checking is just starting
                    m4Key1.clock.reset()  # now t=0
                if m4Key1.status == STARTED:
                    theseKeys = m4Key1.getKeys(keyList=['space'], waitRelease=False)
                    _m4Key1_allKeys.extend(theseKeys)
                    if len(_m4Key1_allKeys):
                        m4Key1.keys = _m4Key1_allKeys[-1].name  # just the last key pressed
                        m4Key1.rt = _m4Key1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space10* updates
                
                # if space10 is starting this frame...
                if space10.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space10.frameNStart = frameN  # exact frame index
                    space10.tStart = t  # local t and not account for scr refresh
                    space10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space10, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space10.status = STARTED
                    space10.setAutoDraw(True)
                
                # if space10 is active this frame...
                if space10.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini4_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini4_2" ---
            for thisComponent in mini4_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m4Code1
            if m4Count == 12:
                mini4Loop.finished = True
            m4Sound1.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini4_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM4Corr repeats of 'm4CorrLoop'
        
        
        # set up handler to look after randomisation of conditions etc
        m4IncorrLoop = data.TrialHandler(nReps=nRepsM4Incorr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m4IncorrLoop')
        thisExp.addLoop(m4IncorrLoop)  # add the loop to the experiment
        thisM4IncorrLoop = m4IncorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM4IncorrLoop.rgb)
        if thisM4IncorrLoop != None:
            for paramName in thisM4IncorrLoop:
                exec('{} = thisM4IncorrLoop[paramName]'.format(paramName))
        
        for thisM4IncorrLoop in m4IncorrLoop:
            currentLoop = m4IncorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM4IncorrLoop.rgb)
            if thisM4IncorrLoop != None:
                for paramName in thisM4IncorrLoop:
                    exec('{} = thisM4IncorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini4_3" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m4Code3
            m4Count = m4Count+1
            m4IncorrPL.setImage(img)
            m4IncorrCON.setPos([m4Posi[0]])
            m4IncorrCON.setText(conWord)
            m4IncorrDIST.setPos(incorrPosi4)
            m4IncorrDIST.setText(incorrAns4)
            m4Sound2.setSound(audio, secs=2, hamming=True)
            m4Sound2.setVolume(3.0, log=False)
            m4Key2.keys = []
            m4Key2.rt = []
            _m4Key2_allKeys = []
            # keep track of which components have finished
            mini4_3Components = [m4IncorrPL, m4IncorrCON, m4IncorrDIST, m4Sound2, m4Key2, space11]
            for thisComponent in mini4_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini4_3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m4IncorrPL* updates
                
                # if m4IncorrPL is starting this frame...
                if m4IncorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m4IncorrPL.frameNStart = frameN  # exact frame index
                    m4IncorrPL.tStart = t  # local t and not account for scr refresh
                    m4IncorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m4IncorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m4IncorrPL.status = STARTED
                    m4IncorrPL.setAutoDraw(True)
                
                # if m4IncorrPL is active this frame...
                if m4IncorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m4IncorrCON* updates
                
                # if m4IncorrCON is starting this frame...
                if m4IncorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m4IncorrCON.frameNStart = frameN  # exact frame index
                    m4IncorrCON.tStart = t  # local t and not account for scr refresh
                    m4IncorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m4IncorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m4IncorrCON.status = STARTED
                    m4IncorrCON.setAutoDraw(True)
                
                # if m4IncorrCON is active this frame...
                if m4IncorrCON.status == STARTED:
                    # update params
                    pass
                
                # *m4IncorrDIST* updates
                
                # if m4IncorrDIST is starting this frame...
                if m4IncorrDIST.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m4IncorrDIST.frameNStart = frameN  # exact frame index
                    m4IncorrDIST.tStart = t  # local t and not account for scr refresh
                    m4IncorrDIST.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m4IncorrDIST, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m4IncorrDIST.status = STARTED
                    m4IncorrDIST.setAutoDraw(True)
                
                # if m4IncorrDIST is active this frame...
                if m4IncorrDIST.status == STARTED:
                    # update params
                    pass
                # start/stop m4Sound2
                
                # if m4Sound2 is starting this frame...
                if m4Sound2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m4Sound2.frameNStart = frameN  # exact frame index
                    m4Sound2.tStart = t  # local t and not account for scr refresh
                    m4Sound2.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m4Sound2.status = STARTED
                    m4Sound2.play(when=win)  # sync with win flip
                
                # if m4Sound2 is stopping this frame...
                if m4Sound2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m4Sound2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m4Sound2.tStop = t  # not accounting for scr refresh
                        m4Sound2.frameNStop = frameN  # exact frame index
                        # update status
                        m4Sound2.status = FINISHED
                        m4Sound2.stop()
                
                # *m4Key2* updates
                
                # if m4Key2 is starting this frame...
                if m4Key2.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m4Key2.frameNStart = frameN  # exact frame index
                    m4Key2.tStart = t  # local t and not account for scr refresh
                    m4Key2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m4Key2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m4Key2.status = STARTED
                    # keyboard checking is just starting
                    m4Key2.clock.reset()  # now t=0
                if m4Key2.status == STARTED:
                    theseKeys = m4Key2.getKeys(keyList=['space'], waitRelease=False)
                    _m4Key2_allKeys.extend(theseKeys)
                    if len(_m4Key2_allKeys):
                        m4Key2.keys = _m4Key2_allKeys[-1].name  # just the last key pressed
                        m4Key2.rt = _m4Key2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space11* updates
                
                # if space11 is starting this frame...
                if space11.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space11.frameNStart = frameN  # exact frame index
                    space11.tStart = t  # local t and not account for scr refresh
                    space11.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space11, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space11.status = STARTED
                    space11.setAutoDraw(True)
                
                # if space11 is active this frame...
                if space11.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini4_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini4_3" ---
            for thisComponent in mini4_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m4Code3
            if m4Count==12:
                mini4Loop.finished = True
            m4Sound2.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini4_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM4Incorr repeats of 'm4IncorrLoop'
        
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'mini4Loop'
    
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'img2'


# set up handler to look after randomisation of conditions etc
ortho3 = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='ortho3')
thisExp.addLoop(ortho3)  # add the loop to the experiment
thisOrtho3 = ortho3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOrtho3.rgb)
if thisOrtho3 != None:
    for paramName in thisOrtho3:
        exec('{} = thisOrtho3[paramName]'.format(paramName))

for thisOrtho3 in ortho3:
    currentLoop = ortho3
    # abbreviate parameter names if possible (e.g. rgb = thisOrtho3.rgb)
    if thisOrtho3 != None:
        for paramName in thisOrtho3:
            exec('{} = thisOrtho3[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    exp5Loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("orthostim_" + expInfo['group'] + ".xlsx", selection='8:12'),
        seed=None, name='exp5Loop')
    thisExp.addLoop(exp5Loop)  # add the loop to the experiment
    thisExp5Loop = exp5Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExp5Loop.rgb)
    if thisExp5Loop != None:
        for paramName in thisExp5Loop:
            exec('{} = thisExp5Loop[paramName]'.format(paramName))
    
    for thisExp5Loop in exp5Loop:
        currentLoop = exp5Loop
        # abbreviate parameter names if possible (e.g. rgb = thisExp5Loop.rgb)
        if thisExp5Loop != None:
            for paramName in thisExp5Loop:
                exec('{} = thisExp5Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "exp5_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        e5PL.setText(plWord)
        # keep track of which components have finished
        exp5_1Components = [e5Focal1, e5PL]
        for thisComponent in exp5_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp5_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e5Focal1* updates
            
            # if e5Focal1 is starting this frame...
            if e5Focal1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                e5Focal1.frameNStart = frameN  # exact frame index
                e5Focal1.tStart = t  # local t and not account for scr refresh
                e5Focal1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e5Focal1, 'tStartRefresh')  # time at next scr refresh
                # update status
                e5Focal1.status = STARTED
                e5Focal1.setAutoDraw(True)
            
            # if e5Focal1 is active this frame...
            if e5Focal1.status == STARTED:
                # update params
                pass
            
            # if e5Focal1 is stopping this frame...
            if e5Focal1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e5Focal1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    e5Focal1.tStop = t  # not accounting for scr refresh
                    e5Focal1.frameNStop = frameN  # exact frame index
                    # update status
                    e5Focal1.status = FINISHED
                    e5Focal1.setAutoDraw(False)
            
            # *e5PL* updates
            
            # if e5PL is starting this frame...
            if e5PL.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
                # keep track of start time/frame for later
                e5PL.frameNStart = frameN  # exact frame index
                e5PL.tStart = t  # local t and not account for scr refresh
                e5PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e5PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                e5PL.status = STARTED
                e5PL.setAutoDraw(True)
            
            # if e5PL is active this frame...
            if e5PL.status == STARTED:
                # update params
                pass
            
            # if e5PL is stopping this frame...
            if e5PL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e5PL.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    e5PL.tStop = t  # not accounting for scr refresh
                    e5PL.frameNStop = frameN  # exact frame index
                    # update status
                    e5PL.status = FINISHED
                    e5PL.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp5_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp5_1" ---
        for thisComponent in exp5_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.100000)
        
        # --- Prepare to start Routine "exp5_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from e5Code2
        e5Count = e5Count+1
        e5Con.setText(conWord)
        e5Sound.setSound(audio, hamming=True)
        e5Sound.setVolume(3.0, log=False)
        e5Key.keys = []
        e5Key.rt = []
        _e5Key_allKeys = []
        # keep track of which components have finished
        exp5_2Components = [e5Focal2, e5Con, e5Sound, e5Key, space12]
        for thisComponent in exp5_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp5_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e5Focal2* updates
            
            # if e5Focal2 is starting this frame...
            if e5Focal2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                e5Focal2.frameNStart = frameN  # exact frame index
                e5Focal2.tStart = t  # local t and not account for scr refresh
                e5Focal2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e5Focal2, 'tStartRefresh')  # time at next scr refresh
                # update status
                e5Focal2.status = STARTED
                e5Focal2.setAutoDraw(True)
            
            # if e5Focal2 is active this frame...
            if e5Focal2.status == STARTED:
                # update params
                pass
            
            # if e5Focal2 is stopping this frame...
            if e5Focal2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e5Focal2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    e5Focal2.tStop = t  # not accounting for scr refresh
                    e5Focal2.frameNStop = frameN  # exact frame index
                    # update status
                    e5Focal2.status = FINISHED
                    e5Focal2.setAutoDraw(False)
            
            # *e5Con* updates
            
            # if e5Con is starting this frame...
            if e5Con.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e5Con.frameNStart = frameN  # exact frame index
                e5Con.tStart = t  # local t and not account for scr refresh
                e5Con.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e5Con, 'tStartRefresh')  # time at next scr refresh
                # update status
                e5Con.status = STARTED
                e5Con.setAutoDraw(True)
            
            # if e5Con is active this frame...
            if e5Con.status == STARTED:
                # update params
                pass
            # start/stop e5Sound
            
            # if e5Sound is starting this frame...
            if e5Sound.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e5Sound.frameNStart = frameN  # exact frame index
                e5Sound.tStart = t  # local t and not account for scr refresh
                e5Sound.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                e5Sound.status = STARTED
                e5Sound.play(when=win)  # sync with win flip
            
            # *e5Key* updates
            
            # if e5Key is starting this frame...
            if e5Key.status == NOT_STARTED and t >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                e5Key.frameNStart = frameN  # exact frame index
                e5Key.tStart = t  # local t and not account for scr refresh
                e5Key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e5Key, 'tStartRefresh')  # time at next scr refresh
                # update status
                e5Key.status = STARTED
                # keyboard checking is just starting
                e5Key.clock.reset()  # now t=0
            if e5Key.status == STARTED:
                theseKeys = e5Key.getKeys(keyList=['space'], waitRelease=False)
                _e5Key_allKeys.extend(theseKeys)
                if len(_e5Key_allKeys):
                    e5Key.keys = _e5Key_allKeys[-1].name  # just the last key pressed
                    e5Key.rt = _e5Key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *space12* updates
            
            # if space12 is starting this frame...
            if space12.status == NOT_STARTED and tThisFlip >= 3.2-frameTolerance:
                # keep track of start time/frame for later
                space12.frameNStart = frameN  # exact frame index
                space12.tStart = t  # local t and not account for scr refresh
                space12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space12, 'tStartRefresh')  # time at next scr refresh
                # update status
                space12.status = STARTED
                space12.setAutoDraw(True)
            
            # if space12 is active this frame...
            if space12.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp5_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp5_2" ---
        for thisComponent in exp5_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from e5Code2
        if e5Count == 4:
            exp5Loop.finished = True
        else:
            pass
        e5Sound.stop()  # ensure sound has stopped at end of routine
        # the Routine "exp5_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'exp5Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    mini5Loop = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("orthostim_" + expInfo['group'] + ".xlsx", selection='8:12'),
        seed=None, name='mini5Loop')
    thisExp.addLoop(mini5Loop)  # add the loop to the experiment
    thisMini5Loop = mini5Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMini5Loop.rgb)
    if thisMini5Loop != None:
        for paramName in thisMini5Loop:
            exec('{} = thisMini5Loop[paramName]'.format(paramName))
    
    for thisMini5Loop in mini5Loop:
        currentLoop = mini5Loop
        # abbreviate parameter names if possible (e.g. rgb = thisMini5Loop.rgb)
        if thisMini5Loop != None:
            for paramName in thisMini5Loop:
                exec('{} = thisMini5Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mini5_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from m5Code1
        random.shuffle(m5Posi)
        m5PL.setText(plWord)
        m5CON.setPos([m5Posi[0]])
        m5CON.setText(conWord)
        # reset m5CON to account for continued clicks & clear times on/off
        m5CON.reset()
        m5DIST1.setPos([m5Posi[1]])
        m5DIST1.setText(incorr1)
        # reset m5DIST1 to account for continued clicks & clear times on/off
        m5DIST1.reset()
        m5DIST2.setPos([m5Posi[2]])
        m5DIST2.setText(incorr2)
        # reset m5DIST2 to account for continued clicks & clear times on/off
        m5DIST2.reset()
        m5DIST3.setPos([m5Posi[3]])
        m5DIST3.setText(incorr3)
        # reset m5DIST3 to account for continued clicks & clear times on/off
        m5DIST3.reset()
        # setup some python lists for storing info about the m5Mouse
        m5Mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        mini5_1Components = [m5PL, m5CON, m5DIST1, m5DIST2, m5DIST3, m5Mouse]
        for thisComponent in mini5_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mini5_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *m5PL* updates
            
            # if m5PL is starting this frame...
            if m5PL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m5PL.frameNStart = frameN  # exact frame index
                m5PL.tStart = t  # local t and not account for scr refresh
                m5PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m5PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                m5PL.status = STARTED
                m5PL.setAutoDraw(True)
            
            # if m5PL is active this frame...
            if m5PL.status == STARTED:
                # update params
                pass
            # *m5CON* updates
            
            # if m5CON is starting this frame...
            if m5CON.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m5CON.frameNStart = frameN  # exact frame index
                m5CON.tStart = t  # local t and not account for scr refresh
                m5CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m5CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                m5CON.status = STARTED
                m5CON.setAutoDraw(True)
            
            # if m5CON is active this frame...
            if m5CON.status == STARTED:
                # update params
                pass
                # check whether m5CON has been pressed
                if m5CON.isClicked:
                    if not m5CON.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m5CON.timesOn.append(m5CON.buttonClock.getTime())
                        m5CON.timesOff.append(m5CON.buttonClock.getTime())
                    elif len(m5CON.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m5CON.timesOff[-1] = m5CON.buttonClock.getTime()
                    if not m5CON.wasClicked:
                        # end routine when m5CON is clicked
                        continueRoutine = False
                    if not m5CON.wasClicked:
                        # run callback code when m5CON is clicked
                        pass
            # take note of whether m5CON was clicked, so that next frame we know if clicks are new
            m5CON.wasClicked = m5CON.isClicked and m5CON.status == STARTED
            # *m5DIST1* updates
            
            # if m5DIST1 is starting this frame...
            if m5DIST1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m5DIST1.frameNStart = frameN  # exact frame index
                m5DIST1.tStart = t  # local t and not account for scr refresh
                m5DIST1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m5DIST1, 'tStartRefresh')  # time at next scr refresh
                # update status
                m5DIST1.status = STARTED
                m5DIST1.setAutoDraw(True)
            
            # if m5DIST1 is active this frame...
            if m5DIST1.status == STARTED:
                # update params
                pass
                # check whether m5DIST1 has been pressed
                if m5DIST1.isClicked:
                    if not m5DIST1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m5DIST1.timesOn.append(m5DIST1.buttonClock.getTime())
                        m5DIST1.timesOff.append(m5DIST1.buttonClock.getTime())
                    elif len(m5DIST1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m5DIST1.timesOff[-1] = m5DIST1.buttonClock.getTime()
                    if not m5DIST1.wasClicked:
                        # end routine when m5DIST1 is clicked
                        continueRoutine = False
                    if not m5DIST1.wasClicked:
                        # run callback code when m5DIST1 is clicked
                        pass
            # take note of whether m5DIST1 was clicked, so that next frame we know if clicks are new
            m5DIST1.wasClicked = m5DIST1.isClicked and m5DIST1.status == STARTED
            # *m5DIST2* updates
            
            # if m5DIST2 is starting this frame...
            if m5DIST2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m5DIST2.frameNStart = frameN  # exact frame index
                m5DIST2.tStart = t  # local t and not account for scr refresh
                m5DIST2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m5DIST2, 'tStartRefresh')  # time at next scr refresh
                # update status
                m5DIST2.status = STARTED
                m5DIST2.setAutoDraw(True)
            
            # if m5DIST2 is active this frame...
            if m5DIST2.status == STARTED:
                # update params
                pass
                # check whether m5DIST2 has been pressed
                if m5DIST2.isClicked:
                    if not m5DIST2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m5DIST2.timesOn.append(m5DIST2.buttonClock.getTime())
                        m5DIST2.timesOff.append(m5DIST2.buttonClock.getTime())
                    elif len(m5DIST2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m5DIST2.timesOff[-1] = m5DIST2.buttonClock.getTime()
                    if not m5DIST2.wasClicked:
                        # end routine when m5DIST2 is clicked
                        continueRoutine = False
                    if not m5DIST2.wasClicked:
                        # run callback code when m5DIST2 is clicked
                        pass
            # take note of whether m5DIST2 was clicked, so that next frame we know if clicks are new
            m5DIST2.wasClicked = m5DIST2.isClicked and m5DIST2.status == STARTED
            # *m5DIST3* updates
            
            # if m5DIST3 is starting this frame...
            if m5DIST3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m5DIST3.frameNStart = frameN  # exact frame index
                m5DIST3.tStart = t  # local t and not account for scr refresh
                m5DIST3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m5DIST3, 'tStartRefresh')  # time at next scr refresh
                # update status
                m5DIST3.status = STARTED
                m5DIST3.setAutoDraw(True)
            
            # if m5DIST3 is active this frame...
            if m5DIST3.status == STARTED:
                # update params
                pass
                # check whether m5DIST3 has been pressed
                if m5DIST3.isClicked:
                    if not m5DIST3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m5DIST3.timesOn.append(m5DIST3.buttonClock.getTime())
                        m5DIST3.timesOff.append(m5DIST3.buttonClock.getTime())
                    elif len(m5DIST3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m5DIST3.timesOff[-1] = m5DIST3.buttonClock.getTime()
                    if not m5DIST3.wasClicked:
                        # end routine when m5DIST3 is clicked
                        continueRoutine = False
                    if not m5DIST3.wasClicked:
                        # run callback code when m5DIST3 is clicked
                        pass
            # take note of whether m5DIST3 was clicked, so that next frame we know if clicks are new
            m5DIST3.wasClicked = m5DIST3.isClicked and m5DIST3.status == STARTED
            # *m5Mouse* updates
            
            # if m5Mouse is starting this frame...
            if m5Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m5Mouse.frameNStart = frameN  # exact frame index
                m5Mouse.tStart = t  # local t and not account for scr refresh
                m5Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m5Mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'm5Mouse.started')
                # update status
                m5Mouse.status = STARTED
                m5Mouse.mouseClock.reset()
                prevButtonState = m5Mouse.getPressed()  # if button is down already this ISN'T a new click
            if m5Mouse.status == STARTED:  # only update if started and not finished!
                buttons = m5Mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = core.getFromNames([m3CON,m3DIST1,m3DIST2,m3DIST3])
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(m5Mouse):
                                gotValidClick = True
                                m5Mouse.clicked_name.append(obj.name)
                        continueRoutine = False  # end routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mini5_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mini5_1" ---
        for thisComponent in mini5_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from m5Code1
        if m5Mouse.isPressedIn(m5CON):
            nRepsM5Corr = True
            nRepsM5Incorr = False
            thisExp.addData("mCorr Response",m5CON.text)
        else:
            nRepsM5Corr = False
            nRepsM5Incorr = True
        
        if m5Mouse.isPressedIn(m5DIST1):
            incorrAns5=m5DIST1.text
            incorrPosi5=m5DIST1.pos
            thisExp.addData("mIncorr Repsonse",m5DIST1.text)
        elif m5Mouse.isPressedIn(m5DIST2):
            incorrAns5=m5DIST2.text
            incorrPosi5=m5DIST2.pos
            thisExp.addData("mIncorr Repsonse",m5DIST2.text)
        elif m5Mouse.isPressedIn(m5DIST3):
            incorrAns5=m5DIST3.text
            incorrPosi5=m5DIST3.pos
            thisExp.addData("mIncorr Repsonse",m5DIST3.text)
        # store data for mini5Loop (TrialHandler)
        # the Routine "mini5_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        m5CorrLoop = data.TrialHandler(nReps=nRepsM5Corr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m5CorrLoop')
        thisExp.addLoop(m5CorrLoop)  # add the loop to the experiment
        thisM5CorrLoop = m5CorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM5CorrLoop.rgb)
        if thisM5CorrLoop != None:
            for paramName in thisM5CorrLoop:
                exec('{} = thisM5CorrLoop[paramName]'.format(paramName))
        
        for thisM5CorrLoop in m5CorrLoop:
            currentLoop = m5CorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM5CorrLoop.rgb)
            if thisM5CorrLoop != None:
                for paramName in thisM5CorrLoop:
                    exec('{} = thisM5CorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini5_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m5Code2
            m5Count = m5Count+1
            m5CorrPL.setText(plWord)
            m5CorrCON.setPos([m5Posi[0]])
            m5CorrCON.setText(conWord)
            m5Sound1.setSound(audio, secs=2, hamming=True)
            m5Sound1.setVolume(3.0, log=False)
            m5Key1.keys = []
            m5Key1.rt = []
            _m5Key1_allKeys = []
            # keep track of which components have finished
            mini5_2Components = [m5CorrPL, m5CorrCON, m5Sound1, m5Key1, space13]
            for thisComponent in mini5_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini5_2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m5CorrPL* updates
                
                # if m5CorrPL is starting this frame...
                if m5CorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m5CorrPL.frameNStart = frameN  # exact frame index
                    m5CorrPL.tStart = t  # local t and not account for scr refresh
                    m5CorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m5CorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m5CorrPL.status = STARTED
                    m5CorrPL.setAutoDraw(True)
                
                # if m5CorrPL is active this frame...
                if m5CorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m5CorrCON* updates
                
                # if m5CorrCON is starting this frame...
                if m5CorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m5CorrCON.frameNStart = frameN  # exact frame index
                    m5CorrCON.tStart = t  # local t and not account for scr refresh
                    m5CorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m5CorrCON, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'm5CorrCON.started')
                    # update status
                    m5CorrCON.status = STARTED
                    m5CorrCON.setAutoDraw(True)
                
                # if m5CorrCON is active this frame...
                if m5CorrCON.status == STARTED:
                    # update params
                    pass
                # start/stop m5Sound1
                
                # if m5Sound1 is starting this frame...
                if m5Sound1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m5Sound1.frameNStart = frameN  # exact frame index
                    m5Sound1.tStart = t  # local t and not account for scr refresh
                    m5Sound1.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m5Sound1.status = STARTED
                    m5Sound1.play(when=win)  # sync with win flip
                
                # if m5Sound1 is stopping this frame...
                if m5Sound1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m5Sound1.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m5Sound1.tStop = t  # not accounting for scr refresh
                        m5Sound1.frameNStop = frameN  # exact frame index
                        # update status
                        m5Sound1.status = FINISHED
                        m5Sound1.stop()
                
                # *m5Key1* updates
                
                # if m5Key1 is starting this frame...
                if m5Key1.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m5Key1.frameNStart = frameN  # exact frame index
                    m5Key1.tStart = t  # local t and not account for scr refresh
                    m5Key1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m5Key1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m5Key1.status = STARTED
                    # keyboard checking is just starting
                    m5Key1.clock.reset()  # now t=0
                if m5Key1.status == STARTED:
                    theseKeys = m5Key1.getKeys(keyList=['space'], waitRelease=False)
                    _m5Key1_allKeys.extend(theseKeys)
                    if len(_m5Key1_allKeys):
                        m5Key1.keys = _m5Key1_allKeys[-1].name  # just the last key pressed
                        m5Key1.rt = _m5Key1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space13* updates
                
                # if space13 is starting this frame...
                if space13.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space13.frameNStart = frameN  # exact frame index
                    space13.tStart = t  # local t and not account for scr refresh
                    space13.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space13, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space13.status = STARTED
                    space13.setAutoDraw(True)
                
                # if space13 is active this frame...
                if space13.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini5_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini5_2" ---
            for thisComponent in mini5_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m5Code2
            if m5Count == 12:
                mini5Loop.finished = True
            m5Sound1.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini5_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM5Corr repeats of 'm5CorrLoop'
        
        
        # set up handler to look after randomisation of conditions etc
        m5IncorrLoop = data.TrialHandler(nReps=nRepsM5Incorr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m5IncorrLoop')
        thisExp.addLoop(m5IncorrLoop)  # add the loop to the experiment
        thisM5IncorrLoop = m5IncorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM5IncorrLoop.rgb)
        if thisM5IncorrLoop != None:
            for paramName in thisM5IncorrLoop:
                exec('{} = thisM5IncorrLoop[paramName]'.format(paramName))
        
        for thisM5IncorrLoop in m5IncorrLoop:
            currentLoop = m5IncorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM5IncorrLoop.rgb)
            if thisM5IncorrLoop != None:
                for paramName in thisM5IncorrLoop:
                    exec('{} = thisM5IncorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini5_3" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m5Code3
            m5Count = m5Count+1
            m5IncorrPL.setText(plWord)
            m5IncorrCON.setPos([m5Posi[0]])
            m5IncorrCON.setText(conWord)
            m5IncorrDIST.setPos(incorrPosi5)
            m5IncorrDIST.setText(incorrAns5)
            m5Sound2.setSound(audio, secs=2, hamming=True)
            m5Sound2.setVolume(3.0, log=False)
            m5Key2.keys = []
            m5Key2.rt = []
            _m5Key2_allKeys = []
            # keep track of which components have finished
            mini5_3Components = [m5IncorrPL, m5IncorrCON, m5IncorrDIST, m5Sound2, m5Key2, space14]
            for thisComponent in mini5_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini5_3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m5IncorrPL* updates
                
                # if m5IncorrPL is starting this frame...
                if m5IncorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m5IncorrPL.frameNStart = frameN  # exact frame index
                    m5IncorrPL.tStart = t  # local t and not account for scr refresh
                    m5IncorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m5IncorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m5IncorrPL.status = STARTED
                    m5IncorrPL.setAutoDraw(True)
                
                # if m5IncorrPL is active this frame...
                if m5IncorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m5IncorrCON* updates
                
                # if m5IncorrCON is starting this frame...
                if m5IncorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m5IncorrCON.frameNStart = frameN  # exact frame index
                    m5IncorrCON.tStart = t  # local t and not account for scr refresh
                    m5IncorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m5IncorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m5IncorrCON.status = STARTED
                    m5IncorrCON.setAutoDraw(True)
                
                # if m5IncorrCON is active this frame...
                if m5IncorrCON.status == STARTED:
                    # update params
                    pass
                
                # *m5IncorrDIST* updates
                
                # if m5IncorrDIST is starting this frame...
                if m5IncorrDIST.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m5IncorrDIST.frameNStart = frameN  # exact frame index
                    m5IncorrDIST.tStart = t  # local t and not account for scr refresh
                    m5IncorrDIST.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m5IncorrDIST, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m5IncorrDIST.status = STARTED
                    m5IncorrDIST.setAutoDraw(True)
                
                # if m5IncorrDIST is active this frame...
                if m5IncorrDIST.status == STARTED:
                    # update params
                    pass
                # start/stop m5Sound2
                
                # if m5Sound2 is starting this frame...
                if m5Sound2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m5Sound2.frameNStart = frameN  # exact frame index
                    m5Sound2.tStart = t  # local t and not account for scr refresh
                    m5Sound2.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m5Sound2.status = STARTED
                    m5Sound2.play(when=win)  # sync with win flip
                
                # if m5Sound2 is stopping this frame...
                if m5Sound2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m5Sound2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m5Sound2.tStop = t  # not accounting for scr refresh
                        m5Sound2.frameNStop = frameN  # exact frame index
                        # update status
                        m5Sound2.status = FINISHED
                        m5Sound2.stop()
                
                # *m5Key2* updates
                
                # if m5Key2 is starting this frame...
                if m5Key2.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m5Key2.frameNStart = frameN  # exact frame index
                    m5Key2.tStart = t  # local t and not account for scr refresh
                    m5Key2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m5Key2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m5Key2.status = STARTED
                    # keyboard checking is just starting
                    m5Key2.clock.reset()  # now t=0
                if m5Key2.status == STARTED:
                    theseKeys = m5Key2.getKeys(keyList=['space'], waitRelease=False)
                    _m5Key2_allKeys.extend(theseKeys)
                    if len(_m5Key2_allKeys):
                        m5Key2.keys = _m5Key2_allKeys[-1].name  # just the last key pressed
                        m5Key2.rt = _m5Key2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space14* updates
                
                # if space14 is starting this frame...
                if space14.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space14.frameNStart = frameN  # exact frame index
                    space14.tStart = t  # local t and not account for scr refresh
                    space14.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space14, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space14.status = STARTED
                    space14.setAutoDraw(True)
                
                # if space14 is active this frame...
                if space14.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini5_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini5_3" ---
            for thisComponent in mini5_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m5Code3
            if m5Count==12:
                mini5Loop.finished = True
            m5Sound2.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini5_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM5Incorr repeats of 'm5IncorrLoop'
        
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'mini5Loop'
    
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'ortho3'


# set up handler to look after randomisation of conditions etc
img3 = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='img3')
thisExp.addLoop(img3)  # add the loop to the experiment
thisImg3 = img3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisImg3.rgb)
if thisImg3 != None:
    for paramName in thisImg3:
        exec('{} = thisImg3[paramName]'.format(paramName))

for thisImg3 in img3:
    currentLoop = img3
    # abbreviate parameter names if possible (e.g. rgb = thisImg3.rgb)
    if thisImg3 != None:
        for paramName in thisImg3:
            exec('{} = thisImg3[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    exp6Loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("imgstim_"+expInfo['group']+".xlsx", selection='8:12'),
        seed=None, name='exp6Loop')
    thisExp.addLoop(exp6Loop)  # add the loop to the experiment
    thisExp6Loop = exp6Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExp6Loop.rgb)
    if thisExp6Loop != None:
        for paramName in thisExp6Loop:
            exec('{} = thisExp6Loop[paramName]'.format(paramName))
    
    for thisExp6Loop in exp6Loop:
        currentLoop = exp6Loop
        # abbreviate parameter names if possible (e.g. rgb = thisExp6Loop.rgb)
        if thisExp6Loop != None:
            for paramName in thisExp6Loop:
                exec('{} = thisExp6Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "exp6_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        e6PL.setImage(img)
        # keep track of which components have finished
        exp6_1Components = [e6Focal1, e6PL]
        for thisComponent in exp6_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp6_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e6Focal1* updates
            
            # if e6Focal1 is starting this frame...
            if e6Focal1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                e6Focal1.frameNStart = frameN  # exact frame index
                e6Focal1.tStart = t  # local t and not account for scr refresh
                e6Focal1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e6Focal1, 'tStartRefresh')  # time at next scr refresh
                # update status
                e6Focal1.status = STARTED
                e6Focal1.setAutoDraw(True)
            
            # if e6Focal1 is active this frame...
            if e6Focal1.status == STARTED:
                # update params
                pass
            
            # if e6Focal1 is stopping this frame...
            if e6Focal1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e6Focal1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    e6Focal1.tStop = t  # not accounting for scr refresh
                    e6Focal1.frameNStop = frameN  # exact frame index
                    # update status
                    e6Focal1.status = FINISHED
                    e6Focal1.setAutoDraw(False)
            
            # *e6PL* updates
            
            # if e6PL is starting this frame...
            if e6PL.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
                # keep track of start time/frame for later
                e6PL.frameNStart = frameN  # exact frame index
                e6PL.tStart = t  # local t and not account for scr refresh
                e6PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e6PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                e6PL.status = STARTED
                e6PL.setAutoDraw(True)
            
            # if e6PL is active this frame...
            if e6PL.status == STARTED:
                # update params
                pass
            
            # if e6PL is stopping this frame...
            if e6PL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e6PL.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    e6PL.tStop = t  # not accounting for scr refresh
                    e6PL.frameNStop = frameN  # exact frame index
                    # update status
                    e6PL.status = FINISHED
                    e6PL.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp6_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp6_1" ---
        for thisComponent in exp6_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.100000)
        
        # --- Prepare to start Routine "exp6_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from e6Code2
        e6Count = e6Count+1
        e6CON.setText(conWord)
        e6Sound.setSound(audio, hamming=True)
        e6Sound.setVolume(3.0, log=False)
        e6Key.keys = []
        e6Key.rt = []
        _e6Key_allKeys = []
        # keep track of which components have finished
        exp6_2Components = [e6Focal2, e6CON, e6Sound, e6Key, space15]
        for thisComponent in exp6_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp6_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e6Focal2* updates
            
            # if e6Focal2 is starting this frame...
            if e6Focal2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                e6Focal2.frameNStart = frameN  # exact frame index
                e6Focal2.tStart = t  # local t and not account for scr refresh
                e6Focal2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e6Focal2, 'tStartRefresh')  # time at next scr refresh
                # update status
                e6Focal2.status = STARTED
                e6Focal2.setAutoDraw(True)
            
            # if e6Focal2 is active this frame...
            if e6Focal2.status == STARTED:
                # update params
                pass
            
            # if e6Focal2 is stopping this frame...
            if e6Focal2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e6Focal2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    e6Focal2.tStop = t  # not accounting for scr refresh
                    e6Focal2.frameNStop = frameN  # exact frame index
                    # update status
                    e6Focal2.status = FINISHED
                    e6Focal2.setAutoDraw(False)
            
            # *e6CON* updates
            
            # if e6CON is starting this frame...
            if e6CON.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e6CON.frameNStart = frameN  # exact frame index
                e6CON.tStart = t  # local t and not account for scr refresh
                e6CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e6CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                e6CON.status = STARTED
                e6CON.setAutoDraw(True)
            
            # if e6CON is active this frame...
            if e6CON.status == STARTED:
                # update params
                pass
            # start/stop e6Sound
            
            # if e6Sound is starting this frame...
            if e6Sound.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e6Sound.frameNStart = frameN  # exact frame index
                e6Sound.tStart = t  # local t and not account for scr refresh
                e6Sound.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                e6Sound.status = STARTED
                e6Sound.play(when=win)  # sync with win flip
            
            # *e6Key* updates
            
            # if e6Key is starting this frame...
            if e6Key.status == NOT_STARTED and t >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                e6Key.frameNStart = frameN  # exact frame index
                e6Key.tStart = t  # local t and not account for scr refresh
                e6Key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e6Key, 'tStartRefresh')  # time at next scr refresh
                # update status
                e6Key.status = STARTED
                # keyboard checking is just starting
                e6Key.clock.reset()  # now t=0
            if e6Key.status == STARTED:
                theseKeys = e6Key.getKeys(keyList=['space'], waitRelease=False)
                _e6Key_allKeys.extend(theseKeys)
                if len(_e6Key_allKeys):
                    e6Key.keys = _e6Key_allKeys[-1].name  # just the last key pressed
                    e6Key.rt = _e6Key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *space15* updates
            
            # if space15 is starting this frame...
            if space15.status == NOT_STARTED and tThisFlip >= 3.2-frameTolerance:
                # keep track of start time/frame for later
                space15.frameNStart = frameN  # exact frame index
                space15.tStart = t  # local t and not account for scr refresh
                space15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space15, 'tStartRefresh')  # time at next scr refresh
                # update status
                space15.status = STARTED
                space15.setAutoDraw(True)
            
            # if space15 is active this frame...
            if space15.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp6_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp6_2" ---
        for thisComponent in exp6_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from e6Code2
        if e6Count ==4:
            exp6Loop.finished = True
        else:
            pass
        e6Sound.stop()  # ensure sound has stopped at end of routine
        # the Routine "exp6_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'exp6Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    mini6Loop = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("imgstim_"+expInfo['group']+".xlsx", selection='8:12'),
        seed=None, name='mini6Loop')
    thisExp.addLoop(mini6Loop)  # add the loop to the experiment
    thisMini6Loop = mini6Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMini6Loop.rgb)
    if thisMini6Loop != None:
        for paramName in thisMini6Loop:
            exec('{} = thisMini6Loop[paramName]'.format(paramName))
    
    for thisMini6Loop in mini6Loop:
        currentLoop = mini6Loop
        # abbreviate parameter names if possible (e.g. rgb = thisMini6Loop.rgb)
        if thisMini6Loop != None:
            for paramName in thisMini6Loop:
                exec('{} = thisMini6Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mini6_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from m6Code1
        random.shuffle(m6Posi)
        m6PL.setImage(img)
        m6CON.setPos([m6Posi[0]])
        m6CON.setText(conWord)
        # reset m6CON to account for continued clicks & clear times on/off
        m6CON.reset()
        m6DIST1.setPos([m6Posi[1]])
        m6DIST1.setText(incorr1)
        # reset m6DIST1 to account for continued clicks & clear times on/off
        m6DIST1.reset()
        m6DIST2.setPos([m6Posi[2]])
        m6DIST2.setText(incorr2)
        # reset m6DIST2 to account for continued clicks & clear times on/off
        m6DIST2.reset()
        m6DIST3.setPos([m6Posi[3]])
        m6DIST3.setText(incorr3)
        # reset m6DIST3 to account for continued clicks & clear times on/off
        m6DIST3.reset()
        # setup some python lists for storing info about the m6Mouse
        m6Mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        mini6_1Components = [m6PL, m6CON, m6DIST1, m6DIST2, m6DIST3, m6Mouse]
        for thisComponent in mini6_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mini6_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *m6PL* updates
            
            # if m6PL is starting this frame...
            if m6PL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m6PL.frameNStart = frameN  # exact frame index
                m6PL.tStart = t  # local t and not account for scr refresh
                m6PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m6PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                m6PL.status = STARTED
                m6PL.setAutoDraw(True)
            
            # if m6PL is active this frame...
            if m6PL.status == STARTED:
                # update params
                pass
            # *m6CON* updates
            
            # if m6CON is starting this frame...
            if m6CON.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m6CON.frameNStart = frameN  # exact frame index
                m6CON.tStart = t  # local t and not account for scr refresh
                m6CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m6CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                m6CON.status = STARTED
                m6CON.setAutoDraw(True)
            
            # if m6CON is active this frame...
            if m6CON.status == STARTED:
                # update params
                pass
                # check whether m6CON has been pressed
                if m6CON.isClicked:
                    if not m6CON.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m6CON.timesOn.append(m6CON.buttonClock.getTime())
                        m6CON.timesOff.append(m6CON.buttonClock.getTime())
                    elif len(m6CON.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m6CON.timesOff[-1] = m6CON.buttonClock.getTime()
                    if not m6CON.wasClicked:
                        # end routine when m6CON is clicked
                        continueRoutine = False
                    if not m6CON.wasClicked:
                        # run callback code when m6CON is clicked
                        pass
            # take note of whether m6CON was clicked, so that next frame we know if clicks are new
            m6CON.wasClicked = m6CON.isClicked and m6CON.status == STARTED
            # *m6DIST1* updates
            
            # if m6DIST1 is starting this frame...
            if m6DIST1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m6DIST1.frameNStart = frameN  # exact frame index
                m6DIST1.tStart = t  # local t and not account for scr refresh
                m6DIST1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m6DIST1, 'tStartRefresh')  # time at next scr refresh
                # update status
                m6DIST1.status = STARTED
                m6DIST1.setAutoDraw(True)
            
            # if m6DIST1 is active this frame...
            if m6DIST1.status == STARTED:
                # update params
                pass
                # check whether m6DIST1 has been pressed
                if m6DIST1.isClicked:
                    if not m6DIST1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m6DIST1.timesOn.append(m6DIST1.buttonClock.getTime())
                        m6DIST1.timesOff.append(m6DIST1.buttonClock.getTime())
                    elif len(m6DIST1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m6DIST1.timesOff[-1] = m6DIST1.buttonClock.getTime()
                    if not m6DIST1.wasClicked:
                        # end routine when m6DIST1 is clicked
                        continueRoutine = False
                    if not m6DIST1.wasClicked:
                        # run callback code when m6DIST1 is clicked
                        pass
            # take note of whether m6DIST1 was clicked, so that next frame we know if clicks are new
            m6DIST1.wasClicked = m6DIST1.isClicked and m6DIST1.status == STARTED
            # *m6DIST2* updates
            
            # if m6DIST2 is starting this frame...
            if m6DIST2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m6DIST2.frameNStart = frameN  # exact frame index
                m6DIST2.tStart = t  # local t and not account for scr refresh
                m6DIST2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m6DIST2, 'tStartRefresh')  # time at next scr refresh
                # update status
                m6DIST2.status = STARTED
                m6DIST2.setAutoDraw(True)
            
            # if m6DIST2 is active this frame...
            if m6DIST2.status == STARTED:
                # update params
                pass
                # check whether m6DIST2 has been pressed
                if m6DIST2.isClicked:
                    if not m6DIST2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m6DIST2.timesOn.append(m6DIST2.buttonClock.getTime())
                        m6DIST2.timesOff.append(m6DIST2.buttonClock.getTime())
                    elif len(m6DIST2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m6DIST2.timesOff[-1] = m6DIST2.buttonClock.getTime()
                    if not m6DIST2.wasClicked:
                        # end routine when m6DIST2 is clicked
                        continueRoutine = False
                    if not m6DIST2.wasClicked:
                        # run callback code when m6DIST2 is clicked
                        pass
            # take note of whether m6DIST2 was clicked, so that next frame we know if clicks are new
            m6DIST2.wasClicked = m6DIST2.isClicked and m6DIST2.status == STARTED
            # *m6DIST3* updates
            
            # if m6DIST3 is starting this frame...
            if m6DIST3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m6DIST3.frameNStart = frameN  # exact frame index
                m6DIST3.tStart = t  # local t and not account for scr refresh
                m6DIST3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m6DIST3, 'tStartRefresh')  # time at next scr refresh
                # update status
                m6DIST3.status = STARTED
                m6DIST3.setAutoDraw(True)
            
            # if m6DIST3 is active this frame...
            if m6DIST3.status == STARTED:
                # update params
                pass
                # check whether m6DIST3 has been pressed
                if m6DIST3.isClicked:
                    if not m6DIST3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m6DIST3.timesOn.append(m6DIST3.buttonClock.getTime())
                        m6DIST3.timesOff.append(m6DIST3.buttonClock.getTime())
                    elif len(m6DIST3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m6DIST3.timesOff[-1] = m6DIST3.buttonClock.getTime()
                    if not m6DIST3.wasClicked:
                        # end routine when m6DIST3 is clicked
                        continueRoutine = False
                    if not m6DIST3.wasClicked:
                        # run callback code when m6DIST3 is clicked
                        pass
            # take note of whether m6DIST3 was clicked, so that next frame we know if clicks are new
            m6DIST3.wasClicked = m6DIST3.isClicked and m6DIST3.status == STARTED
            # *m6Mouse* updates
            
            # if m6Mouse is starting this frame...
            if m6Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m6Mouse.frameNStart = frameN  # exact frame index
                m6Mouse.tStart = t  # local t and not account for scr refresh
                m6Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m6Mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'm6Mouse.started')
                # update status
                m6Mouse.status = STARTED
                m6Mouse.mouseClock.reset()
                prevButtonState = m6Mouse.getPressed()  # if button is down already this ISN'T a new click
            if m6Mouse.status == STARTED:  # only update if started and not finished!
                buttons = m6Mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = core.getFromNames([m6CON,m6DIST1,m6DIST2,m6DIST3])
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(m6Mouse):
                                gotValidClick = True
                                m6Mouse.clicked_name.append(obj.name)
                        continueRoutine = False  # end routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mini6_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mini6_1" ---
        for thisComponent in mini6_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from m6Code1
        if m6Mouse.isPressedIn(m6CON):
            nRepsM6Corr = True
            nRepsM6Incorr = False
            thisExp.addData("mCorr Response",m6CON.text)
        else:
            nRepsM6Corr = False
            nRepsM6Incorr = True
        
        if m6Mouse.isPressedIn(m6DIST1):
            incorrAns6=m6DIST1.text
            incorrPosi6=m6DIST1.pos
            thisExp.addData("mIncorr Repsonse",m6DIST1.text)
        elif m6Mouse.isPressedIn(m6DIST2):
            incorrAns6=m6DIST2.text
            incorrPosi6=m6DIST2.pos
            thisExp.addData("mIncorr Repsonse",m6DIST2.text)
        elif m6Mouse.isPressedIn(m6DIST3):
            incorrAns6=m6DIST3.text
            incorrPosi6=m6DIST3.pos
            thisExp.addData("mIncorr Repsonse",m6DIST3.text)
        # store data for mini6Loop (TrialHandler)
        # the Routine "mini6_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        m6CorrLoop = data.TrialHandler(nReps=nRepsM6Corr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m6CorrLoop')
        thisExp.addLoop(m6CorrLoop)  # add the loop to the experiment
        thisM6CorrLoop = m6CorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM6CorrLoop.rgb)
        if thisM6CorrLoop != None:
            for paramName in thisM6CorrLoop:
                exec('{} = thisM6CorrLoop[paramName]'.format(paramName))
        
        for thisM6CorrLoop in m6CorrLoop:
            currentLoop = m6CorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM6CorrLoop.rgb)
            if thisM6CorrLoop != None:
                for paramName in thisM6CorrLoop:
                    exec('{} = thisM6CorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini6_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m6Code2
            m6Count = m6Count+1
            m6CorrPL.setImage(img)
            m6CorrCON.setPos([m6Posi[0]])
            m6CorrCON.setText(conWord)
            m6Sound1.setSound(audio, secs=2, hamming=True)
            m6Sound1.setVolume(3.0, log=False)
            m6Key1.keys = []
            m6Key1.rt = []
            _m6Key1_allKeys = []
            # keep track of which components have finished
            mini6_2Components = [m6CorrPL, m6CorrCON, m6Sound1, m6Key1, space16]
            for thisComponent in mini6_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini6_2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m6CorrPL* updates
                
                # if m6CorrPL is starting this frame...
                if m6CorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m6CorrPL.frameNStart = frameN  # exact frame index
                    m6CorrPL.tStart = t  # local t and not account for scr refresh
                    m6CorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m6CorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m6CorrPL.status = STARTED
                    m6CorrPL.setAutoDraw(True)
                
                # if m6CorrPL is active this frame...
                if m6CorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m6CorrCON* updates
                
                # if m6CorrCON is starting this frame...
                if m6CorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m6CorrCON.frameNStart = frameN  # exact frame index
                    m6CorrCON.tStart = t  # local t and not account for scr refresh
                    m6CorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m6CorrCON, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'm6CorrCON.started')
                    # update status
                    m6CorrCON.status = STARTED
                    m6CorrCON.setAutoDraw(True)
                
                # if m6CorrCON is active this frame...
                if m6CorrCON.status == STARTED:
                    # update params
                    pass
                # start/stop m6Sound1
                
                # if m6Sound1 is starting this frame...
                if m6Sound1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m6Sound1.frameNStart = frameN  # exact frame index
                    m6Sound1.tStart = t  # local t and not account for scr refresh
                    m6Sound1.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m6Sound1.status = STARTED
                    m6Sound1.play(when=win)  # sync with win flip
                
                # if m6Sound1 is stopping this frame...
                if m6Sound1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m6Sound1.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m6Sound1.tStop = t  # not accounting for scr refresh
                        m6Sound1.frameNStop = frameN  # exact frame index
                        # update status
                        m6Sound1.status = FINISHED
                        m6Sound1.stop()
                
                # *m6Key1* updates
                
                # if m6Key1 is starting this frame...
                if m6Key1.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m6Key1.frameNStart = frameN  # exact frame index
                    m6Key1.tStart = t  # local t and not account for scr refresh
                    m6Key1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m6Key1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m6Key1.status = STARTED
                    # keyboard checking is just starting
                    m6Key1.clock.reset()  # now t=0
                if m6Key1.status == STARTED:
                    theseKeys = m6Key1.getKeys(keyList=['space'], waitRelease=False)
                    _m6Key1_allKeys.extend(theseKeys)
                    if len(_m6Key1_allKeys):
                        m6Key1.keys = _m6Key1_allKeys[-1].name  # just the last key pressed
                        m6Key1.rt = _m6Key1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space16* updates
                
                # if space16 is starting this frame...
                if space16.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space16.frameNStart = frameN  # exact frame index
                    space16.tStart = t  # local t and not account for scr refresh
                    space16.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space16, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space16.status = STARTED
                    space16.setAutoDraw(True)
                
                # if space16 is active this frame...
                if space16.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini6_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini6_2" ---
            for thisComponent in mini6_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m6Code2
            if m6Count == 12:
                mini6Loop.finished = True
            m6Sound1.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini6_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM6Corr repeats of 'm6CorrLoop'
        
        
        # set up handler to look after randomisation of conditions etc
        m6IncorrLoop = data.TrialHandler(nReps=nRepsM6Incorr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m6IncorrLoop')
        thisExp.addLoop(m6IncorrLoop)  # add the loop to the experiment
        thisM6IncorrLoop = m6IncorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM6IncorrLoop.rgb)
        if thisM6IncorrLoop != None:
            for paramName in thisM6IncorrLoop:
                exec('{} = thisM6IncorrLoop[paramName]'.format(paramName))
        
        for thisM6IncorrLoop in m6IncorrLoop:
            currentLoop = m6IncorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM6IncorrLoop.rgb)
            if thisM6IncorrLoop != None:
                for paramName in thisM6IncorrLoop:
                    exec('{} = thisM6IncorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini6_3" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m6Code3
            m6Count = m6Count+1
            m6IncorrPL.setImage(img)
            m6IncorrCON.setPos([m6Posi[0]])
            m6IncorrCON.setText(conWord)
            m6IncorrDIST.setPos(incorrPosi6)
            m6IncorrDIST.setText(incorrAns6)
            m6Sound2.setSound(audio, secs=2, hamming=True)
            m6Sound2.setVolume(3.0, log=False)
            m6Key2.keys = []
            m6Key2.rt = []
            _m6Key2_allKeys = []
            # keep track of which components have finished
            mini6_3Components = [m6IncorrPL, m6IncorrCON, m6IncorrDIST, m6Sound2, m6Key2, space17]
            for thisComponent in mini6_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini6_3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m6IncorrPL* updates
                
                # if m6IncorrPL is starting this frame...
                if m6IncorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m6IncorrPL.frameNStart = frameN  # exact frame index
                    m6IncorrPL.tStart = t  # local t and not account for scr refresh
                    m6IncorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m6IncorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m6IncorrPL.status = STARTED
                    m6IncorrPL.setAutoDraw(True)
                
                # if m6IncorrPL is active this frame...
                if m6IncorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m6IncorrCON* updates
                
                # if m6IncorrCON is starting this frame...
                if m6IncorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m6IncorrCON.frameNStart = frameN  # exact frame index
                    m6IncorrCON.tStart = t  # local t and not account for scr refresh
                    m6IncorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m6IncorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m6IncorrCON.status = STARTED
                    m6IncorrCON.setAutoDraw(True)
                
                # if m6IncorrCON is active this frame...
                if m6IncorrCON.status == STARTED:
                    # update params
                    pass
                
                # *m6IncorrDIST* updates
                
                # if m6IncorrDIST is starting this frame...
                if m6IncorrDIST.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m6IncorrDIST.frameNStart = frameN  # exact frame index
                    m6IncorrDIST.tStart = t  # local t and not account for scr refresh
                    m6IncorrDIST.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m6IncorrDIST, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m6IncorrDIST.status = STARTED
                    m6IncorrDIST.setAutoDraw(True)
                
                # if m6IncorrDIST is active this frame...
                if m6IncorrDIST.status == STARTED:
                    # update params
                    pass
                # start/stop m6Sound2
                
                # if m6Sound2 is starting this frame...
                if m6Sound2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m6Sound2.frameNStart = frameN  # exact frame index
                    m6Sound2.tStart = t  # local t and not account for scr refresh
                    m6Sound2.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m6Sound2.status = STARTED
                    m6Sound2.play(when=win)  # sync with win flip
                
                # if m6Sound2 is stopping this frame...
                if m6Sound2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m6Sound2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m6Sound2.tStop = t  # not accounting for scr refresh
                        m6Sound2.frameNStop = frameN  # exact frame index
                        # update status
                        m6Sound2.status = FINISHED
                        m6Sound2.stop()
                
                # *m6Key2* updates
                
                # if m6Key2 is starting this frame...
                if m6Key2.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m6Key2.frameNStart = frameN  # exact frame index
                    m6Key2.tStart = t  # local t and not account for scr refresh
                    m6Key2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m6Key2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m6Key2.status = STARTED
                    # keyboard checking is just starting
                    m6Key2.clock.reset()  # now t=0
                if m6Key2.status == STARTED:
                    theseKeys = m6Key2.getKeys(keyList=['space'], waitRelease=False)
                    _m6Key2_allKeys.extend(theseKeys)
                    if len(_m6Key2_allKeys):
                        m6Key2.keys = _m6Key2_allKeys[-1].name  # just the last key pressed
                        m6Key2.rt = _m6Key2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space17* updates
                
                # if space17 is starting this frame...
                if space17.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space17.frameNStart = frameN  # exact frame index
                    space17.tStart = t  # local t and not account for scr refresh
                    space17.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space17, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space17.status = STARTED
                    space17.setAutoDraw(True)
                
                # if space17 is active this frame...
                if space17.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini6_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini6_3" ---
            for thisComponent in mini6_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m6Code3
            if m6Count==12:
                mini6Loop.finished = True
            m6Sound2.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini6_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM6Incorr repeats of 'm6IncorrLoop'
        
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'mini6Loop'
    
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'img3'


# set up handler to look after randomisation of conditions etc
ortho4 = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='ortho4')
thisExp.addLoop(ortho4)  # add the loop to the experiment
thisOrtho4 = ortho4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOrtho4.rgb)
if thisOrtho4 != None:
    for paramName in thisOrtho4:
        exec('{} = thisOrtho4[paramName]'.format(paramName))

for thisOrtho4 in ortho4:
    currentLoop = ortho4
    # abbreviate parameter names if possible (e.g. rgb = thisOrtho4.rgb)
    if thisOrtho4 != None:
        for paramName in thisOrtho4:
            exec('{} = thisOrtho4[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    exp7Loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("orthostim_" + expInfo['group'] + ".xlsx", selection='12:16'),
        seed=None, name='exp7Loop')
    thisExp.addLoop(exp7Loop)  # add the loop to the experiment
    thisExp7Loop = exp7Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExp7Loop.rgb)
    if thisExp7Loop != None:
        for paramName in thisExp7Loop:
            exec('{} = thisExp7Loop[paramName]'.format(paramName))
    
    for thisExp7Loop in exp7Loop:
        currentLoop = exp7Loop
        # abbreviate parameter names if possible (e.g. rgb = thisExp7Loop.rgb)
        if thisExp7Loop != None:
            for paramName in thisExp7Loop:
                exec('{} = thisExp7Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "exp7_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        e7PL.setText(plWord)
        # keep track of which components have finished
        exp7_1Components = [e7Focal1, e7PL]
        for thisComponent in exp7_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp7_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e7Focal1* updates
            
            # if e7Focal1 is starting this frame...
            if e7Focal1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                e7Focal1.frameNStart = frameN  # exact frame index
                e7Focal1.tStart = t  # local t and not account for scr refresh
                e7Focal1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e7Focal1, 'tStartRefresh')  # time at next scr refresh
                # update status
                e7Focal1.status = STARTED
                e7Focal1.setAutoDraw(True)
            
            # if e7Focal1 is active this frame...
            if e7Focal1.status == STARTED:
                # update params
                pass
            
            # if e7Focal1 is stopping this frame...
            if e7Focal1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e7Focal1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    e7Focal1.tStop = t  # not accounting for scr refresh
                    e7Focal1.frameNStop = frameN  # exact frame index
                    # update status
                    e7Focal1.status = FINISHED
                    e7Focal1.setAutoDraw(False)
            
            # *e7PL* updates
            
            # if e7PL is starting this frame...
            if e7PL.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
                # keep track of start time/frame for later
                e7PL.frameNStart = frameN  # exact frame index
                e7PL.tStart = t  # local t and not account for scr refresh
                e7PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e7PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                e7PL.status = STARTED
                e7PL.setAutoDraw(True)
            
            # if e7PL is active this frame...
            if e7PL.status == STARTED:
                # update params
                pass
            
            # if e7PL is stopping this frame...
            if e7PL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e7PL.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    e7PL.tStop = t  # not accounting for scr refresh
                    e7PL.frameNStop = frameN  # exact frame index
                    # update status
                    e7PL.status = FINISHED
                    e7PL.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp7_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp7_1" ---
        for thisComponent in exp7_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.100000)
        
        # --- Prepare to start Routine "exp7_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from e7Code2
        e7Count = e7Count+1
        e7CON.setText(conWord)
        e7Sound.setSound(audio, hamming=True)
        e7Sound.setVolume(3.0, log=False)
        e7Key.keys = []
        e7Key.rt = []
        _e7Key_allKeys = []
        # keep track of which components have finished
        exp7_2Components = [e7Focal2, e7CON, e7Sound, e7Key, space18]
        for thisComponent in exp7_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp7_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e7Focal2* updates
            
            # if e7Focal2 is starting this frame...
            if e7Focal2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                e7Focal2.frameNStart = frameN  # exact frame index
                e7Focal2.tStart = t  # local t and not account for scr refresh
                e7Focal2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e7Focal2, 'tStartRefresh')  # time at next scr refresh
                # update status
                e7Focal2.status = STARTED
                e7Focal2.setAutoDraw(True)
            
            # if e7Focal2 is active this frame...
            if e7Focal2.status == STARTED:
                # update params
                pass
            
            # if e7Focal2 is stopping this frame...
            if e7Focal2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e7Focal2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    e7Focal2.tStop = t  # not accounting for scr refresh
                    e7Focal2.frameNStop = frameN  # exact frame index
                    # update status
                    e7Focal2.status = FINISHED
                    e7Focal2.setAutoDraw(False)
            
            # *e7CON* updates
            
            # if e7CON is starting this frame...
            if e7CON.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e7CON.frameNStart = frameN  # exact frame index
                e7CON.tStart = t  # local t and not account for scr refresh
                e7CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e7CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                e7CON.status = STARTED
                e7CON.setAutoDraw(True)
            
            # if e7CON is active this frame...
            if e7CON.status == STARTED:
                # update params
                pass
            # start/stop e7Sound
            
            # if e7Sound is starting this frame...
            if e7Sound.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e7Sound.frameNStart = frameN  # exact frame index
                e7Sound.tStart = t  # local t and not account for scr refresh
                e7Sound.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                e7Sound.status = STARTED
                e7Sound.play(when=win)  # sync with win flip
            
            # *e7Key* updates
            
            # if e7Key is starting this frame...
            if e7Key.status == NOT_STARTED and t >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                e7Key.frameNStart = frameN  # exact frame index
                e7Key.tStart = t  # local t and not account for scr refresh
                e7Key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e7Key, 'tStartRefresh')  # time at next scr refresh
                # update status
                e7Key.status = STARTED
                # keyboard checking is just starting
                e7Key.clock.reset()  # now t=0
            if e7Key.status == STARTED:
                theseKeys = e7Key.getKeys(keyList=['space'], waitRelease=False)
                _e7Key_allKeys.extend(theseKeys)
                if len(_e7Key_allKeys):
                    e7Key.keys = _e7Key_allKeys[-1].name  # just the last key pressed
                    e7Key.rt = _e7Key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *space18* updates
            
            # if space18 is starting this frame...
            if space18.status == NOT_STARTED and tThisFlip >= 3.2-frameTolerance:
                # keep track of start time/frame for later
                space18.frameNStart = frameN  # exact frame index
                space18.tStart = t  # local t and not account for scr refresh
                space18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space18, 'tStartRefresh')  # time at next scr refresh
                # update status
                space18.status = STARTED
                space18.setAutoDraw(True)
            
            # if space18 is active this frame...
            if space18.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp7_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp7_2" ---
        for thisComponent in exp7_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from e7Code2
        if e7Count == 4:
            exp7Loop.finished = True
        else:
            pass
        e7Sound.stop()  # ensure sound has stopped at end of routine
        # the Routine "exp7_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'exp7Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    mini7Loop = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("orthostim_" + expInfo['group'] + ".xlsx", selection='12:16'),
        seed=None, name='mini7Loop')
    thisExp.addLoop(mini7Loop)  # add the loop to the experiment
    thisMini7Loop = mini7Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMini7Loop.rgb)
    if thisMini7Loop != None:
        for paramName in thisMini7Loop:
            exec('{} = thisMini7Loop[paramName]'.format(paramName))
    
    for thisMini7Loop in mini7Loop:
        currentLoop = mini7Loop
        # abbreviate parameter names if possible (e.g. rgb = thisMini7Loop.rgb)
        if thisMini7Loop != None:
            for paramName in thisMini7Loop:
                exec('{} = thisMini7Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mini7_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from m7Code1
        random.shuffle(m7Posi)
        print (m7CON.text,m7DIST1.text,m7DIST2.text,m7DIST3.text)
        m7PL.setText(plWord)
        m7CON.setPos([m7Posi[0]])
        m7CON.setText(conWord)
        # reset m7CON to account for continued clicks & clear times on/off
        m7CON.reset()
        m7DIST1.setPos([m7Posi[1]])
        m7DIST1.setText(incorr1)
        # reset m7DIST1 to account for continued clicks & clear times on/off
        m7DIST1.reset()
        m7DIST2.setPos([m7Posi[2]])
        m7DIST2.setText(incorr2)
        # reset m7DIST2 to account for continued clicks & clear times on/off
        m7DIST2.reset()
        m7DIST3.setPos([m7Posi[3]])
        m7DIST3.setText(incorr3)
        # reset m7DIST3 to account for continued clicks & clear times on/off
        m7DIST3.reset()
        # setup some python lists for storing info about the m7Mouse
        m7Mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        mini7_1Components = [m7PL, m7CON, m7DIST1, m7DIST2, m7DIST3, m7Mouse]
        for thisComponent in mini7_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mini7_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *m7PL* updates
            
            # if m7PL is starting this frame...
            if m7PL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m7PL.frameNStart = frameN  # exact frame index
                m7PL.tStart = t  # local t and not account for scr refresh
                m7PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m7PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                m7PL.status = STARTED
                m7PL.setAutoDraw(True)
            
            # if m7PL is active this frame...
            if m7PL.status == STARTED:
                # update params
                pass
            # *m7CON* updates
            
            # if m7CON is starting this frame...
            if m7CON.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m7CON.frameNStart = frameN  # exact frame index
                m7CON.tStart = t  # local t and not account for scr refresh
                m7CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m7CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                m7CON.status = STARTED
                m7CON.setAutoDraw(True)
            
            # if m7CON is active this frame...
            if m7CON.status == STARTED:
                # update params
                pass
                # check whether m7CON has been pressed
                if m7CON.isClicked:
                    if not m7CON.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m7CON.timesOn.append(m7CON.buttonClock.getTime())
                        m7CON.timesOff.append(m7CON.buttonClock.getTime())
                    elif len(m7CON.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m7CON.timesOff[-1] = m7CON.buttonClock.getTime()
                    if not m7CON.wasClicked:
                        # end routine when m7CON is clicked
                        continueRoutine = False
                    if not m7CON.wasClicked:
                        # run callback code when m7CON is clicked
                        pass
            # take note of whether m7CON was clicked, so that next frame we know if clicks are new
            m7CON.wasClicked = m7CON.isClicked and m7CON.status == STARTED
            # *m7DIST1* updates
            
            # if m7DIST1 is starting this frame...
            if m7DIST1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m7DIST1.frameNStart = frameN  # exact frame index
                m7DIST1.tStart = t  # local t and not account for scr refresh
                m7DIST1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m7DIST1, 'tStartRefresh')  # time at next scr refresh
                # update status
                m7DIST1.status = STARTED
                m7DIST1.setAutoDraw(True)
            
            # if m7DIST1 is active this frame...
            if m7DIST1.status == STARTED:
                # update params
                pass
                # check whether m7DIST1 has been pressed
                if m7DIST1.isClicked:
                    if not m7DIST1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m7DIST1.timesOn.append(m7DIST1.buttonClock.getTime())
                        m7DIST1.timesOff.append(m7DIST1.buttonClock.getTime())
                    elif len(m7DIST1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m7DIST1.timesOff[-1] = m7DIST1.buttonClock.getTime()
                    if not m7DIST1.wasClicked:
                        # end routine when m7DIST1 is clicked
                        continueRoutine = False
                    if not m7DIST1.wasClicked:
                        # run callback code when m7DIST1 is clicked
                        pass
            # take note of whether m7DIST1 was clicked, so that next frame we know if clicks are new
            m7DIST1.wasClicked = m7DIST1.isClicked and m7DIST1.status == STARTED
            # *m7DIST2* updates
            
            # if m7DIST2 is starting this frame...
            if m7DIST2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m7DIST2.frameNStart = frameN  # exact frame index
                m7DIST2.tStart = t  # local t and not account for scr refresh
                m7DIST2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m7DIST2, 'tStartRefresh')  # time at next scr refresh
                # update status
                m7DIST2.status = STARTED
                m7DIST2.setAutoDraw(True)
            
            # if m7DIST2 is active this frame...
            if m7DIST2.status == STARTED:
                # update params
                pass
                # check whether m7DIST2 has been pressed
                if m7DIST2.isClicked:
                    if not m7DIST2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m7DIST2.timesOn.append(m7DIST2.buttonClock.getTime())
                        m7DIST2.timesOff.append(m7DIST2.buttonClock.getTime())
                    elif len(m7DIST2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m7DIST2.timesOff[-1] = m7DIST2.buttonClock.getTime()
                    if not m7DIST2.wasClicked:
                        # end routine when m7DIST2 is clicked
                        continueRoutine = False
                    if not m7DIST2.wasClicked:
                        # run callback code when m7DIST2 is clicked
                        pass
            # take note of whether m7DIST2 was clicked, so that next frame we know if clicks are new
            m7DIST2.wasClicked = m7DIST2.isClicked and m7DIST2.status == STARTED
            # *m7DIST3* updates
            
            # if m7DIST3 is starting this frame...
            if m7DIST3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m7DIST3.frameNStart = frameN  # exact frame index
                m7DIST3.tStart = t  # local t and not account for scr refresh
                m7DIST3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m7DIST3, 'tStartRefresh')  # time at next scr refresh
                # update status
                m7DIST3.status = STARTED
                m7DIST3.setAutoDraw(True)
            
            # if m7DIST3 is active this frame...
            if m7DIST3.status == STARTED:
                # update params
                pass
                # check whether m7DIST3 has been pressed
                if m7DIST3.isClicked:
                    if not m7DIST3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m7DIST3.timesOn.append(m7DIST3.buttonClock.getTime())
                        m7DIST3.timesOff.append(m7DIST3.buttonClock.getTime())
                    elif len(m7DIST3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m7DIST3.timesOff[-1] = m7DIST3.buttonClock.getTime()
                    if not m7DIST3.wasClicked:
                        # end routine when m7DIST3 is clicked
                        continueRoutine = False
                    if not m7DIST3.wasClicked:
                        # run callback code when m7DIST3 is clicked
                        pass
            # take note of whether m7DIST3 was clicked, so that next frame we know if clicks are new
            m7DIST3.wasClicked = m7DIST3.isClicked and m7DIST3.status == STARTED
            # *m7Mouse* updates
            
            # if m7Mouse is starting this frame...
            if m7Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m7Mouse.frameNStart = frameN  # exact frame index
                m7Mouse.tStart = t  # local t and not account for scr refresh
                m7Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m7Mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'm7Mouse.started')
                # update status
                m7Mouse.status = STARTED
                m7Mouse.mouseClock.reset()
                prevButtonState = m7Mouse.getPressed()  # if button is down already this ISN'T a new click
            if m7Mouse.status == STARTED:  # only update if started and not finished!
                buttons = m7Mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = core.getFromNames([m7CON,m7DIST1,m7DIST2,m7DIST3])
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(m7Mouse):
                                gotValidClick = True
                                m7Mouse.clicked_name.append(obj.name)
                        continueRoutine = False  # end routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mini7_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mini7_1" ---
        for thisComponent in mini7_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from m7Code1
        if m7Mouse.isPressedIn(m7CON):
            nRepsM7Corr = True
            nRepsM7Incorr = False
            thisExp.addData("mCorr Response",m7CON.text)
        else:
            nRepsM7Corr = False
            nRepsM7Incorr = True
        
        if m7Mouse.isPressedIn(m7DIST1):
            incorrAns7=m7DIST1.text
            incorrPosi7=m7DIST1.pos
            thisExp.addData("mIncorr Repsonse",m7DIST1.text)
        elif m7Mouse.isPressedIn(m7DIST2):
            incorrAns7=m7DIST2.text
            incorrPosi7=m7DIST2.pos
            thisExp.addData("mIncorr Repsonse",m7DIST2.text)
        elif m7Mouse.isPressedIn(m7DIST3):
            incorrAns7=m7DIST3.text
            incorrPosi7=m7DIST3.pos
            thisExp.addData("mIncorr Repsonse",m7DIST3.text)
        # store data for mini7Loop (TrialHandler)
        # the Routine "mini7_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        m7CorrLoop = data.TrialHandler(nReps=nRepsM7Corr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m7CorrLoop')
        thisExp.addLoop(m7CorrLoop)  # add the loop to the experiment
        thisM7CorrLoop = m7CorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM7CorrLoop.rgb)
        if thisM7CorrLoop != None:
            for paramName in thisM7CorrLoop:
                exec('{} = thisM7CorrLoop[paramName]'.format(paramName))
        
        for thisM7CorrLoop in m7CorrLoop:
            currentLoop = m7CorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM7CorrLoop.rgb)
            if thisM7CorrLoop != None:
                for paramName in thisM7CorrLoop:
                    exec('{} = thisM7CorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini7_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m7Code2
            m7Count = m7Count+1
            m7CorrPL.setText(plWord)
            m7CorrCON.setPos([m7Posi[0]])
            m7CorrCON.setText(conWord)
            m7Sound1.setSound(audio, secs=2, hamming=True)
            m7Sound1.setVolume(3.0, log=False)
            m7Key1.keys = []
            m7Key1.rt = []
            _m7Key1_allKeys = []
            # keep track of which components have finished
            mini7_2Components = [m7CorrPL, m7CorrCON, m7Sound1, m7Key1, space19]
            for thisComponent in mini7_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini7_2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m7CorrPL* updates
                
                # if m7CorrPL is starting this frame...
                if m7CorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m7CorrPL.frameNStart = frameN  # exact frame index
                    m7CorrPL.tStart = t  # local t and not account for scr refresh
                    m7CorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m7CorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m7CorrPL.status = STARTED
                    m7CorrPL.setAutoDraw(True)
                
                # if m7CorrPL is active this frame...
                if m7CorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m7CorrCON* updates
                
                # if m7CorrCON is starting this frame...
                if m7CorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m7CorrCON.frameNStart = frameN  # exact frame index
                    m7CorrCON.tStart = t  # local t and not account for scr refresh
                    m7CorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m7CorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m7CorrCON.status = STARTED
                    m7CorrCON.setAutoDraw(True)
                
                # if m7CorrCON is active this frame...
                if m7CorrCON.status == STARTED:
                    # update params
                    pass
                # start/stop m7Sound1
                
                # if m7Sound1 is starting this frame...
                if m7Sound1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m7Sound1.frameNStart = frameN  # exact frame index
                    m7Sound1.tStart = t  # local t and not account for scr refresh
                    m7Sound1.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m7Sound1.status = STARTED
                    m7Sound1.play(when=win)  # sync with win flip
                
                # if m7Sound1 is stopping this frame...
                if m7Sound1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m7Sound1.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m7Sound1.tStop = t  # not accounting for scr refresh
                        m7Sound1.frameNStop = frameN  # exact frame index
                        # update status
                        m7Sound1.status = FINISHED
                        m7Sound1.stop()
                
                # *m7Key1* updates
                
                # if m7Key1 is starting this frame...
                if m7Key1.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m7Key1.frameNStart = frameN  # exact frame index
                    m7Key1.tStart = t  # local t and not account for scr refresh
                    m7Key1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m7Key1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m7Key1.status = STARTED
                    # keyboard checking is just starting
                    m7Key1.clock.reset()  # now t=0
                if m7Key1.status == STARTED:
                    theseKeys = m7Key1.getKeys(keyList=['space'], waitRelease=False)
                    _m7Key1_allKeys.extend(theseKeys)
                    if len(_m7Key1_allKeys):
                        m7Key1.keys = _m7Key1_allKeys[-1].name  # just the last key pressed
                        m7Key1.rt = _m7Key1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space19* updates
                
                # if space19 is starting this frame...
                if space19.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space19.frameNStart = frameN  # exact frame index
                    space19.tStart = t  # local t and not account for scr refresh
                    space19.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space19, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space19.status = STARTED
                    space19.setAutoDraw(True)
                
                # if space19 is active this frame...
                if space19.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini7_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini7_2" ---
            for thisComponent in mini7_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m7Code2
            if m7Count == 12:
                mini7Loop.finished = True
            m7Sound1.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini7_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM7Corr repeats of 'm7CorrLoop'
        
        
        # set up handler to look after randomisation of conditions etc
        m7IncorrLoop = data.TrialHandler(nReps=nRepsM7Incorr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m7IncorrLoop')
        thisExp.addLoop(m7IncorrLoop)  # add the loop to the experiment
        thisM7IncorrLoop = m7IncorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM7IncorrLoop.rgb)
        if thisM7IncorrLoop != None:
            for paramName in thisM7IncorrLoop:
                exec('{} = thisM7IncorrLoop[paramName]'.format(paramName))
        
        for thisM7IncorrLoop in m7IncorrLoop:
            currentLoop = m7IncorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM7IncorrLoop.rgb)
            if thisM7IncorrLoop != None:
                for paramName in thisM7IncorrLoop:
                    exec('{} = thisM7IncorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini7_3" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m7Code3
            m7Count = m7Count+1
            m7IncorrPL.setText(plWord)
            m7IncorrCON.setPos([m7Posi[0]])
            m7IncorrCON.setText(conWord)
            m7IncorrDIST.setPos(incorrPosi7)
            m7IncorrDIST.setText(incorrAns7)
            m7Sound2.setSound(audio, secs=2, hamming=True)
            m7Sound2.setVolume(3.0, log=False)
            m7Key2.keys = []
            m7Key2.rt = []
            _m7Key2_allKeys = []
            # keep track of which components have finished
            mini7_3Components = [m7IncorrPL, m7IncorrCON, m7IncorrDIST, m7Sound2, m7Key2, space20]
            for thisComponent in mini7_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini7_3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m7IncorrPL* updates
                
                # if m7IncorrPL is starting this frame...
                if m7IncorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m7IncorrPL.frameNStart = frameN  # exact frame index
                    m7IncorrPL.tStart = t  # local t and not account for scr refresh
                    m7IncorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m7IncorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m7IncorrPL.status = STARTED
                    m7IncorrPL.setAutoDraw(True)
                
                # if m7IncorrPL is active this frame...
                if m7IncorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m7IncorrCON* updates
                
                # if m7IncorrCON is starting this frame...
                if m7IncorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m7IncorrCON.frameNStart = frameN  # exact frame index
                    m7IncorrCON.tStart = t  # local t and not account for scr refresh
                    m7IncorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m7IncorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m7IncorrCON.status = STARTED
                    m7IncorrCON.setAutoDraw(True)
                
                # if m7IncorrCON is active this frame...
                if m7IncorrCON.status == STARTED:
                    # update params
                    pass
                
                # *m7IncorrDIST* updates
                
                # if m7IncorrDIST is starting this frame...
                if m7IncorrDIST.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m7IncorrDIST.frameNStart = frameN  # exact frame index
                    m7IncorrDIST.tStart = t  # local t and not account for scr refresh
                    m7IncorrDIST.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m7IncorrDIST, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m7IncorrDIST.status = STARTED
                    m7IncorrDIST.setAutoDraw(True)
                
                # if m7IncorrDIST is active this frame...
                if m7IncorrDIST.status == STARTED:
                    # update params
                    pass
                # start/stop m7Sound2
                
                # if m7Sound2 is starting this frame...
                if m7Sound2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m7Sound2.frameNStart = frameN  # exact frame index
                    m7Sound2.tStart = t  # local t and not account for scr refresh
                    m7Sound2.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m7Sound2.status = STARTED
                    m7Sound2.play(when=win)  # sync with win flip
                
                # if m7Sound2 is stopping this frame...
                if m7Sound2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m7Sound2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m7Sound2.tStop = t  # not accounting for scr refresh
                        m7Sound2.frameNStop = frameN  # exact frame index
                        # update status
                        m7Sound2.status = FINISHED
                        m7Sound2.stop()
                
                # *m7Key2* updates
                
                # if m7Key2 is starting this frame...
                if m7Key2.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m7Key2.frameNStart = frameN  # exact frame index
                    m7Key2.tStart = t  # local t and not account for scr refresh
                    m7Key2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m7Key2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m7Key2.status = STARTED
                    # keyboard checking is just starting
                    m7Key2.clock.reset()  # now t=0
                if m7Key2.status == STARTED:
                    theseKeys = m7Key2.getKeys(keyList=['space'], waitRelease=False)
                    _m7Key2_allKeys.extend(theseKeys)
                    if len(_m7Key2_allKeys):
                        m7Key2.keys = _m7Key2_allKeys[-1].name  # just the last key pressed
                        m7Key2.rt = _m7Key2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space20* updates
                
                # if space20 is starting this frame...
                if space20.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space20.frameNStart = frameN  # exact frame index
                    space20.tStart = t  # local t and not account for scr refresh
                    space20.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space20, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space20.status = STARTED
                    space20.setAutoDraw(True)
                
                # if space20 is active this frame...
                if space20.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini7_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini7_3" ---
            for thisComponent in mini7_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m7Code3
            if m7Count==12:
                mini7Loop.finished = True
            m7Sound2.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini7_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM7Incorr repeats of 'm7IncorrLoop'
        
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'mini7Loop'
    
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'ortho4'


# set up handler to look after randomisation of conditions etc
img4 = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='img4')
thisExp.addLoop(img4)  # add the loop to the experiment
thisImg4 = img4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisImg4.rgb)
if thisImg4 != None:
    for paramName in thisImg4:
        exec('{} = thisImg4[paramName]'.format(paramName))

for thisImg4 in img4:
    currentLoop = img4
    # abbreviate parameter names if possible (e.g. rgb = thisImg4.rgb)
    if thisImg4 != None:
        for paramName in thisImg4:
            exec('{} = thisImg4[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    exp8Loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("imgstim_"+expInfo['group']+".xlsx", selection='12:16'),
        seed=None, name='exp8Loop')
    thisExp.addLoop(exp8Loop)  # add the loop to the experiment
    thisExp8Loop = exp8Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExp8Loop.rgb)
    if thisExp8Loop != None:
        for paramName in thisExp8Loop:
            exec('{} = thisExp8Loop[paramName]'.format(paramName))
    
    for thisExp8Loop in exp8Loop:
        currentLoop = exp8Loop
        # abbreviate parameter names if possible (e.g. rgb = thisExp8Loop.rgb)
        if thisExp8Loop != None:
            for paramName in thisExp8Loop:
                exec('{} = thisExp8Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "exp8_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        e8PL.setImage(img)
        # keep track of which components have finished
        exp8_1Components = [e8Focal1, e8PL]
        for thisComponent in exp8_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp8_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e8Focal1* updates
            
            # if e8Focal1 is starting this frame...
            if e8Focal1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                e8Focal1.frameNStart = frameN  # exact frame index
                e8Focal1.tStart = t  # local t and not account for scr refresh
                e8Focal1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e8Focal1, 'tStartRefresh')  # time at next scr refresh
                # update status
                e8Focal1.status = STARTED
                e8Focal1.setAutoDraw(True)
            
            # if e8Focal1 is active this frame...
            if e8Focal1.status == STARTED:
                # update params
                pass
            
            # if e8Focal1 is stopping this frame...
            if e8Focal1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e8Focal1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    e8Focal1.tStop = t  # not accounting for scr refresh
                    e8Focal1.frameNStop = frameN  # exact frame index
                    # update status
                    e8Focal1.status = FINISHED
                    e8Focal1.setAutoDraw(False)
            
            # *e8PL* updates
            
            # if e8PL is starting this frame...
            if e8PL.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
                # keep track of start time/frame for later
                e8PL.frameNStart = frameN  # exact frame index
                e8PL.tStart = t  # local t and not account for scr refresh
                e8PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e8PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                e8PL.status = STARTED
                e8PL.setAutoDraw(True)
            
            # if e8PL is active this frame...
            if e8PL.status == STARTED:
                # update params
                pass
            
            # if e8PL is stopping this frame...
            if e8PL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e8PL.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    e8PL.tStop = t  # not accounting for scr refresh
                    e8PL.frameNStop = frameN  # exact frame index
                    # update status
                    e8PL.status = FINISHED
                    e8PL.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp8_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp8_1" ---
        for thisComponent in exp8_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.100000)
        
        # --- Prepare to start Routine "exp8_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from e8Code2
        e8Count = e8Count+1
        e8CON.setText(conWord)
        e8Sound.setSound(audio, hamming=True)
        e8Sound.setVolume(3.0, log=False)
        e8Key.keys = []
        e8Key.rt = []
        _e8Key_allKeys = []
        # keep track of which components have finished
        exp8_2Components = [e8Focal2, e8CON, e8Sound, e8Key, space21]
        for thisComponent in exp8_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp8_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e8Focal2* updates
            
            # if e8Focal2 is starting this frame...
            if e8Focal2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                e8Focal2.frameNStart = frameN  # exact frame index
                e8Focal2.tStart = t  # local t and not account for scr refresh
                e8Focal2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e8Focal2, 'tStartRefresh')  # time at next scr refresh
                # update status
                e8Focal2.status = STARTED
                e8Focal2.setAutoDraw(True)
            
            # if e8Focal2 is active this frame...
            if e8Focal2.status == STARTED:
                # update params
                pass
            
            # if e8Focal2 is stopping this frame...
            if e8Focal2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e8Focal2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    e8Focal2.tStop = t  # not accounting for scr refresh
                    e8Focal2.frameNStop = frameN  # exact frame index
                    # update status
                    e8Focal2.status = FINISHED
                    e8Focal2.setAutoDraw(False)
            
            # *e8CON* updates
            
            # if e8CON is starting this frame...
            if e8CON.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e8CON.frameNStart = frameN  # exact frame index
                e8CON.tStart = t  # local t and not account for scr refresh
                e8CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e8CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                e8CON.status = STARTED
                e8CON.setAutoDraw(True)
            
            # if e8CON is active this frame...
            if e8CON.status == STARTED:
                # update params
                pass
            # start/stop e8Sound
            
            # if e8Sound is starting this frame...
            if e8Sound.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e8Sound.frameNStart = frameN  # exact frame index
                e8Sound.tStart = t  # local t and not account for scr refresh
                e8Sound.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                e8Sound.status = STARTED
                e8Sound.play(when=win)  # sync with win flip
            
            # *e8Key* updates
            
            # if e8Key is starting this frame...
            if e8Key.status == NOT_STARTED and t >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                e8Key.frameNStart = frameN  # exact frame index
                e8Key.tStart = t  # local t and not account for scr refresh
                e8Key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e8Key, 'tStartRefresh')  # time at next scr refresh
                # update status
                e8Key.status = STARTED
                # keyboard checking is just starting
                e8Key.clock.reset()  # now t=0
            if e8Key.status == STARTED:
                theseKeys = e8Key.getKeys(keyList=['space'], waitRelease=False)
                _e8Key_allKeys.extend(theseKeys)
                if len(_e8Key_allKeys):
                    e8Key.keys = _e8Key_allKeys[-1].name  # just the last key pressed
                    e8Key.rt = _e8Key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *space21* updates
            
            # if space21 is starting this frame...
            if space21.status == NOT_STARTED and tThisFlip >= 3.2-frameTolerance:
                # keep track of start time/frame for later
                space21.frameNStart = frameN  # exact frame index
                space21.tStart = t  # local t and not account for scr refresh
                space21.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space21, 'tStartRefresh')  # time at next scr refresh
                # update status
                space21.status = STARTED
                space21.setAutoDraw(True)
            
            # if space21 is active this frame...
            if space21.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp8_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp8_2" ---
        for thisComponent in exp8_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from e8Code2
        if e8Count ==4:
            exp8Loop.finished = True
        else:
            pass
        e8Sound.stop()  # ensure sound has stopped at end of routine
        # the Routine "exp8_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'exp8Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    mini8Loop = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("imgstim_"+expInfo['group']+".xlsx", selection='12:16'),
        seed=None, name='mini8Loop')
    thisExp.addLoop(mini8Loop)  # add the loop to the experiment
    thisMini8Loop = mini8Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMini8Loop.rgb)
    if thisMini8Loop != None:
        for paramName in thisMini8Loop:
            exec('{} = thisMini8Loop[paramName]'.format(paramName))
    
    for thisMini8Loop in mini8Loop:
        currentLoop = mini8Loop
        # abbreviate parameter names if possible (e.g. rgb = thisMini8Loop.rgb)
        if thisMini8Loop != None:
            for paramName in thisMini8Loop:
                exec('{} = thisMini8Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mini8_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from m8Code1
        random.shuffle(m8Posi)
        m8PL.setImage(img)
        m8CON.setPos([m8Posi[0]])
        m8CON.setText(conWord)
        # reset m8CON to account for continued clicks & clear times on/off
        m8CON.reset()
        m8DIST1.setPos([m8Posi[1]])
        m8DIST1.setText(incorr1)
        # reset m8DIST1 to account for continued clicks & clear times on/off
        m8DIST1.reset()
        m8DIST2.setPos([m8Posi[2]])
        m8DIST2.setText(incorr2)
        # reset m8DIST2 to account for continued clicks & clear times on/off
        m8DIST2.reset()
        m8DIST3.setPos([m8Posi[3]])
        m8DIST3.setText(incorr3)
        # reset m8DIST3 to account for continued clicks & clear times on/off
        m8DIST3.reset()
        # setup some python lists for storing info about the m8Mouse
        m8Mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        mini8_1Components = [m8PL, m8CON, m8DIST1, m8DIST2, m8DIST3, m8Mouse]
        for thisComponent in mini8_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mini8_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *m8PL* updates
            
            # if m8PL is starting this frame...
            if m8PL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m8PL.frameNStart = frameN  # exact frame index
                m8PL.tStart = t  # local t and not account for scr refresh
                m8PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m8PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                m8PL.status = STARTED
                m8PL.setAutoDraw(True)
            
            # if m8PL is active this frame...
            if m8PL.status == STARTED:
                # update params
                pass
            # *m8CON* updates
            
            # if m8CON is starting this frame...
            if m8CON.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m8CON.frameNStart = frameN  # exact frame index
                m8CON.tStart = t  # local t and not account for scr refresh
                m8CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m8CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                m8CON.status = STARTED
                m8CON.setAutoDraw(True)
            
            # if m8CON is active this frame...
            if m8CON.status == STARTED:
                # update params
                pass
                # check whether m8CON has been pressed
                if m8CON.isClicked:
                    if not m8CON.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m8CON.timesOn.append(m8CON.buttonClock.getTime())
                        m8CON.timesOff.append(m8CON.buttonClock.getTime())
                    elif len(m8CON.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m8CON.timesOff[-1] = m8CON.buttonClock.getTime()
                    if not m8CON.wasClicked:
                        # end routine when m8CON is clicked
                        continueRoutine = False
                    if not m8CON.wasClicked:
                        # run callback code when m8CON is clicked
                        pass
            # take note of whether m8CON was clicked, so that next frame we know if clicks are new
            m8CON.wasClicked = m8CON.isClicked and m8CON.status == STARTED
            # *m8DIST1* updates
            
            # if m8DIST1 is starting this frame...
            if m8DIST1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m8DIST1.frameNStart = frameN  # exact frame index
                m8DIST1.tStart = t  # local t and not account for scr refresh
                m8DIST1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m8DIST1, 'tStartRefresh')  # time at next scr refresh
                # update status
                m8DIST1.status = STARTED
                m8DIST1.setAutoDraw(True)
            
            # if m8DIST1 is active this frame...
            if m8DIST1.status == STARTED:
                # update params
                pass
                # check whether m8DIST1 has been pressed
                if m8DIST1.isClicked:
                    if not m8DIST1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m8DIST1.timesOn.append(m8DIST1.buttonClock.getTime())
                        m8DIST1.timesOff.append(m8DIST1.buttonClock.getTime())
                    elif len(m8DIST1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m8DIST1.timesOff[-1] = m8DIST1.buttonClock.getTime()
                    if not m8DIST1.wasClicked:
                        # end routine when m8DIST1 is clicked
                        continueRoutine = False
                    if not m8DIST1.wasClicked:
                        # run callback code when m8DIST1 is clicked
                        pass
            # take note of whether m8DIST1 was clicked, so that next frame we know if clicks are new
            m8DIST1.wasClicked = m8DIST1.isClicked and m8DIST1.status == STARTED
            # *m8DIST2* updates
            
            # if m8DIST2 is starting this frame...
            if m8DIST2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m8DIST2.frameNStart = frameN  # exact frame index
                m8DIST2.tStart = t  # local t and not account for scr refresh
                m8DIST2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m8DIST2, 'tStartRefresh')  # time at next scr refresh
                # update status
                m8DIST2.status = STARTED
                m8DIST2.setAutoDraw(True)
            
            # if m8DIST2 is active this frame...
            if m8DIST2.status == STARTED:
                # update params
                pass
                # check whether m8DIST2 has been pressed
                if m8DIST2.isClicked:
                    if not m8DIST2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m8DIST2.timesOn.append(m8DIST2.buttonClock.getTime())
                        m8DIST2.timesOff.append(m8DIST2.buttonClock.getTime())
                    elif len(m8DIST2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m8DIST2.timesOff[-1] = m8DIST2.buttonClock.getTime()
                    if not m8DIST2.wasClicked:
                        # end routine when m8DIST2 is clicked
                        continueRoutine = False
                    if not m8DIST2.wasClicked:
                        # run callback code when m8DIST2 is clicked
                        pass
            # take note of whether m8DIST2 was clicked, so that next frame we know if clicks are new
            m8DIST2.wasClicked = m8DIST2.isClicked and m8DIST2.status == STARTED
            # *m8DIST3* updates
            
            # if m8DIST3 is starting this frame...
            if m8DIST3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m8DIST3.frameNStart = frameN  # exact frame index
                m8DIST3.tStart = t  # local t and not account for scr refresh
                m8DIST3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m8DIST3, 'tStartRefresh')  # time at next scr refresh
                # update status
                m8DIST3.status = STARTED
                m8DIST3.setAutoDraw(True)
            
            # if m8DIST3 is active this frame...
            if m8DIST3.status == STARTED:
                # update params
                pass
                # check whether m8DIST3 has been pressed
                if m8DIST3.isClicked:
                    if not m8DIST3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m8DIST3.timesOn.append(m8DIST3.buttonClock.getTime())
                        m8DIST3.timesOff.append(m8DIST3.buttonClock.getTime())
                    elif len(m8DIST3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m8DIST3.timesOff[-1] = m8DIST3.buttonClock.getTime()
                    if not m8DIST3.wasClicked:
                        # end routine when m8DIST3 is clicked
                        continueRoutine = False
                    if not m8DIST3.wasClicked:
                        # run callback code when m8DIST3 is clicked
                        pass
            # take note of whether m8DIST3 was clicked, so that next frame we know if clicks are new
            m8DIST3.wasClicked = m8DIST3.isClicked and m8DIST3.status == STARTED
            # *m8Mouse* updates
            
            # if m8Mouse is starting this frame...
            if m8Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m8Mouse.frameNStart = frameN  # exact frame index
                m8Mouse.tStart = t  # local t and not account for scr refresh
                m8Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m8Mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'm8Mouse.started')
                # update status
                m8Mouse.status = STARTED
                m8Mouse.mouseClock.reset()
                prevButtonState = m8Mouse.getPressed()  # if button is down already this ISN'T a new click
            if m8Mouse.status == STARTED:  # only update if started and not finished!
                buttons = m8Mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = core.getFromNames([m8CON,m8DIST1,m8DIST2,m8DIST3])
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(m8Mouse):
                                gotValidClick = True
                                m8Mouse.clicked_name.append(obj.name)
                        continueRoutine = False  # end routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mini8_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mini8_1" ---
        for thisComponent in mini8_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from m8Code1
        if m8Mouse.isPressedIn(m8CON):
            nRepsM8Corr = True
            nRepsM8Incorr = False
            thisExp.addData("mCorr Response",m8CON.text)
        else:
            nRepsM8Corr = False
            nRepsM8Incorr = True
        
        if m8Mouse.isPressedIn(m8DIST1):
            incorrAns8=m8DIST1.text
            incorrPosi8=m8DIST1.pos
            thisExp.addData("mIncorr Repsonse",m8DIST1.text)
        elif m8Mouse.isPressedIn(m8DIST2):
            incorrAns8=m8DIST2.text
            incorrPosi8=m8DIST2.pos
            thisExp.addData("mIncorr Repsonse",m8DIST2.text)
        elif m8Mouse.isPressedIn(m8DIST3):
            incorrAns8=m8DIST3.text
            incorrPosi8=m8DIST3.pos
            thisExp.addData("mIncorr Repsonse",m8DIST3.text)
        # store data for mini8Loop (TrialHandler)
        # the Routine "mini8_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        m8CorrLoop = data.TrialHandler(nReps=nRepsM8Corr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m8CorrLoop')
        thisExp.addLoop(m8CorrLoop)  # add the loop to the experiment
        thisM8CorrLoop = m8CorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM8CorrLoop.rgb)
        if thisM8CorrLoop != None:
            for paramName in thisM8CorrLoop:
                exec('{} = thisM8CorrLoop[paramName]'.format(paramName))
        
        for thisM8CorrLoop in m8CorrLoop:
            currentLoop = m8CorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM8CorrLoop.rgb)
            if thisM8CorrLoop != None:
                for paramName in thisM8CorrLoop:
                    exec('{} = thisM8CorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini8_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m8Code2
            m8Count = m8Count+1
            m8CorrPL.setImage(img)
            m8CorrCON.setPos([m8Posi[0]])
            m8CorrCON.setText(conWord)
            m8Sound1.setSound(audio, secs=2, hamming=True)
            m8Sound1.setVolume(3.0, log=False)
            m8Key1.keys = []
            m8Key1.rt = []
            _m8Key1_allKeys = []
            # keep track of which components have finished
            mini8_2Components = [m8CorrPL, m8CorrCON, m8Sound1, m8Key1, space22]
            for thisComponent in mini8_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini8_2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m8CorrPL* updates
                
                # if m8CorrPL is starting this frame...
                if m8CorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m8CorrPL.frameNStart = frameN  # exact frame index
                    m8CorrPL.tStart = t  # local t and not account for scr refresh
                    m8CorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m8CorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m8CorrPL.status = STARTED
                    m8CorrPL.setAutoDraw(True)
                
                # if m8CorrPL is active this frame...
                if m8CorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m8CorrCON* updates
                
                # if m8CorrCON is starting this frame...
                if m8CorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m8CorrCON.frameNStart = frameN  # exact frame index
                    m8CorrCON.tStart = t  # local t and not account for scr refresh
                    m8CorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m8CorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m8CorrCON.status = STARTED
                    m8CorrCON.setAutoDraw(True)
                
                # if m8CorrCON is active this frame...
                if m8CorrCON.status == STARTED:
                    # update params
                    pass
                # start/stop m8Sound1
                
                # if m8Sound1 is starting this frame...
                if m8Sound1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m8Sound1.frameNStart = frameN  # exact frame index
                    m8Sound1.tStart = t  # local t and not account for scr refresh
                    m8Sound1.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m8Sound1.status = STARTED
                    m8Sound1.play(when=win)  # sync with win flip
                
                # if m8Sound1 is stopping this frame...
                if m8Sound1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m8Sound1.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m8Sound1.tStop = t  # not accounting for scr refresh
                        m8Sound1.frameNStop = frameN  # exact frame index
                        # update status
                        m8Sound1.status = FINISHED
                        m8Sound1.stop()
                
                # *m8Key1* updates
                
                # if m8Key1 is starting this frame...
                if m8Key1.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m8Key1.frameNStart = frameN  # exact frame index
                    m8Key1.tStart = t  # local t and not account for scr refresh
                    m8Key1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m8Key1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m8Key1.status = STARTED
                    # keyboard checking is just starting
                    m8Key1.clock.reset()  # now t=0
                if m8Key1.status == STARTED:
                    theseKeys = m8Key1.getKeys(keyList=['space'], waitRelease=False)
                    _m8Key1_allKeys.extend(theseKeys)
                    if len(_m8Key1_allKeys):
                        m8Key1.keys = _m8Key1_allKeys[-1].name  # just the last key pressed
                        m8Key1.rt = _m8Key1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space22* updates
                
                # if space22 is starting this frame...
                if space22.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space22.frameNStart = frameN  # exact frame index
                    space22.tStart = t  # local t and not account for scr refresh
                    space22.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space22, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space22.status = STARTED
                    space22.setAutoDraw(True)
                
                # if space22 is active this frame...
                if space22.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini8_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini8_2" ---
            for thisComponent in mini8_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m8Code2
            if m8Count == 12:
                mini8Loop.finished = True
            m8Sound1.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini8_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM8Corr repeats of 'm8CorrLoop'
        
        
        # set up handler to look after randomisation of conditions etc
        m8IncorrLoop = data.TrialHandler(nReps=nRepsM8Incorr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m8IncorrLoop')
        thisExp.addLoop(m8IncorrLoop)  # add the loop to the experiment
        thisM8IncorrLoop = m8IncorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM8IncorrLoop.rgb)
        if thisM8IncorrLoop != None:
            for paramName in thisM8IncorrLoop:
                exec('{} = thisM8IncorrLoop[paramName]'.format(paramName))
        
        for thisM8IncorrLoop in m8IncorrLoop:
            currentLoop = m8IncorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM8IncorrLoop.rgb)
            if thisM8IncorrLoop != None:
                for paramName in thisM8IncorrLoop:
                    exec('{} = thisM8IncorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini8_3" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m8Code3
            m8Count = m8Count+1
            m8IncorrPL.setImage(img)
            m8IncorrCON.setPos([m8Posi[0]])
            m8IncorrCON.setText(conWord)
            m8IncorrDIST.setPos(incorrPosi8)
            m8IncorrDIST.setText(incorrAns8)
            m8Sound2.setSound(audio, secs=2, hamming=True)
            m8Sound2.setVolume(3.0, log=False)
            m8Key2.keys = []
            m8Key2.rt = []
            _m8Key2_allKeys = []
            # keep track of which components have finished
            mini8_3Components = [m8IncorrPL, m8IncorrCON, m8IncorrDIST, m8Sound2, m8Key2, space23]
            for thisComponent in mini8_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini8_3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m8IncorrPL* updates
                
                # if m8IncorrPL is starting this frame...
                if m8IncorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m8IncorrPL.frameNStart = frameN  # exact frame index
                    m8IncorrPL.tStart = t  # local t and not account for scr refresh
                    m8IncorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m8IncorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m8IncorrPL.status = STARTED
                    m8IncorrPL.setAutoDraw(True)
                
                # if m8IncorrPL is active this frame...
                if m8IncorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m8IncorrCON* updates
                
                # if m8IncorrCON is starting this frame...
                if m8IncorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m8IncorrCON.frameNStart = frameN  # exact frame index
                    m8IncorrCON.tStart = t  # local t and not account for scr refresh
                    m8IncorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m8IncorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m8IncorrCON.status = STARTED
                    m8IncorrCON.setAutoDraw(True)
                
                # if m8IncorrCON is active this frame...
                if m8IncorrCON.status == STARTED:
                    # update params
                    pass
                
                # *m8IncorrDIST* updates
                
                # if m8IncorrDIST is starting this frame...
                if m8IncorrDIST.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m8IncorrDIST.frameNStart = frameN  # exact frame index
                    m8IncorrDIST.tStart = t  # local t and not account for scr refresh
                    m8IncorrDIST.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m8IncorrDIST, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m8IncorrDIST.status = STARTED
                    m8IncorrDIST.setAutoDraw(True)
                
                # if m8IncorrDIST is active this frame...
                if m8IncorrDIST.status == STARTED:
                    # update params
                    pass
                # start/stop m8Sound2
                
                # if m8Sound2 is starting this frame...
                if m8Sound2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m8Sound2.frameNStart = frameN  # exact frame index
                    m8Sound2.tStart = t  # local t and not account for scr refresh
                    m8Sound2.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m8Sound2.status = STARTED
                    m8Sound2.play(when=win)  # sync with win flip
                
                # if m8Sound2 is stopping this frame...
                if m8Sound2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m8Sound2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m8Sound2.tStop = t  # not accounting for scr refresh
                        m8Sound2.frameNStop = frameN  # exact frame index
                        # update status
                        m8Sound2.status = FINISHED
                        m8Sound2.stop()
                
                # *m8Key2* updates
                
                # if m8Key2 is starting this frame...
                if m8Key2.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m8Key2.frameNStart = frameN  # exact frame index
                    m8Key2.tStart = t  # local t and not account for scr refresh
                    m8Key2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m8Key2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m8Key2.status = STARTED
                    # keyboard checking is just starting
                    m8Key2.clock.reset()  # now t=0
                if m8Key2.status == STARTED:
                    theseKeys = m8Key2.getKeys(keyList=['space'], waitRelease=False)
                    _m8Key2_allKeys.extend(theseKeys)
                    if len(_m8Key2_allKeys):
                        m8Key2.keys = _m8Key2_allKeys[-1].name  # just the last key pressed
                        m8Key2.rt = _m8Key2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space23* updates
                
                # if space23 is starting this frame...
                if space23.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space23.frameNStart = frameN  # exact frame index
                    space23.tStart = t  # local t and not account for scr refresh
                    space23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space23, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space23.status = STARTED
                    space23.setAutoDraw(True)
                
                # if space23 is active this frame...
                if space23.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini8_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini8_3" ---
            for thisComponent in mini8_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m8Code3
            if m8Count==12:
                mini8Loop.finished = True
            m8Sound2.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini8_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM8Incorr repeats of 'm8IncorrLoop'
        
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'mini8Loop'
    
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'img4'


# set up handler to look after randomisation of conditions etc
ortho5 = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='ortho5')
thisExp.addLoop(ortho5)  # add the loop to the experiment
thisOrtho5 = ortho5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOrtho5.rgb)
if thisOrtho5 != None:
    for paramName in thisOrtho5:
        exec('{} = thisOrtho5[paramName]'.format(paramName))

for thisOrtho5 in ortho5:
    currentLoop = ortho5
    # abbreviate parameter names if possible (e.g. rgb = thisOrtho5.rgb)
    if thisOrtho5 != None:
        for paramName in thisOrtho5:
            exec('{} = thisOrtho5[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    exp9Loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("orthostim_" + expInfo['group'] + ".xlsx", selection='16:20'),
        seed=None, name='exp9Loop')
    thisExp.addLoop(exp9Loop)  # add the loop to the experiment
    thisExp9Loop = exp9Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExp9Loop.rgb)
    if thisExp9Loop != None:
        for paramName in thisExp9Loop:
            exec('{} = thisExp9Loop[paramName]'.format(paramName))
    
    for thisExp9Loop in exp9Loop:
        currentLoop = exp9Loop
        # abbreviate parameter names if possible (e.g. rgb = thisExp9Loop.rgb)
        if thisExp9Loop != None:
            for paramName in thisExp9Loop:
                exec('{} = thisExp9Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "exp9_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        e9PL.setText(plWord)
        # keep track of which components have finished
        exp9_1Components = [e9Focal1, e9PL]
        for thisComponent in exp9_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp9_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e9Focal1* updates
            
            # if e9Focal1 is starting this frame...
            if e9Focal1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                e9Focal1.frameNStart = frameN  # exact frame index
                e9Focal1.tStart = t  # local t and not account for scr refresh
                e9Focal1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e9Focal1, 'tStartRefresh')  # time at next scr refresh
                # update status
                e9Focal1.status = STARTED
                e9Focal1.setAutoDraw(True)
            
            # if e9Focal1 is active this frame...
            if e9Focal1.status == STARTED:
                # update params
                pass
            
            # if e9Focal1 is stopping this frame...
            if e9Focal1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e9Focal1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    e9Focal1.tStop = t  # not accounting for scr refresh
                    e9Focal1.frameNStop = frameN  # exact frame index
                    # update status
                    e9Focal1.status = FINISHED
                    e9Focal1.setAutoDraw(False)
            
            # *e9PL* updates
            
            # if e9PL is starting this frame...
            if e9PL.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
                # keep track of start time/frame for later
                e9PL.frameNStart = frameN  # exact frame index
                e9PL.tStart = t  # local t and not account for scr refresh
                e9PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e9PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                e9PL.status = STARTED
                e9PL.setAutoDraw(True)
            
            # if e9PL is active this frame...
            if e9PL.status == STARTED:
                # update params
                pass
            
            # if e9PL is stopping this frame...
            if e9PL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e9PL.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    e9PL.tStop = t  # not accounting for scr refresh
                    e9PL.frameNStop = frameN  # exact frame index
                    # update status
                    e9PL.status = FINISHED
                    e9PL.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp9_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp9_1" ---
        for thisComponent in exp9_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.100000)
        
        # --- Prepare to start Routine "exp9_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from e9Code2
        e9Count = e9Count+1
        e9CON.setText(conWord)
        e9Sound.setSound(audio, hamming=True)
        e9Sound.setVolume(3.0, log=False)
        e9Key.keys = []
        e9Key.rt = []
        _e9Key_allKeys = []
        # keep track of which components have finished
        exp9_2Components = [e9Focal2, e9CON, e9Sound, e9Key, space24]
        for thisComponent in exp9_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp9_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e9Focal2* updates
            
            # if e9Focal2 is starting this frame...
            if e9Focal2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                e9Focal2.frameNStart = frameN  # exact frame index
                e9Focal2.tStart = t  # local t and not account for scr refresh
                e9Focal2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e9Focal2, 'tStartRefresh')  # time at next scr refresh
                # update status
                e9Focal2.status = STARTED
                e9Focal2.setAutoDraw(True)
            
            # if e9Focal2 is active this frame...
            if e9Focal2.status == STARTED:
                # update params
                pass
            
            # if e9Focal2 is stopping this frame...
            if e9Focal2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e9Focal2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    e9Focal2.tStop = t  # not accounting for scr refresh
                    e9Focal2.frameNStop = frameN  # exact frame index
                    # update status
                    e9Focal2.status = FINISHED
                    e9Focal2.setAutoDraw(False)
            
            # *e9CON* updates
            
            # if e9CON is starting this frame...
            if e9CON.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e9CON.frameNStart = frameN  # exact frame index
                e9CON.tStart = t  # local t and not account for scr refresh
                e9CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e9CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                e9CON.status = STARTED
                e9CON.setAutoDraw(True)
            
            # if e9CON is active this frame...
            if e9CON.status == STARTED:
                # update params
                pass
            # start/stop e9Sound
            
            # if e9Sound is starting this frame...
            if e9Sound.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e9Sound.frameNStart = frameN  # exact frame index
                e9Sound.tStart = t  # local t and not account for scr refresh
                e9Sound.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                e9Sound.status = STARTED
                e9Sound.play(when=win)  # sync with win flip
            
            # *e9Key* updates
            
            # if e9Key is starting this frame...
            if e9Key.status == NOT_STARTED and t >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                e9Key.frameNStart = frameN  # exact frame index
                e9Key.tStart = t  # local t and not account for scr refresh
                e9Key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e9Key, 'tStartRefresh')  # time at next scr refresh
                # update status
                e9Key.status = STARTED
                # keyboard checking is just starting
                e9Key.clock.reset()  # now t=0
            if e9Key.status == STARTED:
                theseKeys = e9Key.getKeys(keyList=['space'], waitRelease=False)
                _e9Key_allKeys.extend(theseKeys)
                if len(_e9Key_allKeys):
                    e9Key.keys = _e9Key_allKeys[-1].name  # just the last key pressed
                    e9Key.rt = _e9Key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *space24* updates
            
            # if space24 is starting this frame...
            if space24.status == NOT_STARTED and tThisFlip >= 3.2-frameTolerance:
                # keep track of start time/frame for later
                space24.frameNStart = frameN  # exact frame index
                space24.tStart = t  # local t and not account for scr refresh
                space24.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space24, 'tStartRefresh')  # time at next scr refresh
                # update status
                space24.status = STARTED
                space24.setAutoDraw(True)
            
            # if space24 is active this frame...
            if space24.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp9_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp9_2" ---
        for thisComponent in exp9_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from e9Code2
        if e9Count == 4:
            exp9Loop.finished = True
        else:
            pass
        e9Sound.stop()  # ensure sound has stopped at end of routine
        # the Routine "exp9_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'exp9Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    mini9Loop = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("orthostim_" + expInfo['group'] + ".xlsx", selection='16:20'),
        seed=None, name='mini9Loop')
    thisExp.addLoop(mini9Loop)  # add the loop to the experiment
    thisMini9Loop = mini9Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMini9Loop.rgb)
    if thisMini9Loop != None:
        for paramName in thisMini9Loop:
            exec('{} = thisMini9Loop[paramName]'.format(paramName))
    
    for thisMini9Loop in mini9Loop:
        currentLoop = mini9Loop
        # abbreviate parameter names if possible (e.g. rgb = thisMini9Loop.rgb)
        if thisMini9Loop != None:
            for paramName in thisMini9Loop:
                exec('{} = thisMini9Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mini9_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from m9Code1
        random.shuffle(m9Posi)
        m9PL.setText(plWord)
        m9CON.setPos([m9Posi[0]])
        m9CON.setText(conWord)
        # reset m9CON to account for continued clicks & clear times on/off
        m9CON.reset()
        m9DIST1.setPos([m9Posi[1]])
        m9DIST1.setText(incorr1)
        # reset m9DIST1 to account for continued clicks & clear times on/off
        m9DIST1.reset()
        m9DIST2.setPos([m9Posi[2]])
        m9DIST2.setText(incorr2)
        # reset m9DIST2 to account for continued clicks & clear times on/off
        m9DIST2.reset()
        m9DIST3.setPos([m9Posi[3]])
        m9DIST3.setText(incorr3)
        # reset m9DIST3 to account for continued clicks & clear times on/off
        m9DIST3.reset()
        # setup some python lists for storing info about the m9Mouse
        m9Mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        mini9_1Components = [m9PL, m9CON, m9DIST1, m9DIST2, m9DIST3, m9Mouse]
        for thisComponent in mini9_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mini9_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *m9PL* updates
            
            # if m9PL is starting this frame...
            if m9PL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m9PL.frameNStart = frameN  # exact frame index
                m9PL.tStart = t  # local t and not account for scr refresh
                m9PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m9PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                m9PL.status = STARTED
                m9PL.setAutoDraw(True)
            
            # if m9PL is active this frame...
            if m9PL.status == STARTED:
                # update params
                pass
            # *m9CON* updates
            
            # if m9CON is starting this frame...
            if m9CON.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m9CON.frameNStart = frameN  # exact frame index
                m9CON.tStart = t  # local t and not account for scr refresh
                m9CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m9CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                m9CON.status = STARTED
                m9CON.setAutoDraw(True)
            
            # if m9CON is active this frame...
            if m9CON.status == STARTED:
                # update params
                pass
                # check whether m9CON has been pressed
                if m9CON.isClicked:
                    if not m9CON.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m9CON.timesOn.append(m9CON.buttonClock.getTime())
                        m9CON.timesOff.append(m9CON.buttonClock.getTime())
                    elif len(m9CON.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m9CON.timesOff[-1] = m9CON.buttonClock.getTime()
                    if not m9CON.wasClicked:
                        # end routine when m9CON is clicked
                        continueRoutine = False
                    if not m9CON.wasClicked:
                        # run callback code when m9CON is clicked
                        pass
            # take note of whether m9CON was clicked, so that next frame we know if clicks are new
            m9CON.wasClicked = m9CON.isClicked and m9CON.status == STARTED
            # *m9DIST1* updates
            
            # if m9DIST1 is starting this frame...
            if m9DIST1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m9DIST1.frameNStart = frameN  # exact frame index
                m9DIST1.tStart = t  # local t and not account for scr refresh
                m9DIST1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m9DIST1, 'tStartRefresh')  # time at next scr refresh
                # update status
                m9DIST1.status = STARTED
                m9DIST1.setAutoDraw(True)
            
            # if m9DIST1 is active this frame...
            if m9DIST1.status == STARTED:
                # update params
                pass
                # check whether m9DIST1 has been pressed
                if m9DIST1.isClicked:
                    if not m9DIST1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m9DIST1.timesOn.append(m9DIST1.buttonClock.getTime())
                        m9DIST1.timesOff.append(m9DIST1.buttonClock.getTime())
                    elif len(m9DIST1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m9DIST1.timesOff[-1] = m9DIST1.buttonClock.getTime()
                    if not m9DIST1.wasClicked:
                        # end routine when m9DIST1 is clicked
                        continueRoutine = False
                    if not m9DIST1.wasClicked:
                        # run callback code when m9DIST1 is clicked
                        pass
            # take note of whether m9DIST1 was clicked, so that next frame we know if clicks are new
            m9DIST1.wasClicked = m9DIST1.isClicked and m9DIST1.status == STARTED
            # *m9DIST2* updates
            
            # if m9DIST2 is starting this frame...
            if m9DIST2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m9DIST2.frameNStart = frameN  # exact frame index
                m9DIST2.tStart = t  # local t and not account for scr refresh
                m9DIST2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m9DIST2, 'tStartRefresh')  # time at next scr refresh
                # update status
                m9DIST2.status = STARTED
                m9DIST2.setAutoDraw(True)
            
            # if m9DIST2 is active this frame...
            if m9DIST2.status == STARTED:
                # update params
                pass
                # check whether m9DIST2 has been pressed
                if m9DIST2.isClicked:
                    if not m9DIST2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m9DIST2.timesOn.append(m9DIST2.buttonClock.getTime())
                        m9DIST2.timesOff.append(m9DIST2.buttonClock.getTime())
                    elif len(m9DIST2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m9DIST2.timesOff[-1] = m9DIST2.buttonClock.getTime()
                    if not m9DIST2.wasClicked:
                        # end routine when m9DIST2 is clicked
                        continueRoutine = False
                    if not m9DIST2.wasClicked:
                        # run callback code when m9DIST2 is clicked
                        pass
            # take note of whether m9DIST2 was clicked, so that next frame we know if clicks are new
            m9DIST2.wasClicked = m9DIST2.isClicked and m9DIST2.status == STARTED
            # *m9DIST3* updates
            
            # if m9DIST3 is starting this frame...
            if m9DIST3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m9DIST3.frameNStart = frameN  # exact frame index
                m9DIST3.tStart = t  # local t and not account for scr refresh
                m9DIST3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m9DIST3, 'tStartRefresh')  # time at next scr refresh
                # update status
                m9DIST3.status = STARTED
                m9DIST3.setAutoDraw(True)
            
            # if m9DIST3 is active this frame...
            if m9DIST3.status == STARTED:
                # update params
                pass
                # check whether m9DIST3 has been pressed
                if m9DIST3.isClicked:
                    if not m9DIST3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m9DIST3.timesOn.append(m9DIST3.buttonClock.getTime())
                        m9DIST3.timesOff.append(m9DIST3.buttonClock.getTime())
                    elif len(m9DIST3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m9DIST3.timesOff[-1] = m9DIST3.buttonClock.getTime()
                    if not m9DIST3.wasClicked:
                        # end routine when m9DIST3 is clicked
                        continueRoutine = False
                    if not m9DIST3.wasClicked:
                        # run callback code when m9DIST3 is clicked
                        pass
            # take note of whether m9DIST3 was clicked, so that next frame we know if clicks are new
            m9DIST3.wasClicked = m9DIST3.isClicked and m9DIST3.status == STARTED
            # *m9Mouse* updates
            
            # if m9Mouse is starting this frame...
            if m9Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m9Mouse.frameNStart = frameN  # exact frame index
                m9Mouse.tStart = t  # local t and not account for scr refresh
                m9Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m9Mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'm9Mouse.started')
                # update status
                m9Mouse.status = STARTED
                m9Mouse.mouseClock.reset()
                prevButtonState = m9Mouse.getPressed()  # if button is down already this ISN'T a new click
            if m9Mouse.status == STARTED:  # only update if started and not finished!
                buttons = m9Mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = core.getFromNames([m9CON,m9DIST1,m9DIST2,m9DIST3])
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(m9Mouse):
                                gotValidClick = True
                                m9Mouse.clicked_name.append(obj.name)
                        continueRoutine = False  # end routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mini9_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mini9_1" ---
        for thisComponent in mini9_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from m9Code1
        if m9Mouse.isPressedIn(m9CON):
            nRepsM9Corr = True
            nRepsM9Incorr = False
            thisExp.addData("mCorr Response",m9CON.text)
        else:
            nRepsM9Corr = False
            nRepsM9Incorr = True
        
        if m9Mouse.isPressedIn(m9DIST1):
            incorrAns9=m9DIST1.text
            incorrPosi9=m9DIST1.pos
            thisExp.addData("mIncorr Repsonse",m9DIST1.text)
        elif m9Mouse.isPressedIn(m9DIST2):
            incorrAns9=m9DIST2.text
            incorrPosi9=m9DIST2.pos
            thisExp.addData("mIncorr Repsonse",m9DIST2.text)
        elif m9Mouse.isPressedIn(m9DIST3):
            incorrAns9=m9DIST3.text
            incorrPosi9=m9DIST3.pos
            thisExp.addData("mIncorr Repsonse",m9DIST3.text)
        # store data for mini9Loop (TrialHandler)
        # the Routine "mini9_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        m9CorrLoop = data.TrialHandler(nReps=nRepsM9Corr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m9CorrLoop')
        thisExp.addLoop(m9CorrLoop)  # add the loop to the experiment
        thisM9CorrLoop = m9CorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM9CorrLoop.rgb)
        if thisM9CorrLoop != None:
            for paramName in thisM9CorrLoop:
                exec('{} = thisM9CorrLoop[paramName]'.format(paramName))
        
        for thisM9CorrLoop in m9CorrLoop:
            currentLoop = m9CorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM9CorrLoop.rgb)
            if thisM9CorrLoop != None:
                for paramName in thisM9CorrLoop:
                    exec('{} = thisM9CorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini9_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m9Code2
            m9Count = m9Count+1
            m9CorrPL.setText(plWord)
            m9CorrCON.setPos([m9Posi[0]])
            m9CorrCON.setText(conWord)
            m9Sound1.setSound(audio, secs=2, hamming=True)
            m9Sound1.setVolume(3.0, log=False)
            m9Key1.keys = []
            m9Key1.rt = []
            _m9Key1_allKeys = []
            # keep track of which components have finished
            mini9_2Components = [m9CorrPL, m9CorrCON, m9Sound1, m9Key1, space25]
            for thisComponent in mini9_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini9_2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m9CorrPL* updates
                
                # if m9CorrPL is starting this frame...
                if m9CorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m9CorrPL.frameNStart = frameN  # exact frame index
                    m9CorrPL.tStart = t  # local t and not account for scr refresh
                    m9CorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m9CorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m9CorrPL.status = STARTED
                    m9CorrPL.setAutoDraw(True)
                
                # if m9CorrPL is active this frame...
                if m9CorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m9CorrCON* updates
                
                # if m9CorrCON is starting this frame...
                if m9CorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m9CorrCON.frameNStart = frameN  # exact frame index
                    m9CorrCON.tStart = t  # local t and not account for scr refresh
                    m9CorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m9CorrCON, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'm9CorrCON.started')
                    # update status
                    m9CorrCON.status = STARTED
                    m9CorrCON.setAutoDraw(True)
                
                # if m9CorrCON is active this frame...
                if m9CorrCON.status == STARTED:
                    # update params
                    pass
                # start/stop m9Sound1
                
                # if m9Sound1 is starting this frame...
                if m9Sound1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m9Sound1.frameNStart = frameN  # exact frame index
                    m9Sound1.tStart = t  # local t and not account for scr refresh
                    m9Sound1.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m9Sound1.status = STARTED
                    m9Sound1.play(when=win)  # sync with win flip
                
                # if m9Sound1 is stopping this frame...
                if m9Sound1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m9Sound1.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m9Sound1.tStop = t  # not accounting for scr refresh
                        m9Sound1.frameNStop = frameN  # exact frame index
                        # update status
                        m9Sound1.status = FINISHED
                        m9Sound1.stop()
                
                # *m9Key1* updates
                
                # if m9Key1 is starting this frame...
                if m9Key1.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m9Key1.frameNStart = frameN  # exact frame index
                    m9Key1.tStart = t  # local t and not account for scr refresh
                    m9Key1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m9Key1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m9Key1.status = STARTED
                    # keyboard checking is just starting
                    m9Key1.clock.reset()  # now t=0
                if m9Key1.status == STARTED:
                    theseKeys = m9Key1.getKeys(keyList=['space'], waitRelease=False)
                    _m9Key1_allKeys.extend(theseKeys)
                    if len(_m9Key1_allKeys):
                        m9Key1.keys = _m9Key1_allKeys[-1].name  # just the last key pressed
                        m9Key1.rt = _m9Key1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space25* updates
                
                # if space25 is starting this frame...
                if space25.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space25.frameNStart = frameN  # exact frame index
                    space25.tStart = t  # local t and not account for scr refresh
                    space25.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space25, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space25.status = STARTED
                    space25.setAutoDraw(True)
                
                # if space25 is active this frame...
                if space25.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini9_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini9_2" ---
            for thisComponent in mini9_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m9Code2
            if m9Count == 12:
                mini9Loop.finished = True
            m9Sound1.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini9_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM9Corr repeats of 'm9CorrLoop'
        
        
        # set up handler to look after randomisation of conditions etc
        m9IncorrLoop = data.TrialHandler(nReps=nRepsM9Incorr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m9IncorrLoop')
        thisExp.addLoop(m9IncorrLoop)  # add the loop to the experiment
        thisM9IncorrLoop = m9IncorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM9IncorrLoop.rgb)
        if thisM9IncorrLoop != None:
            for paramName in thisM9IncorrLoop:
                exec('{} = thisM9IncorrLoop[paramName]'.format(paramName))
        
        for thisM9IncorrLoop in m9IncorrLoop:
            currentLoop = m9IncorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM9IncorrLoop.rgb)
            if thisM9IncorrLoop != None:
                for paramName in thisM9IncorrLoop:
                    exec('{} = thisM9IncorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini9_3" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m9Code3
            m9Count = m9Count+1
            m9IncorrPL.setText(plWord)
            m9IncorrCON.setPos([m9Posi[0]])
            m9IncorrCON.setText(conWord)
            m9incorrDIST.setPos(incorrPosi9)
            m9incorrDIST.setText(incorrAns9)
            m9Sound2.setSound(audio, secs=2, hamming=True)
            m9Sound2.setVolume(3.0, log=False)
            m9Key2.keys = []
            m9Key2.rt = []
            _m9Key2_allKeys = []
            # keep track of which components have finished
            mini9_3Components = [m9IncorrPL, m9IncorrCON, m9incorrDIST, m9Sound2, m9Key2, space26]
            for thisComponent in mini9_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini9_3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m9IncorrPL* updates
                
                # if m9IncorrPL is starting this frame...
                if m9IncorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m9IncorrPL.frameNStart = frameN  # exact frame index
                    m9IncorrPL.tStart = t  # local t and not account for scr refresh
                    m9IncorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m9IncorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m9IncorrPL.status = STARTED
                    m9IncorrPL.setAutoDraw(True)
                
                # if m9IncorrPL is active this frame...
                if m9IncorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m9IncorrCON* updates
                
                # if m9IncorrCON is starting this frame...
                if m9IncorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m9IncorrCON.frameNStart = frameN  # exact frame index
                    m9IncorrCON.tStart = t  # local t and not account for scr refresh
                    m9IncorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m9IncorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m9IncorrCON.status = STARTED
                    m9IncorrCON.setAutoDraw(True)
                
                # if m9IncorrCON is active this frame...
                if m9IncorrCON.status == STARTED:
                    # update params
                    pass
                
                # *m9incorrDIST* updates
                
                # if m9incorrDIST is starting this frame...
                if m9incorrDIST.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m9incorrDIST.frameNStart = frameN  # exact frame index
                    m9incorrDIST.tStart = t  # local t and not account for scr refresh
                    m9incorrDIST.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m9incorrDIST, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m9incorrDIST.status = STARTED
                    m9incorrDIST.setAutoDraw(True)
                
                # if m9incorrDIST is active this frame...
                if m9incorrDIST.status == STARTED:
                    # update params
                    pass
                # start/stop m9Sound2
                
                # if m9Sound2 is starting this frame...
                if m9Sound2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m9Sound2.frameNStart = frameN  # exact frame index
                    m9Sound2.tStart = t  # local t and not account for scr refresh
                    m9Sound2.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m9Sound2.status = STARTED
                    m9Sound2.play(when=win)  # sync with win flip
                
                # if m9Sound2 is stopping this frame...
                if m9Sound2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m9Sound2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m9Sound2.tStop = t  # not accounting for scr refresh
                        m9Sound2.frameNStop = frameN  # exact frame index
                        # update status
                        m9Sound2.status = FINISHED
                        m9Sound2.stop()
                
                # *m9Key2* updates
                
                # if m9Key2 is starting this frame...
                if m9Key2.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m9Key2.frameNStart = frameN  # exact frame index
                    m9Key2.tStart = t  # local t and not account for scr refresh
                    m9Key2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m9Key2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m9Key2.status = STARTED
                    # keyboard checking is just starting
                    m9Key2.clock.reset()  # now t=0
                if m9Key2.status == STARTED:
                    theseKeys = m9Key2.getKeys(keyList=['space'], waitRelease=False)
                    _m9Key2_allKeys.extend(theseKeys)
                    if len(_m9Key2_allKeys):
                        m9Key2.keys = _m9Key2_allKeys[-1].name  # just the last key pressed
                        m9Key2.rt = _m9Key2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space26* updates
                
                # if space26 is starting this frame...
                if space26.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space26.frameNStart = frameN  # exact frame index
                    space26.tStart = t  # local t and not account for scr refresh
                    space26.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space26, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space26.status = STARTED
                    space26.setAutoDraw(True)
                
                # if space26 is active this frame...
                if space26.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini9_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini9_3" ---
            for thisComponent in mini9_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m9Code3
            if m9Count==12:
                mini9Loop.finished = True
            m9Sound2.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini9_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM9Incorr repeats of 'm9IncorrLoop'
        
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'mini9Loop'
    
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'ortho5'


# set up handler to look after randomisation of conditions etc
img5 = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='img5')
thisExp.addLoop(img5)  # add the loop to the experiment
thisImg5 = img5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisImg5.rgb)
if thisImg5 != None:
    for paramName in thisImg5:
        exec('{} = thisImg5[paramName]'.format(paramName))

for thisImg5 in img5:
    currentLoop = img5
    # abbreviate parameter names if possible (e.g. rgb = thisImg5.rgb)
    if thisImg5 != None:
        for paramName in thisImg5:
            exec('{} = thisImg5[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    exp0Loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("imgstim_"+expInfo['group']+".xlsx", selection='16:20'),
        seed=None, name='exp0Loop')
    thisExp.addLoop(exp0Loop)  # add the loop to the experiment
    thisExp0Loop = exp0Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExp0Loop.rgb)
    if thisExp0Loop != None:
        for paramName in thisExp0Loop:
            exec('{} = thisExp0Loop[paramName]'.format(paramName))
    
    for thisExp0Loop in exp0Loop:
        currentLoop = exp0Loop
        # abbreviate parameter names if possible (e.g. rgb = thisExp0Loop.rgb)
        if thisExp0Loop != None:
            for paramName in thisExp0Loop:
                exec('{} = thisExp0Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "exp10_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        e0PL.setImage(img)
        # keep track of which components have finished
        exp10_1Components = [e0Focal1, e0PL]
        for thisComponent in exp10_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp10_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.1:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e0Focal1* updates
            
            # if e0Focal1 is starting this frame...
            if e0Focal1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                e0Focal1.frameNStart = frameN  # exact frame index
                e0Focal1.tStart = t  # local t and not account for scr refresh
                e0Focal1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e0Focal1, 'tStartRefresh')  # time at next scr refresh
                # update status
                e0Focal1.status = STARTED
                e0Focal1.setAutoDraw(True)
            
            # if e0Focal1 is active this frame...
            if e0Focal1.status == STARTED:
                # update params
                pass
            
            # if e0Focal1 is stopping this frame...
            if e0Focal1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e0Focal1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    e0Focal1.tStop = t  # not accounting for scr refresh
                    e0Focal1.frameNStop = frameN  # exact frame index
                    # update status
                    e0Focal1.status = FINISHED
                    e0Focal1.setAutoDraw(False)
            
            # *e0PL* updates
            
            # if e0PL is starting this frame...
            if e0PL.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
                # keep track of start time/frame for later
                e0PL.frameNStart = frameN  # exact frame index
                e0PL.tStart = t  # local t and not account for scr refresh
                e0PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e0PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                e0PL.status = STARTED
                e0PL.setAutoDraw(True)
            
            # if e0PL is active this frame...
            if e0PL.status == STARTED:
                # update params
                pass
            
            # if e0PL is stopping this frame...
            if e0PL.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e0PL.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    e0PL.tStop = t  # not accounting for scr refresh
                    e0PL.frameNStop = frameN  # exact frame index
                    # update status
                    e0PL.status = FINISHED
                    e0PL.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp10_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp10_1" ---
        for thisComponent in exp10_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.100000)
        
        # --- Prepare to start Routine "exp10_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from e0Code2
        e0Count = e0Count+1
        e0CON.setText(conWord)
        e0Sound.setSound(audio, hamming=True)
        e0Sound.setVolume(3.0, log=False)
        e0Key.keys = []
        e0Key.rt = []
        _e0Key_allKeys = []
        # keep track of which components have finished
        exp10_2Components = [e0Focal2, e0CON, e0Sound, e0Key, space27]
        for thisComponent in exp10_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exp10_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *e0Focal2* updates
            
            # if e0Focal2 is starting this frame...
            if e0Focal2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                e0Focal2.frameNStart = frameN  # exact frame index
                e0Focal2.tStart = t  # local t and not account for scr refresh
                e0Focal2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e0Focal2, 'tStartRefresh')  # time at next scr refresh
                # update status
                e0Focal2.status = STARTED
                e0Focal2.setAutoDraw(True)
            
            # if e0Focal2 is active this frame...
            if e0Focal2.status == STARTED:
                # update params
                pass
            
            # if e0Focal2 is stopping this frame...
            if e0Focal2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > e0Focal2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    e0Focal2.tStop = t  # not accounting for scr refresh
                    e0Focal2.frameNStop = frameN  # exact frame index
                    # update status
                    e0Focal2.status = FINISHED
                    e0Focal2.setAutoDraw(False)
            
            # *e0CON* updates
            
            # if e0CON is starting this frame...
            if e0CON.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e0CON.frameNStart = frameN  # exact frame index
                e0CON.tStart = t  # local t and not account for scr refresh
                e0CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e0CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                e0CON.status = STARTED
                e0CON.setAutoDraw(True)
            
            # if e0CON is active this frame...
            if e0CON.status == STARTED:
                # update params
                pass
            # start/stop e0Sound
            
            # if e0Sound is starting this frame...
            if e0Sound.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                e0Sound.frameNStart = frameN  # exact frame index
                e0Sound.tStart = t  # local t and not account for scr refresh
                e0Sound.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                e0Sound.status = STARTED
                e0Sound.play(when=win)  # sync with win flip
            
            # *e0Key* updates
            
            # if e0Key is starting this frame...
            if e0Key.status == NOT_STARTED and t >= 2.2-frameTolerance:
                # keep track of start time/frame for later
                e0Key.frameNStart = frameN  # exact frame index
                e0Key.tStart = t  # local t and not account for scr refresh
                e0Key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(e0Key, 'tStartRefresh')  # time at next scr refresh
                # update status
                e0Key.status = STARTED
                # keyboard checking is just starting
                e0Key.clock.reset()  # now t=0
            if e0Key.status == STARTED:
                theseKeys = e0Key.getKeys(keyList=['space'], waitRelease=False)
                _e0Key_allKeys.extend(theseKeys)
                if len(_e0Key_allKeys):
                    e0Key.keys = _e0Key_allKeys[-1].name  # just the last key pressed
                    e0Key.rt = _e0Key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *space27* updates
            
            # if space27 is starting this frame...
            if space27.status == NOT_STARTED and tThisFlip >= 3.2-frameTolerance:
                # keep track of start time/frame for later
                space27.frameNStart = frameN  # exact frame index
                space27.tStart = t  # local t and not account for scr refresh
                space27.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space27, 'tStartRefresh')  # time at next scr refresh
                # update status
                space27.status = STARTED
                space27.setAutoDraw(True)
            
            # if space27 is active this frame...
            if space27.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exp10_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exp10_2" ---
        for thisComponent in exp10_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from e0Code2
        if e0Count ==4:
            exp0Loop.finished = True
        else:
            pass
        e0Sound.stop()  # ensure sound has stopped at end of routine
        # the Routine "exp10_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'exp0Loop'
    
    
    # set up handler to look after randomisation of conditions etc
    mini0Loop = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("imgstim_"+expInfo['group']+".xlsx", selection='16:20'),
        seed=None, name='mini0Loop')
    thisExp.addLoop(mini0Loop)  # add the loop to the experiment
    thisMini0Loop = mini0Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMini0Loop.rgb)
    if thisMini0Loop != None:
        for paramName in thisMini0Loop:
            exec('{} = thisMini0Loop[paramName]'.format(paramName))
    
    for thisMini0Loop in mini0Loop:
        currentLoop = mini0Loop
        # abbreviate parameter names if possible (e.g. rgb = thisMini0Loop.rgb)
        if thisMini0Loop != None:
            for paramName in thisMini0Loop:
                exec('{} = thisMini0Loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "mini10_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from m0Code1
        random.shuffle(m0Posi)
        m0PL.setImage(img)
        m0CON.setPos([m0Posi[0]])
        m0CON.setText(conWord)
        # reset m0CON to account for continued clicks & clear times on/off
        m0CON.reset()
        m0DIST1.setPos([m0Posi[1]])
        m0DIST1.setText(incorr1)
        # reset m0DIST1 to account for continued clicks & clear times on/off
        m0DIST1.reset()
        m0DIST2.setPos([m0Posi[2]])
        m0DIST2.setText(incorr2)
        # reset m0DIST2 to account for continued clicks & clear times on/off
        m0DIST2.reset()
        m0DIST3.setPos([m0Posi[3]])
        m0DIST3.setText(incorr3)
        # reset m0DIST3 to account for continued clicks & clear times on/off
        m0DIST3.reset()
        # setup some python lists for storing info about the m0Mouse
        m0Mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        mini10_1Components = [m0PL, m0CON, m0DIST1, m0DIST2, m0DIST3, m0Mouse]
        for thisComponent in mini10_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "mini10_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *m0PL* updates
            
            # if m0PL is starting this frame...
            if m0PL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m0PL.frameNStart = frameN  # exact frame index
                m0PL.tStart = t  # local t and not account for scr refresh
                m0PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m0PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                m0PL.status = STARTED
                m0PL.setAutoDraw(True)
            
            # if m0PL is active this frame...
            if m0PL.status == STARTED:
                # update params
                pass
            # *m0CON* updates
            
            # if m0CON is starting this frame...
            if m0CON.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m0CON.frameNStart = frameN  # exact frame index
                m0CON.tStart = t  # local t and not account for scr refresh
                m0CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m0CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                m0CON.status = STARTED
                m0CON.setAutoDraw(True)
            
            # if m0CON is active this frame...
            if m0CON.status == STARTED:
                # update params
                pass
                # check whether m0CON has been pressed
                if m0CON.isClicked:
                    if not m0CON.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m0CON.timesOn.append(m0CON.buttonClock.getTime())
                        m0CON.timesOff.append(m0CON.buttonClock.getTime())
                    elif len(m0CON.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m0CON.timesOff[-1] = m0CON.buttonClock.getTime()
                    if not m0CON.wasClicked:
                        # end routine when m0CON is clicked
                        continueRoutine = False
                    if not m0CON.wasClicked:
                        # run callback code when m0CON is clicked
                        pass
            # take note of whether m0CON was clicked, so that next frame we know if clicks are new
            m0CON.wasClicked = m0CON.isClicked and m0CON.status == STARTED
            # *m0DIST1* updates
            
            # if m0DIST1 is starting this frame...
            if m0DIST1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m0DIST1.frameNStart = frameN  # exact frame index
                m0DIST1.tStart = t  # local t and not account for scr refresh
                m0DIST1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m0DIST1, 'tStartRefresh')  # time at next scr refresh
                # update status
                m0DIST1.status = STARTED
                m0DIST1.setAutoDraw(True)
            
            # if m0DIST1 is active this frame...
            if m0DIST1.status == STARTED:
                # update params
                pass
                # check whether m0DIST1 has been pressed
                if m0DIST1.isClicked:
                    if not m0DIST1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m0DIST1.timesOn.append(m0DIST1.buttonClock.getTime())
                        m0DIST1.timesOff.append(m0DIST1.buttonClock.getTime())
                    elif len(m0DIST1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m0DIST1.timesOff[-1] = m0DIST1.buttonClock.getTime()
                    if not m0DIST1.wasClicked:
                        # end routine when m0DIST1 is clicked
                        continueRoutine = False
                    if not m0DIST1.wasClicked:
                        # run callback code when m0DIST1 is clicked
                        pass
            # take note of whether m0DIST1 was clicked, so that next frame we know if clicks are new
            m0DIST1.wasClicked = m0DIST1.isClicked and m0DIST1.status == STARTED
            # *m0DIST2* updates
            
            # if m0DIST2 is starting this frame...
            if m0DIST2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m0DIST2.frameNStart = frameN  # exact frame index
                m0DIST2.tStart = t  # local t and not account for scr refresh
                m0DIST2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m0DIST2, 'tStartRefresh')  # time at next scr refresh
                # update status
                m0DIST2.status = STARTED
                m0DIST2.setAutoDraw(True)
            
            # if m0DIST2 is active this frame...
            if m0DIST2.status == STARTED:
                # update params
                pass
                # check whether m0DIST2 has been pressed
                if m0DIST2.isClicked:
                    if not m0DIST2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m0DIST2.timesOn.append(m0DIST2.buttonClock.getTime())
                        m0DIST2.timesOff.append(m0DIST2.buttonClock.getTime())
                    elif len(m0DIST2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m0DIST2.timesOff[-1] = m0DIST2.buttonClock.getTime()
                    if not m0DIST2.wasClicked:
                        # end routine when m0DIST2 is clicked
                        continueRoutine = False
                    if not m0DIST2.wasClicked:
                        # run callback code when m0DIST2 is clicked
                        pass
            # take note of whether m0DIST2 was clicked, so that next frame we know if clicks are new
            m0DIST2.wasClicked = m0DIST2.isClicked and m0DIST2.status == STARTED
            # *m0DIST3* updates
            
            # if m0DIST3 is starting this frame...
            if m0DIST3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                m0DIST3.frameNStart = frameN  # exact frame index
                m0DIST3.tStart = t  # local t and not account for scr refresh
                m0DIST3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m0DIST3, 'tStartRefresh')  # time at next scr refresh
                # update status
                m0DIST3.status = STARTED
                m0DIST3.setAutoDraw(True)
            
            # if m0DIST3 is active this frame...
            if m0DIST3.status == STARTED:
                # update params
                pass
                # check whether m0DIST3 has been pressed
                if m0DIST3.isClicked:
                    if not m0DIST3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        m0DIST3.timesOn.append(m0DIST3.buttonClock.getTime())
                        m0DIST3.timesOff.append(m0DIST3.buttonClock.getTime())
                    elif len(m0DIST3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        m0DIST3.timesOff[-1] = m0DIST3.buttonClock.getTime()
                    if not m0DIST3.wasClicked:
                        # end routine when m0DIST3 is clicked
                        continueRoutine = False
                    if not m0DIST3.wasClicked:
                        # run callback code when m0DIST3 is clicked
                        pass
            # take note of whether m0DIST3 was clicked, so that next frame we know if clicks are new
            m0DIST3.wasClicked = m0DIST3.isClicked and m0DIST3.status == STARTED
            # *m0Mouse* updates
            
            # if m0Mouse is starting this frame...
            if m0Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                m0Mouse.frameNStart = frameN  # exact frame index
                m0Mouse.tStart = t  # local t and not account for scr refresh
                m0Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(m0Mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'm0Mouse.started')
                # update status
                m0Mouse.status = STARTED
                m0Mouse.mouseClock.reset()
                prevButtonState = m0Mouse.getPressed()  # if button is down already this ISN'T a new click
            if m0Mouse.status == STARTED:  # only update if started and not finished!
                buttons = m0Mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = core.getFromNames([m0CON,m0DIST1,m0DIST2,m0DIST3])
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(m0Mouse):
                                gotValidClick = True
                                m0Mouse.clicked_name.append(obj.name)
                        continueRoutine = False  # end routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in mini10_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "mini10_1" ---
        for thisComponent in mini10_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from m0Code1
        if m0Mouse.isPressedIn(m0CON):
            nRepsM0Corr = True
            nRepsM0Incorr = False
            thisExp.addData("mCorr Response",m0CON.text)
        else:
            nRepsM0Corr = False
            nRepsM0Incorr = True
        
        if m0Mouse.isPressedIn(m0DIST1):
            incorrAns0=m0DIST1.text
            incorrPosi0=m0DIST1.pos
            thisExp.addData("mIncorr Repsonse",m0DIST1.text)
        elif m0Mouse.isPressedIn(m0DIST2):
            incorrAns0=m0DIST2.text
            incorrPosi0=m0DIST2.pos
            thisExp.addData("mIncorr Repsonse",m0DIST2.text)
        elif m0Mouse.isPressedIn(m0DIST3):
            incorrAns0=m0DIST3.text
            incorrPosi0=m0DIST3.pos
            thisExp.addData("mIncorr Repsonse",m0DIST3.text)
        # store data for mini0Loop (TrialHandler)
        # the Routine "mini10_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        m0CorrLoop = data.TrialHandler(nReps=nRepsM0Corr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m0CorrLoop')
        thisExp.addLoop(m0CorrLoop)  # add the loop to the experiment
        thisM0CorrLoop = m0CorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM0CorrLoop.rgb)
        if thisM0CorrLoop != None:
            for paramName in thisM0CorrLoop:
                exec('{} = thisM0CorrLoop[paramName]'.format(paramName))
        
        for thisM0CorrLoop in m0CorrLoop:
            currentLoop = m0CorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM0CorrLoop.rgb)
            if thisM0CorrLoop != None:
                for paramName in thisM0CorrLoop:
                    exec('{} = thisM0CorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini10_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m0Code2
            m0Count = m0Count+1
            m0CorrPL.setImage(img)
            m0CorrCON.setPos([m0Posi[0]])
            m0CorrCON.setText(conWord)
            m0Sound1.setSound(audio, secs=2, hamming=True)
            m0Sound1.setVolume(3.0, log=False)
            m0Key1.keys = []
            m0Key1.rt = []
            _m0Key1_allKeys = []
            # keep track of which components have finished
            mini10_2Components = [m0CorrPL, m0CorrCON, m0Sound1, m0Key1, space28]
            for thisComponent in mini10_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini10_2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m0CorrPL* updates
                
                # if m0CorrPL is starting this frame...
                if m0CorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m0CorrPL.frameNStart = frameN  # exact frame index
                    m0CorrPL.tStart = t  # local t and not account for scr refresh
                    m0CorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m0CorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m0CorrPL.status = STARTED
                    m0CorrPL.setAutoDraw(True)
                
                # if m0CorrPL is active this frame...
                if m0CorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m0CorrCON* updates
                
                # if m0CorrCON is starting this frame...
                if m0CorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m0CorrCON.frameNStart = frameN  # exact frame index
                    m0CorrCON.tStart = t  # local t and not account for scr refresh
                    m0CorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m0CorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m0CorrCON.status = STARTED
                    m0CorrCON.setAutoDraw(True)
                
                # if m0CorrCON is active this frame...
                if m0CorrCON.status == STARTED:
                    # update params
                    pass
                # start/stop m0Sound1
                
                # if m0Sound1 is starting this frame...
                if m0Sound1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m0Sound1.frameNStart = frameN  # exact frame index
                    m0Sound1.tStart = t  # local t and not account for scr refresh
                    m0Sound1.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m0Sound1.status = STARTED
                    m0Sound1.play(when=win)  # sync with win flip
                
                # if m0Sound1 is stopping this frame...
                if m0Sound1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m0Sound1.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m0Sound1.tStop = t  # not accounting for scr refresh
                        m0Sound1.frameNStop = frameN  # exact frame index
                        # update status
                        m0Sound1.status = FINISHED
                        m0Sound1.stop()
                
                # *m0Key1* updates
                
                # if m0Key1 is starting this frame...
                if m0Key1.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m0Key1.frameNStart = frameN  # exact frame index
                    m0Key1.tStart = t  # local t and not account for scr refresh
                    m0Key1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m0Key1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m0Key1.status = STARTED
                    # keyboard checking is just starting
                    m0Key1.clock.reset()  # now t=0
                if m0Key1.status == STARTED:
                    theseKeys = m0Key1.getKeys(keyList=['space'], waitRelease=False)
                    _m0Key1_allKeys.extend(theseKeys)
                    if len(_m0Key1_allKeys):
                        m0Key1.keys = _m0Key1_allKeys[-1].name  # just the last key pressed
                        m0Key1.rt = _m0Key1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space28* updates
                
                # if space28 is starting this frame...
                if space28.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space28.frameNStart = frameN  # exact frame index
                    space28.tStart = t  # local t and not account for scr refresh
                    space28.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space28, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space28.status = STARTED
                    space28.setAutoDraw(True)
                
                # if space28 is active this frame...
                if space28.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini10_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini10_2" ---
            for thisComponent in mini10_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m0Code2
            if m0Count == 12:
                mini0Loop.finished = True
            m0Sound1.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini10_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM0Corr repeats of 'm0CorrLoop'
        
        
        # set up handler to look after randomisation of conditions etc
        m0IncorrLoop = data.TrialHandler(nReps=nRepsM0Incorr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='m0IncorrLoop')
        thisExp.addLoop(m0IncorrLoop)  # add the loop to the experiment
        thisM0IncorrLoop = m0IncorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisM0IncorrLoop.rgb)
        if thisM0IncorrLoop != None:
            for paramName in thisM0IncorrLoop:
                exec('{} = thisM0IncorrLoop[paramName]'.format(paramName))
        
        for thisM0IncorrLoop in m0IncorrLoop:
            currentLoop = m0IncorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisM0IncorrLoop.rgb)
            if thisM0IncorrLoop != None:
                for paramName in thisM0IncorrLoop:
                    exec('{} = thisM0IncorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "mini10_3" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from m0Code3
            m0Count = m0Count+1
            m0IncorrPL.setImage(img)
            m0IncorrCON.setPos([m0Posi[0]])
            m0IncorrCON.setText(conWord)
            m0IncorrDIST.setPos(incorrPosi0)
            m0IncorrDIST.setText(incorrAns0)
            m0Sound2.setSound(audio, secs=2, hamming=True)
            m0Sound2.setVolume(3.0, log=False)
            m0Key2.keys = []
            m0Key2.rt = []
            _m0Key2_allKeys = []
            # keep track of which components have finished
            mini10_3Components = [m0IncorrPL, m0IncorrCON, m0IncorrDIST, m0Sound2, m0Key2, space29]
            for thisComponent in mini10_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mini10_3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *m0IncorrPL* updates
                
                # if m0IncorrPL is starting this frame...
                if m0IncorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m0IncorrPL.frameNStart = frameN  # exact frame index
                    m0IncorrPL.tStart = t  # local t and not account for scr refresh
                    m0IncorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m0IncorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m0IncorrPL.status = STARTED
                    m0IncorrPL.setAutoDraw(True)
                
                # if m0IncorrPL is active this frame...
                if m0IncorrPL.status == STARTED:
                    # update params
                    pass
                
                # *m0IncorrCON* updates
                
                # if m0IncorrCON is starting this frame...
                if m0IncorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m0IncorrCON.frameNStart = frameN  # exact frame index
                    m0IncorrCON.tStart = t  # local t and not account for scr refresh
                    m0IncorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m0IncorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m0IncorrCON.status = STARTED
                    m0IncorrCON.setAutoDraw(True)
                
                # if m0IncorrCON is active this frame...
                if m0IncorrCON.status == STARTED:
                    # update params
                    pass
                
                # *m0IncorrDIST* updates
                
                # if m0IncorrDIST is starting this frame...
                if m0IncorrDIST.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m0IncorrDIST.frameNStart = frameN  # exact frame index
                    m0IncorrDIST.tStart = t  # local t and not account for scr refresh
                    m0IncorrDIST.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m0IncorrDIST, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m0IncorrDIST.status = STARTED
                    m0IncorrDIST.setAutoDraw(True)
                
                # if m0IncorrDIST is active this frame...
                if m0IncorrDIST.status == STARTED:
                    # update params
                    pass
                # start/stop m0Sound2
                
                # if m0Sound2 is starting this frame...
                if m0Sound2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    m0Sound2.frameNStart = frameN  # exact frame index
                    m0Sound2.tStart = t  # local t and not account for scr refresh
                    m0Sound2.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    m0Sound2.status = STARTED
                    m0Sound2.play(when=win)  # sync with win flip
                
                # if m0Sound2 is stopping this frame...
                if m0Sound2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > m0Sound2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        m0Sound2.tStop = t  # not accounting for scr refresh
                        m0Sound2.frameNStop = frameN  # exact frame index
                        # update status
                        m0Sound2.status = FINISHED
                        m0Sound2.stop()
                
                # *m0Key2* updates
                
                # if m0Key2 is starting this frame...
                if m0Key2.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    m0Key2.frameNStart = frameN  # exact frame index
                    m0Key2.tStart = t  # local t and not account for scr refresh
                    m0Key2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(m0Key2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    m0Key2.status = STARTED
                    # keyboard checking is just starting
                    m0Key2.clock.reset()  # now t=0
                if m0Key2.status == STARTED:
                    theseKeys = m0Key2.getKeys(keyList=['space'], waitRelease=False)
                    _m0Key2_allKeys.extend(theseKeys)
                    if len(_m0Key2_allKeys):
                        m0Key2.keys = _m0Key2_allKeys[-1].name  # just the last key pressed
                        m0Key2.rt = _m0Key2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space29* updates
                
                # if space29 is starting this frame...
                if space29.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space29.frameNStart = frameN  # exact frame index
                    space29.tStart = t  # local t and not account for scr refresh
                    space29.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space29, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space29.status = STARTED
                    space29.setAutoDraw(True)
                
                # if space29 is active this frame...
                if space29.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mini10_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mini10_3" ---
            for thisComponent in mini10_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from m0Code3
            if m0Count==12:
                mini0Loop.finished = True
            m0Sound2.stop()  # ensure sound has stopped at end of routine
            # the Routine "mini10_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsM0Incorr repeats of 'm0IncorrLoop'
        
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'mini0Loop'
    
    
    # --- Prepare to start Routine "learnTimer_End" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from timer2
    #learnEnd = timer()
    # keep track of which components have finished
    learnTimer_EndComponents = []
    for thisComponent in learnTimer_EndComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "learnTimer_End" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTimer_EndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "learnTimer_End" ---
    for thisComponent in learnTimer_EndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from timer2
    
    #learnTotal = learnEnd - learnStart
    
    #thisExp.addData("Learning/Exposure Time", learnTotal)
    # the Routine "learnTimer_End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'img5'


# --- Prepare to start Routine "instruction9" ---
continueRoutine = True
# update component parameters for each repeat
iKey1_3.keys = []
iKey1_3.rt = []
_iKey1_3_allKeys = []
# keep track of which components have finished
instruction9Components = [iText1_3, iKey1_3]
for thisComponent in instruction9Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instruction9" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *iText1_3* updates
    
    # if iText1_3 is starting this frame...
    if iText1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iText1_3.frameNStart = frameN  # exact frame index
        iText1_3.tStart = t  # local t and not account for scr refresh
        iText1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iText1_3, 'tStartRefresh')  # time at next scr refresh
        # update status
        iText1_3.status = STARTED
        iText1_3.setAutoDraw(True)
    
    # if iText1_3 is active this frame...
    if iText1_3.status == STARTED:
        # update params
        pass
    
    # *iKey1_3* updates
    
    # if iKey1_3 is starting this frame...
    if iKey1_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iKey1_3.frameNStart = frameN  # exact frame index
        iKey1_3.tStart = t  # local t and not account for scr refresh
        iKey1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iKey1_3, 'tStartRefresh')  # time at next scr refresh
        # update status
        iKey1_3.status = STARTED
        # keyboard checking is just starting
        iKey1_3.clock.reset()  # now t=0
    if iKey1_3.status == STARTED:
        theseKeys = iKey1_3.getKeys(keyList=['space'], waitRelease=False)
        _iKey1_3_allKeys.extend(theseKeys)
        if len(_iKey1_3_allKeys):
            iKey1_3.keys = _iKey1_3_allKeys[-1].name  # just the last key pressed
            iKey1_3.rt = _iKey1_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction9" ---
for thisComponent in instruction9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction9" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
timerLoop = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='timerLoop')
thisExp.addLoop(timerLoop)  # add the loop to the experiment
thisTimerLoop = timerLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTimerLoop.rgb)
if thisTimerLoop != None:
    for paramName in thisTimerLoop:
        exec('{} = thisTimerLoop[paramName]'.format(paramName))

for thisTimerLoop in timerLoop:
    currentLoop = timerLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTimerLoop.rgb)
    if thisTimerLoop != None:
        for paramName in thisTimerLoop:
            exec('{} = thisTimerLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "routine_5_minute_break" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from timer
    if timerLoop.thisN == 0:
        task_timer = core.CountdownTimer(start = 300) # duration in seconds
    # keep track of which components have finished
    routine_5_minute_breakComponents = [timer_text]
    for thisComponent in routine_5_minute_breakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_5_minute_break" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from timer
        # end task after 5 min:
        time_left = task_timer.getTime()
        
        # optional - only needed if you want to display these to the subject:
        minutes = int(time_left/60)
        seconds = int(time_left - minutes * 60)
        
        if time_left <= 0.0:
            timerLoop.finished = True
            continueRoutine = False
        
        # *timer_text* updates
        
        # if timer_text is starting this frame...
        if timer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_text.frameNStart = frameN  # exact frame index
            timer_text.tStart = t  # local t and not account for scr refresh
            timer_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            timer_text.status = STARTED
            timer_text.setAutoDraw(True)
        
        # if timer_text is active this frame...
        if timer_text.status == STARTED:
            # update params
            timer_text.setText(f'{minutes}:{seconds}', log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_5_minute_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_5_minute_break" ---
    for thisComponent in routine_5_minute_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "routine_5_minute_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'timerLoop'


# --- Prepare to start Routine "instructions10" ---
continueRoutine = True
# update component parameters for each repeat
iKey1_4.keys = []
iKey1_4.rt = []
_iKey1_4_allKeys = []
# keep track of which components have finished
instructions10Components = [iText1_4, iKey1_4]
for thisComponent in instructions10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions10" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *iText1_4* updates
    
    # if iText1_4 is starting this frame...
    if iText1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iText1_4.frameNStart = frameN  # exact frame index
        iText1_4.tStart = t  # local t and not account for scr refresh
        iText1_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iText1_4, 'tStartRefresh')  # time at next scr refresh
        # update status
        iText1_4.status = STARTED
        iText1_4.setAutoDraw(True)
    
    # if iText1_4 is active this frame...
    if iText1_4.status == STARTED:
        # update params
        pass
    
    # *iKey1_4* updates
    
    # if iKey1_4 is starting this frame...
    if iKey1_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iKey1_4.frameNStart = frameN  # exact frame index
        iKey1_4.tStart = t  # local t and not account for scr refresh
        iKey1_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iKey1_4, 'tStartRefresh')  # time at next scr refresh
        # update status
        iKey1_4.status = STARTED
        # keyboard checking is just starting
        iKey1_4.clock.reset()  # now t=0
    if iKey1_4.status == STARTED:
        theseKeys = iKey1_4.getKeys(keyList=['space'], waitRelease=False)
        _iKey1_4_allKeys.extend(theseKeys)
        if len(_iKey1_4_allKeys):
            iKey1_4.keys = _iKey1_4_allKeys[-1].name  # just the last key pressed
            iKey1_4.rt = _iKey1_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions10" ---
for thisComponent in instructions10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
bigAFC = data.TrialHandler(nReps=30000.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='bigAFC')
thisExp.addLoop(bigAFC)  # add the loop to the experiment
thisBigAFC = bigAFC.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBigAFC.rgb)
if thisBigAFC != None:
    for paramName in thisBigAFC:
        exec('{} = thisBigAFC[paramName]'.format(paramName))

for thisBigAFC in bigAFC:
    currentLoop = bigAFC
    # abbreviate parameter names if possible (e.g. rgb = thisBigAFC.rgb)
    if thisBigAFC != None:
        for paramName in thisBigAFC:
            exec('{} = thisBigAFC[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "afcRoute_Code" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from afcRoutingCode
    choice = random.choice([0,1])
    # keep track of which components have finished
    afcRoute_CodeComponents = []
    for thisComponent in afcRoute_CodeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "afcRoute_Code" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in afcRoute_CodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "afcRoute_Code" ---
    for thisComponent in afcRoute_CodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from afcRoutingCode
    if choice == 0 and orthoRep != 20:
        nRepsAfcOrtho = True
        nRepsAfcImg = False
    elif choice == 0 and orthoRep == 20:
        nRepsAfcOrtho = False
        nRepsAfcImg = True
    elif choice == 1 and imgRep != 20:
        nRepsAfcOrtho = False
        nRepsAfcImg = True
    elif choice == 1 and imgRep == 20:
        nRepsAfcOrtho = True
        nRepsAfcImg = False
    elif choice == 1 or choice == 0 and orthoRep ==20 and imgRep ==20:
        continueRoutine = False
    # the Routine "afcRoute_Code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    afcOrtho = data.TrialHandler(nReps=nRepsAfcOrtho, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("orthostim_" + expInfo['group'] + ".xlsx", selection=str(orthoRep) + ':' + str(orthoRep + 1)),
        seed=None, name='afcOrtho')
    thisExp.addLoop(afcOrtho)  # add the loop to the experiment
    thisAfcOrtho = afcOrtho.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAfcOrtho.rgb)
    if thisAfcOrtho != None:
        for paramName in thisAfcOrtho:
            exec('{} = thisAfcOrtho[paramName]'.format(paramName))
    
    for thisAfcOrtho in afcOrtho:
        currentLoop = afcOrtho
        # abbreviate parameter names if possible (e.g. rgb = thisAfcOrtho.rgb)
        if thisAfcOrtho != None:
            for paramName in thisAfcOrtho:
                exec('{} = thisAfcOrtho[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "afc1_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from a1Code1
        if orthoRep == 20:
            afcOrtho.finished = True
        else:
            afcOrtho.finished = False
            
        thisExp.addData("repetitions",totalCount)
        
        random.shuffle(a1Posi)
        
        a1PL.setText(plWord)
        a1CON.setPos([a1Posi[0]])
        a1CON.setText(conWord)
        # reset a1CON to account for continued clicks & clear times on/off
        a1CON.reset()
        a1DIST1.setPos([a1Posi[1]])
        a1DIST1.setText(incorr1)
        # reset a1DIST1 to account for continued clicks & clear times on/off
        a1DIST1.reset()
        a1DIST2.setPos([a1Posi[2]])
        a1DIST2.setText(incorr2)
        # reset a1DIST2 to account for continued clicks & clear times on/off
        a1DIST2.reset()
        a1DIST3.setPos([a1Posi[3]])
        a1DIST3.setText(incorr3)
        # reset a1DIST3 to account for continued clicks & clear times on/off
        a1DIST3.reset()
        # setup some python lists for storing info about the a1Mouse
        a1Mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        afc1_1Components = [a1PL, a1CON, a1DIST1, a1DIST2, a1DIST3, a1Mouse]
        for thisComponent in afc1_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "afc1_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *a1PL* updates
            
            # if a1PL is starting this frame...
            if a1PL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                a1PL.frameNStart = frameN  # exact frame index
                a1PL.tStart = t  # local t and not account for scr refresh
                a1PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a1PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                a1PL.status = STARTED
                a1PL.setAutoDraw(True)
            
            # if a1PL is active this frame...
            if a1PL.status == STARTED:
                # update params
                pass
            # *a1CON* updates
            
            # if a1CON is starting this frame...
            if a1CON.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                a1CON.frameNStart = frameN  # exact frame index
                a1CON.tStart = t  # local t and not account for scr refresh
                a1CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a1CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                a1CON.status = STARTED
                a1CON.setAutoDraw(True)
            
            # if a1CON is active this frame...
            if a1CON.status == STARTED:
                # update params
                pass
                # check whether a1CON has been pressed
                if a1CON.isClicked:
                    if not a1CON.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        a1CON.timesOn.append(a1CON.buttonClock.getTime())
                        a1CON.timesOff.append(a1CON.buttonClock.getTime())
                    elif len(a1CON.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        a1CON.timesOff[-1] = a1CON.buttonClock.getTime()
                    if not a1CON.wasClicked:
                        # end routine when a1CON is clicked
                        continueRoutine = False
                    if not a1CON.wasClicked:
                        # run callback code when a1CON is clicked
                        pass
            # take note of whether a1CON was clicked, so that next frame we know if clicks are new
            a1CON.wasClicked = a1CON.isClicked and a1CON.status == STARTED
            # *a1DIST1* updates
            
            # if a1DIST1 is starting this frame...
            if a1DIST1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                a1DIST1.frameNStart = frameN  # exact frame index
                a1DIST1.tStart = t  # local t and not account for scr refresh
                a1DIST1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a1DIST1, 'tStartRefresh')  # time at next scr refresh
                # update status
                a1DIST1.status = STARTED
                a1DIST1.setAutoDraw(True)
            
            # if a1DIST1 is active this frame...
            if a1DIST1.status == STARTED:
                # update params
                pass
                # check whether a1DIST1 has been pressed
                if a1DIST1.isClicked:
                    if not a1DIST1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        a1DIST1.timesOn.append(a1DIST1.buttonClock.getTime())
                        a1DIST1.timesOff.append(a1DIST1.buttonClock.getTime())
                    elif len(a1DIST1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        a1DIST1.timesOff[-1] = a1DIST1.buttonClock.getTime()
                    if not a1DIST1.wasClicked:
                        # end routine when a1DIST1 is clicked
                        continueRoutine = False
                    if not a1DIST1.wasClicked:
                        # run callback code when a1DIST1 is clicked
                        pass
            # take note of whether a1DIST1 was clicked, so that next frame we know if clicks are new
            a1DIST1.wasClicked = a1DIST1.isClicked and a1DIST1.status == STARTED
            # *a1DIST2* updates
            
            # if a1DIST2 is starting this frame...
            if a1DIST2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                a1DIST2.frameNStart = frameN  # exact frame index
                a1DIST2.tStart = t  # local t and not account for scr refresh
                a1DIST2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a1DIST2, 'tStartRefresh')  # time at next scr refresh
                # update status
                a1DIST2.status = STARTED
                a1DIST2.setAutoDraw(True)
            
            # if a1DIST2 is active this frame...
            if a1DIST2.status == STARTED:
                # update params
                pass
                # check whether a1DIST2 has been pressed
                if a1DIST2.isClicked:
                    if not a1DIST2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        a1DIST2.timesOn.append(a1DIST2.buttonClock.getTime())
                        a1DIST2.timesOff.append(a1DIST2.buttonClock.getTime())
                    elif len(a1DIST2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        a1DIST2.timesOff[-1] = a1DIST2.buttonClock.getTime()
                    if not a1DIST2.wasClicked:
                        # end routine when a1DIST2 is clicked
                        continueRoutine = False
                    if not a1DIST2.wasClicked:
                        # run callback code when a1DIST2 is clicked
                        pass
            # take note of whether a1DIST2 was clicked, so that next frame we know if clicks are new
            a1DIST2.wasClicked = a1DIST2.isClicked and a1DIST2.status == STARTED
            # *a1DIST3* updates
            
            # if a1DIST3 is starting this frame...
            if a1DIST3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                a1DIST3.frameNStart = frameN  # exact frame index
                a1DIST3.tStart = t  # local t and not account for scr refresh
                a1DIST3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a1DIST3, 'tStartRefresh')  # time at next scr refresh
                # update status
                a1DIST3.status = STARTED
                a1DIST3.setAutoDraw(True)
            
            # if a1DIST3 is active this frame...
            if a1DIST3.status == STARTED:
                # update params
                pass
                # check whether a1DIST3 has been pressed
                if a1DIST3.isClicked:
                    if not a1DIST3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        a1DIST3.timesOn.append(a1DIST3.buttonClock.getTime())
                        a1DIST3.timesOff.append(a1DIST3.buttonClock.getTime())
                    elif len(a1DIST3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        a1DIST3.timesOff[-1] = a1DIST3.buttonClock.getTime()
                    if not a1DIST3.wasClicked:
                        # end routine when a1DIST3 is clicked
                        continueRoutine = False
                    if not a1DIST3.wasClicked:
                        # run callback code when a1DIST3 is clicked
                        pass
            # take note of whether a1DIST3 was clicked, so that next frame we know if clicks are new
            a1DIST3.wasClicked = a1DIST3.isClicked and a1DIST3.status == STARTED
            # *a1Mouse* updates
            
            # if a1Mouse is starting this frame...
            if a1Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                a1Mouse.frameNStart = frameN  # exact frame index
                a1Mouse.tStart = t  # local t and not account for scr refresh
                a1Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a1Mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'a1Mouse.started')
                # update status
                a1Mouse.status = STARTED
                a1Mouse.mouseClock.reset()
                prevButtonState = a1Mouse.getPressed()  # if button is down already this ISN'T a new click
            if a1Mouse.status == STARTED:  # only update if started and not finished!
                buttons = a1Mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = core.getFromNames([a1CON,a1DIST1,a1DIST2,a1DIST3])
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(a1Mouse):
                                gotValidClick = True
                                a1Mouse.clicked_name.append(obj.name)
                        continueRoutine = False  # end routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in afc1_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "afc1_1" ---
        for thisComponent in afc1_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from a1Code1
        totalCount = totalCount+1
        
        if a1Mouse.isPressedIn(a1CON):
            nRepsA1Corr = 1
            nRepsA1Incorr = 0
            thisExp.addData("Corr Response",a1CON.text)
        else:
            nRepsA1Corr = 0
            nRepsA1Incorr = 1
        
        if a1Mouse.isPressedIn(a1DIST1):
            incorrAns00=a1DIST1.text
            incorrPosi00=a1DIST1.pos
            thisExp.addData("Incorr Response",a1DIST1.text)
        elif a1Mouse.isPressedIn(a1DIST2):
            incorrAns00=a1DIST2.text
            incorrPosi00=a1DIST2.pos
            thisExp.addData("Incorr Repsonse",a1DIST2.text)
        elif a1Mouse.isPressedIn(a1DIST3):
            incorrAns00=a1DIST3.text
            incorrPosi00=a1DIST3.pos
            thisExp.addData("Incorr Repsonse",a1DIST3.text)
        # store data for afcOrtho (TrialHandler)
        # the Routine "afc1_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        afc1CorrLoop = data.TrialHandler(nReps=nRepsA1Corr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='afc1CorrLoop')
        thisExp.addLoop(afc1CorrLoop)  # add the loop to the experiment
        thisAfc1CorrLoop = afc1CorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAfc1CorrLoop.rgb)
        if thisAfc1CorrLoop != None:
            for paramName in thisAfc1CorrLoop:
                exec('{} = thisAfc1CorrLoop[paramName]'.format(paramName))
        
        for thisAfc1CorrLoop in afc1CorrLoop:
            currentLoop = afc1CorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisAfc1CorrLoop.rgb)
            if thisAfc1CorrLoop != None:
                for paramName in thisAfc1CorrLoop:
                    exec('{} = thisAfc1CorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "afc1_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            a1CORRPL.setText(plWord)
            a1CorrCON.setPos([a1Posi[0]])
            a1CorrCON.setText(conWord)
            a1Sound1.setSound(audio, secs=2, hamming=True)
            a1Sound1.setVolume(3.0, log=False)
            a1Key1.keys = []
            a1Key1.rt = []
            _a1Key1_allKeys = []
            # keep track of which components have finished
            afc1_2Components = [a1CORRPL, a1CorrCON, a1Sound1, a1Key1, space30]
            for thisComponent in afc1_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "afc1_2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *a1CORRPL* updates
                
                # if a1CORRPL is starting this frame...
                if a1CORRPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    a1CORRPL.frameNStart = frameN  # exact frame index
                    a1CORRPL.tStart = t  # local t and not account for scr refresh
                    a1CORRPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(a1CORRPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    a1CORRPL.status = STARTED
                    a1CORRPL.setAutoDraw(True)
                
                # if a1CORRPL is active this frame...
                if a1CORRPL.status == STARTED:
                    # update params
                    pass
                
                # *a1CorrCON* updates
                
                # if a1CorrCON is starting this frame...
                if a1CorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    a1CorrCON.frameNStart = frameN  # exact frame index
                    a1CorrCON.tStart = t  # local t and not account for scr refresh
                    a1CorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(a1CorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    a1CorrCON.status = STARTED
                    a1CorrCON.setAutoDraw(True)
                
                # if a1CorrCON is active this frame...
                if a1CorrCON.status == STARTED:
                    # update params
                    pass
                # start/stop a1Sound1
                
                # if a1Sound1 is starting this frame...
                if a1Sound1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    a1Sound1.frameNStart = frameN  # exact frame index
                    a1Sound1.tStart = t  # local t and not account for scr refresh
                    a1Sound1.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    a1Sound1.status = STARTED
                    a1Sound1.play(when=win)  # sync with win flip
                
                # if a1Sound1 is stopping this frame...
                if a1Sound1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > a1Sound1.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        a1Sound1.tStop = t  # not accounting for scr refresh
                        a1Sound1.frameNStop = frameN  # exact frame index
                        # update status
                        a1Sound1.status = FINISHED
                        a1Sound1.stop()
                
                # *a1Key1* updates
                
                # if a1Key1 is starting this frame...
                if a1Key1.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    a1Key1.frameNStart = frameN  # exact frame index
                    a1Key1.tStart = t  # local t and not account for scr refresh
                    a1Key1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(a1Key1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    a1Key1.status = STARTED
                    # keyboard checking is just starting
                    a1Key1.clock.reset()  # now t=0
                if a1Key1.status == STARTED:
                    theseKeys = a1Key1.getKeys(keyList=['space'], waitRelease=False)
                    _a1Key1_allKeys.extend(theseKeys)
                    if len(_a1Key1_allKeys):
                        a1Key1.keys = _a1Key1_allKeys[-1].name  # just the last key pressed
                        a1Key1.rt = _a1Key1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space30* updates
                
                # if space30 is starting this frame...
                if space30.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space30.frameNStart = frameN  # exact frame index
                    space30.tStart = t  # local t and not account for scr refresh
                    space30.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space30, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space30.status = STARTED
                    space30.setAutoDraw(True)
                
                # if space30 is active this frame...
                if space30.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in afc1_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "afc1_2" ---
            for thisComponent in afc1_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from a1Code2
            orthoCount = orthoCount+1
            orthoRep = orthoRep+1
            thisExp.addData("response","correct")
            a1Sound1.stop()  # ensure sound has stopped at end of routine
            # the Routine "afc1_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsA1Corr repeats of 'afc1CorrLoop'
        
        
        # set up handler to look after randomisation of conditions etc
        afc1IncorrLoop = data.TrialHandler(nReps=nRepsA1Incorr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='afc1IncorrLoop')
        thisExp.addLoop(afc1IncorrLoop)  # add the loop to the experiment
        thisAfc1IncorrLoop = afc1IncorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAfc1IncorrLoop.rgb)
        if thisAfc1IncorrLoop != None:
            for paramName in thisAfc1IncorrLoop:
                exec('{} = thisAfc1IncorrLoop[paramName]'.format(paramName))
        
        for thisAfc1IncorrLoop in afc1IncorrLoop:
            currentLoop = afc1IncorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisAfc1IncorrLoop.rgb)
            if thisAfc1IncorrLoop != None:
                for paramName in thisAfc1IncorrLoop:
                    exec('{} = thisAfc1IncorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "afc1_3" ---
            continueRoutine = True
            # update component parameters for each repeat
            a1IncorrPL.setText(plWord)
            a1IncorrCON.setPos([a1Posi[0]])
            a1IncorrCON.setText(conWord)
            a1IncorrDIST.setPos(incorrPosi00)
            a1IncorrDIST.setText(incorrAns00)
            a1Sound2.setSound(audio, secs=2, hamming=True)
            a1Sound2.setVolume(3.0, log=False)
            a1Key2.keys = []
            a1Key2.rt = []
            _a1Key2_allKeys = []
            # keep track of which components have finished
            afc1_3Components = [a1IncorrPL, a1IncorrCON, a1IncorrDIST, a1Sound2, a1Key2, space31]
            for thisComponent in afc1_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "afc1_3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *a1IncorrPL* updates
                
                # if a1IncorrPL is starting this frame...
                if a1IncorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    a1IncorrPL.frameNStart = frameN  # exact frame index
                    a1IncorrPL.tStart = t  # local t and not account for scr refresh
                    a1IncorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(a1IncorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    a1IncorrPL.status = STARTED
                    a1IncorrPL.setAutoDraw(True)
                
                # if a1IncorrPL is active this frame...
                if a1IncorrPL.status == STARTED:
                    # update params
                    pass
                
                # *a1IncorrCON* updates
                
                # if a1IncorrCON is starting this frame...
                if a1IncorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    a1IncorrCON.frameNStart = frameN  # exact frame index
                    a1IncorrCON.tStart = t  # local t and not account for scr refresh
                    a1IncorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(a1IncorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    a1IncorrCON.status = STARTED
                    a1IncorrCON.setAutoDraw(True)
                
                # if a1IncorrCON is active this frame...
                if a1IncorrCON.status == STARTED:
                    # update params
                    pass
                
                # *a1IncorrDIST* updates
                
                # if a1IncorrDIST is starting this frame...
                if a1IncorrDIST.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    a1IncorrDIST.frameNStart = frameN  # exact frame index
                    a1IncorrDIST.tStart = t  # local t and not account for scr refresh
                    a1IncorrDIST.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(a1IncorrDIST, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    a1IncorrDIST.status = STARTED
                    a1IncorrDIST.setAutoDraw(True)
                
                # if a1IncorrDIST is active this frame...
                if a1IncorrDIST.status == STARTED:
                    # update params
                    pass
                # start/stop a1Sound2
                
                # if a1Sound2 is starting this frame...
                if a1Sound2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    a1Sound2.frameNStart = frameN  # exact frame index
                    a1Sound2.tStart = t  # local t and not account for scr refresh
                    a1Sound2.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    a1Sound2.status = STARTED
                    a1Sound2.play(when=win)  # sync with win flip
                
                # if a1Sound2 is stopping this frame...
                if a1Sound2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > a1Sound2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        a1Sound2.tStop = t  # not accounting for scr refresh
                        a1Sound2.frameNStop = frameN  # exact frame index
                        # update status
                        a1Sound2.status = FINISHED
                        a1Sound2.stop()
                
                # *a1Key2* updates
                
                # if a1Key2 is starting this frame...
                if a1Key2.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    a1Key2.frameNStart = frameN  # exact frame index
                    a1Key2.tStart = t  # local t and not account for scr refresh
                    a1Key2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(a1Key2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    a1Key2.status = STARTED
                    # keyboard checking is just starting
                    a1Key2.clock.reset()  # now t=0
                if a1Key2.status == STARTED:
                    theseKeys = a1Key2.getKeys(keyList=['space'], waitRelease=False)
                    _a1Key2_allKeys.extend(theseKeys)
                    if len(_a1Key2_allKeys):
                        a1Key2.keys = _a1Key2_allKeys[-1].name  # just the last key pressed
                        a1Key2.rt = _a1Key2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space31* updates
                
                # if space31 is starting this frame...
                if space31.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space31.frameNStart = frameN  # exact frame index
                    space31.tStart = t  # local t and not account for scr refresh
                    space31.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space31, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space31.status = STARTED
                    space31.setAutoDraw(True)
                
                # if space31 is active this frame...
                if space31.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in afc1_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "afc1_3" ---
            for thisComponent in afc1_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from a1Code3
            incorrCount = incorrCount+1
            orthoCount = orthoCount+1
            orthoRep = orthoRep+1
            thisExp.addData("response","incorrect")
            a1Sound2.stop()  # ensure sound has stopped at end of routine
            # the Routine "afc1_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsA1Incorr repeats of 'afc1IncorrLoop'
        
        
        # --- Prepare to start Routine "afc1_4" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from a1Code4
        if orthoCount ==1:
            orthoCount = 0
            afcOrtho.finished = True
            
        
        # keep track of which components have finished
        afc1_4Components = []
        for thisComponent in afc1_4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "afc1_4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in afc1_4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "afc1_4" ---
        for thisComponent in afc1_4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "afc1_4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nRepsAfcOrtho repeats of 'afcOrtho'
    
    
    # set up handler to look after randomisation of conditions etc
    afcImg = data.TrialHandler(nReps=nRepsAfcImg, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("imgstim_"+expInfo['group']+".xlsx", selection=str(imgRep) + ':' + str(imgRep + 1)),
        seed=None, name='afcImg')
    thisExp.addLoop(afcImg)  # add the loop to the experiment
    thisAfcImg = afcImg.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAfcImg.rgb)
    if thisAfcImg != None:
        for paramName in thisAfcImg:
            exec('{} = thisAfcImg[paramName]'.format(paramName))
    
    for thisAfcImg in afcImg:
        currentLoop = afcImg
        # abbreviate parameter names if possible (e.g. rgb = thisAfcImg.rgb)
        if thisAfcImg != None:
            for paramName in thisAfcImg:
                exec('{} = thisAfcImg[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "afc2_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from a2Code1
        if imgRep == 20:
            afcImg.finished = True
        else:
            afcImg.finished = False
            
        thisExp.addData("repetitions",totalCount)
        
        random.shuffle(a2Posi)
        a2PL.setImage(img)
        a2CON.setPos([a2Posi[0]])
        a2CON.setText(conWord)
        # reset a2CON to account for continued clicks & clear times on/off
        a2CON.reset()
        a2DIST1.setPos([a2Posi[1]])
        a2DIST1.setText(incorr1)
        # reset a2DIST1 to account for continued clicks & clear times on/off
        a2DIST1.reset()
        a2DIST2.setPos([a2Posi[2]])
        a2DIST2.setText(incorr2)
        # reset a2DIST2 to account for continued clicks & clear times on/off
        a2DIST2.reset()
        a2DIST3.setPos([a2Posi[3]])
        a2DIST3.setText(incorr3)
        # reset a2DIST3 to account for continued clicks & clear times on/off
        a2DIST3.reset()
        # setup some python lists for storing info about the a2Mouse
        a2Mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        afc2_1Components = [a2PL, a2CON, a2DIST1, a2DIST2, a2DIST3, a2Mouse]
        for thisComponent in afc2_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "afc2_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *a2PL* updates
            
            # if a2PL is starting this frame...
            if a2PL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                a2PL.frameNStart = frameN  # exact frame index
                a2PL.tStart = t  # local t and not account for scr refresh
                a2PL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a2PL, 'tStartRefresh')  # time at next scr refresh
                # update status
                a2PL.status = STARTED
                a2PL.setAutoDraw(True)
            
            # if a2PL is active this frame...
            if a2PL.status == STARTED:
                # update params
                pass
            # *a2CON* updates
            
            # if a2CON is starting this frame...
            if a2CON.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                a2CON.frameNStart = frameN  # exact frame index
                a2CON.tStart = t  # local t and not account for scr refresh
                a2CON.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a2CON, 'tStartRefresh')  # time at next scr refresh
                # update status
                a2CON.status = STARTED
                a2CON.setAutoDraw(True)
            
            # if a2CON is active this frame...
            if a2CON.status == STARTED:
                # update params
                pass
                # check whether a2CON has been pressed
                if a2CON.isClicked:
                    if not a2CON.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        a2CON.timesOn.append(a2CON.buttonClock.getTime())
                        a2CON.timesOff.append(a2CON.buttonClock.getTime())
                    elif len(a2CON.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        a2CON.timesOff[-1] = a2CON.buttonClock.getTime()
                    if not a2CON.wasClicked:
                        # end routine when a2CON is clicked
                        continueRoutine = False
                    if not a2CON.wasClicked:
                        # run callback code when a2CON is clicked
                        pass
            # take note of whether a2CON was clicked, so that next frame we know if clicks are new
            a2CON.wasClicked = a2CON.isClicked and a2CON.status == STARTED
            # *a2DIST1* updates
            
            # if a2DIST1 is starting this frame...
            if a2DIST1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                a2DIST1.frameNStart = frameN  # exact frame index
                a2DIST1.tStart = t  # local t and not account for scr refresh
                a2DIST1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a2DIST1, 'tStartRefresh')  # time at next scr refresh
                # update status
                a2DIST1.status = STARTED
                a2DIST1.setAutoDraw(True)
            
            # if a2DIST1 is active this frame...
            if a2DIST1.status == STARTED:
                # update params
                pass
                # check whether a2DIST1 has been pressed
                if a2DIST1.isClicked:
                    if not a2DIST1.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        a2DIST1.timesOn.append(a2DIST1.buttonClock.getTime())
                        a2DIST1.timesOff.append(a2DIST1.buttonClock.getTime())
                    elif len(a2DIST1.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        a2DIST1.timesOff[-1] = a2DIST1.buttonClock.getTime()
                    if not a2DIST1.wasClicked:
                        # end routine when a2DIST1 is clicked
                        continueRoutine = False
                    if not a2DIST1.wasClicked:
                        # run callback code when a2DIST1 is clicked
                        pass
            # take note of whether a2DIST1 was clicked, so that next frame we know if clicks are new
            a2DIST1.wasClicked = a2DIST1.isClicked and a2DIST1.status == STARTED
            # *a2DIST2* updates
            
            # if a2DIST2 is starting this frame...
            if a2DIST2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                a2DIST2.frameNStart = frameN  # exact frame index
                a2DIST2.tStart = t  # local t and not account for scr refresh
                a2DIST2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a2DIST2, 'tStartRefresh')  # time at next scr refresh
                # update status
                a2DIST2.status = STARTED
                a2DIST2.setAutoDraw(True)
            
            # if a2DIST2 is active this frame...
            if a2DIST2.status == STARTED:
                # update params
                pass
                # check whether a2DIST2 has been pressed
                if a2DIST2.isClicked:
                    if not a2DIST2.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        a2DIST2.timesOn.append(a2DIST2.buttonClock.getTime())
                        a2DIST2.timesOff.append(a2DIST2.buttonClock.getTime())
                    elif len(a2DIST2.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        a2DIST2.timesOff[-1] = a2DIST2.buttonClock.getTime()
                    if not a2DIST2.wasClicked:
                        # end routine when a2DIST2 is clicked
                        continueRoutine = False
                    if not a2DIST2.wasClicked:
                        # run callback code when a2DIST2 is clicked
                        pass
            # take note of whether a2DIST2 was clicked, so that next frame we know if clicks are new
            a2DIST2.wasClicked = a2DIST2.isClicked and a2DIST2.status == STARTED
            # *a2DIST3* updates
            
            # if a2DIST3 is starting this frame...
            if a2DIST3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                a2DIST3.frameNStart = frameN  # exact frame index
                a2DIST3.tStart = t  # local t and not account for scr refresh
                a2DIST3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a2DIST3, 'tStartRefresh')  # time at next scr refresh
                # update status
                a2DIST3.status = STARTED
                a2DIST3.setAutoDraw(True)
            
            # if a2DIST3 is active this frame...
            if a2DIST3.status == STARTED:
                # update params
                pass
                # check whether a2DIST3 has been pressed
                if a2DIST3.isClicked:
                    if not a2DIST3.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        a2DIST3.timesOn.append(a2DIST3.buttonClock.getTime())
                        a2DIST3.timesOff.append(a2DIST3.buttonClock.getTime())
                    elif len(a2DIST3.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        a2DIST3.timesOff[-1] = a2DIST3.buttonClock.getTime()
                    if not a2DIST3.wasClicked:
                        # end routine when a2DIST3 is clicked
                        continueRoutine = False
                    if not a2DIST3.wasClicked:
                        # run callback code when a2DIST3 is clicked
                        pass
            # take note of whether a2DIST3 was clicked, so that next frame we know if clicks are new
            a2DIST3.wasClicked = a2DIST3.isClicked and a2DIST3.status == STARTED
            # *a2Mouse* updates
            
            # if a2Mouse is starting this frame...
            if a2Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                a2Mouse.frameNStart = frameN  # exact frame index
                a2Mouse.tStart = t  # local t and not account for scr refresh
                a2Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(a2Mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'a2Mouse.started')
                # update status
                a2Mouse.status = STARTED
                a2Mouse.mouseClock.reset()
                prevButtonState = a2Mouse.getPressed()  # if button is down already this ISN'T a new click
            if a2Mouse.status == STARTED:  # only update if started and not finished!
                buttons = a2Mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = core.getFromNames([a2CON,a2DIST1,a2DIST2,a2DIST3])
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(a2Mouse):
                                gotValidClick = True
                                a2Mouse.clicked_name.append(obj.name)
                        continueRoutine = False  # end routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in afc2_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "afc2_1" ---
        for thisComponent in afc2_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from a2Code1
        totalCount = totalCount+1
        
        if a2Mouse.isPressedIn(a2CON):
            nRepsA2Corr = 1
            nRepsA2Incorr = 0
            thisExp.addData("Corr Response",a2CON.text)
        else:
            nRepsA2Corr = 0
            nRepsA2Incorr = 1
        
        if a2Mouse.isPressedIn(a2DIST1):
            incorrAns01=a2DIST1.text
            incorrPosi01=a2DIST1.pos
            thisExp.addData("Incorr Repsonse",a2DIST1.text)
        elif a2Mouse.isPressedIn(a2DIST2):
            incorrAns01=a2DIST2.text
            incorrPosi01=a2DIST2.pos
            thisExp.addData("Incorr Repsonse",a2DIST2.text)
        elif a2Mouse.isPressedIn(a2DIST3):
            incorrAns01=a2DIST3.text
            incorrPosi01=a2DIST3.pos
            thisExp.addData("Incorr Repsonse",a2DIST3.text)
        # store data for afcImg (TrialHandler)
        # the Routine "afc2_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        afcCorrLoop = data.TrialHandler(nReps=nRepsA2Corr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='afcCorrLoop')
        thisExp.addLoop(afcCorrLoop)  # add the loop to the experiment
        thisAfcCorrLoop = afcCorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAfcCorrLoop.rgb)
        if thisAfcCorrLoop != None:
            for paramName in thisAfcCorrLoop:
                exec('{} = thisAfcCorrLoop[paramName]'.format(paramName))
        
        for thisAfcCorrLoop in afcCorrLoop:
            currentLoop = afcCorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisAfcCorrLoop.rgb)
            if thisAfcCorrLoop != None:
                for paramName in thisAfcCorrLoop:
                    exec('{} = thisAfcCorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "afc2_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            a2CorrPL.setImage(img)
            a2CorrCON.setPos([a2Posi[0]])
            a2CorrCON.setText(conWord)
            a2Sound1.setSound(audio, secs=2, hamming=True)
            a2Sound1.setVolume(3.0, log=False)
            a2Key1.keys = []
            a2Key1.rt = []
            _a2Key1_allKeys = []
            # keep track of which components have finished
            afc2_2Components = [a2CorrPL, a2CorrCON, a2Sound1, a2Key1, space32]
            for thisComponent in afc2_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "afc2_2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *a2CorrPL* updates
                
                # if a2CorrPL is starting this frame...
                if a2CorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    a2CorrPL.frameNStart = frameN  # exact frame index
                    a2CorrPL.tStart = t  # local t and not account for scr refresh
                    a2CorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(a2CorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    a2CorrPL.status = STARTED
                    a2CorrPL.setAutoDraw(True)
                
                # if a2CorrPL is active this frame...
                if a2CorrPL.status == STARTED:
                    # update params
                    pass
                
                # *a2CorrCON* updates
                
                # if a2CorrCON is starting this frame...
                if a2CorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    a2CorrCON.frameNStart = frameN  # exact frame index
                    a2CorrCON.tStart = t  # local t and not account for scr refresh
                    a2CorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(a2CorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    a2CorrCON.status = STARTED
                    a2CorrCON.setAutoDraw(True)
                
                # if a2CorrCON is active this frame...
                if a2CorrCON.status == STARTED:
                    # update params
                    pass
                # start/stop a2Sound1
                
                # if a2Sound1 is starting this frame...
                if a2Sound1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    a2Sound1.frameNStart = frameN  # exact frame index
                    a2Sound1.tStart = t  # local t and not account for scr refresh
                    a2Sound1.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    a2Sound1.status = STARTED
                    a2Sound1.play(when=win)  # sync with win flip
                
                # if a2Sound1 is stopping this frame...
                if a2Sound1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > a2Sound1.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        a2Sound1.tStop = t  # not accounting for scr refresh
                        a2Sound1.frameNStop = frameN  # exact frame index
                        # update status
                        a2Sound1.status = FINISHED
                        a2Sound1.stop()
                
                # *a2Key1* updates
                
                # if a2Key1 is starting this frame...
                if a2Key1.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    a2Key1.frameNStart = frameN  # exact frame index
                    a2Key1.tStart = t  # local t and not account for scr refresh
                    a2Key1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(a2Key1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    a2Key1.status = STARTED
                    # keyboard checking is just starting
                    a2Key1.clock.reset()  # now t=0
                if a2Key1.status == STARTED:
                    theseKeys = a2Key1.getKeys(keyList=['space'], waitRelease=False)
                    _a2Key1_allKeys.extend(theseKeys)
                    if len(_a2Key1_allKeys):
                        a2Key1.keys = _a2Key1_allKeys[-1].name  # just the last key pressed
                        a2Key1.rt = _a2Key1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space32* updates
                
                # if space32 is starting this frame...
                if space32.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space32.frameNStart = frameN  # exact frame index
                    space32.tStart = t  # local t and not account for scr refresh
                    space32.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space32, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space32.status = STARTED
                    space32.setAutoDraw(True)
                
                # if space32 is active this frame...
                if space32.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in afc2_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "afc2_2" ---
            for thisComponent in afc2_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from a2Code2
            imgCount = imgCount+1
            imgRep = imgRep+1
            thisExp.addData("response","correct")
            a2Sound1.stop()  # ensure sound has stopped at end of routine
            # the Routine "afc2_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsA2Corr repeats of 'afcCorrLoop'
        
        
        # set up handler to look after randomisation of conditions etc
        afcIncorrLoop = data.TrialHandler(nReps=nRepsA2Incorr, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='afcIncorrLoop')
        thisExp.addLoop(afcIncorrLoop)  # add the loop to the experiment
        thisAfcIncorrLoop = afcIncorrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAfcIncorrLoop.rgb)
        if thisAfcIncorrLoop != None:
            for paramName in thisAfcIncorrLoop:
                exec('{} = thisAfcIncorrLoop[paramName]'.format(paramName))
        
        for thisAfcIncorrLoop in afcIncorrLoop:
            currentLoop = afcIncorrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisAfcIncorrLoop.rgb)
            if thisAfcIncorrLoop != None:
                for paramName in thisAfcIncorrLoop:
                    exec('{} = thisAfcIncorrLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "afc2_3" ---
            continueRoutine = True
            # update component parameters for each repeat
            a2IncorrPL.setImage(img)
            a2IncorrCON.setPos([a2Posi[0]])
            a2IncorrCON.setText(conWord)
            a2IncorrDIST.setPos(incorrPosi01)
            a2IncorrDIST.setText(incorrAns01)
            a2Sound2.setSound(audio, secs=2, hamming=True)
            a2Sound2.setVolume(3.0, log=False)
            a2Key2.keys = []
            a2Key2.rt = []
            _a2Key2_allKeys = []
            # keep track of which components have finished
            afc2_3Components = [a2IncorrPL, a2IncorrCON, a2IncorrDIST, a2Sound2, a2Key2, space33]
            for thisComponent in afc2_3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "afc2_3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *a2IncorrPL* updates
                
                # if a2IncorrPL is starting this frame...
                if a2IncorrPL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    a2IncorrPL.frameNStart = frameN  # exact frame index
                    a2IncorrPL.tStart = t  # local t and not account for scr refresh
                    a2IncorrPL.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(a2IncorrPL, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    a2IncorrPL.status = STARTED
                    a2IncorrPL.setAutoDraw(True)
                
                # if a2IncorrPL is active this frame...
                if a2IncorrPL.status == STARTED:
                    # update params
                    pass
                
                # *a2IncorrCON* updates
                
                # if a2IncorrCON is starting this frame...
                if a2IncorrCON.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    a2IncorrCON.frameNStart = frameN  # exact frame index
                    a2IncorrCON.tStart = t  # local t and not account for scr refresh
                    a2IncorrCON.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(a2IncorrCON, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    a2IncorrCON.status = STARTED
                    a2IncorrCON.setAutoDraw(True)
                
                # if a2IncorrCON is active this frame...
                if a2IncorrCON.status == STARTED:
                    # update params
                    pass
                
                # *a2IncorrDIST* updates
                
                # if a2IncorrDIST is starting this frame...
                if a2IncorrDIST.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    a2IncorrDIST.frameNStart = frameN  # exact frame index
                    a2IncorrDIST.tStart = t  # local t and not account for scr refresh
                    a2IncorrDIST.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(a2IncorrDIST, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    a2IncorrDIST.status = STARTED
                    a2IncorrDIST.setAutoDraw(True)
                
                # if a2IncorrDIST is active this frame...
                if a2IncorrDIST.status == STARTED:
                    # update params
                    pass
                # start/stop a2Sound2
                
                # if a2Sound2 is starting this frame...
                if a2Sound2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    a2Sound2.frameNStart = frameN  # exact frame index
                    a2Sound2.tStart = t  # local t and not account for scr refresh
                    a2Sound2.tStartRefresh = tThisFlipGlobal  # on global time
                    # update status
                    a2Sound2.status = STARTED
                    a2Sound2.play(when=win)  # sync with win flip
                
                # if a2Sound2 is stopping this frame...
                if a2Sound2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > a2Sound2.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        a2Sound2.tStop = t  # not accounting for scr refresh
                        a2Sound2.frameNStop = frameN  # exact frame index
                        # update status
                        a2Sound2.status = FINISHED
                        a2Sound2.stop()
                
                # *a2Key2* updates
                
                # if a2Key2 is starting this frame...
                if a2Key2.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    a2Key2.frameNStart = frameN  # exact frame index
                    a2Key2.tStart = t  # local t and not account for scr refresh
                    a2Key2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(a2Key2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    a2Key2.status = STARTED
                    # keyboard checking is just starting
                    a2Key2.clock.reset()  # now t=0
                if a2Key2.status == STARTED:
                    theseKeys = a2Key2.getKeys(keyList=['space'], waitRelease=False)
                    _a2Key2_allKeys.extend(theseKeys)
                    if len(_a2Key2_allKeys):
                        a2Key2.keys = _a2Key2_allKeys[-1].name  # just the last key pressed
                        a2Key2.rt = _a2Key2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *space33* updates
                
                # if space33 is starting this frame...
                if space33.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    space33.frameNStart = frameN  # exact frame index
                    space33.tStart = t  # local t and not account for scr refresh
                    space33.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space33, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    space33.status = STARTED
                    space33.setAutoDraw(True)
                
                # if space33 is active this frame...
                if space33.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in afc2_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "afc2_3" ---
            for thisComponent in afc2_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from a2Code3
            incorrCount = incorrCount+1
            imgCount = imgCount+1
            imgRep = imgRep+1
            thisExp.addData("response","incorrect")
            a2Sound2.stop()  # ensure sound has stopped at end of routine
            # the Routine "afc2_3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed nRepsA2Incorr repeats of 'afcIncorrLoop'
        
        
        # --- Prepare to start Routine "afc2_4" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from a2Code4
        if imgCount ==1:
            imgCount = 0
            afcImg.finished = True
        # keep track of which components have finished
        afc2_4Components = []
        for thisComponent in afc2_4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "afc2_4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in afc2_4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "afc2_4" ---
        for thisComponent in afc2_4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "afc2_4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nRepsAfcImg repeats of 'afcImg'
    
    
    # --- Prepare to start Routine "afcEnd_Code" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    afcEnd_CodeComponents = []
    for thisComponent in afcEnd_CodeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "afcEnd_Code" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in afcEnd_CodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "afcEnd_Code" ---
    for thisComponent in afcEnd_CodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from AfcFinalCode
    if incorrCount >= 1 and totalCount < 40:
        pass
    elif incorrCount >= 1 and totalCount in [40,80,120,160,200,240,280,320,360,400,440,480,520,560,600]:
        orthoRep = 0
        imgRep = 0
        incorrCount = 0
        thisExp.addData("loop count",'1')
    elif incorrCount == 0 and totalCount == 40:
        orthoRep = 0
        imgRep = 0
        incorrCount = 0
        thisExp.addData("loop count","all correct first loop")
    elif incorrCount == 0 and totalCount in [80,120,160,200,240,280,320,360,400,440,480,520,560,600]:
        bigAFC.finished = True
        thisExp.addData('repetitions',totalCount)
    # the Routine "afcEnd_Code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 30000.0 repeats of 'bigAFC'


# --- Prepare to start Routine "endOfExp" ---
continueRoutine = True
# update component parameters for each repeat
endofExp_key.keys = []
endofExp_key.rt = []
_endofExp_key_allKeys = []
# keep track of which components have finished
endOfExpComponents = [endOfExp_text, endofExp_key]
for thisComponent in endOfExpComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "endOfExp" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endOfExp_text* updates
    
    # if endOfExp_text is starting this frame...
    if endOfExp_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endOfExp_text.frameNStart = frameN  # exact frame index
        endOfExp_text.tStart = t  # local t and not account for scr refresh
        endOfExp_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endOfExp_text, 'tStartRefresh')  # time at next scr refresh
        # update status
        endOfExp_text.status = STARTED
        endOfExp_text.setAutoDraw(True)
    
    # if endOfExp_text is active this frame...
    if endOfExp_text.status == STARTED:
        # update params
        pass
    
    # *endofExp_key* updates
    
    # if endofExp_key is starting this frame...
    if endofExp_key.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endofExp_key.frameNStart = frameN  # exact frame index
        endofExp_key.tStart = t  # local t and not account for scr refresh
        endofExp_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endofExp_key, 'tStartRefresh')  # time at next scr refresh
        # update status
        endofExp_key.status = STARTED
        # keyboard checking is just starting
        endofExp_key.clock.reset()  # now t=0
    if endofExp_key.status == STARTED:
        theseKeys = endofExp_key.getKeys(keyList=['space'], waitRelease=False)
        _endofExp_key_allKeys.extend(theseKeys)
        if len(_endofExp_key_allKeys):
            endofExp_key.keys = _endofExp_key_allKeys[-1].name  # just the last key pressed
            endofExp_key.rt = _endofExp_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endOfExpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "endOfExp" ---
for thisComponent in endOfExpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "endOfExp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
