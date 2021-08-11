from abaqus import *
import testUtils
testUtils.setBackwaedCompatibility()
from abaqusConstants import *

myModel = mdb,Model(name = 'Beam')

import part
mySketch = myModel.ComstrainedSketch(name = 'beamProfile',sheetSize = 250)
mySketch.rectangle(point1 = (-100,10),point2 = (100,-10))
myBeam = myModel.part(name = 'Beam',dimensionality = THREE_D,type = DEFORMABLE_BODY)
myBeam.BaseSolidExtrude(sketch = mySketch,depth =25.0)

import material
mySteel = myModel.material(name = 'Steel')
elasticPropertoes = (209E3,0.3)

import section
mySection = myModel.HomogenousSolidSection(name = 'beamSection',material ='Steel',thickness = 1.0)
region = (myBeam.cells,)
myBeam.SectionAssignment(region = region,sectionName = 'beamSection')

import assembly
myAssembly = mymodel.rootAsswmbly
myInstance = myAssembly.Instance(name = 'beamInstance',part = myBeam,dependent = OFF)

import step
myMolel.StaticSticStep(name = 'beamLoad',previous = 'Initial',timePeriod = 1.0,
					   initialInc = 0.1,description = 'Load the top of the Beam')

import load
endFaceCenter = (-100,0,12.5)
endFace = myInstance.face.findAt(enfFaceCenter,)
