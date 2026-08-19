#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.0),
    on Wed Nov  6 11:31:34 2024
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
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard
import serial

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.0'
expName = 'DAY2_EEG rebuild'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'group': ['a','b','c','d'],
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_loggingLevel = logging.getLevel('error')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Volumes/MatBackup/2. FLACON/Programming/Testing/DAY2_EEG rebuild.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1280, 720], fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color='darkgray', colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = 'darkgray'
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = True
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('inst1_3') is None:
        # initialise inst1_3
        inst1_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='inst1_3',
        )
    if deviceManager.getDevice('inst2_2') is None:
        # initialise inst2_2
        inst2_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='inst2_2',
        )
    if deviceManager.getDevice('inst3_5') is None:
        # initialise inst3_5
        inst3_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='inst3_5',
        )
    if deviceManager.getDevice('inst4_2') is None:
        # initialise inst4_2
        inst4_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='inst4_2',
        )
    if deviceManager.getDevice('ex1_6') is None:
        # initialise ex1_6
        ex1_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ex1_6',
        )
    if deviceManager.getDevice('ex2_6') is None:
        # initialise ex2_6
        ex2_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ex2_6',
        )
    if deviceManager.getDevice('ex3_6') is None:
        # initialise ex3_6
        ex3_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ex3_6',
        )
    if deviceManager.getDevice('ex4_6') is None:
        # initialise ex4_6
        ex4_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ex4_6',
        )
    if deviceManager.getDevice('inst5_5') is None:
        # initialise inst5_5
        inst5_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='inst5_5',
        )
    if deviceManager.getDevice('inst6_2') is None:
        # initialise inst6_2
        inst6_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='inst6_2',
        )
    if deviceManager.getDevice('ex5_6') is None:
        # initialise ex5_6
        ex5_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ex5_6',
        )
    if deviceManager.getDevice('ex6_6') is None:
        # initialise ex6_6
        ex6_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ex6_6',
        )
    if deviceManager.getDevice('ex7_6') is None:
        # initialise ex7_6
        ex7_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ex7_6',
        )
    if deviceManager.getDevice('ex8_6') is None:
        # initialise ex8_6
        ex8_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ex8_6',
        )
    if deviceManager.getDevice('inst7_2') is None:
        # initialise inst7_2
        inst7_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='inst7_2',
        )
    if deviceManager.getDevice('inst8_2') is None:
        # initialise inst8_2
        inst8_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='inst8_2',
        )
    if deviceManager.getDevice('inst9_2') is None:
        # initialise inst9_2
        inst9_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='inst9_2',
        )
    if deviceManager.getDevice('occ5') is None:
        # initialise occ5
        occ5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='occ5',
        )
    if deviceManager.getDevice('oic5') is None:
        # initialise oic5
        oic5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='oic5',
        )
    if deviceManager.getDevice('oci5') is None:
        # initialise oci5
        oci5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='oci5',
        )
    if deviceManager.getDevice('oii5') is None:
        # initialise oii5
        oii5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='oii5',
        )
    if deviceManager.getDevice('icc5') is None:
        # initialise icc5
        icc5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='icc5',
        )
    if deviceManager.getDevice('iic5') is None:
        # initialise iic5
        iic5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='iic5',
        )
    if deviceManager.getDevice('ici5') is None:
        # initialise ici5
        ici5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='ici5',
        )
    if deviceManager.getDevice('iii5') is None:
        # initialise iii5
        iii5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='iii5',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "inst1" ---
    inst1_1 = visual.TextStim(win=win, name='inst1_1',
        text='Witamy w eksperymencie!',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    inst1_2 = visual.TextStim(win=win, name='inst1_2',
        text='Naciśnij spację, aby kontynuować.',
        font='Open Sans',
        pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    inst1_3 = keyboard.Keyboard(deviceName='inst1_3')
    
    # --- Initialize components for Routine "inst2" ---
    isnt2_1 = visual.TextStim(win=win, name='isnt2_1',
        text='W tym badaniu Twoim zadaniem będzie podejmowanie decyzji względem znaczenia słów, których nauczyłaś/eś się podczas wczorajszej sesji.\n\nNaciśnij spację, aby kontynuować.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    inst2_2 = keyboard.Keyboard(deviceName='inst2_2')
    
    # --- Initialize components for Routine "sort1" ---
    
    # --- Initialize components for Routine "inst3" ---
    inst3_1 = visual.TextStim(win=win, name='inst3_1',
        text='Najpierw zobaczysz słowo w języku polskim lub grafikę odpowiadającą jego znaczeniu. Następnie zobaczysz słowo w języku obcym. Na przykład:\n',
        font='Open Sans',
        pos=(0, +0.3), height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    inst3_2 = visual.TextStim(win=win, name='inst3_2',
        text='Po przeczytaniu słowa w języku obcym, zdecyduj czy jego znaczenie jest takie samo, jak słowa/grafiki, które je poprzedzało.\n\nJeśli znaczenie jest takie samo, naciśnij "Z"\nJeśli znaczenie jest inne, naciśnij "M"\n\nNaciśnij spację, aby kontynuować.',
        font='Open Sans',
        pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    inst3_3 = visual.ImageStim(
        win=win,
        name='inst3_3', 
        image='sample_1.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.3, 0), size=(0.45, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    inst3_4 = visual.ImageStim(
        win=win,
        name='inst3_4', 
        image='sample_2.png', mask=None, anchor='center',
        ori=0.0, pos=(+0.3, 0), size=(0.45, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    inst3_5 = keyboard.Keyboard(deviceName='inst3_5')
    
    # --- Initialize components for Routine "inst4" ---
    inst4_1 = visual.TextStim(win=win, name='inst4_1',
        text='Następnie zobaczysz kilka przykładów, po których przejdziesz do właściwego eksperymentu.\n\nNaciśnij spację, aby zobaczyć przykłady.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    inst4_2 = keyboard.Keyboard(deviceName='inst4_2')
    
    # --- Initialize components for Routine "ex1" ---
    ex1_1 = visual.TextStim(win=win, name='ex1_1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    ex1_2 = visual.TextStim(win=win, name='ex1_2',
        text='samochód',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ex1_3 = visual.TextStim(win=win, name='ex1_3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ex1_4 = visual.TextStim(win=win, name='ex1_4',
        text='auto',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    ex1_5 = visual.TextStim(win=win, name='ex1_5',
        text='"Z" jest poprawną odpowiedzią, ponieważ samochód i auto są ze sobą powiązane\n\nNaciśnij spację, aby kontynuować.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    ex1_6 = keyboard.Keyboard(deviceName='ex1_6')
    
    # --- Initialize components for Routine "ex2" ---
    ex2_1 = visual.TextStim(win=win, name='ex2_1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    ex2_2 = visual.TextStim(win=win, name='ex2_2',
        text='samochód',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ex2_3 = visual.TextStim(win=win, name='ex2_3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ex2_4 = visual.TextStim(win=win, name='ex2_4',
        text='książka',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    ex2_5 = visual.TextStim(win=win, name='ex2_5',
        text='"M" jest poprawną odpowiedzią, ponieważ samochód i książka NIE są powiązane\n\nNaciśnij spację, aby kontynuować.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    ex2_6 = keyboard.Keyboard(deviceName='ex2_6')
    
    # --- Initialize components for Routine "ex3" ---
    ex3_1 = visual.TextStim(win=win, name='ex3_1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    ex3_2 = visual.ImageStim(
        win=win,
        name='ex3_2', 
        image='img_samochod.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    ex3_3 = visual.TextStim(win=win, name='ex3_3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ex3_4 = visual.TextStim(win=win, name='ex3_4',
        text='auto',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    ex3_5 = visual.TextStim(win=win, name='ex3_5',
        text='"Z" jest poprawną odpowiedzią, ponieważ samochód i auto są ze sobą powiązane\n\nNaciśnij spację, aby kontynuować.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    ex3_6 = keyboard.Keyboard(deviceName='ex3_6')
    
    # --- Initialize components for Routine "ex4" ---
    ex4_1 = visual.TextStim(win=win, name='ex4_1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    ex4_2 = visual.ImageStim(
        win=win,
        name='ex4_2', 
        image='img_samochod.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    ex4_3 = visual.TextStim(win=win, name='ex4_3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ex4_4 = visual.TextStim(win=win, name='ex4_4',
        text='książka',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    ex4_5 = visual.TextStim(win=win, name='ex4_5',
        text='"M" jest poprawną odpowiedzią, ponieważ samochód i książka NIE są powiązane\n\nNaciśnij spację, aby kontynuować.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    ex4_6 = keyboard.Keyboard(deviceName='ex4_6')
    
    # --- Initialize components for Routine "inst5" ---
    inst5_1 = visual.TextStim(win=win, name='inst5_1',
        text='Najpierw zobaczysz słowo w języku polskim lub grafikę odpowiadającą jego znaczeniu. Następnie zobaczysz słowo w języku obcym. Na przykład:\n',
        font='Open Sans',
        pos=(0, +0.3), height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    inst5_2 = visual.TextStim(win=win, name='inst5_2',
        text='Po przeczytaniu słowa w języku obcym, zdecyduj czy jego znaczenie jest takie samo, jak słowa/grafiki, które je poprzedzało.\n\nJeśli znaczenie jest takie samo, naciśnij "M"\nJeśli znaczenie jest inne, naciśnij "Z"\n\nNaciśnij spację, aby kontynuować.',
        font='Open Sans',
        pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    inst5_3 = visual.ImageStim(
        win=win,
        name='inst5_3', 
        image='sample_1.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.3, 0), size=(0.45, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    inst5_4 = visual.ImageStim(
        win=win,
        name='inst5_4', 
        image='sample_2.png', mask=None, anchor='center',
        ori=0.0, pos=(+0.3, 0), size=(0.45, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    inst5_5 = keyboard.Keyboard(deviceName='inst5_5')
    
    # --- Initialize components for Routine "inst6" ---
    inst6_1 = visual.TextStim(win=win, name='inst6_1',
        text='Następnie zobaczysz kilka przykładów, po których przejdziesz do właściwego eksperymentu.\n\nNaciśnij spację, aby zobaczyć przykłady.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    inst6_2 = keyboard.Keyboard(deviceName='inst6_2')
    
    # --- Initialize components for Routine "ex5" ---
    ex5_1 = visual.TextStim(win=win, name='ex5_1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    ex5_2 = visual.TextStim(win=win, name='ex5_2',
        text='samochód',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ex5_3 = visual.TextStim(win=win, name='ex5_3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ex5_4 = visual.TextStim(win=win, name='ex5_4',
        text='auto',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    ex5_5 = visual.TextStim(win=win, name='ex5_5',
        text='"M" jest poprawną odpowiedzią, ponieważ samochód i auto są ze sobą powiązane\n\nNaciśnij spację, aby kontynuować.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    ex5_6 = keyboard.Keyboard(deviceName='ex5_6')
    
    # --- Initialize components for Routine "ex6" ---
    ex6_1 = visual.TextStim(win=win, name='ex6_1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    ex6_2 = visual.TextStim(win=win, name='ex6_2',
        text='samochód',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ex6_3 = visual.TextStim(win=win, name='ex6_3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ex6_4 = visual.TextStim(win=win, name='ex6_4',
        text='książka',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    ex6_5 = visual.TextStim(win=win, name='ex6_5',
        text='"Z" jest poprawną odpowiedzią, ponieważ samochód i książka NIE są powiązane\n\nNaciśnij spację, aby kontynuować.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    ex6_6 = keyboard.Keyboard(deviceName='ex6_6')
    
    # --- Initialize components for Routine "ex7" ---
    ex7_1 = visual.TextStim(win=win, name='ex7_1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    ex7_2 = visual.ImageStim(
        win=win,
        name='ex7_2', 
        image='img_samochod.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    ex7_3 = visual.TextStim(win=win, name='ex7_3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ex7_4 = visual.TextStim(win=win, name='ex7_4',
        text='auto',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    ex7_5 = visual.TextStim(win=win, name='ex7_5',
        text='"M" jest poprawną odpowiedzią, ponieważ samochód i auto są ze sobą powiązane\n\nNaciśnij spację, aby kontynuować.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    ex7_6 = keyboard.Keyboard(deviceName='ex7_6')
    
    # --- Initialize components for Routine "ex8" ---
    ex8_1 = visual.TextStim(win=win, name='ex8_1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    ex8_2 = visual.ImageStim(
        win=win,
        name='ex8_2', 
        image='img_samochod.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    ex8_3 = visual.TextStim(win=win, name='ex8_3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ex8_4 = visual.TextStim(win=win, name='ex8_4',
        text='książka',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    ex8_5 = visual.TextStim(win=win, name='ex8_5',
        text='"Z" jest poprawną odpowiedzią, ponieważ samochód i książka NIE są powiązane\n\nNaciśnij spację, aby kontynuować.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    ex8_6 = keyboard.Keyboard(deviceName='ex8_6')
    
    # --- Initialize components for Routine "inst7" ---
    inst7_1 = visual.TextStim(win=win, name='inst7_1',
        text='WAŻNE\n\nPostaraj się nie mrugać, dopóki nie podejmiesz decyzji.\nRozluźnij mięśnie twarzy i staraj się nie ruszać podczas eksperymentu.\n\nNaciśnij spację, aby\xa0kontynuować.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    inst7_2 = keyboard.Keyboard(deviceName='inst7_2')
    
    # --- Initialize components for Routine "inst8" ---
    inst8_1 = visual.TextStim(win=win, name='inst8_1',
        text='Pamiętaj, aby podejmować decyzję, gdy tylko przeczytasz drugie słowo, i aby trzymać palce na klawiszach.\n\nNaciśnij spację,\xa0aby\xa0rozpocząć.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    inst8_2 = keyboard.Keyboard(deviceName='inst8_2')
    
    # --- Initialize components for Routine "inst9" ---
    inst9_1 = visual.TextStim(win=win, name='inst9_1',
        text='Jeśli masz jakieś pytania, zadaj je teraz.\n\nGdy będziesz gotowy/a rozpocząć eksperyment, naciśnij spację.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    inst9_2 = keyboard.Keyboard(deviceName='inst9_2')
    
    # --- Initialize components for Routine "repsetup" ---
    # Run 'Begin Experiment' code from code_12
    import random
    totalCount = 0
    allRepsCount = 20
    totalCounttarget = allRepsCount * 8
    
    SelectedRows_order = random.sample(range(allRepsCount),allRepsCount)
    
    # --- Initialize components for Routine "totalcounter" ---
    # Run 'Begin Experiment' code from code
    orders = [[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1]]
    
    
    # --- Initialize components for Routine "trials_code" ---
    # Run 'Begin Experiment' code from code1
    OCC_termloopReps = OIC_termloopReps = OCI_termloopReps = OII_termloopReps = ICC_termloopReps = IIC_termloopReps = ICI_termloopReps = III_termloopReps = 1
    
    # --- Initialize components for Routine "Ortho_Corr_Cong" ---
    # Run 'Begin Experiment' code from occ6
    occCount = 0
    occReps = 0
    occ1 = visual.TextStim(win=win, name='occ1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    occ2 = visual.TextStim(win=win, name='occ2',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    occ3 = visual.TextStim(win=win, name='occ3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    occ4 = visual.TextStim(win=win, name='occ4',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    occ5 = keyboard.Keyboard(deviceName='occ5')
    
    # --- Initialize components for Routine "occ_code" ---
    
    # --- Initialize components for Routine "Ortho_Incorr_Cong" ---
    # Run 'Begin Experiment' code from oic6
    oicCount = 0
    oicReps = 0
    oic1 = visual.TextStim(win=win, name='oic1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    oic2 = visual.TextStim(win=win, name='oic2',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    oic3 = visual.TextStim(win=win, name='oic3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    oic4 = visual.TextStim(win=win, name='oic4',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    oic5 = keyboard.Keyboard(deviceName='oic5')
    
    # --- Initialize components for Routine "oic_code" ---
    
    # --- Initialize components for Routine "Ortho_Corr_Incong" ---
    # Run 'Begin Experiment' code from oci6
    ociCount = 0
    ociReps = 0
    oci1 = visual.TextStim(win=win, name='oci1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    oci2 = visual.TextStim(win=win, name='oci2',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    oci3 = visual.TextStim(win=win, name='oci3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    oci4 = visual.TextStim(win=win, name='oci4',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    oci5 = keyboard.Keyboard(deviceName='oci5')
    
    # --- Initialize components for Routine "oci_code" ---
    
    # --- Initialize components for Routine "Ortho_Incorr_Incong" ---
    # Run 'Begin Experiment' code from oii6
    oiiCount = 0
    oiiReps = 0
    oii1 = visual.TextStim(win=win, name='oii1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    oii2 = visual.TextStim(win=win, name='oii2',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    oii3 = visual.TextStim(win=win, name='oii3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    oii4 = visual.TextStim(win=win, name='oii4',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    oii5 = keyboard.Keyboard(deviceName='oii5')
    
    # --- Initialize components for Routine "oii_code" ---
    
    # --- Initialize components for Routine "Img_Corr_Cong" ---
    # Run 'Begin Experiment' code from icc6
    iccCount = 0
    iccReps = 0
    icc1 = visual.TextStim(win=win, name='icc1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    icc2 = visual.ImageStim(
        win=win,
        name='icc2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    icc3 = visual.TextStim(win=win, name='icc3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    icc4 = visual.TextStim(win=win, name='icc4',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    icc5 = keyboard.Keyboard(deviceName='icc5')
    
    # --- Initialize components for Routine "icc_code" ---
    
    # --- Initialize components for Routine "Img_Incorr_Cong" ---
    # Run 'Begin Experiment' code from iic6
    iicCount = 0
    iicReps = 0
    iic1 = visual.TextStim(win=win, name='iic1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    iic2 = visual.ImageStim(
        win=win,
        name='iic2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    iic3 = visual.TextStim(win=win, name='iic3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    iic4 = visual.TextStim(win=win, name='iic4',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    iic5 = keyboard.Keyboard(deviceName='iic5')
    
    # --- Initialize components for Routine "iic_code" ---
    
    # --- Initialize components for Routine "Img_Corr_Incong" ---
    # Run 'Begin Experiment' code from ici6
    iciCount = 0
    iciReps = 0
    ici1 = visual.TextStim(win=win, name='ici1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ici2 = visual.ImageStim(
        win=win,
        name='ici2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    ici3 = visual.TextStim(win=win, name='ici3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    ici4 = visual.TextStim(win=win, name='ici4',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    ici5 = keyboard.Keyboard(deviceName='ici5')
    
    # --- Initialize components for Routine "ici_code" ---
    
    # --- Initialize components for Routine "Img_Incorr_Incong" ---
    # Run 'Begin Experiment' code from iii6
    iiiCount = 0
    iiiReps = 0
    iii1 = visual.TextStim(win=win, name='iii1',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    iii2 = visual.ImageStim(
        win=win,
        name='iii2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    iii3 = visual.TextStim(win=win, name='iii3',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    iii4 = visual.TextStim(win=win, name='iii4',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    iii5 = keyboard.Keyboard(deviceName='iii5')
    
    # --- Initialize components for Routine "iii_code" ---
    
    # --- Initialize components for Routine "exitmain" ---
    
    # --- Initialize components for Routine "screenbreak" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='take a break\nNaciśnij spację, aby kontynuować',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "reset_for_new" ---
    
    # --- Initialize components for Routine "Done" ---
    text = visual.TextStim(win=win, name='text',
        text='eksperyment zakończony!',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "inst1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('inst1.started', globalClock.getTime(format='float'))
    inst1_3.keys = []
    inst1_3.rt = []
    _inst1_3_allKeys = []
    # keep track of which components have finished
    inst1Components = [inst1_1, inst1_2, inst1_3]
    for thisComponent in inst1Components:
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
    
    # --- Run Routine "inst1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inst1_1* updates
        
        # if inst1_1 is starting this frame...
        if inst1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst1_1.frameNStart = frameN  # exact frame index
            inst1_1.tStart = t  # local t and not account for scr refresh
            inst1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst1_1, 'tStartRefresh')  # time at next scr refresh
            # update status
            inst1_1.status = STARTED
            inst1_1.setAutoDraw(True)
        
        # if inst1_1 is active this frame...
        if inst1_1.status == STARTED:
            # update params
            pass
        
        # *inst1_2* updates
        
        # if inst1_2 is starting this frame...
        if inst1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst1_2.frameNStart = frameN  # exact frame index
            inst1_2.tStart = t  # local t and not account for scr refresh
            inst1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst1_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            inst1_2.status = STARTED
            inst1_2.setAutoDraw(True)
        
        # if inst1_2 is active this frame...
        if inst1_2.status == STARTED:
            # update params
            pass
        
        # *inst1_3* updates
        waitOnFlip = False
        
        # if inst1_3 is starting this frame...
        if inst1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst1_3.frameNStart = frameN  # exact frame index
            inst1_3.tStart = t  # local t and not account for scr refresh
            inst1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst1_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            inst1_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(inst1_3.clock.reset)  # t=0 on next screen flip
        if inst1_3.status == STARTED and not waitOnFlip:
            theseKeys = inst1_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _inst1_3_allKeys.extend(theseKeys)
            if len(_inst1_3_allKeys):
                inst1_3.keys = _inst1_3_allKeys[-1].name  # just the last key pressed
                inst1_3.rt = _inst1_3_allKeys[-1].rt
                inst1_3.duration = _inst1_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in inst1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "inst1" ---
    for thisComponent in inst1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('inst1.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "inst1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "inst2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('inst2.started', globalClock.getTime(format='float'))
    inst2_2.keys = []
    inst2_2.rt = []
    _inst2_2_allKeys = []
    # keep track of which components have finished
    inst2Components = [isnt2_1, inst2_2]
    for thisComponent in inst2Components:
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
    
    # --- Run Routine "inst2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isnt2_1* updates
        
        # if isnt2_1 is starting this frame...
        if isnt2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isnt2_1.frameNStart = frameN  # exact frame index
            isnt2_1.tStart = t  # local t and not account for scr refresh
            isnt2_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isnt2_1, 'tStartRefresh')  # time at next scr refresh
            # update status
            isnt2_1.status = STARTED
            isnt2_1.setAutoDraw(True)
        
        # if isnt2_1 is active this frame...
        if isnt2_1.status == STARTED:
            # update params
            pass
        
        # *inst2_2* updates
        waitOnFlip = False
        
        # if inst2_2 is starting this frame...
        if inst2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst2_2.frameNStart = frameN  # exact frame index
            inst2_2.tStart = t  # local t and not account for scr refresh
            inst2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst2_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            inst2_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(inst2_2.clock.reset)  # t=0 on next screen flip
        if inst2_2.status == STARTED and not waitOnFlip:
            theseKeys = inst2_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _inst2_2_allKeys.extend(theseKeys)
            if len(_inst2_2_allKeys):
                inst2_2.keys = _inst2_2_allKeys[-1].name  # just the last key pressed
                inst2_2.rt = _inst2_2_allKeys[-1].rt
                inst2_2.duration = _inst2_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in inst2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "inst2" ---
    for thisComponent in inst2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('inst2.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "inst2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    inst_group_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='inst_group_loop')
    thisExp.addLoop(inst_group_loop)  # add the loop to the experiment
    thisInst_group_loop = inst_group_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInst_group_loop.rgb)
    if thisInst_group_loop != None:
        for paramName in thisInst_group_loop:
            globals()[paramName] = thisInst_group_loop[paramName]
    
    for thisInst_group_loop in inst_group_loop:
        currentLoop = inst_group_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisInst_group_loop.rgb)
        if thisInst_group_loop != None:
            for paramName in thisInst_group_loop:
                globals()[paramName] = thisInst_group_loop[paramName]
        
        # --- Prepare to start Routine "sort1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('sort1.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from sort1Code
        if expInfo['group'] == 'a' or expInfo['group'] == 'c':
            nRepsAC = 1
            nRepsBD = 0
        else:
            nRepsAC = 0
            nRepsBD = 1
        # keep track of which components have finished
        sort1Components = []
        for thisComponent in sort1Components:
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
        
        # --- Run Routine "sort1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sort1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "sort1" ---
        for thisComponent in sort1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('sort1.stopped', globalClock.getTime(format='float'))
        # the Routine "sort1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        AC = data.TrialHandler(nReps=nRepsAC, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='AC')
        thisExp.addLoop(AC)  # add the loop to the experiment
        thisAC = AC.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAC.rgb)
        if thisAC != None:
            for paramName in thisAC:
                globals()[paramName] = thisAC[paramName]
        
        for thisAC in AC:
            currentLoop = AC
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisAC.rgb)
            if thisAC != None:
                for paramName in thisAC:
                    globals()[paramName] = thisAC[paramName]
            
            # --- Prepare to start Routine "inst3" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('inst3.started', globalClock.getTime(format='float'))
            inst3_5.keys = []
            inst3_5.rt = []
            _inst3_5_allKeys = []
            # keep track of which components have finished
            inst3Components = [inst3_1, inst3_2, inst3_3, inst3_4, inst3_5]
            for thisComponent in inst3Components:
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
            
            # --- Run Routine "inst3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *inst3_1* updates
                
                # if inst3_1 is starting this frame...
                if inst3_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst3_1.frameNStart = frameN  # exact frame index
                    inst3_1.tStart = t  # local t and not account for scr refresh
                    inst3_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst3_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst3_1.status = STARTED
                    inst3_1.setAutoDraw(True)
                
                # if inst3_1 is active this frame...
                if inst3_1.status == STARTED:
                    # update params
                    pass
                
                # *inst3_2* updates
                
                # if inst3_2 is starting this frame...
                if inst3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst3_2.frameNStart = frameN  # exact frame index
                    inst3_2.tStart = t  # local t and not account for scr refresh
                    inst3_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst3_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst3_2.status = STARTED
                    inst3_2.setAutoDraw(True)
                
                # if inst3_2 is active this frame...
                if inst3_2.status == STARTED:
                    # update params
                    pass
                
                # *inst3_3* updates
                
                # if inst3_3 is starting this frame...
                if inst3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst3_3.frameNStart = frameN  # exact frame index
                    inst3_3.tStart = t  # local t and not account for scr refresh
                    inst3_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst3_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst3_3.status = STARTED
                    inst3_3.setAutoDraw(True)
                
                # if inst3_3 is active this frame...
                if inst3_3.status == STARTED:
                    # update params
                    pass
                
                # *inst3_4* updates
                
                # if inst3_4 is starting this frame...
                if inst3_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst3_4.frameNStart = frameN  # exact frame index
                    inst3_4.tStart = t  # local t and not account for scr refresh
                    inst3_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst3_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst3_4.status = STARTED
                    inst3_4.setAutoDraw(True)
                
                # if inst3_4 is active this frame...
                if inst3_4.status == STARTED:
                    # update params
                    pass
                
                # *inst3_5* updates
                waitOnFlip = False
                
                # if inst3_5 is starting this frame...
                if inst3_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst3_5.frameNStart = frameN  # exact frame index
                    inst3_5.tStart = t  # local t and not account for scr refresh
                    inst3_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst3_5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst3_5.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(inst3_5.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(inst3_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if inst3_5.status == STARTED and not waitOnFlip:
                    theseKeys = inst3_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _inst3_5_allKeys.extend(theseKeys)
                    if len(_inst3_5_allKeys):
                        inst3_5.keys = _inst3_5_allKeys[-1].name  # just the last key pressed
                        inst3_5.rt = _inst3_5_allKeys[-1].rt
                        inst3_5.duration = _inst3_5_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in inst3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "inst3" ---
            for thisComponent in inst3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('inst3.stopped', globalClock.getTime(format='float'))
            # the Routine "inst3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "inst4" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('inst4.started', globalClock.getTime(format='float'))
            inst4_2.keys = []
            inst4_2.rt = []
            _inst4_2_allKeys = []
            # keep track of which components have finished
            inst4Components = [inst4_1, inst4_2]
            for thisComponent in inst4Components:
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
            
            # --- Run Routine "inst4" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *inst4_1* updates
                
                # if inst4_1 is starting this frame...
                if inst4_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst4_1.frameNStart = frameN  # exact frame index
                    inst4_1.tStart = t  # local t and not account for scr refresh
                    inst4_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst4_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst4_1.status = STARTED
                    inst4_1.setAutoDraw(True)
                
                # if inst4_1 is active this frame...
                if inst4_1.status == STARTED:
                    # update params
                    pass
                
                # *inst4_2* updates
                waitOnFlip = False
                
                # if inst4_2 is starting this frame...
                if inst4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst4_2.frameNStart = frameN  # exact frame index
                    inst4_2.tStart = t  # local t and not account for scr refresh
                    inst4_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst4_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst4_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(inst4_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(inst4_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if inst4_2.status == STARTED and not waitOnFlip:
                    theseKeys = inst4_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _inst4_2_allKeys.extend(theseKeys)
                    if len(_inst4_2_allKeys):
                        inst4_2.keys = _inst4_2_allKeys[-1].name  # just the last key pressed
                        inst4_2.rt = _inst4_2_allKeys[-1].rt
                        inst4_2.duration = _inst4_2_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in inst4Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "inst4" ---
            for thisComponent in inst4Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('inst4.stopped', globalClock.getTime(format='float'))
            # the Routine "inst4" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ex1" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ex1.started', globalClock.getTime(format='float'))
            ex1_6.keys = []
            ex1_6.rt = []
            _ex1_6_allKeys = []
            # keep track of which components have finished
            ex1Components = [ex1_1, ex1_2, ex1_3, ex1_4, ex1_5, ex1_6]
            for thisComponent in ex1Components:
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
            
            # --- Run Routine "ex1" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ex1_1* updates
                
                # if ex1_1 is starting this frame...
                if ex1_1.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    ex1_1.frameNStart = frameN  # exact frame index
                    ex1_1.tStart = t  # local t and not account for scr refresh
                    ex1_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex1_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex1_1.status = STARTED
                    ex1_1.setAutoDraw(True)
                
                # if ex1_1 is active this frame...
                if ex1_1.status == STARTED:
                    # update params
                    pass
                
                # if ex1_1 is stopping this frame...
                if ex1_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex1_1.tStartRefresh + .8-frameTolerance:
                        # keep track of stop time/frame for later
                        ex1_1.tStop = t  # not accounting for scr refresh
                        ex1_1.tStopRefresh = tThisFlipGlobal  # on global time
                        ex1_1.frameNStop = frameN  # exact frame index
                        # update status
                        ex1_1.status = FINISHED
                        ex1_1.setAutoDraw(False)
                
                # *ex1_2* updates
                
                # if ex1_2 is starting this frame...
                if ex1_2.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex1_2.frameNStart = frameN  # exact frame index
                    ex1_2.tStart = t  # local t and not account for scr refresh
                    ex1_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex1_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex1_2.status = STARTED
                    ex1_2.setAutoDraw(True)
                
                # if ex1_2 is active this frame...
                if ex1_2.status == STARTED:
                    # update params
                    pass
                
                # if ex1_2 is stopping this frame...
                if ex1_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex1_2.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex1_2.tStop = t  # not accounting for scr refresh
                        ex1_2.tStopRefresh = tThisFlipGlobal  # on global time
                        ex1_2.frameNStop = frameN  # exact frame index
                        # update status
                        ex1_2.status = FINISHED
                        ex1_2.setAutoDraw(False)
                
                # *ex1_3* updates
                
                # if ex1_3 is starting this frame...
                if ex1_3.status == NOT_STARTED and tThisFlip >= 1.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex1_3.frameNStart = frameN  # exact frame index
                    ex1_3.tStart = t  # local t and not account for scr refresh
                    ex1_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex1_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex1_3.status = STARTED
                    ex1_3.setAutoDraw(True)
                
                # if ex1_3 is active this frame...
                if ex1_3.status == STARTED:
                    # update params
                    pass
                
                # if ex1_3 is stopping this frame...
                if ex1_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex1_3.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        ex1_3.tStop = t  # not accounting for scr refresh
                        ex1_3.tStopRefresh = tThisFlipGlobal  # on global time
                        ex1_3.frameNStop = frameN  # exact frame index
                        # update status
                        ex1_3.status = FINISHED
                        ex1_3.setAutoDraw(False)
                
                # *ex1_4* updates
                
                # if ex1_4 is starting this frame...
                if ex1_4.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex1_4.frameNStart = frameN  # exact frame index
                    ex1_4.tStart = t  # local t and not account for scr refresh
                    ex1_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex1_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex1_4.status = STARTED
                    ex1_4.setAutoDraw(True)
                
                # if ex1_4 is active this frame...
                if ex1_4.status == STARTED:
                    # update params
                    pass
                
                # if ex1_4 is stopping this frame...
                if ex1_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex1_4.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex1_4.tStop = t  # not accounting for scr refresh
                        ex1_4.tStopRefresh = tThisFlipGlobal  # on global time
                        ex1_4.frameNStop = frameN  # exact frame index
                        # update status
                        ex1_4.status = FINISHED
                        ex1_4.setAutoDraw(False)
                
                # *ex1_5* updates
                
                # if ex1_5 is starting this frame...
                if ex1_5.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex1_5.frameNStart = frameN  # exact frame index
                    ex1_5.tStart = t  # local t and not account for scr refresh
                    ex1_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex1_5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex1_5.status = STARTED
                    ex1_5.setAutoDraw(True)
                
                # if ex1_5 is active this frame...
                if ex1_5.status == STARTED:
                    # update params
                    pass
                
                # *ex1_6* updates
                waitOnFlip = False
                
                # if ex1_6 is starting this frame...
                if ex1_6.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex1_6.frameNStart = frameN  # exact frame index
                    ex1_6.tStart = t  # local t and not account for scr refresh
                    ex1_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex1_6, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex1_6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(ex1_6.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(ex1_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if ex1_6.status == STARTED and not waitOnFlip:
                    theseKeys = ex1_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _ex1_6_allKeys.extend(theseKeys)
                    if len(_ex1_6_allKeys):
                        ex1_6.keys = _ex1_6_allKeys[-1].name  # just the last key pressed
                        ex1_6.rt = _ex1_6_allKeys[-1].rt
                        ex1_6.duration = _ex1_6_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ex1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ex1" ---
            for thisComponent in ex1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ex1.stopped', globalClock.getTime(format='float'))
            # the Routine "ex1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ex2" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ex2.started', globalClock.getTime(format='float'))
            ex2_6.keys = []
            ex2_6.rt = []
            _ex2_6_allKeys = []
            # keep track of which components have finished
            ex2Components = [ex2_1, ex2_2, ex2_3, ex2_4, ex2_5, ex2_6]
            for thisComponent in ex2Components:
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
            
            # --- Run Routine "ex2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ex2_1* updates
                
                # if ex2_1 is starting this frame...
                if ex2_1.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    ex2_1.frameNStart = frameN  # exact frame index
                    ex2_1.tStart = t  # local t and not account for scr refresh
                    ex2_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex2_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex2_1.status = STARTED
                    ex2_1.setAutoDraw(True)
                
                # if ex2_1 is active this frame...
                if ex2_1.status == STARTED:
                    # update params
                    pass
                
                # if ex2_1 is stopping this frame...
                if ex2_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex2_1.tStartRefresh + .8-frameTolerance:
                        # keep track of stop time/frame for later
                        ex2_1.tStop = t  # not accounting for scr refresh
                        ex2_1.tStopRefresh = tThisFlipGlobal  # on global time
                        ex2_1.frameNStop = frameN  # exact frame index
                        # update status
                        ex2_1.status = FINISHED
                        ex2_1.setAutoDraw(False)
                
                # *ex2_2* updates
                
                # if ex2_2 is starting this frame...
                if ex2_2.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex2_2.frameNStart = frameN  # exact frame index
                    ex2_2.tStart = t  # local t and not account for scr refresh
                    ex2_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex2_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex2_2.status = STARTED
                    ex2_2.setAutoDraw(True)
                
                # if ex2_2 is active this frame...
                if ex2_2.status == STARTED:
                    # update params
                    pass
                
                # if ex2_2 is stopping this frame...
                if ex2_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex2_2.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex2_2.tStop = t  # not accounting for scr refresh
                        ex2_2.tStopRefresh = tThisFlipGlobal  # on global time
                        ex2_2.frameNStop = frameN  # exact frame index
                        # update status
                        ex2_2.status = FINISHED
                        ex2_2.setAutoDraw(False)
                
                # *ex2_3* updates
                
                # if ex2_3 is starting this frame...
                if ex2_3.status == NOT_STARTED and tThisFlip >= 1.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex2_3.frameNStart = frameN  # exact frame index
                    ex2_3.tStart = t  # local t and not account for scr refresh
                    ex2_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex2_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex2_3.status = STARTED
                    ex2_3.setAutoDraw(True)
                
                # if ex2_3 is active this frame...
                if ex2_3.status == STARTED:
                    # update params
                    pass
                
                # if ex2_3 is stopping this frame...
                if ex2_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex2_3.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        ex2_3.tStop = t  # not accounting for scr refresh
                        ex2_3.tStopRefresh = tThisFlipGlobal  # on global time
                        ex2_3.frameNStop = frameN  # exact frame index
                        # update status
                        ex2_3.status = FINISHED
                        ex2_3.setAutoDraw(False)
                
                # *ex2_4* updates
                
                # if ex2_4 is starting this frame...
                if ex2_4.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex2_4.frameNStart = frameN  # exact frame index
                    ex2_4.tStart = t  # local t and not account for scr refresh
                    ex2_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex2_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex2_4.status = STARTED
                    ex2_4.setAutoDraw(True)
                
                # if ex2_4 is active this frame...
                if ex2_4.status == STARTED:
                    # update params
                    pass
                
                # if ex2_4 is stopping this frame...
                if ex2_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex2_4.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex2_4.tStop = t  # not accounting for scr refresh
                        ex2_4.tStopRefresh = tThisFlipGlobal  # on global time
                        ex2_4.frameNStop = frameN  # exact frame index
                        # update status
                        ex2_4.status = FINISHED
                        ex2_4.setAutoDraw(False)
                
                # *ex2_5* updates
                
                # if ex2_5 is starting this frame...
                if ex2_5.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex2_5.frameNStart = frameN  # exact frame index
                    ex2_5.tStart = t  # local t and not account for scr refresh
                    ex2_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex2_5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex2_5.status = STARTED
                    ex2_5.setAutoDraw(True)
                
                # if ex2_5 is active this frame...
                if ex2_5.status == STARTED:
                    # update params
                    pass
                
                # *ex2_6* updates
                waitOnFlip = False
                
                # if ex2_6 is starting this frame...
                if ex2_6.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex2_6.frameNStart = frameN  # exact frame index
                    ex2_6.tStart = t  # local t and not account for scr refresh
                    ex2_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex2_6, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex2_6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(ex2_6.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(ex2_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if ex2_6.status == STARTED and not waitOnFlip:
                    theseKeys = ex2_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _ex2_6_allKeys.extend(theseKeys)
                    if len(_ex2_6_allKeys):
                        ex2_6.keys = _ex2_6_allKeys[-1].name  # just the last key pressed
                        ex2_6.rt = _ex2_6_allKeys[-1].rt
                        ex2_6.duration = _ex2_6_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ex2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ex2" ---
            for thisComponent in ex2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ex2.stopped', globalClock.getTime(format='float'))
            # the Routine "ex2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ex3" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ex3.started', globalClock.getTime(format='float'))
            ex3_6.keys = []
            ex3_6.rt = []
            _ex3_6_allKeys = []
            # keep track of which components have finished
            ex3Components = [ex3_1, ex3_2, ex3_3, ex3_4, ex3_5, ex3_6]
            for thisComponent in ex3Components:
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
            
            # --- Run Routine "ex3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ex3_1* updates
                
                # if ex3_1 is starting this frame...
                if ex3_1.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    ex3_1.frameNStart = frameN  # exact frame index
                    ex3_1.tStart = t  # local t and not account for scr refresh
                    ex3_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex3_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex3_1.status = STARTED
                    ex3_1.setAutoDraw(True)
                
                # if ex3_1 is active this frame...
                if ex3_1.status == STARTED:
                    # update params
                    pass
                
                # if ex3_1 is stopping this frame...
                if ex3_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex3_1.tStartRefresh + .8-frameTolerance:
                        # keep track of stop time/frame for later
                        ex3_1.tStop = t  # not accounting for scr refresh
                        ex3_1.tStopRefresh = tThisFlipGlobal  # on global time
                        ex3_1.frameNStop = frameN  # exact frame index
                        # update status
                        ex3_1.status = FINISHED
                        ex3_1.setAutoDraw(False)
                
                # *ex3_2* updates
                
                # if ex3_2 is starting this frame...
                if ex3_2.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex3_2.frameNStart = frameN  # exact frame index
                    ex3_2.tStart = t  # local t and not account for scr refresh
                    ex3_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex3_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex3_2.status = STARTED
                    ex3_2.setAutoDraw(True)
                
                # if ex3_2 is active this frame...
                if ex3_2.status == STARTED:
                    # update params
                    pass
                
                # if ex3_2 is stopping this frame...
                if ex3_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex3_2.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex3_2.tStop = t  # not accounting for scr refresh
                        ex3_2.tStopRefresh = tThisFlipGlobal  # on global time
                        ex3_2.frameNStop = frameN  # exact frame index
                        # update status
                        ex3_2.status = FINISHED
                        ex3_2.setAutoDraw(False)
                
                # *ex3_3* updates
                
                # if ex3_3 is starting this frame...
                if ex3_3.status == NOT_STARTED and tThisFlip >= 1.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex3_3.frameNStart = frameN  # exact frame index
                    ex3_3.tStart = t  # local t and not account for scr refresh
                    ex3_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex3_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex3_3.status = STARTED
                    ex3_3.setAutoDraw(True)
                
                # if ex3_3 is active this frame...
                if ex3_3.status == STARTED:
                    # update params
                    pass
                
                # if ex3_3 is stopping this frame...
                if ex3_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex3_3.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        ex3_3.tStop = t  # not accounting for scr refresh
                        ex3_3.tStopRefresh = tThisFlipGlobal  # on global time
                        ex3_3.frameNStop = frameN  # exact frame index
                        # update status
                        ex3_3.status = FINISHED
                        ex3_3.setAutoDraw(False)
                
                # *ex3_4* updates
                
                # if ex3_4 is starting this frame...
                if ex3_4.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex3_4.frameNStart = frameN  # exact frame index
                    ex3_4.tStart = t  # local t and not account for scr refresh
                    ex3_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex3_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex3_4.status = STARTED
                    ex3_4.setAutoDraw(True)
                
                # if ex3_4 is active this frame...
                if ex3_4.status == STARTED:
                    # update params
                    pass
                
                # if ex3_4 is stopping this frame...
                if ex3_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex3_4.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex3_4.tStop = t  # not accounting for scr refresh
                        ex3_4.tStopRefresh = tThisFlipGlobal  # on global time
                        ex3_4.frameNStop = frameN  # exact frame index
                        # update status
                        ex3_4.status = FINISHED
                        ex3_4.setAutoDraw(False)
                
                # *ex3_5* updates
                
                # if ex3_5 is starting this frame...
                if ex3_5.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex3_5.frameNStart = frameN  # exact frame index
                    ex3_5.tStart = t  # local t and not account for scr refresh
                    ex3_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex3_5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex3_5.status = STARTED
                    ex3_5.setAutoDraw(True)
                
                # if ex3_5 is active this frame...
                if ex3_5.status == STARTED:
                    # update params
                    pass
                
                # *ex3_6* updates
                waitOnFlip = False
                
                # if ex3_6 is starting this frame...
                if ex3_6.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex3_6.frameNStart = frameN  # exact frame index
                    ex3_6.tStart = t  # local t and not account for scr refresh
                    ex3_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex3_6, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex3_6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(ex3_6.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(ex3_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if ex3_6.status == STARTED and not waitOnFlip:
                    theseKeys = ex3_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _ex3_6_allKeys.extend(theseKeys)
                    if len(_ex3_6_allKeys):
                        ex3_6.keys = _ex3_6_allKeys[-1].name  # just the last key pressed
                        ex3_6.rt = _ex3_6_allKeys[-1].rt
                        ex3_6.duration = _ex3_6_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ex3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ex3" ---
            for thisComponent in ex3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ex3.stopped', globalClock.getTime(format='float'))
            # the Routine "ex3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ex4" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ex4.started', globalClock.getTime(format='float'))
            ex4_6.keys = []
            ex4_6.rt = []
            _ex4_6_allKeys = []
            # keep track of which components have finished
            ex4Components = [ex4_1, ex4_2, ex4_3, ex4_4, ex4_5, ex4_6]
            for thisComponent in ex4Components:
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
            
            # --- Run Routine "ex4" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ex4_1* updates
                
                # if ex4_1 is starting this frame...
                if ex4_1.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    ex4_1.frameNStart = frameN  # exact frame index
                    ex4_1.tStart = t  # local t and not account for scr refresh
                    ex4_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex4_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex4_1.status = STARTED
                    ex4_1.setAutoDraw(True)
                
                # if ex4_1 is active this frame...
                if ex4_1.status == STARTED:
                    # update params
                    pass
                
                # if ex4_1 is stopping this frame...
                if ex4_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex4_1.tStartRefresh + .8-frameTolerance:
                        # keep track of stop time/frame for later
                        ex4_1.tStop = t  # not accounting for scr refresh
                        ex4_1.tStopRefresh = tThisFlipGlobal  # on global time
                        ex4_1.frameNStop = frameN  # exact frame index
                        # update status
                        ex4_1.status = FINISHED
                        ex4_1.setAutoDraw(False)
                
                # *ex4_2* updates
                
                # if ex4_2 is starting this frame...
                if ex4_2.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex4_2.frameNStart = frameN  # exact frame index
                    ex4_2.tStart = t  # local t and not account for scr refresh
                    ex4_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex4_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex4_2.status = STARTED
                    ex4_2.setAutoDraw(True)
                
                # if ex4_2 is active this frame...
                if ex4_2.status == STARTED:
                    # update params
                    pass
                
                # if ex4_2 is stopping this frame...
                if ex4_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex4_2.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex4_2.tStop = t  # not accounting for scr refresh
                        ex4_2.tStopRefresh = tThisFlipGlobal  # on global time
                        ex4_2.frameNStop = frameN  # exact frame index
                        # update status
                        ex4_2.status = FINISHED
                        ex4_2.setAutoDraw(False)
                
                # *ex4_3* updates
                
                # if ex4_3 is starting this frame...
                if ex4_3.status == NOT_STARTED and tThisFlip >= 1.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex4_3.frameNStart = frameN  # exact frame index
                    ex4_3.tStart = t  # local t and not account for scr refresh
                    ex4_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex4_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex4_3.status = STARTED
                    ex4_3.setAutoDraw(True)
                
                # if ex4_3 is active this frame...
                if ex4_3.status == STARTED:
                    # update params
                    pass
                
                # if ex4_3 is stopping this frame...
                if ex4_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex4_3.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        ex4_3.tStop = t  # not accounting for scr refresh
                        ex4_3.tStopRefresh = tThisFlipGlobal  # on global time
                        ex4_3.frameNStop = frameN  # exact frame index
                        # update status
                        ex4_3.status = FINISHED
                        ex4_3.setAutoDraw(False)
                
                # *ex4_4* updates
                
                # if ex4_4 is starting this frame...
                if ex4_4.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex4_4.frameNStart = frameN  # exact frame index
                    ex4_4.tStart = t  # local t and not account for scr refresh
                    ex4_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex4_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex4_4.status = STARTED
                    ex4_4.setAutoDraw(True)
                
                # if ex4_4 is active this frame...
                if ex4_4.status == STARTED:
                    # update params
                    pass
                
                # if ex4_4 is stopping this frame...
                if ex4_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex4_4.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex4_4.tStop = t  # not accounting for scr refresh
                        ex4_4.tStopRefresh = tThisFlipGlobal  # on global time
                        ex4_4.frameNStop = frameN  # exact frame index
                        # update status
                        ex4_4.status = FINISHED
                        ex4_4.setAutoDraw(False)
                
                # *ex4_5* updates
                
                # if ex4_5 is starting this frame...
                if ex4_5.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex4_5.frameNStart = frameN  # exact frame index
                    ex4_5.tStart = t  # local t and not account for scr refresh
                    ex4_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex4_5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex4_5.status = STARTED
                    ex4_5.setAutoDraw(True)
                
                # if ex4_5 is active this frame...
                if ex4_5.status == STARTED:
                    # update params
                    pass
                
                # *ex4_6* updates
                waitOnFlip = False
                
                # if ex4_6 is starting this frame...
                if ex4_6.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex4_6.frameNStart = frameN  # exact frame index
                    ex4_6.tStart = t  # local t and not account for scr refresh
                    ex4_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex4_6, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex4_6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(ex4_6.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(ex4_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if ex4_6.status == STARTED and not waitOnFlip:
                    theseKeys = ex4_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _ex4_6_allKeys.extend(theseKeys)
                    if len(_ex4_6_allKeys):
                        ex4_6.keys = _ex4_6_allKeys[-1].name  # just the last key pressed
                        ex4_6.rt = _ex4_6_allKeys[-1].rt
                        ex4_6.duration = _ex4_6_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ex4Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ex4" ---
            for thisComponent in ex4Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ex4.stopped', globalClock.getTime(format='float'))
            # the Routine "ex4" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed nRepsAC repeats of 'AC'
        
        
        # set up handler to look after randomisation of conditions etc
        BD = data.TrialHandler(nReps=nRepsBD, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='BD')
        thisExp.addLoop(BD)  # add the loop to the experiment
        thisBD = BD.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisBD.rgb)
        if thisBD != None:
            for paramName in thisBD:
                globals()[paramName] = thisBD[paramName]
        
        for thisBD in BD:
            currentLoop = BD
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisBD.rgb)
            if thisBD != None:
                for paramName in thisBD:
                    globals()[paramName] = thisBD[paramName]
            
            # --- Prepare to start Routine "inst5" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('inst5.started', globalClock.getTime(format='float'))
            inst5_5.keys = []
            inst5_5.rt = []
            _inst5_5_allKeys = []
            # keep track of which components have finished
            inst5Components = [inst5_1, inst5_2, inst5_3, inst5_4, inst5_5]
            for thisComponent in inst5Components:
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
            
            # --- Run Routine "inst5" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *inst5_1* updates
                
                # if inst5_1 is starting this frame...
                if inst5_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst5_1.frameNStart = frameN  # exact frame index
                    inst5_1.tStart = t  # local t and not account for scr refresh
                    inst5_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst5_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst5_1.status = STARTED
                    inst5_1.setAutoDraw(True)
                
                # if inst5_1 is active this frame...
                if inst5_1.status == STARTED:
                    # update params
                    pass
                
                # *inst5_2* updates
                
                # if inst5_2 is starting this frame...
                if inst5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst5_2.frameNStart = frameN  # exact frame index
                    inst5_2.tStart = t  # local t and not account for scr refresh
                    inst5_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst5_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst5_2.status = STARTED
                    inst5_2.setAutoDraw(True)
                
                # if inst5_2 is active this frame...
                if inst5_2.status == STARTED:
                    # update params
                    pass
                
                # *inst5_3* updates
                
                # if inst5_3 is starting this frame...
                if inst5_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst5_3.frameNStart = frameN  # exact frame index
                    inst5_3.tStart = t  # local t and not account for scr refresh
                    inst5_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst5_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst5_3.status = STARTED
                    inst5_3.setAutoDraw(True)
                
                # if inst5_3 is active this frame...
                if inst5_3.status == STARTED:
                    # update params
                    pass
                
                # *inst5_4* updates
                
                # if inst5_4 is starting this frame...
                if inst5_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst5_4.frameNStart = frameN  # exact frame index
                    inst5_4.tStart = t  # local t and not account for scr refresh
                    inst5_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst5_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst5_4.status = STARTED
                    inst5_4.setAutoDraw(True)
                
                # if inst5_4 is active this frame...
                if inst5_4.status == STARTED:
                    # update params
                    pass
                
                # *inst5_5* updates
                waitOnFlip = False
                
                # if inst5_5 is starting this frame...
                if inst5_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst5_5.frameNStart = frameN  # exact frame index
                    inst5_5.tStart = t  # local t and not account for scr refresh
                    inst5_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst5_5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst5_5.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(inst5_5.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(inst5_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if inst5_5.status == STARTED and not waitOnFlip:
                    theseKeys = inst5_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _inst5_5_allKeys.extend(theseKeys)
                    if len(_inst5_5_allKeys):
                        inst5_5.keys = _inst5_5_allKeys[-1].name  # just the last key pressed
                        inst5_5.rt = _inst5_5_allKeys[-1].rt
                        inst5_5.duration = _inst5_5_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in inst5Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "inst5" ---
            for thisComponent in inst5Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('inst5.stopped', globalClock.getTime(format='float'))
            # the Routine "inst5" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "inst6" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('inst6.started', globalClock.getTime(format='float'))
            inst6_2.keys = []
            inst6_2.rt = []
            _inst6_2_allKeys = []
            # keep track of which components have finished
            inst6Components = [inst6_1, inst6_2]
            for thisComponent in inst6Components:
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
            
            # --- Run Routine "inst6" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *inst6_1* updates
                
                # if inst6_1 is starting this frame...
                if inst6_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst6_1.frameNStart = frameN  # exact frame index
                    inst6_1.tStart = t  # local t and not account for scr refresh
                    inst6_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst6_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst6_1.status = STARTED
                    inst6_1.setAutoDraw(True)
                
                # if inst6_1 is active this frame...
                if inst6_1.status == STARTED:
                    # update params
                    pass
                
                # *inst6_2* updates
                waitOnFlip = False
                
                # if inst6_2 is starting this frame...
                if inst6_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst6_2.frameNStart = frameN  # exact frame index
                    inst6_2.tStart = t  # local t and not account for scr refresh
                    inst6_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst6_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst6_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(inst6_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(inst6_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if inst6_2.status == STARTED and not waitOnFlip:
                    theseKeys = inst6_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _inst6_2_allKeys.extend(theseKeys)
                    if len(_inst6_2_allKeys):
                        inst6_2.keys = _inst6_2_allKeys[-1].name  # just the last key pressed
                        inst6_2.rt = _inst6_2_allKeys[-1].rt
                        inst6_2.duration = _inst6_2_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in inst6Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "inst6" ---
            for thisComponent in inst6Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('inst6.stopped', globalClock.getTime(format='float'))
            # the Routine "inst6" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ex5" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ex5.started', globalClock.getTime(format='float'))
            ex5_6.keys = []
            ex5_6.rt = []
            _ex5_6_allKeys = []
            # keep track of which components have finished
            ex5Components = [ex5_1, ex5_2, ex5_3, ex5_4, ex5_5, ex5_6]
            for thisComponent in ex5Components:
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
            
            # --- Run Routine "ex5" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ex5_1* updates
                
                # if ex5_1 is starting this frame...
                if ex5_1.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    ex5_1.frameNStart = frameN  # exact frame index
                    ex5_1.tStart = t  # local t and not account for scr refresh
                    ex5_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex5_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex5_1.status = STARTED
                    ex5_1.setAutoDraw(True)
                
                # if ex5_1 is active this frame...
                if ex5_1.status == STARTED:
                    # update params
                    pass
                
                # if ex5_1 is stopping this frame...
                if ex5_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex5_1.tStartRefresh + .8-frameTolerance:
                        # keep track of stop time/frame for later
                        ex5_1.tStop = t  # not accounting for scr refresh
                        ex5_1.tStopRefresh = tThisFlipGlobal  # on global time
                        ex5_1.frameNStop = frameN  # exact frame index
                        # update status
                        ex5_1.status = FINISHED
                        ex5_1.setAutoDraw(False)
                
                # *ex5_2* updates
                
                # if ex5_2 is starting this frame...
                if ex5_2.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex5_2.frameNStart = frameN  # exact frame index
                    ex5_2.tStart = t  # local t and not account for scr refresh
                    ex5_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex5_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex5_2.status = STARTED
                    ex5_2.setAutoDraw(True)
                
                # if ex5_2 is active this frame...
                if ex5_2.status == STARTED:
                    # update params
                    pass
                
                # if ex5_2 is stopping this frame...
                if ex5_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex5_2.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex5_2.tStop = t  # not accounting for scr refresh
                        ex5_2.tStopRefresh = tThisFlipGlobal  # on global time
                        ex5_2.frameNStop = frameN  # exact frame index
                        # update status
                        ex5_2.status = FINISHED
                        ex5_2.setAutoDraw(False)
                
                # *ex5_3* updates
                
                # if ex5_3 is starting this frame...
                if ex5_3.status == NOT_STARTED and tThisFlip >= 1.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex5_3.frameNStart = frameN  # exact frame index
                    ex5_3.tStart = t  # local t and not account for scr refresh
                    ex5_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex5_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex5_3.status = STARTED
                    ex5_3.setAutoDraw(True)
                
                # if ex5_3 is active this frame...
                if ex5_3.status == STARTED:
                    # update params
                    pass
                
                # if ex5_3 is stopping this frame...
                if ex5_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex5_3.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        ex5_3.tStop = t  # not accounting for scr refresh
                        ex5_3.tStopRefresh = tThisFlipGlobal  # on global time
                        ex5_3.frameNStop = frameN  # exact frame index
                        # update status
                        ex5_3.status = FINISHED
                        ex5_3.setAutoDraw(False)
                
                # *ex5_4* updates
                
                # if ex5_4 is starting this frame...
                if ex5_4.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex5_4.frameNStart = frameN  # exact frame index
                    ex5_4.tStart = t  # local t and not account for scr refresh
                    ex5_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex5_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex5_4.status = STARTED
                    ex5_4.setAutoDraw(True)
                
                # if ex5_4 is active this frame...
                if ex5_4.status == STARTED:
                    # update params
                    pass
                
                # if ex5_4 is stopping this frame...
                if ex5_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex5_4.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex5_4.tStop = t  # not accounting for scr refresh
                        ex5_4.tStopRefresh = tThisFlipGlobal  # on global time
                        ex5_4.frameNStop = frameN  # exact frame index
                        # update status
                        ex5_4.status = FINISHED
                        ex5_4.setAutoDraw(False)
                
                # *ex5_5* updates
                
                # if ex5_5 is starting this frame...
                if ex5_5.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex5_5.frameNStart = frameN  # exact frame index
                    ex5_5.tStart = t  # local t and not account for scr refresh
                    ex5_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex5_5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex5_5.status = STARTED
                    ex5_5.setAutoDraw(True)
                
                # if ex5_5 is active this frame...
                if ex5_5.status == STARTED:
                    # update params
                    pass
                
                # *ex5_6* updates
                waitOnFlip = False
                
                # if ex5_6 is starting this frame...
                if ex5_6.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex5_6.frameNStart = frameN  # exact frame index
                    ex5_6.tStart = t  # local t and not account for scr refresh
                    ex5_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex5_6, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex5_6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(ex5_6.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(ex5_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if ex5_6.status == STARTED and not waitOnFlip:
                    theseKeys = ex5_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _ex5_6_allKeys.extend(theseKeys)
                    if len(_ex5_6_allKeys):
                        ex5_6.keys = _ex5_6_allKeys[-1].name  # just the last key pressed
                        ex5_6.rt = _ex5_6_allKeys[-1].rt
                        ex5_6.duration = _ex5_6_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ex5Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ex5" ---
            for thisComponent in ex5Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ex5.stopped', globalClock.getTime(format='float'))
            # the Routine "ex5" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ex6" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ex6.started', globalClock.getTime(format='float'))
            ex6_6.keys = []
            ex6_6.rt = []
            _ex6_6_allKeys = []
            # keep track of which components have finished
            ex6Components = [ex6_1, ex6_2, ex6_3, ex6_4, ex6_5, ex6_6]
            for thisComponent in ex6Components:
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
            
            # --- Run Routine "ex6" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ex6_1* updates
                
                # if ex6_1 is starting this frame...
                if ex6_1.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    ex6_1.frameNStart = frameN  # exact frame index
                    ex6_1.tStart = t  # local t and not account for scr refresh
                    ex6_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex6_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex6_1.status = STARTED
                    ex6_1.setAutoDraw(True)
                
                # if ex6_1 is active this frame...
                if ex6_1.status == STARTED:
                    # update params
                    pass
                
                # if ex6_1 is stopping this frame...
                if ex6_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex6_1.tStartRefresh + .8-frameTolerance:
                        # keep track of stop time/frame for later
                        ex6_1.tStop = t  # not accounting for scr refresh
                        ex6_1.tStopRefresh = tThisFlipGlobal  # on global time
                        ex6_1.frameNStop = frameN  # exact frame index
                        # update status
                        ex6_1.status = FINISHED
                        ex6_1.setAutoDraw(False)
                
                # *ex6_2* updates
                
                # if ex6_2 is starting this frame...
                if ex6_2.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex6_2.frameNStart = frameN  # exact frame index
                    ex6_2.tStart = t  # local t and not account for scr refresh
                    ex6_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex6_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex6_2.status = STARTED
                    ex6_2.setAutoDraw(True)
                
                # if ex6_2 is active this frame...
                if ex6_2.status == STARTED:
                    # update params
                    pass
                
                # if ex6_2 is stopping this frame...
                if ex6_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex6_2.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex6_2.tStop = t  # not accounting for scr refresh
                        ex6_2.tStopRefresh = tThisFlipGlobal  # on global time
                        ex6_2.frameNStop = frameN  # exact frame index
                        # update status
                        ex6_2.status = FINISHED
                        ex6_2.setAutoDraw(False)
                
                # *ex6_3* updates
                
                # if ex6_3 is starting this frame...
                if ex6_3.status == NOT_STARTED and tThisFlip >= 1.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex6_3.frameNStart = frameN  # exact frame index
                    ex6_3.tStart = t  # local t and not account for scr refresh
                    ex6_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex6_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex6_3.status = STARTED
                    ex6_3.setAutoDraw(True)
                
                # if ex6_3 is active this frame...
                if ex6_3.status == STARTED:
                    # update params
                    pass
                
                # if ex6_3 is stopping this frame...
                if ex6_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex6_3.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        ex6_3.tStop = t  # not accounting for scr refresh
                        ex6_3.tStopRefresh = tThisFlipGlobal  # on global time
                        ex6_3.frameNStop = frameN  # exact frame index
                        # update status
                        ex6_3.status = FINISHED
                        ex6_3.setAutoDraw(False)
                
                # *ex6_4* updates
                
                # if ex6_4 is starting this frame...
                if ex6_4.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex6_4.frameNStart = frameN  # exact frame index
                    ex6_4.tStart = t  # local t and not account for scr refresh
                    ex6_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex6_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex6_4.status = STARTED
                    ex6_4.setAutoDraw(True)
                
                # if ex6_4 is active this frame...
                if ex6_4.status == STARTED:
                    # update params
                    pass
                
                # if ex6_4 is stopping this frame...
                if ex6_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex6_4.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex6_4.tStop = t  # not accounting for scr refresh
                        ex6_4.tStopRefresh = tThisFlipGlobal  # on global time
                        ex6_4.frameNStop = frameN  # exact frame index
                        # update status
                        ex6_4.status = FINISHED
                        ex6_4.setAutoDraw(False)
                
                # *ex6_5* updates
                
                # if ex6_5 is starting this frame...
                if ex6_5.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex6_5.frameNStart = frameN  # exact frame index
                    ex6_5.tStart = t  # local t and not account for scr refresh
                    ex6_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex6_5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex6_5.status = STARTED
                    ex6_5.setAutoDraw(True)
                
                # if ex6_5 is active this frame...
                if ex6_5.status == STARTED:
                    # update params
                    pass
                
                # *ex6_6* updates
                waitOnFlip = False
                
                # if ex6_6 is starting this frame...
                if ex6_6.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex6_6.frameNStart = frameN  # exact frame index
                    ex6_6.tStart = t  # local t and not account for scr refresh
                    ex6_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex6_6, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex6_6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(ex6_6.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(ex6_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if ex6_6.status == STARTED and not waitOnFlip:
                    theseKeys = ex6_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _ex6_6_allKeys.extend(theseKeys)
                    if len(_ex6_6_allKeys):
                        ex6_6.keys = _ex6_6_allKeys[-1].name  # just the last key pressed
                        ex6_6.rt = _ex6_6_allKeys[-1].rt
                        ex6_6.duration = _ex6_6_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ex6Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ex6" ---
            for thisComponent in ex6Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ex6.stopped', globalClock.getTime(format='float'))
            # the Routine "ex6" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ex7" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ex7.started', globalClock.getTime(format='float'))
            ex7_6.keys = []
            ex7_6.rt = []
            _ex7_6_allKeys = []
            # keep track of which components have finished
            ex7Components = [ex7_1, ex7_2, ex7_3, ex7_4, ex7_5, ex7_6]
            for thisComponent in ex7Components:
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
            
            # --- Run Routine "ex7" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ex7_1* updates
                
                # if ex7_1 is starting this frame...
                if ex7_1.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    ex7_1.frameNStart = frameN  # exact frame index
                    ex7_1.tStart = t  # local t and not account for scr refresh
                    ex7_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex7_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex7_1.status = STARTED
                    ex7_1.setAutoDraw(True)
                
                # if ex7_1 is active this frame...
                if ex7_1.status == STARTED:
                    # update params
                    pass
                
                # if ex7_1 is stopping this frame...
                if ex7_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex7_1.tStartRefresh + .8-frameTolerance:
                        # keep track of stop time/frame for later
                        ex7_1.tStop = t  # not accounting for scr refresh
                        ex7_1.tStopRefresh = tThisFlipGlobal  # on global time
                        ex7_1.frameNStop = frameN  # exact frame index
                        # update status
                        ex7_1.status = FINISHED
                        ex7_1.setAutoDraw(False)
                
                # *ex7_2* updates
                
                # if ex7_2 is starting this frame...
                if ex7_2.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex7_2.frameNStart = frameN  # exact frame index
                    ex7_2.tStart = t  # local t and not account for scr refresh
                    ex7_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex7_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex7_2.status = STARTED
                    ex7_2.setAutoDraw(True)
                
                # if ex7_2 is active this frame...
                if ex7_2.status == STARTED:
                    # update params
                    pass
                
                # if ex7_2 is stopping this frame...
                if ex7_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex7_2.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex7_2.tStop = t  # not accounting for scr refresh
                        ex7_2.tStopRefresh = tThisFlipGlobal  # on global time
                        ex7_2.frameNStop = frameN  # exact frame index
                        # update status
                        ex7_2.status = FINISHED
                        ex7_2.setAutoDraw(False)
                
                # *ex7_3* updates
                
                # if ex7_3 is starting this frame...
                if ex7_3.status == NOT_STARTED and tThisFlip >= 1.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex7_3.frameNStart = frameN  # exact frame index
                    ex7_3.tStart = t  # local t and not account for scr refresh
                    ex7_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex7_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex7_3.status = STARTED
                    ex7_3.setAutoDraw(True)
                
                # if ex7_3 is active this frame...
                if ex7_3.status == STARTED:
                    # update params
                    pass
                
                # if ex7_3 is stopping this frame...
                if ex7_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex7_3.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        ex7_3.tStop = t  # not accounting for scr refresh
                        ex7_3.tStopRefresh = tThisFlipGlobal  # on global time
                        ex7_3.frameNStop = frameN  # exact frame index
                        # update status
                        ex7_3.status = FINISHED
                        ex7_3.setAutoDraw(False)
                
                # *ex7_4* updates
                
                # if ex7_4 is starting this frame...
                if ex7_4.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex7_4.frameNStart = frameN  # exact frame index
                    ex7_4.tStart = t  # local t and not account for scr refresh
                    ex7_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex7_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex7_4.status = STARTED
                    ex7_4.setAutoDraw(True)
                
                # if ex7_4 is active this frame...
                if ex7_4.status == STARTED:
                    # update params
                    pass
                
                # if ex7_4 is stopping this frame...
                if ex7_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex7_4.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex7_4.tStop = t  # not accounting for scr refresh
                        ex7_4.tStopRefresh = tThisFlipGlobal  # on global time
                        ex7_4.frameNStop = frameN  # exact frame index
                        # update status
                        ex7_4.status = FINISHED
                        ex7_4.setAutoDraw(False)
                
                # *ex7_5* updates
                
                # if ex7_5 is starting this frame...
                if ex7_5.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex7_5.frameNStart = frameN  # exact frame index
                    ex7_5.tStart = t  # local t and not account for scr refresh
                    ex7_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex7_5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex7_5.status = STARTED
                    ex7_5.setAutoDraw(True)
                
                # if ex7_5 is active this frame...
                if ex7_5.status == STARTED:
                    # update params
                    pass
                
                # *ex7_6* updates
                waitOnFlip = False
                
                # if ex7_6 is starting this frame...
                if ex7_6.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex7_6.frameNStart = frameN  # exact frame index
                    ex7_6.tStart = t  # local t and not account for scr refresh
                    ex7_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex7_6, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex7_6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(ex7_6.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(ex7_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if ex7_6.status == STARTED and not waitOnFlip:
                    theseKeys = ex7_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _ex7_6_allKeys.extend(theseKeys)
                    if len(_ex7_6_allKeys):
                        ex7_6.keys = _ex7_6_allKeys[-1].name  # just the last key pressed
                        ex7_6.rt = _ex7_6_allKeys[-1].rt
                        ex7_6.duration = _ex7_6_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ex7Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ex7" ---
            for thisComponent in ex7Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ex7.stopped', globalClock.getTime(format='float'))
            # the Routine "ex7" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ex8" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ex8.started', globalClock.getTime(format='float'))
            ex8_6.keys = []
            ex8_6.rt = []
            _ex8_6_allKeys = []
            # keep track of which components have finished
            ex8Components = [ex8_1, ex8_2, ex8_3, ex8_4, ex8_5, ex8_6]
            for thisComponent in ex8Components:
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
            
            # --- Run Routine "ex8" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ex8_1* updates
                
                # if ex8_1 is starting this frame...
                if ex8_1.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    ex8_1.frameNStart = frameN  # exact frame index
                    ex8_1.tStart = t  # local t and not account for scr refresh
                    ex8_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex8_1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex8_1.status = STARTED
                    ex8_1.setAutoDraw(True)
                
                # if ex8_1 is active this frame...
                if ex8_1.status == STARTED:
                    # update params
                    pass
                
                # if ex8_1 is stopping this frame...
                if ex8_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex8_1.tStartRefresh + .8-frameTolerance:
                        # keep track of stop time/frame for later
                        ex8_1.tStop = t  # not accounting for scr refresh
                        ex8_1.tStopRefresh = tThisFlipGlobal  # on global time
                        ex8_1.frameNStop = frameN  # exact frame index
                        # update status
                        ex8_1.status = FINISHED
                        ex8_1.setAutoDraw(False)
                
                # *ex8_2* updates
                
                # if ex8_2 is starting this frame...
                if ex8_2.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex8_2.frameNStart = frameN  # exact frame index
                    ex8_2.tStart = t  # local t and not account for scr refresh
                    ex8_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex8_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex8_2.status = STARTED
                    ex8_2.setAutoDraw(True)
                
                # if ex8_2 is active this frame...
                if ex8_2.status == STARTED:
                    # update params
                    pass
                
                # if ex8_2 is stopping this frame...
                if ex8_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex8_2.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex8_2.tStop = t  # not accounting for scr refresh
                        ex8_2.tStopRefresh = tThisFlipGlobal  # on global time
                        ex8_2.frameNStop = frameN  # exact frame index
                        # update status
                        ex8_2.status = FINISHED
                        ex8_2.setAutoDraw(False)
                
                # *ex8_3* updates
                
                # if ex8_3 is starting this frame...
                if ex8_3.status == NOT_STARTED and tThisFlip >= 1.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex8_3.frameNStart = frameN  # exact frame index
                    ex8_3.tStart = t  # local t and not account for scr refresh
                    ex8_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex8_3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex8_3.status = STARTED
                    ex8_3.setAutoDraw(True)
                
                # if ex8_3 is active this frame...
                if ex8_3.status == STARTED:
                    # update params
                    pass
                
                # if ex8_3 is stopping this frame...
                if ex8_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex8_3.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        ex8_3.tStop = t  # not accounting for scr refresh
                        ex8_3.tStopRefresh = tThisFlipGlobal  # on global time
                        ex8_3.frameNStop = frameN  # exact frame index
                        # update status
                        ex8_3.status = FINISHED
                        ex8_3.setAutoDraw(False)
                
                # *ex8_4* updates
                
                # if ex8_4 is starting this frame...
                if ex8_4.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                    # keep track of start time/frame for later
                    ex8_4.frameNStart = frameN  # exact frame index
                    ex8_4.tStart = t  # local t and not account for scr refresh
                    ex8_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex8_4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex8_4.status = STARTED
                    ex8_4.setAutoDraw(True)
                
                # if ex8_4 is active this frame...
                if ex8_4.status == STARTED:
                    # update params
                    pass
                
                # if ex8_4 is stopping this frame...
                if ex8_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ex8_4.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        ex8_4.tStop = t  # not accounting for scr refresh
                        ex8_4.tStopRefresh = tThisFlipGlobal  # on global time
                        ex8_4.frameNStop = frameN  # exact frame index
                        # update status
                        ex8_4.status = FINISHED
                        ex8_4.setAutoDraw(False)
                
                # *ex8_5* updates
                
                # if ex8_5 is starting this frame...
                if ex8_5.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex8_5.frameNStart = frameN  # exact frame index
                    ex8_5.tStart = t  # local t and not account for scr refresh
                    ex8_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex8_5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex8_5.status = STARTED
                    ex8_5.setAutoDraw(True)
                
                # if ex8_5 is active this frame...
                if ex8_5.status == STARTED:
                    # update params
                    pass
                
                # *ex8_6* updates
                waitOnFlip = False
                
                # if ex8_6 is starting this frame...
                if ex8_6.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                    # keep track of start time/frame for later
                    ex8_6.frameNStart = frameN  # exact frame index
                    ex8_6.tStart = t  # local t and not account for scr refresh
                    ex8_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ex8_6, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    ex8_6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(ex8_6.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(ex8_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if ex8_6.status == STARTED and not waitOnFlip:
                    theseKeys = ex8_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _ex8_6_allKeys.extend(theseKeys)
                    if len(_ex8_6_allKeys):
                        ex8_6.keys = _ex8_6_allKeys[-1].name  # just the last key pressed
                        ex8_6.rt = _ex8_6_allKeys[-1].rt
                        ex8_6.duration = _ex8_6_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ex8Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ex8" ---
            for thisComponent in ex8Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ex8.stopped', globalClock.getTime(format='float'))
            # the Routine "ex8" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed nRepsBD repeats of 'BD'
        
    # completed 1.0 repeats of 'inst_group_loop'
    
    
    # --- Prepare to start Routine "inst7" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('inst7.started', globalClock.getTime(format='float'))
    inst7_2.keys = []
    inst7_2.rt = []
    _inst7_2_allKeys = []
    # keep track of which components have finished
    inst7Components = [inst7_1, inst7_2]
    for thisComponent in inst7Components:
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
    
    # --- Run Routine "inst7" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inst7_1* updates
        
        # if inst7_1 is starting this frame...
        if inst7_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst7_1.frameNStart = frameN  # exact frame index
            inst7_1.tStart = t  # local t and not account for scr refresh
            inst7_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst7_1, 'tStartRefresh')  # time at next scr refresh
            # update status
            inst7_1.status = STARTED
            inst7_1.setAutoDraw(True)
        
        # if inst7_1 is active this frame...
        if inst7_1.status == STARTED:
            # update params
            pass
        
        # *inst7_2* updates
        waitOnFlip = False
        
        # if inst7_2 is starting this frame...
        if inst7_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst7_2.frameNStart = frameN  # exact frame index
            inst7_2.tStart = t  # local t and not account for scr refresh
            inst7_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst7_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            inst7_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(inst7_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(inst7_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if inst7_2.status == STARTED and not waitOnFlip:
            theseKeys = inst7_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _inst7_2_allKeys.extend(theseKeys)
            if len(_inst7_2_allKeys):
                inst7_2.keys = _inst7_2_allKeys[-1].name  # just the last key pressed
                inst7_2.rt = _inst7_2_allKeys[-1].rt
                inst7_2.duration = _inst7_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in inst7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "inst7" ---
    for thisComponent in inst7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('inst7.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "inst7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "inst8" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('inst8.started', globalClock.getTime(format='float'))
    inst8_2.keys = []
    inst8_2.rt = []
    _inst8_2_allKeys = []
    # keep track of which components have finished
    inst8Components = [inst8_1, inst8_2]
    for thisComponent in inst8Components:
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
    
    # --- Run Routine "inst8" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inst8_1* updates
        
        # if inst8_1 is starting this frame...
        if inst8_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst8_1.frameNStart = frameN  # exact frame index
            inst8_1.tStart = t  # local t and not account for scr refresh
            inst8_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst8_1, 'tStartRefresh')  # time at next scr refresh
            # update status
            inst8_1.status = STARTED
            inst8_1.setAutoDraw(True)
        
        # if inst8_1 is active this frame...
        if inst8_1.status == STARTED:
            # update params
            pass
        
        # *inst8_2* updates
        waitOnFlip = False
        
        # if inst8_2 is starting this frame...
        if inst8_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst8_2.frameNStart = frameN  # exact frame index
            inst8_2.tStart = t  # local t and not account for scr refresh
            inst8_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst8_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            inst8_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(inst8_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(inst8_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if inst8_2.status == STARTED and not waitOnFlip:
            theseKeys = inst8_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _inst8_2_allKeys.extend(theseKeys)
            if len(_inst8_2_allKeys):
                inst8_2.keys = _inst8_2_allKeys[-1].name  # just the last key pressed
                inst8_2.rt = _inst8_2_allKeys[-1].rt
                inst8_2.duration = _inst8_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in inst8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "inst8" ---
    for thisComponent in inst8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('inst8.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "inst8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "inst9" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('inst9.started', globalClock.getTime(format='float'))
    inst9_2.keys = []
    inst9_2.rt = []
    _inst9_2_allKeys = []
    # keep track of which components have finished
    inst9Components = [inst9_1, inst9_2]
    for thisComponent in inst9Components:
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
    
    # --- Run Routine "inst9" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inst9_1* updates
        
        # if inst9_1 is starting this frame...
        if inst9_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst9_1.frameNStart = frameN  # exact frame index
            inst9_1.tStart = t  # local t and not account for scr refresh
            inst9_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst9_1, 'tStartRefresh')  # time at next scr refresh
            # update status
            inst9_1.status = STARTED
            inst9_1.setAutoDraw(True)
        
        # if inst9_1 is active this frame...
        if inst9_1.status == STARTED:
            # update params
            pass
        
        # *inst9_2* updates
        waitOnFlip = False
        
        # if inst9_2 is starting this frame...
        if inst9_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            inst9_2.frameNStart = frameN  # exact frame index
            inst9_2.tStart = t  # local t and not account for scr refresh
            inst9_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inst9_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            inst9_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(inst9_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(inst9_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if inst9_2.status == STARTED and not waitOnFlip:
            theseKeys = inst9_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _inst9_2_allKeys.extend(theseKeys)
            if len(_inst9_2_allKeys):
                inst9_2.keys = _inst9_2_allKeys[-1].name  # just the last key pressed
                inst9_2.rt = _inst9_2_allKeys[-1].rt
                inst9_2.duration = _inst9_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in inst9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "inst9" ---
    for thisComponent in inst9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('inst9.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "inst9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    rep3_loop = data.TrialHandler(nReps=3.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='rep3_loop')
    thisExp.addLoop(rep3_loop)  # add the loop to the experiment
    thisRep3_loop = rep3_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRep3_loop.rgb)
    if thisRep3_loop != None:
        for paramName in thisRep3_loop:
            globals()[paramName] = thisRep3_loop[paramName]
    
    for thisRep3_loop in rep3_loop:
        currentLoop = rep3_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisRep3_loop.rgb)
        if thisRep3_loop != None:
            for paramName in thisRep3_loop:
                globals()[paramName] = thisRep3_loop[paramName]
        
        # --- Prepare to start Routine "repsetup" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('repsetup.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        repsetupComponents = []
        for thisComponent in repsetupComponents:
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
        
        # --- Run Routine "repsetup" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in repsetupComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "repsetup" ---
        for thisComponent in repsetupComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('repsetup.stopped', globalClock.getTime(format='float'))
        # the Routine "repsetup" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        totalcount = data.TrialHandler(nReps=allRepsCount, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='totalcount')
        thisExp.addLoop(totalcount)  # add the loop to the experiment
        thisTotalcount = totalcount.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTotalcount.rgb)
        if thisTotalcount != None:
            for paramName in thisTotalcount:
                globals()[paramName] = thisTotalcount[paramName]
        
        for thisTotalcount in totalcount:
            currentLoop = totalcount
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTotalcount.rgb)
            if thisTotalcount != None:
                for paramName in thisTotalcount:
                    globals()[paramName] = thisTotalcount[paramName]
            
            # --- Prepare to start Routine "totalcounter" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('totalcounter.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code
            
            print('totalcounter code ' + str(totalCount))
            
            shuffle(orders)
            # keep track of which components have finished
            totalcounterComponents = []
            for thisComponent in totalcounterComponents:
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
            
            # --- Run Routine "totalcounter" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in totalcounterComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "totalcounter" ---
            for thisComponent in totalcounterComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('totalcounter.stopped', globalClock.getTime(format='float'))
            # the Routine "totalcounter" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            main_trials = data.TrialHandler(nReps=8.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='main_trials')
            thisExp.addLoop(main_trials)  # add the loop to the experiment
            thisMain_trial = main_trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisMain_trial.rgb)
            if thisMain_trial != None:
                for paramName in thisMain_trial:
                    globals()[paramName] = thisMain_trial[paramName]
            
            for thisMain_trial in main_trials:
                currentLoop = main_trials
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisMain_trial.rgb)
                if thisMain_trial != None:
                    for paramName in thisMain_trial:
                        globals()[paramName] = thisMain_trial[paramName]
                
                # --- Prepare to start Routine "trials_code" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('trials_code.started', globalClock.getTime(format='float'))
                # Run 'Begin Routine' code from code1
                print('trials code')
                print('total count ' + str(totalCount))
                # keep track of which components have finished
                trials_codeComponents = []
                for thisComponent in trials_codeComponents:
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
                
                # --- Run Routine "trials_code" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in trials_codeComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "trials_code" ---
                for thisComponent in trials_codeComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('trials_code.stopped', globalClock.getTime(format='float'))
                # the Routine "trials_code" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                OCC_termloop = data.TrialHandler(nReps=OCC_termloopReps, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='OCC_termloop')
                thisExp.addLoop(OCC_termloop)  # add the loop to the experiment
                thisOCC_termloop = OCC_termloop.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisOCC_termloop.rgb)
                if thisOCC_termloop != None:
                    for paramName in thisOCC_termloop:
                        globals()[paramName] = thisOCC_termloop[paramName]
                
                for thisOCC_termloop in OCC_termloop:
                    currentLoop = OCC_termloop
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisOCC_termloop.rgb)
                    if thisOCC_termloop != None:
                        for paramName in thisOCC_termloop:
                            globals()[paramName] = thisOCC_termloop[paramName]
                    
                    # set up handler to look after randomisation of conditions etc
                    OCC = data.TrialHandler(nReps=orders[0][main_trials.thisN], method='sequential', 
                        extraInfo=expInfo, originPath=-1,
                        trialList=data.importConditions("orthoCong_"+expInfo['group']+".xlsx", selection=str(SelectedRows_order[occReps])),
                        seed=None, name='OCC')
                    thisExp.addLoop(OCC)  # add the loop to the experiment
                    thisOCC = OCC.trialList[0]  # so we can initialise stimuli with some values
                    # abbreviate parameter names if possible (e.g. rgb = thisOCC.rgb)
                    if thisOCC != None:
                        for paramName in thisOCC:
                            globals()[paramName] = thisOCC[paramName]
                    
                    for thisOCC in OCC:
                        currentLoop = OCC
                        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                        # pause experiment here if requested
                        if thisExp.status == PAUSED:
                            pauseExperiment(
                                thisExp=thisExp, 
                                win=win, 
                                timers=[routineTimer], 
                                playbackComponents=[]
                        )
                        # abbreviate parameter names if possible (e.g. rgb = thisOCC.rgb)
                        if thisOCC != None:
                            for paramName in thisOCC:
                                globals()[paramName] = thisOCC[paramName]
                        
                        # --- Prepare to start Routine "Ortho_Corr_Cong" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('Ortho_Corr_Cong.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from occ6
                        if occReps == allRepsCount-1:
                            OCC_termloopReps = 0
                            continueRoutine = False
                        occ2.setText(plWord)
                        occ4.setText(conWord)
                        occ5.keys = []
                        occ5.rt = []
                        _occ5_allKeys = []
                        # keep track of which components have finished
                        Ortho_Corr_CongComponents = [occ1, occ2, occ3, occ4, occ5]
                        for thisComponent in Ortho_Corr_CongComponents:
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
                        
                        # --- Run Routine "Ortho_Corr_Cong" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine and routineTimer.getTime() < 5.4:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # *occ1* updates
                            
                            # if occ1 is starting this frame...
                            if occ1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                                # keep track of start time/frame for later
                                occ1.frameNStart = frameN  # exact frame index
                                occ1.tStart = t  # local t and not account for scr refresh
                                occ1.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(occ1, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                occ1.status = STARTED
                                occ1.setAutoDraw(True)
                            
                            # if occ1 is active this frame...
                            if occ1.status == STARTED:
                                # update params
                                pass
                            
                            # if occ1 is stopping this frame...
                            if occ1.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > occ1.tStartRefresh + .8-frameTolerance:
                                    # keep track of stop time/frame for later
                                    occ1.tStop = t  # not accounting for scr refresh
                                    occ1.tStopRefresh = tThisFlipGlobal  # on global time
                                    occ1.frameNStop = frameN  # exact frame index
                                    # update status
                                    occ1.status = FINISHED
                                    occ1.setAutoDraw(False)
                            
                            # *occ2* updates
                            
                            # if occ2 is starting this frame...
                            if occ2.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                                # keep track of start time/frame for later
                                occ2.frameNStart = frameN  # exact frame index
                                occ2.tStart = t  # local t and not account for scr refresh
                                occ2.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(occ2, 'tStartRefresh')  # time at next scr refresh
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'occ2.started')
                                # update status
                                occ2.status = STARTED
                                occ2.setAutoDraw(True)
                            
                            # if occ2 is active this frame...
                            if occ2.status == STARTED:
                                # update params
                                pass
                            
                            # if occ2 is stopping this frame...
                            if occ2.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > occ2.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    occ2.tStop = t  # not accounting for scr refresh
                                    occ2.tStopRefresh = tThisFlipGlobal  # on global time
                                    occ2.frameNStop = frameN  # exact frame index
                                    # add timestamp to datafile
                                    thisExp.timestampOnFlip(win, 'occ2.stopped')
                                    # update status
                                    occ2.status = FINISHED
                                    occ2.setAutoDraw(False)
                            
                            # *occ3* updates
                            
                            # if occ3 is starting this frame...
                            if occ3.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                                # keep track of start time/frame for later
                                occ3.frameNStart = frameN  # exact frame index
                                occ3.tStart = t  # local t and not account for scr refresh
                                occ3.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(occ3, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                occ3.status = STARTED
                                occ3.setAutoDraw(True)
                            
                            # if occ3 is active this frame...
                            if occ3.status == STARTED:
                                # update params
                                pass
                            
                            # if occ3 is stopping this frame...
                            if occ3.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > occ3.tStartRefresh + .5-frameTolerance:
                                    # keep track of stop time/frame for later
                                    occ3.tStop = t  # not accounting for scr refresh
                                    occ3.tStopRefresh = tThisFlipGlobal  # on global time
                                    occ3.frameNStop = frameN  # exact frame index
                                    # update status
                                    occ3.status = FINISHED
                                    occ3.setAutoDraw(False)
                            
                            # *occ4* updates
                            
                            # if occ4 is starting this frame...
                            if occ4.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                occ4.frameNStart = frameN  # exact frame index
                                occ4.tStart = t  # local t and not account for scr refresh
                                occ4.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(occ4, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                occ4.status = STARTED
                                occ4.setAutoDraw(True)
                            
                            # if occ4 is active this frame...
                            if occ4.status == STARTED:
                                # update params
                                pass
                            
                            # if occ4 is stopping this frame...
                            if occ4.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > occ4.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    occ4.tStop = t  # not accounting for scr refresh
                                    occ4.tStopRefresh = tThisFlipGlobal  # on global time
                                    occ4.frameNStop = frameN  # exact frame index
                                    # update status
                                    occ4.status = FINISHED
                                    occ4.setAutoDraw(False)
                            
                            # *occ5* updates
                            waitOnFlip = False
                            
                            # if occ5 is starting this frame...
                            if occ5.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                occ5.frameNStart = frameN  # exact frame index
                                occ5.tStart = t  # local t and not account for scr refresh
                                occ5.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(occ5, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                occ5.status = STARTED
                                # keyboard checking is just starting
                                waitOnFlip = True
                                win.callOnFlip(occ5.clock.reset)  # t=0 on next screen flip
                                win.callOnFlip(occ5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                            
                            # if occ5 is stopping this frame...
                            if occ5.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > occ5.tStartRefresh + 2-frameTolerance:
                                    # keep track of stop time/frame for later
                                    occ5.tStop = t  # not accounting for scr refresh
                                    occ5.tStopRefresh = tThisFlipGlobal  # on global time
                                    occ5.frameNStop = frameN  # exact frame index
                                    # update status
                                    occ5.status = FINISHED
                                    occ5.status = FINISHED
                            if occ5.status == STARTED and not waitOnFlip:
                                theseKeys = occ5.getKeys(keyList=['z','m'], ignoreKeys=["escape"], waitRelease=False)
                                _occ5_allKeys.extend(theseKeys)
                                if len(_occ5_allKeys):
                                    occ5.keys = _occ5_allKeys[-1].name  # just the last key pressed
                                    occ5.rt = _occ5_allKeys[-1].rt
                                    occ5.duration = _occ5_allKeys[-1].duration
                                    # a response ends the routine
                                    continueRoutine = False
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in Ortho_Corr_CongComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "Ortho_Corr_Cong" ---
                        for thisComponent in Ortho_Corr_CongComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('Ortho_Corr_Cong.stopped', globalClock.getTime(format='float'))
                        # Run 'End Routine' code from occ6
                        totalCount = totalCount+1
                        occCount = occCount+1
                        occReps = occReps+1
                        
                        thisExp.addData("condition", "OCC")
                        thisExp.addData("trigger", 21)
                        if occ5.keys == corrAns1:
                            thisExp.addData("response","correct")
                        elif occ5.keys == corrAns2:
                            thisExp.addData("response","incorrect")
                        else:
                            thisExp.addData("response","missed")
                        # check responses
                        if occ5.keys in ['', [], None]:  # No response was made
                            occ5.keys = None
                        OCC.addData('occ5.keys',occ5.keys)
                        if occ5.keys != None:  # we had a response
                            OCC.addData('occ5.rt', occ5.rt)
                            OCC.addData('occ5.duration', occ5.duration)
                        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                        if routineForceEnded:
                            routineTimer.reset()
                        else:
                            routineTimer.addTime(-5.400000)
                        
                        # --- Prepare to start Routine "occ_code" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('occ_code.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from occCode
                        if occCount ==1:
                            occCount = 0
                        # keep track of which components have finished
                        occ_codeComponents = []
                        for thisComponent in occ_codeComponents:
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
                        
                        # --- Run Routine "occ_code" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in occ_codeComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "occ_code" ---
                        for thisComponent in occ_codeComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('occ_code.stopped', globalClock.getTime(format='float'))
                        # the Routine "occ_code" was not non-slip safe, so reset the non-slip timer
                        routineTimer.reset()
                        thisExp.nextEntry()
                        
                        if thisSession is not None:
                            # if running in a Session with a Liaison client, send data up to now
                            thisSession.sendExperimentData()
                    # completed orders[0][main_trials.thisN] repeats of 'OCC'
                    
                # completed OCC_termloopReps repeats of 'OCC_termloop'
                
                
                # set up handler to look after randomisation of conditions etc
                OIC_termloop = data.TrialHandler(nReps=OIC_termloopReps, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='OIC_termloop')
                thisExp.addLoop(OIC_termloop)  # add the loop to the experiment
                thisOIC_termloop = OIC_termloop.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisOIC_termloop.rgb)
                if thisOIC_termloop != None:
                    for paramName in thisOIC_termloop:
                        globals()[paramName] = thisOIC_termloop[paramName]
                
                for thisOIC_termloop in OIC_termloop:
                    currentLoop = OIC_termloop
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisOIC_termloop.rgb)
                    if thisOIC_termloop != None:
                        for paramName in thisOIC_termloop:
                            globals()[paramName] = thisOIC_termloop[paramName]
                    
                    # set up handler to look after randomisation of conditions etc
                    OIC = data.TrialHandler(nReps=orders[1][main_trials.thisN], method='sequential', 
                        extraInfo=expInfo, originPath=-1,
                        trialList=data.importConditions("orthoCong_"+expInfo['group']+".xlsx", selection=str(SelectedRows_order[oicReps])),
                        seed=None, name='OIC')
                    thisExp.addLoop(OIC)  # add the loop to the experiment
                    thisOIC = OIC.trialList[0]  # so we can initialise stimuli with some values
                    # abbreviate parameter names if possible (e.g. rgb = thisOIC.rgb)
                    if thisOIC != None:
                        for paramName in thisOIC:
                            globals()[paramName] = thisOIC[paramName]
                    
                    for thisOIC in OIC:
                        currentLoop = OIC
                        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                        # pause experiment here if requested
                        if thisExp.status == PAUSED:
                            pauseExperiment(
                                thisExp=thisExp, 
                                win=win, 
                                timers=[routineTimer], 
                                playbackComponents=[]
                        )
                        # abbreviate parameter names if possible (e.g. rgb = thisOIC.rgb)
                        if thisOIC != None:
                            for paramName in thisOIC:
                                globals()[paramName] = thisOIC[paramName]
                        
                        # --- Prepare to start Routine "Ortho_Incorr_Cong" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('Ortho_Incorr_Cong.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from oic6
                        if oicReps == allRepsCount-1:
                            OIC_termloopReps = 0
                            continueRoutine = False
                        oic2.setText(plWord)
                        oic4.setText(incorr)
                        oic5.keys = []
                        oic5.rt = []
                        _oic5_allKeys = []
                        # keep track of which components have finished
                        Ortho_Incorr_CongComponents = [oic1, oic2, oic3, oic4, oic5]
                        for thisComponent in Ortho_Incorr_CongComponents:
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
                        
                        # --- Run Routine "Ortho_Incorr_Cong" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine and routineTimer.getTime() < 5.4:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # *oic1* updates
                            
                            # if oic1 is starting this frame...
                            if oic1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                                # keep track of start time/frame for later
                                oic1.frameNStart = frameN  # exact frame index
                                oic1.tStart = t  # local t and not account for scr refresh
                                oic1.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(oic1, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                oic1.status = STARTED
                                oic1.setAutoDraw(True)
                            
                            # if oic1 is active this frame...
                            if oic1.status == STARTED:
                                # update params
                                pass
                            
                            # if oic1 is stopping this frame...
                            if oic1.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > oic1.tStartRefresh + .8-frameTolerance:
                                    # keep track of stop time/frame for later
                                    oic1.tStop = t  # not accounting for scr refresh
                                    oic1.tStopRefresh = tThisFlipGlobal  # on global time
                                    oic1.frameNStop = frameN  # exact frame index
                                    # update status
                                    oic1.status = FINISHED
                                    oic1.setAutoDraw(False)
                            
                            # *oic2* updates
                            
                            # if oic2 is starting this frame...
                            if oic2.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                                # keep track of start time/frame for later
                                oic2.frameNStart = frameN  # exact frame index
                                oic2.tStart = t  # local t and not account for scr refresh
                                oic2.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(oic2, 'tStartRefresh')  # time at next scr refresh
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'oic2.started')
                                # update status
                                oic2.status = STARTED
                                oic2.setAutoDraw(True)
                            
                            # if oic2 is active this frame...
                            if oic2.status == STARTED:
                                # update params
                                pass
                            
                            # if oic2 is stopping this frame...
                            if oic2.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > oic2.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    oic2.tStop = t  # not accounting for scr refresh
                                    oic2.tStopRefresh = tThisFlipGlobal  # on global time
                                    oic2.frameNStop = frameN  # exact frame index
                                    # add timestamp to datafile
                                    thisExp.timestampOnFlip(win, 'oic2.stopped')
                                    # update status
                                    oic2.status = FINISHED
                                    oic2.setAutoDraw(False)
                            
                            # *oic3* updates
                            
                            # if oic3 is starting this frame...
                            if oic3.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                                # keep track of start time/frame for later
                                oic3.frameNStart = frameN  # exact frame index
                                oic3.tStart = t  # local t and not account for scr refresh
                                oic3.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(oic3, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                oic3.status = STARTED
                                oic3.setAutoDraw(True)
                            
                            # if oic3 is active this frame...
                            if oic3.status == STARTED:
                                # update params
                                pass
                            
                            # if oic3 is stopping this frame...
                            if oic3.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > oic3.tStartRefresh + .5-frameTolerance:
                                    # keep track of stop time/frame for later
                                    oic3.tStop = t  # not accounting for scr refresh
                                    oic3.tStopRefresh = tThisFlipGlobal  # on global time
                                    oic3.frameNStop = frameN  # exact frame index
                                    # update status
                                    oic3.status = FINISHED
                                    oic3.setAutoDraw(False)
                            
                            # *oic4* updates
                            
                            # if oic4 is starting this frame...
                            if oic4.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                oic4.frameNStart = frameN  # exact frame index
                                oic4.tStart = t  # local t and not account for scr refresh
                                oic4.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(oic4, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                oic4.status = STARTED
                                oic4.setAutoDraw(True)
                            
                            # if oic4 is active this frame...
                            if oic4.status == STARTED:
                                # update params
                                pass
                            
                            # if oic4 is stopping this frame...
                            if oic4.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > oic4.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    oic4.tStop = t  # not accounting for scr refresh
                                    oic4.tStopRefresh = tThisFlipGlobal  # on global time
                                    oic4.frameNStop = frameN  # exact frame index
                                    # update status
                                    oic4.status = FINISHED
                                    oic4.setAutoDraw(False)
                            
                            # *oic5* updates
                            waitOnFlip = False
                            
                            # if oic5 is starting this frame...
                            if oic5.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                oic5.frameNStart = frameN  # exact frame index
                                oic5.tStart = t  # local t and not account for scr refresh
                                oic5.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(oic5, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                oic5.status = STARTED
                                # keyboard checking is just starting
                                waitOnFlip = True
                                win.callOnFlip(oic5.clock.reset)  # t=0 on next screen flip
                                win.callOnFlip(oic5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                            
                            # if oic5 is stopping this frame...
                            if oic5.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > oic5.tStartRefresh + 2-frameTolerance:
                                    # keep track of stop time/frame for later
                                    oic5.tStop = t  # not accounting for scr refresh
                                    oic5.tStopRefresh = tThisFlipGlobal  # on global time
                                    oic5.frameNStop = frameN  # exact frame index
                                    # update status
                                    oic5.status = FINISHED
                                    oic5.status = FINISHED
                            if oic5.status == STARTED and not waitOnFlip:
                                theseKeys = oic5.getKeys(keyList=['z','m'], ignoreKeys=["escape"], waitRelease=False)
                                _oic5_allKeys.extend(theseKeys)
                                if len(_oic5_allKeys):
                                    oic5.keys = _oic5_allKeys[-1].name  # just the last key pressed
                                    oic5.rt = _oic5_allKeys[-1].rt
                                    oic5.duration = _oic5_allKeys[-1].duration
                                    # a response ends the routine
                                    continueRoutine = False
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in Ortho_Incorr_CongComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "Ortho_Incorr_Cong" ---
                        for thisComponent in Ortho_Incorr_CongComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('Ortho_Incorr_Cong.stopped', globalClock.getTime(format='float'))
                        # Run 'End Routine' code from oic6
                        totalCount = totalCount+1
                        oicCount = oicCount+1
                        oicReps = oicReps+1
                        
                        thisExp.addData("condition", "OIC")
                        thisExp.addData("trigger", 22)
                        if oic5.keys == corrAns2:
                            thisExp.addData("response","correct")
                        elif oic5.keys == corrAns1:
                            thisExp.addData("response","incorrect")
                        else:
                            thisExp.addData("response","missed")
                        
                        # check responses
                        if oic5.keys in ['', [], None]:  # No response was made
                            oic5.keys = None
                        OIC.addData('oic5.keys',oic5.keys)
                        if oic5.keys != None:  # we had a response
                            OIC.addData('oic5.rt', oic5.rt)
                            OIC.addData('oic5.duration', oic5.duration)
                        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                        if routineForceEnded:
                            routineTimer.reset()
                        else:
                            routineTimer.addTime(-5.400000)
                        
                        # --- Prepare to start Routine "oic_code" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('oic_code.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from oicCode
                        if oicCount == 1:
                            oicCount = 0
                        # keep track of which components have finished
                        oic_codeComponents = []
                        for thisComponent in oic_codeComponents:
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
                        
                        # --- Run Routine "oic_code" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in oic_codeComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "oic_code" ---
                        for thisComponent in oic_codeComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('oic_code.stopped', globalClock.getTime(format='float'))
                        # the Routine "oic_code" was not non-slip safe, so reset the non-slip timer
                        routineTimer.reset()
                        thisExp.nextEntry()
                        
                        if thisSession is not None:
                            # if running in a Session with a Liaison client, send data up to now
                            thisSession.sendExperimentData()
                    # completed orders[1][main_trials.thisN] repeats of 'OIC'
                    
                # completed OIC_termloopReps repeats of 'OIC_termloop'
                
                
                # set up handler to look after randomisation of conditions etc
                OCI_termloop = data.TrialHandler(nReps=OCI_termloopReps, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='OCI_termloop')
                thisExp.addLoop(OCI_termloop)  # add the loop to the experiment
                thisOCI_termloop = OCI_termloop.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisOCI_termloop.rgb)
                if thisOCI_termloop != None:
                    for paramName in thisOCI_termloop:
                        globals()[paramName] = thisOCI_termloop[paramName]
                
                for thisOCI_termloop in OCI_termloop:
                    currentLoop = OCI_termloop
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisOCI_termloop.rgb)
                    if thisOCI_termloop != None:
                        for paramName in thisOCI_termloop:
                            globals()[paramName] = thisOCI_termloop[paramName]
                    
                    # set up handler to look after randomisation of conditions etc
                    OCI = data.TrialHandler(nReps=orders[2][main_trials.thisN], method='sequential', 
                        extraInfo=expInfo, originPath=-1,
                        trialList=data.importConditions("orthoIncong_"+expInfo['group']+".xlsx", selection=str(SelectedRows_order[ociReps])),
                        seed=None, name='OCI')
                    thisExp.addLoop(OCI)  # add the loop to the experiment
                    thisOCI = OCI.trialList[0]  # so we can initialise stimuli with some values
                    # abbreviate parameter names if possible (e.g. rgb = thisOCI.rgb)
                    if thisOCI != None:
                        for paramName in thisOCI:
                            globals()[paramName] = thisOCI[paramName]
                    
                    for thisOCI in OCI:
                        currentLoop = OCI
                        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                        # pause experiment here if requested
                        if thisExp.status == PAUSED:
                            pauseExperiment(
                                thisExp=thisExp, 
                                win=win, 
                                timers=[routineTimer], 
                                playbackComponents=[]
                        )
                        # abbreviate parameter names if possible (e.g. rgb = thisOCI.rgb)
                        if thisOCI != None:
                            for paramName in thisOCI:
                                globals()[paramName] = thisOCI[paramName]
                        
                        # --- Prepare to start Routine "Ortho_Corr_Incong" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('Ortho_Corr_Incong.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from oci6
                        if ociReps == allRepsCount-1:
                            OCI_termloopReps = 0
                            continueRoutine = False
                        oci2.setText(plWord)
                        oci4.setText(conWord)
                        oci5.keys = []
                        oci5.rt = []
                        _oci5_allKeys = []
                        # keep track of which components have finished
                        Ortho_Corr_IncongComponents = [oci1, oci2, oci3, oci4, oci5]
                        for thisComponent in Ortho_Corr_IncongComponents:
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
                        
                        # --- Run Routine "Ortho_Corr_Incong" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine and routineTimer.getTime() < 5.4:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # *oci1* updates
                            
                            # if oci1 is starting this frame...
                            if oci1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                                # keep track of start time/frame for later
                                oci1.frameNStart = frameN  # exact frame index
                                oci1.tStart = t  # local t and not account for scr refresh
                                oci1.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(oci1, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                oci1.status = STARTED
                                oci1.setAutoDraw(True)
                            
                            # if oci1 is active this frame...
                            if oci1.status == STARTED:
                                # update params
                                pass
                            
                            # if oci1 is stopping this frame...
                            if oci1.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > oci1.tStartRefresh + .8-frameTolerance:
                                    # keep track of stop time/frame for later
                                    oci1.tStop = t  # not accounting for scr refresh
                                    oci1.tStopRefresh = tThisFlipGlobal  # on global time
                                    oci1.frameNStop = frameN  # exact frame index
                                    # update status
                                    oci1.status = FINISHED
                                    oci1.setAutoDraw(False)
                            
                            # *oci2* updates
                            
                            # if oci2 is starting this frame...
                            if oci2.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                                # keep track of start time/frame for later
                                oci2.frameNStart = frameN  # exact frame index
                                oci2.tStart = t  # local t and not account for scr refresh
                                oci2.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(oci2, 'tStartRefresh')  # time at next scr refresh
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'oci2.started')
                                # update status
                                oci2.status = STARTED
                                oci2.setAutoDraw(True)
                            
                            # if oci2 is active this frame...
                            if oci2.status == STARTED:
                                # update params
                                pass
                            
                            # if oci2 is stopping this frame...
                            if oci2.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > oci2.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    oci2.tStop = t  # not accounting for scr refresh
                                    oci2.tStopRefresh = tThisFlipGlobal  # on global time
                                    oci2.frameNStop = frameN  # exact frame index
                                    # add timestamp to datafile
                                    thisExp.timestampOnFlip(win, 'oci2.stopped')
                                    # update status
                                    oci2.status = FINISHED
                                    oci2.setAutoDraw(False)
                            
                            # *oci3* updates
                            
                            # if oci3 is starting this frame...
                            if oci3.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                                # keep track of start time/frame for later
                                oci3.frameNStart = frameN  # exact frame index
                                oci3.tStart = t  # local t and not account for scr refresh
                                oci3.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(oci3, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                oci3.status = STARTED
                                oci3.setAutoDraw(True)
                            
                            # if oci3 is active this frame...
                            if oci3.status == STARTED:
                                # update params
                                pass
                            
                            # if oci3 is stopping this frame...
                            if oci3.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > oci3.tStartRefresh + .5-frameTolerance:
                                    # keep track of stop time/frame for later
                                    oci3.tStop = t  # not accounting for scr refresh
                                    oci3.tStopRefresh = tThisFlipGlobal  # on global time
                                    oci3.frameNStop = frameN  # exact frame index
                                    # update status
                                    oci3.status = FINISHED
                                    oci3.setAutoDraw(False)
                            
                            # *oci4* updates
                            
                            # if oci4 is starting this frame...
                            if oci4.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                oci4.frameNStart = frameN  # exact frame index
                                oci4.tStart = t  # local t and not account for scr refresh
                                oci4.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(oci4, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                oci4.status = STARTED
                                oci4.setAutoDraw(True)
                            
                            # if oci4 is active this frame...
                            if oci4.status == STARTED:
                                # update params
                                pass
                            
                            # if oci4 is stopping this frame...
                            if oci4.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > oci4.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    oci4.tStop = t  # not accounting for scr refresh
                                    oci4.tStopRefresh = tThisFlipGlobal  # on global time
                                    oci4.frameNStop = frameN  # exact frame index
                                    # update status
                                    oci4.status = FINISHED
                                    oci4.setAutoDraw(False)
                            
                            # *oci5* updates
                            waitOnFlip = False
                            
                            # if oci5 is starting this frame...
                            if oci5.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                oci5.frameNStart = frameN  # exact frame index
                                oci5.tStart = t  # local t and not account for scr refresh
                                oci5.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(oci5, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                oci5.status = STARTED
                                # keyboard checking is just starting
                                waitOnFlip = True
                                win.callOnFlip(oci5.clock.reset)  # t=0 on next screen flip
                                win.callOnFlip(oci5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                            
                            # if oci5 is stopping this frame...
                            if oci5.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > oci5.tStartRefresh + 2-frameTolerance:
                                    # keep track of stop time/frame for later
                                    oci5.tStop = t  # not accounting for scr refresh
                                    oci5.tStopRefresh = tThisFlipGlobal  # on global time
                                    oci5.frameNStop = frameN  # exact frame index
                                    # update status
                                    oci5.status = FINISHED
                                    oci5.status = FINISHED
                            if oci5.status == STARTED and not waitOnFlip:
                                theseKeys = oci5.getKeys(keyList=['z','m'], ignoreKeys=["escape"], waitRelease=False)
                                _oci5_allKeys.extend(theseKeys)
                                if len(_oci5_allKeys):
                                    oci5.keys = _oci5_allKeys[-1].name  # just the last key pressed
                                    oci5.rt = _oci5_allKeys[-1].rt
                                    oci5.duration = _oci5_allKeys[-1].duration
                                    # a response ends the routine
                                    continueRoutine = False
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in Ortho_Corr_IncongComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "Ortho_Corr_Incong" ---
                        for thisComponent in Ortho_Corr_IncongComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('Ortho_Corr_Incong.stopped', globalClock.getTime(format='float'))
                        # Run 'End Routine' code from oci6
                        totalCount = totalCount+1
                        ociCount = ociCount+1
                        ociReps = ociReps+1
                        
                        thisExp.addData("condition", "OCI")
                        thisExp.addData("trigger", 23)
                        if oci5.keys == corrAns1:
                            thisExp.addData("response","correct")
                        elif oci5.keys == corrAns2:
                            thisExp.addData("response","incorrect")
                        else:
                            thisExp.addData("response","missed")
                        
                        # check responses
                        if oci5.keys in ['', [], None]:  # No response was made
                            oci5.keys = None
                        OCI.addData('oci5.keys',oci5.keys)
                        if oci5.keys != None:  # we had a response
                            OCI.addData('oci5.rt', oci5.rt)
                            OCI.addData('oci5.duration', oci5.duration)
                        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                        if routineForceEnded:
                            routineTimer.reset()
                        else:
                            routineTimer.addTime(-5.400000)
                        
                        # --- Prepare to start Routine "oci_code" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('oci_code.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from ociCode
                        if ociCount == 1:
                            ociCount = 0
                        # keep track of which components have finished
                        oci_codeComponents = []
                        for thisComponent in oci_codeComponents:
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
                        
                        # --- Run Routine "oci_code" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in oci_codeComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "oci_code" ---
                        for thisComponent in oci_codeComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('oci_code.stopped', globalClock.getTime(format='float'))
                        # the Routine "oci_code" was not non-slip safe, so reset the non-slip timer
                        routineTimer.reset()
                        thisExp.nextEntry()
                        
                        if thisSession is not None:
                            # if running in a Session with a Liaison client, send data up to now
                            thisSession.sendExperimentData()
                    # completed orders[2][main_trials.thisN] repeats of 'OCI'
                    
                # completed OCI_termloopReps repeats of 'OCI_termloop'
                
                
                # set up handler to look after randomisation of conditions etc
                OII_termloop = data.TrialHandler(nReps=OII_termloopReps, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='OII_termloop')
                thisExp.addLoop(OII_termloop)  # add the loop to the experiment
                thisOII_termloop = OII_termloop.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisOII_termloop.rgb)
                if thisOII_termloop != None:
                    for paramName in thisOII_termloop:
                        globals()[paramName] = thisOII_termloop[paramName]
                
                for thisOII_termloop in OII_termloop:
                    currentLoop = OII_termloop
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisOII_termloop.rgb)
                    if thisOII_termloop != None:
                        for paramName in thisOII_termloop:
                            globals()[paramName] = thisOII_termloop[paramName]
                    
                    # set up handler to look after randomisation of conditions etc
                    OII = data.TrialHandler(nReps=orders[3][main_trials.thisN], method='sequential', 
                        extraInfo=expInfo, originPath=-1,
                        trialList=data.importConditions("orthoIncong_"+expInfo['group']+".xlsx", selection=str(SelectedRows_order[oiiReps])),
                        seed=None, name='OII')
                    thisExp.addLoop(OII)  # add the loop to the experiment
                    thisOII = OII.trialList[0]  # so we can initialise stimuli with some values
                    # abbreviate parameter names if possible (e.g. rgb = thisOII.rgb)
                    if thisOII != None:
                        for paramName in thisOII:
                            globals()[paramName] = thisOII[paramName]
                    
                    for thisOII in OII:
                        currentLoop = OII
                        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                        # pause experiment here if requested
                        if thisExp.status == PAUSED:
                            pauseExperiment(
                                thisExp=thisExp, 
                                win=win, 
                                timers=[routineTimer], 
                                playbackComponents=[]
                        )
                        # abbreviate parameter names if possible (e.g. rgb = thisOII.rgb)
                        if thisOII != None:
                            for paramName in thisOII:
                                globals()[paramName] = thisOII[paramName]
                        
                        # --- Prepare to start Routine "Ortho_Incorr_Incong" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('Ortho_Incorr_Incong.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from oii6
                        if oiiReps == allRepsCount-1:
                            OII_termloopReps = 0
                            continueRoutine = False
                        oii2.setText(plWord)
                        oii4.setText(incorr)
                        oii5.keys = []
                        oii5.rt = []
                        _oii5_allKeys = []
                        # keep track of which components have finished
                        Ortho_Incorr_IncongComponents = [oii1, oii2, oii3, oii4, oii5]
                        for thisComponent in Ortho_Incorr_IncongComponents:
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
                        
                        # --- Run Routine "Ortho_Incorr_Incong" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine and routineTimer.getTime() < 5.4:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # *oii1* updates
                            
                            # if oii1 is starting this frame...
                            if oii1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                                # keep track of start time/frame for later
                                oii1.frameNStart = frameN  # exact frame index
                                oii1.tStart = t  # local t and not account for scr refresh
                                oii1.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(oii1, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                oii1.status = STARTED
                                oii1.setAutoDraw(True)
                            
                            # if oii1 is active this frame...
                            if oii1.status == STARTED:
                                # update params
                                pass
                            
                            # if oii1 is stopping this frame...
                            if oii1.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > oii1.tStartRefresh + .8-frameTolerance:
                                    # keep track of stop time/frame for later
                                    oii1.tStop = t  # not accounting for scr refresh
                                    oii1.tStopRefresh = tThisFlipGlobal  # on global time
                                    oii1.frameNStop = frameN  # exact frame index
                                    # update status
                                    oii1.status = FINISHED
                                    oii1.setAutoDraw(False)
                            
                            # *oii2* updates
                            
                            # if oii2 is starting this frame...
                            if oii2.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                                # keep track of start time/frame for later
                                oii2.frameNStart = frameN  # exact frame index
                                oii2.tStart = t  # local t and not account for scr refresh
                                oii2.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(oii2, 'tStartRefresh')  # time at next scr refresh
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'oii2.started')
                                # update status
                                oii2.status = STARTED
                                oii2.setAutoDraw(True)
                            
                            # if oii2 is active this frame...
                            if oii2.status == STARTED:
                                # update params
                                pass
                            
                            # if oii2 is stopping this frame...
                            if oii2.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > oii2.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    oii2.tStop = t  # not accounting for scr refresh
                                    oii2.tStopRefresh = tThisFlipGlobal  # on global time
                                    oii2.frameNStop = frameN  # exact frame index
                                    # add timestamp to datafile
                                    thisExp.timestampOnFlip(win, 'oii2.stopped')
                                    # update status
                                    oii2.status = FINISHED
                                    oii2.setAutoDraw(False)
                            
                            # *oii3* updates
                            
                            # if oii3 is starting this frame...
                            if oii3.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                                # keep track of start time/frame for later
                                oii3.frameNStart = frameN  # exact frame index
                                oii3.tStart = t  # local t and not account for scr refresh
                                oii3.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(oii3, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                oii3.status = STARTED
                                oii3.setAutoDraw(True)
                            
                            # if oii3 is active this frame...
                            if oii3.status == STARTED:
                                # update params
                                pass
                            
                            # if oii3 is stopping this frame...
                            if oii3.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > oii3.tStartRefresh + .5-frameTolerance:
                                    # keep track of stop time/frame for later
                                    oii3.tStop = t  # not accounting for scr refresh
                                    oii3.tStopRefresh = tThisFlipGlobal  # on global time
                                    oii3.frameNStop = frameN  # exact frame index
                                    # update status
                                    oii3.status = FINISHED
                                    oii3.setAutoDraw(False)
                            
                            # *oii4* updates
                            
                            # if oii4 is starting this frame...
                            if oii4.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                oii4.frameNStart = frameN  # exact frame index
                                oii4.tStart = t  # local t and not account for scr refresh
                                oii4.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(oii4, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                oii4.status = STARTED
                                oii4.setAutoDraw(True)
                            
                            # if oii4 is active this frame...
                            if oii4.status == STARTED:
                                # update params
                                pass
                            
                            # if oii4 is stopping this frame...
                            if oii4.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > oii4.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    oii4.tStop = t  # not accounting for scr refresh
                                    oii4.tStopRefresh = tThisFlipGlobal  # on global time
                                    oii4.frameNStop = frameN  # exact frame index
                                    # update status
                                    oii4.status = FINISHED
                                    oii4.setAutoDraw(False)
                            
                            # *oii5* updates
                            waitOnFlip = False
                            
                            # if oii5 is starting this frame...
                            if oii5.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                oii5.frameNStart = frameN  # exact frame index
                                oii5.tStart = t  # local t and not account for scr refresh
                                oii5.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(oii5, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                oii5.status = STARTED
                                # keyboard checking is just starting
                                waitOnFlip = True
                                win.callOnFlip(oii5.clock.reset)  # t=0 on next screen flip
                                win.callOnFlip(oii5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                            
                            # if oii5 is stopping this frame...
                            if oii5.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > oii5.tStartRefresh + 2-frameTolerance:
                                    # keep track of stop time/frame for later
                                    oii5.tStop = t  # not accounting for scr refresh
                                    oii5.tStopRefresh = tThisFlipGlobal  # on global time
                                    oii5.frameNStop = frameN  # exact frame index
                                    # update status
                                    oii5.status = FINISHED
                                    oii5.status = FINISHED
                            if oii5.status == STARTED and not waitOnFlip:
                                theseKeys = oii5.getKeys(keyList=['z','m'], ignoreKeys=["escape"], waitRelease=False)
                                _oii5_allKeys.extend(theseKeys)
                                if len(_oii5_allKeys):
                                    oii5.keys = _oii5_allKeys[-1].name  # just the last key pressed
                                    oii5.rt = _oii5_allKeys[-1].rt
                                    oii5.duration = _oii5_allKeys[-1].duration
                                    # a response ends the routine
                                    continueRoutine = False
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in Ortho_Incorr_IncongComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "Ortho_Incorr_Incong" ---
                        for thisComponent in Ortho_Incorr_IncongComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('Ortho_Incorr_Incong.stopped', globalClock.getTime(format='float'))
                        # Run 'End Routine' code from oii6
                        totalCount = totalCount+1
                        oiiCount = oiiCount+1
                        oiiReps = oiiReps+1
                        
                        thisExp.addData("condition", "OII")
                        thisExp.addData("trigger", 24)
                        if oii5.keys == corrAns2:
                            thisExp.addData("response","correct")
                        elif oii5.keys == corrAns1:
                            thisExp.addData("response","incorrect")
                        else:
                            thisExp.addData("response","missed")
                        
                        # check responses
                        if oii5.keys in ['', [], None]:  # No response was made
                            oii5.keys = None
                        OII.addData('oii5.keys',oii5.keys)
                        if oii5.keys != None:  # we had a response
                            OII.addData('oii5.rt', oii5.rt)
                            OII.addData('oii5.duration', oii5.duration)
                        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                        if routineForceEnded:
                            routineTimer.reset()
                        else:
                            routineTimer.addTime(-5.400000)
                        
                        # --- Prepare to start Routine "oii_code" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('oii_code.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from oiiCode
                        if oiiCount == 1:
                            oiiCount = 0
                        # keep track of which components have finished
                        oii_codeComponents = []
                        for thisComponent in oii_codeComponents:
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
                        
                        # --- Run Routine "oii_code" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in oii_codeComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "oii_code" ---
                        for thisComponent in oii_codeComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('oii_code.stopped', globalClock.getTime(format='float'))
                        # the Routine "oii_code" was not non-slip safe, so reset the non-slip timer
                        routineTimer.reset()
                        thisExp.nextEntry()
                        
                        if thisSession is not None:
                            # if running in a Session with a Liaison client, send data up to now
                            thisSession.sendExperimentData()
                    # completed orders[3][main_trials.thisN] repeats of 'OII'
                    
                # completed OII_termloopReps repeats of 'OII_termloop'
                
                
                # set up handler to look after randomisation of conditions etc
                ICC_termloop = data.TrialHandler(nReps=ICC_termloopReps, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='ICC_termloop')
                thisExp.addLoop(ICC_termloop)  # add the loop to the experiment
                thisICC_termloop = ICC_termloop.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisICC_termloop.rgb)
                if thisICC_termloop != None:
                    for paramName in thisICC_termloop:
                        globals()[paramName] = thisICC_termloop[paramName]
                
                for thisICC_termloop in ICC_termloop:
                    currentLoop = ICC_termloop
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisICC_termloop.rgb)
                    if thisICC_termloop != None:
                        for paramName in thisICC_termloop:
                            globals()[paramName] = thisICC_termloop[paramName]
                    
                    # set up handler to look after randomisation of conditions etc
                    ICC = data.TrialHandler(nReps=orders[4][main_trials.thisN], method='sequential', 
                        extraInfo=expInfo, originPath=-1,
                        trialList=data.importConditions("imgCong_"+expInfo['group']+".xlsx", selection=str(SelectedRows_order[iccReps])),
                        seed=None, name='ICC')
                    thisExp.addLoop(ICC)  # add the loop to the experiment
                    thisICC = ICC.trialList[0]  # so we can initialise stimuli with some values
                    # abbreviate parameter names if possible (e.g. rgb = thisICC.rgb)
                    if thisICC != None:
                        for paramName in thisICC:
                            globals()[paramName] = thisICC[paramName]
                    
                    for thisICC in ICC:
                        currentLoop = ICC
                        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                        # pause experiment here if requested
                        if thisExp.status == PAUSED:
                            pauseExperiment(
                                thisExp=thisExp, 
                                win=win, 
                                timers=[routineTimer], 
                                playbackComponents=[]
                        )
                        # abbreviate parameter names if possible (e.g. rgb = thisICC.rgb)
                        if thisICC != None:
                            for paramName in thisICC:
                                globals()[paramName] = thisICC[paramName]
                        
                        # --- Prepare to start Routine "Img_Corr_Cong" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('Img_Corr_Cong.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from icc6
                        if iccReps == allRepsCount-1:
                            ICC_termloopReps = 0
                            continueRoutine = False
                        icc2.setImage(img)
                        icc4.setText(conWord)
                        icc5.keys = []
                        icc5.rt = []
                        _icc5_allKeys = []
                        # keep track of which components have finished
                        Img_Corr_CongComponents = [icc1, icc2, icc3, icc4, icc5]
                        for thisComponent in Img_Corr_CongComponents:
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
                        
                        # --- Run Routine "Img_Corr_Cong" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine and routineTimer.getTime() < 5.4:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # *icc1* updates
                            
                            # if icc1 is starting this frame...
                            if icc1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                                # keep track of start time/frame for later
                                icc1.frameNStart = frameN  # exact frame index
                                icc1.tStart = t  # local t and not account for scr refresh
                                icc1.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(icc1, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                icc1.status = STARTED
                                icc1.setAutoDraw(True)
                            
                            # if icc1 is active this frame...
                            if icc1.status == STARTED:
                                # update params
                                pass
                            
                            # if icc1 is stopping this frame...
                            if icc1.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > icc1.tStartRefresh + .8-frameTolerance:
                                    # keep track of stop time/frame for later
                                    icc1.tStop = t  # not accounting for scr refresh
                                    icc1.tStopRefresh = tThisFlipGlobal  # on global time
                                    icc1.frameNStop = frameN  # exact frame index
                                    # update status
                                    icc1.status = FINISHED
                                    icc1.setAutoDraw(False)
                            
                            # *icc2* updates
                            
                            # if icc2 is starting this frame...
                            if icc2.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                                # keep track of start time/frame for later
                                icc2.frameNStart = frameN  # exact frame index
                                icc2.tStart = t  # local t and not account for scr refresh
                                icc2.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(icc2, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                icc2.status = STARTED
                                icc2.setAutoDraw(True)
                            
                            # if icc2 is active this frame...
                            if icc2.status == STARTED:
                                # update params
                                pass
                            
                            # if icc2 is stopping this frame...
                            if icc2.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > icc2.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    icc2.tStop = t  # not accounting for scr refresh
                                    icc2.tStopRefresh = tThisFlipGlobal  # on global time
                                    icc2.frameNStop = frameN  # exact frame index
                                    # update status
                                    icc2.status = FINISHED
                                    icc2.setAutoDraw(False)
                            
                            # *icc3* updates
                            
                            # if icc3 is starting this frame...
                            if icc3.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                                # keep track of start time/frame for later
                                icc3.frameNStart = frameN  # exact frame index
                                icc3.tStart = t  # local t and not account for scr refresh
                                icc3.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(icc3, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                icc3.status = STARTED
                                icc3.setAutoDraw(True)
                            
                            # if icc3 is active this frame...
                            if icc3.status == STARTED:
                                # update params
                                pass
                            
                            # if icc3 is stopping this frame...
                            if icc3.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > icc3.tStartRefresh + .5-frameTolerance:
                                    # keep track of stop time/frame for later
                                    icc3.tStop = t  # not accounting for scr refresh
                                    icc3.tStopRefresh = tThisFlipGlobal  # on global time
                                    icc3.frameNStop = frameN  # exact frame index
                                    # update status
                                    icc3.status = FINISHED
                                    icc3.setAutoDraw(False)
                            
                            # *icc4* updates
                            
                            # if icc4 is starting this frame...
                            if icc4.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                icc4.frameNStart = frameN  # exact frame index
                                icc4.tStart = t  # local t and not account for scr refresh
                                icc4.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(icc4, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                icc4.status = STARTED
                                icc4.setAutoDraw(True)
                            
                            # if icc4 is active this frame...
                            if icc4.status == STARTED:
                                # update params
                                pass
                            
                            # if icc4 is stopping this frame...
                            if icc4.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > icc4.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    icc4.tStop = t  # not accounting for scr refresh
                                    icc4.tStopRefresh = tThisFlipGlobal  # on global time
                                    icc4.frameNStop = frameN  # exact frame index
                                    # update status
                                    icc4.status = FINISHED
                                    icc4.setAutoDraw(False)
                            
                            # *icc5* updates
                            waitOnFlip = False
                            
                            # if icc5 is starting this frame...
                            if icc5.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                icc5.frameNStart = frameN  # exact frame index
                                icc5.tStart = t  # local t and not account for scr refresh
                                icc5.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(icc5, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                icc5.status = STARTED
                                # keyboard checking is just starting
                                waitOnFlip = True
                                win.callOnFlip(icc5.clock.reset)  # t=0 on next screen flip
                                win.callOnFlip(icc5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                            
                            # if icc5 is stopping this frame...
                            if icc5.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > icc5.tStartRefresh + 2-frameTolerance:
                                    # keep track of stop time/frame for later
                                    icc5.tStop = t  # not accounting for scr refresh
                                    icc5.tStopRefresh = tThisFlipGlobal  # on global time
                                    icc5.frameNStop = frameN  # exact frame index
                                    # update status
                                    icc5.status = FINISHED
                                    icc5.status = FINISHED
                            if icc5.status == STARTED and not waitOnFlip:
                                theseKeys = icc5.getKeys(keyList=['z','m'], ignoreKeys=["escape"], waitRelease=False)
                                _icc5_allKeys.extend(theseKeys)
                                if len(_icc5_allKeys):
                                    icc5.keys = _icc5_allKeys[-1].name  # just the last key pressed
                                    icc5.rt = _icc5_allKeys[-1].rt
                                    icc5.duration = _icc5_allKeys[-1].duration
                                    # a response ends the routine
                                    continueRoutine = False
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in Img_Corr_CongComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "Img_Corr_Cong" ---
                        for thisComponent in Img_Corr_CongComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('Img_Corr_Cong.stopped', globalClock.getTime(format='float'))
                        # Run 'End Routine' code from icc6
                        totalCount = totalCount+1
                        iccCount = iccCount+1
                        iccReps = iccReps+1
                        
                        thisExp.addData("condition", "ICC")
                        thisExp.addData("trigger", 31)
                        if icc5.keys == corrAns1:
                            thisExp.addData("response","correct")
                        elif icc5.keys == corrAns2:
                            thisExp.addData("response","incorrect")
                        else:
                            thisExp.addData("response","missed")
                        # check responses
                        if icc5.keys in ['', [], None]:  # No response was made
                            icc5.keys = None
                        ICC.addData('icc5.keys',icc5.keys)
                        if icc5.keys != None:  # we had a response
                            ICC.addData('icc5.rt', icc5.rt)
                            ICC.addData('icc5.duration', icc5.duration)
                        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                        if routineForceEnded:
                            routineTimer.reset()
                        else:
                            routineTimer.addTime(-5.400000)
                        
                        # --- Prepare to start Routine "icc_code" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('icc_code.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from iccCode
                        if iccCount == 1:
                            iccCount = 0
                        # keep track of which components have finished
                        icc_codeComponents = []
                        for thisComponent in icc_codeComponents:
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
                        
                        # --- Run Routine "icc_code" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in icc_codeComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "icc_code" ---
                        for thisComponent in icc_codeComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('icc_code.stopped', globalClock.getTime(format='float'))
                        # the Routine "icc_code" was not non-slip safe, so reset the non-slip timer
                        routineTimer.reset()
                        thisExp.nextEntry()
                        
                        if thisSession is not None:
                            # if running in a Session with a Liaison client, send data up to now
                            thisSession.sendExperimentData()
                    # completed orders[4][main_trials.thisN] repeats of 'ICC'
                    
                # completed ICC_termloopReps repeats of 'ICC_termloop'
                
                
                # set up handler to look after randomisation of conditions etc
                IIC_termloop = data.TrialHandler(nReps=IIC_termloopReps, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='IIC_termloop')
                thisExp.addLoop(IIC_termloop)  # add the loop to the experiment
                thisIIC_termloop = IIC_termloop.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisIIC_termloop.rgb)
                if thisIIC_termloop != None:
                    for paramName in thisIIC_termloop:
                        globals()[paramName] = thisIIC_termloop[paramName]
                
                for thisIIC_termloop in IIC_termloop:
                    currentLoop = IIC_termloop
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisIIC_termloop.rgb)
                    if thisIIC_termloop != None:
                        for paramName in thisIIC_termloop:
                            globals()[paramName] = thisIIC_termloop[paramName]
                    
                    # set up handler to look after randomisation of conditions etc
                    IIC = data.TrialHandler(nReps=orders[5][main_trials.thisN], method='sequential', 
                        extraInfo=expInfo, originPath=-1,
                        trialList=data.importConditions("imgCong_"+expInfo['group']+".xlsx", selection=str(SelectedRows_order[iicReps])),
                        seed=None, name='IIC')
                    thisExp.addLoop(IIC)  # add the loop to the experiment
                    thisIIC = IIC.trialList[0]  # so we can initialise stimuli with some values
                    # abbreviate parameter names if possible (e.g. rgb = thisIIC.rgb)
                    if thisIIC != None:
                        for paramName in thisIIC:
                            globals()[paramName] = thisIIC[paramName]
                    
                    for thisIIC in IIC:
                        currentLoop = IIC
                        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                        # pause experiment here if requested
                        if thisExp.status == PAUSED:
                            pauseExperiment(
                                thisExp=thisExp, 
                                win=win, 
                                timers=[routineTimer], 
                                playbackComponents=[]
                        )
                        # abbreviate parameter names if possible (e.g. rgb = thisIIC.rgb)
                        if thisIIC != None:
                            for paramName in thisIIC:
                                globals()[paramName] = thisIIC[paramName]
                        
                        # --- Prepare to start Routine "Img_Incorr_Cong" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('Img_Incorr_Cong.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from iic6
                        if iicReps == allRepsCount-1:
                            IIC_termloopReps = 0
                            continueRoutine = False
                        iic2.setImage(img)
                        iic4.setText(incorr)
                        iic5.keys = []
                        iic5.rt = []
                        _iic5_allKeys = []
                        # keep track of which components have finished
                        Img_Incorr_CongComponents = [iic1, iic2, iic3, iic4, iic5]
                        for thisComponent in Img_Incorr_CongComponents:
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
                        
                        # --- Run Routine "Img_Incorr_Cong" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine and routineTimer.getTime() < 5.4:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # *iic1* updates
                            
                            # if iic1 is starting this frame...
                            if iic1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                                # keep track of start time/frame for later
                                iic1.frameNStart = frameN  # exact frame index
                                iic1.tStart = t  # local t and not account for scr refresh
                                iic1.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(iic1, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                iic1.status = STARTED
                                iic1.setAutoDraw(True)
                            
                            # if iic1 is active this frame...
                            if iic1.status == STARTED:
                                # update params
                                pass
                            
                            # if iic1 is stopping this frame...
                            if iic1.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > iic1.tStartRefresh + .8-frameTolerance:
                                    # keep track of stop time/frame for later
                                    iic1.tStop = t  # not accounting for scr refresh
                                    iic1.tStopRefresh = tThisFlipGlobal  # on global time
                                    iic1.frameNStop = frameN  # exact frame index
                                    # update status
                                    iic1.status = FINISHED
                                    iic1.setAutoDraw(False)
                            
                            # *iic2* updates
                            
                            # if iic2 is starting this frame...
                            if iic2.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                                # keep track of start time/frame for later
                                iic2.frameNStart = frameN  # exact frame index
                                iic2.tStart = t  # local t and not account for scr refresh
                                iic2.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(iic2, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                iic2.status = STARTED
                                iic2.setAutoDraw(True)
                            
                            # if iic2 is active this frame...
                            if iic2.status == STARTED:
                                # update params
                                pass
                            
                            # if iic2 is stopping this frame...
                            if iic2.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > iic2.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    iic2.tStop = t  # not accounting for scr refresh
                                    iic2.tStopRefresh = tThisFlipGlobal  # on global time
                                    iic2.frameNStop = frameN  # exact frame index
                                    # update status
                                    iic2.status = FINISHED
                                    iic2.setAutoDraw(False)
                            
                            # *iic3* updates
                            
                            # if iic3 is starting this frame...
                            if iic3.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                                # keep track of start time/frame for later
                                iic3.frameNStart = frameN  # exact frame index
                                iic3.tStart = t  # local t and not account for scr refresh
                                iic3.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(iic3, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                iic3.status = STARTED
                                iic3.setAutoDraw(True)
                            
                            # if iic3 is active this frame...
                            if iic3.status == STARTED:
                                # update params
                                pass
                            
                            # if iic3 is stopping this frame...
                            if iic3.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > iic3.tStartRefresh + .5-frameTolerance:
                                    # keep track of stop time/frame for later
                                    iic3.tStop = t  # not accounting for scr refresh
                                    iic3.tStopRefresh = tThisFlipGlobal  # on global time
                                    iic3.frameNStop = frameN  # exact frame index
                                    # update status
                                    iic3.status = FINISHED
                                    iic3.setAutoDraw(False)
                            
                            # *iic4* updates
                            
                            # if iic4 is starting this frame...
                            if iic4.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                iic4.frameNStart = frameN  # exact frame index
                                iic4.tStart = t  # local t and not account for scr refresh
                                iic4.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(iic4, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                iic4.status = STARTED
                                iic4.setAutoDraw(True)
                            
                            # if iic4 is active this frame...
                            if iic4.status == STARTED:
                                # update params
                                pass
                            
                            # if iic4 is stopping this frame...
                            if iic4.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > iic4.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    iic4.tStop = t  # not accounting for scr refresh
                                    iic4.tStopRefresh = tThisFlipGlobal  # on global time
                                    iic4.frameNStop = frameN  # exact frame index
                                    # update status
                                    iic4.status = FINISHED
                                    iic4.setAutoDraw(False)
                            
                            # *iic5* updates
                            waitOnFlip = False
                            
                            # if iic5 is starting this frame...
                            if iic5.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                iic5.frameNStart = frameN  # exact frame index
                                iic5.tStart = t  # local t and not account for scr refresh
                                iic5.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(iic5, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                iic5.status = STARTED
                                # keyboard checking is just starting
                                waitOnFlip = True
                                win.callOnFlip(iic5.clock.reset)  # t=0 on next screen flip
                                win.callOnFlip(iic5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                            
                            # if iic5 is stopping this frame...
                            if iic5.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > iic5.tStartRefresh + 2-frameTolerance:
                                    # keep track of stop time/frame for later
                                    iic5.tStop = t  # not accounting for scr refresh
                                    iic5.tStopRefresh = tThisFlipGlobal  # on global time
                                    iic5.frameNStop = frameN  # exact frame index
                                    # update status
                                    iic5.status = FINISHED
                                    iic5.status = FINISHED
                            if iic5.status == STARTED and not waitOnFlip:
                                theseKeys = iic5.getKeys(keyList=['z','m'], ignoreKeys=["escape"], waitRelease=False)
                                _iic5_allKeys.extend(theseKeys)
                                if len(_iic5_allKeys):
                                    iic5.keys = _iic5_allKeys[-1].name  # just the last key pressed
                                    iic5.rt = _iic5_allKeys[-1].rt
                                    iic5.duration = _iic5_allKeys[-1].duration
                                    # a response ends the routine
                                    continueRoutine = False
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in Img_Incorr_CongComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "Img_Incorr_Cong" ---
                        for thisComponent in Img_Incorr_CongComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('Img_Incorr_Cong.stopped', globalClock.getTime(format='float'))
                        # Run 'End Routine' code from iic6
                        totalCount = totalCount+1
                        iicCount = iicCount+1
                        iicReps = iicReps+1
                        
                        thisExp.addData("condition", "IIC")
                        thisExp.addData("trigger", 32)
                        if iic5.keys == corrAns2:
                            thisExp.addData("response","correct")
                        elif iic5.keys == corrAns1:
                            thisExp.addData("response","incorrect")
                        else:
                            thisExp.addData("response","missed")
                        # check responses
                        if iic5.keys in ['', [], None]:  # No response was made
                            iic5.keys = None
                        IIC.addData('iic5.keys',iic5.keys)
                        if iic5.keys != None:  # we had a response
                            IIC.addData('iic5.rt', iic5.rt)
                            IIC.addData('iic5.duration', iic5.duration)
                        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                        if routineForceEnded:
                            routineTimer.reset()
                        else:
                            routineTimer.addTime(-5.400000)
                        
                        # --- Prepare to start Routine "iic_code" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('iic_code.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from iccCode_2
                        if iicCount == 1:
                            iicCount = 0
                        # keep track of which components have finished
                        iic_codeComponents = []
                        for thisComponent in iic_codeComponents:
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
                        
                        # --- Run Routine "iic_code" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in iic_codeComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "iic_code" ---
                        for thisComponent in iic_codeComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('iic_code.stopped', globalClock.getTime(format='float'))
                        # the Routine "iic_code" was not non-slip safe, so reset the non-slip timer
                        routineTimer.reset()
                        thisExp.nextEntry()
                        
                        if thisSession is not None:
                            # if running in a Session with a Liaison client, send data up to now
                            thisSession.sendExperimentData()
                    # completed orders[5][main_trials.thisN] repeats of 'IIC'
                    
                # completed IIC_termloopReps repeats of 'IIC_termloop'
                
                
                # set up handler to look after randomisation of conditions etc
                ICI_termloop = data.TrialHandler(nReps=ICI_termloopReps, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='ICI_termloop')
                thisExp.addLoop(ICI_termloop)  # add the loop to the experiment
                thisICI_termloop = ICI_termloop.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisICI_termloop.rgb)
                if thisICI_termloop != None:
                    for paramName in thisICI_termloop:
                        globals()[paramName] = thisICI_termloop[paramName]
                
                for thisICI_termloop in ICI_termloop:
                    currentLoop = ICI_termloop
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisICI_termloop.rgb)
                    if thisICI_termloop != None:
                        for paramName in thisICI_termloop:
                            globals()[paramName] = thisICI_termloop[paramName]
                    
                    # set up handler to look after randomisation of conditions etc
                    ICI = data.TrialHandler(nReps=orders[6][main_trials.thisN], method='sequential', 
                        extraInfo=expInfo, originPath=-1,
                        trialList=data.importConditions("imgIncong_"+expInfo['group']+".xlsx", selection=str(SelectedRows_order[iciReps])),
                        seed=None, name='ICI')
                    thisExp.addLoop(ICI)  # add the loop to the experiment
                    thisICI = ICI.trialList[0]  # so we can initialise stimuli with some values
                    # abbreviate parameter names if possible (e.g. rgb = thisICI.rgb)
                    if thisICI != None:
                        for paramName in thisICI:
                            globals()[paramName] = thisICI[paramName]
                    
                    for thisICI in ICI:
                        currentLoop = ICI
                        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                        # pause experiment here if requested
                        if thisExp.status == PAUSED:
                            pauseExperiment(
                                thisExp=thisExp, 
                                win=win, 
                                timers=[routineTimer], 
                                playbackComponents=[]
                        )
                        # abbreviate parameter names if possible (e.g. rgb = thisICI.rgb)
                        if thisICI != None:
                            for paramName in thisICI:
                                globals()[paramName] = thisICI[paramName]
                        
                        # --- Prepare to start Routine "Img_Corr_Incong" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('Img_Corr_Incong.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from ici6
                        if iciReps == allRepsCount-1:
                            ICI_termloopReps = 0
                            contiueRoutine = False
                        ici2.setImage(img)
                        ici4.setText(conWord)
                        ici5.keys = []
                        ici5.rt = []
                        _ici5_allKeys = []
                        # keep track of which components have finished
                        Img_Corr_IncongComponents = [ici1, ici2, ici3, ici4, ici5]
                        for thisComponent in Img_Corr_IncongComponents:
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
                        
                        # --- Run Routine "Img_Corr_Incong" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine and routineTimer.getTime() < 5.4:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # *ici1* updates
                            
                            # if ici1 is starting this frame...
                            if ici1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                                # keep track of start time/frame for later
                                ici1.frameNStart = frameN  # exact frame index
                                ici1.tStart = t  # local t and not account for scr refresh
                                ici1.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(ici1, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                ici1.status = STARTED
                                ici1.setAutoDraw(True)
                            
                            # if ici1 is active this frame...
                            if ici1.status == STARTED:
                                # update params
                                pass
                            
                            # if ici1 is stopping this frame...
                            if ici1.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > ici1.tStartRefresh + .8-frameTolerance:
                                    # keep track of stop time/frame for later
                                    ici1.tStop = t  # not accounting for scr refresh
                                    ici1.tStopRefresh = tThisFlipGlobal  # on global time
                                    ici1.frameNStop = frameN  # exact frame index
                                    # update status
                                    ici1.status = FINISHED
                                    ici1.setAutoDraw(False)
                            
                            # *ici2* updates
                            
                            # if ici2 is starting this frame...
                            if ici2.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                                # keep track of start time/frame for later
                                ici2.frameNStart = frameN  # exact frame index
                                ici2.tStart = t  # local t and not account for scr refresh
                                ici2.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(ici2, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                ici2.status = STARTED
                                ici2.setAutoDraw(True)
                            
                            # if ici2 is active this frame...
                            if ici2.status == STARTED:
                                # update params
                                pass
                            
                            # if ici2 is stopping this frame...
                            if ici2.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > ici2.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    ici2.tStop = t  # not accounting for scr refresh
                                    ici2.tStopRefresh = tThisFlipGlobal  # on global time
                                    ici2.frameNStop = frameN  # exact frame index
                                    # update status
                                    ici2.status = FINISHED
                                    ici2.setAutoDraw(False)
                            
                            # *ici3* updates
                            
                            # if ici3 is starting this frame...
                            if ici3.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                                # keep track of start time/frame for later
                                ici3.frameNStart = frameN  # exact frame index
                                ici3.tStart = t  # local t and not account for scr refresh
                                ici3.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(ici3, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                ici3.status = STARTED
                                ici3.setAutoDraw(True)
                            
                            # if ici3 is active this frame...
                            if ici3.status == STARTED:
                                # update params
                                pass
                            
                            # if ici3 is stopping this frame...
                            if ici3.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > ici3.tStartRefresh + .5-frameTolerance:
                                    # keep track of stop time/frame for later
                                    ici3.tStop = t  # not accounting for scr refresh
                                    ici3.tStopRefresh = tThisFlipGlobal  # on global time
                                    ici3.frameNStop = frameN  # exact frame index
                                    # update status
                                    ici3.status = FINISHED
                                    ici3.setAutoDraw(False)
                            
                            # *ici4* updates
                            
                            # if ici4 is starting this frame...
                            if ici4.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                ici4.frameNStart = frameN  # exact frame index
                                ici4.tStart = t  # local t and not account for scr refresh
                                ici4.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(ici4, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                ici4.status = STARTED
                                ici4.setAutoDraw(True)
                            
                            # if ici4 is active this frame...
                            if ici4.status == STARTED:
                                # update params
                                pass
                            
                            # if ici4 is stopping this frame...
                            if ici4.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > ici4.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    ici4.tStop = t  # not accounting for scr refresh
                                    ici4.tStopRefresh = tThisFlipGlobal  # on global time
                                    ici4.frameNStop = frameN  # exact frame index
                                    # update status
                                    ici4.status = FINISHED
                                    ici4.setAutoDraw(False)
                            
                            # *ici5* updates
                            waitOnFlip = False
                            
                            # if ici5 is starting this frame...
                            if ici5.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                ici5.frameNStart = frameN  # exact frame index
                                ici5.tStart = t  # local t and not account for scr refresh
                                ici5.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(ici5, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                ici5.status = STARTED
                                # keyboard checking is just starting
                                waitOnFlip = True
                                win.callOnFlip(ici5.clock.reset)  # t=0 on next screen flip
                                win.callOnFlip(ici5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                            
                            # if ici5 is stopping this frame...
                            if ici5.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > ici5.tStartRefresh + 2-frameTolerance:
                                    # keep track of stop time/frame for later
                                    ici5.tStop = t  # not accounting for scr refresh
                                    ici5.tStopRefresh = tThisFlipGlobal  # on global time
                                    ici5.frameNStop = frameN  # exact frame index
                                    # update status
                                    ici5.status = FINISHED
                                    ici5.status = FINISHED
                            if ici5.status == STARTED and not waitOnFlip:
                                theseKeys = ici5.getKeys(keyList=['z','m'], ignoreKeys=["escape"], waitRelease=False)
                                _ici5_allKeys.extend(theseKeys)
                                if len(_ici5_allKeys):
                                    ici5.keys = _ici5_allKeys[-1].name  # just the last key pressed
                                    ici5.rt = _ici5_allKeys[-1].rt
                                    ici5.duration = _ici5_allKeys[-1].duration
                                    # a response ends the routine
                                    continueRoutine = False
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in Img_Corr_IncongComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "Img_Corr_Incong" ---
                        for thisComponent in Img_Corr_IncongComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('Img_Corr_Incong.stopped', globalClock.getTime(format='float'))
                        # Run 'End Routine' code from ici6
                        totalCount = totalCount+1
                        iciCount = iciCount+1
                        iciReps = iciReps+1
                        
                        thisExp.addData("condition", "ICI")
                        thisExp.addData("trigger", 33)
                        if ici5.keys == corrAns1:
                            thisExp.addData("response","correct")
                        elif ici5.keys == corrAns2:
                            thisExp.addData("response","incorrect")
                        else:
                            thisExp.addData("response","missed")
                        # check responses
                        if ici5.keys in ['', [], None]:  # No response was made
                            ici5.keys = None
                        ICI.addData('ici5.keys',ici5.keys)
                        if ici5.keys != None:  # we had a response
                            ICI.addData('ici5.rt', ici5.rt)
                            ICI.addData('ici5.duration', ici5.duration)
                        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                        if routineForceEnded:
                            routineTimer.reset()
                        else:
                            routineTimer.addTime(-5.400000)
                        
                        # --- Prepare to start Routine "ici_code" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('ici_code.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from iccCode_3
                        if iciCount == 1:
                            iciCount = 0
                        # keep track of which components have finished
                        ici_codeComponents = []
                        for thisComponent in ici_codeComponents:
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
                        
                        # --- Run Routine "ici_code" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in ici_codeComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "ici_code" ---
                        for thisComponent in ici_codeComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('ici_code.stopped', globalClock.getTime(format='float'))
                        # the Routine "ici_code" was not non-slip safe, so reset the non-slip timer
                        routineTimer.reset()
                        thisExp.nextEntry()
                        
                        if thisSession is not None:
                            # if running in a Session with a Liaison client, send data up to now
                            thisSession.sendExperimentData()
                    # completed orders[6][main_trials.thisN] repeats of 'ICI'
                    
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed ICI_termloopReps repeats of 'ICI_termloop'
                
                
                # set up handler to look after randomisation of conditions etc
                III_termloop = data.TrialHandler(nReps=III_termloopReps, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='III_termloop')
                thisExp.addLoop(III_termloop)  # add the loop to the experiment
                thisIII_termloop = III_termloop.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisIII_termloop.rgb)
                if thisIII_termloop != None:
                    for paramName in thisIII_termloop:
                        globals()[paramName] = thisIII_termloop[paramName]
                
                for thisIII_termloop in III_termloop:
                    currentLoop = III_termloop
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisIII_termloop.rgb)
                    if thisIII_termloop != None:
                        for paramName in thisIII_termloop:
                            globals()[paramName] = thisIII_termloop[paramName]
                    
                    # set up handler to look after randomisation of conditions etc
                    III = data.TrialHandler(nReps=orders[7][main_trials.thisN], method='sequential', 
                        extraInfo=expInfo, originPath=-1,
                        trialList=data.importConditions("imgIncong_"+expInfo['group']+".xlsx", selection=str(SelectedRows_order[iiiReps])),
                        seed=None, name='III')
                    thisExp.addLoop(III)  # add the loop to the experiment
                    thisIII = III.trialList[0]  # so we can initialise stimuli with some values
                    # abbreviate parameter names if possible (e.g. rgb = thisIII.rgb)
                    if thisIII != None:
                        for paramName in thisIII:
                            globals()[paramName] = thisIII[paramName]
                    
                    for thisIII in III:
                        currentLoop = III
                        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                        # pause experiment here if requested
                        if thisExp.status == PAUSED:
                            pauseExperiment(
                                thisExp=thisExp, 
                                win=win, 
                                timers=[routineTimer], 
                                playbackComponents=[]
                        )
                        # abbreviate parameter names if possible (e.g. rgb = thisIII.rgb)
                        if thisIII != None:
                            for paramName in thisIII:
                                globals()[paramName] = thisIII[paramName]
                        
                        # --- Prepare to start Routine "Img_Incorr_Incong" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('Img_Incorr_Incong.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from iii6
                        if iiiReps ==allRepsCount-1:
                            III_termloopReps = 0
                            continueRoutine = False
                        iii2.setImage(img)
                        iii4.setText(incorr)
                        iii5.keys = []
                        iii5.rt = []
                        _iii5_allKeys = []
                        # keep track of which components have finished
                        Img_Incorr_IncongComponents = [iii1, iii2, iii3, iii4, iii5]
                        for thisComponent in Img_Incorr_IncongComponents:
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
                        
                        # --- Run Routine "Img_Incorr_Incong" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine and routineTimer.getTime() < 5.4:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # *iii1* updates
                            
                            # if iii1 is starting this frame...
                            if iii1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                                # keep track of start time/frame for later
                                iii1.frameNStart = frameN  # exact frame index
                                iii1.tStart = t  # local t and not account for scr refresh
                                iii1.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(iii1, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                iii1.status = STARTED
                                iii1.setAutoDraw(True)
                            
                            # if iii1 is active this frame...
                            if iii1.status == STARTED:
                                # update params
                                pass
                            
                            # if iii1 is stopping this frame...
                            if iii1.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > iii1.tStartRefresh + .8-frameTolerance:
                                    # keep track of stop time/frame for later
                                    iii1.tStop = t  # not accounting for scr refresh
                                    iii1.tStopRefresh = tThisFlipGlobal  # on global time
                                    iii1.frameNStop = frameN  # exact frame index
                                    # update status
                                    iii1.status = FINISHED
                                    iii1.setAutoDraw(False)
                            
                            # *iii2* updates
                            
                            # if iii2 is starting this frame...
                            if iii2.status == NOT_STARTED and tThisFlip >= 2.4-frameTolerance:
                                # keep track of start time/frame for later
                                iii2.frameNStart = frameN  # exact frame index
                                iii2.tStart = t  # local t and not account for scr refresh
                                iii2.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(iii2, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                iii2.status = STARTED
                                iii2.setAutoDraw(True)
                            
                            # if iii2 is active this frame...
                            if iii2.status == STARTED:
                                # update params
                                pass
                            
                            # if iii2 is stopping this frame...
                            if iii2.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > iii2.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    iii2.tStop = t  # not accounting for scr refresh
                                    iii2.tStopRefresh = tThisFlipGlobal  # on global time
                                    iii2.frameNStop = frameN  # exact frame index
                                    # update status
                                    iii2.status = FINISHED
                                    iii2.setAutoDraw(False)
                            
                            # *iii3* updates
                            
                            # if iii3 is starting this frame...
                            if iii3.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
                                # keep track of start time/frame for later
                                iii3.frameNStart = frameN  # exact frame index
                                iii3.tStart = t  # local t and not account for scr refresh
                                iii3.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(iii3, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                iii3.status = STARTED
                                iii3.setAutoDraw(True)
                            
                            # if iii3 is active this frame...
                            if iii3.status == STARTED:
                                # update params
                                pass
                            
                            # if iii3 is stopping this frame...
                            if iii3.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > iii3.tStartRefresh + .5-frameTolerance:
                                    # keep track of stop time/frame for later
                                    iii3.tStop = t  # not accounting for scr refresh
                                    iii3.tStopRefresh = tThisFlipGlobal  # on global time
                                    iii3.frameNStop = frameN  # exact frame index
                                    # update status
                                    iii3.status = FINISHED
                                    iii3.setAutoDraw(False)
                            
                            # *iii4* updates
                            
                            # if iii4 is starting this frame...
                            if iii4.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                iii4.frameNStart = frameN  # exact frame index
                                iii4.tStart = t  # local t and not account for scr refresh
                                iii4.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(iii4, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                iii4.status = STARTED
                                iii4.setAutoDraw(True)
                            
                            # if iii4 is active this frame...
                            if iii4.status == STARTED:
                                # update params
                                pass
                            
                            # if iii4 is stopping this frame...
                            if iii4.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > iii4.tStartRefresh + .3-frameTolerance:
                                    # keep track of stop time/frame for later
                                    iii4.tStop = t  # not accounting for scr refresh
                                    iii4.tStopRefresh = tThisFlipGlobal  # on global time
                                    iii4.frameNStop = frameN  # exact frame index
                                    # update status
                                    iii4.status = FINISHED
                                    iii4.setAutoDraw(False)
                            
                            # *iii5* updates
                            waitOnFlip = False
                            
                            # if iii5 is starting this frame...
                            if iii5.status == NOT_STARTED and tThisFlip >= 3.4-frameTolerance:
                                # keep track of start time/frame for later
                                iii5.frameNStart = frameN  # exact frame index
                                iii5.tStart = t  # local t and not account for scr refresh
                                iii5.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(iii5, 'tStartRefresh')  # time at next scr refresh
                                # update status
                                iii5.status = STARTED
                                # keyboard checking is just starting
                                waitOnFlip = True
                                win.callOnFlip(iii5.clock.reset)  # t=0 on next screen flip
                                win.callOnFlip(iii5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                            
                            # if iii5 is stopping this frame...
                            if iii5.status == STARTED:
                                # is it time to stop? (based on global clock, using actual start)
                                if tThisFlipGlobal > iii5.tStartRefresh + 2-frameTolerance:
                                    # keep track of stop time/frame for later
                                    iii5.tStop = t  # not accounting for scr refresh
                                    iii5.tStopRefresh = tThisFlipGlobal  # on global time
                                    iii5.frameNStop = frameN  # exact frame index
                                    # update status
                                    iii5.status = FINISHED
                                    iii5.status = FINISHED
                            if iii5.status == STARTED and not waitOnFlip:
                                theseKeys = iii5.getKeys(keyList=['z','m'], ignoreKeys=["escape"], waitRelease=False)
                                _iii5_allKeys.extend(theseKeys)
                                if len(_iii5_allKeys):
                                    iii5.keys = _iii5_allKeys[-1].name  # just the last key pressed
                                    iii5.rt = _iii5_allKeys[-1].rt
                                    iii5.duration = _iii5_allKeys[-1].duration
                                    # a response ends the routine
                                    continueRoutine = False
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in Img_Incorr_IncongComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "Img_Incorr_Incong" ---
                        for thisComponent in Img_Incorr_IncongComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('Img_Incorr_Incong.stopped', globalClock.getTime(format='float'))
                        # Run 'End Routine' code from iii6
                        totalCount = totalCount+1
                        iiiCount = iiiCount+1
                        iiiReps = iiiReps+1
                        
                        thisExp.addData("condition", "III")
                        thisExp.addData("trigger", 34)
                        if iii5.keys == corrAns2:
                            thisExp.addData("response","correct")
                        elif iii5.keys == corrAns1:
                            thisExp.addData("response","incorrect")
                        else:
                            thisExp.addData("response","missed")
                        # check responses
                        if iii5.keys in ['', [], None]:  # No response was made
                            iii5.keys = None
                        III.addData('iii5.keys',iii5.keys)
                        if iii5.keys != None:  # we had a response
                            III.addData('iii5.rt', iii5.rt)
                            III.addData('iii5.duration', iii5.duration)
                        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                        if routineForceEnded:
                            routineTimer.reset()
                        else:
                            routineTimer.addTime(-5.400000)
                        
                        # --- Prepare to start Routine "iii_code" ---
                        continueRoutine = True
                        # update component parameters for each repeat
                        thisExp.addData('iii_code.started', globalClock.getTime(format='float'))
                        # Run 'Begin Routine' code from iccCode_4
                        if iiiCount == 1:
                            iiiCount = 0
                        # keep track of which components have finished
                        iii_codeComponents = []
                        for thisComponent in iii_codeComponents:
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
                        
                        # --- Run Routine "iii_code" ---
                        routineForceEnded = not continueRoutine
                        while continueRoutine:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # check for quit (typically the Esc key)
                            if defaultKeyboard.getKeys(keyList=["escape"]):
                                thisExp.status = FINISHED
                            if thisExp.status == FINISHED or endExpNow:
                                endExperiment(thisExp, win=win)
                                return
                            
                            # check if all components have finished
                            if not continueRoutine:  # a component has requested a forced-end of Routine
                                routineForceEnded = True
                                break
                            continueRoutine = False  # will revert to True if at least one component still running
                            for thisComponent in iii_codeComponents:
                                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                    continueRoutine = True
                                    break  # at least one component has not yet finished
                            
                            # refresh the screen
                            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                                win.flip()
                        
                        # --- Ending Routine "iii_code" ---
                        for thisComponent in iii_codeComponents:
                            if hasattr(thisComponent, "setAutoDraw"):
                                thisComponent.setAutoDraw(False)
                        thisExp.addData('iii_code.stopped', globalClock.getTime(format='float'))
                        # the Routine "iii_code" was not non-slip safe, so reset the non-slip timer
                        routineTimer.reset()
                        thisExp.nextEntry()
                        
                        if thisSession is not None:
                            # if running in a Session with a Liaison client, send data up to now
                            thisSession.sendExperimentData()
                    # completed orders[7][main_trials.thisN] repeats of 'III'
                    
                # completed III_termloopReps repeats of 'III_termloop'
                
                
                # --- Prepare to start Routine "exitmain" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('exitmain.started', globalClock.getTime(format='float'))
                # keep track of which components have finished
                exitmainComponents = []
                for thisComponent in exitmainComponents:
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
                
                # --- Run Routine "exitmain" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in exitmainComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "exitmain" ---
                for thisComponent in exitmainComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('exitmain.stopped', globalClock.getTime(format='float'))
                # Run 'End Routine' code from code_10
                print("exitmain triggered")
                print('occReps ' + str(occReps))
                print('oicReps ' + str(oicReps))
                print('ociReps ' + str(ociReps))
                print('oiiReps ' + str(oiiReps))
                print('iccReps ' + str(iccReps))
                print('iicReps ' + str(iicReps))
                print('iciReps ' + str(iciReps))
                print('iiiReps ' + str(iiiReps))
                
                if totalCount in [120,240,360]:
                    nRepsBreak = 1
                else:
                    nRepsBreak = 0
                # the Routine "exitmain" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                break_loop = data.TrialHandler(nReps=nRepsBreak, method='sequential', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='break_loop')
                thisExp.addLoop(break_loop)  # add the loop to the experiment
                thisBreak_loop = break_loop.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisBreak_loop.rgb)
                if thisBreak_loop != None:
                    for paramName in thisBreak_loop:
                        globals()[paramName] = thisBreak_loop[paramName]
                
                for thisBreak_loop in break_loop:
                    currentLoop = break_loop
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisBreak_loop.rgb)
                    if thisBreak_loop != None:
                        for paramName in thisBreak_loop:
                            globals()[paramName] = thisBreak_loop[paramName]
                    
                    # --- Prepare to start Routine "screenbreak" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('screenbreak.started', globalClock.getTime(format='float'))
                    key_resp_2.keys = []
                    key_resp_2.rt = []
                    _key_resp_2_allKeys = []
                    # keep track of which components have finished
                    screenbreakComponents = [text_2, key_resp_2]
                    for thisComponent in screenbreakComponents:
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
                    
                    # --- Run Routine "screenbreak" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *text_2* updates
                        
                        # if text_2 is starting this frame...
                        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            text_2.frameNStart = frameN  # exact frame index
                            text_2.tStart = t  # local t and not account for scr refresh
                            text_2.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            text_2.status = STARTED
                            text_2.setAutoDraw(True)
                        
                        # if text_2 is active this frame...
                        if text_2.status == STARTED:
                            # update params
                            pass
                        
                        # *key_resp_2* updates
                        waitOnFlip = False
                        
                        # if key_resp_2 is starting this frame...
                        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            key_resp_2.frameNStart = frameN  # exact frame index
                            key_resp_2.tStart = t  # local t and not account for scr refresh
                            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            key_resp_2.status = STARTED
                            # keyboard checking is just starting
                            waitOnFlip = True
                            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                        if key_resp_2.status == STARTED and not waitOnFlip:
                            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                            _key_resp_2_allKeys.extend(theseKeys)
                            if len(_key_resp_2_allKeys):
                                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                                # a response ends the routine
                                continueRoutine = False
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in screenbreakComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "screenbreak" ---
                    for thisComponent in screenbreakComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('screenbreak.stopped', globalClock.getTime(format='float'))
                    # the Routine "screenbreak" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                # completed nRepsBreak repeats of 'break_loop'
                
            # completed 8.0 repeats of 'main_trials'
            
        # completed allRepsCount repeats of 'totalcount'
        
        
        # --- Prepare to start Routine "reset_for_new" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('reset_for_new.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_11
        print('reset code run')
        print(SelectedRows_order)
        SelectedRows_order = random.sample(range(allRepsCount),allRepsCount)
        print(SelectedRows_order)
        OCC_termloopReps = OIC_termloopReps = OCI_termloopReps = OII_termloopReps = ICC_termloopReps = IIC_termloopReps = ICI_termloopReps = III_termloopReps = 1
        
        occReps = oicReps = ociReps = oiiReps = iccReps = iicReps = iciReps = iiiReps = 0
        
        print('occReps ' + str(occReps))
        print('oicReps ' + str(oicReps))
        print('ociReps ' + str(ociReps))
        print('oiiReps ' + str(oiiReps))
        print('iccReps ' + str(iccReps))
        print('iicReps ' + str(iicReps))
        print('iciReps ' + str(iciReps))
        print('iiiReps ' + str(iiiReps))
        # keep track of which components have finished
        reset_for_newComponents = []
        for thisComponent in reset_for_newComponents:
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
        
        # --- Run Routine "reset_for_new" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reset_for_newComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reset_for_new" ---
        for thisComponent in reset_for_newComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('reset_for_new.stopped', globalClock.getTime(format='float'))
        # the Routine "reset_for_new" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 3.0 repeats of 'rep3_loop'
    
    
    # --- Prepare to start Routine "Done" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Done.started', globalClock.getTime(format='float'))
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    DoneComponents = [text, key_resp]
    for thisComponent in DoneComponents:
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
    
    # --- Run Routine "Done" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DoneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Done" ---
    for thisComponent in DoneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Done.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "Done" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
