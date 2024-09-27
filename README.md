# Projeto de Conclusão de Curso - Pós-Graduação em Engenharia de Software

Este projeto foi desenvolvido como parte da conclusão do curso de pós-graduação em Engenharia de Software. Ele envolve a criação de um modelo de machine learning para resolver um problema de classificação, juntamente com o desenvolvimento de uma aplicação full stack que consome o modelo treinado para realizar predições.


## Para esse projeto, foram utilizadas as seguintes tecnologias e versões:


### Backend
    
    Python - 22.3.1
    Flask - 2.1.3
    Flask-SQLAlchemy - 2.5.1
    SQLAlchemy - 1.4.41
    Scikit-Learn - 1.5.2
    Pandas - 2.2.2
    Pytest - 8.3.3
    Jupyter - 1.1.1

### Frontend

    Node.js - 18.17.0
    React - 18
    Next.js - 14.0.4
	TypeScript - 5.3.3
	ESLint - 8.0.0
	Tailwind CSS - 3.3.0

## Estrutura do Projeto

### 1. Treinamento do Modelo de Machine Learning

O modelo de machine learning foi treinado usando um dataset selecionado e passou pelas etapas de:

<ul>
    <li>Carga e pré-processamento dos dados (incluindo normalização/padronização).</li>
    <li>Separação dos dados em conjunto de treino e teste.</li>
    <li>Treinamento utilizando algoritmos clássicos: KNN, Árvore de Decisão, Naive Bayes e SVM.</li>
    <li>Otimização de hiperparâmetros com cross-validation.</li>
    <li>Avaliação e comparação dos resultados.</li>
    <li>O modelo resultante foi exportado e utilizado no backend da aplicação.</li>
</ul>

### 2. Aplicação Full Stack

A aplicação full stack permite:

<ul>
    <li>Entrada de novos dados no frontend para que o modelo faça a predição..</li>
    <li>Exibição do resultado da predição diretamente na interface.</li>
</ul>

