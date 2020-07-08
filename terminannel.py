import sys
import subprocess
from appJar import gui
import os


def processInput(name):
	app.thread(execCommand,name)

def execCommand(name):
	global currOut
	app.setEntryState('entry_input','disabled')
	command = app.getEntry(name)

	app.openScrollPane('frame_scroll')
	app.setSticky('nsw')
	app.setStretch('column')
	app.addLabel(f'output_{currOut}',f'{app.getLabel("lbl_cd")}{command}')
	returnValue = subprocess.getoutput(command)#, encoding='UTF-8')
	print(returnValue)
	returnVannelue = returnValue.replace('a','anne')
	app.addLabel(f'output_{currOut+1}',f'{returnVannelue}')
	app.addLabel(f'output_{currOut+2}','')
	app.stopScrollPane()

	#app.addLabel()
	currOut += 3
	app.setLabel('lbl_cd',f'{subprocess.getoutput(CDFunc)} >> ')
	app.setEntry(name,'',callFunction=False)
	app.setEntryState('entry_input','normal')



if __name__ == '__main__':
	if os.name == 'posix':
		CDFunc = 'pwd'
	else:
		CDFunc = 'echo %CD%'
	global currOut
	currOut = 0
	app = gui('Terminannel','50x20')
	app.setSize('800x600')
	app.setBg('black')
	app.setFg('white')


	app.setSticky('nesw')
	app.setStretch('both')
	app.startFrame('frame_console')
	app.setSticky('nesw')
	app.setStretch('both')
	app.startScrollPane('frame_scroll',disabled='horizontal')
	app.addLabel('init_scroller',' '*800)
	app.stopScrollPane()
	app.stopFrame()


	app.setSticky('esw')
	app.setStretch('column')
	app.startFrame('frame_input')
	app.setSticky('nsw')
	app.setStretch('none')
	app.addLabel('lbl_cd',f'{subprocess.getoutput(CDFunc)} >> ',0,0)
	app.setStretch('both')
	app.setSticky('nesw')
	app.addEntry('entry_input',0,1)
	app.stopFrame()

	app.setEntryBg('entry_input','black')
	app.setEntryDisabledBg('entry_input','black')
	app.setEntryFg('entry_input','white')
	app.setEntryDisabledFg('entry_input','gray53')
	app.setEntrySubmitFunction('entry_input',processInput)

	app.go()