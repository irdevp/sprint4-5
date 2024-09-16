[Python]: https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white
[Flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Docker]:https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[AWS]: https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&amazon-aws&logoColor=white



<h1 align="center">HotelPriceClassifier</h1>

![undraw_apartment_rent_o-0-ut](https://github.com/user-attachments/assets/61b022bf-d91a-4f7f-97ba-ccb0d6bf1431)


<p align="center">O projeto HotelPriceClassifier visa desenvolver um modelo de machine learning para classificar reservas de hotéis com base no preço médio por quarto. Utilizando um dataset de reservas, o modelo irá categorizar cada reserva em três faixas de preço distintas, permitindo uma análise mais detalhada e previsões automatizadas sobre o custo das estadias. A solução será exposta através de uma API, permitindo que sistemas externos realizem consultas e obtenham previsões de forma rápida e eficiente, contribuindo para otimizar a gestão de preços e tomada de decisão no setor hoteleiro.</p>

<hr>

![MIT License](https://img.shields.io/badge/License-MIT-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9-yellow)
![Flask](https://img.shields.io/badge/Flask-3.0.3-blue)
![Docker](https://img.shields.io/badge/Docker-20.10.7-blue)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)



## 📌 URL para Acesso

- Coloque aqui o link para acessar a API na AWS


## 🛠 Metodologia e Organização

- **Scrum**: Metodologia ágil de gerenciamento de projetos que ajuda equipes a se auto-organizar e trabalhar em conjunto para atingir um objetivo comum.
- **Trello**: Utilizado para organização de tarefas.


## 🧑‍🤝‍🧑 Divisão de Tarefas

- **Cicero Lucas Silva**:
  - Conexão com o banco
  - Modelo do Banco API
- **Francisco Ivo Bezerra**:
  - Sage Maker
  - Banco RDS
  - Treinamento do Modelo
- **Igor Melo Gonçalo**:
  - Estrutura Base da API
  - Docker API
  - End Points
- **Jhonatan Sousa**:
  - ScrumMaster
  - Organização e Documentação
  - READ.me

## 📌 Funcionalidades

- Classificação de reservas de hotéis em três faixas de preço diferentes com base no preço médio por quarto.
- API RESTful desenvolvida com Flask para fazer previsões automatizadas.
- Integração com AWS S3, EC2, RDS, e SageMaker para armazenamento de dados, gerenciamento de banco de dados e treinamento de modelos de machine learning.
- Desenvolvimento e implementação de containers Docker para facilitar a implantação.

## ⚙️ Tecnologias Utilizadas

### Back-end

- **Python e Flask**: Desenvolvimento da API para previsões.
- **Docker**: Containerização da aplicação para fácil implantação.
- **MySQL**: Banco de dados utilizado para armazenar informações das reservas de hotéis.

### Serviços AWS
- **S3**: Armazenar o modelo de machine learning treinado e outros arquivos necessários.
- **EC2**: Hospedar a API publicamente, permitindo o acesso e consumo da mesma.
- **RDS**: Armazenar os dados de reservas e permite o treinamento contínuo do modelo
- **SageMaker**: Serviço para treinar e otimizar o modelo de machine learning.

<hr>

## 📁Estrutura de Pastas do Projeto

```
    ├── assets/
    ├── src/
    │    ├── api/
    │    │   └── v1/
    │    │       └── endpoints/
    │    ├── core/
    │    │   
    │    ├── models/
    │    │   
    │    └── scripts/
                 

```
<hr>

## ❕ Justificativa da Escolha do Modelo
O RandomForestClassifier foi escolhido por seu equilíbrio entre simplicidade e robustez, sua capacidade de evitar overfitting por meio do ensemble de árvores, e por ser um algoritmo que funciona bem em várias situações, mesmo sem grande pré-processamento dos dados. Ele fornece um bom desempenho com relativamente pouco ajuste fino, o que o torna uma excelente escolha para a classificação.

- **Capacidade de lidar com dados complexos:** O Random Forest pode capturar relações complexas nos dados, pois é composto por várias árvores de decisão que, em conjunto, aumentam a capacidade preditiva.

- **Robustez ao overfitting:** Ao contrário de uma única árvore de decisão que pode facilmente superestimar o padrão dos dados (overfitting), o Random Forest constrói múltiplas árvores de decisão com subconjuntos aleatórios de dados e características. A votação entre essas árvores reduz o risco de overfitting, especialmente com dados ruidosos ou de grande dimensionalidade.

- **Facilidade de uso e bom desempenho geral:** O Random Forest funciona bem em diversas tarefas de classificação, mesmo com dados não normalizados, e lida bem com variáveis categóricas. Ele também tem poucos hiperparâmetros críticos, o que facilita sua aplicação sem ajustes complexos.

- **Redução de variância:** O Random Forest combina o output de muitas árvores de decisão independentes para produzir uma predição final. Isso ajuda a reduzir a variância do modelo, resultando em previsões mais estáveis e confiáveis.


<hr>

## 🚀 Começando

### Pré-requisitos

- Conta AWS configurada com permissões para S3, EC2, RDS, e SageMaker.
- Docker instalado para a containerização da aplicação.
- Python e bibliotecas necessárias listadas no `requirements.txt`.



 **Documentação do Desenvolvimento Passo a Passo**:

[Documentação do Projeto de Machine Learning e API.docx](https://github.com/user-attachments/files/17007003/Documentacao.do.Projeto.de.Machine.Learning.e.API.docx)



<hr>

## ❎ Dificuldades Encontradas

- **Falta de Experiência Técnica**: Falta de domínio sobre as tecnologias e ferramentas necessárias para o projeto.

- **Gestão de Tempo**: Dificuldade em cumprir prazos e gerenciar o tempo de forma eficiente.

- **Comunicação Ineficiente**: Dificuldade em manter uma comunicação clara e eficaz entre os membros da equipe.


## ✅ Lições Aprendidas

- **Gestão de Tempo e Priorização**: Aprender a definir prioridades e gerenciar o tempo de forma mais eficaz.

- **Flexibilidade e Adaptabilidade**: Aprender a ser mais flexível e se adaptar rapidamente a mudanças durante o projeto.

- **Aprimoramento das Habilidades Técnicas**: A importância de investir tempo em capacitação e aprendizado contínuo.



<hr>
<table >
  <tr>
    <td align="center">
      <a href="https://github.com/cicero-lucas">
        <img src="https://avatars.githubusercontent.com/u/109551418?v=4" width="120" alt="Cicero Lucas" style="border-radius: 50%;">
      </a>
      <p><strong>Cicero Lucas</strong></p>
      <a href="https://github.com/cicero-lucas">Perfil no GitHub</a>
    </td>
    <td align="center">
      <a href="https://github.com/Ivo-Aragao">
        <img src="https://avatars.githubusercontent.com/u/105293872?v=4" width="120" alt="Francisco Ivo" style="border-radius: 50%;">
      </a>
      <p><strong>Francisco Ivo</strong></p>
      <a href="https://github.com/Ivo-Aragao">Perfil no GitHub</a>
    </td>
    <td align="center">
      <a href="https://github.com/irdevp">
        <img src="https://avatars.githubusercontent.com/u/47428695?v=4" width="120" alt="Igor Melo" style="border-radius: 50%;">
      </a>
      <p><strong>Igor Melo</strong></p>
      <a href="https://github.com/irdevp">Perfil no GitHub</a>
    </td>
    <td align="center">
      <a href="https://github.com/JohnOliverz">
        <img src="https://avatars.githubusercontent.com/u/171964865?v=4" width="120" alt="Jhonatan Sousa" style="border-radius: 50%;">
      </a>
      <p><strong>Jhonatan Sousa</strong></p>
      <a href="https://github.com/JohnOliverz">Perfil no GitHub</a>
    </td>
  </tr>
</table>
