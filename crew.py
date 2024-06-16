from crewai import Crew, Process
from models.agents.content_development_agents import content_expert, instructional_designer, technical_writer
from models.tasks.content_development_tasks import (
  identification_and_summary_of_main_topics, 
  extraction_of_relevant_information, 
  content_validation,
  course_structure_creation,
  development_of_pedagogical_methodology,
  creating_instruction_guides,
  development_of_teaching_materials,
  creation_of_scripts_for_videos,
  content_review_and_editing
)

crew = Crew(
  agents=[content_expert, instructional_designer, technical_writer],
  tasks=[
    identification_and_summary_of_main_topics,
    extraction_of_relevant_information, 
    content_validation,
    course_structure_creation,
    development_of_pedagogical_methodology,
    creating_instruction_guides,
    development_of_teaching_materials,
    creation_of_scripts_for_videos,
    content_review_and_editing
  ],
  process=Process.sequential,
  # memory=True,
  cache=True,
  max_rpm=100,
)

result = crew.kickoff(inputs={'tema_curso': 'HTML5 e CSS3'})
print(result)