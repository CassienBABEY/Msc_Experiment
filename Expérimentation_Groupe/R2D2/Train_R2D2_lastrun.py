#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on mars 06, 2023, at 19:28
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
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
psychopyVersion = '2022.2.5'
expName = 'Train_deepblue'  # from the Builder filename that created this script
expInfo = {
    'participant': '0',
    'session': '001',
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
    originPath='C:\\Users\\cassi\\OneDrive\\Bureau\\Dossier_exp\\Expérimentation_Groupe\\R2D2\\Train_R2D2_lastrun.py',
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
    size=[1024, 980], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
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

# --- Initialize components for Routine "Start" ---
Welcome_text = visual.TextStim(win=win, name='Welcome_text',
    text='Bonjour\n\net \n\nMerci pour votre participation !',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Instructions" ---
Instructions_1 = visual.TextStim(win=win, name='Instructions_1',
    text="INSTRUCTIONS\n\n\nVous allez lire 6 anecdotes sur cet ordinateur.\nLa tâche consiste à lire et/ou réécrire des anecdotes qui seront affichées sur l'écran.\nVous avez un temps limité pour lire/écrire l'anecdote affichée.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Instructions_2 = visual.TextStim(win=win, name='Instructions_2',
    text="Vous verrez le message suivant après chaque validation d'une anecdote :\n'L'anecdote a été sauvegardée dans le fichier FAITS' (ou DONNEES, INFOS, NOMS, ITEMS, POINTS) par : ['NOMPERSONNAGE']\n\nVous allez tout d'abord réaliser une phase d'entrainement pour vous familiariser avec la tâche.\n\nAppelez l'expérimentateur quand vous êtes prêt.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
blank1 = visual.TextStim(win=win, name='blank1',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Pikachu" ---
anecdotes_2 = visual.TextStim(win=win, name='anecdotes_2',
    text='Une voiture a 4 roues',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
blank_2 = visual.TextStim(win=win, name='blank_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
feedback_phrase_2 = visual.TextStim(win=win, name='feedback_phrase_2',
    text="L'anecdote a été sauvegardée dans le fichier POINTS",
    font='Open Sans',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
feedback_fichier_train_2 = visual.TextStim(win=win, name='feedback_fichier_train_2',
    text='par Pikachu',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "E_T" ---
anecdotes_1 = visual.TextStim(win=win, name='anecdotes_1',
    text="Le kangourou est l'animal emblématique de l'Australie",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
feedback_phrase = visual.TextStim(win=win, name='feedback_phrase',
    text="L'anecdote a été sauvegardée dans le fichier DONNEES",
    font='Open Sans',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
feedback_fichier_train_1 = visual.TextStim(win=win, name='feedback_fichier_train_1',
    text='par E.T',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "DeepBlue" ---
anecdotes_3 = visual.TextStim(win=win, name='anecdotes_3',
    text='Le Coca Cola était à la base un médicament',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
blank_3 = visual.TextStim(win=win, name='blank_3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
feedback_phrase_3 = visual.TextStim(win=win, name='feedback_phrase_3',
    text="L'anecdote a été sauvegardée dans le fichier FAITS",
    font='Open Sans',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
feedback_fichier_train_3 = visual.TextStim(win=win, name='feedback_fichier_train_3',
    text='par DeepBlue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "Sam" ---
anecdotes_4 = visual.TextStim(win=win, name='anecdotes_4',
    text="L'escargot est un animal hermaphrodite",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
blank_4 = visual.TextStim(win=win, name='blank_4',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
feedback_phrase_4 = visual.TextStim(win=win, name='feedback_phrase_4',
    text="L'anecdote a été sauvegardée dans le fichier INFOS",
    font='Open Sans',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
feedback_fichier_train_4 = visual.TextStim(win=win, name='feedback_fichier_train_4',
    text='par Sam',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "Amazon_" ---
anecdotes_5 = visual.TextStim(win=win, name='anecdotes_5',
    text='Mâcher un chewing-gum en épluchant un oignon éviterait de nous faire pleurer',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
blank_5 = visual.TextStim(win=win, name='blank_5',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
feedback_phrase_5 = visual.TextStim(win=win, name='feedback_phrase_5',
    text="L'anecdote a été sauvegardée dans le fichier ITEMS",
    font='Open Sans',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
feedback_fichier_train_5 = visual.TextStim(win=win, name='feedback_fichier_train_5',
    text='par Amazon',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "R2D2" ---
anecdotes_6 = visual.TextStim(win=win, name='anecdotes_6',
    text='Le diamètre du soleil diminue d’un mètre par heure',
    font='Open Sans',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
train_text = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -.1),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='train_text',
     autoLog=True,
)
blank_6 = visual.TextStim(win=win, name='blank_6',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
feedback_phrase_6 = visual.TextStim(win=win, name='feedback_phrase_6',
    text="L'anecdote a été sauvegardée dans le fichier :",
    font='Open Sans',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
feedback_fichier_train_6 = visual.TextStim(win=win, name='feedback_fichier_train_6',
    text='NOMS',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "blank500" ---
blank1 = visual.TextStim(win=win, name='blank1',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Instructions_reco" ---
Instructions_reco_1 = visual.TextStim(win=win, name='Instructions_reco_1',
    text="Les anecdotes préalablement vues vont être à nouveau affichées à l'écran.\n\nVous allez devoir écrire le nom du fichier dans lequel l'anecdote a été sauvegardée ou le personnage qui l'a sauvegardé.\n\nVous avez accès au dossier sur le bureau de l'ordinateur. Ce dossier contient les fichiers et les noms des personnages vus préalablemment.\n\nPour rappel, les noms des fichiers sont :  DONNEES, INFOS, NOMS, ITEMS, FAITS, POINTS.\n\nAppelez l'expérimentateur pour commencer. ",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_reco_key = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
blank1 = visual.TextStim(win=win, name='blank1',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Reco_task" ---
anecdotes_train_2 = visual.TextStim(win=win, name='anecdotes_train_2',
    text='',
    font='Open Sans',
    pos=(0, .25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
reco_text_train = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -.1),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='reco_text_train',
     autoLog=True,
)
validation_train_reco = visual.TextStim(win=win, name='validation_train_reco',
    text='Valider',
    font='Open Sans',
    pos=(0, -.4), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);
mouse_reco_train = event.Mouse(win=win)
x, y = [None, None]
mouse_reco_train.mouseClock = core.Clock()

# --- Initialize components for Routine "blank400" ---
blank2 = visual.TextStim(win=win, name='blank2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "blank500" ---
blank1 = visual.TextStim(win=win, name='blank1',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "End" ---
text = visual.TextStim(win=win, name='text',
    text="Merci pour votre participation !\n\nVeuillez appelez l'expérimentateur pour commencer la tâche.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Start" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
StartComponents = [Welcome_text]
for thisComponent in StartComponents:
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

# --- Run Routine "Start" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome_text* updates
    if Welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome_text.frameNStart = frameN  # exact frame index
        Welcome_text.tStart = t  # local t and not account for scr refresh
        Welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Welcome_text.started')
        Welcome_text.setAutoDraw(True)
    if Welcome_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Welcome_text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            Welcome_text.tStop = t  # not accounting for scr refresh
            Welcome_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Welcome_text.stopped')
            Welcome_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Start" ---
for thisComponent in StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstructionsComponents = [Instructions_1, Instructions_2, key_resp]
for thisComponent in InstructionsComponents:
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

# --- Run Routine "Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions_1* updates
    if Instructions_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_1.frameNStart = frameN  # exact frame index
        Instructions_1.tStart = t  # local t and not account for scr refresh
        Instructions_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructions_1.started')
        Instructions_1.setAutoDraw(True)
    if Instructions_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Instructions_1.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            Instructions_1.tStop = t  # not accounting for scr refresh
            Instructions_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_1.stopped')
            Instructions_1.setAutoDraw(False)
    
    # *Instructions_2* updates
    if Instructions_2.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
        # keep track of start time/frame for later
        Instructions_2.frameNStart = frameN  # exact frame index
        Instructions_2.tStart = t  # local t and not account for scr refresh
        Instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructions_2.started')
        Instructions_2.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['i'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
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
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "blank500" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blank500Components = [blank1]
for thisComponent in blank500Components:
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

# --- Run Routine "blank500" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blank1* updates
    if blank1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blank1.frameNStart = frameN  # exact frame index
        blank1.tStart = t  # local t and not account for scr refresh
        blank1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'blank1.started')
        blank1.setAutoDraw(True)
    if blank1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            blank1.tStop = t  # not accounting for scr refresh
            blank1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank1.stopped')
            blank1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank500" ---
for thisComponent in blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- Prepare to start Routine "Pikachu" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
PikachuComponents = [anecdotes_2, blank_2, feedback_phrase_2, feedback_fichier_train_2]
for thisComponent in PikachuComponents:
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

# --- Run Routine "Pikachu" ---
while continueRoutine and routineTimer.getTime() < 15.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *anecdotes_2* updates
    if anecdotes_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        anecdotes_2.frameNStart = frameN  # exact frame index
        anecdotes_2.tStart = t  # local t and not account for scr refresh
        anecdotes_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(anecdotes_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'anecdotes_2.started')
        anecdotes_2.setAutoDraw(True)
    if anecdotes_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > anecdotes_2.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            anecdotes_2.tStop = t  # not accounting for scr refresh
            anecdotes_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'anecdotes_2.stopped')
            anecdotes_2.setAutoDraw(False)
    
    # *blank_2* updates
    if blank_2.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
        # keep track of start time/frame for later
        blank_2.frameNStart = frameN  # exact frame index
        blank_2.tStart = t  # local t and not account for scr refresh
        blank_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'blank_2.started')
        blank_2.setAutoDraw(True)
    if blank_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank_2.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            blank_2.tStop = t  # not accounting for scr refresh
            blank_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_2.stopped')
            blank_2.setAutoDraw(False)
    
    # *feedback_phrase_2* updates
    if feedback_phrase_2.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
        # keep track of start time/frame for later
        feedback_phrase_2.frameNStart = frameN  # exact frame index
        feedback_phrase_2.tStart = t  # local t and not account for scr refresh
        feedback_phrase_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_phrase_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_phrase_2.started')
        feedback_phrase_2.setAutoDraw(True)
    if feedback_phrase_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback_phrase_2.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            feedback_phrase_2.tStop = t  # not accounting for scr refresh
            feedback_phrase_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_phrase_2.stopped')
            feedback_phrase_2.setAutoDraw(False)
    
    # *feedback_fichier_train_2* updates
    if feedback_fichier_train_2.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
        # keep track of start time/frame for later
        feedback_fichier_train_2.frameNStart = frameN  # exact frame index
        feedback_fichier_train_2.tStart = t  # local t and not account for scr refresh
        feedback_fichier_train_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_fichier_train_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_fichier_train_2.started')
        feedback_fichier_train_2.setAutoDraw(True)
    if feedback_fichier_train_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback_fichier_train_2.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            feedback_fichier_train_2.tStop = t  # not accounting for scr refresh
            feedback_fichier_train_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_fichier_train_2.stopped')
            feedback_fichier_train_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PikachuComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Pikachu" ---
for thisComponent in PikachuComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-15.500000)

# --- Prepare to start Routine "E_T" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
E_TComponents = [anecdotes_1, blank, feedback_phrase, feedback_fichier_train_1]
for thisComponent in E_TComponents:
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

# --- Run Routine "E_T" ---
while continueRoutine and routineTimer.getTime() < 15.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *anecdotes_1* updates
    if anecdotes_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        anecdotes_1.frameNStart = frameN  # exact frame index
        anecdotes_1.tStart = t  # local t and not account for scr refresh
        anecdotes_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(anecdotes_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'anecdotes_1.started')
        anecdotes_1.setAutoDraw(True)
    if anecdotes_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > anecdotes_1.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            anecdotes_1.tStop = t  # not accounting for scr refresh
            anecdotes_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'anecdotes_1.stopped')
            anecdotes_1.setAutoDraw(False)
    
    # *blank* updates
    if blank.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
        # keep track of start time/frame for later
        blank.frameNStart = frameN  # exact frame index
        blank.tStart = t  # local t and not account for scr refresh
        blank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'blank.started')
        blank.setAutoDraw(True)
    if blank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            blank.tStop = t  # not accounting for scr refresh
            blank.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank.stopped')
            blank.setAutoDraw(False)
    
    # *feedback_phrase* updates
    if feedback_phrase.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
        # keep track of start time/frame for later
        feedback_phrase.frameNStart = frameN  # exact frame index
        feedback_phrase.tStart = t  # local t and not account for scr refresh
        feedback_phrase.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_phrase, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_phrase.started')
        feedback_phrase.setAutoDraw(True)
    if feedback_phrase.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback_phrase.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            feedback_phrase.tStop = t  # not accounting for scr refresh
            feedback_phrase.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_phrase.stopped')
            feedback_phrase.setAutoDraw(False)
    
    # *feedback_fichier_train_1* updates
    if feedback_fichier_train_1.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
        # keep track of start time/frame for later
        feedback_fichier_train_1.frameNStart = frameN  # exact frame index
        feedback_fichier_train_1.tStart = t  # local t and not account for scr refresh
        feedback_fichier_train_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_fichier_train_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_fichier_train_1.started')
        feedback_fichier_train_1.setAutoDraw(True)
    if feedback_fichier_train_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback_fichier_train_1.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            feedback_fichier_train_1.tStop = t  # not accounting for scr refresh
            feedback_fichier_train_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_fichier_train_1.stopped')
            feedback_fichier_train_1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in E_TComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "E_T" ---
for thisComponent in E_TComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-15.500000)

# --- Prepare to start Routine "DeepBlue" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
DeepBlueComponents = [anecdotes_3, blank_3, feedback_phrase_3, feedback_fichier_train_3]
for thisComponent in DeepBlueComponents:
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

# --- Run Routine "DeepBlue" ---
while continueRoutine and routineTimer.getTime() < 15.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *anecdotes_3* updates
    if anecdotes_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        anecdotes_3.frameNStart = frameN  # exact frame index
        anecdotes_3.tStart = t  # local t and not account for scr refresh
        anecdotes_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(anecdotes_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'anecdotes_3.started')
        anecdotes_3.setAutoDraw(True)
    if anecdotes_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > anecdotes_3.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            anecdotes_3.tStop = t  # not accounting for scr refresh
            anecdotes_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'anecdotes_3.stopped')
            anecdotes_3.setAutoDraw(False)
    
    # *blank_3* updates
    if blank_3.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
        # keep track of start time/frame for later
        blank_3.frameNStart = frameN  # exact frame index
        blank_3.tStart = t  # local t and not account for scr refresh
        blank_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'blank_3.started')
        blank_3.setAutoDraw(True)
    if blank_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank_3.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            blank_3.tStop = t  # not accounting for scr refresh
            blank_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_3.stopped')
            blank_3.setAutoDraw(False)
    
    # *feedback_phrase_3* updates
    if feedback_phrase_3.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
        # keep track of start time/frame for later
        feedback_phrase_3.frameNStart = frameN  # exact frame index
        feedback_phrase_3.tStart = t  # local t and not account for scr refresh
        feedback_phrase_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_phrase_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_phrase_3.started')
        feedback_phrase_3.setAutoDraw(True)
    if feedback_phrase_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback_phrase_3.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            feedback_phrase_3.tStop = t  # not accounting for scr refresh
            feedback_phrase_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_phrase_3.stopped')
            feedback_phrase_3.setAutoDraw(False)
    
    # *feedback_fichier_train_3* updates
    if feedback_fichier_train_3.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
        # keep track of start time/frame for later
        feedback_fichier_train_3.frameNStart = frameN  # exact frame index
        feedback_fichier_train_3.tStart = t  # local t and not account for scr refresh
        feedback_fichier_train_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_fichier_train_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_fichier_train_3.started')
        feedback_fichier_train_3.setAutoDraw(True)
    if feedback_fichier_train_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback_fichier_train_3.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            feedback_fichier_train_3.tStop = t  # not accounting for scr refresh
            feedback_fichier_train_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_fichier_train_3.stopped')
            feedback_fichier_train_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DeepBlueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "DeepBlue" ---
for thisComponent in DeepBlueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-15.500000)

# --- Prepare to start Routine "Sam" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
SamComponents = [anecdotes_4, blank_4, feedback_phrase_4, feedback_fichier_train_4]
for thisComponent in SamComponents:
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

# --- Run Routine "Sam" ---
while continueRoutine and routineTimer.getTime() < 15.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *anecdotes_4* updates
    if anecdotes_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        anecdotes_4.frameNStart = frameN  # exact frame index
        anecdotes_4.tStart = t  # local t and not account for scr refresh
        anecdotes_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(anecdotes_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'anecdotes_4.started')
        anecdotes_4.setAutoDraw(True)
    if anecdotes_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > anecdotes_4.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            anecdotes_4.tStop = t  # not accounting for scr refresh
            anecdotes_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'anecdotes_4.stopped')
            anecdotes_4.setAutoDraw(False)
    
    # *blank_4* updates
    if blank_4.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
        # keep track of start time/frame for later
        blank_4.frameNStart = frameN  # exact frame index
        blank_4.tStart = t  # local t and not account for scr refresh
        blank_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'blank_4.started')
        blank_4.setAutoDraw(True)
    if blank_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank_4.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            blank_4.tStop = t  # not accounting for scr refresh
            blank_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_4.stopped')
            blank_4.setAutoDraw(False)
    
    # *feedback_phrase_4* updates
    if feedback_phrase_4.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
        # keep track of start time/frame for later
        feedback_phrase_4.frameNStart = frameN  # exact frame index
        feedback_phrase_4.tStart = t  # local t and not account for scr refresh
        feedback_phrase_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_phrase_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_phrase_4.started')
        feedback_phrase_4.setAutoDraw(True)
    if feedback_phrase_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback_phrase_4.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            feedback_phrase_4.tStop = t  # not accounting for scr refresh
            feedback_phrase_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_phrase_4.stopped')
            feedback_phrase_4.setAutoDraw(False)
    
    # *feedback_fichier_train_4* updates
    if feedback_fichier_train_4.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
        # keep track of start time/frame for later
        feedback_fichier_train_4.frameNStart = frameN  # exact frame index
        feedback_fichier_train_4.tStart = t  # local t and not account for scr refresh
        feedback_fichier_train_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_fichier_train_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_fichier_train_4.started')
        feedback_fichier_train_4.setAutoDraw(True)
    if feedback_fichier_train_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback_fichier_train_4.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            feedback_fichier_train_4.tStop = t  # not accounting for scr refresh
            feedback_fichier_train_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_fichier_train_4.stopped')
            feedback_fichier_train_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SamComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Sam" ---
for thisComponent in SamComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-15.500000)

# --- Prepare to start Routine "Amazon_" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Amazon_Components = [anecdotes_5, blank_5, feedback_phrase_5, feedback_fichier_train_5]
for thisComponent in Amazon_Components:
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

# --- Run Routine "Amazon_" ---
while continueRoutine and routineTimer.getTime() < 15.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *anecdotes_5* updates
    if anecdotes_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        anecdotes_5.frameNStart = frameN  # exact frame index
        anecdotes_5.tStart = t  # local t and not account for scr refresh
        anecdotes_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(anecdotes_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'anecdotes_5.started')
        anecdotes_5.setAutoDraw(True)
    if anecdotes_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > anecdotes_5.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            anecdotes_5.tStop = t  # not accounting for scr refresh
            anecdotes_5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'anecdotes_5.stopped')
            anecdotes_5.setAutoDraw(False)
    
    # *blank_5* updates
    if blank_5.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
        # keep track of start time/frame for later
        blank_5.frameNStart = frameN  # exact frame index
        blank_5.tStart = t  # local t and not account for scr refresh
        blank_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'blank_5.started')
        blank_5.setAutoDraw(True)
    if blank_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank_5.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            blank_5.tStop = t  # not accounting for scr refresh
            blank_5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_5.stopped')
            blank_5.setAutoDraw(False)
    
    # *feedback_phrase_5* updates
    if feedback_phrase_5.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
        # keep track of start time/frame for later
        feedback_phrase_5.frameNStart = frameN  # exact frame index
        feedback_phrase_5.tStart = t  # local t and not account for scr refresh
        feedback_phrase_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_phrase_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_phrase_5.started')
        feedback_phrase_5.setAutoDraw(True)
    if feedback_phrase_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback_phrase_5.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            feedback_phrase_5.tStop = t  # not accounting for scr refresh
            feedback_phrase_5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_phrase_5.stopped')
            feedback_phrase_5.setAutoDraw(False)
    
    # *feedback_fichier_train_5* updates
    if feedback_fichier_train_5.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
        # keep track of start time/frame for later
        feedback_fichier_train_5.frameNStart = frameN  # exact frame index
        feedback_fichier_train_5.tStart = t  # local t and not account for scr refresh
        feedback_fichier_train_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_fichier_train_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_fichier_train_5.started')
        feedback_fichier_train_5.setAutoDraw(True)
    if feedback_fichier_train_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback_fichier_train_5.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            feedback_fichier_train_5.tStop = t  # not accounting for scr refresh
            feedback_fichier_train_5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_fichier_train_5.stopped')
            feedback_fichier_train_5.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Amazon_Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Amazon_" ---
for thisComponent in Amazon_Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-15.500000)

# --- Prepare to start Routine "R2D2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
train_text.reset()
train_text.setText('')
# keep track of which components have finished
R2D2Components = [anecdotes_6, train_text, blank_6, feedback_phrase_6, feedback_fichier_train_6]
for thisComponent in R2D2Components:
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

# --- Run Routine "R2D2" ---
while continueRoutine and routineTimer.getTime() < 15.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *anecdotes_6* updates
    if anecdotes_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        anecdotes_6.frameNStart = frameN  # exact frame index
        anecdotes_6.tStart = t  # local t and not account for scr refresh
        anecdotes_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(anecdotes_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'anecdotes_6.started')
        anecdotes_6.setAutoDraw(True)
    if anecdotes_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > anecdotes_6.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            anecdotes_6.tStop = t  # not accounting for scr refresh
            anecdotes_6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'anecdotes_6.stopped')
            anecdotes_6.setAutoDraw(False)
    
    # *train_text* updates
    if train_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        train_text.frameNStart = frameN  # exact frame index
        train_text.tStart = t  # local t and not account for scr refresh
        train_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'train_text.started')
        train_text.setAutoDraw(True)
    if train_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > train_text.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            train_text.tStop = t  # not accounting for scr refresh
            train_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'train_text.stopped')
            train_text.setAutoDraw(False)
    
    # *blank_6* updates
    if blank_6.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
        # keep track of start time/frame for later
        blank_6.frameNStart = frameN  # exact frame index
        blank_6.tStart = t  # local t and not account for scr refresh
        blank_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'blank_6.started')
        blank_6.setAutoDraw(True)
    if blank_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank_6.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            blank_6.tStop = t  # not accounting for scr refresh
            blank_6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_6.stopped')
            blank_6.setAutoDraw(False)
    
    # *feedback_phrase_6* updates
    if feedback_phrase_6.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
        # keep track of start time/frame for later
        feedback_phrase_6.frameNStart = frameN  # exact frame index
        feedback_phrase_6.tStart = t  # local t and not account for scr refresh
        feedback_phrase_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_phrase_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_phrase_6.started')
        feedback_phrase_6.setAutoDraw(True)
    if feedback_phrase_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback_phrase_6.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            feedback_phrase_6.tStop = t  # not accounting for scr refresh
            feedback_phrase_6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_phrase_6.stopped')
            feedback_phrase_6.setAutoDraw(False)
    
    # *feedback_fichier_train_6* updates
    if feedback_fichier_train_6.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
        # keep track of start time/frame for later
        feedback_fichier_train_6.frameNStart = frameN  # exact frame index
        feedback_fichier_train_6.tStart = t  # local t and not account for scr refresh
        feedback_fichier_train_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(feedback_fichier_train_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'feedback_fichier_train_6.started')
        feedback_fichier_train_6.setAutoDraw(True)
    if feedback_fichier_train_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > feedback_fichier_train_6.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            feedback_fichier_train_6.tStop = t  # not accounting for scr refresh
            feedback_fichier_train_6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_fichier_train_6.stopped')
            feedback_fichier_train_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in R2D2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "R2D2" ---
for thisComponent in R2D2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('train_text.text',train_text.text)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-15.500000)

# --- Prepare to start Routine "blank500" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blank500Components = [blank1]
for thisComponent in blank500Components:
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

# --- Run Routine "blank500" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blank1* updates
    if blank1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blank1.frameNStart = frameN  # exact frame index
        blank1.tStart = t  # local t and not account for scr refresh
        blank1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'blank1.started')
        blank1.setAutoDraw(True)
    if blank1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            blank1.tStop = t  # not accounting for scr refresh
            blank1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank1.stopped')
            blank1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank500" ---
for thisComponent in blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- Prepare to start Routine "Instructions_reco" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instructions_reco_key.keys = []
instructions_reco_key.rt = []
_instructions_reco_key_allKeys = []
# keep track of which components have finished
Instructions_recoComponents = [Instructions_reco_1, instructions_reco_key]
for thisComponent in Instructions_recoComponents:
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

# --- Run Routine "Instructions_reco" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions_reco_1* updates
    if Instructions_reco_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_reco_1.frameNStart = frameN  # exact frame index
        Instructions_reco_1.tStart = t  # local t and not account for scr refresh
        Instructions_reco_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_reco_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructions_reco_1.started')
        Instructions_reco_1.setAutoDraw(True)
    
    # *instructions_reco_key* updates
    waitOnFlip = False
    if instructions_reco_key.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        instructions_reco_key.frameNStart = frameN  # exact frame index
        instructions_reco_key.tStart = t  # local t and not account for scr refresh
        instructions_reco_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_reco_key, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructions_reco_key.started')
        instructions_reco_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructions_reco_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructions_reco_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructions_reco_key.status == STARTED and not waitOnFlip:
        theseKeys = instructions_reco_key.getKeys(keyList=['i'], waitRelease=False)
        _instructions_reco_key_allKeys.extend(theseKeys)
        if len(_instructions_reco_key_allKeys):
            instructions_reco_key.keys = _instructions_reco_key_allKeys[-1].name  # just the last key pressed
            instructions_reco_key.rt = _instructions_reco_key_allKeys[-1].rt
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
    for thisComponent in Instructions_recoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions_reco" ---
for thisComponent in Instructions_recoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instructions_reco_key.keys in ['', [], None]:  # No response was made
    instructions_reco_key.keys = None
thisExp.addData('instructions_reco_key.keys',instructions_reco_key.keys)
if instructions_reco_key.keys != None:  # we had a response
    thisExp.addData('instructions_reco_key.rt', instructions_reco_key.rt)
thisExp.nextEntry()
# the Routine "Instructions_reco" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "blank500" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blank500Components = [blank1]
for thisComponent in blank500Components:
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

# --- Run Routine "blank500" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blank1* updates
    if blank1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blank1.frameNStart = frameN  # exact frame index
        blank1.tStart = t  # local t and not account for scr refresh
        blank1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'blank1.started')
        blank1.setAutoDraw(True)
    if blank1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            blank1.tStop = t  # not accounting for scr refresh
            blank1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank1.stopped')
            blank1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank500" ---
for thisComponent in blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
reco_train = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('C:/Users/cassi/OneDrive/Bureau/Dossier_exp/Expérimentation_Groupe/StimTrainPersoFinal.xlsx'),
    seed=None, name='reco_train')
thisExp.addLoop(reco_train)  # add the loop to the experiment
thisReco_train = reco_train.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisReco_train.rgb)
if thisReco_train != None:
    for paramName in thisReco_train:
        exec('{} = thisReco_train[paramName]'.format(paramName))

for thisReco_train in reco_train:
    currentLoop = reco_train
    # abbreviate parameter names if possible (e.g. rgb = thisReco_train.rgb)
    if thisReco_train != None:
        for paramName in thisReco_train:
            exec('{} = thisReco_train[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Reco_task" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    anecdotes_train_2.setText(anec)
    reco_text_train.reset()
    reco_text_train.setText('')
    # setup some python lists for storing info about the mouse_reco_train
    mouse_reco_train.x = []
    mouse_reco_train.y = []
    mouse_reco_train.leftButton = []
    mouse_reco_train.midButton = []
    mouse_reco_train.rightButton = []
    mouse_reco_train.time = []
    mouse_reco_train.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Reco_taskComponents = [anecdotes_train_2, reco_text_train, validation_train_reco, mouse_reco_train]
    for thisComponent in Reco_taskComponents:
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
    
    # --- Run Routine "Reco_task" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *anecdotes_train_2* updates
        if anecdotes_train_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            anecdotes_train_2.frameNStart = frameN  # exact frame index
            anecdotes_train_2.tStart = t  # local t and not account for scr refresh
            anecdotes_train_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(anecdotes_train_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'anecdotes_train_2.started')
            anecdotes_train_2.setAutoDraw(True)
        
        # *reco_text_train* updates
        if reco_text_train.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reco_text_train.frameNStart = frameN  # exact frame index
            reco_text_train.tStart = t  # local t and not account for scr refresh
            reco_text_train.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reco_text_train, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'reco_text_train.started')
            reco_text_train.setAutoDraw(True)
        
        # *validation_train_reco* updates
        if validation_train_reco.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            validation_train_reco.frameNStart = frameN  # exact frame index
            validation_train_reco.tStart = t  # local t and not account for scr refresh
            validation_train_reco.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(validation_train_reco, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'validation_train_reco.started')
            validation_train_reco.setAutoDraw(True)
        # *mouse_reco_train* updates
        if mouse_reco_train.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_reco_train.frameNStart = frameN  # exact frame index
            mouse_reco_train.tStart = t  # local t and not account for scr refresh
            mouse_reco_train.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_reco_train, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_reco_train.started', t)
            mouse_reco_train.status = STARTED
            mouse_reco_train.mouseClock.reset()
            prevButtonState = mouse_reco_train.getPressed()  # if button is down already this ISN'T a new click
        if mouse_reco_train.status == STARTED:  # only update if started and not finished!
            buttons = mouse_reco_train.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(validation_train_reco)
                        clickableList = validation_train_reco
                    except:
                        clickableList = [validation_train_reco]
                    for obj in clickableList:
                        if obj.contains(mouse_reco_train):
                            gotValidClick = True
                            mouse_reco_train.clicked_name.append(obj.name)
                    x, y = mouse_reco_train.getPos()
                    mouse_reco_train.x.append(x)
                    mouse_reco_train.y.append(y)
                    buttons = mouse_reco_train.getPressed()
                    mouse_reco_train.leftButton.append(buttons[0])
                    mouse_reco_train.midButton.append(buttons[1])
                    mouse_reco_train.rightButton.append(buttons[2])
                    mouse_reco_train.time.append(mouse_reco_train.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Reco_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Reco_task" ---
    for thisComponent in Reco_taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    reco_train.addData('reco_text_train.text',reco_text_train.text)
    # store data for reco_train (TrialHandler)
    reco_train.addData('mouse_reco_train.x', mouse_reco_train.x)
    reco_train.addData('mouse_reco_train.y', mouse_reco_train.y)
    reco_train.addData('mouse_reco_train.leftButton', mouse_reco_train.leftButton)
    reco_train.addData('mouse_reco_train.midButton', mouse_reco_train.midButton)
    reco_train.addData('mouse_reco_train.rightButton', mouse_reco_train.rightButton)
    reco_train.addData('mouse_reco_train.time', mouse_reco_train.time)
    reco_train.addData('mouse_reco_train.clicked_name', mouse_reco_train.clicked_name)
    # the Routine "Reco_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blank400" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    blank400Components = [blank2]
    for thisComponent in blank400Components:
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
    
    # --- Run Routine "blank400" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank2* updates
        if blank2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank2.frameNStart = frameN  # exact frame index
            blank2.tStart = t  # local t and not account for scr refresh
            blank2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank2.started')
            blank2.setAutoDraw(True)
        if blank2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank2.tStop = t  # not accounting for scr refresh
                blank2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank2.stopped')
                blank2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank400Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank400" ---
    for thisComponent in blank400Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'reco_train'


# --- Prepare to start Routine "blank500" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blank500Components = [blank1]
for thisComponent in blank500Components:
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

# --- Run Routine "blank500" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blank1* updates
    if blank1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blank1.frameNStart = frameN  # exact frame index
        blank1.tStart = t  # local t and not account for scr refresh
        blank1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'blank1.started')
        blank1.setAutoDraw(True)
    if blank1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            blank1.tStop = t  # not accounting for scr refresh
            blank1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank1.stopped')
            blank1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank500" ---
for thisComponent in blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- Prepare to start Routine "End" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [text]
for thisComponent in EndComponents:
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

# --- Run Routine "End" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End" ---
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

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
