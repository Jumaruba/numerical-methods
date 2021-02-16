<h2 align="center"> Numerical Methods (MNUM) </h2> 

<p align="center"> Explanation and code for classes of numerical methods</p> 

<p align="center"> Final Grade: 18   </p> 


[Subject Goals](https://sigarra.up.pt/feup/en/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=436436)

# Table of contents 
- [Zeros of functions - C++](#zeros-c)   
- [Zeros of functions - Python](#zeros-python) 
- [Gauss - Python](#gauss-python)  
- [Integrals - Python](#integrals-python)  
- [Diferential Equations - Python](#eqDif-python)  
- [Optimization - Python](#optimization-python)   
- [Jupyter notebook](#jupyterNotebook-python)   
- [Revisions](#revision)  
  - [Levenberg Marquadt](#levenberg)  
  - [Revision to the 2nd test](#secondTest)  
  - [Previous Exams](#previousExams)
  
# Content
  The language in which algorithm was developed is explicitly written in the title of each content. However, the biggest part of the code in this repository was developed in python, in order to improve understandment.  
  
<a name="zeros-c"></a> 
### Zeros of functions - C++

|Method name| Explanation|
|---|---|
| [Successive Bissection](https://github.com/Jumaruba/MNUM/blob/master/Real_Zeros_functions/C%2B%2B/successiveBissection.cpp) | to add |
| [Falsi Position](https://github.com/Jumaruba/MNUM/blob/master/Real_Zeros_functions/C%2B%2B/falsiPosition.cpp) | to add |
| [Picard Peano One Variable](https://github.com/Jumaruba/MNUM/blob/master/Real_Zeros_functions/C%2B%2B/pircardPeano_1variable.cpp) | to add |
| [Newton Method One Variable](https://github.com/Jumaruba/MNUM/blob/master/Real_Zeros_functions/C%2B%2B/newtonMethod_1variable.cpp) | to add |

<a name="zeros-python"></a>
### Zeros of functions - Python 

|Method name| Explanation|
|---|---|
| [Sucessive Bissection](https://github.com/Jumaruba/MNUM/blob/master/Real_Zeros_functions/Python/bissection.py)| to add|
| [Falsi Position](https://github.com/Jumaruba/MNUM/blob/master/Real_Zeros_functions/Python/falsiPosition.py) | to add |
| [Picard Peano One Variable](https://github.com/Jumaruba/MNUM/blob/master/Real_Zeros_functions/Python/picardPeano.py) | to add |
| [Newton Method One Variable](https://github.com/Jumaruba/MNUM/blob/master/Real_Zeros_functions/Python/newtonMethod.py)| to add|
| [Picard Peano Two Variables](https://github.com/Jumaruba/MNUM/blob/master/Real_Zeros_functions/Python/picarPeano_2variables.py) | to add |
| [Newton Method Two Variable](https://github.com/Jumaruba/MNUM/blob/master/Real_Zeros_functions/Python/newtonMethod_2variables.py) | to add |

<a name="gauss-python"></a>
### Gauss - Python

|Method Name| Explanation|
|---|---|
|[Simple Gauss](https://github.com/Jumaruba/MNUM/blob/master/Gauss_Methods/Gauss.py)| [Algorithm](https://github.com/Jumaruba/MNUM/tree/master/Gauss_Methods) and [Extern Stability](https://github.com/Jumaruba/MNUM/blob/master/Gauss_Methods/Estabilidade_Externa.pdf)|
|[Simple Gauss with numpy](https://github.com/Jumaruba/MNUM/blob/master/Gauss_Methods/Gauss_numpy.py)| to add|
|[Gauss Seidel](https://github.com/Jumaruba/MNUM/blob/master/Gauss_Methods/Gauss_Seidel.py)| to add| 
|[Gauss Jacobi](https://github.com/Jumaruba/MNUM/blob/master/Gauss_Methods/Gauss_Jacobi.py)|to add| 

<a name="integrals-python"></a>
### Integrals - Python 

|Method Name| Explanation| 
|---|---|
|[Regra dos Trapézios](https://github.com/Jumaruba/MNUM/blob/master/Integrais/Trapezio.py)| [PDF](https://github.com/Jumaruba/MNUM/blob/master/Integrais/Regra_dos_trapezios.pdf)| 
|[Simpson](https://github.com/Jumaruba/MNUM/blob/master/Integrais/Simpson.py)| to add| 

<a name="eqDif-python"></a>
### Diferential Equations - Python 

|Method Name| Explanation| 
|---|---|
|[Euler](https://github.com/Jumaruba/MNUM/blob/master/Diferenciais/Euler.py) | [Image](https://github.com/Jumaruba/MNUM/blob/master/Images/mnum_euler.png) |
|[Runge Kutta 2](https://github.com/Jumaruba/MNUM/blob/master/Diferenciais/RK2.py) | [Image](https://github.com/Jumaruba/MNUM/blob/master/Images/mnum_rk2.png) |
|[Runge Kutta 4](https://github.com/Jumaruba/MNUM/blob/master/Diferenciais/RK4.py) | To add | 
|[Runge Kutta 4 - systems](https://github.com/Jumaruba/MNUM/blob/master/Diferenciais/RK4_Sistemas_diferenciais.py) | To add |
|[Runge Kutta 4 - superior order](https://github.com/Jumaruba/MNUM/blob/master/Diferenciais/RK4_Sistema_Ordem_superior.py) | [PDF](https://github.com/Jumaruba/MNUM/blob/master/Diferenciais/RK4_Ordem_Superior.pdf), obs: first must learn RK4 systems|

<a name="optimization-python"></a>
### Optimization - Python 
|Method Name| Explanation|
|---|---|
|[Search/Golden Search](https://github.com/Jumaruba/MNUM/blob/master/Optimiza%C3%A7%C3%A3o/Pesquisa.py)| [PDF](https://github.com/Jumaruba/MNUM/blob/master/Optimiza%C3%A7%C3%A3o/Golden-Search.pdf) | 
| [Multidimensional/Quadrica](https://github.com/Jumaruba/MNUM/blob/master/Optimiza%C3%A7%C3%A3o/Quadrica.py) | To add | 
| [Multidimensional/Gradient](https://github.com/Jumaruba/MNUM/blob/master/Optimiza%C3%A7%C3%A3o/Multidimensional_gradiente.py) | [PDF](https://github.com/Jumaruba/MNUM/blob/master/Optimiza%C3%A7%C3%A3o/Golden-Search.pdf)| 
| [Multidimensional/Levenberg-Marquardt](https://github.com/Jumaruba/MNUM/blob/master/Optimiza%C3%A7%C3%A3o/Levenberg-Marquardt.py) | To add |

<a name="jupyterNotebook-python"></a>
## Jupyter notebook
You can also check some jupyter notebook with the code: 
- [Diferential equations](https://github.com/Jumaruba/MNUM/blob/master/Jupyter_notebooks/Diferenciais.ipynb)    
- [Integrals](https://github.com/Jumaruba/MNUM/blob/master/Jupyter_notebooks/Integrais.ipynb)  
- [Optimization](https://github.com/Jumaruba/MNUM/blob/master/Jupyter_notebooks/Optimiza%C3%A7%C3%A3o.ipynb)  

<a name="revision"></a>
# Revisions  
Here are some colected exercises for tests and exames to revision and test your knowledge.

<a name="levenberg"></a>
## Levenberg Marquadt 
- [Questions](https://github.com/Jumaruba/MNUM/blob/master/Exames_testes/Revisao_teste2.3/MIEIC_Optimizacao_Aula_13_12_2019.pdf)
- [Question_1 solution](https://github.com/Jumaruba/MNUM/blob/master/Exames_testes/Revisao_teste2.3/Question_1.ipynb)
- [Question_2 soltuion](https://github.com/Jumaruba/MNUM/blob/master/Exames_testes/Revisao_teste2.3/Question_2.ipynb)

<a name="Optimization"></a>
## Optmization exercises 
- [Questions](https://github.com/Jumaruba/MNUM/blob/master/Exames_testes/Optimization_exercises/Enunciado.pdf)   
- [Question_1 solution](https://github.com/Jumaruba/MNUM/blob/master/Exames_testes/Optimization_exercises/Question_1.ipynb)   
- [Question_2 solution](https://github.com/Jumaruba/MNUM/blob/master/Exames_testes/Optimization_exercises/Question_2.ipynb)  
- [Question_3 solution](https://github.com/Jumaruba/MNUM/blob/master/Exames_testes/Optimization_exercises/Question_3.ipynb)  
- [Question_4 solution](https://github.com/Jumaruba/MNUM/blob/master/Exames_testes/Optimization_exercises/Question_4.ipynb)  

<a name="secondTest"></a>
### Revision to the 2nd test
These exercises do not include kaletsy algorithm.  
- [Questions](https://github.com/Jumaruba/MNUM/blob/master/Exames_testes/Revisao_teste2.2/Enunciado.pdf)  
- [Solutions](https://github.com/Jumaruba/MNUM/blob/master/Exames_testes/Revisao_teste2.2/Solutions.ipynb)

<a name="previousExams"></a>
### Previous Exams 
|Exame|Exame without solution| Exam with solution| Code Solution|
|---|---|---|---|
|2017.1|[Link](https://github.com/Jumaruba/MNUM/tree/master/Exames_testes/Exames_anteriores/2017.1/Enuciado_sem_resposta)|[Link](https://github.com/Jumaruba/MNUM/tree/master/Exames_testes/Exames_anteriores/2017.1/Enunciado_com_resposta)|[Link](https://github.com/Jumaruba/MNUM/tree/master/Exames_testes/Exames_anteriores/2017.1/Solutions)|
