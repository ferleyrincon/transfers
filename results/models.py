from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'results'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pago_total = models.CurrencyField()

    p_sex = models.IntegerField(
    choices=[
        [1, 'Hombre'],
        [2, 'Mujer'],
        [3, 'Otro'],
    ], label="1. ¿Cuál es su sexo?")
    p_age = models.IntegerField(label="2. Edad")
    p_married = models.IntegerField(
    choices=[
        [1, 'Unión libre'],
        [2, 'Casado (a)'],
        [3, 'Viudo (a)'],
        [4, 'Soltero (a)'],
        [5, 'Divorciado (a)/Separado(a)'],
    ], label="3. Estado civil")
    p_job = models.IntegerField(
    choices=[
        [1,'Solo estudio'],
        [2,'Desempleado'],
        [3,'Empleado a jornada completa'],
        [4,'Empleado a tiempo parcial'],
        [5,'Trabajador independiente'],
        [6,'Trabajador no remunerado (por ejemplo: ama de casa, empresa familiar)'],
        [7,'Retirado/pensionado'],
        [8,'Otro'],
        [9,'No sabe']
    ], label="4. ¿Cuál es su situación laboral actual?")
    p_educ = models.IntegerField(
    choices=[
        [1,'Ninguno'],
        [2,'Primaria'],
        [3,'Bachillerato'],
        [4,'Técnico o Tecnólogo'],
        [5,'Pregrado'],
        [6,'Posgrado (Especialización, Maestría, Doctorado)']
    ], label="5. ¿Cuál es el nivel educativo más alto que cursó o está cursando?")
    p_educ1 = models.IntegerField(label="6.¿Cuántos años de educación ha cursado en el nivel educativo que indicó previamente? (por ejemplo, si antes seleccionó Bachillerato debe escribir el número de años de Bachillerato que ha completado)")
    p_ocupation = models.StringField(label="7.Escriba el nombre de su profesión/ocupación/carrera")
    p_health = models.IntegerField(
    choices=[
        [1,'Subsidiado'],
        [2,'Contributivo (incluye regímenes especiales)']
    ], label="9. ¿A qué régimen de seguridad social en salud pertenece?")
    p_inc = models.IntegerField(
    choices=[
        [1,'Menos del Salario Mínimo Mensual (SMMLV)'],
        [2,'Entre 1 SMMLV - $ 1.500.000'],
        [3,'Entre $ 1.500.000 - $ 2.000.000'],
        [4,'Entre $ 2.000.000 - $ 4.000.000'],
        [5,'Mayor a $ 4.000.000'],
    ], label="8. ¿Cuál es el rango de su ingreso mensual?")

    p_pc = models.IntegerField(
    choices=[
        [1,'Portátil'],
        [2,'Equipo de escritorio']
    ], label="10. ¿Qué tipo de computador usó durante la actividad?")

    p_daughter = models.IntegerField(label="11.1. Número de hijas")
    p_son = models.IntegerField(label="11.2. Número de hijos ")

    p_sister = models.IntegerField(label="12.1. Número de hermanas vivas")
    p_brother= models.IntegerField(label="12.2. Número de hermanos vivos")

    p_parents = models.IntegerField(
    choices=[
        [1, 'Fallecieron'],
        [2, 'Viven en su misma casa'],
        [3, 'Viven en una casa en la misma ciudad'],
        [4, 'Viven en otra ciudad'],
    ], label="13. Sus padres:")

    p_mother_age= models.IntegerField(label="15.1. ¿Cuántos años tiene(alcanzó) su papá?")
    p_father_age= models.IntegerField(label="15.2. ¿Cuántos años tiene(alcanzó) su mamá?")

    p_parents_married = models.IntegerField(
    choices=[
        [1, 'Viven (vivían) juntos [casados, unión libre]'],
        [2, 'Son (eran) separados [divorciados]'],
    ], label="14. Estado civil de sus padres:")

    p_women1 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Los hombres son mejores en matemáticas que las mujeres."
                                       )
    p_women2 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Una madre que trabaja puede formar una relación tan cálida y segura con sus hijos como una madre que no trabaja."
                                       )
    p_women3 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Ambos, el hombre y la mujer, deberían contribuir al ingreso del hogar. "
                                       )
    p_women4 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="El deber de un hombre es ganar dinero, el deber de la mujer es cuidar del hogar y la familia."
                                       )
    p_women5 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Las mujeres son mejores para el trabajo doméstico que los hombres."
                                       )
    p_women6 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="El esposo debe tomar las decisiones relacionadas con la vida de la esposa."
                                       )
    p_women7 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="La cabeza del hogar debe ser el hombre."
                                       )
    p_women8 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Los hombres son mejores para manejar el dinero que las mujeres"
                                       )
    
    p_risk = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="¿Qué tan dispuesto (a) está o no está usted a tomar riesgos?"
                                       )
    p_time = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="¿Qué tan dispuesto está a renunciar a algo que es beneficioso para usted en este momento a fin de obtener mayores beneficios en el futuro?"
                                       )
    p_you = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="¿Qué tan dispuesto está a castigar a alguien que lo(a) trata injustamente, incluso cuando existan riesgos de sufrir consecuencias? "
                                       )
    p_others = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="¿Qué tan dispuesto(a) está a castigar a alguien que trata a los demás injustamente, incluso cuando exista el riesgo de sufrir consecuencias?"
                                       )
    p_altruism = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="¿Qué tan dispuesto(a) está a hacer donaciones a causas benéficas sin esperar nada a cambio?"
                                       )
    p_reciprocity = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Cuando alguien me hace un favor, estoy dispuesto a devolverlo."
                                       )
    p_inequality = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Si me tratan muy injustamente, tomaré revancha en la primera ocasión, incluso aunque deba pagar un costo por ello."
                                       )
    p_beliefs = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Supongo que la gente tiene sólo las mejores intenciones."
                                       )
    p_math = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Soy bueno(a) en matemáticas."
                                       )
    p_time2 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Tiendo a posponer las tareas, incluso cuando sé que sería mejor hacerlas de inmediato."
                                       )
    
    p_pension = models.IntegerField(
    choices=[
        [1,'Aportando en un fondo de pensiones obligatorias'],
        [2,'Aportando en un fondo de pensiones voluntarias (por ejemplo, BEPS)'],
        [3,'Ahorrando'],
        [4,'Haciendo inversiones'],
        [5,'Pagando un seguro por su cuenta'],
        [6,'Preparando a sus hijos para que puedan ayudarlo en su vejez'],
        [7,'Nada'],
    ], label="¿Qué está haciendo usted actualmente para mantenerse económicamente en su vejez?")

    p_pension2 = models.IntegerField(
    choices=[
        [1,'Aportando en un fondo de pensiones obligatorias'],
        [2,'Aportando en un fondo de pensiones voluntarias (por ejemplo, BEPS)'],
        [3,'Ahorrando'],
        [4,'Haciendo inversiones'],
        [5,'Pagando un seguro por su cuenta'],
        [6,'Preparando a los hijos para que puedan ayudarlos en su vejez'],
        [7,'Nada'],
    ], label="¿Qué están haciendo (hicieron) sus padres para mantenerse económicamente en la vejez?")
    
    A1 = models.IntegerField(
    choices=[
        [1,'Muy malo'],
        [2,'Malo'],
        [3,'Regular'],
        [4,'Bueno'],
        [5,'Excelente'],
    ], label="1. A los 65 años, ¿cómo aspira se su estado de salud?")

    A2 = models.IntegerField(
    choices=[
        [1,'Actividades laborales'],
        [2,'Jubilación ó pensión'],
        [3,'Hijos'],
        [4,'Familiares'],
        [5,'Subsidios del gobierno'],
        [6,'Ingresos de inversiones (por ejemplo, arriendos)'],
        [7,'Ahorros'],
    ], label="2. A los 65 años, ¿Cuál aspira sea su principal fuente de ingreso?")

    A3_1 = models.IntegerField(label="3.1. A los 65 años, ¿Cuál aspira que sea su ingreso mensual?")
    A3_2 = models.IntegerField(label="3.2. A los 65 años, ¿Cuántas horas a la semana aspira trabajar?")
    A3_3 = models.IntegerField(label="3.3. A los 65 años, ¿Cuánto dinero espera recibir de sus hijos al mes?")
    A3_4 = models.IntegerField(label="3.4. A los 65 años, ¿Cuántas horas de ayuda a la semana espera recibir de sus hijos?")

    A4 = models.IntegerField(
    choices=[
        [1,'Casa propia'],
        [2,'Casa en arriendo'],
        [3,'Casa de un familiar'],
        [4,'Hogar geriátrico público'],
        [5,'Hogar geriátrico privado'],
    ], label="4. A los 65 años, ¿Dónde aspira vivir?")

    A5 = models.IntegerField(
    choices=[
        [1,'Zona urbana'],
        [2,'Zona rural'],
    ], label="5. A los 65 años, ¿En qué zona aspira vivir?")

    A6 = models.IntegerField(
    choices=[
        [1,'Solo (a)'],
        [2,'Con su pareja'],
        [3,'Con alguno de sus hijos'],
        [4,'Con otro familiar'],
        [5,'Con conocidos'],
        [6,'Otro'],
    ], label="6. A los 65 años, ¿Con quién le gustaría vivir?")

    A7 = models.IntegerField(
    choices=[
        [1,'Menos del Salario Mínimo Mensual (SMMLV)'],
        [2,'Entre 1 SMMLV - $ 1.500.000'],
        [3,'Entre $ 1.500.000 - $ 2.000.000'],
        [4,'Entre $ 2.000.000 - $ 4.000.000'],
        [5,'Mayor a $ 4.000.000']
    ], label="7. ¿Cuál es el nivel educativo más alto que aspira alcancen sus hijos?")

    A8 = models.IntegerField(
    choices=[
        [1,'Ninguno'],
        [2,'Primaria'],
        [3,'Bachillerato'],
        [4,'Técnico o Tecnólogo'],
        [5,'Pregrado'],
        [6,'Posgrado (Especialización, Maestría, Doctorado)'],
    ], label="8. ¿Cuál es el rango de su ingreso mensual que aspira reciban sus hijos?")

    A9 = models.IntegerField(label="9. ¿Cuántos años le gustaría vivir?")
