#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on mars 03, 2023, at 13:05
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
expName = 'Expérimentation1_SOLO_TRAIN'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
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
    originPath='C:\\Users\\cassi\\OneDrive\\Bureau\\Dossier_exp\\Expérimentation_Sparrow_Solo\\Expérimentation_SOLO_train_lastrun.py',
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
    size=[1366, 768], fullscr=False, screen=0, 
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
textWelcome = visual.TextStim(win=win, name='textWelcome',
    text='Bienvenue \n\net \n\nmerci pour votre participation !',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Instructions = visual.TextStim(win=win, name='Instructions',
    text="INSTRUCTIONS\n\nVous allez lire et taper 6 anecdotes sur cet ordinateur.\nLa tâche consiste à réécrire des anecdotes qui seront affichées sur l'écran.\nVous verrez le message suivant après chaque validation d'une anecdote :\n'Votre entrée a été enregistrée dans le dossier FAITS' (ou DONNEES, INFO, NOMS, ITEMS, POINTS).\n\nVous allez tout d'abord réaliser une phase d'entrainement pour vous familiariser avec la tâche.\n\nAppuyer sur la touche 'espace' pour commencer",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Training" ---
anecdote_train = visual.TextStim(win=win, name='anecdote_train',
    text='',
    font='Open Sans',
    pos=(0, .25), height=0.05, wrapWidth=None, ori=0.0, 
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
validation_train = visual.TextStim(win=win, name='validation_train',
    text='Valider',
    font='Open Sans',
    pos=(0, -.4), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);
mouse_train = event.Mouse(win=win)
x, y = [None, None]
mouse_train.mouseClock = core.Clock()

# --- Initialize components for Routine "feedback" ---
feedbacktext = visual.TextStim(win=win, name='feedbacktext',
    text='Votre entrée a été sauvegardée dans le fichier :',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
feedback_fichier_train = visual.TextStim(win=win, name='feedback_fichier_train',
    text='',
    font='Open Sans',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "blank500" ---
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Instruciton_reco_train" ---
Instruc_reco_train = visual.TextStim(win=win, name='Instruc_reco_train',
    text="Les anecdotes préalablement vues vont être à nouveau affichées à l'écran.\n\nVous allez devoir écrire le nom du fichier dans lequel l'anecdote a été sauvegardée.\n\nPour rappel, les noms des fichiers sont :  DONNEES, INFO, NOMS, ITEMS, FAITS, POINTS\n\nAppuyez sur la touche 'espace' pour commencer.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "Training_reco" ---
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

# --- Initialize components for Routine "blank500" ---
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Blank500" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "EndScreen" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text="Veuillez appeler l'expérimentateur. ",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Start" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
StartComponents = [textWelcome, Instructions, key_resp]
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
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcome* updates
    if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcome.frameNStart = frameN  # exact frame index
        textWelcome.tStart = t  # local t and not account for scr refresh
        textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textWelcome.started')
        textWelcome.setAutoDraw(True)
    if textWelcome.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textWelcome.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            textWelcome.tStop = t  # not accounting for scr refresh
            textWelcome.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelcome.stopped')
            textWelcome.setAutoDraw(False)
    
    # *Instructions* updates
    if Instructions.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.tStart = t  # local t and not account for scr refresh
        Instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instructions.started')
        Instructions.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
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
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
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
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "Start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Train_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('StimTrain.xlsx'),
    seed=None, name='Train_loop')
thisExp.addLoop(Train_loop)  # add the loop to the experiment
thisTrain_loop = Train_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrain_loop.rgb)
if thisTrain_loop != None:
    for paramName in thisTrain_loop:
        exec('{} = thisTrain_loop[paramName]'.format(paramName))

for thisTrain_loop in Train_loop:
    currentLoop = Train_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrain_loop.rgb)
    if thisTrain_loop != None:
        for paramName in thisTrain_loop:
            exec('{} = thisTrain_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Training" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    anecdote_train.setText(anecdotes_train)
    train_text.reset()
    train_text.setText('')
    # setup some python lists for storing info about the mouse_train
    mouse_train.x = []
    mouse_train.y = []
    mouse_train.leftButton = []
    mouse_train.midButton = []
    mouse_train.rightButton = []
    mouse_train.time = []
    mouse_train.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    TrainingComponents = [anecdote_train, train_text, validation_train, mouse_train]
    for thisComponent in TrainingComponents:
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
    
    # --- Run Routine "Training" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *anecdote_train* updates
        if anecdote_train.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            anecdote_train.frameNStart = frameN  # exact frame index
            anecdote_train.tStart = t  # local t and not account for scr refresh
            anecdote_train.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(anecdote_train, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'anecdote_train.started')
            anecdote_train.setAutoDraw(True)
        
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
        
        # *validation_train* updates
        if validation_train.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            validation_train.frameNStart = frameN  # exact frame index
            validation_train.tStart = t  # local t and not account for scr refresh
            validation_train.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(validation_train, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'validation_train.started')
            validation_train.setAutoDraw(True)
        # *mouse_train* updates
        if mouse_train.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_train.frameNStart = frameN  # exact frame index
            mouse_train.tStart = t  # local t and not account for scr refresh
            mouse_train.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_train, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_train.started', t)
            mouse_train.status = STARTED
            mouse_train.mouseClock.reset()
            prevButtonState = mouse_train.getPressed()  # if button is down already this ISN'T a new click
        if mouse_train.status == STARTED:  # only update if started and not finished!
            buttons = mouse_train.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(validation_train)
                        clickableList = validation_train
                    except:
                        clickableList = [validation_train]
                    for obj in clickableList:
                        if obj.contains(mouse_train):
                            gotValidClick = True
                            mouse_train.clicked_name.append(obj.name)
                    x, y = mouse_train.getPos()
                    mouse_train.x.append(x)
                    mouse_train.y.append(y)
                    buttons = mouse_train.getPressed()
                    mouse_train.leftButton.append(buttons[0])
                    mouse_train.midButton.append(buttons[1])
                    mouse_train.rightButton.append(buttons[2])
                    mouse_train.time.append(mouse_train.mouseClock.getTime())
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
        for thisComponent in TrainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Training" ---
    for thisComponent in TrainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Train_loop.addData('train_text.text',train_text.text)
    # store data for Train_loop (TrialHandler)
    Train_loop.addData('mouse_train.x', mouse_train.x)
    Train_loop.addData('mouse_train.y', mouse_train.y)
    Train_loop.addData('mouse_train.leftButton', mouse_train.leftButton)
    Train_loop.addData('mouse_train.midButton', mouse_train.midButton)
    Train_loop.addData('mouse_train.rightButton', mouse_train.rightButton)
    Train_loop.addData('mouse_train.time', mouse_train.time)
    Train_loop.addData('mouse_train.clicked_name', mouse_train.clicked_name)
    # the Routine "Training" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    feedback_fichier_train.setText(fichier_train)
    # keep track of which components have finished
    feedbackComponents = [feedbacktext, feedback_fichier_train]
    for thisComponent in feedbackComponents:
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
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbacktext* updates
        if feedbacktext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbacktext.frameNStart = frameN  # exact frame index
            feedbacktext.tStart = t  # local t and not account for scr refresh
            feedbacktext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbacktext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedbacktext.started')
            feedbacktext.setAutoDraw(True)
        if feedbacktext.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbacktext.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                feedbacktext.tStop = t  # not accounting for scr refresh
                feedbacktext.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbacktext.stopped')
                feedbacktext.setAutoDraw(False)
        
        # *feedback_fichier_train* updates
        if feedback_fichier_train.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_fichier_train.frameNStart = frameN  # exact frame index
            feedback_fichier_train.tStart = t  # local t and not account for scr refresh
            feedback_fichier_train.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_fichier_train, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_fichier_train.started')
            feedback_fichier_train.setAutoDraw(True)
        if feedback_fichier_train.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_fichier_train.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                feedback_fichier_train.tStop = t  # not accounting for scr refresh
                feedback_fichier_train.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_fichier_train.stopped')
                feedback_fichier_train.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "blank500" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
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
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            if tThisFlipGlobal > blank.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank.stopped')
                blank.setAutoDraw(False)
        
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
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Train_loop'


# --- Prepare to start Routine "Instruciton_reco_train" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
Instruciton_reco_trainComponents = [Instruc_reco_train, key_resp_4]
for thisComponent in Instruciton_reco_trainComponents:
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

# --- Run Routine "Instruciton_reco_train" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruc_reco_train* updates
    if Instruc_reco_train.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruc_reco_train.frameNStart = frameN  # exact frame index
        Instruc_reco_train.tStart = t  # local t and not account for scr refresh
        Instruc_reco_train.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruc_reco_train, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Instruc_reco_train.started')
        Instruc_reco_train.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_4.started')
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
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
    for thisComponent in Instruciton_reco_trainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruciton_reco_train" ---
for thisComponent in Instruciton_reco_trainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "Instruciton_reco_train" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Train_reco_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('StimTrain.xlsx'),
    seed=None, name='Train_reco_loop')
thisExp.addLoop(Train_reco_loop)  # add the loop to the experiment
thisTrain_reco_loop = Train_reco_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrain_reco_loop.rgb)
if thisTrain_reco_loop != None:
    for paramName in thisTrain_reco_loop:
        exec('{} = thisTrain_reco_loop[paramName]'.format(paramName))

for thisTrain_reco_loop in Train_reco_loop:
    currentLoop = Train_reco_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrain_reco_loop.rgb)
    if thisTrain_reco_loop != None:
        for paramName in thisTrain_reco_loop:
            exec('{} = thisTrain_reco_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Training_reco" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    anecdotes_train_2.setText(anecdotes_train)
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
    Training_recoComponents = [anecdotes_train_2, reco_text_train, validation_train_reco, mouse_reco_train]
    for thisComponent in Training_recoComponents:
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
    
    # --- Run Routine "Training_reco" ---
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
        for thisComponent in Training_recoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Training_reco" ---
    for thisComponent in Training_recoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Train_reco_loop.addData('reco_text_train.text',reco_text_train.text)
    # store data for Train_reco_loop (TrialHandler)
    Train_reco_loop.addData('mouse_reco_train.x', mouse_reco_train.x)
    Train_reco_loop.addData('mouse_reco_train.y', mouse_reco_train.y)
    Train_reco_loop.addData('mouse_reco_train.leftButton', mouse_reco_train.leftButton)
    Train_reco_loop.addData('mouse_reco_train.midButton', mouse_reco_train.midButton)
    Train_reco_loop.addData('mouse_reco_train.rightButton', mouse_reco_train.rightButton)
    Train_reco_loop.addData('mouse_reco_train.time', mouse_reco_train.time)
    Train_reco_loop.addData('mouse_reco_train.clicked_name', mouse_reco_train.clicked_name)
    # the Routine "Training_reco" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blank500" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [blank]
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
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            if tThisFlipGlobal > blank.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank.stopped')
                blank.setAutoDraw(False)
        
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
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Train_reco_loop'


# --- Prepare to start Routine "Blank500" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [text]
for thisComponent in Blank500Components:
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

# --- Run Routine "Blank500" ---
while continueRoutine and routineTimer.getTime() < 0.5:
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
        if tThisFlipGlobal > text.tStartRefresh + 0.5-frameTolerance:
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
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Blank500" ---
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.500000)

# --- Prepare to start Routine "EndScreen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
end.keys = []
end.rt = []
_end_allKeys = []
# keep track of which components have finished
EndScreenComponents = [text_2, end]
for thisComponent in EndScreenComponents:
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

# --- Run Routine "EndScreen" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.stopped')
            text_2.setAutoDraw(False)
    
    # *end* updates
    waitOnFlip = False
    if end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end.frameNStart = frameN  # exact frame index
        end.tStart = t  # local t and not account for scr refresh
        end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end.started')
        end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end.status == STARTED and not waitOnFlip:
        theseKeys = end.getKeys(keyList=['i'], waitRelease=False)
        _end_allKeys.extend(theseKeys)
        if len(_end_allKeys):
            end.keys = _end_allKeys[-1].name  # just the last key pressed
            end.rt = _end_allKeys[-1].rt
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
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EndScreen" ---
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end.keys in ['', [], None]:  # No response was made
    end.keys = None
thisExp.addData('end.keys',end.keys)
if end.keys != None:  # we had a response
    thisExp.addData('end.rt', end.rt)
thisExp.nextEntry()
# the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
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
