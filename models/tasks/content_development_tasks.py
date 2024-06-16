from crewai import Task
from models.agents.content_development_agents import content_expert, instructional_designer, technical_writer

#============================================================================
# Content Expert tasks
identification_and_summary_of_main_topics = Task(
  description=(
    "Leia os livros fornecidos e identifique os tópicos principais e subtópicos relevantes para o curso sobre {tema_curso}."
  ),
  expected_output='Resumo detalhado dos pontos-chave de cada capítulo, com marcações das seções essenciais. Um documento estruturado com os tópicos principais e subtópicos identificados.',
  agent=content_expert,
  output_file='../../generated_files/content_expert/sumarized-topics.md'
)

extraction_of_relevant_information = Task(
  description=(
    "Extraia informações críticas, dados e exemplos dos textos."
  ),
  expected_output='Banco de dados estruturado com informações extraídas, categorizadas por relevância e tema. Inclua citações diretas e referências bibliográficas.',
  agent=content_expert,
  output_file='../../generated_files/content_expert/extracted-revelant-informations.md'
)

content_validation = Task(
  description=(
    "Verifique a precisão das informações extraídas, comparando com outras fontes confiáveis."
  ),
  expected_output='Documento de validação detalhado, com ajustes feitos conforme necessário e referências adicionais usadas para validação.',
  agent=content_expert,
  output_file='../../generated_files/content_expert/content_validation.md'
)

#============================================================================
# Instructional Designer tasks
course_structure_creation = Task(
  description=(
    "Organize o conteúdo extraído em módulos, unidades e lições."
  ),
  expected_output='Esboço detalhado do curso, especificando os objetivos de aprendizagem para cada módulo e unidade, garantindo uma estrutura lógica e uma progressão de aprendizado clara.',
  agent=instructional_designer,
  output_file='../../generated_files/instructional_designer/course_structure.md'
)

development_of_pedagogical_methodology = Task(
  description=(
    "Aplique princípios pedagógicos na organização do conteúdo, incluindo atividades interativas e avaliações."
  ),
  expected_output='Plano pedagógico detalhado, com métodos de ensino, tipos de atividades e avaliações definidas para cada módulo, otimizando a retenção de conhecimento.',
  agent=instructional_designer,
  output_file='../../generated_files/instructional_designer/pedagogical_methodology.md'
)

creating_instruction_guides = Task(
  description=(
    "Desenvolva guias de instrução claros e detalhados para cada módulo e unidade."
  ),
  expected_output='Guias de instrução completos para alunos, incluindo diretrizes para o uso eficaz dos recursos do curso e explicações detalhadas sobre como completar as atividades e alcançar os objetivos de aprendizagem.',
  agent=instructional_designer,
  output_file='../../generated_files/instructional_designer/instruction_guides.md'
)

#============================================================================
# Technical Writer tasks
development_of_teaching_materials = Task(
  description=(
    "Redigir textos claros e acessíveis baseados no conteúdo organizado pelo Designer Instrucional."
  ),
  expected_output='Materiais didáticos completos, incluindo leituras, slides de apresentação e notas de aula, escritos de maneira clara e livre de jargões desnecessários.',
  agent=technical_writer,
  output_file='../../generated_files/technical_writer/teaching_materials.md'
)

creation_of_scripts_for_videos = Task(
  description=(
    "Escrever scripts detalhados para vídeos instrucionais, descrevendo claramente os conceitos e exemplos importantes."
  ),
  expected_output='Scripts de vídeo bem estruturados e engajadores, incluindo instruções para o uso de gráficos e animações, garantindo que os vídeos sejam informativos e atraentes.',
  agent=technical_writer,
  output_file='../../generated_files/technical_writer/scripts_for_videos.md'
)

content_review_and_editing = Task(
  description=(
    "Revisar e editar todo o conteúdo textual para garantir coesão, clareza e correção gramatical."
  ),
  expected_output='Conteúdo revisado e editado, ajustado para coesão, clareza e consistência, com melhorias contínuas baseadas em feedback.',
  agent=technical_writer,
)