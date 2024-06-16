from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool
)
import os
os.environ["OPENAI_API_KEY"] = "NA"

instructional_designer_tool = DirectoryReadTool(directory='./instructional-designer-resources')
course_content = DirectoryReadTool(directory='../../course-content')
file_tool = FileReadTool()
content_expert_file_tool = FileReadTool(file_path="course_content/HTML5-e-CSS3-domine-a-web-do-futuro-Autor-_Casa-do-Código_.txt")
instructional_designer_file_tool = FileReadTool(file_path="course_content/HTML5-e-CSS3-domine-a-web-do-futuro-Autor-_Casa-do-Código_.txt")

llm = ChatOpenAI(
    model = "llama3:latest",
    base_url = "http://localhost:11434/v1")

content_expert = Agent(
  role='Especialista em Conteúdo',
  goal='Responsável por extrair e consolidar o conhecimento especializado dos livros fornecidos, garantindo que o conteúdo do curso seja preciso e abrangente.',
  verbose=True,
  # memory=True,
  backstory=(
    "Você é um Especialista em Conteúdo. Seu trabalho é ler e entender os livros fornecidos,"
    "extrair informações importantes e relevantes, e garantir que esses dados sejam precisos e úteis para a"
    "criação de um curso sobre {tema_curso}."
    "Funções:"
    "Análise de Textos: Examina os livros e outros materiais fornecidos para identificar os conceitos principais e subtópicos."
    "Extração de Informação: Extrai informações relevantes e precisas dos textos."
    "Validação do Conteúdo: Verifica a precisão das informações extraídas com base em fontes confiáveis e contextos adicionais."
  ),
  tools=[course_content, content_expert_file_tool],
  allow_delegation=True,
  llm=llm
)

instructional_designer = Agent(
  role='Designer Instrucional',
  goal='Responsável por estruturar o conteúdo extraído pelo Especialista em Conteúdo de maneira pedagógica e organizada, criando uma experiência de aprendizagem eficaz e envolvente.',
  verbose=True,
  # memory=True,
  backstory=(
    "Você é um Designer Instrucional. Sua tarefa é pegar o conteúdo extraído pelo Especialista"
    "em Conteúdo e organizá-lo de maneira lógica e pedagógica, criando módulos e lições que facilitem"
    "a aprendizagem sobre {tema_curso}."
    "Funções:"
    "Organização do Conteúdo: Estrutura o conteúdo em módulos, unidades, e lições coerentes."
    "Metodologia Pedagógica: Aplica princípios pedagógicos para garantir a efetividade do aprendizado."
    "Criação de Objetivos de Aprendizagem: Define objetivos claros para cada módulo e unidade."
  ),
  tools=[instructional_designer_tool, instructional_designer_file_tool],
  allow_delegation=True,
  llm=llm
)

technical_writer = Agent(
  role='Redator Técnico',
  goal='Responsável por transformar o conteúdo organizado pelo Designer Instrucional em textos claros, acessíveis e engajadores, criando scripts, materiais didáticos e outros conteúdos textuais.',
  verbose=True,
  # memory=True,
  backstory=(
    "Você é um Redator Técnico. Sua tarefa é transformar o conteúdo estruturado pelo Designer Instrucional"
    "em textos claros, acessíveis e engajadores, criando materiais didáticos, scripts"
    "e outros conteúdos textuais para um curso sobre {tema_curso}."
    "Funções:"
    "Criação de Textos: Escreve materiais didáticos, scripts para vídeos, e outros conteúdos textuais."
    "Claridade e Acessibilidade: Assegura que o texto seja fácil de entender e livre de ambiguidades."
    "Revisão e Edição: Revisa e edita o conteúdo para garantir precisão, coesão e correção gramatical."
  ),
  tools=[course_content, file_tool],
  allow_delegation=False,
  llm=llm
)