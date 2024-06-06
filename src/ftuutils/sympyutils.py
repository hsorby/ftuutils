import json
from sympy import *
init_printing()

def checkUserPhenomenologicalPHS(statevector,JMatrix,RMatrix,BMatrix,EMatrix,QMatrix,uvector):
      stateVector = None
      try:
        Matrixx = Matrix(sympify(statevector))
        stateVector = Matrixx
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        statevector = {'success':True,'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        statevector ={'exception':f'{inst}','success':False}

      try:
        Matrixx = Matrix(sympify(JMatrix))
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        JMatrix = {'success':True,'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        JMatrix = {'exception':f'{inst}','success':False}

      try:
        Matrixx = Matrix(sympify(RMatrix))
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        RMatrix = {'success':True,'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        RMatrix = {'exception':f'{inst}','success':False}    

      try:
        Matrixx = Matrix(sympify(BMatrix))
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        BMatrix = {'success':True,'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        BMatrix = {'exception':f'{inst}','success':False}

      try:
        Matrixx = Matrix(sympify(EMatrix))
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        EMatrix = {'success':True,'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        EMatrix = {'exception':f'{inst}','success':False}       
      QMatrixx = None
      try:
        Matrixx = Matrix(sympify(QMatrix))
        QMatrixx = Matrixx
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        QMatrix = {'success':True,'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        QMatrix = {'exception':f'{inst}','success':False}       

      try:
        Matrixx = Matrix(sympify(uvector))
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        uvector = {'success':True, 'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        uvector = {'exception':f'{inst}','success':False}
      #Create the hamiltonian as pseudo-hamiltonian
      try:
        Matrixx = 0.5*stateVector.T*QMatrixx*stateVector
        hamiltonian = {'result':str(Matrixx),'success':True}
      except Exception as inst:
        hamiltonian ={'exception':f'{inst}','success':False}

      try:
        Matrixx = QMatrixx*stateVector
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        hamiltonianderivatives = {'success':True,'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        hamiltonianderivatives ={'exception':f'{inst}','success':False}
      Bbarm = {'success':True,'result':{'cols':0,'rows':0,'elements':[]}}
      Cxm = {'success':True,'result':{'cols':0,'rows':0,'elements':[]}}

      return json.dumps({
      'statevector':statevector,
      'hamiltonian':hamiltonian,
      'hamiltonianderivatives':hamiltonianderivatives,
      'JMatrix':JMatrix,
      'RMatrix':RMatrix,
      'BMatrix':BMatrix,
      'BbarMatrix':Bbarm,
      'EMatrix':EMatrix,
      'QMatrix':QMatrix, 
      'Cmatrix':Cxm,         
      'uvector':uvector,
      'isphenomenological':True
      })
    
def checkUserPHS(statevector,hamiltonian,hamiltonianderivatives,JMatrix,RMatrix,BMatrix,EMatrix,QMatrix,uvector):
      try:
        Matrixx = Matrix(sympify(statevector))
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        statevector = {'success':True,'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        statevector ={'exception':f'{inst}','success':False}

      try:
        hamiltonian = {'result':str(sympify(hamiltonian)),'success':True}
      except Exception as inst:
        hamiltonian ={'exception':f'{inst}','success':False}

      try:
        Matrixx = Matrix(sympify(hamiltonianderivatives))
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        hamiltonianderivatives = {'success':True,'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        hamiltonianderivatives ={'exception':f'{inst}','success':False}

      try:
        Matrixx = Matrix(sympify(JMatrix))
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        JMatrix = {'success':True,'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        JMatrix = {'exception':f'{inst}','success':False}

      try:
        Matrixx = Matrix(sympify(RMatrix))
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        RMatrix = {'success':True,'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        RMatrix = {'exception':f'{inst}','success':False}    

      try:
        Matrixx = Matrix(sympify(BMatrix))
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        BMatrix = {'success':True,'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        BMatrix = {'exception':f'{inst}','success':False}

      try:
        Matrixx = Matrix(sympify(EMatrix))
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        EMatrix = {'success':True,'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        EMatrix = {'exception':f'{inst}','success':False}       

      try:
        Matrixx = Matrix(sympify(QMatrix))
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        QMatrix = {'success':True,'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        QMatrix = {'exception':f'{inst}','success':False}       

      try:
        Matrixx = Matrix(sympify(uvector))
        elems = []
        for i in range(Matrixx.rows):
          for j in range(Matrixx.cols):
            elems.append(str(Matrixx[i,j]))
        uvector = {'success':True, 'result':{'cols':Matrixx.cols,'rows':Matrixx.rows,'elements':elems}}
      except Exception as inst:
        uvector = {'exception':f'{inst}','success':False}

      Bbarm = {'success':True,'result':{'cols':0,'rows':0,'elements':[]}}
      Cxm = {'success':True,'result':{'cols':0,'rows':0,'elements':[]}}

      return json.dumps({
      'statevector':statevector,
      'hamiltonian':hamiltonian,
      'hamiltonianderivatives':hamiltonianderivatives,
      'JMatrix':JMatrix,
      'RMatrix':RMatrix,
      'BMatrix':BMatrix,
      'BbarMatrix':Bbarm,
      'EMatrix':EMatrix,
      'QMatrix':QMatrix, 
      'Cmatrix':Cxm,       
      'uvector':uvector,
      'isphenomenological':False
      })    

